# Changelog

Mudanças relevantes para quem usa ou adota a coleção. O formato segue o
[Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/). As versões seguem o
[SemVer](https://semver.org/lang/pt-BR/); na série 0.x, uma versão MINOR pode quebrar
compatibilidade.

## [Não lançado]

### Adicionado

- `criticar-interface`: critica UI e UX com uma rubrica fixa: percurso cognitivo, heurísticas
  de Nielsen, WCAG 2.2 AA (com WCAG2ICT fora da web), hierarquia visual, conteúdo, confiança e
  escolha, estados e convenções da plataforma. Cada achado traz padrão, impacto, severidade de
  0 a 4 com notas definidas e a base no material examinado. Decisões do projeto não reduzem os
  pisos de acessibilidade e de escolha da pessoa. A skill consulta o design system do projeto
  e as diretrizes vigentes da plataforma, com `pesquisar-web` quando houver acesso, e declara
  o que não pôde examinar.
- `criticar-interface-em-conselho`: reúne avaliadores independentes com a mesma rubrica, agrupa
  achados com rastreio, pede a todos notas para a lista consolidada e registra mediana,
  intervalo e controvérsias, seguindo `conselho`. `conselho` passa a encaminhar críticas de
  interface para essa skill.

### Mudado

- Desenvolvimento e PRs passam a usar a branch permanente `nightly`; `main` é o canal estável,
  com promoções integrais e tags de versão. CI verifica ambos os canais e o Dependabot abre
  PRs para `nightly`.
- `atualizar-harness`: respeita a revisão pedida ou o canal escolhido e registrado no destino.
  Nesta coleção, usa `main` por padrão e permite acompanhar `nightly`, fixando o SHA adotado.
- `diagnosticar`: quando variantes do mesmo defeito reaparecem no mesmo mecanismo, mesmo com
  cada correção passando, mapeia estados, transições e invariantes antes da próxima correção e
  confere a solução com oráculos independentes. `implementar`, `delegar` e `escrever-objetivo`
  acionam `diagnosticar` nessa situação.
- `especificar` e `implementar`: cada fase começa por uma jornada representativa com a fixture
  aprovada; testes específicos continuam cobrindo os detalhes.
- `especificar`: cada prova indica as funcionalidades que exige e a fase que as entrega; o aceite
  de uma fase não depende de funcionalidade de fase posterior.
- `testing.md` (em `implementar`) e `verificar-aceite`: verificações rápidas, regressões e
  jornadas afetadas vêm antes da revisão, e a campanha completa roda só no candidato
  estabilizado. Um resultado vale para a revisão em que foi obtido. Uma execução só atende a
  várias obrigações quando preserva os controles de cada uma e consta do plano.
- `configurar-harness`: testes do validador usam fixtures mínimas próprias, separadas da
  verificação do repositório real, e o índice de comandos põe o validador antes das suítes longas.
- `escrever-objetivo`, `delegar` e `passar-contexto`: o objetivo autoriza avançar tarefas com
  dependências satisfeitas, preservando os portões; durante esperas, a execução avança trabalho
  independente e relata só mudanças de estado; a passagem lista tarefas e processos ativos e
  liga cada resultado à revisão a que se aplica.

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
