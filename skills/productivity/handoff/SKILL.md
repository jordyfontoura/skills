---
name: handoff
description: Preserva o estado do trabalho, a próxima etapa, as decisões e as provas pendentes para retomada por outra sessão.
license: Apache-2.0
---

# Preservar o contexto para retomada

Leia o trabalho atual e a passagem de contexto mais recente. Resuma o que outra sessão precisa
para continuar sem repetir a investigação:

- Objetivo, escopo combinado e links para o plano ou os requisitos.
- Branch e worktree, base fixa do diff, commits, arquivos sob sua responsabilidade e alterações
  ainda não commitadas, com explicação.
- O que foi comprovado, com comandos e resultados exatos, e o que continua sem prova.
- Próxima etapa exata (`review`, `implement`, `evaluate`, `specify` ou outra atividade nomeada)
  e primeira ação concreta.
- Decisões já tomadas, dúvidas abertas, tentativas sem sucesso e acessos necessários.
- Para trabalho bloqueado, falha observada e condição de retomada. Para trabalho recorrente,
  última entrada processada e lote incompleto.

Aponte para evidências existentes em vez de copiar a conversa. Não trate trabalho incompleto
como aprovado nem reinicie uma entrevista com decisões já resolvidas.

Entregue uma passagem curta na resposta. Para continuar entre sessões, atualize um documento
existente ou salve um Markdown conciso no local escolhido pelo usuário. Informe onde salvou
ou deixe explícito que o conteúdo está apenas na conversa.

Não faça commits, transfira responsabilidade nem encerre outra sessão apenas para registrar
o contexto. Siga as convenções do projeto e a autorização existente para essas ações.
