"""Valida o catálogo Markdown e as cópias dos provedores com a biblioteca padrão."""

import json
from pathlib import Path
import re
import sys
import tomllib

from catalog import (CLAUDE_AGENTS, COPY_ROOTS, PLUGIN_AGENTS, catalog, copy_files,
                     local_targets, plugin_agent_files)
from model_policy import load_policy


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_FIELDS = {"name", "version", "description", "author", "homepage", "repository",
                 "license", "keywords", "skills"}
CATALOG_DOCUMENTS = ("README.md", "docs/HARNESS.md")
EXECUTABLE_COMPONENTS = ("hooks", "bin", "monitors", "commands", ".mcp.json", ".lsp.json")
TEXT_DIRECTORIES = ("skills", "agents", "docs", "scripts", ".agents", ".claude", ".claude-plugin",
                    ".codex", ".github")
TEXT_SUFFIXES = {".md", ".json", ".toml", ".py", ".yml", ".yaml", ".svg", ""}
HIDDEN = re.compile("[\u200b-\u200f\u202a-\u202e\u2060-\u2064\u2066-\u2069\ufeff"
                    "\U000e0000-\U000e007f\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
RENAME = re.compile(r"^- `([a-z0-9-]+)` passou a se chamar `([a-z0-9-]+)`\.$", re.M)
STALE_NAME_SUFFIXES = {".md", ".toml", ".yml", ".yaml", ".json", ""}
URL = re.compile(r"https?://[^\s)>\]]+")
# Trechos em que um nome antigo continua correto, por arquivo (sufixo do caminho).
STALE_NAME_EXCEPTIONS = {
    # Nomes das skills de origem no pstack, preservados na atribuição.
    "THIRD_PARTY_NOTICES.md": ("das skills `unslop` e `technical-writing`",),
    # `council` aqui é a chave de papel `roles.council`, que continua em inglês.
    "docs/MODELS.md": ("`evaluator` e `council`",),
    "delegar/SKILL.md": ("`representative` ou `council`", "`evaluator` e `council`"),
    # O comando nativo do Claude Code que motivou a mudança de nomes.
    "docs/STANDARDS.md": ("`/review`",),
}


def read(path):
    return path.read_text(encoding="utf-8")


def document(path):
    text = read(path)
    match = re.match(r"\A---\n(.*?)\n---\n\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError(f"{path}: metadados iniciais ou corpo ausentes")
    metadata = {}
    for line in match[1].splitlines():
        key, separator, value = line.partition(":")
        if not separator or not value.strip() or key in metadata:
            raise ValueError(f"{path}: metadados inválidos: {line}")
        metadata[key] = value.strip()
    if not metadata.get("name") or not metadata.get("description") or not match[2].strip():
        raise ValueError(f"{path}: name, description e corpo são obrigatórios")
    return metadata, match[2]


def validate(root=ROOT):
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    sources = catalog(root)
    require(bool(sources), "O catálogo de skills está vazio")
    for name, source in sources.items():
        metadata, _ = document(source / "SKILL.md")
        require(metadata["name"] == name, f"{source}: o nome da skill difere do diretório")
        for path in sorted(source.rglob("*.md")):
            for target, relative in local_targets(read(path)):
                inside = (path.parent / relative).resolve().is_relative_to(source.resolve())
                require(inside, f"{path.relative_to(root)}: link sai da skill; "
                                f"cite outra skill pelo nome: {target}")
    for relative in COPY_ROOTS:
        directory = root / relative
        require(set(sources) == {p.name for p in directory.iterdir() if p.is_dir()},
                f"{relative}: os diretórios divergem do catálogo agrupado")
        expected = copy_files(root, directory, sources)
        actual = {p.resolve() for p in directory.rglob("*") if p.is_file()}
        require(set(expected) == actual, f"{relative}: os arquivos de apoio divergem")
        for path in set(expected) & actual:
            require(path.read_bytes() == expected[path], f"{path}: difere da skill canônica")

    roles = root / ".agents/roles"
    role_names = {p.stem for p in roles.glob("*.md")}
    require(bool(role_names), "O catálogo de papéis está vazio")
    load_policy(root / ".agents/models.toml", required_roles=role_names)
    load_policy(root / ".agents/models.example.toml", required_roles=role_names)
    for directory, suffix in [(".claude/agents", "*.md"), (".codex/agents", "*.toml")]:
        require(role_names == {p.stem for p in (root / directory).glob(suffix)},
                f"{directory}: os nomes dos papéis diferem dos canônicos")
    for name in sorted(role_names):
        meta, body = document(roles / f"{name}.md")
        require(meta["name"] == name, f"{name}: o nome do papel difere do nome do arquivo")
        claude_meta, claude_body = document(root / f".claude/agents/{name}.md")
        require(all(claude_meta.get(key) == meta[key] for key in ("name", "description")),
                f"{name}: os metadados do papel no Claude divergem")
        require(bool(claude_meta.get("tools")), f"{name}: faltam as ferramentas do papel no Claude")
        require(body == claude_body, f"{name}: as instruções do papel no Claude divergem")
        codex = tomllib.loads(read(root / f".codex/agents/{name}.toml"))
        require(all(codex.get(key) == meta[key] for key in ("name", "description")),
                f"{name}: os metadados do papel no Codex divergem")
        require(codex.get("developer_instructions") == body,
                f"{name}: as instruções do papel no Codex divergem")

    plugin = json.loads(read(root / ".claude-plugin/plugin.json"))
    marketplace = json.loads(read(root / ".claude-plugin/marketplace.json"))
    require(set(plugin) <= PLUGIN_FIELDS,
            f"plugin.json: campos fora da lista permitida: {sorted(set(plugin) - PLUGIN_FIELDS)}")
    require(bool(re.fullmatch(r"\d+\.\d+\.\d+", str(plugin.get("version", "")))),
            "plugin.json: version deve seguir MAJOR.MINOR.PATCH")
    groups = sorted({f"./skills/{source.parent.name}/" for source in sources.values()})
    require(plugin.get("skills") == groups,
            f"plugin.json: skills deve listar os grupos do catálogo em ordem: {groups}")
    entries = marketplace.get("plugins", [])
    entry = entries[0] if len(entries) == 1 and isinstance(entries[0], dict) else {}
    require(entry.get("name") == plugin.get("name") and entry.get("source") == "./",
            "marketplace.json: a única entrada deve publicar este plugin a partir de ./")
    require("version" not in entry, "marketplace.json: a versão fica apenas em plugin.json")
    changelog = root / "CHANGELOG.md"
    version = re.escape(str(plugin.get("version", "")))
    require(changelog.is_file() and re.search(rf"^## \[{version}\]", read(changelog), re.M),
            "CHANGELOG.md: falta a seção da versão de plugin.json")
    for relative in EXECUTABLE_COMPONENTS:
        require(not (root / relative).exists(),
                f"{relative}: o plugin não distribui componentes executáveis")
    agents = plugin_agent_files(root)
    directory = root / PLUGIN_AGENTS
    actual = {p.resolve() for p in directory.iterdir()} if directory.exists() else set()
    require(set(agents) == actual and all(p.read_bytes() == agents[p] for p in actual & set(agents)),
            f"{PLUGIN_AGENTS}/: difere de {CLAUDE_AGENTS}; execute python scripts/sync.py")

    for path in sorted(root.glob("*.json")) + [root / ".claude/settings.json"]:
        json.loads(read(path))
    text_files = [p for p in root.iterdir() if p.is_file()]
    for relative in TEXT_DIRECTORIES:
        text_files.extend(p for p in (root / relative).rglob("*") if p.is_file())
    for path in sorted(text_files):
        if path.suffix.lower() in TEXT_SUFFIXES:
            character = HIDDEN.search(read(path))
            require(character is None, f"{path.relative_to(root)}: caractere invisível ou de "
                                       f"controle U+{ord(character[0]):04X}" if character else "")
    markdown = sorted(root.glob("*.md"))
    for directory in ("docs", "skills", ".agents", ".claude", ".github"):
        markdown.extend(sorted((root / directory).rglob("*.md")))
    for path in markdown:
        for target, relative in local_targets(read(path)):
            destination = path.parent / relative
            require(destination.exists(), f"{path.relative_to(root)}: link quebrado: {target}")
    for relative in CATALOG_DOCUMENTS:
        listed = re.findall(r"^\| `([a-z0-9-]+)` \|", read(root / relative), re.M)
        missing, extra = sorted(set(sources) - set(listed)), sorted(set(listed) - set(sources))
        require(not missing and not extra and len(listed) == len(set(listed)),
                f"{relative}: o catálogo difere das skills; faltam {missing}, sobram {extra}")
    errors.extend(stale_names(root, sources))
    return errors, len(sources), len(role_names)


def stale_names(root, sources):
    """Recusa nomes de skills renomeadas, lidos do CHANGELOG, citados como skill."""
    changelog = root / "CHANGELOG.md"
    renames = dict(RENAME.findall(read(changelog))) if changelog.is_file() else {}
    if not renames:
        return ["CHANGELOG.md: nenhuma renomeação no formato "
                "\"- `antigo` passou a se chamar `novo`.\"; a verificação de nomes antigos depende dela"]
    errors = []
    current = {}
    for old in renames:
        seen, name = {old}, renames[old]
        while name in renames and name not in seen:
            seen.add(name)
            name = renames[name]
        if old in sources:
            errors.append(f"CHANGELOG.md: `{old}` foi renomeada, mas ainda está no catálogo")
        elif name in seen or name not in sources:
            errors.append(f"CHANGELOG.md: a renomeação de `{old}` não termina numa skill do catálogo")
        else:
            current[old] = name
    if not current:
        return errors
    names = "|".join(re.escape(n) for n in sorted(current, key=len, reverse=True))
    end = r"(?![\w-])"
    patterns = (
        re.compile(rf"`({names})`"),
        re.compile(rf"\$({names}){end}"),
        re.compile(rf"(?<=[/:])({names}){end}"),
        re.compile(rf"^\s*(?:name|placeholder):\s*({names})\s*$", re.M),
        re.compile(rf"(?<![\w-])(?:[Uu]se|siga|seguindo|menciona|pedir|skills?)\s+({names}){end}"),
        re.compile(rf"^description:.*?(?<![\w-])({names}){end}", re.M),
    )
    files = [p for p in root.iterdir() if p.is_file() and p.name != "CHANGELOG.md"]
    for relative in TEXT_DIRECTORIES:
        if relative != "scripts":
            files.extend(p for p in (root / relative).rglob("*") if p.is_file())
    used = set()
    for path in sorted(files):
        if path.suffix.lower() not in STALE_NAME_SUFFIXES:
            continue
        relative = path.relative_to(root).as_posix()
        text = URL.sub(lambda m: " " * len(m[0]), read(path))
        for suffix, excerpts in STALE_NAME_EXCEPTIONS.items():
            if relative == suffix or relative.endswith("/" + suffix):
                for excerpt in excerpts:
                    if excerpt in text:
                        used.add((suffix, excerpt))
                        text = text.replace(excerpt, " " * len(excerpt))
        found = set()
        for pattern in patterns:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start(1)) + 1
                found.add((line, match[1]))
        for line, old in sorted(found):
            errors.append(f"{relative}:{line}: nome antigo `{old}`; use `{current[old]}`")
    for suffix, excerpts in STALE_NAME_EXCEPTIONS.items():
        for excerpt in excerpts:
            if (suffix, excerpt) not in used:
                errors.append(f"{suffix}: exceção de nome antigo sem uso: {excerpt}")
    return errors


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    try:
        errors, skills, roles = validate()
    except (OSError, ValueError) as error:
        print(f"FALHA: {error}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"FALHA: {error}", file=sys.stderr)
        return 1
    print(f"OK: {skills} skills, {roles} papéis; cópias dos provedores, metadados e links locais")
    return 0


if __name__ == "__main__":
    sys.exit(main())
