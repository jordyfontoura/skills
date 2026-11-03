@../AGENTS.md

## Claude Code

As skills em `.claude/skills/` e `.agents/skills/` são cópias das fontes agrupadas em
`skills/<grupo>/<nome>/`. Edite as fontes e use `python scripts/sync.py` para gerar as cópias.
Os papéis em `.claude/agents/` correspondem a `.agents/roles/`; atualize-os na mesma alteração.

Acesse `planner` por `especificar`, `evaluator` por `verificar-aceite` e `representative` apenas para escolhas
dentro de uma execução autônoma autorizada. Use `delegar` para delegação autorizada.
Use modelos e ferramentas disponíveis na sessão; declare configurações não suportadas.
Use nomes de skills em português, preserve os demais identificadores técnicos em inglês e
escreva as orientações em português.
