#!/usr/bin/env python3
"""Gera amostras de como cada modelo responde a cenários fixos, com e sem as skills.

As amostras ficam versionadas em `samples/`; o diff de um PR mostra o efeito de uma mudança
nas skills. Veja `samples/README.md`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import tomllib
import uuid
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = "samples"
VARIANTS = ("without-skills", "with-skills")
# Aumente ao mudar a forma de executar ou de registrar: as amostras do provedor ficam desatualizadas.
FORMAT = {"claude": 2, "codex": 4}
TURN_TIMEOUT = 1200
TOKEN_METRICS = ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_tokens")
LINK = re.compile(r"\]\(([^)#\s]+)")
SKILL_PATH = re.compile(r"skills[\\/]+([a-z0-9-]+)[\\/]+SKILL\.md")
CLAUDE_TOOLS = "Read,Write,Edit,Glob,Grep,Skill"
CLAUDE_ALLOWED = "Read,Glob,Grep,Skill"
CLAUDE_WEB = ",WebSearch,WebFetch"


class SampleError(Exception):
    """Falha de configuração ou de execução de uma amostra."""


@dataclass(frozen=True)
class Model:
    name: str
    provider: str
    model: str
    effort: str


@dataclass(frozen=True)
class Scenario:
    name: str
    path: Path
    skills: tuple[str, ...]
    turns: tuple[Path, ...]
    web: bool = False

    @property
    def source(self) -> Path:
        return self.path / "scenario"


@dataclass(frozen=True)
class Task:
    scenario: Scenario
    model: Model
    variant: str
    inputs_hash: str

    @property
    def output(self) -> Path:
        return self.scenario.path / self.model.name / self.variant

    @property
    def label(self) -> str:
        return f"{self.scenario.name} · {self.model.name} · {self.variant}"


# ---------------------------------------------------------------- configuração


def load_models(config: Path) -> list[Model]:
    data = tomllib.loads(config.read_text(encoding="utf-8"))
    models = [Model(**entry) for entry in data.get("models", [])]
    for model in models:
        if model.provider not in RUNNERS:
            raise SampleError(f"{config}: provedor desconhecido em {model.name}: {model.provider}")
    if len({model.name for model in models}) != len(models):
        raise SampleError(f"{config}: nomes de modelo repetidos")
    return models


def load_scenarios(root: Path) -> list[Scenario]:
    scenarios = []
    for definition in sorted((root / SAMPLES).glob("*/scenario/scenario.toml")):
        path = definition.parents[1]
        data = tomllib.loads(definition.read_text(encoding="utf-8"))
        turns = tuple(sorted((definition.parent / "turns").glob("*.md")))
        if not turns:
            raise SampleError(f"{path.name}: nenhum turno em scenario/turns/")
        scenarios.append(Scenario(path.name, path, tuple(data.get("skills", [])), turns,
                                  bool(data.get("web", False))))
    return scenarios


# ------------------------------------------------------------------------ hash


def normalized(data: bytes) -> bytes:
    """Ignora a diferença de fim de linha entre sistemas."""
    try:
        data.decode("utf-8")
    except UnicodeDecodeError:
        return data
    return data.replace(b"\r\n", b"\n")


def files_under(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(item for item in path.rglob("*") if item.is_file())


def digest(root: Path, paths: list[Path], extra: dict) -> str:
    sha = hashlib.sha256(json.dumps(extra, sort_keys=True).encode())
    for path in sorted(set(paths)):
        sha.update(path.relative_to(root).as_posix().encode() + b"\0")
        sha.update(hashlib.sha256(normalized(path.read_bytes())).digest())
    return sha.hexdigest()


def skill_dir(root: Path, name: str) -> Path:
    found = [path for path in (root / "skills").glob(f"*/{name}") if (path / "SKILL.md").is_file()]
    if len(found) != 1:
        raise SampleError(f"skill não encontrada em skills/<grupo>/: {name}")
    return found[0]


def skill_inputs(root: Path, names: tuple[str, ...]) -> list[Path]:
    """Arquivos das skills indicadas e os arquivos do repositório que elas referenciam."""
    if not names:
        return files_under(root / "skills") + files_under(root / "knowledge")
    paths = []
    for name in names:
        directory = skill_dir(root, name)
        own = files_under(directory)
        paths += own
        for document in own:
            if document.suffix != ".md":
                continue
            for target in LINK.findall(document.read_text(encoding="utf-8")):
                if "://" in target:
                    continue
                linked = (document.parent / target).resolve()
                if linked.is_file() and linked.is_relative_to(root.resolve()):
                    paths.append(root / linked.relative_to(root.resolve()))
    return paths


def inputs_hash(root: Path, scenario: Scenario, model: Model, variant: str) -> str:
    paths = files_under(scenario.source)
    if variant == "with-skills":
        paths += skill_inputs(root, scenario.skills)
    extra = {"format": FORMAT[model.provider], "variant": variant, "provider": model.provider,
             "model": model.model, "effort": model.effort}
    return digest(root, paths, extra)


def recorded_hash(task: Task) -> str | None:
    try:
        return json.loads((task.output / "run.json").read_text(encoding="utf-8"))["inputs_hash"]
    except (OSError, ValueError, KeyError):
        return None


def plan(root: Path, models: list[Model], scenarios: list[Scenario]) -> list[Task]:
    return [Task(scenario, model, variant, inputs_hash(root, scenario, model, variant))
            for scenario in scenarios for model in models for variant in VARIANTS]


def stale(tasks: list[Task]) -> list[Task]:
    return [task for task in tasks if recorded_hash(task) != task.inputs_hash]


# ------------------------------------------------------------------- execução


def executable(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise SampleError(f"CLI não encontrado no PATH: {name}")
    return path


def call(command: list[str], cwd: Path, prompt: str) -> list[dict]:
    """Roda um turno e devolve os eventos JSON emitidos pelo CLI."""
    try:
        result = subprocess.run(command, cwd=cwd, input=prompt, capture_output=True, text=True,
                                encoding="utf-8", errors="replace", timeout=TURN_TIMEOUT)
    except subprocess.TimeoutExpired as error:
        raise SampleError(f"turno excedeu {TURN_TIMEOUT}s") from error
    events = []
    for line in result.stdout.splitlines():
        if line.startswith("{"):
            try:
                events.append(json.loads(line))
            except ValueError:
                pass
    if "blocked by policy" in result.stderr:
        raise SampleError("o sandbox recusou um comando do agente: " + result.stderr.strip()[-300:])
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()[-800:]
        raise SampleError(f"{Path(command[0]).name} saiu com código {result.returncode}: {detail}")
    return events


def cli_version(name: str) -> str:
    result = subprocess.run([executable(name), "--version"], capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=60)
    return result.stdout.strip()


def plugin_name(root: Path) -> str:
    manifest = json.loads((root / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    return manifest["name"]


def repo_skill_names(root: Path) -> set[str]:
    return {path.parent.name for path in (root / "skills").glob("*/*/SKILL.md")}


def run_claude(root: Path, task: Task, workspace: Path, prompts: list[str]):
    """Sem skills: só o que vem embutido no CLI. Com skills: o repositório carregado como plugin."""
    with_skills = task.variant == "with-skills"
    prefix = plugin_name(root) + ":"
    session = str(uuid.uuid4())
    web = CLAUDE_WEB if task.scenario.web else ""
    base = [executable("claude"), "-p", "--model", task.model.model, "--effort", task.model.effort,
            "--setting-sources", "project", "--strict-mcp-config",
            "--tools", CLAUDE_TOOLS + web, "--allowedTools", CLAUDE_ALLOWED + web,
            "--permission-mode", "acceptEdits", "--output-format", "stream-json", "--verbose"]
    if with_skills:
        base += ["--plugin-dir", str(root)]
    replies, used, metrics = [], [], Counter()
    for index, prompt in enumerate(prompts):
        events = call(base + (["--resume", session] if index else ["--session-id", session]),
                      workspace, prompt)
        if index == 0:
            init = next((e for e in events if e.get("subtype") == "init"), {})
            available = set(init.get("skills", []))
            from_plugin = {name for name in available if name.startswith(prefix)}
            leaked = available & repo_skill_names(root)
            if leaked or bool(from_plugin) != with_skills:
                raise SampleError("isolamento das skills falhou: "
                                  f"globais={sorted(leaked)} do repositório={len(from_plugin)}")
        final = next((e for e in reversed(events) if e.get("type") == "result"), None)
        if not final or final.get("is_error"):
            raise SampleError(f"turno {index + 1} sem resultado: {str(final)[:400]}")
        replies.append(final.get("result", ""))
        usage = final.get("usage", {})
        cached = usage.get("cache_read_input_tokens", 0)
        metrics["input_tokens"] += (usage.get("input_tokens", 0) + cached
                                    + usage.get("cache_creation_input_tokens", 0))
        metrics["cached_input_tokens"] += cached
        metrics["output_tokens"] += usage.get("output_tokens", 0)
        metrics["reasoning_tokens"] += usage.get("output_tokens_details", {}).get("thinking_tokens", 0)
        metrics["estimated_cost_usd"] += final.get("total_cost_usd", 0)
        for event in events:
            if event.get("type") != "assistant":
                continue
            for block in event.get("message", {}).get("content", []):
                if block.get("type") != "tool_use":
                    continue
                metrics["tool_calls"] += 1
                if block.get("name") == "Skill":
                    used.append(str(block.get("input", {}).get("skill", "")).removeprefix(prefix))
    metrics["estimated_cost_usd"] = round(metrics["estimated_cost_usd"], 4)
    return replies, used, dict(metrics)


def codex_disabled_skills() -> str:
    """Desativa, só nesta execução, as skills instaladas na pasta pessoal."""
    home = Path.home()
    entries = []
    for base in (home / ".agents" / "skills", home / ".codex" / "skills"):
        for path in sorted(base.glob("*/SKILL.md")):
            entries.append('{path="%s", enabled=false}' % path.as_posix())
    return "skills.config=[" + ",".join(entries) + "]"


def install_codex_skills(root: Path, workspace: Path) -> None:
    """Copia as skills do repositório e as referências que elas apontam por caminho relativo."""
    shutil.copytree(root / ".agents" / "skills", workspace / ".agents" / "skills")
    shutil.copytree(root / "knowledge", workspace / "knowledge", dirs_exist_ok=True)


def run_codex(root: Path, task: Task, workspace: Path, prompts: list[str]):
    """Sem skills: as pessoais desativadas. Com skills: as do repositório no workspace."""
    search = "live" if task.scenario.web else "disabled"
    options = ["--skip-git-repo-check", "--json", "--disable", "apps",
               "-c", f'web_search="{search}"', "-m", task.model.model,
               "-c", f'model_reasoning_effort="{task.model.effort}"',
               "-c", 'sandbox_mode="workspace-write"', "-c", 'approval_policy="never"',
               "-c", codex_disabled_skills(), "-"]
    replies, used, thread, metrics = [], [], None, Counter()
    for index, prompt in enumerate(prompts):
        head = [executable("codex"), "exec"] + (["resume", thread] if index else [])
        events = call(head + options, workspace, prompt)
        thread = thread or next((e["thread_id"] for e in events if e.get("thread_id")), None)
        if not thread:
            raise SampleError("o Codex não informou o id da sessão")
        messages = []
        for event in events:
            item = event.get("item", {})
            if event.get("type") == "turn.completed":
                usage = event.get("usage", {})
                metrics["input_tokens"] += usage.get("input_tokens", 0)
                metrics["cached_input_tokens"] += usage.get("cached_input_tokens", 0)
                metrics["output_tokens"] += usage.get("output_tokens", 0)
                metrics["reasoning_tokens"] += usage.get("reasoning_output_tokens", 0)
            if event.get("type") != "item.completed":
                continue
            if item.get("type") == "agent_message":
                messages.append(item.get("text", ""))
            elif item.get("type") != "reasoning":
                metrics["tool_calls"] += 1
                used += SKILL_PATH.findall(item.get("command", ""))
        if not messages:
            raise SampleError(f"turno {index + 1} sem resposta")
        replies.append(messages[-1])
    return replies, used, dict(metrics)


RUNNERS = {"claude": run_claude, "codex": run_codex}
CLI_NAMES = {"claude": "claude", "codex": "codex"}


# ------------------------------------------------------------------ resultado


def read_when_released(path: Path) -> bytes:
    """Lê o arquivo, esperando quando o agente ou o sandbox ainda o mantém bloqueado."""
    for wait in (0.5, 1, 2, 4, 8, None):
        try:
            return path.read_bytes()
        except PermissionError as error:
            if wait is None:
                raise SampleError(f"sem permissão para ler {path.name}: {error}") from error
            time.sleep(wait)


def snapshot(workspace: Path) -> dict[str, str]:
    return {path.relative_to(workspace).as_posix(): hashlib.sha256(read_when_released(path)).hexdigest()
            for path in files_under(workspace)}


def changed_files(workspace: Path, before: dict[str, str]) -> list[str]:
    after = snapshot(workspace)
    return sorted(name for name, sha in after.items()
                  if before.get(name) != sha and not name.startswith((".claude/", ".agents/")))


def without_workspace_path(text: str, workspace: Path) -> str:
    """Tira o caminho temporário, que muda a cada execução, do texto registrado."""
    native = str(workspace)
    forms = {native, native.replace("\\", "\\\\"), workspace.as_posix(), "/" + workspace.as_posix()}
    for form in sorted(forms, key=len, reverse=True):
        text = re.sub(re.escape(form), "<workspace>", text, flags=re.I)
    return text


def transcript(task: Task, prompts: list[str], replies: list[str]) -> str:
    lines = [f"# {task.scenario.name}", "", f"- Modelo: `{task.model.name}`",
             f"- Variante: `{task.variant}`", ""]
    for number, (prompt, reply) in enumerate(zip(prompts, replies), start=1):
        lines += [f"## Usuário, turno {number}", "", prompt.strip(), "",
                  f"## Agente, turno {number}", "", reply.strip(), ""]
    return "\n".join(lines)


def execute(root: Path, task: Task) -> None:
    prompts = [turn.read_text(encoding="utf-8") for turn in task.scenario.turns]
    temporary = Path(tempfile.mkdtemp(prefix="samples-")).resolve()
    try:
        workspace = temporary / "workspace"
        seed = task.scenario.source / "workspace"
        if seed.is_dir():
            shutil.copytree(seed, workspace)
        else:
            workspace.mkdir()
        if task.model.provider == "codex" and task.variant == "with-skills":
            install_codex_skills(root, workspace)
        before = snapshot(workspace)
        started = time.monotonic()
        replies, used, raw = RUNNERS[task.model.provider](root, task, workspace, prompts)
        metrics = {name: raw.get(name, 0) for name in TOKEN_METRICS}
        metrics |= {"tool_calls": raw.get("tool_calls", 0),
                    "duration_seconds": round(time.monotonic() - started),
                    "reply_words": sum(len(reply.split()) for reply in replies),
                    "turns": len(prompts)}
        if "estimated_cost_usd" in raw:
            metrics["estimated_cost_usd"] = raw["estimated_cost_usd"]
        produced = changed_files(workspace, before)
        replies = [without_workspace_path(reply, workspace) for reply in replies]

        if task.output.exists():
            shutil.rmtree(task.output)
        task.output.mkdir(parents=True)
        (task.output / "transcript.md").write_text(transcript(task, prompts, replies),
                                                   encoding="utf-8", newline="\n")
        for name in produced:
            target = task.output / "files" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(workspace / name, target)
        record = {
            "inputs_hash": task.inputs_hash,
            "provider": task.model.provider,
            "model": task.model.model,
            "effort": task.model.effort,
            "cli_version": cli_version(CLI_NAMES[task.model.provider]),
            "skills_used": sorted(set(filter(None, used))),
            "files": produced,
            "metrics": metrics,
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        (task.output / "run.json").write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    finally:
        shutil.rmtree(temporary, ignore_errors=True)


def number(value) -> str:
    return f"{value:,}".replace(",", ".") if isinstance(value, int) else "—"


def metrics_table(scenario: Scenario, models: list[Model]) -> str:
    """Tabela das execuções registradas do cenário, na ordem de `models.toml`."""
    lines = [f"# Métricas: {scenario.name}", "",
             "Gerado por `scripts/samples.py` a partir dos `run.json`. Os tokens de entrada incluem",
             "as instruções do próprio agente; compare variantes do mesmo modelo.", "",
             "| Modelo | Variante | Entrada | Em cache | Saída | Raciocínio | Ferramentas | Tempo "
             "| Palavras | Skills usadas |",
             "|---|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for model in models:
        for variant in VARIANTS:
            try:
                record = json.loads((scenario.path / model.name / variant / "run.json")
                                    .read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            data = record.get("metrics", {})
            cells = [model.name, variant] + [number(data.get(name)) for name in TOKEN_METRICS]
            cells += [number(data.get("tool_calls")), number(data.get("duration_seconds")) + " s",
                      number(data.get("reply_words")), ", ".join(record.get("skills_used", [])) or "—"]
            lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def write_metrics(scenario: Scenario, models: list[Model]) -> None:
    (scenario.path / "METRICS.md").write_text(metrics_table(scenario, models),
                                              encoding="utf-8", newline="\n")


# ------------------------------------------------------------------------ CLI


def select(tasks: list[Task], args) -> list[Task]:
    chosen = [task for task in tasks
              if (not args.scenario or task.scenario.name in args.scenario)
              and (not args.model or task.model.name in args.model)
              and (not args.variant or task.variant == args.variant)]
    if not chosen:
        raise SampleError("nenhuma amostra corresponde aos filtros")
    return chosen


def command_run(root: Path, args) -> int:
    models = load_models(args.config)
    tasks = select(plan(root, models, load_scenarios(root)), args)
    pending = tasks if args.all else stale(tasks)
    print(f"{len(pending)} de {len(tasks)} amostras a gerar.")
    for task in pending:
        print(f"  - {task.label}")
    if args.dry_run or not pending:
        return 0

    def attempt(task: Task) -> str | None:
        try:
            execute(root, task)
            print(f"ok     {task.label}", flush=True)
            return None
        except (SampleError, OSError) as error:
            print(f"falhou {task.label}: {error}", flush=True)
            return task.label

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        failures = [label for label in pool.map(attempt, pending) if label]
    for scenario in {task.scenario.name: task.scenario for task in pending}.values():
        write_metrics(scenario, models)
    print(f"{len(pending) - len(failures)} geradas, {len(failures)} com falha.")
    return 1 if failures else 0


def command_check(root: Path, args) -> int:
    outdated = stale(plan(root, load_models(args.config), load_scenarios(root)))
    for task in outdated:
        state = "ausente" if recorded_hash(task) is None else "desatualizada"
        print(f"{state}: {task.label}")
    if outdated:
        print("Gere de novo com `python scripts/samples.py run` e inclua o resultado no commit.")
        return 1
    print("Amostras em dia.")
    return 0


def parser() -> argparse.ArgumentParser:
    main = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    main.add_argument("--config", type=Path, default=ROOT / SAMPLES / "models.toml",
                      help="arquivo com os modelos (padrão: samples/models.toml)")
    commands = main.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run", help="gera as amostras ausentes ou desatualizadas")
    run.add_argument("--scenario", action="append", help="limita a um cenário (repetível)")
    run.add_argument("--model", action="append", help="limita a um modelo (repetível)")
    run.add_argument("--variant", choices=VARIANTS, help="limita a uma variante")
    run.add_argument("--all", action="store_true", help="gera também as que estão em dia")
    run.add_argument("--dry-run", action="store_true", help="só lista o que seria gerado")
    run.add_argument("--jobs", type=int, default=2, help="execuções em paralelo (padrão: 2)")
    run.set_defaults(handler=command_run)
    check = commands.add_parser("check", help="acusa amostras ausentes ou desatualizadas")
    check.set_defaults(handler=command_check)
    return main


def main(argv=None, root: Path = ROOT) -> int:
    args = parser().parse_args(argv)
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    try:
        return args.handler(root, args)
    except SampleError as error:
        print(f"erro: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
