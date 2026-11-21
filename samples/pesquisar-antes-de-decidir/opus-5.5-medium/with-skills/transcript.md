# pesquisar-antes-de-decidir

- Modelo: `opus-5.5-medium`
- Variante: `with-skills`

## Usuário, turno 1

Tô pensando em trocar o Jest pelo Vitest num projeto Node com TypeScript que tem uns 800 testes. Pesquisa pontos negativos e reclamações de quem já migrou e me ajuda a decidir se vale a pena.

## Agente, turno 1

## Resposta curta

Para um projeto Node + TypeScript com uns 800 testes, a troca **só vale a pena se o Jest estiver incomodando hoje** (ESM, configuração do `ts-jest`/Babel, lentidão no modo watch, travamentos). Se ele funciona bem, o ganho costuma ser pequeno e o trabalho de migração é real. Minha sugestão é fazer um piloto de 1 ou 2 dias e decidir com números do seu projeto.

Não encontrei o seu projeto no diretório de trabalho, que está vazio. Por isso esta análise é geral, não do seu código.

## Reclamações de quem migrou

**1. Ficou mais lento, não mais rápido.** É a reclamação mais comum, e contraria o marketing.
- Uma SPA com 1.256 testes ficou cerca de 38% mais lenta localmente sem coverage (322s contra 200s). No CI a diferença foi pequena (138s contra 128s) ([Wilcurt](https://dev.to/thejaredwilcurt/vitest-vs-jest-benchmarks-on-a-5-year-old-real-work-spa-4mf1)).
- Um post de 2022 relata CI de 10 a 15 min com Vitest contra 3 a 4 min com Jest ([Mankevicius](https://dev.to/neophen/vitest-is-fast-jest-is-faster--ln1)). Nos comentários do mesmo post, alguém com **800 testes** desistiu porque, mesmo ajustado, o Vitest ficou 2,5x mais lento. Outra pessoa com 800 testes conseguiu ficar mais rápida que o Jest depois de ajustar pool e isolamento. O resultado varia de projeto para projeto.
- Há issues abertas sobre isso, por exemplo [#579](https://github.meowingcats01.workers.dev/vitest-dev/vitest/issues/579) ("3x mais lento") e [#5668](https://github.com/vitest-dev/vitest/issues/5668) (CI na AWS: 500s com Jest contra 818s com Vitest). Não confirmei se já foram resolvidas.
- A causa principal é o **isolamento por arquivo**, que vem ligado por padrão. A [documentação oficial](https://vitest.dev/guide/improving-performance) admite que ele "aumenta bastante o tempo dos testes".

**2. O mock de módulos funciona de outro jeito.** Essa é a maior fonte de retrabalho. Pela [guia oficial de migração](https://vitest.dev/guide/migration/jest):
- A factory do `vi.mock` precisa retornar um objeto com todos os exports. No Jest, o retorno vira o export default.
- Mocks em `__mocks__` **não são carregados sozinhos**. Só entram com `vi.mock()` ou via `setupFiles`.
- `mockReset` volta para a implementação original, em vez de uma função vazia. Testes que dependiam do comportamento do Jest podem passar ou falhar por outro motivo.
- Para mockar libs de `node_modules`, às vezes é preciso listar em `server.deps.inline`.
- Uma factory que usa variáveis de fora dela dá ReferenceError. A solução é `vi.hoisted`.

**3. APIs que não existem ou mudaram:** callbacks `done` não existem (é preciso usar async/await), os legacy fake timers não existem, `jest.setTimeout` vira `vi.setConfig`, os tipos `jest.Mock` passam a ser importados de `vitest`, a ordem dos hooks muda (agora em pilha) e o filtro `-t` usa `>` como separador. Um time relatou que precisou ajustar testes de cron que usam fake timers ([relato](https://dev.to/whoffagents/vitest-20-vs-jest-we-migrated-400-tests-and-heres-what-actually-changed-59hh)).

**4. A API muda bastante entre versões.** O Vitest já está na 5, e a [migração para a 5](https://vitest.dev/guide/migration) mudou de novo alguns padrões, como `clearMocks: true` e a semântica de `toThrow("")`. O Jest muda menos.

**5. Pode revelar testes que já estavam quebrados.** Um time com 2.900 testes descobriu snapshots vazios que o Jest aceitava sem reclamar. Também disseram que o ganho de velocidade foi "menor que o esperado" ([relato](https://dev.to/56_kode/migration-from-jest-to-vitest-a-real-world-experience-with-2900-tests-39np)). Isso é bom no fim das contas, mas aumenta o trabalho.

## O que pesa a favor no seu caso

- **Quase todos os relatos de lentidão vêm de frontend com jsdom.** Em Node puro, o Vitest pode rodar com `pool: 'threads'` e `isolate: false`, que a documentação aponta como a configuração mais rápida e como normalmente segura para ambiente `node`. A condição é que os testes limpem o próprio estado.
- O TypeScript e o ESM funcionam sem `ts-jest` nem Babel, e a configuração fica bem menor.
- A API é quase compatível. Na maior parte dos arquivos, a troca é `jest.` por `vi.`.

## O que pesa contra trocar

O [Jest 30](https://jestjs.io/blog/2025/06/04/jest-30) (jun/2025) reduziu boa parte da diferença. Ele aceita config em TS e `.mts`/`.cts`, pode usar o type stripping nativo do Node, e num app grande os testes de servidor ficaram cerca de 37% mais rápidos e usaram cerca de 77% menos memória. Se você ainda está no Jest 29, **atualizar para o 30 é muito mais barato** e talvez resolva o problema. O suporte a ESM continua experimental no Jest, segundo a [SitePoint](https://www.sitepoint.com/vitest-vs-jest-2026-migration-benchmark/).

## Como decidir

| Situação | Recomendação |
|---|---|
| O Jest funciona, o projeto é CJS e o tempo é aceitável | Não migre. Se estiver no 29, atualize para o Jest 30 |
| Sofre com ESM, `ts-jest` ou dependências ESM-only | Migre, é o caso mais forte a favor |
| O problema é só velocidade | Faça o piloto abaixo antes de decidir |
| Usa muito `__mocks__`, `done` ou legacy timers | Conte com bastante retrabalho e meça antes |

**Piloto sugerido (1 ou 2 dias):**
1. Instale o Vitest ao lado do Jest, com `globals: true`, e rode um módulo de cerca de 100 testes que use mocks de forma representativa.
2. Meça o tempo frio e o tempo do watch nos dois, **também no CI**, com o pool padrão (`forks`) e com `threads` + `isolate: false`.
3. Conte quantos testes quebraram e por quê. Isso dá uma estimativa do custo para os 800.
4. Se o Vitest com `isolate: false` não ficar claramente mais rápido e não houver problema de ESM, fique no Jest.

Se quiser, posso montar o piloto quando você me passar o projeto.

**Limites desta pesquisa:** a maior parte das fontes são relatos individuais de frontend, não benchmarks controlados em backend Node. Não verifiquei se as issues citadas foram resolvidas nas versões 4 e 5 do Vitest.
