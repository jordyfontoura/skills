---
name: criticar
description: Critica a qualidade de um artefato ou experiência com critérios especializados, evidências, prioridades e nota obrigatória com duas casas decimais. Use para pedir um crítico independente ou compor uma crítica com conselho; inclui notas por categoria quando pertinentes. Não corrige; para diff use `revisar` e para aceite use `verificar-aceite`.
license: Apache-2.0
---

# Criticar um artefato ou experiência

Fixe o objeto e a versão, o público, a intenção, o foco pedido, as referências e as ações
permitidas. Consulte decisões, críticas anteriores e descartes antes de perguntar. Preserve
o escopo e as escolhas estabelecidas; especializar a crítica não autoriza redefinir o produto.
Para escolher entre propostas, use `conselho`; para reescrever texto, use `escrever-claro`.

## Escolher o método e os critérios

Declare a especialização pertinente ao pedido e os critérios desta crítica antes do exame:

- **UI e UX**, inclusive a interface de jogos: siga a rubrica de interface abaixo e consulte
  os guias nela indicados conforme os critérios examinados.
- **Game design:** consulte [mecânicas, ritmo, dificuldade e resposta ao jogador](../../../knowledge/gamedev/game-design.md).
- **Assets 3D para jogos:** consulte [geometria, materiais, rig e requisitos de uso](../../../knowledge/3d-modeling/game-ready-assets.md).
- **Outros aspectos**, como direção de arte ou argumentação de um texto: derive
  os critérios do pedido, das referências, das regras do projeto e de princípios do domínio
  com mecanismo explícito. Para clareza de texto, consulte `escrever-claro` sem reescrever.

Identifique a origem e os limites dos critérios em qualquer domínio; não apresente uma rubrica
criada para o caso como padrão validado. Use `consultar-conhecimento` para localizar outros
guias pertinentes e leia apenas os necessários ao objeto, sem carregar toda a biblioteca.
Consulte fontes externas com `pesquisar-web` quando um julgamento depender delas;
sem consulta, declare a origem não conferida.

Combine os métodos quando o objeto exigir. Uma rubrica de interface não cobre sozinha
cooperação, ritmo de jogo ou coerência de um argumento. Pergunte apenas se uma definição
ausente mudar o julgamento; nos demais casos, declare suposições razoáveis.

## Rubrica de interface

Fixe público, tarefas principais e de saída, plataforma, entradas, tamanhos de tela, temas,
etapa, design system, guias de marca e conteúdo, meta de acessibilidade e versão em escopo.
Em exploração, priorize fluxos e estrutura e agrupe acabamento; antes do lançamento, examine
também acabamento e estados por completo. A etapa muda o foco, não a severidade.

Diretrizes do projeto e da plataforma prevalecem em convenções, estilo e componentes, mas
não reduzem os pisos de **WCAG 2.2 nível AA**, ou meta mais exigente inclusive legal, e de
**escolha da pessoa**: a interface não leva ninguém a decidir contra o próprio interesse.
Registre conflitos com esses pisos sem rebaixar a severidade.

Primeiro entenda a interface e as tarefas; depois percorra as sete seções nesta ordem,
marcando cada uma como examinada ou não examinada:

1. **Tarefas e fluxos:** use [usabilidade](../../../knowledge/ux/usability.md), incluindo
   percurso cognitivo quando aprendizagem ou padrões pouco familiares importarem.
2. **Heurísticas de usabilidade:** examine as dez heurísticas do mesmo guia conforme as
   convenções do público; uma violação aparente precisa de impacto concreto na tarefa.
3. **Acessibilidade:** use os [critérios por forma de acesso](../../../knowledge/accessibility/interface-criteria.md).
   Numa auditoria, percorra todos os critérios dos níveis da meta e indique número e nível
   nos achados. Registre o que o acesso não permite verificar. Inspeção parcial não comprova
   conformidade; o piso permanece obrigatório.
4. **Hierarquia visual, layout e consistência:** compare [hierarquia, estados e conteúdo](../../../knowledge/ux/states-and-content.md)
   com o design system; consulte [direção visual e tokens](../../../knowledge/ux/visual-direction.md)
   para avaliar coerência com a tarefa. Quando a causa for compartilhada, recomende corrigir
   o componente ou a regra de origem. Preferências estéticas e sinais de genericidade só
   fundamentam defeito quando houver regra verificável ou impacto com mecanismo explícito.
