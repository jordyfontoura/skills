# Uso observado das skills

Retrato de **185 conversas pessoais do autor**, consultadas no T3 Code
em 02/11/2026, com corte às 12h17 (Brasília). Inclui histórico anterior a essa data.

## Como foi contado

- **Pedidos do usuário:** chamadas diretas pelo nome da skill, como `$progress`,
  `/write-goal` ou uma frase explícita pedindo seu uso. São pedidos, sem comprovação de execução.
- **Uso declarado pelo agente:** mensagens em que o agente anuncia ou relata usar uma skill.
  Inclui o atendimento a pedidos do usuário; não mede apenas iniciativa própria.
- Cada skill conta uma vez por mensagem. Repetições em mensagens diferentes contam novamente.
- A coluna **Threads** conta conversas distintas e não determina a ordem do ranking.
- Os grupos podem se sobrepor. Seus totais não devem ser somados como execuções distintas.

Foram excluídos catálogos, citações, sugestões de uso futuro e pedidos para editar a própria
skill. No ranking humano, também ficaram de fora regras embutidas em goals e automações.
Usos silenciosos e atividades internas de subagentes não foram contados. Nomes antigos
diferentes não foram agregados aos atuais. Zero significa ausência de registro neste critério.

A amostra depende das conversas disponíveis e da identificação das declarações. Não é
telemetria de execução nem uma medida da utilidade ou da qualidade de cada skill.

## Pedidos do usuário

| Skill | Ocorrências | Threads |
| --- | ---: | ---: |
| `write-goal` | 26 | 16 |
| `interview` | 23 | 15 |
| `council` | 22 | 11 |
| `research` | 19 | 9 |
| `propose` | 15 | 9 |
| `progress` | 4 | 1 |
| `prototype` | 3 | 1 |
| `unslop` | 2 | 2 |
| `architecture-review` | 1 | 1 |
| `clarify` | 1 | 1 |
| `delegate` | 1 | 1 |
| `interview-async` | 1 | 1 |
| `setup-harness` | 1 | 1 |
| `update-harness` | 1 | 1 |
| `address-review` | 0 | 0 |
| `diagnose` | 0 | 0 |
| `evaluate` | 0 | 0 |
| `handoff` | 0 | 0 |
| `implement` | 0 | 0 |
| `improve-harness` | 0 | 0 |
| `integrate` | 0 | 0 |
| `pull-request` | 0 | 0 |
| `reconcile` | 0 | 0 |
| `review` | 0 | 0 |
| `specify` | 0 | 0 |
| `toolbox` | 0 | 0 |

## Uso declarado pelo agente

| Skill | Ocorrências | Threads |
| --- | ---: | ---: |
| `delegate` | 46 | 16 |
| `implement` | 43 | 19 |
| `diagnose` | 42 | 15 |
| `specify` | 34 | 13 |
| `unslop` | 24 | 19 |
| `evaluate` | 22 | 10 |
| `interview` | 18 | 12 |
| `council` | 15 | 8 |
| `write-goal` | 15 | 10 |
| `handoff` | 14 | 11 |
| `setup-harness` | 13 | 13 |
| `propose` | 10 | 6 |
| `research` | 8 | 5 |
| `progress` | 7 | 2 |
| `address-review` | 5 | 2 |
| `review` | 4 | 3 |
| `update-harness` | 3 | 2 |
| `prototype` | 2 | 1 |
| `reconcile` | 2 | 1 |
| `toolbox` | 2 | 2 |
| `improve-harness` | 1 | 1 |
| `integrate` | 1 | 1 |
| `interview-async` | 1 | 1 |
| `architecture-review` | 0 | 0 |
| `clarify` | 0 | 0 |
| `pull-request` | 0 | 0 |

## Atualizar o retrato

Os números agregados estão em [data/skill-usage.json](data/skill-usage.json).
Para publicar uma nova análise, atualize os dados e a data de corte e gere os gráficos
e esta tabela a partir da raiz do repositório:

```bash
python scripts/render_skill_usage.py
```

O comando só gera os arquivos locais; não consulta conversas nem atualiza as contagens.
