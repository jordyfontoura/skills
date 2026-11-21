# Biblioteca de referências

Consulte os arquivos pertinentes à tarefa, sem carregar toda a biblioteca. Skills contêm
procedimentos; esta pasta reúne conhecimento reutilizável por domínio ou tema transversal.
Requisitos, design systems e decisões específicos continuam no projeto de destino.

| Referência | Quando consultar |
| --- | --- |
| [Usabilidade, tarefas e fluxos](ux/usability.md) | Compreensão, navegação, aprendizagem e recuperação de erros em interfaces. |
| [Hierarquia, estados, conteúdo e escolha](ux/states-and-content.md) | Composição, mensagens, interação, adaptação e padrões enganosos. |
| [Direção visual e tokens](ux/visual-direction.md) | Paleta, tipografia, densidade e tokens quando a direção estiver aberta ou sua coerência precisar de avaliação. |
| [Movimento e animação de interfaces](ux/motion.md) | Finalidade, interrupção, movimento reduzido, desempenho e uso contextual de GSAP na web. |
| [Convenções de plataforma](ux/platform-conventions.md) | Entradas, navegação do sistema, janelas e integrações. |
| [Acessibilidade por forma de acesso](accessibility/interface-criteria.md) | Critérios WCAG e WCAG2ICT que cada forma de inspeção permite examinar. |
| [Fontes de assets para jogos](gamedev/asset-sources.md) | Escolha de arte, áudio, modelos, texturas e addons de terceiros, com a licença de cada site. |
| [Padrões de programação de jogos](gamedev/programming-patterns.md) | Laço de jogo, passo fixo, entidades, comunicação entre sistemas e otimização. |
| [Práticas de engenharia em jogos com Godot](gamedev/engineering-practices.md) | Desempenho, organização de cenas e código, dados, entrada, persistência e versionamento. |
| [Técnicas de game design](gamedev/game-design.md) | Mecânicas, ritmo, dificuldade, resposta ao jogador, escopo e acessibilidade de jogos. |
| [Modelos 3D prontos para jogo](3d-modeling/game-ready-assets.md) | Escala, geometria, UVs, materiais PBR, rig, LOD e colisão em modelos para tempo real. |
| [Pipeline de exportação do Blender para o Godot](3d-modeling/export-pipeline.md) | Formato, opções de exportação, sufixos e opções de importação de cenas e texturas. |
| [Explicação clara](writing/clear-explanation.md) | Explicar um conceito, mecanismo, decisão ou estado em conversa, documento, página ou diagrama. |

UI é compartilhada entre frontend, aplicações nativas e jogos; não replique o mesmo guia por
domínio. Pastas como `frontend`, `legal` e `scientific-research` podem surgir quando
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

Edite apenas estas fontes. O plugin completo e as cópias em `.agents/skills/` e
`.claude/skills/` usam a mesma biblioteca `knowledge/` na raiz. `sync.py` ajusta os links
das skills sem duplicar os guias. Na adoção manual, copie também a biblioteca para a raiz
do projeto de destino, preservando os caminhos e as adaptações existentes.

Nas instalações pelo CLI, os mesmos guias ficam uma única vez em `knowledge/harness/`,
na raiz do projeto, para Codex e Claude Code. A skill `consultar-conhecimento` e as demais
skills instaladas apontam para essa biblioteca. O índice ajuda a escolher o que ler;
instalar a biblioteca não obriga seu carregamento completo em cada sessão.
