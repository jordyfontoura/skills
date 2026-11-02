<p align="center">
  <img src="docs/assets/banner.svg" alt="skills, por Jordy Fontoura: para engenharia com agentes de código, em português" width="100%">
</p>

# Mais controle sobre o trabalho dos seus agentes

Skills em português para alinhar decisões, orientar implementações e pedir provas do que foi
feito. Para Claude Code e Codex, com 26 skills e 3 papéis que você pode usar ou adaptar.

**[Instalar](#instalar) · [Experimentar uma skill](#primeiro-uso) · [Ver exemplos](docs/EXAMPLES.md)**

## Quando usar

- **Quer ver a abordagem antes de alterar?** `propose` orienta o agente a apresentar uma proposta e esperar seu aceite.
- **Precisa conferir uma entrega?** `implement` pede comandos e resultados observados; `evaluate` confere os critérios de forma independente.
- **Vai retomar em outra sessão?** `handoff` preserva a próxima etapa e as provas pendentes; `progress` resume o andamento.

É tudo Markdown, sem serviço em segundo plano. As skills não instalam hooks, não trocam o
modelo da conversa nem autorizam delegação por conta própria. Seus testes continuam necessários.

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

## Primeiro uso

Num repositório seu, peça uma proposta para uma mudança. `propose` instrui o agente a ler o
projeto, explicar a abordagem e esperar sua aprovação antes de alterar arquivos.

**Claude Code**
```text
/jordyfontoura-skills:propose Quero exportar os relatórios em CSV.
```

**Codex**
```text
$jordyfontoura-skills:propose Quero exportar os relatórios em CSV.
```

Um "pode fazer" libera aquela proposta. Para outras situações, veja
[quando usar cada skill e um pedido pronto para copiar](docs/EXAMPLES.md).

## Como chamar as skills

| Agente | Forma |
| --- | --- |
| Claude Code | `/jordyfontoura-skills:<skill>`. Use a forma completa para `review`: `/review` é um comando do próprio Claude Code. |
| Codex | `$jordyfontoura-skills:<skill>` ou selecione a skill na lista de `$`. |
| Qualquer um | Peça em linguagem natural. O agente pode escolher pela descrição, mas isso não é garantido. |

Se também usar mattpocock/skills, prefira o nome completo do plugin: `handoff`, `implement`,
`prototype` e `research` existem nas duas coleções.

## Explorar as skills

Escolha pela situação no [guia de exemplos](docs/EXAMPLES.md) ou consulte o catálogo abaixo.

<details>
<summary>Ver as 26 skills</summary>

### Entender e decidir

| Skill | Use para |
| --- | --- |
| `propose` | Avaliar uma abordagem antes de autorizar alterações. |
| `interview` | Resolver escolhas abertas pela conversa. |
| `interview-async` | Responder perguntas em Markdown, em rodadas. |
| `clarify` | Retomar uma explicação que ficou confusa. |
| `research` | Buscar fontes na internet para fundamentar uma conclusão. |
| `council` | Consultar perspectivas independentes sobre uma decisão. |
| `prototype` | Experimentar uma interação antes da implementação completa. |
| `specify` | Definir comportamentos, critérios e tarefas. |
| `write-goal` | Preparar uma instrução de execução autônoma com limites claros. |

### Entregar e conferir

| Skill | Use para |
| --- | --- |
| `implement` | Entregar e verificar o trabalho combinado. |
| `diagnose` | Reproduzir uma falha e investigar sua causa. |
| `review` | Analisar um diff fixo contra requisitos e padrões. |
| `address-review` | Conferir feedback recebido e aplicar correções válidas. |
| `architecture-review` | Identificar atrito estrutural no código e propor melhorias. |
| `evaluate` | Conferir critérios de aceite de forma independente. |
| `reconcile` | Comparar requisitos, implementação e evidências. |
| `pull-request` | Escrever a descrição de uma mudança para quem vai revisá-la. |
| `integrate` | Integrar branches no destino autorizado e verificar o resultado. |

### Acompanhar e dividir o trabalho

| Skill | Use para |
| --- | --- |
| `progress` | Consultar andamento, pendências e bloqueios. |
| `handoff` | Deixar outra sessão pronta para continuar. |
| `delegate` | Dividir trabalho autorizado e conferir o retorno. |

### Escrever e cuidar das ferramentas

| Skill | Use para |
| --- | --- |
| `unslop` | Escrever e revisar textos, preservando fatos e voz. |
| `setup-harness` | Configurar comandos e verificações para o projeto. |
| `improve-harness` | Propor melhorias nas instruções a partir de dificuldades observadas. |
| `update-harness` | Atualizar skills copiadas preservando adaptações locais. |
| `toolbox` | Entender e preparar ferramentas de linha de comando, quando autorizado. |

O nome interno da coleção é harness; daí os nomes das skills de manutenção.

</details>

## Como o autor usa

Frequência relativa nas conversas pessoais do autor, consultadas em 02/11/2026.
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
- **Cópia editável:** peça ao agente `update-harness`.

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
