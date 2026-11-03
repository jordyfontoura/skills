# Contribuir

Obrigado pelo interesse. Esta é uma coleção pessoal e curada de skills em português. PRs são
bem-vindos quando resolvem um problema observado ao usar uma skill.

## Antes de abrir um PR

- **Comece por uma issue** para skills novas, renomeações ou mudanças de comportamento. Correções
  de texto, links quebrados e erros evidentes podem ir direto para um PR.
- **Descreva o cenário:** o pedido feito ao agente, o estado inicial, o resultado observado e o
  esperado. Uma mudança entra quando teria mudado esse resultado.
- **Uma mudança por PR.** Não reescreva um `SKILL.md` inteiro para ajustar uma regra.
- **Textos gerados por IA** são aceitos depois de revisados por você. Confira fatos, links e se
  a mudança cabe no escopo pedido.
- **Opções de configuração** de um projeto ficam no `AGENTS.md` ou `CLAUDE.md` desse projeto,
  não nas skills.

## Idioma e padrões

Nomes de skills e comandos ficam em português; papéis, grupos, arquivos e demais identificadores
ficam em inglês. Descrições, instruções e documentação ficam em português brasileiro. Issues e PRs podem ser em português ou inglês.
Consulte os [padrões](docs/STANDARDS.md), o [glossário](docs/GLOSSARY.md) e a
[arquitetura](docs/ARCHITECTURE.md).

Uma skill cita outras skills e papéis pelo nome, sem links que saiam da sua pasta. Arquivos de
apoio ficam dentro da skill que os usa. Assim cada skill funciona quando copiada sozinha.

## Editar

Edite as fontes em `skills/<grupo>/<nome>/` e os papéis em `.agents/roles/`. Não edite as cópias.

1. Para papéis, atualize na mesma mudança `.claude/agents/<nome>.md` (metadados de nome,
   descrição e ferramentas, seguidos do corpo canônico) e `.codex/agents/<nome>.toml` (mesmo nome,
   descrição e corpo em `developer_instructions`). Os arquivos não fixam modelo.
2. Gere as cópias com `python scripts/sync.py`. O comando atualiza `.agents/skills/`,
   `.claude/skills/` e `agents/`, ajusta links ao layout sem grupos e recusa arquivos fora do
   catálogo em vez de apagá-los.
3. Valide com Python 3.11 ou mais recente:

   ```text
   python scripts/check.py
   python -m unittest discover -s scripts
   ```

   `check.py` confere metadados, links locais, JSON e TOML, a política de modelos, os manifestos
   do plugin e a consistência das cópias. Também recusa componentes executáveis no plugin e
   caracteres invisíveis. Não usa rede nem instala pacotes. A CI roda os mesmos comandos.
4. Se tiver o Claude Code instalado, confira o plugin:

   ```text
   claude plugin validate . --strict
   claude --plugin-dir . plugin details jordyfontoura-skills
   ```

Essas verificações provam organização e consistência. A qualidade de uma skill também exige
exercitar o procedimento num cenário real; descreva no PR o que você executou e observou.

Se você instalou o plugin e trabalha neste repositório, as skills aparecem duas vezes: as do
plugin e as de `.claude/skills/`. Desative o plugin enquanto edita.

## Licença das contribuições

Ao enviar uma contribuição, você concorda que ela seja licenciada sob a
[Apache-2.0](LICENSE), conforme a seção 5 da licença. Envie apenas conteúdo que você tem
direito de licenciar. Não traga texto de outras coleções sem licença compatível e o aviso
correspondente. Isso inclui as skills proprietárias `docx`, `pdf`, `pptx` e `xlsx` da Anthropic.
Declare no PR as fontes e inspirações usadas.

## Versões

O mantenedor define a versão em `.claude-plugin/plugin.json` e a entrada correspondente em
[CHANGELOG.md](CHANGELOG.md) ao preparar um release. Contribuidores não alteram a versão.
Na série 0.x, renomear ou remover uma skill ou papel, ou mudar a semântica de autorização,
sobe a versão MINOR; mudanças compatíveis sobem a PATCH.
