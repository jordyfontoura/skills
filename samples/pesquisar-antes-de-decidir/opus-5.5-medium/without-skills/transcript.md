# pesquisar-antes-de-decidir

- Modelo: `opus-5.5-medium`
- Variante: `without-skills`

## Usuário, turno 1

Tô pensando em trocar o Jest pelo Vitest num projeto Node com TypeScript que tem uns 800 testes. Pesquisa pontos negativos e reclamações de quem já migrou e me ajuda a decidir se vale a pena.

## Agente, turno 1

## Resumo

Para 800 testes num projeto Node com TypeScript, a troca costuma valer a pena **se você tiver alguma dor real com o Jest hoje**: ts-jest lento, configuração de ESM complicada, ou duas pipelines diferentes de transformação de TS. Se o Jest está rodando bem e ninguém reclama, o ganho é pequeno e o risco não é zero. Não achei arquivos de projeto na pasta de trabalho, então o que segue é uma análise geral, não do seu código.

## Principais reclamações de quem migrou

**1. Mocks são o maior problema.**
- `vi.mock` é içado (hoisted) para o topo do arquivo. Se a factory usa variáveis de fora dela, dá `ReferenceError` ou `undefined`, e é preciso reescrever com `vi.hoisted`. Várias fontes dizem que essa é a falha mais comum na migração.
- `vi.importActual()` é assíncrono, diferente do `jest.requireActual()`, que é síncrono. Se faltar o `await`, um Promise é espalhado dentro do mock sem erro óbvio.
- Não existe automock. Um `jest.mock('./x')` sem factory não se comporta igual no Vitest.
- A factory precisa declarar cada export, e o export default tem que aparecer como `default`.
- O estado dos mocks muda depois de `mockClear`/`mockReset`. O Jest recria o estado, e o Vitest mantém a mesma referência. Isso pode causar falhas sutis.

**2. A velocidade não é garantida, e às vezes piora.**
- Há relatos de Vitest **mais lento** que o Jest em suítes grandes: 818s contra 500s numa [issue oficial](https://github.com/vitest-dev/vitest/issues/5668), e 1,5x a 2x mais lento em CI [neste artigo](https://dev.to/neophen/vitest-is-fast-jest-is-faster--ln1).
- O motivo principal é o isolamento por arquivo combinado com grafos de import pesados. Desligar com `isolate: false` acelera muito (relatos de 3 a 6x), mas quebra testes que compartilham estado. Num benchmark, 19 testes falharam.
- Por outro lado, um dev com exatamente 800 testes conseguiu ~4x de ganho e ficou mais rápido que o Jest depois de ajustar a configuração. Outros relatam quedas de 14min para 7min ou de 47s para 11s.
- O ganho é maior em projetos que já usam Vite. Num backend Node puro, a vantagem vem principalmente de trocar o ts-jest pelo esbuild.

**3. Diferenças menores**
- Fake timers se comportam um pouco diferente, e alguns testes que dependem de tempo precisam de ajuste.
- Há detalhes de `spyOn` e de matchers raros que não batem 100%.

**4. Considerações minhas (não vieram das fontes)**
- O Jest 30 melhorou desempenho e configuração. Vale comparar com ele, não com um Jest antigo.
- Plugins, reporters e integrações de CI feitos para Jest podem não ter equivalente direto.

## Como decidir

| Situação | Recomendação |
|---|---|
| Usa ts-jest e a suíte demora | Vale testar a migração |
| Quer ESM nativo ou já tem dor com `"type": "module"` | Vale testar a migração |
| Muitos `jest.mock` com automock ou factories com variáveis externas | O custo é maior; faça um levantamento antes |
| Muito estado global, singletons ou conexões de banco entre testes | Risco de não ganhar velocidade |
| Jest rápido e estável, já usando `@swc/jest` | Provavelmente não compensa |

## Como eu faria

1. **Contar o tamanho do problema antes:** `grep -r "jest.mock\|requireActual\|useFakeTimers"`. Se tiver poucas dezenas de ocorrências, a migração é tranquila.
2. **Fazer uma prova de conceito num branch** com `globals: true`, para evitar mudar todos os imports. Migre 50 a 100 testes representativos e compare o tempo localmente **e no CI**.
3. **Testar as opções de desempenho:** `pool: 'threads'` contra `'forks'`, e `isolate: false` se os testes aguentarem.
4. **Migrar aos poucos:** dá para rodar Jest e Vitest lado a lado durante a transição.

Se você me mostrar o `package.json`, o `jest.config` e alguns testes com mocks, consigo estimar o esforço para o seu caso.

**Observação:** vários desses artigos são posts de blog, e alguns parecem gerados por IA. Leia os números como relatos individuais, não como benchmarks confiáveis. O único teste que vale para a sua decisão é medir a sua própria suíte.

**Fontes:**
- [Migração real com 2900 testes](https://dev.to/56_kode/migration-from-jest-to-vitest-a-real-world-experience-with-2900-tests-39np)
- [Vitest is fast, Jest is faster](https://dev.to/neophen/vitest-is-fast-jest-is-faster--ln1)
- [Vitest issue #5668](https://github.com/vitest-dev/vitest/issues/5668)
- [Discussão #5623: Vitest lento na AWS](https://www.github.com/vitest-dev/vitest/discussions/5623)
- [Improving Vitest performance](https://dev.to/thejaredwilcurt/improving-vitest-performance-42c6)
- [Vitest vs Jest benchmarks em SPA real](https://dev.to/thejaredwilcurt/vitest-vs-jest-benchmarks-on-a-5-year-old-real-work-spa-4mf1)
- [Why your Vitest suite is slow](https://maximedubourg-com.pages.dev/posts/why-your-vitest-test-suite-is-slow)
- [Guia oficial de performance](https://main.vitest.dev/guide/improving-performance)
- [Guia oficial de migração do Jest](https://main.vitest.dev/guide/migration/jest)
- [Documentação do vi.mock](https://vitest.dev/api/vi)
- [Armadilhas de hoisting do vi.mock (Mergify)](https://mergify.com/blog/vitest-vimock-hoisting-traps)
- [Migração de 400 testes](https://dev.to/whoffagents/vitest-20-vs-jest-we-migrated-400-tests-and-heres-what-actually-changed-59hh)
- [Retrospectiva: -50% no tempo](https://dev.to/johalputt/retrospective-switching-from-jest-to-vitest-2-reduced-our-frontend-test-suite-time-by-50-for-1gbj)
- [Migração e benchmark (comentários)](https://dev.to/mbarzeev/from-jest-to-vitest-migration-and-benchmark-23pl/comments)
- [Guia de migração Vitest 4](https://dev.to/jangwook_kim_e31e7291ad98/migrating-from-jest-to-vitest-4-a-complete-2026-guide-4132)
- [SitePoint: benchmark 2026](https://www.sitepoint.com/vitest-vs-jest-2026-migration-benchmark/)
