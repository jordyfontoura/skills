"""Atualiza as cópias das skills e dos papéis do plugin; as fontes não são alteradas."""

from pathlib import Path
import sys

from catalog import CLAUDE_AGENTS, COPY_ROOTS, PLUGIN_AGENTS, copy_files, plugin_agent_files


ROOT = Path(__file__).resolve().parents[1]


def sync(root=ROOT):
    planned = {}
    for relative in COPY_ROOTS:
        directory = root / relative
        expected = copy_files(root, directory)
        actual = {p.resolve() for p in directory.rglob("*") if p.is_file()}
        extra = actual - set(expected)
        expected_names = {p.relative_to(directory.resolve()).parts[0] for p in expected}
        extra_directories = ({p.resolve() for p in directory.iterdir()
                              if p.is_dir() and p.name not in expected_names}
                             if directory.exists() else set())
        if extra or extra_directories:
            paths = ", ".join(str(p.relative_to(root.resolve()))
                              for p in sorted(extra | extra_directories))
            raise ValueError(f"Cópias fora do catálogo; confira antes de remover: {paths}")
        planned.update(expected)
    agents = plugin_agent_files(root)
    directory = root / PLUGIN_AGENTS
    extra = ({p.resolve() for p in directory.iterdir()} - set(agents)
             if directory.exists() else set())
    if extra:
        paths = ", ".join(str(p.relative_to(root.resolve())) for p in sorted(extra))
        raise ValueError(f"Papéis do plugin fora de {CLAUDE_AGENTS}; confira antes de remover: {paths}")
    planned.update(agents)
    changed = 0
    for target, content in planned.items():
        if not target.exists() or target.read_bytes() != content:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
            changed += 1
    return changed


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    try:
        changed = sync()
    except (OSError, ValueError) as error:
        print(f"FALHA: {error}", file=sys.stderr)
        return 1
    print(f"OK: {changed} arquivos de cópia atualizados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
