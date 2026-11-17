"""Prova empacotamento seletivo e integridade com uma biblioteca e skills mínimas."""

from pathlib import Path
import shutil
import tempfile
import unittest

from catalog import (catalog, copy_files, knowledge_catalog, knowledge_dependencies,
                     local_targets)
from check import ROOT
from sync import sync


class KnowledgeTests(unittest.TestCase):
    def setUp(self):
        workspace = tempfile.TemporaryDirectory(dir=ROOT / "scripts")
        self.addCleanup(workspace.cleanup)
        self.root = Path(workspace.name)
        self.write("knowledge/README.md", "[UI](ux/ui.md)\n[Teclado](accessibility/keyboard.md)\n"
                   "[Outro](games/other.md)\n")
        self.write("knowledge/ux/ui.md", "# UI\n[Teclado](../accessibility/keyboard.md#focus)\n")
        self.write("knowledge/accessibility/keyboard.md", "# Teclado\n[UI](../ux/ui.md)\n")
        self.write("knowledge/games/other.md", "# Outro domínio\n")
        for name in ("avaliar", "criar"):
            self.write(f"skills/development/{name}/SKILL.md",
                       f"---\nname: {name}\ndescription: Uma tarefa.\n---\n\n"
                       "Leia [UI][ui].\n\n[ui]: ../../../knowledge/ux/ui.md?view=1#layout\n"
                       "```md\n[Exemplo](../../../knowledge/not-installed.md)\n```\n")

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_default_copies_link_to_root_without_duplicating_guides(self):
        copy_root = self.root / "export"
        output = copy_files(self.root, copy_root)
        for name in ("avaliar", "criar"):
            skill = copy_root / name
            main = output[(skill / "SKILL.md").resolve()].decode("utf-8")
            self.assertIn("[ui]: ../../knowledge/ux/ui.md?view=1#layout", main)
            self.assertIn("[Exemplo](../../../knowledge/not-installed.md)", main)
        self.assertTrue(all(path.name == "SKILL.md" for path in output))

    def test_single_skill_and_root_library_survive_project_relocation(self):
        skill = catalog(self.root)["avaliar"]
        project = self.root / "export"
        output = copy_files(self.root, project / ".agents/skills", {"avaliar": skill},
                            knowledge_root=project / "knowledge")
        for path, content in output.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        installed = self.root / "installed"
        shutil.move(str(project), installed)
        # Remove the source files so no dependency can accidentally resolve against them.
        for relative in ("skills", "knowledge"):
            directory = (self.root / relative).resolve()
            self.assertTrue(directory.is_relative_to(self.root.resolve()))
            self.assertTrue(self.root.resolve().is_relative_to((ROOT / "scripts").resolve()))
            shutil.rmtree(directory)
        for path in installed.rglob("*.md"):
            for _, relative in local_targets(path.read_text(encoding="utf-8")):
                target = (path.parent / relative).resolve()
                self.assertTrue(target.is_relative_to(installed.resolve()), (path, target))
                self.assertTrue(target.is_file(), (path, target))

    def test_library_requires_complete_index(self):
        self.write("knowledge/unlisted.md", "Não listado.\n")
        with self.assertRaisesRegex(ValueError, "índice diverge"):
            knowledge_catalog(self.root)

    def test_missing_dependency_is_rejected(self):
        self.write("skills/development/avaliar/SKILL.md", "[Guia](../../../knowledge/missing.md)\n")
        with self.assertRaisesRegex(ValueError, "referência de conhecimento ausente"):
            copy_files(self.root, self.root / "export")

    def test_library_cannot_link_back_to_skills_or_outside_repository(self):
        for target in ("../../skills/development/avaliar/SKILL.md", "../../../outside.md"):
            with self.subTest(target=target):
                self.write("knowledge/ux/ui.md", f"[Fora]({target})\n")
                with self.assertRaisesRegex(ValueError, "link fora da biblioteca ou ausente"):
                    knowledge_catalog(self.root)

    def test_index_cannot_whitelist_files_outside_library(self):
        with (self.root / "knowledge/README.md").open("a", encoding="utf-8") as stream:
            stream.write("[Fora](../skills/development/avaliar/SKILL.md)\n")
        with self.assertRaisesRegex(ValueError, "índice diverge"):
            knowledge_catalog(self.root)

    def test_generated_resource_cannot_overwrite_authored_file(self):
        self.write("skills/development/avaliar/references/knowledge/ux/ui.md", "Adaptação.\n")
        with self.assertRaisesRegex(ValueError, "reservado às cópias geradas"):
            copy_files(self.root, self.root / "export", knowledge_root=(
                self.root / "export/avaliar/references/knowledge"))

    def test_non_markdown_files_are_rejected(self):
        self.write("knowledge/tool.py", "print('not documentation')\n")
        with self.assertRaisesRegex(ValueError, "somente referências Markdown"):
            knowledge_catalog(self.root)

    def test_library_change_never_rewrites_sources_or_generates_duplicates(self):
        sources = catalog(self.root)
        before = {name: (skill / "SKILL.md").read_bytes() for name, skill in sources.items()}
        self.write("knowledge/accessibility/keyboard.md", "# Teclado\nCritério atualizado.\n")
        output = copy_files(self.root, self.root / "export")
        for name, source in sources.items():
            self.assertEqual((source / "SKILL.md").read_bytes(), before[name])
        self.assertTrue(all(path.name == "SKILL.md" for path in output))
        self.assertIn("Critério atualizado.", (self.root / "knowledge/accessibility/keyboard.md").read_text(encoding="utf-8"))

    def test_real_ui_consumers_have_relocatable_links(self):
        # Check the actual distribution, including its own support files, outside its layout.
        sources = catalog(ROOT)
        consumers = {name: sources[name] for name in ("criticar", "implementar", "prototipar")}
        for name, source in consumers.items():
            expected = {"ux/usability.md", "ux/states-and-content.md",
                        "ux/visual-direction.md", "ux/motion.md",
                        "ux/platform-conventions.md", "accessibility/interface-criteria.md"}
            if name == "criticar":
                expected.update({"gamedev/game-design.md", "3d-modeling/game-ready-assets.md",
                                 "3d-modeling/export-pipeline.md", "gamedev/asset-sources.md"})
            actual = {path.relative_to(ROOT / "knowledge").as_posix()
                      for path in knowledge_dependencies(ROOT, source)}
            self.assertEqual(actual, expected)
        project = self.root / "real-export"
        output = copy_files(ROOT, project / ".agents/skills", consumers,
                            knowledge_root=project / "knowledge")
        for path, content in output.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        for name in consumers:
            installed = project / ".agents/skills" / name
            for path in installed.rglob("*.md"):
                for _, relative in local_targets(path.read_text(encoding="utf-8")):
                    target = (path.parent / relative).resolve()
                    self.assertTrue(target.is_relative_to(project.resolve()), (path, target))
                    self.assertTrue(target.is_file(), (path, target))

    def install_legacy_copies(self):
        for provider in (".agents/skills", ".claude/skills"):
            for name, source in catalog(self.root).items():
                directory = self.root / provider
                output = copy_files(self.root, directory, {name: source},
                                    knowledge_root=directory / name / "references/knowledge")
                for path, content in output.items():
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(content)

    def test_sync_migrates_identical_legacy_guides_and_is_idempotent(self):
        self.install_legacy_copies()
        before = {path: path.read_bytes() for path in knowledge_catalog(self.root)}
        self.assertGreater(sync(self.root), 0)
        for provider in (".agents/skills", ".claude/skills"):
            directory = self.root / provider
            self.assertFalse(list(directory.rglob("references/knowledge")))
            for path in directory.rglob("*.md"):
                for _, relative in local_targets(path.read_text(encoding="utf-8")):
                    self.assertTrue((path.parent / relative).resolve().is_file())
        self.assertEqual(before, {path: path.read_bytes() for path in before})
        self.assertEqual(sync(self.root), 0)

    def test_sync_preserves_modified_or_unknown_legacy_guides_before_any_write(self):
        self.install_legacy_copies()
        for relative in ("ux/ui.md", "custom.md"):
            with self.subTest(relative=relative):
                target = self.root / ".claude/skills/criar/references/knowledge" / relative
                original = target.read_bytes() if target.exists() else None
                self.write(str(target.relative_to(self.root)), "Adaptação local.\n")
                before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
                with self.assertRaisesRegex(ValueError, "Cópias fora do catálogo"):
                    sync(self.root)
                self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})
                if original is not None:
                    target.write_bytes(original)

    def test_full_plugin_sources_resolve_after_relocation(self):
        plugin = self.root / "plugin-cache/arbitrary-version"
        shutil.copytree(ROOT / "knowledge", plugin / "knowledge")
        for name in ("criticar", "implementar", "prototipar"):
            source = ROOT / "skills/development" / name
            shutil.copytree(source, plugin / "skills/development" / name)
        for path in plugin.rglob("*.md"):
            for _, relative in local_targets(path.read_text(encoding="utf-8")):
                target = (path.parent / relative).resolve()
                self.assertTrue(target.is_relative_to(plugin.resolve()), (path, target))
                self.assertTrue(target.is_file(), (path, target))


if __name__ == "__main__":
    unittest.main()
