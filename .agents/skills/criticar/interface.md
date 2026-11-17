# Rubrica de interface

Leia ao criticar UI e UX, inclusive a interface de jogos.

Fixe público, tarefas principais e de saída, plataforma, entradas, tamanhos de tela, temas,
etapa, design system, guias de marca e conteúdo, meta de acessibilidade e versão em escopo.
Em exploração, priorize fluxos e estrutura e agrupe acabamento; antes do lançamento, examine
também acabamento e estados por completo. A etapa muda o foco, não a severidade.

Diretrizes do projeto e da plataforma prevalecem em convenções, estilo e componentes. Dois
pisos não cedem: **WCAG 2.2 nível AA**, ou meta mais exigente, inclusive legal, e **escolha da
pessoa**, pela qual a interface não leva ninguém a decidir contra o próprio interesse.
Registre conflitos com esses pisos sem rebaixar a severidade.

## As sete seções

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

## Severidade e formato dos achados

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

## Painel de interface

Num painel, siga também [panel.md](panel.md). O padrão é de 3 a 5 avaliadores. Cada um
examina a interface inteira nas sete seções e aprofunda usabilidade, acessibilidade,
hierarquia, conteúdo ou plataforma conforme os riscos. A faixa vem de avaliações humanas e
não garante independência entre instâncias de IA.

Consolide a severidade assim:

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
notas de avaliadores sem o mesmo acesso não a rebaixam. A escala de severidade e a faixa de
avaliadores valem para UI, não para jogos, textos ou outros aspectos.
