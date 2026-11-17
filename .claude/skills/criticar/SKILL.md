---
name: criticar
description: Critica a qualidade de um artefato ou experiência com critérios especializados, evidências, prioridades e nota obrigatória com duas casas decimais. Use para pedir um crítico independente ou compor uma crítica com conselho; inclui notas por categoria quando pertinentes. Não corrige; para diff use `revisar` e para aceite use `verificar-aceite`.
license: Apache-2.0
---

# Criticar um artefato ou experiência

Avalie o objeto pedido com critérios declarados e evidências, sem corrigi-lo. Fixe objeto e
versão, público, intenção, foco, referências e ações permitidas, consultando decisões, críticas
anteriores e descartes antes de perguntar. Especializar a crítica não autoriza redefinir o
produto. Para escolher entre propostas, use `conselho`; para reescrever texto, `escrever-claro`.

## Escolher o método e os critérios

Declare a especialização e os critérios antes do exame, combinando métodos quando o objeto exigir:

- **UI e UX**, inclusive a interface de jogos: a rubrica de interface abaixo.
- **Game design:** [mecânicas, ritmo, dificuldade e resposta ao jogador](../../../knowledge/gamedev/game-design.md).
- **Assets 3D para jogos:** [geometria, materiais, rig e requisitos de uso](../../../knowledge/3d-modeling/game-ready-assets.md).
- **Outros aspectos**, como direção de arte ou argumentação de um texto: critérios derivados
  do pedido, das referências, das regras do projeto e de princípios do domínio com mecanismo
  explícito. Para clareza de texto, consulte `escrever-claro` sem reescrever.

Informe a origem e os limites dos critérios; uma rubrica criada para o caso não é padrão
validado. Use `consultar-conhecimento` para localizar outros guias e leia só os necessários.
Quando um julgamento depender de fonte externa, consulte-a com `pesquisar-web` ou declare a
origem não conferida. Pergunte apenas se uma definição ausente mudar o julgamento; nos demais
casos, declare suposições razoáveis.

## Rubrica de interface

Fixe público, tarefas principais e de saída, plataforma, entradas, tamanhos de tela, temas,
etapa, design system, guias de marca e conteúdo, meta de acessibilidade e versão em escopo.
Em exploração, priorize fluxos e estrutura e agrupe acabamento; antes do lançamento, examine
também acabamento e estados por completo. A etapa muda o foco, não a severidade.

Diretrizes do projeto e da plataforma prevalecem em convenções, estilo e componentes. Dois
pisos não cedem: **WCAG 2.2 nível AA**, ou meta mais exigente, inclusive legal, e **escolha da
pessoa**, pela qual a interface não leva ninguém a decidir contra o próprio interesse.
Registre conflitos com esses pisos sem rebaixar a severidade.

Entenda a interface e as tarefas e percorra as sete seções nesta ordem, marcando cada uma
como examinada ou não examinada:

1. **Tarefas e fluxos:** [usabilidade](../../../knowledge/ux/usability.md), com percurso
   cognitivo quando aprendizagem ou padrões pouco familiares importarem.
2. **Heurísticas de usabilidade:** as dez heurísticas do mesmo guia, conforme as convenções
   do público. Uma violação aparente precisa de impacto concreto na tarefa.
3. **Acessibilidade:** [critérios por forma de acesso](../../../knowledge/accessibility/interface-criteria.md).
   Numa auditoria, percorra todos os critérios dos níveis da meta e indique número e nível
   nos achados. Registre o que o acesso não permite verificar; inspeção parcial não comprova
   conformidade.
4. **Hierarquia visual, layout e consistência:** [hierarquia, estados e conteúdo](../../../knowledge/ux/states-and-content.md)
   contra o design system, e [direção visual e tokens](../../../knowledge/ux/visual-direction.md)
   para a coerência com a tarefa. Com causa compartilhada, recomende corrigir o componente
   ou a regra de origem.
5. **Conteúdo, confiança e escolha:** conteúdo e padrões enganosos no mesmo guia.
6. **Estados, interação e adaptação:** os estados e extremos pertinentes do mesmo guia, com
   os limites de simulações, capturas e operação. Havendo animação, consulte
   [movimento](../../../knowledge/ux/motion.md) e examine interrupção, retorno com movimento
   reduzido e desempenho.
7. **Convenções da plataforma:** [inventário de plataforma](../../../knowledge/ux/platform-conventions.md)
   e diretrizes oficiais vigentes, com URL, data e versão do sistema, SDK ou biblioteca.
   Sem consulta, marque a diretriz como de memória, versão não conferida.

