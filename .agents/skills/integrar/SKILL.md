---
name: integrar
description: Integra trabalho entre branches ou conclui a integração de um PR no destino autorizado, preservando alterações e verificando a árvore resultante. Não confunda com pull-request, que escreve a descrição.
license: Apache-2.0
---

# Integrar trabalho verificado

Leia o pedido e as convenções do projeto. Identifique repositório, branch ou PR de origem,
destino, revisão atual e ação autorizada: atualizar uma branch, integrar localmente, publicar
ou fazer merge remoto. Diferencie trazer a base para a branch de integrar a branch na base.
Use o destino já definido; se uma escolha essencial continuar aberta, esclareça apenas ela.
Um pedido vago para terminar o trabalho não escolhe sozinho publicação, destino ou descarte.

## Preparar a integração

Inspecione estado Git, histórico, relação entre as branches, commits envolvidos, diff e checks
aplicáveis. Confira se as referências locais refletem o estado remoto quando isso afetar a ação.
Não confunda branch com nome parecido, PR aprovado de outra revisão ou testes de um SHA anterior
com a revisão que será integrada. Uma branch não precisa ser integrada se o resultado já está
no destino; confira essa condição antes de repetir ações.

Preserve mudanças locais e trabalho alheio. Não descarte, esconda ou comite alterações de outra
pessoa para liberar a operação. Se não puder preservar o estado durante a integração, explique
o impedimento e a próxima ação específica. Não crie worktrees por fora das ferramentas e regras
do ambiente nem altere checkouts de outros agentes.

Use a estratégia combinada ou a convenção do projeto. Não substitua um merge pedido por rebase
nem reescreva histórico compartilhado por conveniência. Nunca force push, use `--no-verify`
ou enfraqueça uma verificação para permitir a integração.
Isso inclui mecanismos equivalentes, como desabilitar hooks com `core.hooksPath`, alterar
configurações de checks ou omitir suas etapas. Não use esses atalhos nem quando supuser que
nenhuma verificação está ativa; use a operação normal e trate falhas reais.

## Resolver e comprovar o resultado

Resolva conflitos preservando a intenção das duas mudanças e as decisões vigentes. Examine
os pontos de uso, não apenas os marcadores de conflito. Uma escolha de produto ou contrato
sem resposta continua pendente; continue o trabalho independente que já estiver autorizado.
Se houver merge em andamento, relate esse estado e não inicie outra operação Git incompatível.
Não conclua um conflito cuja resolução depende de uma decisão ainda ausente.

Execute as verificações exigidas pelo projeto e as pertinentes às partes integradas sobre
a árvore resultante. Registre o estado anterior para distinguir falhas preexistentes de
regressões, sem dispensar um check exigido. Não aprove um resultado só porque cada branch
passava isoladamente. Alterações posteriores podem invalidar a prova anterior.

Se um check obrigatório falhar ou faltar evidência exigida, não declare a integração pronta
nem finalize publicação ou merge remoto. Preserve e relate o estado local real, inclusive
se um merge local já ocorreu; não tente desfazê-lo apagando trabalho alheio.
Desfazer uma integração também precisa estar no escopo e preservar alterações locais.
Não use reset destrutivo como limpeza automática; se não puder preservar o estado, reporte-o.

## Finalizar no limite autorizado

Publicação, criação de PR e merge remoto seguem a autorização existente. Não peça novamente
uma ação já autorizada, mas não deduza autorização remota de uma integração só local.
Respeite as proteções do destino e confira o SHA e o resultado da ação. Se um push for rejeitado
ou uma resposta se perder, leia o estado atual antes de tentar novamente; não force a operação.

Use `descrever-pr` para a descrição e `tratar-revisao` para feedback recebido. Siga os mecanismos
do ambiente para acompanhar checks quando necessário; informe os pendentes sem fingir sucesso.
Remova branches ou worktrees somente quando essa limpeza estiver autorizada, o trabalho estiver
preservado e a propriedade do recurso estiver comprovada. Não remova ambientes geridos externamente.

Relate origem e destino, revisões, conflitos resolvidos, provas e o estado final observado:
integrado localmente, publicado, merge remoto concluído ou ainda pendente. Esses estados não
são equivalentes. Use `passar-contexto` se outra sessão precisar concluir.
Nomeie checks com falha ou sem execução e o que falta para concluir, quando houver.

Inspirada em [finishing-a-development-branch, do Superpowers](https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md),
sem menu fixo ou autorização implícita para publicar e limpar ambientes.
