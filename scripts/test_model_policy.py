"""Verifica herança, alternativas ordenadas e falhas da política de modelos."""

import copy
from pathlib import Path
import unittest

from model_policy import load_policy, resolve_policy, validate_policy


ROOT = Path(__file__).resolve().parents[1]


class ModelPolicyTests(unittest.TestCase):
    def setUp(self):
        # Fixture da v1: compatibilidade independente da política pessoal.
        self.policy = {
            "version": 1,
            "defaults": {"provider": "inherit", "model": "inherit", "effort": "inherit"},
            "roles": {name: {"when": "Trabalho autorizado.", "fallbacks": []} for name in
                      ("orchestrator", "planner", "implementer", "reviewer", "evaluator", "representative", "council")},
        }

    def test_initial_roles_inherit_without_pin_or_fallback(self):
        for role in self.policy["roles"]:
            with self.subTest(role=role):
                options = resolve_policy(self.policy, role)["candidates"]
                self.assertEqual(options, [{"provider": "inherit", "model": "inherit", "effort": "inherit"}])

    def test_legacy_result_shape_and_selection_remain_unchanged(self):
        expected = {"role": "implementer", "when": "Trabalho autorizado.",
                    "candidates": [dict(self.policy["defaults"])]}
        self.assertEqual(resolve_policy(self.policy, "implementer"), expected)
        self.assertEqual(resolve_policy(self.policy, "implementer", "hard"), expected)
        with self.assertRaisesRegex(ValueError, "nível desconhecido"):
            resolve_policy(self.policy, "implementer", "typo")

    def test_role_override_preserves_defaults_and_other_roles(self):
        self.policy["roles"]["representative"].update(provider="provider-a", model="model-a", effort="high")
        self.assertEqual(resolve_policy(self.policy, "representative")["candidates"][0],
                         {"provider": "provider-a", "model": "model-a", "effort": "high"})
        self.assertEqual(resolve_policy(self.policy, "implementer")["candidates"][0]["model"], "inherit")

    def test_explicit_defaults_and_effort_override_are_combined(self):
        self.policy["defaults"].update(provider="provider-a", model="model-a", effort="medium")
        self.policy["roles"]["planner"]["effort"] = "high"
        self.assertEqual(resolve_policy(self.policy, "planner")["candidates"][0],
                         {"provider": "provider-a", "model": "model-a", "effort": "high"})
        self.assertEqual(resolve_policy(self.policy, "implementer")["candidates"][0]["effort"], "medium")

    def test_fallback_order_and_explicit_effort_are_preserved(self):
        options = [{"provider": "provider-b", "model": "model-b", "effort": "medium"},
                   {"provider": "provider-a", "model": "model-c", "effort": "inherit"}]
        self.policy["roles"]["evaluator"]["fallbacks"] = options
        resolved = resolve_policy(self.policy, "evaluator")["candidates"]
        self.assertEqual(resolved[1:], options)
        resolved[1]["model"] = "edited"
        self.assertEqual(options[0]["model"], "model-b")

    def test_unknown_role_reference_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "sem configuração"):
            resolve_policy(self.policy, "unconfigured")
        with self.assertRaisesRegex(ValueError, "sem configuração"):
            validate_policy(self.policy, required_roles=["unconfigured"])

    def test_invalid_configurations_are_rejected(self):
        mutations = [
            lambda p: p.update(version=True),
            lambda p: p.update(version=3),
            lambda p: p["defaults"].update(provder="typo"),
            lambda p: p["defaults"].update(model=""),
            lambda p: p["roles"]["representative"].update(provider="provider-a"),
            lambda p: p["roles"]["council"].update(when=""),
            lambda p: p["roles"]["council"].update(modle="typo"),
            lambda p: p["roles"]["council"].update(effort=False),
            lambda p: p["roles"]["council"].update(fallbacks="model-a"),
            lambda p: p["roles"]["council"].update(fallbacks=[{"model": "model-a"}]),
            lambda p: p["roles"]["council"].update(fallbacks=[dict(p["defaults"])]),
        ]
        for mutation in mutations:
            policy = copy.deepcopy(self.policy)
            mutation(policy)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                validate_policy(policy)

    def test_repeated_fallback_is_rejected(self):
        option = {"provider": "provider-a", "model": "model-a", "effort": "high"}
        self.policy["roles"]["reviewer"]["fallbacks"] = [option, dict(option)]
        with self.assertRaisesRegex(ValueError, "alternativa repetida"):
            validate_policy(self.policy)

    def test_explicit_primary_cannot_be_its_own_fallback(self):
        role = self.policy["roles"]["reviewer"]
        option = {"provider": "provider-a", "model": "model-a", "effort": "inherit"}
        role.update(option)
        role["fallbacks"] = [dict(option)]
        with self.assertRaisesRegex(ValueError, "alternativa repetida"):
            validate_policy(self.policy)