Um achado precisa de regra verificável ou de princípio com mecanismo explícito, com impacto
em tarefa, compreensão, confiança percebida ou coerência do produto. Uma reação como "parece
datado", uma preferência estética ou um sinal de genericidade, sem regra nem mecanismo, é
sugestão de direção. Decisões deliberadas do projeto, sem violação de piso nem impacto
comprovado, ficam em divergências e riscos, com o teste que confirmaria o risco. Um problema
que cruza seções entra na primeira em que aparecer, citando todos os padrões violados.

### Severidade e formato dos achados de interface

A severidade combina frequência no grupo afetado, impacto na tarefa e persistência depois
que o problema é conhecido. Certeza fica na base; esforço de correção não altera a nota.

| Nota | Consequência |
| --- | --- |
| 0 | Não é problema de uso; apenas para reavaliar achados alheios. |
| 1 | Cosmético, sem atraso nem erro na tarefa. |
| 2 | Hesitação ou pequeno atraso; recuperação sem ajuda nem perda. |
| 3 | Erro, atraso significativo ou abandono para parte do público; recuperação exige esforço ou ajuda. |
| 4 | Impede tarefa em escopo para algum grupo ou causa perda de dados, dinheiro, privacidade ou segurança. |

Uma barreira de acessibilidade que impede tarefa em escopo recebe 4, mesmo afetando um grupo
pequeno. Não registre achado próprio com severidade 0.

Cada achado informa ID estável, local e ocorrências, observação verificável, padrões violados,
impacto com público e tarefa, severidade justificada, base com evidência e recomendação
concreta, que liga padrão esperado, lacuna e origem da correção. Para calibrar: um botão de
checkout desabilitado sem explicar o campo pendente pode receber 3 quando bloqueia o avanço;
pesos de títulos inconsistentes, sem atraso ou erro, podem receber 1.

## Preservar a independência

Quem produziu o objeto não apresenta sua autocrítica como independente. Uma crítica pontual
pode ocorrer no contexto atual se ele não produziu o objeto. Para um crítico independente ou
um ciclo produtor-crítico autorizado, use `delegar` com um contexto novo e forneça objeto,
versão, critérios, acesso, achados anteriores e decisões, sem a defesa nem a autoavaliação
de quem implementou.

Respeite o modelo escolhido. Havendo política local, a consulta usa `roles.council` conforme
`delegar`, mesmo com um só crítico. Sem contexto independente ou ferramenta adequada, declare
a crítica pendente ou limitada, sem simular outro especialista. Como crítico delegado, faça
só a sua análise, sem abrir novos agentes ou conselhos.

## Crítica em painel

Use somente quando o pedido incluir conselho, painel ou várias perspectivas independentes.
O coordenador organiza as consultas uma vez com `conselho` e as executa com `delegar`. Todos
recebem o mesmo objeto, versão, intenção, contexto, critérios, diretrizes e descartes
anteriores, com as formas de acesso de cada um. Cada especialista pode investigar fontes, mas
não redefine o objeto nem conhece os primeiros pareceres dos demais. O retorno de `criticar`,
com as notas de qualidade justificadas, substitui o relatório genérico de especialista de `conselho`.

Escolha perspectivas pela cobertura necessária e respeite quantidade e modelos pedidos. Para
UI, o padrão é de 3 a 5 avaliadores. Cada um examina a interface inteira nas sete seções e
aprofunda usabilidade, acessibilidade, hierarquia, conteúdo ou plataforma conforme os riscos.
A faixa vem de avaliações humanas e não garante independência entre instâncias de IA: prefira
modelos diferentes, quando disponíveis e autorizados, e trate a concordância entre instâncias
do mesmo modelo como fraca.

Agrupe achados equivalentes com IDs consolidados, rastreando os originais e o motivo da união;
na dúvida, mantenha-os separados e relacionados. Preserve achados de um único crítico e
recomendações diferentes. Quantidade de relatores não mede gravidade, e disputa factual não
se resolve por maioria. Para UI, consolide a severidade assim:

1. Envie a lista consolidada, sem notas nem autores, para reavaliação independente. Cada
   avaliador atribui de 0 a 4 a todos os itens, com motivo; 0 significa que não considera
   problema de uso.
2. Registre notas, mediana, intervalo e quais avaliadores relataram cada achado originalmente.
   Com quantidade par, a mediana pode ser intermediária, como 2,5.
3. Diferença de 2 níveis ou mais abre nova rodada, com evidências e argumentos sem autoria.
   Cada avaliador mantém ou altera a nota com justificativa; alterar exige evidência nova.
   Preserve os pareceres originais. Se a disputa depender do comportamento das pessoas,
   recomende o teste que a resolveria.

