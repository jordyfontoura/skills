# Registrar verificações com a Bateia

Leia quando as instruções do projeto (`AGENTS.md` ou `CLAUDE.md`) declararem a Bateia para
registrar verificações, com o comando a usar e o contrato `HC-*`. Sem essa declaração, este apoio
não se aplica: siga o fluxo da skill sem exigir nem citar o executável.

A Bateia executa um comando, registra fatos sobre a execução e não emite veredito. Quem aplica as
regras abaixo é o agente. O texto canônico do contrato e o schema das tags pertencem à Bateia;
este apoio reproduz o necessário para usá-lo.

## Contrato e compatibilidade

- Contrato: `HC-2026-11-12`. Registros compatíveis têm `schema_version: "0.1"`.
- `bateia --version` imprime exatamente `bateia <versão>`, e a versão precisa ser ≥ `0.1.0`,
  comparando os números de `MAJOR.MINOR.PATCH`.
- Registro com outra `schema_version` é "não suportado": não serve de prova e é relatado como tal.
- Uma declaração com outro `HC-*` não é atendida por este apoio; trate-a como incompatibilidade.

## Ativação e falha de ambiente

A declaração do projeto informa o comando da Bateia (um programa do `PATH` ou um caminho) e o
`HC-*`. Pode também predeclarar verificações mecânicas sem contagem, com o argv e o diretório de
execução de cada uma.

Antes da primeira evidência, execute o exemplo `version` e confira formato e versão. Com a Bateia
indisponível (código `127`, `bateia_error`) ou incompatível, relate falha de ambiente e mantenha
os critérios sem prova (`UNPROVED`). Não volte ao fluxo genérico em silêncio: não há fallback.
Uma execução direta do comando pode ajudar no diagnóstico, mas não serve de evidência no fluxo
declarado. Voltar ao fluxo genérico exige retirar a declaração do projeto.

## Tags

Passe as tags por `--tag <chave>=<valor>`. A variável `BATEIA_TAG_<CHAVE EM MAIÚSCULAS>` produz a
mesma tag (`BATEIA_TAG_HARNESS_TASK` vira `harness_task`); em conflito, `--tag` vence. As tags são
gravadas antes do registro de início e constam também de um registro `incomplete`.

| Chave | Obrigatória no fluxo integrado | Valor |
| --- | --- | --- |
| `harness_contract` | sim | `HC-2026-11-12` |
| `harness_rev` | sim | SHA de 40 hex do registro de adoção do projeto; senão `plugin:<versão>`; senão `unknown` |
| `harness_task` | sim | identificador estável da tarefa no registro oficial do projeto (ex.: `HI-T03`); sem registro, um slug declarado no brief e mantido na passagem |
| `harness_attempt` | sim | inteiro decimal ≥ 1; nova tentativa começa quando uma avaliação reprova ou a abordagem é refeita |
| `harness_role` | sim | `implementer`, `reviewer`, `evaluator` ou `other` |
| `harness_eval` | só com `harness_role=evaluator` | inteiro ≥ 1, ordinal da avaliação dentro da tentativa |
| `harness_model` | sim | modelo exposto pelo runtime ou pela ferramenta de delegação; senão `unknown` |
| `harness_effort` | sim | esforço exposto pelo runtime ou pela ferramenta; senão `unknown` |

- Todos os valores são texto. Valores nunca contêm caminho absoluto, segredo, nome pessoal ou id
  de thread; nunca são inferidos de nome de papel, de política ou de perfil. `unknown` é
  permitido; valor inventado é defeito.
- `harness_attempt` e `harness_eval` usam a forma canônica, em decimal sem zeros à esquerda
  (`1`, não `01`), porque `runs --tag` compara textos. `harness_eval` em outro papel é permitido
  e ignorado.
- `harness_rev` vem do registro de adoção do harness no projeto (SHA incorporado) ou da versão do
  plugin instalado. Não use o SHA do próprio projeto, o da Bateia nem o de uma revisão que ainda
  não exista; sem fonte, use `unknown`.
- `harness_model` e `harness_effort` vêm do que o runtime ou a ferramenta de delegação expõe para
  o contexto que executa. Nome de perfil, papel ou entrada da política de modelos não é observação.
