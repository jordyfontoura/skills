# pesquisar-antes-de-decidir

- Modelo: `gpt-6.1-sol-medium`
- Variante: `with-skills`

## Usuário, turno 1

Tô pensando em trocar o Jest pelo Vitest num projeto Node com TypeScript que tem uns 800 testes. Pesquisa pontos negativos e reclamações de quem já migrou e me ajuda a decidir se vale a pena.

## Agente, turno 1

**Eu faria um piloto antes de decidir. Se o Jest está estável e não atrapalha vocês hoje, eu tenderia a manter.** Ter 800 testes, por si só, não justifica a troca: o custo depende mais dos mocks, da configuração e do sistema de módulos.

Pesquisei relatos de migração e conferi as diferenças na documentação atual. Os principais pontos negativos são estes:

**1. A promessa de velocidade pode não se cumprir no CI.**

Há um relato de fevereiro de 2026 com mais de 300 testes, migrados para Vitest 4.0.18: no GitHub Actions, a execução passou de **3 para 11 minutos**, embora localmente estivesse aceitável. A discussão continuava sem resposta marcada como solução quando consultei. É um caso individual, mas mostra por que medir só no notebook é insuficiente. [Relato no repositório do Vitest](https://github.com/vitest-dev/vitest/discussions/9683).

A equipe da Subito também relatou que, em dois repositórios, o Vitest inicialmente ficou mais lento. Num deles, uma execução de aproximadamente 35 segundos passou para 3 minutos; ajustar os workers resolveu. A migração inteira envolveu 10.144 testes, oito repositórios e cerca de três semanas. **Configurar e medir virou parte relevante do trabalho.** [Relato da própria equipe, com Vitest 4](https://dev.to/subito/we-migrated-10144-tests-from-jest-to-vitest-in-3-weeks-the-honest-ai-assisted-truth-527).

**2. CommonJS com mocks pode ser um impedimento concreto.**

Uma reclamação antiga descreve justamente isso: a suíte CommonJS funcionava, mas um módulo carregado com `require()` não era interceptado pelo mock, levando o autor a adotar `mock-require`. **A limitação continua documentada hoje: `vi.mock` não funciona para módulos carregados por `require()`.** Isso também merece atenção em dependências internas já compiladas para CommonJS. [Discussão original](https://github.com/vitest-dev/vitest/discussions/3134), [documentação atual](https://vitest.dev/api/vi.html#vi-mock).

Minha leitura para seu caso: se vocês dependem bastante desse mecanismo, o custo pode ultrapassar os arquivos de teste e atingir a forma de carregar dependências.

**3. API parecida não significa comportamento idêntico.**

A documentação confirma diferenças que exigem revisão:

- `jest.requireActual()` dá lugar ao assíncrono `vi.importActual()`;
- mocks em `__mocks__` precisam de chamadas explícitas a `vi.mock`;
- `mockReset()` tem semântica diferente;
- callbacks `done` e timers legados do Jest não são suportados;
- há diferenças na ordem dos hooks e nos tipos `jest.Mock`.

Isso torna arriscado tratar a migração como uma substituição de `jest` por `vi`. [Guia oficial de migração](https://vitest.dev/guide/migration/jest.html).

No relato da Subito, mudanças nos mocks fizeram alguns testes exercitarem caminhos diferentes sem falhar claramente; também houve um rollback por testes instáveis. **Conseguir uma suíte verde não encerra a validação.** [Experiência da equipe](https://dev.to/subito/we-migrated-10144-tests-from-jest-to-vitest-in-3-weeks-the-honest-ai-assisted-truth-527).

**4. Algumas otimizações cobram um preço em isolamento.**

O Vitest documenta que desativar isolamento pode acelerar testes, especialmente em Node quando há limpeza adequada de estado. Minha preocupação prática seria com singletons, variáveis de ambiente e mocks vazando entre arquivos. Eu começaria o comparativo preservando o isolamento. [Documentação de desempenho](https://vitest.dev/guide/improving-performance.html).

**5. TypeScript precisa entrar na conta completa.**

O typecheck do Vitest fica desativado por padrão. Se hoje a configuração do `ts-jest` detecta erros de tipos, preserve essa verificação com `tsc --noEmit` ou uma configuração equivalente e inclua seu tempo no comparativo. [Configuração oficial de typecheck](https://vitest.dev/config/typecheck).

Os relatos citados usam principalmente Vitest 4; eles demonstram riscos, não provam que a versão atual reproduzirá os problemas. A documentação atual do Vitest 5 também exige Node ≥ 22.12 e Vite ≥ 6.4, então a compatibilidade do ambiente entra na decisão. [Requisitos oficiais](https://vitest.dev/guide/migration/).

Para os seus 800 testes, eu decidiria assim:

| Situação do projeto | Minha tendência |
|---|---|
| Jest estável, CI aceitável, poucos problemas de manutenção | Manter Jest |
| Problemas recorrentes com ESM ou configuração de transformação | Experimentar Vitest |
| Muitos mocks de módulos carregados por `require()` | Forte motivo para adiar |
| Objetivo principal é velocidade | Decidir pelo benchmark no CI |
| Grande parte do tempo está em banco, rede ou inicialização da aplicação | Investigar esse custo primeiro |

O Vitest oferece suporte direto a TypeScript, foco em ESM e modo watch integrado ao Vite — vantagens que podem compensar uma dor real de configuração. [Recursos oficiais](https://vitest.dev/guide/features.html). Também vale comparar com um Jest atualizado: o Jest 30 trouxe melhorias de desempenho e memória. [Anúncio oficial](https://jestjs.io/blog/2025/06/04/jest-30).

**Meu piloto seria limitado a 1–2 dias**, como orçamento de investigação, sem promessa de concluir a migração:

1. Migrar uma amostra com mocks difíceis, timers, integrações e testes simples.
2. Comparar no mesmo CI, com e sem cobertura, repetindo as execuções; medir tempo total e pico de memória.
3. Conferir contagem de testes, cobertura dos mesmos arquivos, typecheck e se falhas introduzidas deliberadamente continuam sendo detectadas.
4. Se a amostra for promissora, validar a suíte inteira antes da troca.

**Minha recomendação é migrar apenas com benefício mensurável ou redução clara de manutenção.** Como critério sugerido, eu buscaria algo como 25–30% de redução no tempo total do CI, ou a eliminação de problemas recorrentes com ESM. Sem isso, manter os 800 testes no Jest é uma decisão bem defensável.
