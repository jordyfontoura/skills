---
name: fazer-direto
description: Executa mudanças priorizando velocidade de entrega, sem criar specs nem seguir o fluxo habitual de planejamento e revisão. Use somente quando o usuário pedir para só fazer, ir direto ao código ou trabalhar em modo gohorse.
license: Apache-2.0
---

# Fazer direto

Entregue o resultado pedido pelo caminho mais curto que funcione. O modo vale até concluir
o pedido, inclusive suas correções; termina num novo pedido ou se o usuário mudar o modo.
Comunique brevemente a ação e as suposições relevantes, sem esperar aprovação da abordagem.
Se o usuário também pedir `propor` ou aprovação antes da execução, respeite essa espera.

## Começar pela execução

Leia as instruções aplicáveis e localize o código e as decisões que afetam a mudança.
Se já houver spec, aproveite os requisitos e contratos pertinentes. Não crie nem atualize
specs, planos formais, listas de tarefas ou relatórios de processo. Atualize documentação
de uso quando a mudança exigir.

Implemente diretamente, sem acionar planejamento, entrevista, conselho ou rodadas de revisão
por rotina. Não carregue o fluxo de `implementar` como pré-requisito deste modo. Preserve
consultas e provas expressamente pedidas pelo usuário ou exigidas pelas instruções aplicáveis.

Escolha os detalhes técnicos reversíveis com base nos padrões existentes. Pergunte de forma
pontual somente quando uma informação ausente mudar o resultado esperado ou exigir uma
decisão humana. Continue as partes independentes enquanto
aguarda; uma dúvida não exige abrir uma spec ou uma entrevista completa.

## Entregar sem ampliar

Faça a solução mais simples que cumpra o pedido inteiro, mesmo quando exigir vários arquivos.
Reutilize o que existe. Deixe abstrações para necessidades futuras, refatorações laterais e
melhorias opcionais fora da entrega. Não reduza silenciosamente o escopo a um protótipo ou
a uma primeira etapa. A preferência por velocidade não autoriza delegação nem ações externas.

## Conferir e encerrar

Exercite o comportamento alterado e execute as verificações obrigatórias e as regressões
afetadas. Use a menor prova suficiente para a mudança; amplie quando houver falha ou risco
concreto. Não crie testes redundantes nem repita uma campanha já válida sem motivo.
Não remova ou enfraqueça verificações para passar, nem apresente prova não executada como sucesso.

Se correções sucessivas não resolverem a falha, investigue a causa antes de tentar outro remendo.
Preserve permissões, dados, alterações alheias e requisitos de segurança do projeto.

Conclua quando o resultado pedido estiver entregue e conferido. Responda brevemente com o
que mudou, o que foi verificado e qualquer pendência concreta. Não acrescente um plano de
melhorias nem documentação de processo para encerrar.