5. **Conteúdo, confiança e escolha:** examine conteúdo e padrões enganosos no mesmo guia,
   preservando o piso de escolha. Para clareza, consulte `escrever-claro` sem reescrever.
6. **Estados, interação e adaptação:** exercite os estados e extremos pertinentes do mesmo
   guia e registre os limites de simulações, capturas e operação. Quando houver animação,
   consulte [movimento](../../../knowledge/ux/motion.md) e examine interrupção, retorno com
   movimento reduzido e desempenho conforme a meta e o acesso disponível.
7. **Convenções da plataforma:** use o [inventário de plataforma](../../../knowledge/ux/platform-conventions.md)
   e confira diretrizes oficiais vigentes. Registre URL, data e versão do sistema, SDK ou
   biblioteca; sem consulta, marque a diretriz como de memória, versão não conferida.

Uma regra verificável ou princípio com mecanismo explícito fundamenta um achado. O impacto
pode atingir tarefa, compreensão, confiança percebida ou coerência do produto. Uma reação
como "parece datado", sem regra nem mecanismo, é sugestão de direção. Decisões deliberadas
do projeto sem violação de piso nem impacto comprovado ficam em divergências e riscos,
com o teste que confirmaria o risco. Registre um problema que cruza seções na primeira
em que aparecer, citando todos os padrões violados.

### Severidade e formato dos achados de interface

A severidade combina frequência no grupo afetado, impacto na tarefa e persistência após
o problema ser conhecido. Certeza fica na base; esforço de correção não altera a nota.

| Nota | Consequência |
| --- | --- |
| 0 | Não é problema de uso; apenas para reavaliar achados alheios. |
| 1 | Cosmético, sem atraso nem erro na tarefa. |
| 2 | Hesitação ou pequeno atraso; recuperação sem ajuda nem perda. |
| 3 | Erro, atraso significativo ou abandono para parte do público; recuperação exige esforço ou ajuda. |
| 4 | Impede tarefa em escopo para algum grupo ou causa perda de dados, dinheiro, privacidade ou segurança. |

Por política do harness, uma barreira de acessibilidade que impede tarefa em escopo recebe
4, mesmo afetando um grupo pequeno. Não registre achado próprio com severidade 0.

Cada achado informa ID estável, local e ocorrências, observação verificável, padrões
violados, impacto com público e tarefa, severidade justificada, base com evidência e
recomendação concreta que liga padrão esperado, lacuna e origem da correção.
Exemplos de calibração: botão de checkout desabilitado sem explicar o campo pendente pode
receber 3 quando bloqueia o avanço; pesos de títulos inconsistentes, sem atraso ou erro,
podem receber 1. Adapte ao contexto e à evidência, sem transformar exemplos em notas fixas.

## Preservar a independência

Uma crítica pontual pode ocorrer no contexto atual se ele não produziu o objeto. Quem fez o
trabalho não apresenta sua autocrítica como independente. Num pedido de crítico independente
ou num ciclo produtor-crítico autorizado, use `delegar` para uma consulta em contexto novo.
Forneça objeto, versão, critérios, acesso, achados anteriores e decisões, sem usar a defesa
ou a autoavaliação do implementador como evidência.

Respeite o modelo explicitamente escolhido. Havendo política local, a consulta crítica usa
`roles.council` conforme `delegar`, inclusive quando individual; esse papel não exige painel.
Sem política, preserve as seleções do ambiente e do usuário. Configuração não comprova execução.
Se não houver contexto independente ou ferramenta adequada, declare a crítica pendente ou
limitada, sem simular outro especialista.

Para várias perspectivas solicitadas, siga a seção de painel abaixo e `conselho` para a
coordenação geral. Como crítico delegado, faça apenas sua análise, sem abrir novos agentes
ou conselhos.

## Crítica em painel

Use somente quando o pedido incluir conselho, painel ou várias perspectivas independentes.
O coordenador organiza as consultas uma única vez com `conselho` e as executa com `delegar`.
Entregue a todos o mesmo objeto, versão, intenção, contexto, critérios, diretrizes e descartes
anteriores, indicando as formas de acesso de cada um. Cada especialista pode investigar fontes,
mas não redefine o objeto nem conhece os primeiros pareceres dos demais. O retorno de
`criticar`, incluindo notas de qualidade justificadas, substitui o relatório genérico de
especialista de `conselho`.

