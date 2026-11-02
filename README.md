<p align="center">
  <img src="docs/assets/banner.svg" alt="skills, por Jordy Fontoura: para engenharia com agentes de código, em português" width="100%">
</p>

# Skills para agentes de código, em português

Uma coleção de 26 skills e 3 papéis para Claude Code e Codex. Elas orientam o agente a
alinhar antes de agir, entregar em partes verificáveis e relatar as provas do que fez.
É tudo Markdown: não há serviço, conta ou processo em segundo plano.

Internamente, a coleção se chama harness; daí os nomes `configurar-harness`, `atualizar-harness` e
`melhorar-harness`. O plugin se chama `jordyfontoura-skills`.

## Para quem é

- Para quem usa Claude Code ou Codex e quer instruções e respostas em português.
- Para quem quer decidir quando o agente pode alterar arquivos, e ver provas antes de aceitar.
- Para quem prefere skills pequenas, que se combinam e podem ser adaptadas.

As skills não instalam hooks, não trocam o modelo da conversa, não delegam trabalho sem sua
autorização e não substituem os testes do seu projeto.

## Instalar

Escolha uma rota por agente. Instalar o plugin e copiar as skills ao mesmo tempo faz cada skill
aparecer duas vezes.

### Claude Code

```bash
claude plugin marketplace add jordyfontoura/skills
claude plugin install jordyfontoura-skills@jordyfontoura
```

Dentro de uma sessão, use `/plugin marketplace add jordyfontoura/skills` e
`/plugin install jordyfontoura-skills@jordyfontoura`. Para conferir, digite
`/jordyfontoura-skills:` ou rode `claude plugin list`.

### Codex

```bash
codex plugin marketplace add jordyfontoura/skills
codex plugin add jordyfontoura-skills@jordyfontoura
```

Abra uma sessão nova e digite `$` para ver as skills. O Codex não recebe os papéis pelo plugin;
veja como copiá-los em [docs/ADOPTING.md](docs/ADOPTING.md).

### Cópia editável

