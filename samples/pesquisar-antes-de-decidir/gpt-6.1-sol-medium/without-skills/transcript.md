# pesquisar-antes-de-decidir

- Modelo: `gpt-6.1-sol-medium`
- Variante: `without-skills`

## Usuário, turno 1

Tô pensando em trocar o Jest pelo Vitest num projeto Node com TypeScript que tem uns 800 testes. Pesquisa pontos negativos e reclamações de quem já migrou e me ajuda a decidir se vale a pena.

## Agente, turno 1

**Eu faria um piloto, mas não migraria os 800 testes só pela promessa de velocidade.** Se o Jest está estável e não atrapalha o trabalho, falta uma justificativa concreta. Se vocês vivem corrigindo problemas de ESM ou da configuração de TypeScript, o Vitest fica mais atraente.

Pesquisei relatos de quem migrou e confrontei as reclamações com a documentação. Estes são os pontos que mais pesariam na sua decisão:

**1. O CI pode ficar mais lento, mesmo quando localmente parece bom.**

Em fevereiro de 2026, uma equipe relatou que uma suíte com mais de 300 testes, migrada para **Vitest 4.0.18**, passou de **3 minutos no Jest para 11 minutos no GitHub Actions**. Após ajustes de workers e timers, caiu para aproximadamente 8,5 minutos; o autor interrompeu a migração. É um caso específico, sem reprodução mínima publicada, mas mostra por que medir só no notebook pode enganar. [Relato e acompanhamento](https://github.com/vitest-dev/vitest/discussions/9683)

**2. Mocks são o maior risco de retrabalho.**

A semelhança da API esconde diferenças importantes:

- `vi.mock` **não intercepta módulos carregados por `require()`**.
- Factories de mocks precisam declarar os exports, incluindo `default`.
- `mockReset()` tem comportamento diferente.
- `__mocks__` não é carregado automaticamente nas mesmas condições.
- `jest.requireActual()` vira uma operação assíncrona com `vi.importActual()`.

Para um backend com bastante CommonJS e mocks de módulos, isso pode pesar mais que a quantidade de testes. [API de mocks](https://vitest.dev/api/vi.html#vi-mock), [guia de migração](https://vitest.dev/guide/migration/jest.html)

**3. Ganhar velocidade pode exigir abrir mão de isolamento.**

A documentação recomenda considerar `isolate: false` para reduzir custos de execução. Só que arquivos no mesmo worker passam a compartilhar estado de módulos e ambiente. Minha leitura: um benchmark obtido assim só é relevante se sua suíte tolerar esse compartilhamento — especialmente com singletons, caches e estado global. [Documentação de desempenho](https://vitest.dev/guide/improving-performance.html)

**4. Um piloto pequeno pode esconder problemas de escala.**

No relato da migração de **70 mil testes da Miro**, o consumo de memória piorou no meio do caminho, apesar do piloto favorável. O problema estava na configuração com muitos projetos Vitest interligados, repetindo transformações; consolidá-los resolveu o gargalo. A migração terminou com ganhos, mas exigiu trabalho de infraestrutura.

Isso é mais relevante se seu projeto for um monorepo. **Não dá para extrapolar esse problema diretamente para 800 testes em um único pacote.** [Relato do engenheiro responsável](https://dev.to/n0th1ng_else/we-migrated-70000-tests-from-jest-to-vitest-yes-in-2-months-3lmn)

**5. Migrar aos poucos também tem custo.**

Uma equipe migrando em 2026 relatou dificuldade para consolidar cobertura de Jest e Vitest, descrevendo a solução como trabalhosa. Rodar os dois em paralelo ajuda na transição, mas exige planejar relatórios e thresholds do CI. [Discussão sobre cobertura](https://github.com/vitest-dev/vitest/discussions/9637)

Há ainda incompatibilidades menores: callbacks `done`, timers legados e tipos `jest.*` precisam de adaptação. [Guia oficial](https://vitest.dev/guide/migration/jest.html)

Minha recomendação para o seu cenário:

| Situação atual | Minha decisão |
|---|---|
| Jest estável, tempo aceitável, pouca manutenção | Continuar no Jest |
| Problemas recorrentes com ESM e configuração de TS | Fazer piloto com Vitest |
| Muito `require()` e mock de módulos | Investigar esses casos primeiro |
| Objetivo principal é acelerar CI | Decidir exclusivamente por medição no CI |
| Testes gastam a maior parte do tempo em banco/rede | Medir esse gargalo antes de trocar o runner |

Eu reservaria **1–2 dias para um piloto**, como limite de investigação, não como estimativa da migração inteira:

1. Selecionar arquivos representativos: mocks difíceis, timers, integrações, setup pesado e alguns testes simples.
2. Comparar os mesmos testes nos dois runners, no CI real, com cobertura ligada e desligada, repetindo as execuções.
3. Medir duração, pico de memória, instabilidade e esforço para adaptar os testes.
4. Conferir se os testes continuam detectando falhas reais, introduzindo temporariamente um erro conhecido.

**Meu voto provisório é manter o Jest até o piloto mostrar um benefício claro.** Os 800 testes tornam a investigação viável; o que decide o custo são os mocks, o sistema de módulos e a configuração compartilhada. O Vitest oferece suporte direto a TS e uma abordagem ESM-first, mas esses benefícios precisam resolver uma dor que vocês realmente tenham. [Recursos oficiais](https://vitest.dev/guide/features.html)
