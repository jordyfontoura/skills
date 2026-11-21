"""Mede o histórico de conversas de um projeto e gera o relatório HTML de `melhorar-harness`.

Lê somente os registros locais do Claude Code e do Codex cujo diretório de trabalho pertence
ao projeto. Usa apenas a biblioteca padrão do Python 3.11+.

    python history.py collect --project . --days 30 --data dados.json
    python history.py render --data dados.json --findings achados.json --out relatorio.html
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from html import escape
import json
from pathlib import Path
import re
import subprocess
import sys


SECRET = re.compile(r"(?i)\b(sk-[\w-]{8,}|gh[pousr]_\w{8,}|xox[abp]-[\w-]{8,}|AKIA\w{12,}"
                    r"|(?:token|secret|password|senha|api[_-]?key)\s*[=:]\s*\S+)")
SKILL_MENTION = re.compile(r"(?<![\w$/])[$/](?:[\w-]+:)?([a-z][a-z0-9]*(?:-[a-z0-9]+)*)(?![\w-])")
COMMAND_NAME = re.compile(r"<command-name>/?(?:[\w-]+:)?([\w-]+)</command-name>")
NESTED_TOOL = re.compile(r"\btools\.(\w+)\s*\(")
CODEX_COMMAND = re.compile(r"""\bcmd\s*:\s*(["'`])((?:\\.|(?!\1).)*)\1""", re.S)
TOKEN_KINDS = ("input", "cache_read", "cache_write", "output")
REPEAT_THRESHOLD = 3
IDLE_GAP = 1800  # Intervalos maiores que este, em segundos, não contam como trabalho do turno.
CAUSE_KINDS = ("observada", "inferida")


def clean(text, limit):
    text = SECRET.sub("[segredo omitido]", " ".join(str(text).split()))
    return text if len(text) <= limit else text[:limit - 1] + "…"


def moment(value):
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def records(path):
    with open(path, encoding="utf-8", errors="replace") as handle:
        for line in handle:
            try:
                record = json.loads(line)
            except ValueError:
                continue
            if isinstance(record, dict):
                yield record


def normal(path):
    return str(path).replace("\\", "/").rstrip("/").lower()


def error_key(message):
    """Agrupa mensagens que só diferem por caminhos, números ou identificadores."""
    line = next((part for part in str(message).splitlines() if part.strip()), "")
    line = re.sub(r"<[^>]{1,40}>", " ", line)
    line = re.sub(r"(?:[A-Za-z]:)?[\\/][\w.\\/ ~-]+", "<caminho>", line)
    line = re.sub(r"\b[0-9a-f]{8,}\b", "<id>", line)
    line = re.sub(r"\d+", "N", line)
    return clean(line, 140)


def command_key(command):
    """Reduz um comando ao programa e ao subcomando, para contar repetições."""
    steps = [step.strip() for step in re.split(r"&&|\|\||[;|\n]", str(command)) if step.strip()]
    for step in steps:
        words = [word for word in step.split() if not re.match(r"^\w+=", word)]
        if words and words[0] not in ("cd", "pushd", "Set-Location", "export", "set"):
            break
    else:
        return clean(steps[0] if steps else "", 60)
    # Caminhos, variáveis e textos entre aspas mudam a cada chamada e não identificam o comando.
    extra = []
    for word in words[1:3]:
        if re.search(r"""[/\\"'$<>(){}]""", word):
            break
        extra.append(word)
    return clean(" ".join([words[0].strip("\"'").replace("\\", "/").rsplit("/", 1)[-1], *extra]), 60)


class Session:
    def __init__(self, provider, identifier, path):
        self.provider, self.id, self.path = provider, identifier, str(path)
        self.title, self.cwd, self.branch = "", "", ""
        self.start = self.end = None
        self.tokens = Counter()
        self.subagent_tokens = Counter()
        self.models = Counter()
        self.tools, self.errors = Counter(), Counter()
        self.error_samples = defaultdict(lambda: {"count": 0, "sample": ""})
        self.reads, self.commands = Counter(), Counter()
        self.skills = Counter()
        self.prompts = self.interruptions = self.compactions = self.subagents = 0
        self.active = self.longest_turn = 0.0
        self.peak_context = 0
        self.cost_usd = None
        self._turn = self._last = None

    def seen(self, when):
        if when is None:
            return
        self.start = min(self.start or when, when)
        self.end = max(self.end or when, when)
        if self._turn is not None and self._last:
            gap = (when - self._last).total_seconds()
            if 0 < gap <= IDLE_GAP:
                self._turn += gap
        self._last = when

    def open_turn(self, when):
        self.close_turn()
        self._turn, self._last = 0.0, when

    def close_turn(self):
        if self._turn:
            self.active += self._turn
            self.longest_turn = max(self.longest_turn, self._turn)
        self._turn = None

    def prompt(self, text, when, known):
        self.prompts += 1
        self.open_turn(when)
        if not self.title:
            self.title = clean(text, 90)
        for name in set(SKILL_MENTION.findall(text)):
            if name in known:
                self.skills[name] += 1

    def tool(self, name, arguments, root):
        self.tools[name] += 1
        if name == "Read" and arguments.get("file_path"):
            path = str(arguments["file_path"]).replace("\\", "/")
            self.reads[path[len(root) + 1:] if normal(path).startswith(root + "/") else path] += 1
        elif name in ("Bash", "PowerShell", "exec_command") and arguments.get("command"):
            self.commands[command_key(arguments["command"])] += 1
        elif name == "Skill" and arguments.get("skill"):
            self.skills[str(arguments["skill"]).split(":")[-1]] += 1

    def error(self, tool, message, command=None):
        self.errors[tool] += 1
        pattern = error_key(message)
        if command:
            pattern = f"{command_key(command)}: {pattern}"
        entry = self.error_samples[f"{tool}\t{pattern}"]
        entry["count"] += 1
        entry["sample"] = entry["sample"] or clean(message, 260)

    def export(self):
        self.close_turn()
        return {
            "provider": self.provider, "id": self.id, "path": self.path, "title": self.title,
            "branch": self.branch, "start": self.start.isoformat() if self.start else None,
            "end": self.end.isoformat() if self.end else None,
            "wall_seconds": (self.end - self.start).total_seconds() if self.start else 0,
            "active_seconds": self.active, "longest_turn_seconds": self.longest_turn,
            "prompts": self.prompts, "interruptions": self.interruptions,
            "compactions": self.compactions, "subagents": self.subagents,
            "tokens": {kind: self.tokens[kind] for kind in TOKEN_KINDS},
            "subagent_tokens": {kind: self.subagent_tokens[kind] for kind in TOKEN_KINDS},
            "peak_context": self.peak_context, "cost_usd": self.cost_usd,
            "models": {k: v for k, v in self.models.items() if v}, "tools": dict(self.tools), "errors": dict(self.errors),
            "error_samples": dict(self.error_samples), "skills": dict(self.skills),
            "reads": {k: v for k, v in self.reads.items() if v >= REPEAT_THRESHOLD},
            "commands": {k: v for k, v in self.commands.items() if v >= REPEAT_THRESHOLD},
        }


def text_of(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(str(block.get("text", "")) for block in content
                         if isinstance(block, dict) and block.get("type") in ("text", "input_text"))
    return ""


def read_claude(path, root, known, session=None):
    """Lê uma conversa do Claude Code; com `session`, soma um subagente à conversa principal."""
    main = session is None
    session = session or Session("claude", path.stem, path)
    requests, calls, attributed = {}, {}, set()
    for record in records(path):
        kind = record.get("type")
        when = moment(record.get("timestamp"))
        if main:
            session.seen(when)
            session.cwd = session.cwd or record.get("cwd") or ""
            session.branch = record.get("gitBranch") or session.branch
        if kind == "custom-title" and main:
            session.title = clean(record.get("customTitle", ""), 90) or session.title
        elif kind == "cost-state" and main:
            cost = record.get("totalCostUSD")
            if isinstance(cost, (int, float)):
                session.cost_usd = max(session.cost_usd or 0, cost)
        elif kind == "system" and record.get("subtype") == "compact_boundary":
            session.compactions += 1
        elif kind == "assistant":
            message = record.get("message") or {}
            if isinstance(message.get("usage"), dict) and message.get("id"):
                # Cada bloco da mesma resposta repete o uso; vale um registro por resposta.
                requests[message["id"]] = (message.get("model") or "desconhecido", message["usage"])
            if main and record.get("attributionSkill"):
                attributed.add(str(record["attributionSkill"]).split(":")[-1])
            for block in message.get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    arguments = block.get("input") if isinstance(block.get("input"), dict) else {}
                    calls[block.get("id")] = (block.get("name", "?"), arguments.get("command"))
                    session.tool(block.get("name", "?"), arguments, root)
        elif kind == "user":
            content = (record.get("message") or {}).get("content")
            results = [b for b in content if isinstance(b, dict) and b.get("type") == "tool_result"] \
                if isinstance(content, list) else []
            for block in results:
                if block.get("is_error"):
                    name, command = calls.get(block.get("tool_use_id"), ("?", None))
                    session.error(name, text_of(block.get("content")) or block.get("content") or "",
                                  command)
            text = text_of(content).strip()
            if results or not text or not main or record.get("isMeta") \
                    or record.get("isCompactSummary") or record.get("isSidechain"):
                continue
            if text.startswith("[Request interrupted"):
                session.interruptions += 1
                continue
            command = COMMAND_NAME.search(text)
            if command:
                if command[1] in known:
                    session.skills[command[1]] += 1
                session.prompts += 1
                session.open_turn(when)
            elif not text.startswith("<"):
                session.prompt(text, when, known)
    for name in attributed - set(session.skills):
        session.skills[name] = 1
    target = session.tokens if main else session.subagent_tokens
    for model, usage in requests.values():
        amounts = {"input": usage.get("input_tokens") or 0,
                   "cache_read": usage.get("cache_read_input_tokens") or 0,
                   "cache_write": usage.get("cache_creation_input_tokens") or 0,
                   "output": usage.get("output_tokens") or 0}
        target.update(amounts)
        session.models[model] += sum(amounts.values())
        if main:
            # Uma resposta com várias iterações soma o uso de todas; o contexto é o da maior.
            steps = [step for step in usage.get("iterations") or [usage] if isinstance(step, dict)]
            session.peak_context = max([session.peak_context] + [
                sum(step.get(key) or 0 for key in
                    ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"))
                for step in steps])
    if main:
        for child in sorted((path.with_suffix("") / "subagents").glob("*.jsonl")):
            session.subagents += 1
            read_claude(child, root, known, session)
    return session


def read_codex(path, root, known):
    session = Session("codex", path.stem[-36:], path)
    calls, usage = {}, None
    for record in records(path):
        kind, payload = record.get("type"), record.get("payload")
        if not isinstance(payload, dict):
            continue
        when = moment(record.get("timestamp"))
        session.seen(when)
        inner = payload.get("type")
        if kind == "session_meta":
            session.cwd = payload.get("cwd") or session.cwd
            session.id = payload.get("id") or session.id
        elif kind == "turn_context":
            session.branch = (payload.get("git") or {}).get("branch") or session.branch \
                if isinstance(payload.get("git"), dict) else session.branch
            session.models[payload.get("model") or "desconhecido"] += 0
        elif kind == "event_msg":
            if inner == "token_count" and isinstance((payload.get("info") or {}).get("total_token_usage"), dict):
                usage = payload["info"]["total_token_usage"]
            elif inner == "task_complete":
                session.close_turn()
            elif inner == "turn_aborted":
                session.interruptions += 1
                session.close_turn()
            elif inner and "compact" in inner:
                session.compactions += 1
            elif inner == "item_completed" and (payload.get("item") or {}).get("type") == "UserMessage":
                session.prompt(text_of(payload["item"].get("content")), when, known)
            elif inner == "user_message" and payload.get("message"):
                session.prompt(str(payload["message"]), when, known)
        elif kind == "response_item" and inner in ("custom_tool_call", "function_call"):
            name, source = payload.get("name", "?"), payload.get("input") or payload.get("arguments") or ""
            names = NESTED_TOOL.findall(str(source)) if name == "exec" else []
            calls[payload.get("call_id")] = names[0] if names else name
            for nested in names or [name]:
                session.tool(nested, {}, root)
            for match in CODEX_COMMAND.finditer(str(source)):
                session.commands[command_key(match[2])] += 1
        elif kind == "response_item" and inner in ("custom_tool_call_output", "function_call_output"):
            output = payload.get("output")
            text = output if isinstance(output, str) else text_of(output)
            if text.startswith("Script failed") or "Script error:" in text[:400]:
                detail = text.split("Script error:", 1)[-1] if "Script error:" in text else text
                session.error(calls.get(payload.get("call_id"), "?"), detail)
    if usage:
        cached = usage.get("cached_input_tokens") or 0
        session.tokens.update({"input": max((usage.get("input_tokens") or 0) - cached, 0),
                               "cache_read": cached,
                               "cache_write": usage.get("cache_write_input_tokens") or 0,
                               "output": usage.get("output_tokens") or 0})
        model = next(reversed(session.models), "desconhecido")
        session.models[model] += sum(session.tokens.values())
    return session


def first_cwd(path, limit=60):
    for index, record in enumerate(records(path)):
        payload = record.get("payload")
        cwd = record.get("cwd") or (payload.get("cwd") if isinstance(payload, dict) else None)
        if cwd or index >= limit:
            return cwd or ""
    return ""


def project_roots(project, extra):
    """Raiz do projeto, worktrees do Git e raízes informadas, em forma comparável."""
    roots = {normal(project.resolve())} | {normal(Path(p).resolve()) for p in extra}
    try:
        listing = subprocess.run(["git", "-C", str(project), "worktree", "list", "--porcelain"],
                                 capture_output=True, text=True, encoding="utf-8", timeout=20).stdout
    except (OSError, subprocess.SubprocessError):
        listing = ""
    roots |= {normal(line[9:]) for line in listing.splitlines() if line.startswith("worktree ")}
    return roots


def belongs(cwd, roots, name):
    cwd = normal(cwd)
    return bool(cwd) and (any(cwd == root or cwd.startswith(root + "/") for root in roots)
                          or f"/worktrees/{name}/" in cwd + "/")


def known_skills(project):
    names = set()
    for pattern in (".claude/skills/*/SKILL.md", ".agents/skills/*/SKILL.md", "skills/*/*/SKILL.md"):
        names |= {path.parent.name for path in project.glob(pattern)}
    return names


def collect(project, days, claude_home, codex_home, extra=()):
    project = project.resolve()
    root, name = normal(project), project.name.lower()
    roots, known = project_roots(project, extra), known_skills(project)
    since = datetime.now(timezone.utc) - timedelta(days=days)
    sources = {"claude": {"home": str(claude_home), "examined": 0, "included": 0},
               "codex": {"home": str(codex_home), "examined": 0, "included": 0}}
    sessions = []

    def consider(provider, path, reader):
        if datetime.fromtimestamp(path.stat().st_mtime, timezone.utc) < since:
            return
        sources[provider]["examined"] += 1
        if not belongs(first_cwd(path), roots, name):
            return
        session = reader(path, root, known)
        if session.end and session.end >= since and (session.prompts or sum(session.tokens.values())):
            sources[provider]["included"] += 1
            sessions.append(session.export())

    slugs = {re.sub(r"[^a-z0-9]", "-", item) for item in roots}
    directory = claude_home / "projects"
    for folder in sorted(directory.iterdir()) if directory.is_dir() else []:
        lowered = folder.name.lower()
        if folder.is_dir() and (lowered in slugs or f"worktrees-{name}-" in lowered):
            for path in sorted(folder.glob("*.jsonl")):
                consider("claude", path, read_claude)
    for folder in ("sessions", "archived_sessions"):
        for path in sorted((codex_home / folder).rglob("*.jsonl")) if (codex_home / folder).is_dir() else []:
            consider("codex", path, read_codex)
    sessions.sort(key=lambda item: item["start"] or "")
    return {"project": str(project), "generated": datetime.now(timezone.utc).isoformat(),
            "days": days, "since": since.isoformat(), "sources": sources,
            "known_skills": sorted(known), "sessions": sessions, "totals": summarize(sessions)}


def total_tokens(session):
    return sum(session["tokens"].values()) + sum(session["subagent_tokens"].values())


def summarize(sessions):
    tokens, models, tools, errors, days = Counter(), Counter(), Counter(), Counter(), defaultdict(Counter)
    skills, clusters = defaultdict(Counter), {}
    reads, commands = defaultdict(Counter), defaultdict(Counter)
    for session in sessions:
        for kind in TOKEN_KINDS:
            tokens[kind] += session["tokens"][kind] + session["subagent_tokens"][kind]
        models.update(session["models"])
        tools.update(session["tools"])
        errors.update(session["errors"])
        day = (moment(session["start"]) or datetime.now(timezone.utc)).astimezone().date().isoformat()
        days[day].update(sessions=1, tokens=total_tokens(session), active_seconds=session["active_seconds"],
                         errors=sum(session["errors"].values()))
        for name, mentions in session["skills"].items():
            skills[name].update(sessions=1, mentions=mentions, tokens=total_tokens(session),
                                active_seconds=session["active_seconds"],
                                errors=sum(session["errors"].values()))
        for key, entry in session["error_samples"].items():
            cluster = clusters.setdefault(key, {"tool": key.split("\t")[0], "pattern": key.split("\t", 1)[1],
                                                "count": 0, "sessions": 0, "sample": entry["sample"]})
            cluster["count"] += entry["count"]
            cluster["sessions"] += 1
        for source, target in ((session["reads"], reads), (session["commands"], commands)):
            for key, count in source.items():
                target[key].update(count=count, sessions=1)
                target[key]["max"] = max(target[key]["max"], count)
    costs = [s["cost_usd"] for s in sessions if s["cost_usd"] is not None]
    calls = sum(tools.values())
    return {
        "sessions": len(sessions), "prompts": sum(s["prompts"] for s in sessions),
        "active_seconds": sum(s["active_seconds"] for s in sessions),
        "tokens": dict(tokens), "cost_usd": sum(costs) if costs else None, "cost_sessions": len(costs),
        "tool_calls": calls, "tool_errors": sum(errors.values()),
        "compactions": sum(s["compactions"] for s in sessions),
        "interruptions": sum(s["interruptions"] for s in sessions),
        "subagents": sum(s["subagents"] for s in sessions),
        "models": dict(models.most_common()),
        "tools": [{"name": n, "calls": c, "errors": errors[n]} for n, c in tools.most_common()],
        "days": [{"day": d, **days[d]} for d in sorted(days)],
        "skills": sorted(({"name": n, **v} for n, v in skills.items()), key=lambda i: -i["tokens"]),
        "errors": sorted(clusters.values(), key=lambda i: -i["count"]),
        "rereads": sorted(({"file": k, **v} for k, v in reads.items()), key=lambda i: -i["count"]),
        "commands": sorted(({"command": k, **v} for k, v in commands.items()), key=lambda i: -i["count"]),
    }


def load_findings(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("findings"), list):
        raise ValueError("achados: esperado um objeto com a lista `findings`")
    for index, finding in enumerate(data["findings"], 1):
        missing = [key for key in ("title", "evidence", "source", "cause", "cause_kind", "proposal", "cost")
                   if not str(finding.get(key, "")).strip()]
        if missing:
            raise ValueError(f"achado {index}: faltam {', '.join(missing)}")
        if finding["cause_kind"] not in CAUSE_KINDS:
            raise ValueError(f"achado {index}: cause_kind deve ser {' ou '.join(CAUSE_KINDS)}")
    return data


# --- Relatório ---------------------------------------------------------------

def number(value):
    value = float(value or 0)
    for limit, suffix in ((1e9, " bi"), (1e6, " mi"), (1e3, " mil")):
        if abs(value) >= limit:
            return f"{value / limit:.1f}".replace(".", ",") + suffix
    return f"{value:.0f}"


def duration(seconds):
    minutes = int(round((seconds or 0) / 60))
    if minutes < 1:
        return f"{int(seconds or 0)} s"
    return f"{minutes} min" if minutes < 60 else f"{minutes // 60} h {minutes % 60:02d} min"


def percent(part, whole):
    return f"{100 * part / whole:.1f}".replace(".", ",") + "%" if whole else "–"


def prose(text):
    """Escapa o texto dos achados e mostra trechos entre crases como código."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", escape(str(text)))


def table(headers, rows, bar=None, empty="Nada registrado no período."):
    """Monta uma tabela; `bar` é o índice da coluna numérica que recebe a barra de magnitude."""
    if not rows:
        return f'<p class="muted">{escape(empty)}</p>'
    peak = max((row[bar][0] for row in rows), default=0) if bar is not None else 0
    # Colunas de texto ficam à esquerda e quebram linha; só valores se alinham à direita.
    numeric = [index == bar or (index > 0 and all(
        not isinstance(row[index], str) or re.match(r"(\d|US\$|–)", row[index]) for row in rows))
        for index in range(len(headers))]
    body = []
    for row in rows:
        cells = []
        for index, cell in enumerate(row):
            if index == bar:
                width = 100 * cell[0] / peak if peak else 0
                cells.append(f'<td class="num"><span class="bar" style="width:{width:.1f}%"></span>'
                             f'<span class="value">{escape(cell[1])}</span></td>')
            else:
                cells.append(f'<td{" class=\"num\"" if numeric[index] else ""}>{escape(str(cell))}</td>')
        body.append("<tr>" + "".join(cells) + "</tr>")
    head = "".join(f'<th{" class=\"num\"" if numeric[i] else ""}>{escape(h)}</th>'
                   for i, h in enumerate(headers))
    return f'<div class="scroll"><table><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


STYLE = """
:root{--bg:#f7f7f5;--card:#fff;--ink:#1c1c1a;--muted:#62625c;--line:#dedcd5;--bar:#b9d2ee;--accent:#1f5fa8}
@media (prefers-color-scheme:dark){:root{--bg:#161615;--card:#1f1f1d;--ink:#ecebe6;--muted:#a3a299;
--line:#34332f;--bar:#274a73;--accent:#8ab8ea}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1080px;margin:0 auto;padding:32px 16px 64px}
h1{font-size:26px;margin:0 0 4px}h2{font-size:18px;margin:40px 0 12px}h3{font-size:16px;margin:0 0 8px}
.muted{color:var(--muted)}.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-top:20px}
.tile,.finding{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.tile b{display:block;font-size:22px;font-variant-numeric:tabular-nums}.tile span{color:var(--muted);font-size:13px}
.finding{margin-bottom:12px}.finding dl{display:grid;grid-template-columns:120px 1fr;gap:6px 14px;margin:0}
.finding dt{color:var(--muted)}.finding dd{margin:0}
.tag{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:0 8px;font-size:12px;color:var(--muted);margin-left:6px}
.scroll{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:10px}
table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;padding:7px 12px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:0}th{color:var(--muted);font-weight:600;white-space:nowrap}
.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap;position:relative}
.bar{position:absolute;right:8px;top:7px;height:20px;background:var(--bar);border-radius:4px;max-width:calc(100% - 16px)}
.value{position:relative}code{font-size:13px;overflow-wrap:break-word}td{overflow-wrap:break-word}td:first-child{min-width:220px}
@media (max-width:560px){.finding dl{grid-template-columns:1fr}}
"""


def render(data, findings=None):
    totals, sessions = data["totals"], data["sessions"]
    tokens = totals["tokens"]
    processed = sum(tokens.values())
    cost = (f"US$ {totals['cost_usd']:.2f}".replace(".", ",") if totals["cost_usd"] is not None else "desconhecido")
    tiles = [
        (str(totals["sessions"]), "conversas"), (str(totals["prompts"]), "pedidos do usuário"),
        (duration(totals["active_seconds"]), "tempo de agente em turnos"),
        (number(tokens.get("output", 0)), "tokens de saída"),
        (number(tokens.get("input", 0) + tokens.get("cache_write", 0)), "tokens de entrada nova"),
        (number(tokens.get("cache_read", 0)), "tokens lidos do cache"),
        (cost, f"custo registrado em {totals['cost_sessions']} conversas"),
        (f"{totals['tool_errors']} ({percent(totals['tool_errors'], totals['tool_calls'])})",
         f"erros em {number(totals['tool_calls'])} chamadas de ferramenta"),
        (str(totals["compactions"]), "compactações de contexto"),
        (str(totals["interruptions"]), "interrupções pelo usuário"),
    ]
    parts = [f"<!doctype html><html lang=\"pt-BR\"><meta charset=\"utf-8\">"
             f"<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
             f"<title>Histórico do harness</title><style>{STYLE}</style><main>",
             f"<h1>Histórico do harness: {escape(Path(data['project']).name)}</h1>",
             f"<p class=\"muted\">Últimos {data['days']} dias, de {escape(data['since'][:10])} a "
             f"{escape(data['generated'][:10])}. Fontes: "
             + "; ".join(f"{escape(name)}: {info['included']} conversas do projeto entre "
                         f"{info['examined']} arquivos examinados" for name, info in data["sources"].items())
             + ".</p>",
             '<div class="tiles">' + "".join(f"<div class=\"tile\"><b>{escape(v)}</b><span>{escape(l)}</span></div>"
                                             for v, l in tiles) + "</div>"]

    parts.append("<h2>Achados e propostas</h2>")
    if findings:
        if findings.get("summary"):
            parts.append(f"<p>{prose(findings['summary'])}</p>")
        for finding in findings["findings"]:
            rows = [(label, finding[key]) for label, key in (
                ("Impacto", "impact"), ("Evidência", "evidence"), ("Fonte", "source"), ("Causa", "cause"),
                ("Proposta", "proposal"), ("Custo ou risco", "cost"), ("Quem aplica", "owner"))
                if finding.get(key)]
            parts.append(f"<div class=\"finding\"><h3>{prose(finding['title'])}"
                         f"<span class=\"tag\">causa {escape(finding['cause_kind'])}</span></h3><dl>"
                         + "".join(f"<dt>{escape(k)}</dt><dd>{prose(v)}</dd>" for k, v in rows)
                         + "</dl></div>")
        if not findings["findings"]:
            parts.append('<p class="muted">Nenhuma melhoria sustentada pelos dados do período.</p>')
        if findings.get("unknowns"):
            parts.append("<h3>O que ficou desconhecido</h3><ul>"
                         + "".join(f"<li>{prose(item)}</li>" for item in findings["unknowns"]) + "</ul>")
    else:
        parts.append('<p class="muted">Relatório gerado sem análise: só os dados coletados.</p>')

    ranked = sorted(sessions, key=total_tokens, reverse=True)[:15]
    parts.append("<h2>Conversas com mais tokens</h2>" + table(
        ["Conversa", "Agente", "Início", "Pedidos", "Subagentes", "Tempo em turnos", "Erros", "Custo",
         "Maior contexto", "Tokens processados"],
        [[s["title"] or s["id"][:8], s["provider"], (s["start"] or "")[:10], s["prompts"], s["subagents"],
          duration(s["active_seconds"]), sum(s["errors"].values()),
          f"US$ {s['cost_usd']:.2f}".replace(".", ",") if s["cost_usd"] is not None else "–",
          number(s["peak_context"]) if s["peak_context"] else "–",
          (total_tokens(s), number(total_tokens(s)))] for s in ranked], bar=9))
    slow = sorted(sessions, key=lambda s: s["longest_turn_seconds"], reverse=True)[:10]
    parts.append("<h2>Turnos mais longos</h2>" + table(
        ["Conversa", "Agente", "Início", "Subagentes", "Tempo total em turnos", "Maior turno"],
        [[s["title"] or s["id"][:8], s["provider"], (s["start"] or "")[:10], s["subagents"],
          duration(s["active_seconds"]), (s["longest_turn_seconds"], duration(s["longest_turn_seconds"]))]
         for s in slow if s["longest_turn_seconds"]], bar=5))
    parts.append("<h2>Erros frequentes de ferramenta</h2>" + table(
        ["Padrão do erro", "Ferramenta", "Exemplo", "Conversas", "Ocorrências"],
        [[e["pattern"], e["tool"], clean(e["sample"], 160), e["sessions"], (e["count"], str(e["count"]))]
         for e in totals["errors"][:20]], bar=4))
    parts.append("<h2>Ferramentas</h2>" + table(
        ["Ferramenta", "Erros", "Taxa de erro", "Chamadas"],
        [[t["name"], t["errors"], percent(t["errors"], t["calls"]), (t["calls"], str(t["calls"]))]
         for t in totals["tools"][:20]], bar=3))
    parts.append("<h2>Skills</h2><p class=\"muted\">Tokens, tempo e erros são da conversa inteira em que a "
                 "skill apareceu, não só do trecho em que ela atuou.</p>" + table(
        ["Skill", "Conversas", "Usos", "Tempo em turnos", "Erros", "Tokens das conversas"],
        [[s["name"], s["sessions"], s["mentions"], duration(s["active_seconds"]), s["errors"],
          (s["tokens"], number(s["tokens"]))] for s in totals["skills"]], bar=5))
    parts.append(f"<h2>Arquivos relidos</h2><p class=\"muted\">Arquivos lidos {REPEAT_THRESHOLD} vezes ou mais "
                 "na mesma conversa.</p>" + table(
        ["Arquivo", "Conversas", "Máximo numa conversa", "Leituras"],
        [[r["file"], r["sessions"], r["max"], (r["count"], str(r["count"]))] for r in totals["rereads"][:15]], bar=3))
    parts.append(f"<h2>Comandos repetidos</h2><p class=\"muted\">Comandos executados {REPEAT_THRESHOLD} vezes ou "
                 "mais na mesma conversa, reduzidos ao programa e ao subcomando.</p>" + table(
        ["Comando", "Conversas", "Máximo numa conversa", "Execuções"],
        [[c["command"], c["sessions"], c["max"], (c["count"], str(c["count"]))]
         for c in totals["commands"][:15]], bar=3))
    parts.append("<h2>Por dia</h2>" + table(
        ["Dia", "Conversas", "Tempo em turnos", "Erros", "Tokens processados"],
        [[d["day"], d["sessions"], duration(d["active_seconds"]), d["errors"], (d["tokens"], number(d["tokens"]))]
         for d in totals["days"]], bar=4))
    parts.append("<h2>Modelos</h2>" + table(
        ["Modelo", "Parcela", "Tokens processados"],
        [[m, percent(v, processed), (v, number(v))] for m, v in totals["models"].items()], bar=2))
    parts.append("""<h2>Limites dos dados</h2><ul>
<li>Os números vêm dos registros locais dos agentes nesta máquina. Conversas em outra máquina, apagadas ou
de agentes sem leitor não aparecem.</li>
<li>Tokens processados somam entrada nova, escrita e leitura de cache e saída, incluindo subagentes. Não
equivalem a custo: cada tipo tem preço diferente e a leitura de cache costuma ser a maior parcela.</li>
<li>O custo é a estimativa que o Claude Code grava na conversa. O Codex não registra custo, então o total
cobre só parte das conversas e não representa a fatura nem a cota da assinatura.</li>
<li>Tempo em turnos vai de cada pedido até o último registro antes do pedido seguinte. Inclui esperas por
ferramentas e exclui intervalos sem registro acima de 30 minutos e o tempo em que o agente aguardava
o usuário.</li>
<li>No Codex, só falhas de execução marcadas pelo cliente contam como erro; comandos que terminam com
código diferente de zero podem ficar de fora.</li>
<li>Correlação não é causa: uma skill presente numa conversa cara não demonstra que ela causou o gasto.</li>
</ul></main></html>""")
    return "".join(parts)


def main(arguments=None):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    gather = commands.add_parser("collect", help="mede as conversas do projeto e grava os dados em JSON")
    gather.add_argument("--project", type=Path, default=Path.cwd())
    gather.add_argument("--days", type=int, default=30)
    gather.add_argument("--data", type=Path, required=True)
    gather.add_argument("--claude-home", type=Path, default=Path.home() / ".claude")
    gather.add_argument("--codex-home", type=Path, default=Path.home() / ".codex")
    gather.add_argument("--worktree", action="append", default=[],
                        help="outra raiz do mesmo projeto, como um worktree já removido do Git")
    page = commands.add_parser("render", help="gera o relatório HTML a partir dos dados e dos achados")
    page.add_argument("--data", type=Path, required=True)
    page.add_argument("--findings", type=Path)
    page.add_argument("--out", type=Path, required=True)
    options = parser.parse_args(arguments)
    try:
        if options.command == "collect":
            data = collect(options.project, options.days, options.claude_home, options.codex_home,
                           options.worktree)
            options.data.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
            totals = data["totals"]
            print(f"OK: {totals['sessions']} conversas, {totals['prompts']} pedidos, "
                  f"{number(sum(totals['tokens'].values()))} tokens processados, "
                  f"{totals['tool_errors']} erros de ferramenta; dados em {options.data}")
        else:
            data = json.loads(options.data.read_text(encoding="utf-8"))
            findings = load_findings(options.findings) if options.findings else None
            options.out.write_text(render(data, findings), encoding="utf-8")
            print(f"OK: relatório em {options.out}")
    except (OSError, ValueError, KeyError) as error:
        print(f"FALHA: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
