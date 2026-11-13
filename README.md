<p align="center">
  <img src="docs/assets/banner.svg" alt="skills, por Jordy Fontoura: para engenharia com agentes de código, em português" width="100%">
</p>

# Mais controle sobre o trabalho dos seus agentes

Skills em português para alinhar decisões, orientar implementações e pedir provas do que foi
feito. Para Claude Code e Codex, com 29 skills e 3 papéis que você pode usar ou adaptar.

O padrão é implementar por entregas úteis, com planejamento proporcional à incerteza e ao
risco. Uma spec é usada quando falta definição ou quando você a pede; não é etapa obrigatória
de toda mudança. Veja o [fluxo, sua base e seus limites](docs/HARNESS.md#fluxo-de-trabalho).

**[Instalar](#instalar) · [Experimentar uma skill](#primeiro-uso) · [Ver exemplos](docs/EXAMPLES.md)**

## Quando usar

- **Quer ver a abordagem antes de alterar?** `propor` orienta o agente a apresentar uma proposta e esperar seu aceite.
- **Quer só fazer e entregar rápido?** `fazer-direto` dispensa specs e etapas de processo, com verificação do resultado.
- **Precisa conferir uma entrega?** `implementar` pede comandos e resultados observados; `verificar-aceite` confere os critérios de forma independente.
- **Vai retomar em outra sessão?** `passar-contexto` preserva a próxima etapa e as provas pendentes; `andamento` resume o andamento.

É tudo Markdown, sem serviço em segundo plano. As skills não instalam hooks, não trocam o
modelo da conversa nem autorizam delegação por conta própria. Seus testes continuam necessários.

A [biblioteca de referências](knowledge/README.md) reúne conhecimento de UI e acessibilidade
para consulta conforme a tarefa. As fontes ficam fora das skills; as cópias avulsas incluem
automaticamente os guias necessários, sem depender do caminho deste repositório.

## Instalar

Escolha uma rota por agente: instalar o plugin e copiar as skills ao mesmo tempo faz cada
skill aparecer duas vezes.

### Claude Code

```bash
claude plugin marketplace add jordyfontoura/skills
claude plugin install jordyfontoura-skills@jordyfontoura
```

Para conferir, digite `/jordyfontoura-skills:` numa sessão ou rode `claude plugin list`.

### Codex

```bash
codex plugin marketplace add jordyfontoura/skills
codex plugin add jordyfontoura-skills@jordyfontoura
```

Abra uma sessão nova e digite `$` para ver as skills. O Codex não recebe os papéis pelo
plugin; veja como copiá-los no [guia de adoção](docs/ADOPTING.md#plugin).

Instalação local testada em 01/11/2026 com Claude Code 2.1.314 e Codex 0.166.0.
Prefere adaptar os arquivos? Use a [cópia editável](docs/ADOPTING.md#cópia-manual).

O [CLI `@jordyfontoura/skills`](cli/README.md) está em desenvolvimento para recomendar e
instalar cópias por projeto, incluindo papéis opcionais. A publicação no npm está pendente;
o guia mostra como experimentar o código local.

## Primeiro uso

Num repositório seu, peça uma mudança com resultado claro. `implementar` orienta o agente a
ler as instruções, executar o trabalho autorizado e apresentar as verificações.

**Claude Code**
```text
/jordyfontoura-skills:implementar Exporte os resultados filtrados em CSV, com as mesmas colunas da tabela. Confira o arquivo gerado e não publique.
```

**Codex**
```text
$jordyfontoura-skills:implementar Exporte os resultados filtrados em CSV, com as mesmas colunas da tabela. Confira o arquivo gerado e não publique.
```

Se quiser aprovar a abordagem antes das alterações, use `propor`: o agente apresenta a proposta
e aguarda seu "pode fazer". Para outras situações, veja
[quando usar cada skill e um pedido pronto para copiar](docs/EXAMPLES.md).

## Como chamar as skills

| Agente | Forma |
| --- | --- |
| Claude Code | `/jordyfontoura-skills:<skill>`. O nome curto, como `/propor`, funciona quando não há outro comando com o mesmo nome. |
| Codex | `$jordyfontoura-skills:<skill>` ou selecione a skill na lista de `$`. |
| Qualquer um | Peça em linguagem natural. O agente pode escolher pela descrição, mas isso não é garantido. |

Os comandos, as instruções e as respostas ficam em português. Até a versão 0.1.0 os comandos
ficavam em inglês; a correspondência entre os nomes está no [CHANGELOG](CHANGELOG.md).

## Explorar as skills

Escolha pela situação no [guia de exemplos](docs/EXAMPLES.md) ou consulte o catálogo abaixo.

<details>
<summary>Ver as 29 skills</summary>

### Entender e decidir

| Skill | Use para |
| --- | --- |
| `propor` | Avaliar uma abordagem antes de autorizar alterações. |
| `entrevistar` | Resolver escolhas abertas pela conversa. |
| `entrevistar-por-arquivo` | Responder perguntas em Markdown, em rodadas. |
| `esclarecer` | Retomar uma explicação que ficou confusa. |
| `pesquisar-web` | Buscar fontes na internet para fundamentar uma conclusão. |
| `conselho` | Consultar perspectivas independentes sobre uma decisão. |
| `prototipar` | Experimentar uma interação antes da implementação completa. |
| `especificar` | Definir comportamentos, critérios e tarefas. |
| `escrever-objetivo` | Preparar uma instrução de execução autônoma com limites claros. |

### Entregar e conferir

| Skill | Use para |
| --- | --- |
| `implementar` | Entregar e verificar o trabalho combinado. |
| `fazer-direto` | Executar diretamente, priorizando velocidade e dispensando specs e etapas de processo. |
| `diagnosticar` | Reproduzir uma falha e investigar sua causa. |
| `revisar` | Analisar um diff fixo contra requisitos e padrões. |
| `tratar-revisao` | Conferir feedback recebido e aplicar correções válidas. |
| `examinar-arquitetura` | Identificar atrito estrutural no código e propor melhorias. |
| `verificar-aceite` | Conferir critérios de aceite de forma independente. |
| `reconciliar` | Comparar requisitos, implementação e evidências. |
| `criticar` | Receber uma crítica especializada de um artefato ou experiência, individual ou com conselho. |
| `descrever-pr` | Escrever a descrição de uma mudança para quem vai revisá-la. |
| `integrar` | Integrar branches no destino autorizado e verificar o resultado. |

### Acompanhar e dividir o trabalho

| Skill | Use para |
| --- | --- |
| `andamento` | Consultar andamento, pendências e bloqueios. |
| `examinar-eficiencia` | Entender por que o trabalho demorou ou gastou muitos tokens e como melhorar. |
| `passar-contexto` | Deixar outra sessão pronta para continuar. |
| `delegar` | Dividir trabalho autorizado e conferir o retorno. |

### Escrever e cuidar das ferramentas

| Skill | Use para |
| --- | --- |
| `escrever-claro` | Escrever e revisar textos, preservando fatos e voz. |
| `configurar-harness` | Configurar comandos e verificações para o projeto. |
| `melhorar-harness` | Propor melhorias nas instruções a partir de dificuldades observadas. |
| `atualizar-harness` | Atualizar skills copiadas preservando adaptações locais. |
| `conhecer-ferramentas` | Entender e preparar ferramentas de linha de comando, quando autorizado. |

O nome interno da coleção é harness; daí os nomes das skills de manutenção.

</details>

## Como o autor usa

Frequência relativa nas conversas pessoais do autor, consultadas em 13/11/2026.
Pedidos e declarações podem se sobrepor e não comprovam execução.

<picture>
  <source media="(max-width: 600px)" srcset="docs/assets/skill-usage-mobile.svg">
  <img src="docs/assets/skill-usage.svg" alt="Dois rankings de frequência relativa, sem contagens: pedidos diretos do usuário e uso declarado pelo agente." width="100%">
</picture>

## Para ir além

- **Exemplos:** [quando e como usar cada skill](docs/EXAMPLES.md).
- **Papéis e modelos:** `planner` planeja, `evaluator` confere e `representative` decide nos limites da autonomia autorizada. Veja o [fluxograma](docs/MODEL-FLOW.md) e a [política de modelos](docs/MODELS.md).
- **Uso pelas instruções do projeto:** acrescente o [bloco para AGENTS.md ou CLAUDE.md](docs/ADOPTING.md#bloco-para-agentsmd-ou-claudemd).
- **Referência e manutenção:** [HARNESS.md](docs/HARNESS.md) e [guia de adoção](docs/ADOPTING.md), incluindo custo de contexto e cópia editável.

## Atualizar

Leia o [CHANGELOG](CHANGELOG.md) antes de atualizar.

- **Claude Code:** a atualização automática de marketplaces de terceiros vem desligada. Ligue em `/plugin` ou rode `claude plugin marketplace update jordyfontoura` e depois `claude plugin update jordyfontoura-skills@jordyfontoura`.
- **Codex:** rode `codex plugin marketplace upgrade`. Se a versão instalada não mudar, rode de novo `codex plugin add jordyfontoura-skills@jordyfontoura`.
- **Cópia editável:** peça ao agente `atualizar-harness`.

`main` é o canal estável; `nightly` reúne novidades em avaliação. Para experimentar com uma
cópia editável, peça `atualizar-harness` indicando a branch `nightly`. O canal escolhido fica
registrado para as próximas atualizações. Uma tag fixa uma versão específica. Veja o
[guia de adoção](docs/ADOPTING.md#cópia-manual) e o [fluxo de contribuição](CONTRIBUTING.md#branches-e-canais).

## Contribuir, créditos e licença

Criado por [Jordy Fontoura](https://github.com/jordyfontoura). PRs são bem-vindos:
leia o [CONTRIBUTING](CONTRIBUTING.md) e o [SECURITY](SECURITY.md).

Inspirado em [mattpocock/skills](https://github.com/mattpocock/skills),
[pstack](https://github.com/cursor/plugins/tree/main/pstack),
[Superpowers](https://github.com/obra/superpowers) e
[anthropics/skills](https://github.com/anthropics/skills).
Créditos e avisos de licença em [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

[Apache-2.0](LICENSE). O retrato do banner não faz parte dessa licença;
veja os [direitos do retrato](THIRD_PARTY_NOTICES.md#retrato-do-autor).
