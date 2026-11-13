<!-- Gerado de knowledge/README.md; edite a fonte no harness. -->

# Biblioteca de referências

Consulte os arquivos pertinentes à tarefa, sem carregar toda a biblioteca. Skills contêm
procedimentos; esta pasta reúne conhecimento reutilizável por domínio ou tema transversal.
Requisitos, design systems e decisões específicos continuam no projeto de destino.

| Referência | Quando consultar |
| --- | --- |
| [Usabilidade, tarefas e fluxos](ux/usability.md) | Compreensão, navegação, aprendizagem e recuperação de erros em interfaces. |
| [Hierarquia, estados, conteúdo e escolha](ux/states-and-content.md) | Composição, mensagens, interação, adaptação e padrões enganosos. |
| [Convenções de plataforma](ux/platform-conventions.md) | Entradas, navegação do sistema, janelas e integrações. |
| [Acessibilidade por forma de acesso](accessibility/interface-criteria.md) | Critérios WCAG e WCAG2ICT que cada forma de inspeção permite examinar. |

UI é compartilhada entre frontend, aplicações nativas e jogos; não replique o mesmo guia por
domínio. Pastas como `games`, `frontend`, `legal` e `scientific-research` podem surgir quando
houver material útil, com nomes de arquivos em inglês e texto em português. Não crie pastas
vazias nem transforme os exemplos de domínio numa taxonomia obrigatória.

Cada referência declara aplicabilidade, origem, fontes e limites. Separe sínteses de fontes,
recomendações contextuais e políticas locais. Registre versão ou data conferida; em direito,
a jurisdição e a vigência são parte do contexto; em pesquisa científica, indique o desenho
do estudo, a população e os limites das evidências. Confirme uma fonte vigente quando ela
for decisiva, sem apresentar uma data de extração como nova pesquisa. Guias não concedem
autorizações nem substituem decisões do projeto ou pisos explícitos do procedimento.

Este índice lista todos os arquivos da biblioteca. Links locais das referências ficam
dentro dela. Uma skill declara dependências com links Markdown diretos aos guias necessários;
evite apontar para o índice quando já souber qual arquivo precisa, pois isso empacotaria
a biblioteca inteira. Não use uma cadeia de guias como requisito de leitura indiscriminada.

Edite apenas estas fontes. O plugin completo usa os arquivos na raiz do pacote. `sync.py`
gera cópias dos guias referenciados em `references/knowledge/` de cada skill avulsa, incluindo
dependências transitivas e ajustando links. O cabeçalho das cópias identifica a origem;
elas são artefatos de distribuição, não outra fonte editável no harness.

Nas instalações pelo CLI, os mesmos guias ficam uma única vez em `knowledge/harness/`,
na raiz do projeto, para Codex e Claude Code. A skill `consultar-conhecimento` e as demais
skills instaladas apontam para essa biblioteca. O índice ajuda a escolher o que ler;
instalar a biblioteca não obriga seu carregamento completo em cada sessão.
