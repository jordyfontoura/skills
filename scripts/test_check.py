"""Testa falhas de validação que precisam impedir o aceite."""

import json
from pathlib import Path
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

from check import ROOT, validate
from catalog import catalog, copy_files, rebase_links
from sync import sync


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory(dir=ROOT / "scripts")
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        for directory in (".agents", ".claude", ".claude-plugin", ".codex", "agents", "docs", "skills"):
            shutil.copytree(ROOT / directory, self.root / directory)
        for path in ROOT.iterdir():
            if path.is_file():
                shutil.copy2(path, self.root / path.name)
        (self.root / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/model_policy.py", self.root / "scripts/model_policy.py")

    def test_current_catalog_passes(self):
        errors, skills, roles = validate(self.root)
        self.assertEqual(errors, [])
        self.assertGreater(skills, 0)
        self.assertGreater(roles, 0)

    def test_skill_copy_drift_is_rejected(self):
        target = self.root / ".claude/skills/implementar/testing.md"
        target.write_text("Instruções desatualizadas\n", encoding="utf-8")
        errors, _, _ = validate(self.root)
        self.assertTrue(any("difere da skill canônica" in error for error in errors))

    def test_role_instruction_drift_is_rejected(self):
        target = self.root / ".codex/agents/planner.toml"
        target.write_text(target.read_text(encoding="utf-8").replace(
            "# Planejar o trabalho", "# Planejamento desatualizado"), encoding="utf-8")
        errors, _, _ = validate(self.root)
        self.assertTrue(any("as instruções do papel no Codex divergem" in error for error in errors))

    def test_broken_local_link_is_rejected(self):
        (self.root / "README.md").write_text("[Guia](missing.md)\n", encoding="utf-8")
        errors, _, _ = validate(self.root)
        self.assertTrue(any("link quebrado: missing.md" in error for error in errors))

    def test_invalid_metadata_is_rejected(self):
        target = self.root / "skills/development/implementar/SKILL.md"
        target.write_text("# Metadados ausentes\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "metadados iniciais"):
            validate(self.root)

    def test_invalid_configuration_is_rejected(self):
        (self.root / ".claude/settings.json").write_text("{invalid", encoding="utf-8")
        with self.assertRaises(ValueError):
            validate(self.root)

    def test_cli_preserves_portuguese_with_legacy_output_encoding(self):
        script = self.root / "scripts/check.py"
        script.parent.mkdir(exist_ok=True)
        shutil.copy2(ROOT / "scripts/check.py", script)
        shutil.copy2(ROOT / "scripts/catalog.py", script.parent / "catalog.py")
        shutil.copy2(ROOT / "scripts/model_policy.py", script.parent / "model_policy.py")
        result = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            env={**os.environ, "PYTHONIOENCODING": "cp1252"},
            check=True,
        )
        output = result.stdout.decode("utf-8")
        self.assertIn("papéis", output)
        self.assertIn("cópias dos provedores", output)

    def test_duplicate_names_across_groups_are_rejected(self):
        target = self.root / "skills/another/escrever-claro"
        target.parent.mkdir()
        shutil.copytree(self.root / "skills/productivity/escrever-claro", target)
        with self.assertRaisesRegex(ValueError, "Skill duplicada"):
            validate(self.root)

    def test_moving_group_keeps_native_command_names(self):
        group = self.root / "skills/writing"
        group.mkdir()
        shutil.move(str(self.root / "skills/productivity/escrever-claro"), str(group / "escrever-claro"))
        errors, _, _ = validate(self.root)
        self.assertTrue(any("plugin.json: skills deve listar os grupos" in e for e in errors))
        manifest = self.root / ".claude-plugin/plugin.json"
        data = json.loads(manifest.read_text(encoding="utf-8"))
        data["skills"] = sorted([*data["skills"], "./skills/writing/"])
        manifest.write_text(json.dumps(data), encoding="utf-8")
        errors, count, _ = validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(count, len(catalog(ROOT)))
        self.assertTrue((self.root / ".agents/skills/escrever-claro/SKILL.md").is_file())

    def append_to_implement(self, text):
        source = self.root / "skills/development/implementar/SKILL.md"
        source.write_text(source.read_text(encoding="utf-8") + text, encoding="utf-8")
        return source

    def test_cross_group_links_are_rebased_in_copies_and_rejected_in_sources(self):
        self.append_to_implement("\nLeia [cargas](../../productivity/delegar/workloads.md).\n")
        exported = copy_files(self.root, self.root / ".agents/skills")
        target = (self.root / ".agents/skills/implementar/SKILL.md").resolve()
        self.assertIn("(../delegar/workloads.md)", exported[target].decode("utf-8"))
        errors, _, _ = validate(self.root)
        self.assertTrue(any("link sai da skill" in error and "workloads.md" in error
                            for error in errors))

    def test_links_leaving_the_skill_are_rejected(self):
        for link in ("../implementar/testing.md", "../../../docs/GLOSSARY.md"):
            with self.subTest(link=link):
                source = self.root / "skills/development/especificar/SKILL.md"
                original = source.read_text(encoding="utf-8")
                source.write_text(original + f"\n[Apoio]({link})\n", encoding="utf-8")
                errors, _, _ = validate(self.root)
                source.write_text(original, encoding="utf-8")
                self.assertTrue(any(f"link sai da skill; cite outra skill pelo nome: {link}"
                                    in error for error in errors))

    def test_reference_links_leaving_the_skill_are_rejected(self):
        self.append_to_implement("\nVeja [cargas].\n\n[cargas]: ../delegar/workloads.md\n")
        errors, _, _ = validate(self.root)
        self.assertTrue(any("link sai da skill" in error for error in errors))

    def test_links_inside_the_skill_and_in_code_are_accepted(self):
        self.append_to_implement("\nLeia [testes](testing.md#prova).\n\n"
                                 "~~~markdown\n[Exemplo](../delegar/workloads.md)\n"
                                 "[ref]: ../../../docs/GLOSSARY.md\n~~~\n")
        self.assertEqual(sync(self.root), 2)
        self.assertEqual(validate(self.root)[0], [])

    def test_rebasing_preserves_anchors_external_links_and_code(self):
        source = self.root / "skills/development/implementar/SKILL.md"
        target = self.root / ".agents/skills/implementar/SKILL.md"
        linked = self.root / "skills/productivity/delegar/workloads.md"
        mapping = {linked.resolve(): (self.root / ".agents/skills/delegar/workloads.md").resolve()}
        text = ("[Guia](../../productivity/delegar/workloads.md?view=1#prova)\n"
                "[Site](https://example.com/guide#prova)\n"
                "```markdown\n[Exemplo](../../productivity/delegar/workloads.md)\n```\n")
        actual = rebase_links(text, source, target, mapping)
        self.assertIn("(../delegar/workloads.md?view=1#prova)", actual)
        self.assertIn("https://example.com/guide#prova", actual)
        self.assertIn("[Exemplo](../../productivity/delegar/workloads.md)", actual)

    def test_sync_updates_copies_without_changing_sources(self):
        source = self.root / "skills/development/implementar/testing.md"
        content = source.read_text(encoding="utf-8") + "\nNota de verificação.\n"
        source.write_text(content, encoding="utf-8")
        self.assertTrue(validate(self.root)[0])
        self.assertGreater(sync(self.root), 0)
        self.assertEqual(validate(self.root)[0], [])
        self.assertEqual(source.read_text(encoding="utf-8"), content)
        self.assertEqual(sync(self.root), 0)

    def test_sync_refuses_orphan_copies_without_overwriting(self):
        extra = self.root / ".claude/skills/custom/SKILL.md"
        extra.parent.mkdir()
        extra.write_text("Conteúdo local a preservar.\n", encoding="utf-8")
        before = (self.root / ".agents/skills/implementar/testing.md").read_bytes()
        source = self.root / "skills/development/implementar/testing.md"
        source.write_text("Alteração ainda não exportada.\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Cópias fora do catálogo"):
            sync(self.root)
        self.assertEqual(extra.read_text(encoding="utf-8"), "Conteúdo local a preservar.\n")
        self.assertEqual((self.root / ".agents/skills/implementar/testing.md").read_bytes(), before)

    def test_sync_rejects_empty_orphan_directories(self):
        (self.root / ".agents/skills/unknown").mkdir()
        with self.assertRaisesRegex(ValueError, "Cópias fora do catálogo"):
            sync(self.root)

    def test_missing_skill_manifest_in_group_is_rejected(self):
        (self.root / "skills/productivity/incomplete").mkdir()
        with self.assertRaisesRegex(ValueError, "SKILL.md ausente"):
            validate(self.root)

    def test_example_policy_must_stay_valid(self):
        path = self.root / ".agents/models.example.toml"
        path.write_text(path.read_text(encoding="utf-8").replace(
            'model = "inherit", effort', 'model = "gpt", effort'), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "provider e model"):
            validate(self.root)

    def write_json(self, relative, change):
        path = self.root / relative
        data = json.loads(path.read_text(encoding="utf-8"))
        change(data)
        path.write_text(json.dumps(data), encoding="utf-8")

    def test_plugin_manifest_drift_is_rejected(self):
        cases = {
            "version deve seguir": lambda: self.write_json(
                ".claude-plugin/plugin.json", lambda d: d.update(version="1.0")),
            "campos fora da lista permitida": lambda: self.write_json(
                ".claude-plugin/plugin.json", lambda d: d.update(hooks="./hooks/hooks.json")),
            "a única entrada deve publicar este plugin": lambda: self.write_json(
                ".claude-plugin/marketplace.json", lambda d: d["plugins"][0].update(name="outro")),
            "a versão fica apenas em plugin.json": lambda: self.write_json(
                ".claude-plugin/marketplace.json", lambda d: d["plugins"][0].update(version="0.1.0")),
            "não distribui componentes executáveis": lambda: (self.root / ".mcp.json").write_text(
                "{}", encoding="utf-8"),
            "agents/: difere de .claude/agents": lambda: (self.root / "agents/planner.md").write_text(
                "Papel desatualizado\n", encoding="utf-8"),
            "falta a seção da versão": lambda: self.write_json(
                ".claude-plugin/plugin.json", lambda d: d.update(version="9.9.9")),
        }
        for message, corrupt in cases.items():
            with self.subTest(message=message):
                self.setUp()
                corrupt()
                errors, _, _ = validate(self.root)
                self.assertTrue(any(message in error for error in errors), errors)

    def test_catalog_documents_must_list_every_skill(self):
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8").replace(
            "| `conhecer-ferramentas` |", "| `toolkit` |"), encoding="utf-8")
        errors, _, _ = validate(self.root)
        self.assertTrue(any("README.md: o catálogo difere das skills; faltam ['conhecer-ferramentas'], "
                            "sobram ['toolkit']" in error for error in errors), errors)

    def test_hidden_characters_are_rejected(self):
        target = self.root / "skills/development/implementar/SKILL.md"
        target.write_text(target.read_text(encoding="utf-8") + "\nTexto\u200bescondido.\n",
                          encoding="utf-8")
        sync(self.root)
        errors, _, _ = validate(self.root)
        self.assertTrue(any("caractere invisível ou de controle U+200B" in e for e in errors))

    def test_sync_generates_plugin_agents_and_refuses_extras(self):
        shutil.rmtree(self.root / "agents")
        self.assertEqual(sync(self.root), 3)
        self.assertEqual(validate(self.root)[0], [])
        (self.root / "agents/custom.md").write_text("Papel local.\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Papéis do plugin fora de"):
            sync(self.root)

    def test_policy_requires_configuration_for_canonical_roles(self):
        path = self.root / ".agents/models.toml"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "[roles.representative]", "[roles.other]"), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Responsabilidades sem configuração: representative"):
            validate(self.root)

    def edit(self, relative, transform):
        path = self.root / relative
        path.write_text(transform(path.read_text(encoding="utf-8")), encoding="utf-8")

    def test_old_skill_names_cited_as_skills_are_rejected(self):
        cases = {
            "Use `review` para analisar o diff.": "nome antigo `review`; use `revisar`",
            "> `$propose Mostre a abordagem.`": "nome antigo `propose`; use `propor`",
            "/jordyfontoura-skills:propose": "nome antigo `propose`; use `propor`",
            "Veja skills/development/review/SKILL.md.": "nome antigo `review`; use `revisar`",
            "Use interview para alinhar.": "nome antigo `interview`; use `entrevistar`",
            "Use `interview-async` para arquivos.": "nome antigo `interview-async`",
            "Rode `retro` ao final.": "nome antigo `retro`; use `melhorar-harness`",
            "Peça `pera-ai`.": "nome antigo `pera-ai`; use `esclarecer`",
        }
        for text, message in cases.items():
            with self.subTest(text=text):
                self.setUp()
                self.edit("docs/HARNESS.md", lambda t: t + "\n" + text + "\n")
                errors, _, _ = validate(self.root)
                self.assertTrue(any(message in e and "docs/HARNESS.md:" in e for e in errors), errors)

    def test_old_skill_name_in_description_is_rejected(self):
        self.edit("skills/development/revisar/SKILL.md",
                  lambda t: t.replace("\ndescription: ", "\ndescription: Antes chamada review. ", 1))
        sync(self.root)
        errors, _, _ = validate(self.root)
        self.assertTrue(any("skills/development/revisar/SKILL.md:3: nome antigo `review`" in e
                            for e in errors), errors)

    def test_legitimate_mentions_of_old_names_pass(self):
        self.edit("docs/HARNESS.md", lambda t: t + (
            "\nInspirada em [prototype, de Matt Pocock]"
            "(https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md).\n"
            "Resolva `roles.council` e `[roles.council]`.\n"
            "- **Passagem de contexto (handoff)**: registro para retomar.\n"
            "A implementação usa receiving-code-review como referência.\n"))
        self.assertEqual(validate(self.root)[0], [])

    def test_renames_come_from_the_changelog(self):
        self.edit("CHANGELOG.md", lambda t: t.replace(
            "### Renomeações\n", "### Renomeações\n\n- `antigo-x` passou a se chamar `revisar`.\n", 1))
        self.edit("docs/HARNESS.md", lambda t: t + "\nUse `antigo-x`.\n")
        errors, _, _ = validate(self.root)
        self.assertTrue(any("nome antigo `antigo-x`; use `revisar`" in e for e in errors), errors)

        self.setUp()
        self.edit("CHANGELOG.md", lambda t: re.sub(r"(?m)^- `[a-z0-9-]+` passou a se chamar .*\n",
                                                   "", t))
        errors, _, _ = validate(self.root)
        self.assertTrue(any("nenhuma renomeação" in e for e in errors), errors)

    def test_renames_must_end_in_the_catalog(self):
        cases = {
            "- `revisar` passou a se chamar `outra`.\n": "`revisar` foi renomeada, mas ainda está",
            "- `velha` passou a se chamar `inexistente`.\n": "renomeação de `velha` não termina",
            "- `ida` passou a se chamar `volta`.\n- `volta` passou a se chamar `ida`.\n":
                "renomeação de `ida` não termina",
        }
        for lines, message in cases.items():
            with self.subTest(message=message):
                self.setUp()
                self.edit("CHANGELOG.md", lambda t: t.replace(
                    "### Renomeações\n", "### Renomeações\n\n" + lines, 1))
                errors, _, _ = validate(self.root)
                self.assertTrue(any(message in e for e in errors), errors)

    def test_old_name_exceptions_are_narrow_and_used(self):
        self.edit("docs/MODELS.md", lambda t: t + "\nUse `council` para pareceres.\n")
        errors, _, _ = validate(self.root)
        self.assertTrue(any("docs/MODELS.md:" in e and "nome antigo `council`" in e
                            for e in errors), errors)

        self.setUp()
        self.edit("THIRD_PARTY_NOTICES.md", lambda t: t.replace(
            "das skills `unslop` e `technical-writing`", "de duas skills"))
        errors, _, _ = validate(self.root)
        self.assertTrue(any("exceção de nome antigo sem uso" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
