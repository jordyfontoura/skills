"""Formato Markdown da política: tabelas legíveis, sem configuração externa obrigatória."""

from html import escape, unescape
import re


HEADERS = {
    "Perfis": ["Perfil", "Ordem", "Provedor", "Modelo", "Esforço"],
    "Papéis": ["Papel", "Quando usar", "Perfil", "Mapa", "Simple", "Hard"],
    "Escadas": ["Escada", "Quando usar", "Ciclos", "Etapa", "Provedor", "Modelo", "Esforço"],
}


def cell(value):
    value = escape(str(value), quote=False).replace("|", "&#124;").replace("\r", "&#13;").replace("\n", "&#10;")
    return re.sub(r"^\s+|\s+$", lambda m: "".join(f"&#{ord(c)};" for c in m[0]), value)


def serialize_markdown(policy):
    rows = {name: [] for name in HEADERS}
    for name, profile in policy["profiles"].items():
        for order, candidate in enumerate(profile["candidates"], 1):
            rows["Perfis"].append([name, order, *(candidate[k] for k in ("provider", "model", "effort"))])
    for name, role in policy["roles"].items():
        rows["Papéis"].append([name, role["when"], role["profile"], "sim" if "complexity" in role else "-",
                               role.get("complexity", {}).get("simple", "-"),
                               role.get("complexity", {}).get("hard", "-")])
    for name, ladder in policy.get("ladders", {}).items():
        for order, stage in enumerate(ladder["stages"], 1):
            rows["Escadas"].append([name, ladder["when"], ladder.get("max_cycles", "-"), order,
                                   *(stage[k] for k in ("provider", "model", "effort"))])
    lines = ["# Seleção de modelos", ""]
    for name, header in HEADERS.items():
        lines.extend([f"## {name}", "", "| " + " | ".join(header) + " |",
                      "| " + " | ".join("---" for _ in header) + " |"])
        lines.extend("| " + " | ".join(cell(v) for v in row) + " |" for row in rows[name])
        lines.append("")
    return "\n".join(lines)


def parse_markdown(text):
    policy = {"version": 2, "profiles": {}, "roles": {}}
    section = None
    seen = set()
    header_seen = False
    separator_seen = False
    for raw in text.split("\n"):
        line = raw.removesuffix("\r")
        if line.startswith("## "):
            if section in HEADERS and not separator_seen:
                raise ValueError(f"{section}: tabela ausente ou incompleta")
            section = line[3:]
            if section in HEADERS:
                if section in seen:
                    raise ValueError(f"Seção repetida: {section}")
                seen.add(section)
            header_seen = separator_seen = False
            continue
        if section not in HEADERS or not line.startswith("|"):
            continue
        if not line.rstrip().endswith("|"):
            raise ValueError(f"{section}: linha de tabela incompleta")
        row = [unescape(v.strip()) for v in line.rstrip()[1:-1].split("|")]
        if not header_seen:
            if row != HEADERS[section]:
                raise ValueError(f"{section}: colunas inválidas")
            header_seen = True
            continue
        if not separator_seen:
            if len(row) != len(HEADERS[section]) or not all(re.fullmatch(r":?-{3,}:?", v) for v in row):
                raise ValueError(f"{section}: separador inválido")
            separator_seen = True
            continue
        if len(row) != len(HEADERS[section]):
            raise ValueError(f"{section}: quantidade de colunas inválida")
        if section == "Perfis":
            name, order, provider, model, effort = row
            options = policy["profiles"].setdefault(name, {"candidates": []})["candidates"]
            if order != str(len(options) + 1):
                raise ValueError(f"{name}: ordem de candidatos inválida")
            options.append(dict(provider=provider, model=model, effort=effort))
        elif section == "Papéis":
            name, when, profile, mapping, simple, hard = row
            if name in policy["roles"]:
                raise ValueError(f"Papel repetido: {name}")
            role = dict(when=when, profile=profile)
            complexity = {k: v for k, v in (("simple", simple), ("hard", hard)) if v != "-"}
            if mapping not in ("sim", "-") or (mapping == "-" and complexity):
                raise ValueError(f"{name}: mapa de complexidade inválido")
            if mapping == "sim":
                role["complexity"] = complexity
            policy["roles"][name] = role
        else:
            name, when, cycles, order, provider, model, effort = row
            ladder = policy.setdefault("ladders", {}).setdefault(name, dict(when=when, stages=[]))
            if when != ladder["when"] or order != str(len(ladder["stages"]) + 1):
                raise ValueError(f"{name}: etapas inconsistentes")
            limit = None if cycles == "-" else int(cycles)
            if ladder["stages"] and limit != ladder.get("max_cycles"):
                raise ValueError(f"{name}: ciclos inconsistentes")
            if limit is not None:
                ladder["max_cycles"] = limit
            ladder["stages"].append(dict(provider=provider, model=model, effort=effort))
    if not {"Perfis", "Papéis"} <= seen:
        raise ValueError("Política Markdown exige Perfis e Papéis")
    if section in HEADERS and not separator_seen:
        raise ValueError(f"{section}: tabela ausente ou incompleta")
    return policy
