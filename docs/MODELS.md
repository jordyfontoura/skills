# Modelos por papel e complexidade

A política fica em [`.agents/models.toml`](../.agents/models.toml). Ela orienta novas delegações,
sem iniciar agentes, instalar serviços ou mudar o modelo da conversa aberta. A escolha explícita
do usuário no pedido atual prevalece. Configurar um modelo não autoriza delegação nem representação.

## Configuração pessoal

O arquivo deste repositório contém as preferências pessoais aprovadas do proprietário:

| Perfil | Primeiro candidato | Alternativa por indisponibilidade |
| --- | --- | --- |
| `simple` | GPT-6 Luna medium | Claude Haiku 5.5 medium |
| `default` | GPT-6.1 Sol medium | Claude Sonnet 5.5 high |
| `hard` | Claude Opus 5.5 high | GPT-6.1 Sol high |
| `orchestrator` | Claude Opus 5.5 high | GPT-6.1 Sol high |
| `representative` | Claude Opus 5.5 high | GPT-6.1 Sol high |
| `evaluator` | Claude Opus 5.5 high | GPT-6.1 Sol high |

`planner`, usado por `specify`, usa sempre `hard`, sem mapa de complexidade. Mesmo uma
especificação pequena usa esse perfil; o tamanho do texto continua proporcional ao trabalho.
`implementer` e `reviewer` usam `default`, com mapas explícitos para `simple` e `hard`.
`orchestrator` e `representative` usam seus perfis próprios. `evaluator` e `council` compartilham
o perfil `evaluator`; alterar essa lista afeta ambos. O representante tem uma lista própria,
mesmo sendo igual à de `hard`, para que mudanças na implementação não alterem suas decisões.

Os IDs de provedor `codex` e `claudeAgent` correspondem ao T3 Code, usado pelo mantenedor.
Outros ambientes podem exigir IDs diferentes ou não oferecer esses candidatos. A tabela
registra preferências, não disponibilidade comprovada, desempenho comparado ou modelos executados.

Antes de elaborar uma spec, confira se o contexto corresponde ao candidato selecionado para
`planner`, incluindo esforço. Se não corresponder, use uma consulta autorizada ao planejador.
Se não houver contexto compatível disponível, informe o limite, sem alegar troca de modelo.
A escolha explícita do pedido prevalece sobre esta preferência. Ao adotar em outro projeto,
preserve sua política local; a skill não fixa nomes de modelos nem exige este TOML.

## Formato da versão 2

`version = 2` usa apenas `profiles` e `roles`, sem `defaults` nem seleção direta nos papéis.
Cada perfil contém uma lista `candidates` não vazia, na ordem autorizada. Cada candidato
declara `provider`, `model` e `effort`. O primeiro é a preferência; os seguintes são alternativas.

Cada `roles.<nome>` exige `when` e `profile`, com um mapa `complexity` opcional:

```toml
[roles.implementer]
when = "Implementar uma parte autorizada e verificável."
profile = "default"

[roles.implementer.complexity]
simple = "simple"
hard = "hard"
```

O mapa aceita somente `simple` e `hard`. O nível `default` sempre usa `profile`, evitando
dois padrões concorrentes. Nomes de perfis não têm significado automático: o vínculo só existe
quando declarado no papel. Um perfil pode ter qualquer nome em `kebab-case` e servir a vários papéis.

`representative`, `evaluator` e `council` não aceitam mapas de complexidade. Isso mantém sua seleção
própria, mesmo quando a implementação avaliada é simples ou difícil. Papéis adicionais podem
declarar mapas. O coordenador desta coleção não tem mapa; um mapa em outro projeto só orienta
a criação autorizada de um novo coordenador, nunca a troca do modelo de uma conversa aberta.

`when` explica o uso; não é um gatilho executável. Referências inexistentes, campos desconhecidos,
versões não suportadas e candidatos repetidos no mesmo perfil são erros. Perfis distintos podem
ter listas iguais e perfis sem uso podem ser mantidos para adoção futura.

Para herdar o ambiente, o primeiro candidato pode usar `provider = "inherit"` e `model = "inherit"`
juntos. Não misture um ID concreto com um herdado. As alternativas exigem provedor e modelo
concretos. `effort = "inherit"` pode aparecer em qualquer candidato; outro valor precisa ser
suportado pela ferramenta. A validação local não consulta provedores.

## Resolver a seleção

