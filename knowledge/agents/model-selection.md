# Seleção de modelos

- **Aplicabilidade:** novas consultas e delegações autorizadas, inclusive `subir-regua`.
- **Origem:** preferências pessoais aprovadas do mantenedor, migradas em 21/11/2026.
- **Limites:** estas listas não comprovam disponibilidade, desempenho ou esforço aceito.
  Não autorizam delegação ou representação e não trocam o modelo da conversa aberta.

## Precedência e ausência de configuração

Use primeiro as escolhas explícitas do pedido. Depois, aplique substituições declaradas
nas instruções do projeto ou em `.agents/models.md`. Uma política legada em
`.agents/models.toml` continua sendo uma personalização local; preserve-a. Se as fontes
locais conflitarem sem precedência declarada, esclareça o conflito antes de delegar.
Para papéis, perfis ou escadas não substituídos localmente, use este documento.
Não exija um arquivo local para aplicar o padrão distribuído com as skills.

No plugin completo, este guia fica em `knowledge/agents/model-selection.md`; pelo CLI,
em `knowledge/harness/agents/model-selection.md`. Siga o link da skill instalada,
sem procurar cópias em artefatos, outros projetos ou na pasta pessoal.
Se o guia estiver ausente e não houver seleção aplicável no pedido ou no projeto,
informe a lacuna e peça a escolha necessária. Não invente modelos, etapas ou esforços.

## Resolver um papel

Identifique o papel e a complexidade do trabalho: `default` sem motivo concreto para outro
nível; `simple` para edições mecânicas delimitadas; `hard` para diagnóstico difícil ou decisões
de arquitetura com consequências relevantes. O pedido pode fixar o nível.
Use o perfil base do papel, salvo substituição explícita nas colunas Simple ou Hard.
`evaluator`, `roles.council` e `representative` têm seleção própria, sem mapas de complexidade.
Planejamento rotineiro continua na conversa; um papel configurado não exige outro agente.

No perfil escolhido, tente os candidatos na ordem indicada. Confira provedor, modelo e
esforço na ferramenta real. Só use a próxima alternativa por indisponibilidade e dentro da
autorização atual; resultado ruim não autoriza trocar de modelo. Uma escolha exigida pelo
usuário não admite substituição automática. Sem candidato elegível, relate o limite.
`inherit` preserva o ambiente: provedor e modelo devem ser herdados juntos; alternativas
exigem IDs concretos. O esforço pode herdar o ambiente em qualquer candidato.
Os IDs abaixo correspondem ao T3 Code usado pelo mantenedor; outro ambiente pode não
oferecê-los. Não adivinhe equivalências nem afirme que um modelo foi executado sem evidência.

Registre a fonte, papel, perfil, complexidade quando mudar a seleção, eventual alternativa
e modelo/esforço pedidos versus observados. Dados não expostos pela ferramenta ficam desconhecidos.

## Usar uma escada

Use a sequência explícita do pedido; depois a escada nomeada, resolvida pela precedência
acima; sem nome, use `padrao`. As etapas são sequenciais: não são alternativas.
Confira os modelos e esforços antes de começar. Uma etapa indisponível fica pendente;
não substitua, pule ou reduza a escada. O limiar de aprovação vem do pedido, nunca desta tabela.
O limite de ciclos vem do pedido, depois da coluna Ciclos; sem ambos, use 3 por etapa.
A ordem é uma preferência do usuário, não uma classificação comprovada de qualidade.

## Formato e personalização

Edite as tabelas abaixo para alterar o padrão do harness. O CLI leva este guia como dependência
das skills que o consultam, sem exigir `--models`. Atualizações preservam adaptações locais.
Para personalizar um projeto, declare somente as substituições necessárias em suas instruções
ou use `models init` para criar `.agents/models.md`. O CLI não sobrescreve políticas existentes
nem migra TOML automaticamente. Um arquivo local parcial substitui somente entradas declaradas;
uma entrada inválida é erro, não um motivo para aplicar silenciosamente o padrão.

As tabelas também são verificadas por ferramentas de manutenção. Preserve os títulos e colunas;
Ordem e Etapa começam em 1 e são consecutivas em cada lista. `-` indica ausência de substituição
ou limite. Mapa `sim` declara um mapa de complexidade, inclusive vazio. Dentro das células,
use entidades HTML para barras verticais ou quebras de linha. Novas políticas usam o contrato
v2 de perfis e papéis; o leitor de TOML v1/v2 permanece para compatibilidade.

## Perfis

| Perfil | Ordem | Provedor | Modelo | Esforço |
| --- | --- | --- | --- | --- |
| simple | 1 | codex | gpt-6-luna | medium |
| simple | 2 | claudeAgent | claude-haiku-5-5 | medium |
| default | 1 | codex | gpt-6.1-sol | medium |
| default | 2 | claudeAgent | claude-sonnet-5-5 | high |
| hard | 1 | claudeAgent | claude-opus-5-5 | high |
| hard | 2 | codex | gpt-6.1-sol | high |
| orchestrator | 1 | claudeAgent | claude-opus-5-5 | high |
| orchestrator | 2 | codex | gpt-6.1-sol | high |
| representative | 1 | claudeAgent | claude-opus-5-5 | high |
| representative | 2 | codex | gpt-6.1-sol | high |
| evaluator | 1 | claudeAgent | claude-opus-5-5 | high |
| evaluator | 2 | codex | gpt-6.1-sol | high |

## Papéis

| Papel | Quando usar | Perfil | Mapa | Simple | Hard |
| --- | --- | --- | --- | --- | --- |
| orchestrator | Organizar trabalho autorizado, distribuir responsabilidades e integrar resultados. | orchestrator | - | - | - |
| planner | Resolver incertezas relevantes de comportamento e planejar uma entrega, quando autorizado. | default | sim | simple | hard |
| implementer | Implementar uma parte delimitada, com arquivos e provas definidos. | default | sim | simple | hard |
| reviewer | Revisar um diff fixo, respeitando os limites de leitura e execução. | default | sim | simple | hard |
| evaluator | Verificar os critérios de aceite independentemente de quem implementou. | evaluator | - | - | - |
| representative | Resolver escolhas dentro de uma execução autônoma em que o usuário autorizou representação. | representative | - | - | - |
| council | Consultar especialistas independentes numa análise multidisciplinar autorizada. | evaluator | - | - | - |

## Escadas

| Escada | Quando usar | Ciclos | Etapa | Provedor | Modelo | Esforço |
| --- | --- | --- | --- | --- | --- | --- |
| padrao | Subir a régua com avaliadores de famílias alternadas até a última etapa aprovar. | 3 | 1 | codex | gpt-6-luna | xhigh |
| padrao | Subir a régua com avaliadores de famílias alternadas até a última etapa aprovar. | 3 | 2 | claudeAgent | claude-haiku-5-5 | xhigh |
| padrao | Subir a régua com avaliadores de famílias alternadas até a última etapa aprovar. | 3 | 3 | codex | gpt-6.1-sol | medium |
| padrao | Subir a régua com avaliadores de famílias alternadas até a última etapa aprovar. | 3 | 4 | claudeAgent | claude-opus-5-5 | medium |
| padrao | Subir a régua com avaliadores de famílias alternadas até a última etapa aprovar. | 3 | 5 | claudeAgent | claude-fable-5-2 | medium |
