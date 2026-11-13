"""Prepara conteúdo autocontido para o CLI; Python só é necessário na origem."""

import hashlib
import json
from pathlib import Path
import subprocess
import tomllib

from catalog import catalog, copy_files, knowledge_catalog, knowledge_dependencies


ROOT = Path(__file__).resolve().parents[1]


def main():
    root = ROOT
    package = root / "cli"
    plugin = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    metadata = json.loads((package / "package.json").read_text(encoding="utf-8"))
    if metadata["version"] != plugin["version"]:
        raise ValueError("Versão do CLI deve acompanhar .claude-plugin/plugin.json")
    copies = copy_files(root, root / ".agents/skills", knowledge_root=root / "knowledge/harness")
    files = {path.relative_to(root).as_posix(): content.decode("utf-8")
             for path, content in copies.items()}
    for directory, pattern in ((".claude/agents", "*.md"), (".codex/agents", "*.toml")):
        for path in sorted((root / directory).glob(pattern)):
            if path.is_file():
                files[path.relative_to(root).as_posix()] = path.read_text(encoding="utf-8")
    files[".agents/models.toml"] = (root / ".agents/models.example.toml").read_text(encoding="utf-8")
    skills = []
    sources = catalog(root)
    library = knowledge_catalog(root)
    for name, source in sorted(sources.items()):
        text = (source / "SKILL.md").read_text(encoding="utf-8")
        description = next(line.removeprefix("description: ") for line in text.splitlines()
                           if line.startswith("description: "))
        skills.append({"name": name, "group": source.parent.name, "description": description,
                       "knowledge": sorted("knowledge/harness/" + path.relative_to(root / "knowledge").as_posix()
                                           for path in knowledge_dependencies(root, source, library)),
                       "related": sorted(other for other in sources
                                         if other != name and f"`{other}`" in text)})
    knowledge = []
    for path in sorted(library):
        target = "knowledge/harness/" + path.relative_to(root / "knowledge").as_posix()
        title = next(line.removeprefix("# ") for line in path.read_text(encoding="utf-8").splitlines()
                     if line.startswith("# "))
        knowledge.append({"path": target, "title": title,
                          "skills": [skill["name"] for skill in skills if target in skill["knowledge"]]})
    # O SHA é da base; o hash do conteúdo identifica também builds locais ainda não commitados.
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=root, text=True))
    digest = hashlib.sha256(json.dumps(files, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    payload = {"schemaVersion": 2,
               "source": {"repository": "https://github.com/jordyfontoura/skills", "sha": sha,
                          "version": plugin["version"], "dirty": dirty, "contentHash": digest},
               "skills": skills, "knowledge": knowledge,
               "roles": ["planner", "evaluator", "representative"], "files": files,
               "modelTemplate": tomllib.loads(files[".agents/models.toml"])}
    (package / "payload.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (package / "LICENSE").write_bytes((root / "LICENSE").read_bytes())
    print(f"OK: pacote com {len(skills)} skills, 3 papéis e {len(files)} arquivos")


if __name__ == "__main__":
    main()
