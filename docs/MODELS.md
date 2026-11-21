# Modelos por papel e complexidade

A fonte principal é o [guia de seleção de modelos](../knowledge/agents/model-selection.md).
Ele reúne candidatos ordenados, esforço, papéis, complexidade, precedência e a escada de
`subir-regua`. O plugin o inclui em `knowledge/`; o CLI instala o guia uma vez em
`knowledge/harness/`, como dependência das skills, sem exigir uma política local.

Para exemplos de aplicação, veja [o fluxo de seleção](MODEL-FLOW.md).

## Personalizar um projeto

O pedido explícito prevalece, seguido das substituições locais e do padrão do guia.
Declare substituições no `AGENTS.md`/`CLAUDE.md` do projeto ou em `.agents/models.md`.
Não edite o guia distribuído para registrar uma preferência específica do projeto.
Políticas antigas `.agents/models.toml` v1/v2 continuam válidas como substituições locais;
atualizar as skills não exige migrá-las. Se duas fontes locais conflitarem, esclareça a prioridade.

O [configurador do CLI](../cli/README.md#configurar-modelos) cria `.agents/models.md`,
com herança do ambiente, um modelo compartilhado ou perfis separados. `--config arquivo.json`
aceita o contrato v2 e produz tabelas Markdown; `--print` mostra a proposta sem gravar.
Arquivos existentes são preservados. O CLI também preserva e reconhece a política TOML legada,
sem criar outra política concorrente. Não há migração automática.

## Escadas de `subir-regua`

A sequência padrão está somente no guia. Cada linha declara escada, finalidade, limite de
ciclos, etapa, provedor, modelo e esforço. Uma etapa indisponível interrompe a sequência;
alternativas de perfis não substituem etapas. O critério de aprovação vem do pedido.
Uma política personalizada gerada com `--config` pode incluir `ladders`; as perguntas
interativas configuram papéis e perfis, sem criar uma escada local.

## Contrato e verificações

Novas políticas usam o contrato v2: `profiles` com `candidates` ordenados e `roles` com
`when`, `profile` e mapa opcional `complexity.simple`/`complexity.hard`. `default` usa o
perfil base; `evaluator`, `roles.council` e `representative` não aceitam mapas. A seção opcional
`ladders` contém `when`, `stages` e `max_cycles` opcional. Etapas exigem IDs concretos.
O guia explica as colunas Markdown correspondentes. Campos desconhecidos, referências
inexistentes, listas vazias, duplicações e herança incompatível continuam sendo erros.

`scripts/model_policy.py` lê Markdown e TOML legado; `resolve_policy` e `resolve_ladder`
consultam a política sem executar modelos. A v1 combina `defaults`, campos do papel e
`fallbacks`; a v2 resolve perfis e mapas. Os validadores não consultam provedores.
`python scripts/check.py` confere a fonte Markdown, os papéis e as cópias dos provedores.
Os testes Python e do CLI cobrem resolução, serialização, preservação e distribuição.
Disponibilidade e esforço realmente aceitos exigem conferência em cada execução.

Configurar modelos não autoriza delegação ou representação nem muda o modelo da conversa.
O representante só decide dentro da autonomia explicitamente autorizada e não amplia o objetivo.
Uma espera pedida por `propor` continua valendo, salvo delegação explícita daquela decisão.
