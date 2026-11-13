# Adotar em outro projeto

Há duas rotas. Escolha uma por agente: usar o plugin e cópias ao mesmo tempo faz cada skill
aparecer duas vezes.

| Rota | Para quem | Atualização |
| --- | --- | --- |
| Plugin | Claude Code e Codex, sem editar as skills. | Pelo gerenciador de plugins do agente. |
| Cópia manual | Quem quer adaptar as skills ou usa outro agente. | Pela skill `atualizar-harness`. |

O [CLI de adoção guiada](../cli/README.md), em desenvolvimento, automatiza a rota de cópias
editáveis para Codex e Claude Code. Ele recomenda skills por práticas de trabalho, oferece
papéis opcionais e mostra os arquivos antes da instalação. A publicação no npm está pendente;
o guia explica como experimentar o código local.

## Plugin

Os comandos estão no [README](../README.md#instalar). O plugin traz as 29 skills; no Claude Code,
também os papéis `planner`, `evaluator` e `representative`. O Codex não recebe papéis por plugin:
copie os arquivos de [.codex/agents/](../.codex/agents/) para a pasta `.codex/agents/` do projeto.

Dentro de uma sessão do Claude Code, a instalação também pode ser feita com
`/plugin marketplace add jordyfontoura/skills` e
`/plugin install jordyfontoura-skills@jordyfontoura`. Para conferir, digite
`/jordyfontoura-skills:` ou rode `claude plugin list` no terminal.

### Custo de contexto

O nome e a descrição de cada skill entram em toda sessão. Na versão 0.2.0, o
`claude plugin details` estima cerca de 1.500 tokens fixos para o plugin inteiro. O texto
completo de uma skill só é carregado quando ela é usada. Desative o plugin nos projetos
em que não o usar.

### Instruções do projeto

O plugin não carrega instruções de projeto. Para que o agente use as skills no momento certo
sem que você as chame, acrescente o bloco abaixo ao seu `AGENTS.md` ou `CLAUDE.md`.

## Bloco para AGENTS.md ou CLAUDE.md

Adapte o texto às regras do seu projeto. As skills funcionam sem ele quando chamadas pelo nome.

```markdown
## Fluxo com as skills

- Quando eu pedir `propor` ou pedir para explicar antes de agir, apresente a abordagem e
  aguarde minha aprovação.
- Com requisitos claros, implemente por entregas úteis, com plano curto quando necessário.
- Use `entrevistar` para escolhas abertas de escopo ou design e `especificar` para definir
  comportamentos, contratos ou dependências ainda incertos, ou quando eu pedir uma spec.
  Preserve definições existentes; tamanho do trabalho não exige especificação por si só.
- Use `implementar` para entregar partes pequenas e verificáveis; relate os comandos executados
  e os resultados observados. Prova ausente continua ausente.
- Use `revisar` para analisar diffs contra requisitos e riscos aplicáveis, sem transformar
  melhorias opcionais em bloqueios. Use `verificar-aceite` quando houver aceite independente exigido.
- Delegue apenas divisões autorizadas com ganho concreto; ter um papel não obriga uma consulta.
- Localize por busca (`rg -n`) e leia o trecho; não releia inteira uma saída já salva.
  Requisitos e critérios continuam lidos por inteiro na revisão e no aceite.
- Repita as provas afetadas por mudanças e preserve as ainda válidas. Uma pendência bloqueia
  seu trabalho dependente; ordens e portões explícitos continuam valendo.
- Use `andamento` para consultas de andamento e `passar-contexto` quando outra sessão for retomar.
- Aplique `escrever-claro` ao escrever documentos, títulos, descrições e mensagens.
- Explorar não autoriza implementar, e uma pergunta não conta como aprovação.
```

## Cópia manual

Escolha a referência da origem antes de copiar: `main` para o canal estável (padrão), `nightly`
para novidades em avaliação ou uma tag `vX.Y.Z` para uma versão específica. Os links abaixo
abrem os arquivos na referência que você está consultando no GitHub; confira a branch ou tag.
Publicar na origem não atualiza as cópias instaladas nos seus projetos.

1. Copie as skills escolhidas de [.agents/skills/](../.agents/skills/) (Codex e outros agentes)
   ou de [.claude/skills/](../.claude/skills/) (Claude Code) para a mesma pasta no seu projeto.
   Copie a pasta inteira, incluindo `references/knowledge/` quando existir: ali estão os
   guias usados pela skill, com links internos. Os arquivos de apoio não dependem do clone
   original. Outras skills são citadas pelo nome; copie também as necessárias ao fluxo pedido.
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
6. Registre na documentação de manutenção do projeto a origem, o canal ou referência fixa,
   a versão, o SHA e as skills copiadas. A skill `atualizar-harness` usa esse registro para preservar suas adaptações na
   próxima atualização.

Para acompanhar as novidades, peça: `$atualizar-harness Atualize as skills pela branch nightly
de jordyfontoura/skills, preservando nossas adaptações.` Nas próximas atualizações, a skill
mantém o canal registrado. Para voltar ao canal estável, peça explicitamente `main`; confira
as mudanças que essa troca pode retirar. Uma versão específica pedida prevalece sobre o canal.

Use `configurar-harness` apenas se quiser que o agente configure comandos e verificações do projeto.
As cópias manuais dispensam instalador. O CLI opcional exige Node.js e npm, sem conta,
serviço ou processo em segundo plano para usar o conteúdo instalado.

## Biblioteca de conhecimento

Na origem, [knowledge/](../knowledge/README.md) é a única fonte editável dos guias de domínio.
O plugin completo leva essa pasta junto das skills. As cópias avulsas já incluem apenas os
guias referenciados por cada skill, inclusive suas dependências, em `references/knowledge/`.
Copiar somente `SKILL.md` deixa recursos de fora. Não é preciso instalar o gerador no destino.

Registre o SHA adotado também para as referências empacotadas. Ao atualizar, compare o
pacote anterior, a origem nova e suas adaptações; um cabeçalho de geração não autoriza
sobrescrever uma edição local. Se o mesmo guia foi adaptado em mais de uma skill, confira
as diferenças antes de mesclar. Não transforme uma cópia antiga em fonte do harness.

Destinos que adotam as fontes agrupadas precisam incluir `knowledge/` e usar geração
compatível; nesse layout, os links canônicos apontam para a biblioteca compartilhada.
Uma referência retirada da origem pode deixar uma cópia extra: confira e migre-a explicitamente,
pois `sync.py` recusa arquivos extras em vez de apagá-los. Conteúdo de domínio e mudanças de
método têm revisões próprias; notas, pisos e critérios de aceite não são reduzidos pela atualização.
