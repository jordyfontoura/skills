---
name: propor
description: Apresenta uma abordagem concreta e aguarda aprovação antes de executar, quando o usuário menciona `propor`, pede uma proposta antes da ação ou pede para explicar o que será feito antes de agir. Permite investigação de leitura, sem alterar arquivos ou sistemas.
license: Apache-2.0
---

# Propor antes de executar

Use quando o usuário pedir uma proposta antes da ação. A menção a esta skill define uma etapa
de explicação e revisão, mesmo se o restante do pedido descrever algo a implementar.
Não transforme todo pedido comum numa aprovação obrigatória; este modo atende à espera
solicitada pelo usuário.

## Entender sem alterar

Leia o pedido, as instruções relevantes, as decisões existentes e os arquivos necessários
para propor algo viável. Use ferramentas de leitura e investigação dentro do escopo permitido.
Não peça ao usuário fatos que você pode conferir. Se uma escolha importante continuar aberta,
explique a dúvida e as opções; use os princípios de `entrevistar` sem reiniciar decisões resolvidas.

Nesta etapa, não edite nem crie arquivos, mude configurações, crie branches ou worktrees,
faça commits, instale dependências, gere protótipos em arquivo ou rode scripts e testes que
alterem estado. Não publique, envie mensagens, configure automações ou execute a solução.
Invocar esta skill também não autoriza delegação. Uma ideia escrita na resposta é suficiente
para tornar a abordagem revisável, sem começar a aplicá-la.

## Mostrar a proposta concreta

Explique em português claro:

- O resultado que entendeu e os limites do pedido.
- A abordagem que pretende seguir, com exemplos do próprio caso.
- Os arquivos, grupos, comportamentos ou sistemas que seriam afetados.
- O motivo das escolhas e as consequências relevantes, incluindo alternativas quando mudarem
  a decisão. Diferencie fatos verificados de hipóteses.
- Como verificaria o resultado depois da implementação e quais escolhas ainda precisam do usuário.

Adapte o tamanho ao pedido. Para reorganizar pastas, mostre a árvore proposta e quais itens
entrariam em cada grupo antes de movê-los. Para mudar um fluxo, descreva o comportamento
esperado e suas diferenças. Não imponha tarefas, IDs ou uma especificação completa a uma
proposta simples. Use os princípios de `especificar` apenas quando esse nível de detalhe ajudar.

## Encerrar e aguardar

Entregue a proposta na resposta final e pare. Deixe explícito que ela está aguardando a decisão
do usuário. Não continue com edições depois de apresentá-la numa atualização de progresso.
Silêncio, passagem do tempo, uma dúvida ou elogio sem autorização não liberam a execução.
Uma autorização genérica anterior não elimina a espera que o usuário acabou de solicitar.

Quando o usuário aprovar a proposta concreta, por exemplo dizendo "pode fazer", siga com
`implementar` ou com o procedimento adequado dentro do escopo aprovado. Não peça a mesma
aprovação novamente nem volte a produzir propostas indefinidamente. Se ele pedir ajustes,
revise a proposta e aguarde; se a aprovação for parcial, execute apenas a parte liberada.
Peça outra decisão somente quando uma mudança importante ultrapassar o que foi aprovado.

`propor` explica uma ação futura antes de executá-la. `esclarecer` esclarece uma explicação
anterior; `especificar` organiza trabalho substancial em tarefas e critérios. A aprovação da
proposta não comprova a implementação: as verificações ainda precisam ocorrer depois.
