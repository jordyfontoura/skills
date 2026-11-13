"""Lê as fontes agrupadas e prepara cópias para os diretórios dos provedores."""

import os
from pathlib import Path
import re
from urllib.parse import quote, unquote, urlsplit, urlunsplit


COPY_ROOTS = (".agents/skills", ".claude/skills")
CLAUDE_AGENTS = ".claude/agents"
PLUGIN_AGENTS = "agents"
LINK = re.compile(r"(!?\[[^\]\n]*\]\()([^)\n]+)(\))")
REFERENCE = re.compile(r"^ {0,3}\[[^\]\n]+\]:[ \t]*(\S+)", re.M)


def catalog(root):
    sources = {}
    for group in sorted((root / "skills").iterdir()):
        if not group.is_dir():
            continue
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", group.name):
            raise ValueError(f"{group}: nome de grupo inválido")
        for source in sorted(group.iterdir()):
            if not source.is_dir():
                continue
            if not (source / "SKILL.md").is_file():
                raise ValueError(f"{source}: SKILL.md ausente")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", source.name):
                raise ValueError(f"{source}: nome de skill inválido")
            if source.name in sources:
                raise ValueError(f"Skill duplicada em grupos diferentes: {source.name}")
            sources[source.name] = source
    return sources


def lines_outside_code(text):
    """Gera cada linha com a indicação de estar fora de blocos de código cercados."""
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not marker[2].strip():
                fence = None
            yield line, False
        else:
            yield line, fence is None


def rewrite_links(text, transform):
    output = []
    for line, prose in lines_outside_code(text):
        if prose:
            line = LINK.sub(lambda m: m[1] + transform(m[2]) + m[3], line)
            reference = REFERENCE.match(line)
            if reference:
                start, end = reference.span(1)
                line = line[:start] + transform(reference[1]) + line[end:]
        output.append(line)
    return "".join(output)


def local_targets(text):
    """Retorna os links relativos fora de blocos de código, com o caminho decodificado."""
    targets = []
    for line, prose in lines_outside_code(text):
        if not prose:
            continue
        candidates = [m[2] for m in LINK.finditer(line)]
        reference = REFERENCE.match(line)
        if reference:
            candidates.append(reference[1])
        for target in candidates:
            angled = target.startswith("<") and target.endswith(">")
            url = urlsplit(target[1:-1] if angled else target)
            if not (url.scheme or url.netloc or not url.path or url.path.startswith("/")):
                targets.append((target, unquote(url.path)))
    return targets


def rebase_links(text, source_file, target_file, file_map):
    def transform(target):
        angled = target.startswith("<") and target.endswith(">")
        url = urlsplit(target[1:-1] if angled else target)
        if url.scheme or url.netloc or not url.path or url.path.startswith("/"):
            return target
        resolved = (source_file.parent / unquote(url.path)).resolve()
        mapped = file_map.get(resolved, resolved)
        relative = Path(os.path.relpath(mapped, target_file.parent)).as_posix()
        value = urlunsplit(("", "", quote(relative, safe="/:-._~"), url.query, url.fragment))
        return f"<{value}>" if angled else value

    return rewrite_links(text, transform)


def knowledge_catalog(root):
    """Confere o índice e mantém a biblioteca restrita a referências Markdown locais."""
    directory = (root / "knowledge").resolve()
    if not directory.exists():
        return set()
    if (root / "knowledge").is_symlink():
        raise ValueError("knowledge/: a biblioteca não pode ser um link simbólico")
    files = set()
    for path in directory.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"{path}: referência não pode ser um link simbólico")
        if path.is_file():
            if path.suffix != ".md":
                raise ValueError(f"{path}: a biblioteca aceita somente referências Markdown")
            files.add(path.resolve())
    index = directory / "README.md"
    if index not in files:
        raise ValueError("knowledge/README.md: índice ausente")
    indexed = {(index.parent / relative).resolve()
               for _, relative in local_targets(index.read_text(encoding="utf-8"))}
    if indexed != files - {index}:
        raise ValueError("knowledge/README.md: o índice diverge dos arquivos da biblioteca")
    for path in files:
        for target, relative in local_targets(path.read_text(encoding="utf-8")):
            if (path.parent / relative).resolve() not in files:
                raise ValueError(f"{path}: link fora da biblioteca ou ausente: {target}")
    return files


def knowledge_dependencies(root, source, library=None):
    """Segue apenas links declarados, inclusive dependências transitivas, sem carregar tudo."""
    library = knowledge_catalog(root) if library is None else library
    directory = (root / "knowledge").resolve()
    pending = list(source.rglob("*.md"))
    dependencies = set()
    while pending:
        path = pending.pop()
        for target, relative in local_targets(path.read_text(encoding="utf-8")):
            resolved = (path.parent / relative).resolve()
            if resolved.is_relative_to(directory):
                if resolved not in library:
                    raise ValueError(f"{path}: referência de conhecimento ausente: {target}")
                if resolved not in dependencies:
                    dependencies.add(resolved)
                    pending.append(resolved)
    return dependencies


def copy_files(root, copy_root, sources=None, knowledge_root=None):
    """Gera cópias autocontidas ou com biblioteca compartilhada no destino informado."""
    sources = catalog(root) if sources is None else sources
    library = knowledge_catalog(root)
    paths = {}
    for name, source in sources.items():
        for path in source.rglob("*"):
            if path.is_file():
                paths[path.resolve()] = (copy_root / name / path.relative_to(source)).resolve()
    output = {}
    for name, skill in sources.items():
        destination = knowledge_root if knowledge_root is not None else copy_root / name / "references/knowledge"
        bundled = {path: (destination /
                          path.relative_to((root / "knowledge").resolve())).resolve()
                   for path in knowledge_dependencies(root, skill, library)}
        if set(bundled.values()) & set(paths.values()):
            raise ValueError(f"{skill}: references/knowledge é reservado às cópias geradas")
        mapping = {**paths, **bundled}
        owned = {path: target for path, target in paths.items()
                 if path.is_relative_to(skill.resolve())}
        for source, target in {**owned, **bundled}.items():
            if source.suffix.lower() == ".md":
                text = rebase_links(source.read_text(encoding="utf-8"), source, target, mapping)
                if source in bundled:
                    origin = source.relative_to(root.resolve()).as_posix()
                    text = f"<!-- Gerado de {origin}; edite a fonte no harness. -->\n\n" + text
                output[target] = text.encode("utf-8")
            else:
                output[target] = source.read_bytes()
    return output


def plugin_agent_files(root):
    """Copia os papéis adaptados ao Claude para a pasta `agents/` lida pelo plugin."""
    target = (root / PLUGIN_AGENTS).resolve()
    return {target / path.name: path.read_bytes()
            for path in sorted((root / CLAUDE_AGENTS).glob("*.md"))}
