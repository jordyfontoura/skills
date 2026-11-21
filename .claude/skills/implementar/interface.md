# Direção visual e comportamento da interface

Leia ao implementar ou prototipar uma interface. Reutilize o produto e o design system existentes:
tokens, componentes, linguagem, conteúdo e padrões de interação. Uma referência externa não
autoriza trocar a identidade do projeto. Se não houver direção definida, proponha uma coerente
com o público e a tarefa; não imponha preferências estéticas como regras universais.

## Definir a direção quando estiver aberta

Distinga refinamento de mudança de identidade. Consulte [direção visual e tokens](../../../knowledge/ux/visual-direction.md)
para relacionar público, tarefa, conteúdo, estados, hierarquia, paleta, tipografia e densidade.
Apresente as escolhas ainda abertas num brief curto; use `entrevistar` quando uma decisão
humana mudar o escopo ou a direção. Preserve aprovações anteriores e a autonomia já concedida;
um ajuste delimitado não exige nova entrevista nem aprovação por rotina.

Use `prototipar` quando um experimento esclarecer uma escolha e `especificar` quando faltar
definição relevante de comportamento ou prova. Registre direção e tokens no projeto de
destino, junto da fonte já adotada; integre saídas externas aos componentes existentes sem
criar um tema ou documento concorrente. Ferramenta externa só entra quando disponível e
autorizada, sem se tornar requisito para aplicar este procedimento.

## Compor para a tarefa

Identifique a ação principal e a informação necessária para realizá-la. Consulte os guias de
[usabilidade](../../../knowledge/ux/usability.md) e de
[hierarquia, estados e conteúdo](../../../knowledge/ux/states-and-content.md).
Não converta tudo em cartões nem corte informação só para obter uma composição limpa.
Conteúdo real orienta o layout; identifique dados simulados. Use `escrever-claro` para revisar
o texto de interface mantendo as condições necessárias à compreensão.

## Cobrir estados e acesso

Selecione no guia os estados e extremos pertinentes à jornada. Confira os
[critérios de acessibilidade](../../../knowledge/accessibility/interface-criteria.md) e as
[convenções da plataforma](../../../knowledge/ux/platform-conventions.md) adotada.
Use componentes semânticos e preserve suas capacidades de acessibilidade. A aparência de
um botão não demonstra que ele é operável. Reorganize o conteúdo nos tamanhos combinados e
respeite a preferência por movimento reduzido; não acrescente animação só para preencher a tela.
Quando houver animação, consulte [movimento e animação](../../../knowledge/ux/motion.md).
Defina sua função e o retorno equivalente com movimento reduzido; confira interrupção e
limpeza no ciclo de vida da interface. Reutilize recursos existentes e avalie GSAP apenas
em projetos web quando a necessidade justificar sua adoção.

## Conferir o resultado

Inspecione o resultado renderizado e percorra as interações pertinentes. Compare com a
referência aprovada e transforme estados e ações relevantes em critérios `visual` ou `run`,
seguindo [testing.md](testing.md). Registre o que foi observado e o que não pôde ser examinado;
uma captura estática não prova navegação, persistência ou conformidade completa de acessibilidade.
Um protótipo pode simular mecanismos, mas precisa declarar os limites dessa simulação.
No acabamento, confira espaçamento, tipografia, alinhamento, conteúdo e estados contra o
design system. Diferencie um defeito local de uma inconsistência no token ou componente
compartilhado e corrija a origem. Acabamento não autoriza redesign. Repita as provas afetadas.
Para uma crítica estruturada da experiência de uso, use a rubrica de interface de `criticar`.
