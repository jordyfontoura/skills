"""Prova cruzada de políticas emitidas pelo CLI; usado só nos testes da origem."""

import json
import sys
import tomllib

from model_policy import validate_policy


def main():
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    cases = json.load(sys.stdin)
    for case in cases:
        parsed = tomllib.loads(case["toml"])
        if parsed != case["policy"]:
            raise ValueError(f"Serialização mudou a política: {case['name']}")
        validate_policy(parsed)
    print(f"OK: {len(cases)} políticas aceitas pelo validador Python, sem perda na serialização")


if __name__ == "__main__":
    main()
