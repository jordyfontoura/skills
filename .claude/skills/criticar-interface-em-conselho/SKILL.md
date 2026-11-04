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
política de modelos. Para uma crítica individual, use `criticar-interface`.

## Preparar o objeto comum

Fixe o que será avaliado e entregue o mesmo material a todos os avaliadores:

- A versão examinada: capturas identificadas, build, URL com data ou commit.
- O contexto da crítica, conforme `criticar-interface`: público, tarefas, plataforma, etapa,
  escopo e suposições.
- As diretrizes aplicáveis: a rubrica `rubric.md` da skill `criticar-interface`, o design system
  do projeto e as diretrizes de plataforma consultadas, com versão e origem.
- Achados descartados anteriormente e seus motivos, quando houver.

Prepare esse objeto antes das consultas; não deixe cada avaliador fixar contexto ou versão
diferentes. Cada um pode investigar as fontes e as diretrizes por conta própria.

## Compor o conselho

Escolha as perspectivas pela interface e seus riscos, por exemplo:

- Usabilidade e fluxos das tarefas principais.
- Acessibilidade.
- Hierarquia visual e consistência com o design system.
- Conteúdo e textos da interface.
- Domínio do produto ou convenções da plataforma.

Use de 3 a 5 avaliadores por padrão; respeite a quantidade e as perspectivas pedidas pelo usuário.
Cada avaliador examina a interface inteira com a rubrica completa e aprofunda sua perspectiva;
a ênfase não limita o que ele pode relatar. Peça a crítica no formato de `criticar-interface`,
com severidade atribuída individualmente, antes de qualquer contato com outros pareceres.

## Consolidar

Agrupe os achados equivalentes: o mesmo problema no mesmo elemento ou padrão, mesmo descrito
com palavras ou heurísticas diferentes. Para cada achado consolidado, registre:

- Quantos avaliadores o relataram e quais perspectivas.
- As notas individuais, a mediana e o intervalo entre a menor e a maior. Com número par de
  notas, a mediana pode ficar entre dois níveis, como 2,5.
- A evidência mais forte disponível e as recomendações, preservando alternativas diferentes.

Mantenha os achados relatados por um único avaliador, identificados como tal; a quantidade de
avaliadores não mede a gravidade. Considere a severidade controversa quando um avaliador atribuir
3 ou 4 e outro atribuir 0 ou 1 ao mesmo achado. Nesse caso, abra uma nova rodada com a
divergência e as evidências, preservando os pareceres originais. Se a disputa depender de
comportamento real das pessoas, recomende o teste que a resolveria em vez de decidir por maioria.

Se não for possível executar avaliadores em contextos independentes, declare o limite e
apresente o resultado como crítica individual.

## Retornar

1. Composição: avaliadores, perspectivas, modelos e limites reais de execução.
2. Objeto avaliado: versão, contexto, suposições e diretrizes consultadas.
3. Achados consolidados por mediana de severidade, com contagem de avaliadores, notas e evidência.
4. Divergências e achados de um único avaliador, com o que poderia resolvê-los.
5. O que preservar e sugestões de direção, separados dos achados.
6. Cobertura: o que nenhum avaliador pôde examinar e as confirmações recomendadas com usuários
   ou ferramentas.

O conselho é consultivo e não altera a interface. Correções exigem autorização e seguem `implementar`.

Fundamentos: a [NN/g recomenda 3 a 5 avaliadores independentes](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/)
e [severidade avaliada individualmente por vários avaliadores](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/).
Um [resumo de 33 estudos da MeasuringU](https://measuringu.com/evaluator-effect/), fonte
secundária, relata concordância mediana de 27% entre dois avaliadores sobre os problemas encontrados.
