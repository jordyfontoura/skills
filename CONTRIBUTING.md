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

## Branches e canais

`main` é o canal estável e continua como branch padrão do GitHub. `nightly` é a branch
permanente de desenvolvimento, com novidades ainda em avaliação. O nome não implica
publicação diária nem atualização automática dos projetos que copiaram as skills.

Crie branches de trabalho a partir de `nightly` e abra PRs com base em `nightly`. Como o
GitHub usa `main` por padrão, confira a base ao abrir cada PR. Por exemplo, com a árvore limpa:

```bash
git fetch origin
git switch nightly
git pull --ff-only origin nightly
git switch -c feat/minha-mudanca
```

A CI verifica pushes nas duas branches e todos os PRs. As atualizações de versão do Dependabot
têm como destino `nightly`; atualizações de segurança continuam seguindo a branch padrão.
O GitHub lê a [configuração do Dependabot na branch padrão](https://docs.github.com/en/code-security/concepts/supply-chain-security/about-the-dependabot-yml-file),
então o novo destino passa a valer quando essa configuração chegar a `main` na primeira promoção.
Branches de trabalho podem ser integradas em `nightly` por merge ou squash.

Quando todo o conteúdo de `nightly` estiver aprovado para uso estável:

1. Prepare a versão e o CHANGELOG em `nightly` e execute as verificações abaixo.
2. Abra um PR de `nightly` para `main`, confira os checks e integre com **Create a merge commit**.
   Preserve o histórico entre as branches: não use squash ou rebase nessa promoção.
3. Crie a tag `vX.Y.Z` no commit resultante em `main` e publique a versão estável.
4. Integre `main` de volta em `nightly` por merge para incorporar o commit da promoção.
   Mantenha `nightly` para o próximo ciclo.

O PR de promoção leva todas as mudanças acumuladas. Se alguma ainda não estiver pronta,
adie a promoção ou retire essa mudança de `nightly` antes de promover.

Para uma correção urgente no canal estável, crie uma branch a partir de `main` e abra o PR
para `main`. Depois de verificar e integrar, traga `main` para `nightly` por merge, preservando
a correção e o histórico. Nunca force push em nenhum dos canais.

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
[CHANGELOG.md](CHANGELOG.md) em `nightly`, ao preparar a promoção estável. Contribuidores não
alteram a versão. Durante o desenvolvimento, registre mudanças em `[Não lançado]`; o SHA de
`nightly` identifica o conteúdo em avaliação, mesmo que a versão do plugin ainda seja a anterior.
Tags `vX.Y.Z` identificam versões estáveis em `main` e não devem ser movidas após publicadas.
Na série 0.x, renomear ou remover uma skill ou papel, ou mudar a semântica de autorização,
sobe a versão MINOR; mudanças compatíveis sobem a PATCH.
