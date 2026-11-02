@../AGENTS.md

## Claude Code

As skills em `.claude/skills/` e `.agents/skills/` são cópias das fontes agrupadas em
`skills/<grupo>/<nome>/`. Edite as fontes e use `python scripts/sync.py` para gerar as cópias.
Os papéis em `.claude/agents/` correspondem a `.agents/roles/`; atualize-os na mesma alteração.

Acesse `planner` por `specify`, `evaluator` por `evaluate` e `representative` apenas para escolhas
dentro de uma execução autônoma autorizada. Use `delegate` para delegação autorizada.
Use modelos e ferramentas disponíveis na sessão; declare configurações não suportadas.
Preserve identificadores técnicos em inglês e escreva as orientações em português.