- Versão e árvore vêm da procedência do registro (`provenance.git.commit/tree/dirty/tree_end`);
  sessão, de `session.id`/`session_source`; versão e esquema da Bateia, de `bateia_version` e
  `schema_version`. Nada disso é duplicado em tags.
- As tags são declaradas pelo consumidor, não autenticadas pela Bateia. Encontrar tags
  `evaluator` num registro não comprova quem o executou.

## Comandos

Cada exemplo é o argv de um comando, como array JSON, num bloco com identificador próprio.
Para executar um exemplo:

1. Substitua cada marcador `<...>` pelo valor real. Nenhum marcador pode sobrar.
2. Troque o primeiro elemento, `bateia`, pelo comando declarado pelo projeto. Se a declaração
   tiver vários elementos, use todos, na ordem.
3. Passe cada elemento como um único argumento. Na shell, coloque entre aspas um elemento com
   espaço ou caractere especial, como um caminho de executável com espaços ou `<revision>^{tree}`;
   no PowerShell, chame um executável entre aspas com `&`. Não use continuação de linha com `\`.

| Marcador | Valor |
| --- | --- |
| `<harness_rev>` | valor da tag `harness_rev` conforme a tabela |
| `<harness_task>` | identificador ou slug da tarefa |
| `<harness_attempt>` | número da tentativa, sem zeros à esquerda |
| `<harness_eval>` | ordinal da avaliação, sem zeros à esquerda |
| `<revision>` | revisão cuja árvore é conferida |

Os exemplos usam `unknown` em `harness_model` e `harness_effort`. Troque pelos valores expostos
pelo runtime ou pela ferramenta quando existirem. O comando verificado nos exemplos é
`cargo test --locked`; use o comando de teste do projeto.

Conferir disponibilidade e versão:

```json version
["bateia", "--version"]
```

Registrar uma verificação de quem implementa:

```json run-implementer
["bateia", "run", "--json", "--tag", "harness_contract=HC-2026-11-12", "--tag", "harness_rev=<harness_rev>", "--tag", "harness_task=<harness_task>", "--tag", "harness_attempt=<harness_attempt>", "--tag", "harness_role=implementer", "--tag", "harness_model=unknown", "--tag", "harness_effort=unknown", "--", "cargo", "test", "--locked"]
```

Registrar a verificação de uma avaliação:

```json run-evaluator
["bateia", "run", "--json", "--tag", "harness_contract=HC-2026-11-12", "--tag", "harness_rev=<harness_rev>", "--tag", "harness_task=<harness_task>", "--tag", "harness_attempt=<harness_attempt>", "--tag", "harness_role=evaluator", "--tag", "harness_eval=<harness_eval>", "--tag", "harness_model=unknown", "--tag", "harness_effort=unknown", "--", "cargo", "test", "--locked"]
```

Registrar uma verificação mecânica sem contagem, somente se o método do critério ou o projeto a
declarou como tal antes da execução, com este argv e na raiz do repositório:

```json run-mechanical
["bateia", "run", "--json", "--tag", "harness_contract=HC-2026-11-12", "--tag", "harness_rev=<harness_rev>", "--tag", "harness_task=<harness_task>", "--tag", "harness_attempt=<harness_attempt>", "--tag", "harness_role=evaluator", "--tag", "harness_eval=<harness_eval>", "--tag", "harness_model=unknown", "--tag", "harness_effort=unknown", "--", "cargo", "fmt", "--check"]
```

Listar os registros de uma tarefa, para retomada:

```json runs-task
["bateia", "runs", "--tag", "harness_task=<harness_task>", "--json"]
```

Listar os registros de uma avaliação:

```json runs-evaluation
["bateia", "runs", "--tag", "harness_task=<harness_task>", "--tag", "harness_attempt=<harness_attempt>", "--tag", "harness_role=evaluator", "--tag", "harness_eval=<harness_eval>", "--json"]
```

Obter a árvore de uma revisão para comparar com `provenance.git.tree`:

```json tree
["git", "rev-parse", "<revision>^{tree}"]
```

## Regras de evidência

Aplicadas por agentes, nunca pela Bateia.

- E1a Testes: só `state: ok` pode apoiar a evidência de execução de testes, e nunca sozinho.
- E1b Verificação mecânica sem contagem, declarada como tal pelo método do critério ou pelo projeto
  antes da execução: o registro pode apoiar apenas o fato de que o comando declarado terminou com zero
  na árvore candidata. Exige conclusão, `state: unrecognized`, `state_reasons` exatamente
  `["no_recognized_runner"]`, `tests.detected_runners` vazio, `exit.code: 0`, argv igual ao declarado,
  E2 e E5. O relato diz "unrecognized (sem contagem); verificação mecânica com código 0".
  Isso não é aprovação global nem prova de testes. Comandos de teste não podem ser reclassificados
  como mecânicos após o resultado; truncamento, filtros, vários executores e motivos desconhecidos recusam E1b.
- E2 Um registro apoia a revisão `R` somente se `provenance.git.tree` = `git rev-parse R^{tree}`.
  `tree_end` diferente de `tree` é relatado (o comando alterou arquivos rastreados).
- E3 `no_tests`, `unrecognized`, `timed_out`, `interrupted`, `bateia_error` e estado desconhecido
  nunca apoiam aprovação de testes; relata-se estado, código e trecho do log. A exceção estrita E1b
  só apoia o fato mecânico predeclarado, sem interpretar o estado como sucesso global.
- E4 `incomplete` é desconhecido (em andamento ou morto, L-07); nunca é sucesso nem falha do produto.
  Na retomada, a verificação é repetida.
- E5 O avaliador só usa como prova registros com `harness_role=evaluator` e o seu `harness_eval`;
  registros de outros papéis podem ser citados como contexto, nunca como prova.
- E6 O log é lido por trecho a partir de `log.path`; não se relê inteiro um log já salvo.

Notas de aplicação:

- E1a: confira também `exit.code` e as contagens de testes do registro; zero testes não é
  aprovação. O registro apoia a evidência junto de E2 e, na avaliação, de E5.
- E1b: o argv comparado é `command.argv` persistido, com `command.argv_lossy: false`. Caminhos
  absolutos em argumentos são redigidos no registro; declare o comando com caminhos relativos à
  raiz ou programas do `PATH` para que a igualdade possa ser conferida. `command.cwd` precisa ser
  igual ao diretório predeclarado, relativo à raiz (`.` quando a declaração não indicar outro).
  Sem igualdade conferida de argv e diretório, E1b não se aplica.
- E5: a avaliação própria é identificada pelo trio `harness_task`, `harness_attempt` e
  `harness_eval`, com `harness_role=evaluator`. Papel e ordinal sem a tarefa e a tentativa não
  bastam. A autoria é conferida pela execução própria e pelo relatório do avaliador.
- Cada execução é relatada com id, `state`, `exit.code`, árvore curta (início de
  `provenance.git.tree`), `dirty` e `log.path`. Com `dirty: true`, a árvore registrada inclui
  alterações não commitadas e só apoia uma revisão se a igualdade de E2 se confirmar.

## Uso por skill

- `implementar`: execute por `bateia run`, com as tags e `harness_role=implementer`, cada
  verificação citada como evidência. Relate os campos de cada execução e nunca declare sucesso
  fora de E1. O registro de quem implementa não comprova aceite independente.
- `verificar-aceite`: em contexto independente, gere as próprias execuções na revisão fixada, com
  `harness_role=evaluator` e o seu `harness_eval`. Para cada critério, cite os ids que satisfazem
  E1, E2 e E5 e confira árvore, `schema_version` e versão. Registros de outra árvore ou de outro
  papel são contexto, nunca prova. `PASS` exige prova para todos os critérios exigidos.
- `passar-contexto`: inclua `harness_task`, `harness_attempt` e os ids relevantes com estado e
  árvore curta, dizendo se a árvore coincide com a revisão atual. Marque `incomplete` como
  desconhecido, a reexecutar na retomada, e indique a consulta `runs-task`. Não transfira prova
  entre árvores.

Relate os campos das execuções na conversa ou nos registros do projeto. Não copie caminhos
locais, ids de sessão ou trechos de log com dados pessoais para documentos públicos.
