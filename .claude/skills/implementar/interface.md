# Direção visual e comportamento da interface

Leia ao implementar ou prototipar uma interface. Reutilize o produto e o design system existentes:
tokens, componentes, linguagem, conteúdo e padrões de interação. Uma referência externa não
autoriza trocar a identidade do projeto. Se não houver direção definida, proponha uma coerente
com o público e a tarefa; não imponha preferências estéticas como regras universais.

## Compor para a tarefa

Identifique a ação principal e a informação necessária para realizá-la. Consulte os guias de
[usabilidade](references/knowledge/ux/usability.md) e de
[hierarquia, estados e conteúdo](references/knowledge/ux/states-and-content.md).
Não converta tudo em cartões nem corte informação só para obter uma composição limpa.
Conteúdo real orienta o layout; identifique dados simulados. Use `escrever-claro` para revisar
o texto de interface mantendo as condições necessárias à compreensão.

## Cobrir estados e acesso

Selecione no guia os estados e extremos pertinentes à jornada. Confira os
[critérios de acessibilidade](references/knowledge/accessibility/interface-criteria.md) e as
[convenções da plataforma](references/knowledge/ux/platform-conventions.md) adotada.
Use componentes semânticos e preserve suas capacidades de acessibilidade. A aparência de
um botão não demonstra que ele é operável. Reorganize o conteúdo nos tamanhos combinados e
respeite a preferência por movimento reduzido; não acrescente animação só para preencher a tela.

## Conferir o resultado

Inspecione o resultado renderizado e percorra as interações pertinentes. Compare com a
referência aprovada e transforme estados e ações relevantes em critérios `visual` ou `run`,
seguindo [testing.md](testing.md). Registre o que foi observado e o que não pôde ser examinado;
uma captura estática não prova navegação, persistência ou conformidade completa de acessibilidade.
Um protótipo pode simular mecanismos, mas precisa declarar os limites dessa simulação.
Para uma crítica estruturada da experiência de uso, use `criticar` com seu apoio de interface.

Inspiração de direção visual: [frontend-design, da Anthropic](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md).
As orientações são adaptadas ao projeto, sem impor a estética da referência.
