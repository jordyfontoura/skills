# Changelog

Mudanças relevantes para quem usa ou adota a coleção. O formato segue o
[Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/). As versões seguem o
[SemVer](https://semver.org/lang/pt-BR/); na série 0.x, uma versão MINOR pode quebrar
compatibilidade.

## [Não lançado]

### Alterado

- `escrever-claro` muda de função: deixa de ser o procedimento de revisão de textos, que
  agora é `redigir`, e passa a aplicar o padrão de explicação clara ao conteúdo pedido, em
  qualquer meio. `AGENTS.md`, o bloco de adoção, o CLI e as skills `criticar`, `implementar`
  e `subir-regua` citam `redigir` onde pediam revisão de texto. O CLI recomenda `redigir`
  por padrão no lugar de `escrever-claro`. Não houve comparação em execuções equivalentes.
- Fontes e créditos de inspiração passam a ficar em `knowledge/references.md`. Skills
  mantêm instruções e avisos de licença; guias apontam para o catálogo compartilhado,
  incluído como dependência nas instalações que o referenciam.
- `andamento`: toda consulta passa a incluir uma faixa de tempo restante até concluir o goal
  ou pedido inteiro. Com pouco contexto, informa uma faixa preliminar com baixa confiança
  e hipóteses; esperas sem prazo ficam como condições fora da estimativa.
- O banner do README ganha animação na rede neural: pulsos entram pelas linhas e percorrem
  as conexões, acendendo os nós. Com movimento reduzido, o banner continua estático.
- `andamento`: o procedimento passa de 86 para 33 linhas e descreve o resultado esperado em
  vez do passo a passo. Mantém a cobertura do pedido inteiro, a previsão fundamentada, a
  leitura sem efeito sobre o trabalho em curso e o cuidado ao observar outra conversa.
- `implementar`, `delegar` e `criticar` passam a descrever o resultado esperado, o formato e
  os limites, sem repetir o que o modelo faz sem instrução nem o roteamento para outras skills.
  `implementar` vai de 63 para 35 linhas e `delegar` de 112 para 88. O `SKILL.md` de `criticar`
  vai de 254 para 110, com 91 linhas em `interface.md` e 29 em `panel.md`.
  Ficam a entrega por jornada, o reaproveitamento do resultado de base, a resolução da política
  de modelos nas versões 1 e 2, o conteúdo do brief, a rubrica de interface com pisos e
  severidade, o painel, as notas com duas casas decimais e os ciclos de correção. Os apoios
  de `implementar` e `delegar` não mudam. Os fundamentos do método de
  interface saem de `criticar` e ficam em `docs/HARNESS.md`. Não houve comparação em execuções
  equivalentes.
- `check.py` recusa também skills removidas citadas como skill. Lê as remoções deste CHANGELOG,
  no formato "- `nome` foi removida.", e aceita renomeações antigas que terminam numa delas.
- O `AGENTS.md` deste repositório deixa de repetir quando usar cada skill; mantém comandos,
  convenções e limites. O bloco de adoção em `docs/ADOPTING.md` não muda.
- `implementar`, `prototipar` e `criticar` consultam direção visual e movimento conforme a
  tarefa, preservando identidade, decisões existentes e separação entre avaliação e correção.
  A documentação explica a convivência opcional com UI/UX Pro Max e Impeccable.
- `criticar` mantém o procedimento geral no `SKILL.md` e traz a rubrica de interface em
  `interface.md` e as regras de painel em `panel.md`, lidos só quando a crítica é de UI ou
  em painel. Os quatro apoios anteriores foram reunidos nesses dois, preservando pisos,
  escalas, independência e consolidação. Os guias de `knowledge/` são consultados conforme o domínio.
- Cópias de `.agents/skills/` e `.claude/skills/` usam `knowledge/` na raiz, sem duplicar
  guias por skill. `sync.py` retira cópias antigas idênticas às geradas e interrompe a
  migração se houver adaptações ou arquivos desconhecidos. A adoção manual inclui a biblioteca.
- `melhorar-harness`: considera simplificar ou retirar componentes com indício de custo ou
  obsolescência, comparando um por vez sem enfraquecer requisitos ou verificações úteis.
- `configurar-harness`: orienta mensagens de falha com local, regra violada e correção possível.

### Adicionado

- `samples/` guarda respostas reais de agentes a cenários fixos, com e sem as skills, para
  cada modelo de `samples/models.toml`. `python scripts/samples.py run` gera as amostras
  desatualizadas com os CLIs do Claude Code e do Codex, e cada cenário ganha um `METRICS.md`
  com tokens, tempo e skills acionadas. A CI acusa amostras desatualizadas nos PRs para `main`.
- Guia `knowledge/writing/clear-explanation.md`: padrão de explicação clara, válido para
  conversa, documento, página ou diagrama. Reúne o que a antiga `esclarecer` ensinava sobre
  partir do leitor, escolher a forma pelo tipo de assunto, definir termos e preservar condições.
- Skill `redigir`: recebe sem mudanças o procedimento de redação e revisão de textos que
  estava em `escrever-claro`, com o aviso de licença do pstack, e aponta para o padrão.
  Quem pedia revisão de texto por `escrever-claro` passa a pedir `redigir`.
- `esclarecer` volta ao catálogo, mais curta: reexplica a mensagem anterior pelo padrão,
  sem executar ações nem tratar a dúvida como aprovação. A remoção de 17/11/2026 não chegou
  a ser lançada.
- Skill `subir-regua`: melhoria em etapas, combinável com `criticar`, `redigir` ou
  outras formas de avaliação. Cada etapa repete avaliar e corrigir em contexto novo até
  cumprir seu critério e então passa ao próximo avaliador ou a uma meta mais alta. Mudanças
  só substituem a referência quando não há regressão, e a escada para na etapa que esgota
  seus ciclos.
- Seção opcional `ladders` na política de modelos v2, validada em Python e no CLI, com
  etapas concretas e `max_cycles` configurável. A política pessoal registra a escada
  `padrao`: Luna XHigh, Haiku XHigh, Sol Medium, Opus Medium e Fable Medium, com 3 ciclos
  por etapa.
- Guias `knowledge/ux/visual-direction.md` e `knowledge/ux/motion.md`: direção e tokens,
  finalidade e interrupção de animações, movimento reduzido e uso contextual de GSAP na web.
  O guia de acessibilidade explicita os critérios temporais 2.2.2 e 2.3.1, ambos de nível A.
- Guias de desenvolvimento de jogos em `knowledge/gamedev/`: fontes de assets com a licença
  de cada site, padrões de programação, práticas de engenharia com Godot e técnicas de game
  design. Cada guia registra as fontes consultadas e o que não pôde ser conferido.
- Guias de modelagem 3D em `knowledge/3d-modeling/`: modelos prontos para jogo e pipeline
  de exportação do Blender para o Godot, com base em glTF 2.0.
- `consultar-conhecimento`: localiza referências pertinentes e orienta sua aplicação por fontes,
  aplicabilidade e limites. Pelo CLI, Codex e Claude Code usam uma biblioteca única em
  `knowledge/harness/`, com links ajustados, recibos e consulta do catálogo por `knowledge list`.
  Cópias manuais usam `knowledge/` na raiz. A instalação não migra nem sobrescreve adaptações antigas.
- Configurador `models init` no CLI, com política neutra, modelo compartilhado ou perfis,
  esforço e alternativas ordenadas. A instalação oferece uma pergunta opcional. A geração
  v2 tem validação estrutural em TypeScript e provas cruzadas com Python, sem editar arquivos
  existentes ou consultar disponibilidade dos provedores. `--print` mostra somente o TOML.
- CLI TypeScript `@jordyfontoura/skills` para adoção guiada e seletiva de skills e papéis,
  com simulação, preservação de arquivos existentes, recibos de origem e consulta de estado.
  O pacote leva referências completas e dispensa Python no destino.
- Biblioteca `knowledge/` com referências de UI e acessibilidade compartilhadas por
  `criticar`, `implementar` e `prototipar`. Procedimentos, pisos e escalas continuam nas skills.
  O índice declara os arquivos disponíveis; os guias registram aplicabilidade, origem,
  fontes e limites. Outros domínios entram quando houver conteúdo útil.
- Empacotamento seletivo das referências do CLI, incluindo dependências transitivas e links
  ajustados. O plugin e as cópias dos provedores usam a biblioteca na raiz. A validação
  continua recusando links arbitrários fora da skill e verifica índice,
  integridade das cópias e isolamento da biblioteca. Atualização e adoção preservam adaptações locais.
- `criticar`: critica artefatos e experiências com critérios especializados pelo pedido,
  público e referências. Preserva a rubrica de UI e UX em apoios, compõe com `conselho` para
  várias perspectivas e usa `roles.council` para consultas independentes, inclusive individuais.
  Sempre entrega nota geral e notas por categoria quando pertinentes, com duas casas decimais
  (como `9.73`), na escala padrão de 0 a 10. Distingue severidade de qualidade e orienta
  ciclos de correção autorizados, com condição
  de parada, sem substituir provas técnicas ou aceite independente.

### Removido

Cinco skills saem do catálogo. Elas descreviam o que os modelos atuais
fazem sem instrução: descrever um PR, comparar requisitos com a
implementação, examinar a arquitetura, apontar onde a sessão gastou tempo e executar sem spec.
Os pedidos continuam valendo em linguagem natural. A remoção não foi comparada em execuções
equivalentes; a economia de contexto e de manutenção é uma hipótese.

As cinco estavam no canal estável: três desde a versão 0.2.0, e `fazer-direto` e
`examinar-eficiencia` desde a promoção de 13/11/2026. Numa cópia editável, `atualizar-harness` preserva as pastas que você
adaptou; a ausência na origem não autoriza apagá-las no destino. O CLI deixa de oferecer a
prática "Executar direto quando eu pedir" e de recomendar `esclarecer` por padrão;
`esclarecer` continua no catálogo.

- `descrever-pr` foi removida.
- `examinar-arquitetura` foi removida.
- `examinar-eficiencia` foi removida.
- `fazer-direto` foi removida.
- `reconciliar` foi removida.

### Mudado

- `configurar-harness` reconhece a adoção pelo CLI, preserva a biblioteca compartilhada e
  orienta a configuração opcional de modelos. `atualizar-harness` distingue o SHA de base
  de builds locais do conteúdo instalado e confere os hashes antes de assumir uma base de comparação.
- `andamento`: cobre o pedido inteiro até sua condição de conclusão, com mudanças desde o
  último resumo, próxima entrega utilizável e previsão fundamentada quando pertinente.
  Perguntas sobre tempo sempre recebem uma estimativa com base e incertezas ou o motivo de
  ainda não estimar e o marco necessário. Distingue etapas de conclusão total e trabalho
  ativo de esperas externas, sem percentual inventado, medições novas ou acompanhamento periódico.
- As duas entradas de crítica de interface foram reunidas em `criticar`. A rubrica e o painel
  de UI ficam no apoio `criticar/interface.md`.
  Para quem adotou `nightly`, `atualizar-harness` deve migrar chamadas e
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
