---
name: criticar-interface-em-conselho
description: Reúne avaliadores independentes para criticar a UI e a UX de uma interface com a mesma rubrica e consolida achados, severidades e divergências. Use quando pedirem um conselho, painel ou avaliação de UI/UX por várias perspectivas.
license: Apache-2.0
---

# Criticar a interface em conselho

Use quando uma única crítica não basta: avaliadores diferentes encontram problemas diferentes
na mesma interface, e a nota de severidade de uma só pessoa é pouco confiável. Esta skill
acrescenta o que é específico de interface. Siga `conselho` para independência, rodadas e
consolidação, e `delegar` para executar as consultas, resolvendo `roles.council` quando houver
política de modelos. Para cada avaliador, o formato de achado de `criticar-interface` substitui
o retorno de especialista de `conselho`. Para uma crítica individual, use `criticar-interface`;
para escolher entre alternativas de design, use `conselho`.

## Preparar o objeto comum

Fixe o que será avaliado e entregue o mesmo material a todos os avaliadores:

- A versão examinada: capturas identificadas, build, URL com data ou commit.
- O contexto da crítica, conforme `criticar-interface`: público, tarefas, plataforma, etapa,
  escopo, suposições e meta de acessibilidade.
- As diretrizes: a rubrica `rubric.md` da skill `criticar-interface`, o design system do
  projeto e as diretrizes de plataforma consultadas, com origem e data.
- As formas de acesso disponíveis a cada avaliador: interface em uso, capturas, código,
  árvore de acessibilidade ou tecnologia assistiva.
- Achados descartados anteriormente e seus motivos, quando houver.

Prepare esse objeto antes das consultas; não deixe cada avaliador fixar contexto ou versão
diferentes. Cada um pode investigar as fontes e as diretrizes por conta própria.

## Compor o conselho

Escolha as perspectivas pela interface e seus riscos, por exemplo:

- Usabilidade e fluxos das tarefas principais.
- Acessibilidade.
- Hierarquia visual e consistência com o design system.
- Conteúdo, confiança e escolha.
- Domínio do produto ou convenções da plataforma.

Use de 3 a 5 avaliadores por padrão; respeite a quantidade e as perspectivas pedidas pelo usuário.
Essa faixa vem de estudos com avaliadores humanos. Várias instâncias do mesmo modelo tendem a
compartilhar pontos cegos; quando houver modelos diferentes disponíveis na política ou no pedido,
prefira diversificá-los. Declare a composição de modelos e trate a concordância entre instâncias
do mesmo modelo como confirmação fraca.

Cada avaliador examina a interface inteira com a rubrica completa e aprofunda sua perspectiva;
a ênfase não limita o que ele pode relatar. Ele entrega a crítica no formato de
`criticar-interface`, sem contato com outros pareceres.

## Consolidar

1. **Agrupar.** Junte achados equivalentes: o mesmo problema no mesmo elemento, mesmo descrito
   com palavras ou padrões diferentes. Dê um ID a cada achado consolidado e registre quais
   achados originais ele reúne e por quê. Na dúvida, mantenha os achados separados e indique
   a relação entre eles.
2. **Reavaliar a severidade.** Envie a lista consolidada, sem notas nem autores, a cada
   avaliador em contexto independente. Cada um atribui de 0 a 4 a todos os itens, com motivo.
   A nota 0 significa "não considero problema de uso".
3. **Calcular.** Para cada achado, registre as notas, a mediana e o intervalo, além de quantos
   e quais avaliadores o relataram originalmente. Com número par de notas, a mediana pode ficar
   entre dois níveis, como 2,5. A mediana é uma escolha deste harness para a escala ordinal.
4. **Resolver controvérsias.** Uma diferença de 2 níveis ou mais entre notas do mesmo achado
   abre nova rodada. Apresente evidências e argumentos sem autoria. Cada avaliador mantém ou
   altera sua nota com justificativa, e uma alteração exige evidência nova. Preserve os
   pareceres originais. Se a disputa depender do comportamento real das pessoas, recomende o
   teste que a resolveria em vez de decidir por maioria.

Uma barreira de acessibilidade com nota 4 e base `observado` mantém a nota 4, salvo refutação
com evidência; notas dadas sem a mesma forma de acesso não a rebaixam. Um achado relatado por
um único avaliador permanece na lista principal, identificado como tal: a quantidade de
avaliadores não mede a gravidade.

Se não for possível executar avaliadores em contextos independentes, declare o limite e
apresente o resultado como crítica individual.

## Retornar

1. **Composição:** avaliadores, perspectivas, modelos, formas de acesso e limites reais de execução.
2. **Objeto avaliado:** versão, contexto, suposições e diretrizes consultadas.
3. **Achados consolidados:** uma única lista ordenada pela mediana de severidade, com notas,
   intervalo, avaliadores que relataram, base e recomendações. Preserve alternativas diferentes.
4. **Controvérsias e sua resolução:** inclui as que continuam abertas e o que as resolveria.
5. **O que preservar, divergências deliberadas e sugestões de direção:** separados dos achados.
6. **Cobertura:** o que nenhum avaliador pôde examinar e as confirmações recomendadas com
   pessoas ou ferramentas.

O conselho é consultivo e não altera a interface. Correções exigem autorização e seguem `implementar`.

Fundamentos: a [NN/g recomenda 3 a 5 avaliadores independentes](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/)
e que [cada avaliador dê notas a todos os problemas encontrados](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/),
porque a nota de um só avaliador é pouco confiável. Um [resumo de 33 estudos da MeasuringU](https://measuringu.com/evaluator-effect/),
fonte secundária, relata concordância mediana de 27% entre dois avaliadores sobre os problemas encontrados.