Barreira de acessibilidade observada com severidade 4 mantém 4, salvo refutação com evidência;
notas de avaliadores sem o mesmo acesso não a rebaixam. As regras de severidade e a faixa de
avaliadores valem para UI, não para jogos, textos ou outros aspectos.

Para notas de qualidade, fixe critérios, âncoras e regra de consolidação antes das consultas.
Preserve as notas individuais e explique as consolidadas. Não calcule médias ou medianas de
prioridades incompatíveis; notas com critérios ou acessos diferentes são apresentadas por
escopo. Retorne composição, modelos, acesso, cobertura, concordâncias, controvérsias e suas
resoluções ou provas pendentes. Sem contextos independentes, declare o painel não realizado
e a análise como individual.

## Examinar e fundamentar

Examine a forma mais fiel disponível para cada critério: jogue, navegue, leia ou opere o
artefato, conforme autorizado, em ambiente de teste e dentro dos limites de ações com efeitos
reais. Para aparência, prefira a interface renderizada em uso, depois capturas, depois código.
Para acessibilidade, use também código, árvore de acessibilidade e tecnologia assistiva.
Medidas vêm do código, de estilos computados ou do arquivo de design; estimativas de captura
são aproximadas. Capturas não demonstram controles, persistência, cooperação ou áudio, e
código lido não comprova execução. Inspeção não substitui testes com o público, incluindo
pessoas com deficiência: indique as hipóteses de alto impacto ou incerteza que os exigem.
Registre passos, condições e materiais examinados; capacidade ou acesso ausentes são limites.

Fora da UI, cada achado traz localização, observação, critério ou mecanismo, impacto,
prioridade justificada pela consequência e pelo alcance, base e recomendação concreta, sem
a escala de UI. Em todo domínio, use IDs estáveis e marque a base como `observado`, `inferido`
ou `hipótese`, citando a evidência. Uma reação prevista do público não é comportamento
observado em pessoas.

Agrupe ocorrências do mesmo problema. Preserve descartes do usuário, salvo evidência nova
declarada. Numa nova versão, marque achados anteriores como resolvidos, persistentes ou
regressões e identifique os novos. Aponte também o que funciona e deve resistir às correções.

## Notas e ciclos de correção

Toda crítica realizada entrega uma nota geral de qualidade, na escala combinada ou, sem ela,
de 0 a 10. Escreva as notas com ponto e exatamente duas casas decimais: `9.73`, `7.00`, `0.00`;
o máximo da escala padrão é `10.00`. Havendo dimensões distintas relevantes, inclua notas por
categoria, como game design e estética, ou usabilidade e acessibilidade, respeitando as
categorias pedidas.

Fixe critérios e âncoras antes do exame, usando os combinados ou declarando os adotados.
Ligue cada nota às evidências, aos pontos fortes e aos problemas que a justificam e explique
a relação da nota geral com as categorias e os pesos. Não suponha média aritmética, e uma
nota alta não compensa uma exigência descumprida. As duas casas são formato, não precisão
estatística: declare cobertura e incerteza. Em exame parcial, a nota vale para a parte
examinada; sem material suficiente, declare a crítica não realizada em vez de dar nota.
Nota de qualidade e severidade são medidas distintas, e a severidade de UI continua de 0 a 4.
Não crie um limiar de aprovação por conta própria.

A crítica não edita o produto. Um ciclo de correção só prossegue com a implementação e as
novas avaliações autorizadas. Antes da primeira rodada, fixe critérios, limiar eventual, regra
de avaliação e condição de parada, com limite de rodadas quando combinado. Quem implementa
confere o feedback com `tratar-revisao`, corrige por prioridade e repete as provas afetadas:
as sugestões do crítico são meios a conferir, não requisitos. Cada nova crítica avalia a
versão resultante. Não repita a avaliação da mesma versão até obter nota favorável, não baixe
o limiar e não troque o crítico para aprovar. Preserve versões recuperáveis para comparar;
a última não é automaticamente a melhor. Encerre ao cumprir os critérios ou atingir a condição
de parada, relatando notas, problemas e provas ausentes. Notas não substituem provas técnicas
nem `verificar-aceite`.

## Retornar

Responda em português, salvo pedido diferente, com:

- contexto, versão, especialização, critérios e formas de acesso;
- achados por prioridade, com evidências;
- o que preservar, e as divergências deliberadas e sugestões de direção, separadas dos achados;
- cobertura, limites e provas recomendadas;
- nota geral e notas por categoria pertinentes, com justificativas. A conclusão pelo limiar
  só existe quando ele foi combinado.

Num painel, preserve divergências e autoria dos achados. Sem problema relevante, diga isso
com a cobertura examinada.
