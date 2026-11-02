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
    return "".join(LINK.sub(lambda m: m[1] + transform(m[2]) + m[3], line) if prose else line
                   for line, prose in lines_outside_code(text))


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


def copy_files(root, copy_root, sources=None):
    sources = catalog(root) if sources is None else sources
    paths = {}
    for name, source in sources.items():
        for path in source.rglob("*"):
            if path.is_file():
                paths[path.resolve()] = (copy_root / name / path.relative_to(source)).resolve()
    output = {}
    for source, target in paths.items():
        if source.suffix.lower() == ".md":
            text = rebase_links(source.read_text(encoding="utf-8"), source, target, paths)
            output[target] = text.encode("utf-8")
        else:
            output[target] = source.read_bytes()
    return output


def plugin_agent_files(root):
    """Copia os papéis adaptados ao Claude para a pasta `agents/` lida pelo plugin."""
    target = (root / PLUGIN_AGENTS).resolve()
    return {target / path.name: path.read_bytes()
            for path in sorted((root / CLAUDE_AGENTS).glob("*.md"))}
