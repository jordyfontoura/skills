"""Valida a política local e consulta opções por responsabilidade, sem executar modelos."""

from pathlib import Path
import re
import tomllib


TARGET_FIELDS = {"provider", "model", "effort"}
COMPLEXITIES = {"simple", "default", "hard"}
FIXED_ROLES = {"representative", "evaluator", "council"}


def identifier(value, location):
    if not isinstance(value, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        raise ValueError(f"{location}: nome inválido")


def candidates(options, location):
    if not isinstance(options, list) or not options:
        raise ValueError(f"{location}: deve conter uma lista não vazia")
    seen = set()
    for index, option in enumerate(options):
        item = target(option, f"{location}[{index}]", concrete=index > 0)
        identity = tuple(item[k] for k in sorted(TARGET_FIELDS))
        if identity in seen:
            raise ValueError(f"{location}: alternativa repetida")
        seen.add(identity)


def fields(value, allowed, required, location):
    if not isinstance(value, dict):
        raise ValueError(f"{location}: deve ser uma tabela")
    if set(value) - allowed:
        raise ValueError(f"{location}: campos desconhecidos: {', '.join(sorted(set(value) - allowed))}")
    if required - set(value):
        raise ValueError(f"{location}: campos ausentes: {', '.join(sorted(required - set(value)))}")


def target(value, location, concrete=False):
    fields(value, TARGET_FIELDS, TARGET_FIELDS, location)
    for key in TARGET_FIELDS:
        item = value[key]
        if not isinstance(item, str) or not item.strip() or item != item.strip():
            raise ValueError(f"{location}.{key}: deve ser texto não vazio, sem espaços nas extremidades")
    provider_inherited = value["provider"] == "inherit"
    model_inherited = value["model"] == "inherit"
    if provider_inherited != model_inherited:
        raise ValueError(f"{location}: provider e model devem ser herdados ou definidos juntos")
    if concrete and model_inherited:
        raise ValueError(f"{location}: uma alternativa deve identificar provider e model concretos")
    return dict(value)


def validate_policy(policy, required_roles=()):
    if not isinstance(policy, dict) or type(policy.get("version")) is not int or policy["version"] not in (1, 2):
        raise ValueError("política.version: versão não suportada")
    if policy["version"] == 2:
        return validate_profiles(policy, required_roles)
    fields(policy, {"version", "defaults", "roles"}, {"version", "defaults", "roles"}, "política")
    if type(policy["version"]) is not int or policy["version"] != 1:
        raise ValueError("política.version: versão não suportada")
    defaults = target(policy["defaults"], "defaults")
    roles = policy["roles"]
    if not isinstance(roles, dict) or not roles:
        raise ValueError("roles: deve conter ao menos uma responsabilidade")
    missing = set(required_roles) - set(roles)
    if missing:
        raise ValueError(f"Responsabilidades sem configuração: {', '.join(sorted(missing))}")
    for name, role in roles.items():
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            raise ValueError(f"roles.{name}: nome inválido")
        location = f"roles.{name}"
        fields(role, TARGET_FIELDS | {"when", "fallbacks"}, {"when", "fallbacks"}, location)
        if not isinstance(role["when"], str) or not role["when"].strip():
            raise ValueError(f"{location}.when: explique quando usar esta responsabilidade")
        primary = target({**defaults, **{k: v for k, v in role.items() if k in TARGET_FIELDS}}, location)
        if not isinstance(role["fallbacks"], list):
            raise ValueError(f"{location}.fallbacks: deve ser uma lista ordenada")
        seen = {tuple(primary[k] for k in sorted(TARGET_FIELDS))}
        for index, fallback in enumerate(role["fallbacks"]):
            option = target(fallback, f"{location}.fallbacks[{index}]", concrete=True)
            identity = tuple(option[k] for k in sorted(TARGET_FIELDS))
            if identity in seen:
                raise ValueError(f"{location}.fallbacks: alternativa repetida")
            seen.add(identity)
    return policy


def validate_profiles(policy, required_roles):
    fields(policy, {"version", "profiles", "roles"}, {"version", "profiles", "roles"}, "política")
    profiles = policy["profiles"]
    if not isinstance(profiles, dict) or not profiles:
        raise ValueError("profiles: deve conter ao menos um perfil")
    for name, profile in profiles.items():
        location = f"profiles.{name}"
        identifier(name, location)
        fields(profile, {"candidates"}, {"candidates"}, location)
        candidates(profile["candidates"], f"{location}.candidates")

    def reference(value, location):
        identifier(value, location)
        if value not in profiles:
            raise ValueError(f"{location}: perfil sem configuração: {value}")

    roles = policy["roles"]
    if not isinstance(roles, dict) or not roles:
        raise ValueError("roles: deve conter ao menos uma responsabilidade")
    missing = set(required_roles) - set(roles)
    if missing:
        raise ValueError(f"Responsabilidades sem configuração: {', '.join(sorted(missing))}")
    for name, role in roles.items():
        location = f"roles.{name}"
        identifier(name, location)
        fields(role, {"when", "profile", "complexity"}, {"when", "profile"}, location)
        if not isinstance(role["when"], str) or not role["when"].strip():
            raise ValueError(f"{location}.when: explique quando usar esta responsabilidade")
        reference(role["profile"], f"{location}.profile")
        if "complexity" in role:
            if name in FIXED_ROLES:
                raise ValueError(f"{location}: papel não aceita mapa de complexidade")
            fields(role["complexity"], {"simple", "hard"}, set(), f"{location}.complexity")
            for level, profile in role["complexity"].items():
                reference(profile, f"{location}.complexity.{level}")
    return policy


def load_policy(path, required_roles=()):
    policy = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    return validate_policy(policy, required_roles)


def resolve_policy(policy, role, complexity="default"):
    validate_policy(policy)
    if not isinstance(complexity, str) or complexity not in COMPLEXITIES:
        raise ValueError("complexity: nível desconhecido; use simple, default ou hard")
    if role not in policy["roles"]:
        raise ValueError(f"Responsabilidade sem configuração: {role}")
    settings = policy["roles"][role]
    if policy["version"] == 2:
        overrides = settings.get("complexity", {})
        profile = overrides.get(complexity, settings["profile"])
        return {
            "role": role,
            "when": settings["when"],
            "profile": profile,
            "complexity": complexity,
            "complexity_applied": complexity in overrides and profile != settings["profile"],
            "candidates": [dict(item) for item in policy["profiles"][profile]["candidates"]],
        }
    primary = {**policy["defaults"], **{k: v for k, v in settings.items() if k in TARGET_FIELDS}}
    return {
        "role": role,
        "when": settings["when"],
        "candidates": [primary, *(dict(item) for item in settings["fallbacks"])],
    }
