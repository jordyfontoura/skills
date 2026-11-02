---
name: passar-contexto
description: Preserva o estado do trabalho, a próxima etapa, as decisões e as provas pendentes para retomada por outra sessão.
license: Apache-2.0
---

# Preservar o contexto para retomada

Leia o trabalho atual e a passagem de contexto mais recente. Resuma o que outra sessão precisa
para continuar sem repetir a investigação:

- Objetivo, escopo combinado e links para o plano ou os requisitos.
- Branch e worktree, base fixa do diff, commits, arquivos sob sua responsabilidade e alterações
  ainda não commitadas, com explicação.
- Tarefas e processos ativos, com identificador, responsável e como conferir o estado ou
  receber o resultado.
- O que foi comprovado, com comandos, resultados exatos e a revisão a que se aplicam, e o que
  continua sem prova.
- Próxima etapa exata (`revisar`, `implementar`, `verificar-aceite`, `especificar` ou outra atividade nomeada)
  e primeira ação concreta.
- Decisões já tomadas, dúvidas abertas, tentativas sem sucesso e acessos necessários.
- Condição de retomada e, para trabalho bloqueado, a falha observada. Para trabalho recorrente,
  última entrada processada e lote incompleto.

Comece pelo estado atual. Aponte para o histórico, as passagens anteriores e as evidências
existentes em vez de copiar a conversa ou acumular resumos. Não trate trabalho incompleto
como aprovado nem reinicie uma entrevista com decisões já resolvidas.

Entregue uma passagem curta na resposta. Para continuar entre sessões, atualize um documento
existente ou salve um Markdown conciso no local escolhido pelo usuário. Informe onde salvou
ou deixe explícito que o conteúdo está apenas na conversa.

Não faça commits, transfira responsabilidade nem encerre outra sessão apenas para registrar
o contexto. Siga as convenções do projeto e a autorização existente para essas ações.
