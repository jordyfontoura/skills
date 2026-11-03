# Ferramentas CLI no desenvolvimento com agentes

Use [`conhecer-ferramentas`](../skills/harness/conhecer-ferramentas/SKILL.md) para conhecer ferramentas, conferir o ambiente
ou preparar as faltantes. O [catálogo de usos](../skills/harness/conhecer-ferramentas/tools.md) explica as
opções e acompanha a skill quando ela é copiada para outro projeto. As CLIs são opcionais:
as ferramentas nativas e as restrições de cada ambiente continuam valendo.

## Como pedir

- `$conhecer-ferramentas Explique quando usar ast-grep em vez de rg.`: explicação, sem instalação.
- `$conhecer-ferramentas Confira o que está disponível para buscar código e testar uma interface.`:
  inventário delimitado, sem preparar recursos adicionais.
- `$conhecer-ferramentas Prepare as ferramentas que faltam para esta tarefa.`: inventário e lote concreto
  de instalação para aprovação, salvo autorização anterior que já cubra o lote e seus efeitos.

Uma aprovação vale para o escopo recebido e não precisa ser solicitada de novo. Instalar uma
CLI não inclui modelos, extensões, hooks ou servidores por associação. A skill registra os
efeitos necessários e diferencia presença, executável funcional e capacidade testada.

## Revalidar o ambiente

Confira resolução e versão antes de usar. No Windows:

```powershell
Get-Command ast-grep, playwright-cli, qmd, just, uv, gh
ast-grep --version
playwright-cli --version
qmd --version
qmd --index <índice> collection list
```

Depois de editar documentos, atualize apenas o índice adotado, com `qmd --index <índice> update`.
Não confunda recuperar texto com provar sua atualidade ou realizar pesquisa na internet.
`pesquisar-web` continua exigindo fontes externas quando invocada.