class ProfilePolicyTests(unittest.TestCase):
    def setUp(self):
        self.policy = load_policy(ROOT / ".agents/models.toml")

    def test_personal_preferences_and_order(self):
        expected = {
            "simple": [("gpt-6-luna", "medium"), ("claude-haiku-5-5", "medium")],
            "default": [("gpt-6.1-sol", "medium"), ("claude-sonnet-5-5", "high")],
            "hard": [("claude-opus-5-5", "high"), ("gpt-6.1-sol", "high")],
            "orchestrator": [("claude-opus-5-5", "high"), ("gpt-6.1-sol", "high")],
            "representative": [("claude-opus-5-5", "high"), ("gpt-6.1-sol", "high")],
            "evaluator": [("claude-opus-5-5", "high"), ("gpt-6.1-sol", "high")],
        }
        for profile, pairs in expected.items():
            options = self.policy["profiles"][profile]["candidates"]
            self.assertEqual([(o["model"], o["effort"]) for o in options], pairs)
            for option in options:
                self.assertEqual(option["provider"], "codex" if option["model"].startswith("gpt-") else "claudeAgent")

    def test_complexity_routing_and_protected_roles(self):
        for role in ("implementer", "reviewer"):
            for level in ("simple", "default", "hard"):
                result = resolve_policy(self.policy, role, level)
                self.assertEqual(result["profile"], level)
                self.assertEqual(result["complexity_applied"], level != "default")
        for role, profile in (("representative", "representative"), ("evaluator", "evaluator"),
                              ("council", "evaluator"), ("orchestrator", "orchestrator")):
            result = resolve_policy(self.policy, role, "hard")
            self.assertEqual(result["profile"], profile)
            self.assertFalse(result["complexity_applied"])

    def test_planner_keeps_hard_candidates_at_every_complexity(self):
        for level in ("simple", "default", "hard"):
            with self.subTest(level=level):
                result = resolve_policy(self.policy, "planner", level)
                self.assertEqual(result["profile"], "hard")
                self.assertEqual(result["candidates"], self.policy["profiles"]["hard"]["candidates"])
                self.assertFalse(result["complexity_applied"])

    def test_known_level_without_override_preserves_role(self):
        del self.policy["roles"]["implementer"]["complexity"]["hard"]
        result = resolve_policy(self.policy, "implementer", "hard")
        self.assertEqual(result["profile"], "default")
        self.assertFalse(result["complexity_applied"])
        with self.assertRaisesRegex(ValueError, "nível desconhecido"):
            resolve_policy(self.policy, "implementer", "medium")

    def test_resolved_options_are_isolated(self):
        result = resolve_policy(self.policy, "council")
        original = copy.deepcopy(resolve_policy(self.policy, "evaluator"))
        result["candidates"][0]["effort"] = "low"
        self.assertEqual(resolve_policy(self.policy, "evaluator"), original)

    def test_profile_names_do_not_imply_complexity(self):
        self.policy["roles"]["implementer"]["complexity"]["hard"] = "simple"
        self.assertEqual(resolve_policy(self.policy, "implementer", "hard")["profile"], "simple")

    def test_neutral_and_custom_roles(self):
        self.policy["profiles"]["neutral"] = {"candidates": [
            {"provider": "inherit", "model": "inherit", "effort": "inherit"}]}
        self.policy["roles"]["researcher"] = {"when": "Pesquisar fontes.", "profile": "neutral",
                                               "complexity": {"hard": "hard"}}
        self.assertEqual(resolve_policy(self.policy, "researcher")["candidates"][0]["model"], "inherit")
        self.assertEqual(resolve_policy(self.policy, "researcher", "hard")["profile"], "hard")

    def test_invalid_profile_policies_are_rejected(self):
        mutations = [
            lambda p: p.update(version=3),
            lambda p: p.update(defaults={}),
            lambda p: p.update(profiles={}),
            lambda p: p.update(roles={}),
            lambda p: p["profiles"].update({"Invalid": {"candidates": []}}),
            lambda p: p["profiles"]["simple"].update(candidates=[]),
            lambda p: p["profiles"]["simple"].update(candidates="typo"),
            lambda p: p["profiles"]["simple"]["candidates"][0].update(provider="inherit"),
            lambda p: p["profiles"]["simple"]["candidates"][1].update(provider="inherit", model="inherit"),
            lambda p: p["profiles"]["simple"]["candidates"].append(dict(p["profiles"]["simple"]["candidates"][0])),
            lambda p: p["roles"]["planner"].update(profile="absent"),
            lambda p: p["roles"]["planner"].update(profile=[]),
            lambda p: p["roles"]["planner"].update(fallbacks=[]),
            lambda p: p["roles"]["planner"].update(when=""),
            lambda p: p["roles"]["implementer"]["complexity"].update(default="default"),
            lambda p: p["roles"]["implementer"]["complexity"].update(medium="simple"),
            lambda p: p["roles"]["implementer"]["complexity"].update(hard="absent"),
            lambda p: p["roles"]["planner"].update(complexity=[]),
        ]
        for role in ("representative", "evaluator", "council"):
            policy = copy.deepcopy(self.policy)
            policy["roles"][role]["complexity"] = {}
            with self.assertRaisesRegex(ValueError, "não aceita mapa"):
                validate_policy(policy)
        for mutation in mutations:
            policy = copy.deepcopy(self.policy)
            mutation(policy)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                validate_policy(policy)


if __name__ == "__main__":
    unittest.main()
