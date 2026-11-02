# Padrões

## Nomes e idioma

| Parte | Convenção |
| --- | --- |
| Identificador da skill e comando | Português, curto e em `kebab-case`, como `entrevistar-por-arquivo` e `escrever-objetivo`. |
| Pasta da skill e campo `name` | Mesmo identificador; ASCII, sem acentos, espaços ou aliases. O nome continua único entre os grupos. |
| Papéis, grupos, arquivos e símbolos de código | Identificadores em inglês; respeitar formatos e convenções da ferramenta. |
| Título, descrição e instruções | Português brasileiro; o título explica a ação, como "Alinhar decisões". |
| Exemplos, modelos, documentação e mensagens de manutenção | Português brasileiro, salvo texto original que precise ser preservado. |
| Campos técnicos e arquivos convencionais | Preservar `name`, `description`, `developer_instructions`, `SKILL.md`, `AGENTS.md`, `CLAUDE.md` e `README.md`. |
| Comandos, APIs, variáveis, formatos e marcas | Preservar identificadores e sintaxe reais; explicar o significado em português quando útil. |

Forme o identificador da skill com um verbo no infinitivo, derivado do título ou do
[glossário](GLOSSARY.md), como `especificar` ("Especificar o trabalho") e `passar-contexto`
("Passagem de contexto"). Acrescente um complemento quando o verbo sozinho for ambíguo, como
`pesquisar-web` e `verificar-aceite`. Use substantivo só nas exceções listadas: `conselho` e
`andamento`. Escreva siglas em minúsculas, como `descrever-pr`. Use um sufixo para uma variação
com finalidade própria, como `entrevistar` e `entrevistar-por-arquivo`. Não mantenha aliases.

Desde a versão 0.2.0, os identificadores ficam em português. Assim o comando corresponde ao título
e ao glossário, e a coleção deixa de colidir com comandos dos agentes, como `/review` do
Claude Code, e com nomes de outras coleções. Prefira nomes que permaneçam estáveis: uma
renomeação quebra chamadas e cópias adaptadas. Registre cada renomeação no [CHANGELOG](../CHANGELOG.md),
na forma usada pela verificação de nomes antigos, e atualize referências e cópias na mesma mudança.

Use o [glossário](GLOSSARY.md) para manter o mesmo nome para o mesmo conceito.
Na primeira ocorrência relevante, explique um termo inglês necessário. Não traduza comandos
executáveis ou respostas humanas originais. Preserve citações e exemplos cujo idioma seja
o próprio objeto da análise. As skills orientam respostas em português por padrão, respeitando
um pedido explícito de outro idioma e a voz do texto que estiver sendo editado.

## Organização das fontes

Mantenha skills em `skills/<grupo>/<nome>/`, com grupos em inglês:

- `development`: desenvolvimento, especificação, diagnóstico, revisão e aceite.
- `productivity`: alinhamento, escrita, coordenação e passagem de contexto.
- `harness`: configuração, melhoria e atualização desta coleção.

A categoria descreve a finalidade principal, sem duplicar skills que servem a mais de um grupo.
Mudar uma skill de categoria não muda seu nome nem o comando. Preserve as cópias de uso em
`.agents/skills/<nome>/` e `.claude/skills/<nome>/`, geradas por `python scripts/sync.py`.
Edite as fontes agrupadas; não mantenha variações manuais nas cópias deste repositório.
Adaptações em projetos de destino continuam pertencendo a esses projetos.

## Escrita e manutenção

- Cada skill trata de um resultado, com um gatilho claro e instruções suficientes para agir.
- Mantenha as fontes neutras em relação a provedores. Coloque metadados específicos nas cópias
  e confira a consistência após editar. Para skills, gere as cópias antes da validação.
- Preserve requisitos, permissões e a diferença entre análise de código e prova de execução.
  Relate evidências ausentes explicitamente.
- Escreva de forma concreta. Acrescente uma regra apenas quando tratar uma dificuldade recorrente observada.
- Use links relativos para documentação. Skills copiadas não devem depender de caminhos da
  máquina original nem de serviço externo obrigatório.
- As verificações de manutenção usam a biblioteca padrão do Python. Ler e aplicar skills
  não exige ambiente de execução.

O validador verifica estrutura e consistência; a escolha do idioma e a qualidade da tradução
também precisam de leitura. Não use uma busca de palavras como prova de equivalência das instruções.
