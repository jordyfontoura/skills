"""Prova empacotamento seletivo e integridade com uma biblioteca e skills mínimas."""

from pathlib import Path
import shutil
import tempfile
import unittest

from catalog import (catalog, copy_files, knowledge_catalog, knowledge_dependencies,
                     local_targets)
from check import ROOT


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

    def test_bundle_is_selective_transitive_and_independent_for_each_consumer(self):
        copy_root = self.root / "export"
        output = copy_files(self.root, copy_root)
        for name in ("avaliar", "criar"):
            skill = copy_root / name
            main = output[(skill / "SKILL.md").resolve()].decode("utf-8")
            self.assertIn("[ui]: references/knowledge/ux/ui.md?view=1#layout", main)
            self.assertIn("[Exemplo](../../../knowledge/not-installed.md)", main)
            self.assertIn((skill / "references/knowledge/accessibility/keyboard.md").resolve(), output)
            self.assertNotIn((skill / "references/knowledge/games/other.md").resolve(), output)
            self.assertIn("Gerado de knowledge/ux/ui.md", output[
                (skill / "references/knowledge/ux/ui.md").resolve()].decode("utf-8"))

    def test_single_skill_copy_survives_relocation_without_source_or_other_skills(self):
        skill = catalog(self.root)["avaliar"]
        output = copy_files(self.root, self.root / "export", {"avaliar": skill})
        for path, content in output.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        installed = self.root / "installed/avaliar"
        installed.parent.mkdir()
        shutil.move(str(self.root / "export/avaliar"), installed)
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
            copy_files(self.root, self.root / "export")

    def test_non_markdown_files_are_rejected(self):
        self.write("knowledge/tool.py", "print('not documentation')\n")
        with self.assertRaisesRegex(ValueError, "somente referências Markdown"):
            knowledge_catalog(self.root)

    def test_library_change_updates_each_bundle_without_editing_consumers(self):
        sources = catalog(self.root)
        before = {name: (skill / "SKILL.md").read_bytes() for name, skill in sources.items()}
        self.write("knowledge/accessibility/keyboard.md", "# Teclado\nCritério atualizado.\n")
        output = copy_files(self.root, self.root / "export")
        for name, source in sources.items():
            bundled = (self.root / "export" / name /
                       "references/knowledge/accessibility/keyboard.md").resolve()
            self.assertIn("Critério atualizado.", output[bundled].decode("utf-8"))
            self.assertEqual((source / "SKILL.md").read_bytes(), before[name])

    def test_real_ui_consumers_have_relocatable_links(self):
        # Check the actual distribution, including its own support files, outside its layout.
        sources = catalog(ROOT)
        consumers = {name: sources[name] for name in ("criticar", "implementar", "prototipar")}
        for name, source in consumers.items():
            self.assertEqual(len(knowledge_dependencies(ROOT, source)), 4)
        output = copy_files(ROOT, self.root / "real-export", consumers)
        for path, content in output.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        for name in consumers:
            installed = self.root / "real-export" / name
            for path in installed.rglob("*.md"):
                for _, relative in local_targets(path.read_text(encoding="utf-8")):
                    target = (path.parent / relative).resolve()
                    self.assertTrue(target.is_relative_to(installed.resolve()), (path, target))
                    self.assertTrue(target.is_file(), (path, target))

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
