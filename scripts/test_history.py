"""Prova a coleta e o relatório de `melhorar-harness` com conversas sintéticas."""

from datetime import datetime, timedelta, timezone
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

from check import ROOT


SOURCE = ROOT / "skills/harness/melhorar-harness/history.py"
spec = importlib.util.spec_from_file_location("history", SOURCE)
history = importlib.util.module_from_spec(spec)
# Um `__pycache__` ao lado da fonte entraria nas cópias da skill.
bytecode, sys.dont_write_bytecode = sys.dont_write_bytecode, True
try:
    spec.loader.exec_module(history)
finally:
    sys.dont_write_bytecode = bytecode


class HistoryTests(unittest.TestCase):
    def setUp(self):
        workspace = tempfile.TemporaryDirectory()
        self.addCleanup(workspace.cleanup)
        self.base = Path(workspace.name).resolve()
        self.project = self.base / "produto"
        (self.project / ".claude/skills/revisar").mkdir(parents=True)
        (self.project / ".claude/skills/revisar/SKILL.md").write_text("x", encoding="utf-8")
        self.claude, self.codex = self.base / "claude", self.base / "codex"
        self.start = datetime.now(timezone.utc) - timedelta(hours=2)

    def at(self, seconds):
        return (self.start + timedelta(seconds=seconds)).isoformat().replace("+00:00", "Z")

    def write(self, path, lines):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(json.dumps(line) for line in lines) + "\n", encoding="utf-8")

    def assistant(self, seconds, identifier, output, content):
        usage = {"input_tokens": 10, "cache_read_input_tokens": 100,
                 "cache_creation_input_tokens": 20, "output_tokens": output}
        return {"type": "assistant", "timestamp": self.at(seconds), "cwd": str(self.project),
                "message": {"id": identifier, "model": "modelo-a", "usage": usage, "content": content}}

    def claude_session(self, cwd=None):
        cwd = str(cwd or self.project)
        read = {"type": "tool_use", "id": "r", "name": "Read",
                "input": {"file_path": str(self.project / "docs" / "A.md")}}
        bash = {"type": "tool_use", "id": "b", "name": "Bash",
                "input": {"command": "cd x && npm test -- --watch"}}
        return [
            {"type": "user", "timestamp": self.at(0), "cwd": cwd,
             "message": {"content": "Confira isso $revisar e ignore $HOME senha=abc123"}},
            # A mesma resposta aparece em dois registros; o uso conta uma vez.
            self.assistant(10, "m1", 5, [{"type": "thinking"}]),
            self.assistant(11, "m1", 5, [read, read, read, bash]),
            {"type": "user", "timestamp": self.at(20), "cwd": cwd, "message": {"content": [
                {"type": "tool_result", "tool_use_id": "b", "is_error": True,
                 "content": "Exit code 1\nfalhou em /tmp/a/b.js linha 42"}]}},
            # Intervalo acima do limite: não entra no tempo do turno.
            self.assistant(20 + history.IDLE_GAP + 60, "m2", 7, [{"type": "text", "text": "fim"}]),
            {"type": "cost-state", "totalCostUSD": 1.5},
            {"type": "user", "timestamp": self.at(4000), "cwd": cwd,
             "message": {"content": "[Request interrupted by user]"}},
        ]

    def collect(self):
        return history.collect(self.project, 7, self.claude, self.codex)

    def test_claude_session_is_measured_once_per_response(self):
        folder = self.claude / "projects" / "qualquer-worktrees-produto-1"
        self.write(folder / "s1.jsonl", self.claude_session(self.base / "worktrees/produto/w1"))
        self.write(folder / "s1/subagents/a.jsonl", [self.assistant(12, "sub", 3, [])])
        self.write(self.claude / "projects" / "outro-worktrees-produto-2" / "s2.jsonl",
                   self.claude_session(self.base / "outro"))
        data = self.collect()
        self.assertEqual(data["sources"]["claude"], {"home": str(self.claude), "examined": 2, "included": 1})
        session = data["sessions"][0]
        self.assertEqual(session["tokens"], {"input": 20, "cache_read": 200, "cache_write": 40, "output": 12})
        self.assertEqual(session["subagent_tokens"]["output"], 3)
        self.assertEqual((session["prompts"], session["interruptions"], session["subagents"]), (1, 1, 1))
        self.assertEqual(session["active_seconds"], 20)
        self.assertEqual(session["skills"], {"revisar": 1})
        self.assertEqual(session["reads"], {"docs/A.md": 3})
        self.assertEqual(session["cost_usd"], 1.5)
        self.assertNotIn("abc123", session["title"])
        error = data["totals"]["errors"][0]
        self.assertEqual((error["tool"], error["pattern"], error["count"]), ("Bash", "npm test --: Exit code N", 1))
        self.assertEqual(data["totals"]["tools"][0], {"name": "Read", "calls": 3, "errors": 0})

    def test_codex_session_uses_cumulative_usage_and_marked_failures(self):
        usage = {"input_tokens": 100, "cached_input_tokens": 60, "output_tokens": 9}
        call = {"type": "custom_tool_call", "name": "exec", "call_id": "c",
                "input": 'await tools.exec_command({cmd:"git status --short"})'}
        lines = [
            {"type": "session_meta", "timestamp": self.at(0), "payload": {"id": "cx", "cwd": str(self.project)}},
            {"type": "turn_context", "timestamp": self.at(0), "payload": {"model": "modelo-b"}},
            {"type": "event_msg", "timestamp": self.at(1), "payload": {
                "type": "item_completed", "item": {"type": "UserMessage",
                                                   "content": [{"type": "text", "text": "Rode $revisar"}]}}},
            {"type": "response_item", "timestamp": self.at(5), "payload": call},
            {"type": "response_item", "timestamp": self.at(6), "payload": {
                "type": "custom_tool_call_output", "call_id": "c",
                "output": [{"type": "input_text", "text": "Script failed\nScript error:\nexec_command failed: x"}]}},
            {"type": "event_msg", "timestamp": self.at(7), "payload": {"type": "token_count", "info": None}},
            {"type": "event_msg", "timestamp": self.at(8), "payload": {
                "type": "token_count", "info": {"total_token_usage": usage}}},
            {"type": "event_msg", "timestamp": self.at(9), "payload": {"type": "task_complete"}},
        ]
        self.write(self.codex / "sessions/2026/01/01/rollout-cx.jsonl", lines)
        session = self.collect()["sessions"][0]
        self.assertEqual(session["provider"], "codex")
        self.assertEqual(session["tokens"], {"input": 40, "cache_read": 60, "cache_write": 0, "output": 9})
        self.assertEqual(session["models"], {"modelo-b": 109})
        self.assertEqual((session["tools"], session["errors"]), ({"exec_command": 1}, {"exec_command": 1}))
        self.assertEqual((session["skills"], session["active_seconds"]), ({"revisar": 1}, 8))

    def test_command_key_ignores_setup_and_changing_arguments(self):
        cases = {"cd /x && python scripts/check.py --all": "python",
                 "S=\"$TEMP/a\"; git status --short | head": "git status --short",
                 "FOO=1 npm run build": "npm run build", "cd /x": "cd /x", "": ""}
        for command, expected in cases.items():
            self.assertEqual(history.command_key(command), expected, command)

    def test_report_escapes_text_and_refuses_incomplete_findings(self):
        folder = self.claude / "projects" / "x-worktrees-produto-1"
        self.write(folder / "s1.jsonl", self.claude_session(self.base / "worktrees/produto/w1"))
        data = json.loads(json.dumps(self.collect()))
        finding = {"title": "Teste <b>", "evidence": "e", "source": "s", "cause": "c",
                   "cause_kind": "observada", "proposal": "p", "cost": "k"}
        path = self.base / "achados.json"
        path.write_text(json.dumps({"findings": [finding], "unknowns": ["u"]}), encoding="utf-8")
        page = history.render(data, history.load_findings(path))
        self.assertIn("Teste &lt;b&gt;", page)
        self.assertIn("causa observada", page)
        self.assertIn("npm test --: Exit code N", page)
        self.assertIn("sem análise", history.render(data))
        for broken in ({**finding, "cause_kind": "certa"}, {**finding, "proposal": " "}):
            path.write_text(json.dumps({"findings": [broken]}), encoding="utf-8")
            with self.assertRaises(ValueError):
                history.load_findings(path)

    def test_cli_reports_failure_without_traceback(self):
        self.assertEqual(history.main(["render", "--data", str(self.base / "ausente.json"),
                                       "--out", str(self.base / "r.html")]), 1)


if __name__ == "__main__":
    unittest.main()
