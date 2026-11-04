---
name: criticar-interface
description: Critica a UI e a UX de uma tela, fluxo, protótipo ou código de interface com uma rubrica fixa, achados com padrão violado, impacto, severidade e evidência, e limites declarados. Use para avaliar experiência de uso; não corrige a interface.
license: Apache-2.0
---

# Criticar a interface

Use para avaliar a experiência de uso de uma interface existente ou proposta: capturas de tela,
aplicação em execução, protótipo, arquivo de design ou código de interface. Use `revisar` para
um diff contra requisitos, `verificar-aceite` para critérios combinados e `implementar` para
construir ou corrigir a interface. Para vários avaliadores independentes, use
`criticar-interface-em-conselho`.

## Fixar o contexto

Antes de criticar, identifique:

- O público e as tarefas principais que a interface deve permitir.
- A plataforma, os tamanhos de tela e os modos de uso relevantes.
- A etapa do trabalho: exploração, refinamento ou preparação para lançamento.
- O design system, guias de marca, decisões registradas e restrições do projeto.
- O que está em escopo: telas, fluxos, estados e a versão examinada.

Procure esses dados no pedido, na documentação e no código do projeto antes de perguntar.
Pergunte apenas quando uma resposta mudar a crítica; nos demais casos, declare a suposição e
prossiga. Sem objetivo definido, um julgamento vira preferência pessoal.

## Consultar as diretrizes aplicáveis

Leia [rubric.md](rubric.md); ela é a base comum. Depois procure as diretrizes específicas:

- No projeto: tokens, componentes, documentação do design system, guias de conteúdo e decisões
  de interface.
- Na plataforma: diretrizes oficiais vigentes, como Apple Human Interface Guidelines,
  Material Design ou o guia do sistema de componentes em uso, na versão adotada.

Quando a versão vigente de uma diretriz externa importar e houver acesso à internet, consulte-a
com `pesquisar-web` e cite o documento usado. Sem acesso, declare o limite e siga com a rubrica e
os materiais locais. Diretrizes do projeto prevalecem sobre a base genérica quando forem mais
específicas; registre conflitos entre elas em vez de escolher em silêncio.

## Examinar a interface

Examine a forma mais fiel disponível. Prefira a interface renderizada e em uso a capturas,
e capturas ao código sozinho; o código não mostra sobreposição, contraste real nem alinhamento
visual. Percorra as tarefas definidas, incluindo estados e tamanhos de tela em escopo.

Aplique as sete seções da rubrica na ordem e registre cada achado no formato da rubrica.
Mantenha a crítica consistente:

- Todo achado indica um padrão e um impacto observável. Sem isso, o comentário vai para
  "Sugestões de direção", identificado como preferência ou ideia.
- Um mesmo problema em vários elementos é um achado só, com todas as ocorrências.
- Não aplique uma regra contra uma convenção consagrada do público ou uma decisão registrada
  do projeto sem impacto observado.
- Não reapresente um achado descartado pelo usuário com outra justificativa. Mantenha o
  descarte, salvo evidência nova, que deve ser explicada.
- Atribua a severidade pela escala da rubrica, não pela facilidade de corrigir.
- Recomende uma mudança concreta, indicando o padrão esperado e a diferença atual.
- Diferencie o que foi observado, o que foi inferido e o que é hipótese.

## Limites

Uma inspeção não substitui teste com pessoas do público. Indique quais achados de alta
incerteza ou alto impacto merecem confirmação com usuários e o que observar nesse teste.
Uma captura estática não prova navegação por teclado, comportamento com leitor de tela,
persistência nem desempenho. Não declare conformidade com a WCAG a partir de uma inspeção.

A crítica produz achados; não altera a interface. Correções exigem autorização e seguem
`implementar`.

## Retornar

Responda em português, salvo pedido diferente, com:

1. Contexto e suposições: público, tarefas, plataforma, etapa, versão examinada e diretrizes
   consultadas, com links ou caminhos.
2. Achados ordenados por severidade, no formato da rubrica.
3. O que preservar: decisões que funcionam bem e devem resistir às mudanças, quando houver.
4. Sugestões de direção, separadas dos achados.
5. Cobertura: seções da rubrica examinadas, o que não pôde ser examinado e por quê, e
   confirmações recomendadas com usuários ou ferramentas.

Se não houver achado relevante, diga isso com a cobertura e os limites da avaliação.
