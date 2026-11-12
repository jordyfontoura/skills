# Criticar a interface

Use para avaliar a experiência de uso de uma interface existente ou proposta: capturas de tela,
aplicação em execução, protótipo, arquivo de design ou código de interface. Use `revisar` para
um diff contra requisitos, `verificar-aceite` para critérios combinados e `implementar` para
construir ou corrigir a interface. Para vários avaliadores independentes, use
o apoio [interface-panel.md](interface-panel.md) de `criticar`;
para escolher entre alternativas de design, use `conselho`.

## Fixar o contexto

Antes de criticar, identifique:

- O público e as tarefas principais que a interface deve permitir.
- A plataforma, os modos de entrada, os tamanhos de tela e os temas relevantes.
- A etapa do trabalho. Ela muda o foco, não a severidade. Em exploração, priorize fluxos e
  estrutura e agrupe o acabamento visual. Antes do lançamento, examine acabamento e estados
  por completo.
- O design system, os guias de marca e de conteúdo, as decisões registradas, a meta de
  acessibilidade e as restrições do projeto.
- Críticas anteriores desta interface, achados descartados e seus motivos.
- O que está em escopo: telas, fluxos, estados e a versão examinada.

Procure esses dados no pedido, na documentação e no código do projeto antes de perguntar.
Pergunte apenas quando uma resposta mudar a crítica; nos demais casos, declare a suposição e
prossiga. Sem objetivo definido, um julgamento vira preferência pessoal.

## Consultar as diretrizes aplicáveis

Leia [interface-rubric.md](interface-rubric.md), a base comum, com seus pisos de acessibilidade e de escolha da
pessoa. Depois procure as diretrizes específicas:

- No projeto: tokens, componentes, documentação do design system, guias de conteúdo e decisões
  de interface.
- Na plataforma: diretrizes oficiais vigentes, como Apple Human Interface Guidelines, Material
  Design, Fluent ou o guia do sistema de componentes em uso.

Quando um achado depender de uma diretriz externa e houver acesso à internet, consulte-a com
`pesquisar-web` e cite URL e data. Sem consulta, marque o padrão como "de memória, versão não
conferida". Sem acesso, declare o limite e siga com a rubrica e os materiais locais. Registre
conflitos entre diretrizes em vez de escolher um lado em silêncio.

## Examinar a interface

Examine a forma mais fiel disponível. Para aspectos visuais, prefira a interface renderizada
e em uso a capturas, e capturas ao código. Para acessibilidade, o código e a árvore de
acessibilidade revelam o que capturas não mostram. Medidas de espaçamento, alinhamento,
tamanho e cor vêm do código, dos estilos computados ou do arquivo de design. Estimadas a
partir de uma captura, são aproximadas.

Opere em ambiente de teste ou com dados fictícios. Não conclua ações com efeito real, como
compra, envio, exclusão ou agendamento, sem autorização; registre o passo como não examinado.

Aplique as sete seções da rubrica na ordem e registre cada achado no formato dela. Mantenha a
crítica consistente:

- Todo achado indica um padrão ou mecanismo e um impacto concreto, conforme "Achado ou
  preferência" na rubrica. O resto vai para sugestões de direção.
- Um mesmo problema é um achado só, com todas as ocorrências e todos os padrões violados.
- Não aplique uma regra contra uma convenção consagrada do público. Uma decisão registrada do
  projeto entra como divergência deliberada, salvo violação de um piso da rubrica ou impacto
  concreto na tarefa.
- Não reapresente um achado descartado pelo usuário com outra justificativa. Mantenha o
  descarte, salvo evidência nova, que deve ser explicada.
- Atribua a severidade pela escala da rubrica e a base pelo material examinado.
- Recomende uma mudança concreta, com o padrão esperado e a diferença atual.

## Limites

Uma inspeção não substitui teste com pessoas do público, incluindo pessoas com deficiência e
usuários de tecnologia assistiva quando a meta de acessibilidade exigir. Indique quais achados
de alta incerteza ou alto impacto merecem esse teste e o que observar nele. Não declare
conformidade com a WCAG a partir de uma inspeção.

Críticas repetidas da mesma interface tendem a perder utilidade. Numa nova versão, parta dos
achados anteriores em vez de recomeçar.

A crítica produz achados; não altera a interface. Correções exigem autorização e seguem
`implementar`.

## Retornar

Responda em português, salvo pedido diferente, com:

1. **Contexto e suposições:** público, tarefas, plataforma, etapa, versão examinada, formas de
   acesso e diretrizes consultadas, com links ou caminhos.
2. **Achados:** ordenados por severidade, no formato da rubrica. Numa nova versão, marque cada
   achado anterior como resolvido, persistente ou novo.
3. **O que preservar:** decisões que funcionam bem e devem resistir às mudanças, quando houver.
4. **Divergências deliberadas e riscos:** separadas dos achados.
5. **Sugestões de direção:** separadas dos achados.
6. **Cobertura:** as seções da rubrica examinadas, o que não pôde ser examinado e por quê, e as
   confirmações recomendadas com pessoas ou ferramentas.

Se não houver achado relevante, diga isso com a cobertura e os limites da avaliação.
