---
name: passar-contexto
description: Preserva o estado do trabalho, a próxima etapa, as decisões e as provas pendentes para retomada por outra sessão.
license: Apache-2.0
---

# Preservar o contexto para retomada

Leia o trabalho atual e a passagem de contexto mais recente. A passagem é a visão atual do
trabalho, não um histórico: reescreva-a em vez de acrescentar resumos às anteriores. Ela deve
bastar para outra sessão continuar sem repetir a investigação e ter no máximo 4.000 caracteres.
Abra pela retomada:

- Condição de retomada, próxima etapa exata (`revisar`, `implementar`, `verificar-aceite`,
  `especificar` ou outra atividade nomeada) e primeira ação concreta. Para trabalho bloqueado,
  a falha observada; para trabalho recorrente, a última entrada processada e o lote incompleto.
- Critérios ainda sem prova, cada um pelo nome ou identificador usado nos requisitos.
- Tarefas e processos ativos, com identificador, responsável e como conferir o estado ou
  receber o resultado.
- Objetivo, escopo combinado e links para o plano ou os requisitos.
- Branch e worktree, base fixa do diff, commits, arquivos sob sua responsabilidade e alterações
  ainda não commitadas, com explicação.
- O que foi comprovado, com comandos, resultados exatos e a revisão a que se aplicam.
- Decisões já tomadas, dúvidas abertas, tentativas sem sucesso e acessos necessários.

Aponte para o histórico, os commits e as evidências existentes em vez de copiar a conversa.
Não trate trabalho incompleto como aprovado nem reinicie uma entrevista com decisões já
resolvidas. Antes de entregar, confira se uma sessão nova conseguiria dizer, só a partir da
passagem, a próxima etapa, as pendências e as decisões; complete o que faltar.

Entregue uma passagem curta na resposta. Para continuar entre sessões, atualize um documento
existente ou salve um Markdown conciso no local escolhido pelo usuário. Informe onde salvou
ou deixe explícito que o conteúdo está apenas na conversa.

Não faça commits, transfira responsabilidade nem encerre outra sessão apenas para registrar
o contexto. Siga as convenções do projeto e a autorização existente para essas ações.
