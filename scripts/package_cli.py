"""Prepara conteúdo autocontido para o CLI; Python só é necessário na origem."""

import hashlib
import json
from pathlib import Path
import subprocess

from catalog import catalog, copy_files


ROOT = Path(__file__).resolve().parents[1]


def main():
    root = ROOT
    package = root / "cli"
    plugin = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    metadata = json.loads((package / "package.json").read_text(encoding="utf-8"))
    if metadata["version"] != plugin["version"]:
        raise ValueError("Versão do CLI deve acompanhar .claude-plugin/plugin.json")
    copies = copy_files(root, root / ".agents/skills")
    files = {path.relative_to(root).as_posix(): content.decode("utf-8")
             for path, content in copies.items()}
    for directory, pattern in ((".claude/agents", "*.md"), (".codex/agents", "*.toml")):
        for path in sorted((root / directory).glob(pattern)):
            if path.is_file():
                files[path.relative_to(root).as_posix()] = path.read_text(encoding="utf-8")
    files[".agents/models.toml"] = (root / ".agents/models.example.toml").read_text(encoding="utf-8")
    skills = []
    sources = catalog(root)
    for name, source in sorted(sources.items()):
        text = (source / "SKILL.md").read_text(encoding="utf-8")
        description = next(line.removeprefix("description: ") for line in text.splitlines()
                           if line.startswith("description: "))
        skills.append({"name": name, "group": source.parent.name, "description": description,
                       "related": sorted(other for other in sources
                                         if other != name and f"`{other}`" in text)})
    # O SHA é da base; o hash do conteúdo identifica também builds locais ainda não commitados.
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=root, text=True))
    digest = hashlib.sha256(json.dumps(files, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    payload = {"schemaVersion": 1,
               "source": {"repository": "https://github.com/jordyfontoura/skills", "sha": sha,
                          "version": plugin["version"], "dirty": dirty, "contentHash": digest},
               "skills": skills, "roles": ["planner", "evaluator", "representative"], "files": files}
    (package / "payload.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (package / "LICENSE").write_bytes((root / "LICENSE").read_bytes())
    print(f"OK: pacote com {len(skills)} skills, 3 papéis e {len(files)} arquivos")


if __name__ == "__main__":
    main()