Para adaptar as skills ou usar outro agente, copie as pastas que quiser e atualize-as com
`atualizar-harness`. O passo a passo está em [docs/ADOPTING.md](docs/ADOPTING.md#cópia-manual).

Instalação local testada em 01/11/2026 com Claude Code 2.1.314 e Codex 0.166.0.

## Primeiro uso

Comece por `propor`. Ela só lê o projeto, apresenta uma abordagem e espera sua aprovação antes
de alterar qualquer coisa. Num repositório seu:

```text
/jordyfontoura-skills:propor Quero adicionar paginação na listagem de pedidos. Mostre a abordagem antes de alterar.
```

O agente lê os arquivos relevantes, explica o que faria e para. Um "pode fazer" libera aquela
proposta. Depois, experimente `entrevistar` para decidir escopo, `especificar` para planejar e
`revisar` para analisar um diff.

## Como chamar as skills

| Agente | Forma |
| --- | --- |
| Claude Code | `/jordyfontoura-skills:<skill>`. O nome curto, como `/propor`, funciona quando não há outro comando com o mesmo nome. |
| Codex | Digite `$` e escolha a skill. O nome completo é `jordyfontoura-skills:<skill>`. |
| Qualquer um | Peça em linguagem natural, como "antes de alterar, me proponha a abordagem". O agente pode escolher a skill pela descrição, mas isso não é garantido. |

Os comandos, as instruções e as respostas ficam em português. Até a versão 0.1.0 os comandos
ficavam em inglês; a correspondência entre os nomes está no [CHANGELOG](CHANGELOG.md).

## Fluxo típico

1. `propor` ou `entrevistar`: alinhar o que fazer antes de alterar.
2. `especificar`: definir comportamentos, critérios e tarefas.
3. `implementar`: entregar em partes verificáveis.
4. `revisar` e `verificar-aceite`: analisar o diff e conferir os critérios de forma independente.
5. `passar-contexto`: deixar a próxima sessão pronta para continuar.

## Catálogo

### Desenvolvimento

| Skill | Para quê |
| --- | --- |
| `especificar` | Especificar comportamentos e contratos e planejar uma entrega verificável. |
| `implementar` | Entregar e verificar o trabalho combinado. |
| `diagnosticar` | Reproduzir uma falha e demonstrar sua causa. |
| `revisar` | Avaliar um diff fixo contra requisitos e padrões. |
| `tratar-revisao` | Verificar feedback recebido e aplicar as correções válidas. |
| `examinar-arquitetura` | Identificar atrito de arquitetura e propor mudanças sustentadas. |
| `verificar-aceite` | Verificar critérios de aceite de forma independente. |
| `prototipar` | Esclarecer uma questão de design com um experimento. |
| `descrever-pr` | Explicar comportamento resultante, provas e riscos de integração. |
| `integrar` | Integrar branches ou concluir o merge de um PR e verificar o resultado. |
| `reconciliar` | Comparar requisitos, documentos e implementação para achar lacunas. |

### Produtividade

| Skill | Para quê |
| --- | --- |
| `propor` | Explicar a abordagem e aguardar aprovação antes de executar. |
| `entrevistar` | Resolver escolhas abertas de escopo e design pela conversa. |
| `entrevistar-por-arquivo` | Conduzir perguntas em arquivo Markdown e consolidar as decisões. |
| `esclarecer` | Reformular em português claro uma explicação que não ficou clara. |
| `andamento` | Resumir andamento, pendências e bloqueios sem mudar o objetivo. |
| `passar-contexto` | Preservar próxima etapa, provas e trabalho restante para outra sessão. |
| `delegar` | Delegar trabalho delimitado e conferir o resultado. |
| `conselho` | Consultar especialistas independentes e consolidar divergências. |
| `pesquisar-web` | Pesquisar na internet e fundamentar conclusões com fontes. |
| `escrever-claro` | Escrever ou revisar textos claros, preservando fatos e voz. |
| `escrever-objetivo` | Escrever uma instrução de execução autônoma com conclusão verificável. |

### Manutenção

| Skill | Para quê |
| --- | --- |
| `configurar-harness` | Configurar comandos e verificações para as tecnologias do projeto. |
| `melhorar-harness` | Propor melhorias nas instruções a partir de dificuldades observadas. |
| `atualizar-harness` | Trazer novas versões das skills preservando adaptações locais. |
| `conhecer-ferramentas` | Explicar e preparar ferramentas de linha de comando, quando autorizado. |

Os procedimentos e exemplos de cada skill estão em [docs/HARNESS.md](docs/HARNESS.md).

## Papéis

`planner` planeja sem implementar, `evaluator` confere critérios sem corrigir o produto e
`representative` escolhe entre alternativas numa execução autônoma que você autorizou. No Claude
Code, eles vêm com o plugin como `jordyfontoura-skills:<papel>`. Um papel disponível não autoriza
delegação: o agente só o usa quando você pede ou autoriza.

A escolha de modelo por papel é opcional e fica no seu projeto. Veja a
[política de modelos](docs/MODELS.md).

## Integrar às instruções do projeto

O plugin não carrega o `AGENTS.md` nem o `CLAUDE.md` deste repositório. Para que o agente use as
skills no momento certo sem que você as chame, copie o bloco curto de
[docs/ADOPTING.md](docs/ADOPTING.md#bloco-para-agentsmd-ou-claudemd) para as instruções do seu
projeto.

## Custo de contexto

O nome e a descrição de cada skill entram em toda sessão. Na versão 0.1.0, o
`claude plugin details` estima cerca de 1.400 tokens fixos para o plugin inteiro. O texto
completo de uma skill só é carregado quando ela é usada. Desative o plugin nos projetos em que
não o usar.

## Atualizar

- **Claude Code:** a atualização automática de marketplaces de terceiros vem desligada. Ligue em
  `/plugin`, na aba de marketplaces, ou rode
  `claude plugin marketplace update jordyfontoura` e depois
  `claude plugin update jordyfontoura-skills@jordyfontoura`.
- **Codex:** rode `codex plugin marketplace upgrade`. Se a versão instalada não mudar, rode de
  novo `codex plugin add jordyfontoura-skills@jordyfontoura`.
- **Cópia editável:** peça ao agente `atualizar-harness`.

Leia o [CHANGELOG](CHANGELOG.md) antes de atualizar: uma nova versão muda as instruções que seus
agentes seguem.

## Por que existe

Estas skills nasceram de problemas recorrentes no trabalho com agentes:

- **O agente altera arquivos antes de entender o pedido.** `propor` e `entrevistar` alinham antes.
- **O agente diz "pronto" sem prova.** `implementar`, `verificar-aceite` e `reconciliar` exigem comandos e
  resultados observados.
- **O contexto se perde entre sessões.** `passar-contexto` e `andamento` registram onde o trabalho parou.
- **O texto fica genérico.** `escrever-claro` e `descrever-pr` pedem fatos concretos.
- **Uma decisão grande depende de uma só opinião.** `conselho` reúne pareceres independentes.

## Relação com mattpocock/skills

A coleção começou inspirada em [mattpocock/skills](https://github.com/mattpocock/skills), e várias
skills seguem ideias de lá. As diferenças: tudo está em português, inclusive os comandos, o que evita
conflito de nomes ao usar as duas coleções; há papéis e uma política de
modelos por responsabilidade; e as skills insistem em autorização explícita e provas.

## Contribuir

PRs são bem-vindos. Leia o [CONTRIBUTING](CONTRIBUTING.md) antes, e o [SECURITY](SECURITY.md)
para relatar uma vulnerabilidade. Usar as skills não exige Python; ele só é necessário para
manter este repositório.

## Créditos

- [mattpocock/skills](https://github.com/mattpocock/skills), de Matt Pocock (MIT).
- [pstack](https://github.com/cursor/plugins/tree/main/pstack), de Lauren Tan (MIT), adaptado
  em `escrever-claro`.
- [Superpowers](https://github.com/obra/superpowers), de Jesse Vincent (MIT).
- [anthropics/skills](https://github.com/anthropics/skills), da Anthropic (Apache-2.0).

Os avisos de licença estão em [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Licença

[Apache-2.0](LICENSE). O retrato do autor no banner não faz parte dessa licença; veja
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md#retrato-do-autor).

## Autor

Criado e mantido por [Jordy Fontoura](https://github.com/jordyfontoura).