Escolha perspectivas pela cobertura necessária e respeite quantidade e modelos pedidos.
Para UI, use de 3 a 5 avaliadores por padrão, aprofundando usabilidade, acessibilidade,
hierarquia, conteúdo ou plataforma conforme os riscos. Cada um examina a interface inteira
com as sete seções; a especialização não limita os achados. Essa faixa vem de avaliações
humanas, não garante independência entre instâncias de IA. Quando disponíveis e autorizados,
prefira modelos diferentes e trate concordância entre instâncias do mesmo modelo como fraca.

Agrupe achados equivalentes com IDs consolidados, rastreando os originais e o motivo da união.
Na dúvida, mantenha-os separados e relacionados. Preserve achados de um único crítico e
recomendações diferentes; quantidade de relatores não mede gravidade. Não resolva disputa
factual por maioria. Para UI, consolide a severidade assim:

1. Envie a lista consolidada sem notas nem autores para reavaliação independente. Cada
   avaliador atribui de 0 a 4 a todos os itens, com motivo; 0 significa que não considera
   problema de uso.
2. Registre notas, mediana, intervalo e quais avaliadores relataram cada achado originalmente.
   Com quantidade par, a mediana pode ser intermediária, como 2,5. Usar mediana é uma escolha
   do harness para essa escala ordinal.
3. Diferença de 2 níveis ou mais abre nova rodada com evidências e argumentos sem autoria.
   Cada avaliador mantém ou altera a nota com justificativa; alteração exige evidência nova.
   Preserve os pareceres originais. Se a disputa depender do comportamento das pessoas,
   recomende o teste que a resolveria.

Barreira de acessibilidade observada com severidade 4 mantém 4, salvo refutação com evidência;
notas de avaliadores sem o mesmo acesso não a rebaixam. As regras de severidade e a faixa
de avaliadores de UI não são universais para jogos, textos ou outros aspectos.

Para notas de qualidade, fixe critérios, âncoras e regra de consolidação antes das consultas.
Preserve notas individuais e explique as consolidadas, com duas casas decimais. Não calcule
médias ou medianas de prioridades incompatíveis; notas com critérios ou acessos diferentes
devem ser apresentadas por escopo, sem consolidação forçada. Retorne composição, modelos,
acesso, cobertura, concordâncias, controvérsias e suas resoluções ou provas pendentes.
Sem contextos independentes, declare o painel não realizado e a análise como individual.

## Examinar e fundamentar

Examine a forma mais fiel disponível para cada critério: jogue, navegue, leia ou opere o
artefato conforme autorizado. Capturas sustentam aparência, mas não demonstram sozinhas
controles, persistência, cooperação ou áudio. Código lido não comprova execução.
Para aparência, prefira interface renderizada em uso, depois capturas e depois código;
para acessibilidade, use também código, árvore de acessibilidade e tecnologia assistiva.
Medidas vêm do código, estilos computados ou arquivo de design; estimativas de captura
são aproximadas. Inspeção não substitui testes com o público, incluindo pessoas com
deficiência; indique quais hipóteses de alto impacto ou incerteza exigem esses testes.
Use ambiente de teste e respeite os limites de ações com efeitos reais. Registre passos,
condições e materiais examinados; capacidade ou acesso ausentes continuam sendo limites.

Cada achado precisa de localização, observação, critério ou mecanismo, impacto, prioridade,
base e recomendação concreta. Use IDs estáveis e distinga `observado`, `inferido` e `hipótese`,
citando a evidência. Na UI, use o formato e a severidade da rubrica. Nos demais domínios,
justifique a prioridade pela consequência e pelo alcance, sem impor a escala de UI.
Um juízo sem critério nem mecanismo fica em sugestões de direção. Não confunda uma reação
prevista do público com comportamento observado em pessoas.

Agrupe ocorrências do mesmo problema. Preserve descartes do usuário, salvo evidência nova
declarada. Numa nova versão, marque achados anteriores como resolvidos, persistentes ou
regressões e identifique os novos. Aponte também o que funciona e deve resistir às correções.