1. Preserve o modelo e esforço explicitamente pedidos pelo usuário e as restrições da tarefa.
2. Identifique o papel. O pedido pode fixar a complexidade; caso contrário, quem delega a classifica
   pelo trabalho e pela consequência do erro. Use `default` quando não houver motivo concreto
   para outro nível. `simple` atende edições mecânicas delimitadas; `hard`, diagnóstico difícil
   e escolhas de arquitetura com consequências relevantes. O tipo visual, escrita, pesquisa ou
   operação orienta ferramentas e provas, sem selecionar sozinho outro modelo.
3. Na v2, use o perfil indicado no mapa para o nível informado, se houver. Sem substituição,
   mantenha o perfil do papel. Nível desconhecido é erro; nível conhecido sem mapa não é.
4. Confira capacidades reais de provedor, modelo e esforço. Se o primeiro candidato estiver
   indisponível, considere somente as alternativas cadastradas, em ordem, dentro da autorização
   atual. Um modelo exigido no pedido não pode ser substituído apenas porque há alternativa.
5. Registre papel, versão, perfil efetivo, complexidade e sua origem, se ela mudou a seleção,
   motivo de eventual alternativa e modelo/esforço pedidos versus observados. O que a ferramenta
   não expuser permanece desconhecido.

Uma saída incorreta não é indisponibilidade e não autoriza escalar o modelo. Investigue ou
corrija o resultado. Se nenhum candidato elegível puder executar, informe o limite real.
Contextos independentes e provas próprias continuam necessários para avaliação; trocar o nome
do modelo não estabelece independência.

## Compatibilidade com a versão 1

A v1 continua válida sem migração: combine `defaults` com `provider`, `model` e `effort`
do papel, depois considere `fallbacks` em ordem. Ela não possui perfis ou mapas de complexidade;
um nível conhecido informado ao resolvedor mantém a seleção antiga. Não misture campos das
duas versões. Uma versão desconhecida exige esclarecimento, sem presumir outro formato.

O helper `resolve_policy(policy, role, complexity="default")`, em
[`scripts/model_policy.py`](../scripts/model_policy.py), preserva o retorno antigo da v1.
Na v2, acrescenta `profile`, `complexity` e `complexity_applied`; o último só é verdadeiro
quando o mapa muda o perfil base. As listas retornadas podem ser editadas sem alterar a política.
Esse helper é de manutenção; as skills também explicam a resolução para uso sem Python.

## Representante em uma execução autônoma

Você autoriza o objetivo e quais escolhas podem ser representadas. Quando surgir uma escolha
dentro desses limites, o coordenador consulta `representative` com contexto, opções, evidências,
preferências e consequências. O representante responde em leitura; o coordenador preserva
a autoria da decisão e continua o trabalho permitido. A revisão final do goal permanece com você.

O representante não amplia o objetivo nem decide ações reservadas ao usuário. Não inventa
fatos pessoais nem é apresentado como se você tivesse respondido. `$propose` continua aguardando
sua aprovação, salvo delegação explícita daquela decisão. O arquivo não concede essa delegação.

## Adoção e atualização

Em outro projeto, a política é opcional. Sem arquivo, preserve as seleções do ambiente e do usuário.
Para adotar as mesmas preferências, copie e adapte o TOML pessoal e este guia. Para começar
sem modelos fixados, copie [`.agents/models.example.toml`](../.agents/models.example.toml),
que herda o ambiente em todas as responsabilidades. O formato mínimo é este:

```toml
version = 2

[profiles.inherited]
candidates = [{ provider = "inherit", model = "inherit", effort = "inherit" }]

[roles.implementer]
when = "Implementar trabalho autorizado."
profile = "inherited"
```

Ao atualizar o harness, mantenha a política e as escolhas locais, inclusive v1. Atualizar skills
não exige migrar o TOML. Se uma migração fizer parte do pedido, preserve valores, ordem e
comportamento, e apresente conflitos reais. Não copie IDs pessoais por cima do destino.
As skills não exigem scripts de manutenção ou serviços para ler e aplicar essas regras.

## Verificação

`python scripts/check.py` valida formato, referências, papéis canônicos e cópias dos provedores.
`python -m unittest discover -s scripts` cobre as duas versões, ordem, isolamento, níveis sem mapa,
papéis protegidos e configurações inválidas. As provas são estruturais: disponibilidade,
esforço aceito e comportamento real do modelo dependem das ferramentas de cada execução.
