---
name: delegar
description: Delega trabalho autorizado e delimitado com responsabilidade clara, ferramentas disponíveis e conferência do resultado.
license: Apache-2.0
---

# Delegar trabalho delimitado

Delegue quando houver autorização e uma parte independente, com dependências satisfeitas e
resultado e responsabilidade claros. Diga o ganho esperado: trabalho em paralelo, investigação
com saída volumosa, avaliação que precisa de independência ou preservação do contexto do
coordenador. Um papel configurado não é motivo para delegar, e uma edição pequena custa menos
feita do que explicada.

Num coordenador com contexto grande ou já compactado, cada leitura, edição ou saída de teste
é paga de novo nas chamadas seguintes. Nesse caso, envie implementação, testes e leituras
longas a contextos novos e guarde decisões, integração e estado. Um pedido explícito para
trabalhar no próprio contexto prevalece.

A delegação herda os limites de permissão: revisão de código não autoriza execução, edição
nem novas delegações. Um revisor em modo de leitura devolve achados com referências.

## Escolher o modelo

Consulte o [guia de seleção de modelos](../../../knowledge/agents/model-selection.md), distribuído com esta skill.
A escolha explícita do pedido prevalece; depois vêm substituições locais declaradas e o padrão
do guia, sem exigir arquivo local. Siga também suas regras para fontes ausentes ou conflitantes.
Identifique a responsabilidade
(`orchestrator`, `planner`, `implementer`, `reviewer`, `evaluator`, `representative` ou `council`,
ou outra configurada pelo projeto) e resolva a seleção, sem precisar de scripts:

- `version = 1`: combine `defaults` com os campos do papel e siga `fallbacks` em ordem.
  Complexidade não altera a seleção.
- `version = 2`: use `roles.<papel>.profile` e os `candidates` ordenados desse perfil; não há
  `defaults` nem seleção direta nos papéis. Se o papel declarar `complexity.simple` ou
  `complexity.hard`, o nível correspondente troca o perfil; `default` e níveis sem mapa mantêm
  o perfil base. O pedido pode fixar o nível. Sem isso, classifique pelo trabalho: `simple`
  para trabalho mecânico delimitado, `hard` para diagnóstico difícil ou arquitetura com
  consequências relevantes e `default` sem motivo concreto para outro.
  `representative`, `evaluator` e `council` não aceitam mapas nem herdam a complexidade da
  implementação. Candidatos exigem provedor, modelo e esforço, sem duplicação; só o primeiro
  pode herdar provedor e modelo, sempre juntos.
- Versão, papel, perfil, campo ou nível desconhecido pede esclarecimento. Não crie vínculos
  por nomes iguais, não misture os formatos e não substitua referências ausentes.

`inherit` preserva a configuração herdada e não é nome de modelo; a complexidade não o troca
por outro. Confira o candidato principal na ferramenta e passe ao seguinte, na ordem
configurada, só quando ele estiver indisponível. Resultado ruim não autoriza trocar de modelo.
Se nenhuma opção puder executar, relate a indisponibilidade em vez de inventar um substituto.
Não apresente um modelo herdado como o modelo pedido nem troque de provedor sem informar.
A política não troca o modelo da conversa nem autoriza delegar.

Leia [workloads.md](workloads.md) para trabalho recorrente, registros e comparações autorizadas.

## Preparar a tarefa

O brief traz o resultado esperado, os requisitos e as provas exigidas; os arquivos para ler
e a revisão das entradas; a responsabilidade por arquivos ou por análise de leitura, com ações
permitidas e exclusões; e o retorno pedido: resultado, arquivos alterados, evidências e
incerteza restante, de forma concisa.

Inclua o que já existe, para evitar retrabalho: as evidências coletadas, com revisão e origem,
separando fatos conferidos de interpretações e lacunas; e o resultado de base das verificações,
com comando, revisão, ambiente e resultado, para o agente rodar só as focadas. Havendo
política, informe responsabilidade, versão, perfil efetivo, alternativa usada e complexidade,
com sua origem e se ela mudou a seleção; na v1, só os campos que existem. Modelo e esforço
entram só quando selecionados ou observados.

Delimite a pergunta em vez de pedir uma nova investigação geral, mas deixe o agente conferir
fontes e questionar premissas: um resumo fornecido não prova que a origem foi validada. Para
pareceres de `conselho`, o brief é só ponto de partida; vale a prioridade de qualidade,
cobertura e investigação independente daquela skill.

Para edições, avise que o agente não está sozinho e deve preservar mudanças alheias. Distribua
arquivos distintos ou use ambientes de trabalho isolados; arquivos compartilhados são editados
em sequência, a partir de uma base recuperável. Enquanto o agente trabalha, não duplique o
trabalho dele: guarde o identificador e a forma de receber o resultado, avance o que for
independente e relate só mudanças de estado.

## Conferir o retorno

"Concluído" não é evidência. Confira os achados contra a fonte, na revisão fixada. Numa entrega,
inspecione o diff e o resultado registrado de cada prova, com comando, revisão e resultado
observado, e rode de novo só o que faltar, estiver inconsistente ou tiver sido invalidado por
mudanças posteriores. O aceite independente, quando exigido, executa as próprias verificações.

Integre sem reverter trabalho alheio. Devolva trabalho incompleto como uma tarefa menor.
Após duas correções sem sucesso, ou quando variantes do mesmo defeito reaparecerem, use
`diagnosticar`. Ao registrar, separe configurações pedidas, informadas pela ferramenta e
observadas; uso não informado continua desconhecido.
