# Ferramentas de apoio ao agente

Catálogo de usos, não lista de instalações obrigatórias. Descubra disponibilidade e versão
no ambiente real. Comandos abaixo são exemplos de uso; instalação e configuração seguem
o escopo de `conhecer-ferramentas`. Leia a ajuda da versão instalada antes de usar opções específicas.

## Encontrar código e recuperar contexto

- **ripgrep (`rg`):** busca textual e seleção de arquivos; use `rg --files` e buscas delimitadas
  antes de carregar árvores inteiras. A fonte é [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep).
- **ast-grep:** encontra padrões sintáticos de código. Complemente o `rg` quando texto ou regex
  não distinguirem as estruturas relevantes. O pacote npm é `@ast-grep/cli`; os executáveis
  são `ast-grep` e `sg`. Prefira o nome menos ambíguo e comece em modo de busca, sem reescrita.
  [Guia oficial](https://ast-grep.github.io/guide/quick-start.html).
- **QMD:** busca em documentos locais indexados, usada diretamente pelo agente. Serve para
  corpus grande ou vocabulário incerto; para termo conhecido, `rg` delimitado basta e está
  sempre atualizado. [Projeto oficial](https://github.com/tobi/qmd).
  - `qmd search` (BM25) é o padrão e não usa modelos. Use `query` ou `vsearch` só com os
    modelos já em cache e embeddings atualizados, escrevendo `intent:`, `lex:` e `vec:`.
    Sem os modelos, eles baixam cerca de 2 GB e podem travar sem erro.
  - Informe sempre `--index` e `-c`, com `-n 3` a `5`, `--json` e `--full-path`. Índice
    inexistente é criado vazio e devolve `[]` sem erro; confirme com
    `qmd --index <índice> collection list`.
  - O índice não avisa quando está desatualizado e pode devolver texto que não existe mais.
    Não cite snippet, docid nem score: leia o arquivo atual na linha do resultado e cite
    caminho e linhas. Busca vazia não prova que algo não existe.
  - Sem autorização, não rode `update`, `embed`, `pull`, `init`, `collection add` nem `trust`;
    não use `mcp --http` nem variáveis `QMD_TRUST_*`. Exija a versão 2.8.3 ou posterior.
    Prefira um índice por projeto restrito a `**/*.md`; não indexe a máquina, `.env` ou logs.
  - Exemplo: `qmd --index harness search 'representante' -c harness-docs -n 3 --json --full-path`.
    O nome do índice é uma escolha deste projeto, não uma convenção obrigatória.
- **Repomix:** prepara pacotes de contexto para sessões sem acesso ao checkout. Selecione
  arquivos por inclusão explícita e confira a saída antes de compartilhar. Evite incluir
  segredos, artefatos ou cópias geradas da mesma fonte. Ler um recorte diretamente costuma
  bastar quando o agente já acessa o repositório. [Guia oficial](https://repomix.com/guide/usage).

## Verificar interfaces

**Playwright CLI:** automatiza interações, snapshots e capturas em sessões de navegador.
O pacote npm é `@playwright/cli` e o comando é `playwright-cli`. Não confunda instalar a CLI
com instalar navegadores, extensões ou as skills oferecidas pelo pacote. Um navegador já
disponível pode atender ao piloto. Use uma sessão própria e feche apenas o que abriu.

Confira os comandos na ajuda local. Um fluxo típico é abrir uma página, obter snapshot,
agir sobre controles observados e conferir o estado final. Para uma regressão durável,
considere os testes automatizados que o projeto já utiliza. Uma captura não comprova salvar
ou recuperar dados. Se o protocolo `file:` for bloqueado, use uma fixture servida localmente
por HTTP quando isso estiver autorizado, sem desabilitar a restrição.
[Documentação oficial](https://github.com/microsoft/playwright-cli).

## Executar comandos e tratar o GitHub

- **just:** reúne receitas que chamam os comandos reais do projeto. Não é um serviço de
  tarefas e não substitui suas verificações. No Windows, configure o shell de acordo com os
  comandos usados; não suponha sintaxe Bash no PowerShell. Para poucos comandos estáveis,
  a documentação existente pode bastar. [Manual](https://just.systems/man/en/prerequisites.html).
- **uv:** executa ferramentas Python em ambientes isolados. Distinga execução temporária
  de instalação persistente e fixe versões quando a reprodução exigir. Não modifica o Python
  do produto só para executar uma ferramenta auxiliar. [Guia](https://docs.astral.sh/uv/guides/tools/).
- **GitHub CLI (`gh`):** consulta PRs, comentários e checks, com saída estruturada quando
  suportada. Ler, publicar resposta, fazer push e integrar são ações diferentes; siga
  `tratar-revisao` e `integrar` dentro da autorização. [Manual](https://cli.github.com/manual/).

## Opções para avaliar depois

- **RTK:** filtra saídas de comandos para reduzir o contexto apresentado ao agente. Teste
  preservando saídas integrais necessárias à prova e ao diagnóstico. Não assuma a economia
  anunciada como resultado local nem instale hooks automáticos por adotá-lo.
  [Projeto oficial](https://github.com/rtk-ai/rtk).
- **MCPorter:** descobre e chama ferramentas MCP pelo terminal e pode gerar CLIs específicas.
  Só acrescente essa camada se houver necessidade fora dos conectores já disponíveis.
  Servidores, credenciais e ações chamadas mantêm seus próprios limites de autorização.
  [Projeto oficial](https://github.com/steipete/mcporter).
