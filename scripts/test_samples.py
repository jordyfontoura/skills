"""Verifica o planejamento das amostras, sem chamar modelos."""

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

import samples


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="")


class SampleTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        write(self.root / "skills/productivity/redigir/SKILL.md",
              "# Redigir\n\nVeja o [padrão](../../../knowledge/writing/clear.md) e o [site](https://example.com).\n")
        write(self.root / "skills/productivity/andamento/SKILL.md", "# Andamento\n")
        write(self.root / "knowledge/writing/clear.md", "# Padrão\n")
        write(self.root / "knowledge/ux/other.md", "# Outro\n")
        write(self.root / "samples/models.toml",
              '[[models]]\nname = "m1"\nprovider = "claude"\nmodel = "model-1"\neffort = "medium"\n')
        write(self.root / "samples/postagem/scenario/scenario.toml", 'skills = ["redigir"]\n')
        write(self.root / "samples/postagem/scenario/turns/01.md", "Escreve uma postagem.\n")
        write(self.root / "samples/postagem/scenario/turns/02.md", "Agora mais curta.\n")

    def tasks(self):
        models = samples.load_models(self.root / "samples/models.toml")
        return samples.plan(self.root, models, samples.load_scenarios(self.root))

    def record(self, tasks):
        for task in tasks:
            write(task.output / "run.json", json.dumps({"inputs_hash": task.inputs_hash}))

    def stale_variants(self):
        return [task.variant for task in samples.stale(self.tasks())]

    def test_scenario_lists_turns_in_order_and_two_variants_per_model(self):
        tasks = self.tasks()
        self.assertEqual([task.variant for task in tasks], ["without-skills", "with-skills"])
        self.assertEqual([turn.name for turn in tasks[0].scenario.turns], ["01.md", "02.md"])
        self.assertEqual(tasks[1].output, self.root / "samples/postagem/m1/with-skills")
        self.assertFalse(tasks[0].scenario.web)

    def test_web_flag_is_read_and_invalidates_both_variants(self):
        self.record(self.tasks())
        write(self.root / "samples/postagem/scenario/scenario.toml", 'skills = ["redigir"]\nweb = true\n')
        self.assertTrue(self.tasks()[0].scenario.web)
        self.assertEqual(self.stale_variants(), ["without-skills", "with-skills"])

    def test_missing_samples_are_stale_until_recorded(self):
        self.assertEqual(self.stale_variants(), ["without-skills", "with-skills"])
        self.record(self.tasks())
        self.assertEqual(self.stale_variants(), [])

    def test_skill_change_only_invalidates_the_variant_with_skills(self):
        self.record(self.tasks())
        write(self.root / "skills/productivity/redigir/SKILL.md", "# Redigir\n\nNova regra.\n")
        self.assertEqual(self.stale_variants(), ["with-skills"])

    def test_referenced_knowledge_invalidates_but_unrelated_files_do_not(self):
        self.record(self.tasks())
        write(self.root / "skills/productivity/andamento/SKILL.md", "# Andamento\n\nMudou.\n")
        write(self.root / "knowledge/ux/other.md", "# Outro\n\nMudou.\n")
        self.assertEqual(self.stale_variants(), [])
        write(self.root / "knowledge/writing/clear.md", "# Padrão\n\nMudou.\n")
        self.assertEqual(self.stale_variants(), ["with-skills"])

    def test_scenario_or_model_change_invalidates_both_variants(self):
        self.record(self.tasks())
        write(self.root / "samples/postagem/scenario/turns/02.md", "Agora mais longa.\n")
        self.assertEqual(self.stale_variants(), ["without-skills", "with-skills"])
        self.record(self.tasks())
        write(self.root / "samples/models.toml",
              '[[models]]\nname = "m1"\nprovider = "claude"\nmodel = "model-1"\neffort = "high"\n')
        self.assertEqual(self.stale_variants(), ["without-skills", "with-skills"])

    def test_scenario_without_listed_skills_depends_on_every_skill(self):
        write(self.root / "samples/postagem/scenario/scenario.toml", "skills = []\n")
        self.record(self.tasks())
        write(self.root / "skills/productivity/andamento/SKILL.md", "# Andamento\n\nMudou.\n")
        self.assertEqual(self.stale_variants(), ["with-skills"])

    def test_line_endings_do_not_change_the_hash(self):
        self.record(self.tasks())
        write(self.root / "samples/postagem/scenario/turns/01.md", "Escreve uma postagem.\r\n")
        self.assertEqual(self.stale_variants(), [])

    def test_hash_order_ignores_case_like_windows_paths(self):
        names = ["README.md", "backup.py", "config.json", "Zeta/a.md", "alfa/B.md"]
        ordered = sorted((Path(name) for name in names), key=samples.hash_order)
        self.assertEqual([path.as_posix() for path in ordered],
                         ["alfa/B.md", "backup.py", "config.json", "README.md", "Zeta/a.md"])

    def test_unknown_skill_and_provider_are_reported(self):
        write(self.root / "samples/postagem/scenario/scenario.toml", 'skills = ["inexistente"]\n')
        with self.assertRaisesRegex(samples.SampleError, "inexistente"):
            self.tasks()
        write(self.root / "samples/models.toml",
              '[[models]]\nname = "m1"\nprovider = "outro"\nmodel = "x"\neffort = "low"\n')
        with self.assertRaisesRegex(samples.SampleError, "provedor desconhecido"):
            self.tasks()

    def test_check_command_fails_only_when_stale(self):
        arguments = ["--config", str(self.root / "samples/models.toml"), "check"]
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(samples.main(arguments, root=self.root), 1)
            self.record(self.tasks())
            self.assertEqual(samples.main(arguments, root=self.root), 0)
        self.assertIn("ausente: postagem · m1 · with-skills", output.getvalue())

    def test_changed_files_ignores_untouched_and_agent_folders(self):
        workspace = self.root / "workspace"
        write(workspace / "kept.md", "igual\n")
        write(workspace / "edited.md", "antes\n")
        before = samples.snapshot(workspace)
        write(workspace / "edited.md", "depois\n")
        write(workspace / "site/index.html", "<p>oi</p>\n")
        write(workspace / ".claude/settings.json", "{}\n")
        self.assertEqual(samples.changed_files(workspace, before), ["edited.md", "site/index.html"])

    def test_workspace_path_is_removed_from_replies(self):
        workspace = Path(r"C:\Temp\samples-abc\workspace")
        text = ("Salvei em [pr.md](/C:/Temp/samples-abc/workspace/pr.md) e em "
                r"C:\Temp\samples-abc\workspace\nota.md.")
        self.assertEqual(samples.without_workspace_path(text, workspace),
                         r"Salvei em [pr.md](<workspace>/pr.md) e em <workspace>\nota.md.")


if __name__ == "__main__":
    unittest.main()
