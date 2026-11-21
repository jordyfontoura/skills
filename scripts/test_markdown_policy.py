"""Protege a política distribuída e o formato legível de personalização."""

from pathlib import Path
import tempfile
import unittest

from markdown_policy import parse_markdown, serialize_markdown
from model_policy import load_policy, resolve_ladder, resolve_policy, validate_policy


ROOT = Path(__file__).resolve().parents[1]


class MarkdownPolicyTests(unittest.TestCase):
    def setUp(self):
        self.policy = load_policy(ROOT / "knowledge/agents/model-selection.md")
        self.text = serialize_markdown(self.policy)

    def test_personal_choices_survive_migration(self):
        self.assertEqual(resolve_policy(self.policy, "implementer")["candidates"][0],
                         dict(provider="codex", model="gpt-6.1-sol", effort="medium"))
        self.assertEqual(resolve_policy(self.policy, "planner", "hard")["profile"], "hard")
        self.assertEqual(resolve_policy(self.policy, "evaluator", "simple")["profile"], "evaluator")
        ladder = resolve_ladder(self.policy, "padrao")
        self.assertEqual(ladder["max_cycles"], 3)
        self.assertEqual([(s["model"], s["effort"]) for s in ladder["stages"]], [
            ("gpt-6-luna", "xhigh"), ("claude-haiku-5-5", "xhigh"),
            ("gpt-6.1-sol", "medium"), ("claude-opus-5-5", "medium"),
            ("claude-fable-5-2", "medium"),
        ])

    def test_round_trip_preserves_tables_and_cell_values(self):
        self.policy["roles"]["planner"]["when"] = '  Texto | <tag> & &#10;\r\n中文.  '
        self.assertEqual(parse_markdown(serialize_markdown(self.policy)), self.policy)
        self.assertEqual(parse_markdown(serialize_markdown(self.policy).replace("\n", "\r\n")), self.policy)

    def test_invalid_tables_and_references_are_rejected(self):
        cases = [
            (self.text.replace("## Perfis", "## Profiles"), "exige Perfis"),
            (self.text.replace("| Perfil | Ordem", "| Perfil | Posição"), "colunas"),
            (self.text.replace("| simple | 1 |", "| simple | 2 |", 1), "ordem"),
            (self.text.replace("| default | sim |", "| missing | sim |", 1), "perfil sem configuração"),
            (self.text + self.text, "Seção repetida"),
            (self.text.replace("| Perfil | Ordem", "| | Perfil | Ordem"), "colunas"),
            (self.text.split("## Escadas")[0] + "## Escadas\n", "tabela ausente"),
        ]
        for text, message in cases:
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                validate_policy(parse_markdown(text))

    def test_legacy_toml_remains_readable(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "scripts") as directory:
            path = Path(directory) / "models.toml"
            path.write_text('version = 1\n[defaults]\nprovider = "inherit"\nmodel = "inherit"\n'
                            'effort = "inherit"\n[roles.implementer]\nwhen = "Implementar."\n'
                            'fallbacks = []\n', encoding="utf-8")
            self.assertEqual(resolve_policy(load_policy(path), "implementer")["candidates"][0]["model"], "inherit")
