# Changelog

Mudanças relevantes para quem usa ou adota a coleção. O formato segue o
[Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/). As versões seguem o
[SemVer](https://semver.org/lang/pt-BR/); na série 0.x, uma versão MINOR pode quebrar
compatibilidade.

## [Não lançado]

## [0.2.0] - 2026-11-02

### Adicionado

- Ícone do plugin em `.claude-plugin/icon.png`: uma rede neural com um caminho de ativação,
  no estilo do banner.
- `check.py` recusa nomes de skills renomeadas citados como skill. Lê as renomeações deste
  CHANGELOG; os trechos em que um nome antigo continua correto ficam listados no script.

### Mudado

- Os identificadores das skills passam a ser em português, com verbo no infinitivo derivado do
  título ou do glossário, como em `docs/STANDARDS.md`. O comando corresponde ao título, e a coleção
  deixa de colidir com `/review` do Claude Code e com nomes de outras coleções. Não há aliases.
- Papéis, chaves `roles.*` da política de modelos, grupos, arquivos de apoio e o nome do plugin
  não mudam.
- Para migrar, troque os nomes nas suas chamadas (`/jordyfontoura-skills:<skill>`, `$<skill>`)
  e no bloco copiado de `docs/ADOPTING.md` para o `AGENTS.md` ou `CLAUDE.md` do seu projeto. Numa
  cópia editável, `atualizar-harness` usa a lista abaixo. Para manter os nomes antigos, fixe a
  versão `v0.1.0`.

### Renomeações

- `address-review` passou a se chamar `tratar-revisao`.
- `architecture-review` passou a se chamar `examinar-arquitetura`.
- `clarify` passou a se chamar `esclarecer`.
- `council` passou a se chamar `conselho`.
- `delegate` passou a se chamar `delegar`.
- `diagnose` passou a se chamar `diagnosticar`.
- `evaluate` passou a se chamar `verificar-aceite`.
- `handoff` passou a se chamar `passar-contexto`.
- `implement` passou a se chamar `implementar`.
- `improve-harness` passou a se chamar `melhorar-harness`.
- `integrate` passou a se chamar `integrar`.
- `interview` passou a se chamar `entrevistar`.
- `interview-async` passou a se chamar `entrevistar-por-arquivo`.
- `progress` passou a se chamar `andamento`.
- `propose` passou a se chamar `propor`.
- `prototype` passou a se chamar `prototipar`.
- `pull-request` passou a se chamar `descrever-pr`.
- `reconcile` passou a se chamar `reconciliar`.
- `research` passou a se chamar `pesquisar-web`.
- `review` passou a se chamar `revisar`.
- `setup-harness` passou a se chamar `configurar-harness`.
- `specify` passou a se chamar `especificar`.
- `toolbox` passou a se chamar `conhecer-ferramentas`.
- `unslop` passou a se chamar `escrever-claro`.
- `update-harness` passou a se chamar `atualizar-harness`.
- `write-goal` passou a se chamar `escrever-objetivo`.

## [0.1.0] - 2026-11-01

### Adicionado

- Primeira versão pública, com 26 skills e 3 papéis em português.
- Plugin `jordyfontoura-skills` no marketplace `jordyfontoura`, para Claude Code e Codex.
  O Codex não recebe os papéis pelo plugin.
- `.agents/models.example.toml`, uma política de modelos que herda o ambiente.

### Mudado

- Skills e papéis citam outras skills e papéis pelo nome, sem links entre pastas. Cada skill
  funciona copiada sozinha.
- A origem passa a ser [jordyfontoura/skills](https://github.com/jordyfontoura/skills).

### Origem

Esta versão começa um histórico novo. Ela corresponde à revisão abaixo do repositório privado
anterior, `jordyfontoura/harness`, que fica arquivado. A árvore publicada difere dela apenas
por esta seção do CHANGELOG.

- Revisão anterior: `jordyfontoura/harness@c647efa3b0fc88e94b8afa32a80ddf67de9c7c0a`.

### Renomeações anteriores à publicação

Projetos que adotaram versões antigas por cópia podem encontrar estes nomes:

- `retro` passou a se chamar `improve-harness`.
- `pera-ai` passou a se chamar `clarify`.
- O modo assíncrono de `interview` (`interview/async.md`) virou a skill `interview-async`.
- `alinhamento.template.md`, em `interview-async`, passou a se chamar `alignment.template.md`.
