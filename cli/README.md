# CLI de adoção guiada

`@jordyfontoura/skills` instala cópias editáveis de skills e papéis no projeto atual.
Pergunta quais agentes você usa e como pretende trabalhar, recomenda skills e permite
revisar a seleção antes de gravar. Requer Node.js 22 ou superior e npm.

O pacote está em desenvolvimento. O comando abaixo ficará disponível depois da publicação
no npm; implementar o CLI não publica o pacote.

```bash
npx @jordyfontoura/skills init
```

## Experimentar o código local

Na raiz deste repositório, com Python 3.11+ e Node.js 22+:

```bash
npm ci --prefix cli
npm run build --prefix cli
node cli/dist/index.js --help
node cli/dist/index.js init --dir ./work/meu-projeto --dry-run
```

O build inclui cada pasta de skill completa, com seus apoios e `references/knowledge/`,
usando o gerador existente. O pacote leva JavaScript compilado e o conteúdo pronto; quem
o instala dispensa Python e o clone deste repositório.

## Escolher conteúdo

Escolha Codex, Claude Code ou ambos. Diretórios existentes sugerem os agentes, mas a
escolha continua editável. Você pode receber recomendações por práticas, escolher no
catálogo ou consultar as instruções do plugin completo.

As recomendações começam com `implementar`, `escrever-claro` e `esclarecer`, e acrescentam
skills conforme suas escolhas: aprovação da abordagem, execução direta quando solicitada,
retomada entre sessões, PRs e revisão, pesquisa e requisitos, aceite independente e interfaces.
Você pode desmarcar qualquer recomendação na seleção final.

Os papéis `planner`, `evaluator` e `representative` são opcionais. Cada papel acrescenta as
skills de apoio necessárias, com aviso antes de instalar. Outras skills citadas são sugestões
e não entram automaticamente. Instalar um papel não autoriza delegação nem representação.

`--models` cria `.agents/models.toml` com o exemplo neutro que herda o ambiente, somente
se o arquivo não existir. Políticas locais são preservadas. A opção é avançada e não faz
parte das recomendações iniciais.

Depois da publicação, será possível usar seleções explícitas:

```bash
npx @jordyfontoura/skills list
npx @jordyfontoura/skills init --agents codex,claude-code --skills implementar,propor --dry-run
npx @jordyfontoura/skills init --agents codex --scenarios sessions,reviews --yes
npx @jordyfontoura/skills init --agents codex --skills none --roles evaluator --models --yes
npx @jordyfontoura/skills status
```

`--skills all` seleciona todo o catálogo; `--roles all`, todos os papéis. Repita as flags
ou separe os nomes por vírgula. Sem terminal interativo, informe `--agents` e `--skills`
ou `--scenarios`; a gravação também exige `--yes`. Essa confirmação nunca permite
sobrescrever conflitos. `--dir` escolhe o projeto e `--dry-run` não cria arquivos nem
diretórios. Os identificadores das situações aparecem em `list`.

## Arquivos e preservação

- Codex recebe skills em `.agents/skills/` e papéis em `.codex/agents/`.
- Claude Code recebe skills em `.claude/skills/` e papéis em `.claude/agents/`.
- Arquivos idênticos são mantidos. Um conflito interrompe toda a instalação antes da escrita.
- Links simbólicos e junções no caminho de destino são recusados.
- Uma falha durante a instalação desfaz os arquivos que essa operação criou.
- `AGENTS.md` e `CLAUDE.md` não são alterados. O CLI mostra um bloco sugerido com as skills
  selecionadas para você adaptar às regras existentes.

Evite cópias das mesmas skills fornecidas pelo plugin. O CLI apresenta essa orientação;
não detecta todos os plugins globais habilitados. A rota de plugin continua disponível.

Cada seleção gera um recibo imutável em `.harness/receipts/`, com origem, versão, SHA de
base, hash do conteúdo empacotado, seleção e hashes dos arquivos. Builds com mudanças
locais são identificados como tal: o SHA de base não é a revisão exata desse conteúdo.
Recibos anteriores são mantidos em adoções parciais. Versione-os com os arquivos instalados.

`status` mostra arquivos íntegros, alterados ou ausentes, sem consultar novidades na rede.
Modelos locais preservados não são reivindicados pelo recibo. Para atualizar ou mesclar
adaptações, use `atualizar-harness` com os recibos e a origem desejada. O CLI não atualiza
automaticamente nem mescla Markdown.

## Manter e verificar

```bash
npm run build --prefix cli
npm run typecheck --prefix cli
npm test --prefix cli
npm run bundle --prefix cli
python scripts/check.py
python -m unittest discover -s scripts
```

Os testes exercitam o executável e um consumidor do `.tgz` real, incluindo referências,
papéis, conflitos, repetição, simulação e preservação de arquivos. O teste do pacote instala
dependências em `work/` e pode precisar de rede. Os testes do harness continuam necessários.
As perguntas e o cancelamento são exercitados com streams controlados; a renderização em
terminais reais precisa de conferência manual. A CI também executa em Linux e Windows,
com Node.js 22 e 24; configurar essa matriz não comprova uma execução remota.

O catálogo é gerado a partir das fontes existentes. As recomendações e apoios dos papéis
ficam em `src/catalog.ts`. O pacote acompanha a versão de `.claude-plugin/plugin.json`;
não altere a versão por commit de desenvolvimento. A publicação não acontece na CI.
