# Direção visual e comportamento da interface

Leia ao implementar ou prototipar uma interface. Reutilize o produto e o design system existentes:
tokens, componentes, linguagem, conteúdo e padrões de interação. Uma referência externa não
autoriza trocar a identidade do projeto. Se não houver direção definida, proponha uma coerente
com o público e a tarefa; não imponha preferências estéticas como regras universais.

## Compor para a tarefa

Identifique a ação principal e a informação necessária para realizá-la. Use hierarquia,
tipografia, espaçamento e contraste para tornar essa ordem legível. Escolha a densidade pelo
conteúdo e pelo contexto de uso; não converta tudo em cartões nem corte informação só para
obter uma composição limpa. Conteúdo real orienta o layout; identifique dados simulados.

Preserve nomes e componentes consistentes. Deixe explícitas ações com consequências diferentes,
sem promessas que o produto não cumpre. Use `escrever-claro` para revisar o texto de interface mantendo
as condições necessárias à compreensão.

## Cobrir estados e acesso

Inclua os estados relevantes à jornada: carregando, vazio, sucesso, erro e indisponibilidade.
Mensagens de erro explicam o problema e, quando possível, como continuar, sem apagar a entrada
do usuário desnecessariamente. Estado vazio pode orientar a próxima ação quando ela existir.

Confira navegação por teclado, ordem de foco, foco visível, nomes acessíveis dos controles
e compreensão sem depender só de cor ou posição. Use componentes semânticos e preserve suas
capacidades de acessibilidade. A aparência de um botão não demonstra que ele é operável.

Reorganize o conteúdo nos tamanhos combinados sem sobreposição ou perda de ações essenciais.
Use movimento quando ajudar a entender a mudança e respeite a preferência por movimento
reduzido. Não acrescente animação apenas para preencher a tela.

## Conferir o resultado

Inspecione o resultado renderizado e percorra as interações pertinentes. Compare com a
referência aprovada e transforme estados e ações relevantes em critérios `visual` ou `run`,
seguindo [testing.md](testing.md). Registre o que foi observado e o que não pôde ser examinado;
uma captura estática não prova navegação, persistência ou conformidade completa de acessibilidade.
Um protótipo pode simular mecanismos, mas precisa declarar os limites dessa simulação.
Para uma crítica estruturada da experiência de uso, use a skill `criticar-interface`.

Inspiração de direção visual: [frontend-design, da Anthropic](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md).
As orientações são adaptadas ao projeto, sem impor a estética da referência.
