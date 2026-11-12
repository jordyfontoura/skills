# Changelog

Mudanças relevantes para quem usa ou adota a coleção. O formato segue o
[Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/). As versões seguem o
[SemVer](https://semver.org/lang/pt-BR/); na série 0.x, uma versão MINOR pode quebrar
compatibilidade.

## [Não lançado]

### Adicionado

- Biblioteca `knowledge/` com referências de UI e acessibilidade compartilhadas por
  `criticar`, `implementar` e `prototipar`. Procedimentos, pisos e escalas continuam nas skills.
  O índice declara os arquivos disponíveis; os guias registram aplicabilidade, origem,
  fontes e limites. Outros domínios entram quando houver conteúdo útil.
- Empacotamento seletivo das referências em `references/knowledge/` das cópias avulsas,
  incluindo dependências transitivas e links ajustados. O plugin completo usa a biblioteca
  na raiz. A validação continua recusando links arbitrários fora da skill e verifica índice,
  integridade das cópias e isolamento da biblioteca. Atualização e adoção preservam adaptações locais.
- `examinar-eficiencia`: explica por que o trabalho com o agente demorou ou gastou muitos
  tokens e propõe a menor mudança para cada causa, sem cortar verificações úteis. Usa a conversa,
  diffs, verificações e métricas expostas; lê logs locais de sessão só a pedido. Não estima
  tokens por contagem de palavras e encaminha causas nas instruções para `melhorar-harness`.
- `criticar`: critica artefatos e experiências com critérios especializados pelo pedido,
  público e referências. Preserva a rubrica de UI e UX em apoios, compõe com `conselho` para
  várias perspectivas e usa `roles.council` para consultas independentes, inclusive individuais.
  Sempre entrega nota geral e notas por categoria quando pertinentes, com duas casas decimais
  (como `9.73`), na escala padrão de 0 a 10. Distingue severidade de qualidade e orienta
  ciclos de correção autorizados, com condição
  de parada, sem substituir provas técnicas ou aceite independente.

### Mudado

- `andamento`: cobre o pedido inteiro até sua condição de conclusão, com mudanças desde o
  último resumo, próxima entrega utilizável e previsão fundamentada quando pertinente.
  Perguntas sobre tempo sempre recebem uma estimativa com base e incertezas ou o motivo de
  ainda não estimar e o marco necessário. Distingue etapas de conclusão total e trabalho
  ativo de esperas externas, sem percentual inventado, medições novas ou acompanhamento periódico.
- As duas entradas de crítica de interface foram reunidas em `criticar`. A rubrica foi
  preservada em `criticar/interface-rubric.md`, o método em `interface.md` e o painel de UI em
  `interface-panel.md`. Para quem adotou `nightly`, `atualizar-harness` deve migrar chamadas e
  apoios, preservando adaptações locais; a ausência dos diretórios antigos não autoriza
  apagá-los no destino. Use `criticar` com `conselho` para várias perspectivas, sem aliases.
- `criticar-interface` passou a se chamar `criticar`.
- `criticar-interface-em-conselho` passou a se chamar `criticar`.
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
