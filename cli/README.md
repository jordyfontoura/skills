# CLI de adoção guiada

`@jordyfontoura/skills` instala cópias editáveis de skills e papéis no projeto atual.
Pergunta quais agentes você usa e como pretende trabalhar, recomenda skills e permite
revisar a seleção antes de gravar. Requer Node.js 22 ou superior e npm.

Execute na raiz do projeto que receberá as skills:

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

O build usa o gerador existente para preparar as skills com seus apoios e links para uma
biblioteca compartilhada. O pacote leva JavaScript compilado e o conteúdo pronto; quem o
instala dispensa Python e o clone deste repositório.

## Biblioteca compartilhada

Nas instalações pelo CLI, Codex e Claude Code usam a mesma pasta `knowledge/harness/` na
raiz do projeto. Os guias não são repetidos dentro das skills nem por agente:

```text
projeto/
├── knowledge/harness/
│   ├── README.md
│   ├── ux/
│   └── accessibility/
├── .agents/skills/consultar-conhecimento/SKILL.md
└── .claude/skills/consultar-conhecimento/SKILL.md
```

O CLI ajusta os links das skills para a biblioteca e inclui `consultar-conhecimento` quando
alguma skill escolhida usa guias. Você também pode escolher essa skill diretamente. Ela
disponibiliza o índice e seus guias e orienta a localizar e ler somente o material pertinente.
Ter a biblioteca instalada não significa carregar todos os textos em toda sessão.

A prévia informa os guias compartilhados e os arquivos que serão criados. O índice e suas
dependências entram uma única vez, inclusive quando ambos os agentes são selecionados.
O catálogo pode ser consultado sem instalar skills no projeto:

```bash
npx @jordyfontoura/skills knowledge list
npx @jordyfontoura/skills init --agents codex,claude-code --skills consultar-conhecimento --dry-run
```

Para usar o código local, execute `node cli/dist/index.js knowledge list` na raiz do
repositório. O comando lista o conteúdo disponível no pacote, não os arquivos instalados
no projeto; para estes, use `status`.

Arquivos próprios fora de `knowledge/harness/` são preservados. Se houver uma adaptação em
um guia compartilhado, o conflito interrompe toda a instalação antes de gravar. Os recibos
incluem os hashes da biblioteca; `status` identifica alterações e ausências nos mesmos guias
usados pelos dois agentes. Remover uma skill não deve remover guias usados por outras.

O layout compartilhado é próprio do CLI. O plugin continua usando `knowledge/` na origem;
as cópias manuais em `.agents/skills/` e `.claude/skills/` continuam autocontidas, com guias
em `references/knowledge/`. O CLI não migra automaticamente uma instalação anterior: use
`atualizar-harness` para comparar adaptações e ajustar os links antes de retirar cópias antigas.

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

`--models` continua criando `.agents/models.toml` com o exemplo neutro, somente se ele não
existir. Quando a seleção inclui papéis, `delegar`, `conselho` ou `verificar-aceite`, o modo
interativo também oferece uma pergunta opcional: pular, criar uma política neutra ou
configurar modelos e perfis. A política entra na mesma prévia e confirmação da instalação.
Se o arquivo já existe, o CLI o preserva e informa que ele não foi validado.

## Configurar modelos

O comando dedicado não exige escolher skills nem agente e também funciona depois da adoção.
Para experimentar o código local:

```bash
node cli/dist/index.js models init --dir ./work/meu-projeto
```

Pelo npm:

```bash
npx @jordyfontoura/skills models init
```

O configurador oferece três caminhos:

- **Herdar o ambiente:** usa o mesmo exemplo neutro de `--models`.
- **Modelo compartilhado:** define candidatos para um perfil base usado pelas sete responsabilidades.
- **Por perfis:** separa trabalho simples, habitual e difícil, coordenação, aceite/conselho e
  representação. Você escolhe quais personalizar; os demais herdam o ambiente. A associação
  de cada responsabilidade ao perfil base pode ser revisada numa etapa opcional.

Para cada perfil personalizado, informe o provedor, o modelo e o esforço que sua ferramenta
de delegação aceita. Também é possível herdar o modelo e definir apenas o esforço. Alternativas
são concretas, ordenadas e usadas por indisponibilidade. Não há catálogo de modelos embutido
nem inferência de provedor a partir de Codex ou Claude Code.

No modo por perfis, `planner`, `implementer` e `reviewer` recebem mapas `simple`/`hard`;
`default` continua sendo o perfil base escolhido. `evaluator`, `council` e `representative`
não recebem esses mapas. Os perfis de representação e trabalho difícil são separados.
Inicialmente o conselho usa o perfil de aceite; você pode mudar a associação opcionalmente.

A política orienta novas delegações autorizadas. Ela não muda o modelo da conversa aberta,
não autoriza delegação nem representação e não grava modelos nos arquivos nativos dos papéis.
A validação é estrutural: não consulta contas, credenciais, disponibilidade ou esforços aceitos
pelos provedores. Não é preciso ter instalado os três arquivos de papéis para configurar as
responsabilidades previstas na política.

O CLI só cria arquivos ausentes. Um arquivo existente é preservado byte a byte, inclusive
comentários, políticas v1 e conteúdo inválido; ele não é lido como TOML nem validado. Não há
migração ou edição automática. Use `--print` para consultar outra proposta sem tocar o destino.

Para automação, `models init` aceita `--neutral` ou `--config arquivo.json`. A segunda opção
recebe o objeto de política v2 completo, valida referências e regras e o serializa como TOML.
Arquivos `.env` não são aceitos como configuração. Exemplo de JSON, com IDs ilustrativos:

```json
{
  "version": 2,
  "profiles": {
    "default": {
      "candidates": [{ "provider": "minha-ferramenta", "model": "meu-modelo", "effort": "inherit" }]
    }
  },
  "roles": {
    "implementer": { "when": "Implementar trabalho autorizado.", "profile": "default" }
  }
}
```

Para gerar a política sem perguntas:

```bash
npx @jordyfontoura/skills models init --neutral --dry-run
npx @jordyfontoura/skills models init --config ./policy.json --print
npx @jordyfontoura/skills models init --config ./policy.json --yes
```

Sem terminal interativo, escolha explicitamente `--neutral` ou `--config`; a gravação exige
`--yes`. `--print` escreve somente TOML na saída e não cria diretórios. Sem uma configuração
explícita, `--print` em execução não interativa mostra a política neutra. `--dry-run` mostra
a prévia sem gravar. Essas opções não permitem sobrescrever um arquivo existente.

Também é possível usar seleções explícitas:

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
Se você editar um `models.toml` criado pelo CLI, `status` mostrará `alterado`; isso é uma
personalização esperada, não uma instrução para restaurar o modelo original.

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
Os testes de política usam casos de contrato compartilhados entre Python e TypeScript e
conferem o TOML emitido com `tomllib` e `model_policy.py`. Python é necessário nessa prova
da origem, mas não no consumidor do pacote.
As perguntas e o cancelamento são exercitados com streams controlados; a renderização em
terminais reais precisa de conferência manual. A CI também executa em Linux e Windows,
com Node.js 22 e 24; configurar essa matriz não comprova uma execução remota.

O catálogo é gerado a partir das fontes existentes. As recomendações e apoios dos papéis
ficam em `src/catalog.ts`. O pacote acompanha a versão de `.claude-plugin/plugin.json`;
não altere a versão por commit de desenvolvimento. A publicação não acontece na CI.
