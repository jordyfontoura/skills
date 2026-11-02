# Arquitetura

Este repositório contém procedimentos em Markdown e configurações opcionais de provedores.

- `AGENTS.md` é o ponto de entrada compartilhado. `.claude/CLAUDE.md` o importa para Claude Code;
  fora da raiz, ele não é confundido com instruções do plugin.
- `skills/<grupo>/<nome>/SKILL.md` contém cada skill canônica e suas referências de apoio.
  Os grupos são `development`, `productivity` e `harness`; os nomes das skills são únicos.
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
- `scripts/catalog.py` lê o catálogo e adapta links relativos ao layout de instalação.
- `scripts/sync.py` gera as cópias das skills e de `agents/`, sem editar as fontes ou remover
  arquivos extras.
- `scripts/check.py` valida metadados, links, configuração, manifestos do plugin e consistência
  das cópias. Ele recusa links que saiam da pasta de uma skill, componentes executáveis no
  plugin e caracteres invisíveis.
- `scripts/model_policy.py` valida e consulta a política, sem executar agentes ou fazer rede.
- `.github/workflows/ci.yml` executa essa verificação e os testes do validador.

As cópias preservam as instruções das fontes. A geração ajusta somente links Markdown relativos
para os arquivos correspondentes no layout de uso; blocos de código e links externos são preservados.
Os papéis acrescentam os metadados próprios de cada provedor. Quem inicia a consulta lê a política
local e verifica as capacidades reais das ferramentas. Campos nativos dos provedores não são
alterados por essa política. Os scripts de manutenção usam apenas a biblioteca padrão do Python.

O contexto de trabalho fica na conversa e nos documentos existentes. Uma especificação ou
passagem de contexto em Markdown pode preservar tarefas longas; não há formato de registro,
serviço ou banco de tarefas obrigatório. O harness não instala hooks, gerencia sessões
nem mantém processos em segundo plano.

Identificadores permanecem em inglês. Textos de leitura ficam em português brasileiro,
conforme os [padrões](STANDARDS.md). A mesma regra vale para fontes e cópias dos provedores.
