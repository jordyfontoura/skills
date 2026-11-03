---
name: especificar
description: Especifica comportamentos e contratos observáveis e organiza sua entrega em tarefas com critérios e dependências, para trabalho substancial.
license: Apache-2.0
---

# Especificar o trabalho

Leia o pedido, as instruções do projeto, o código relevante, os planos e as decisões existentes.
Use `entrevistar` apenas para escolhas não resolvidas que mudem escopo ou design. Preserve
a etapa da última passagem de contexto e as autorizações existentes.

Antes de elaborar, confira a seleção de modelo e esforço do pedido e de `roles.planner`,
quando houver política local, seguindo `delegar`. Use um contexto compatível com essa seleção;
se o atual não corresponder, delegue ao `planner` quando autorizado. Sem contexto compatível
ou delegação disponível, informe o limite antes de elaborar; não apresente outro modelo como o escolhido.
Sem política ou escolha explícita, preserve a seleção do ambiente. Ler a política não troca
o modelo da conversa nem autoriza delegação.

Declare objetivo, contexto, exclusões, riscos e condição observável de conclusão. Separe
comportamentos e contratos esperados da abordagem técnica e das tarefas, mesmo no mesmo
documento. Diferencie fatos observados, com suas fontes, de desejos e hipóteses. Preserve
contratos existentes que não podem regredir. Partes da visão combinada adiadas nesta entrega
continuam explícitas, sem reduzir silenciosamente o produto à primeira etapa.

Divida o trabalho em tarefas completas, verificáveis de forma independente e compatíveis com uma
sessão. Identifique arquivos e interfaces prováveis sem prescrever cada edição. Dependências
expressam pré-requisitos; a ordem expressa prioridade entre tarefas que já podem avançar.
Quando o pedido ou o plano dividir a entrega em fases, a primeira tarefa de cada fase percorre
uma jornada representativa com a fixture aprovada, só pelas camadas que a fase entrega, como
entrada, cálculo, API, interface ou persistência. Testes específicos continuam cobrindo os detalhes.
Use a entrada normal e a configuração padrão, com componentes próprios reais e dados
sintéticos. Respeite a ordem definida pelo usuário e preserve os critérios finais.
Não crie fases, fixtures nem essa estrutura para trabalho de uma sessão.

Para cada critério, declare o comportamento esperado, o método de prova e os passos para
reproduzi-lo. Leia o apoio `testing.md` da skill `implementar` ao escolher a prova. Por exemplo,
uma tarefa de exportação pode exigir o cabeçalho CSV correto para uma entrada vazia,
verificado pela API pública de exportação. Use cenários concretos de entrada, ação e resultado,
incluindo erros e limites relevantes ao risco. Confira antes se os dados, acessos e mecanismos
necessários à prova existem; dependências ausentes ficam explícitas, não viram promessa de aceite.
Quando uma garantia depender de plataforma ou runtime, investigue a viabilidade do mecanismo
e da medição antes de assumir uma solução técnica. Diferencie exigências do usuário de
hipóteses introduzidas pelo plano; falta de prova não rebaixa uma exigência a hipótese.
Numa entrega em fases, indique para cada prova as funcionalidades que ela exige e a fase que as
entrega. O aceite de uma fase não pode depender de funcionalidade de fase posterior.

Em registros duráveis ou com vários critérios, use referências estáveis; não renumere
nem reutilize IDs existentes. Ligue tarefas aos critérios e provas que atendem. Uma prova pode
atender a vários critérios quando essa relação for explícita. Antes de apresentar, confira
critérios sem cobertura, tarefas sem finalidade ou pré-requisito declarado, dependências
contraditórias e, numa entrega em fases, provas que exigem funcionalidade de fase posterior. Não imponha IDs ou arquivos adicionais a trabalho curto na conversa.

Mantenha planos curtos na conversa. Quando várias sessões precisarem de contexto durável,
use o registro oficial do projeto ou o destino escolhido pelo usuário. Inclua escopo,
tarefas, critérios, decisões e próxima etapa. Identifique onde consultar o estado efetivo e
se o registro descreve comportamento vigente, mudança proposta ou histórico. Ao concluir uma
mudança, indique a referência vigente conforme a convenção do projeto; não mantenha cópias
concorrentes nem crie um sistema paralelo de acompanhamento.

Apresente o plano concreto e as perguntas restantes. Prossiga quando o pedido existente
autorizar claramente esse escopo. Um pedido apenas de planejamento ou exploração deixa
a implementação pendente. Peça uma decisão se o trabalho ultrapassar a autorização ou
se uma escolha importante continuar aberta. Planejar não altera o código do produto.