## Notas e ciclos de correção

Toda crítica realizada entrega uma nota geral de qualidade. Use a escala combinada ou,
na ausência dela, de 0 a 10. Escreva as notas de qualidade com ponto e exatamente duas casas
decimais: `9.73`, `7.00`, `0.00`; o extremo superior da escala padrão é `10.00`.
Quando houver dimensões distintas relevantes, inclua também notas por categoria, como
game design e estética, ou usabilidade e acessibilidade. Respeite categorias pedidas e
não crie divisões só para preencher um quadro.

Antes do exame, fixe critérios e âncoras adequados ao domínio, usando os combinados ou
declarando os adotados quando o pedido não os fornecer. Referências comentadas ajudam a
calibrar. Ligue cada nota às evidências, aos pontos fortes e aos problemas que a justificam;
explique a relação da nota geral com as categorias e os pesos, se houver. Não suponha média
aritmética nem use uma nota alta para compensar uma exigência descumprida.

Declare a cobertura e a incerteza: duas casas decimais são formato de apresentação, não
precisão estatística comprovada. Em exame parcial, a nota vale só para a parte examinada;
sem acesso a material suficiente, declare a crítica não realizada em vez de inventar nota.
Nota de qualidade e severidade são medidas distintas: a escala de severidade de UI continua
de 0 a 4, conforme a rubrica. Se faltar uma definição decisiva para aplicar um limiar de
aprovação, esclareça essa definição sem criar um limiar por conta própria.

A crítica não edita o produto. Um ciclo só prossegue quando a implementação e as novas
avaliações estiverem autorizadas. Antes da primeira rodada, fixe critérios, eventual limiar,
regra de avaliação e condição de parada, incluindo o limite de rodadas quando combinado.
Modelo, limiar de aprovação e número de rodadas respeitam o pedido.

Quem implementa confere o feedback com `tratar-revisao`, corrige por prioridade com
`implementar` e repete as provas afetadas. As sugestões são meios a conferir para atingir
o requisito; não ganham autoridade por terem vindo do crítico. Preserve versões recuperáveis
e evidências para comparar melhora e regressões. Cada nova crítica avalia a versão resultante;
não repita avaliações da mesma versão apenas até obter uma nota favorável.

Não baixe o limiar nem troque o crítico para obter aprovação. Após duas correções sem sucesso
ou recorrência do mesmo defeito, use `diagnosticar`. Encerre ao cumprir os critérios ou atingir
a condição de parada, relatando notas, problemas e provas ausentes. Se uma decisão ou acesso
ficar pendente, continue apenas o trabalho independente autorizado. A última versão não é
automaticamente a melhor. Notas não substituem provas técnicas nem `verificar-aceite`.

## Retornar

Responda em português, salvo pedido diferente. Entregue contexto, versão, especialização,
critérios e formas de acesso; achados por prioridade com evidências; o que preservar;
divergências deliberadas e sugestões separadas; cobertura,
limites e provas recomendadas. Inclua sempre a nota geral e as notas por categoria pertinentes,
com duas casas decimais e justificativas. A conclusão pelo limiar só existe quando combinada.
Num painel, preserve divergências e autoria dos achados. Sem problema relevante, diga isso
com a cobertura examinada, sem fabricar críticas nem declarar qualidade que não pôde verificar.

## Fundamentos e limites do método de interface

A [avaliação heurística](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/)
e a [escala de severidade da NN/g](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/)
fundamentam a inspeção e a reavaliação por vários avaliadores. As definições de 1 a 3,
os pisos, a regra de barreiras e a mediana são escolhas deste harness.
O [resumo de 33 estudos da MeasuringU](https://measuringu.com/evaluator-effect/), fonte
secundária, relata concordância mediana de 27% entre dois avaliadores humanos.

Na comparação de [Duan et al., CHI 2024](https://arxiv.org/abs/2403.13139), o GPT-4 teve
precisão menor que especialistas humanos (0,60 contra 0,83) e recall um pouco maior.
Os erros incluíram regras fora de contexto, duplicatas, descartes reapresentados, correções
vagas e leitura visual incorreta sem interface renderizada; a utilidade caiu nas iterações.
As regras desta skill respondem a esses erros, sem medição de ganho nem garantia de que os
resultados se apliquem a outros modelos.
