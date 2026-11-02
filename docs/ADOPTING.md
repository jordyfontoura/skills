# Adotar em outro projeto

Há duas rotas. Escolha uma por agente: usar o plugin e cópias ao mesmo tempo faz cada skill
aparecer duas vezes.

| Rota | Para quem | Atualização |
| --- | --- | --- |
| Plugin | Claude Code e Codex, sem editar as skills. | Pelo gerenciador de plugins do agente. |
| Cópia manual | Quem quer adaptar as skills ou usa outro agente. | Pela skill `atualizar-harness`. |

## Plugin

Os comandos estão no [README](../README.md#instalar). O plugin traz as 26 skills; no Claude Code,
também os papéis `planner`, `evaluator` e `representative`. O Codex não recebe papéis por plugin:
copie os arquivos de [.codex/agents/](../.codex/agents/) para a pasta `.codex/agents/` do projeto.

O plugin não carrega instruções de projeto. Para que o agente use as skills no momento certo
sem que você as chame, acrescente o bloco abaixo ao seu `AGENTS.md` ou `CLAUDE.md`.

## Bloco para AGENTS.md ou CLAUDE.md

Adapte o texto às regras do seu projeto. As skills funcionam sem ele quando chamadas pelo nome.

```markdown
## Fluxo com as skills

- Quando eu pedir `propor` ou pedir para explicar antes de agir, apresente a abordagem e
  aguarde minha aprovação.
- Use `entrevistar` para escolhas abertas de escopo ou design e `especificar` para trabalho substancial.
- Use `implementar` para entregar partes pequenas e verificáveis; relate os comandos executados
  e os resultados observados. Prova ausente continua ausente.
- Use `revisar` para analisar diffs e `verificar-aceite` para aceite independente.
- Use `andamento` para consultas de andamento e `passar-contexto` quando outra sessão for retomar.
- Aplique `escrever-claro` ao escrever documentos, títulos, descrições e mensagens.
- Explorar não autoriza implementar, e uma pergunta não conta como aprovação.
```

## Cópia manual

1. Copie as skills escolhidas de [.agents/skills/](../.agents/skills/) (Codex e outros agentes)
   ou de [.claude/skills/](../.claude/skills/) (Claude Code) para a mesma pasta no seu projeto.
   Cada skill funciona sozinha; outras skills são citadas pelo nome e podem ser copiadas depois.
2. Se quiser os papéis, copie [.claude/agents/](../.claude/agents/) e
   [.codex/agents/](../.codex/agents/) para as pastas correspondentes.
3. Acrescente o bloco acima às instruções do projeto. Preserve os comandos e as convenções
   que já existem.
4. Se quiser escolher modelos por papel, copie
   [.agents/models.example.toml](../.agents/models.example.toml) como `.agents/models.toml`
   e ajuste. Sem esse arquivo, as skills usam o modelo do ambiente. O [guia](MODELS.md)
   explica o formato.
5. `esclarecer` usa o glossário do projeto quando ele existe. Você pode partir do
   [glossário desta coleção](GLOSSARY.md).
6. Registre na documentação de manutenção do projeto a origem, a versão, o SHA e as skills
   copiadas. A skill `atualizar-harness` usa esse registro para preservar suas adaptações na
   próxima atualização.

Use `configurar-harness` apenas se quiser que o agente configure comandos e verificações do projeto.
Não há instalador, conta, serviço ou processo em segundo plano.
