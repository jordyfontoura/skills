# Arquitetura

Este repositório contém procedimentos em Markdown e configurações opcionais de provedores.

- `AGENTS.md` é o ponto de entrada compartilhado. `.claude/CLAUDE.md` o importa para Claude Code;
  fora da raiz, ele não é confundido com instruções do plugin.
- `skills/<grupo>/<nome>/SKILL.md` contém cada skill canônica e suas referências de apoio.
  Os grupos são `development`, `productivity` e `harness`; os nomes das skills são únicos.
- `knowledge/` contém referências de domínio compartilhadas, catalogadas em `knowledge/README.md`.
  As skills mantêm procedimentos e políticas e declaram seus guias com links diretos.
- `.agents/skills/<nome>/` e `.claude/skills/<nome>/` são cópias sem categorias para uso dos agentes.
- `.agents/roles/` contém instruções canônicas de `planner`, `evaluator` e `representative`.
- `.agents/models.toml` define perfis e seleção por papel e complexidade; `docs/MODELS.md`
  explica a versão 2 e a compatibilidade com a versão 1. `.agents/models.example.toml` é o
  ponto de partida neutro para quem adota.
- `.claude/agents/` adapta os papéis canônicos ao Claude Code.
- `.codex/agents/` contém papéis em TOML para Codex. O Codex lê as cópias em `.agents/skills/`.
- `.claude-plugin/plugin.json` descreve o plugin `jordyfontoura-skills`, com os grupos de
  `skills/` e a versão. `.claude-plugin/marketplace.json` publica o repositório como o
  marketplace `jordyfontoura`; Claude Code e Codex leem os mesmos arquivos.
- `agents/` é a cópia de `.claude/agents/` que o plugin carrega. O Codex não recebe papéis
  pelo plugin.
- `scripts/catalog.py` lê o catálogo e o índice de conhecimento, resolve dependências
  transitivas e adapta links relativos ao layout de instalação.
- `scripts/sync.py` gera as cópias das skills e de `agents/`, sem editar as fontes ou remover
  arquivos extras.
- `scripts/check.py` valida metadados, links, configuração, manifestos do plugin e consistência
  das cópias. Links que saem de uma skill só podem apontar para referências catalogadas em
  `knowledge/`. O validador recusa links arbitrários, arquivos fora do índice, escapes da
  biblioteca, componentes executáveis no plugin e caracteres invisíveis.
- `scripts/model_policy.py` valida e consulta a política, sem executar agentes ou fazer rede.
- `.github/workflows/ci.yml` executa essa verificação e os testes do validador.
- `cli/` contém o pacote TypeScript `@jordyfontoura/skills`. `scripts/package_cli.py` usa
  `catalog.py` para empacotar cópias completas, papéis e o exemplo neutro de modelos.
  O pacote publicado usa apenas Node.js; Python permanece na manutenção da origem.

As cópias preservam as instruções das fontes. A geração ajusta somente links Markdown relativos
para os arquivos correspondentes no layout de uso; blocos de código e links externos são preservados.
O plugin completo usa as fontes e a biblioteca na raiz do pacote. Nas cópias avulsas, cada
skill recebe seus guias em `references/knowledge/`, com procedência e links internos ajustados.
Um mesmo guia pode ter várias cópias geradas, mas é editado apenas em `knowledge/` na origem.
O empacotamento inclui apenas o fechamento das dependências declaradas por links Markdown,
inclusive links de referência; não depende de symlinks, variáveis de provedor ou rede.
`sync.py` continua recusando arquivos extras em vez de apagar adaptações.
Os papéis acrescentam os metadados próprios de cada provedor. Quem inicia a consulta lê a política
local e verifica as capacidades reais das ferramentas. Campos nativos dos provedores não são
alterados por essa política. Os scripts de manutenção usam apenas a biblioteca padrão do Python.

O CLI acrescenta um build Node.js opcional, com dependências fixadas em `cli/package-lock.json`.
O pacote npm leva JavaScript compilado e conteúdo pronto, sem fontes Python ou TypeScript.
Como o marketplace aponta para a raiz, o cache do plugin pode conter a pasta `cli/`; ela
não registra executáveis no manifesto e não é executada pelo plugin. A validação continua
recusando `bin/`, hooks e comandos executáveis na raiz.

No destino, o CLI confere os arquivos antes de gravar, recusa conflitos e links simbólicos,
mantém os arquivos idênticos e preserva políticas locais de modelos. Recibos imutáveis em
`.harness/receipts/` registram seleção, origem, SHA de base e hashes de conteúdo. `status`
identifica alterações e ausências sem rede; a mesclagem continua na skill `atualizar-harness`.

O contexto de trabalho fica na conversa e nos documentos existentes. Uma especificação ou
passagem de contexto em Markdown pode preservar tarefas longas; não há formato de registro,
serviço ou banco de tarefas obrigatório. O harness não instala hooks, gerencia sessões
nem mantém processos em segundo plano.

Nomes de skills ficam em português; papéis, grupos, arquivos e demais identificadores, em inglês.
Textos de leitura ficam em português brasileiro,
conforme os [padrões](STANDARDS.md). A mesma regra vale para fontes e cópias dos provedores.
