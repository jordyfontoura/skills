---
name: entrevistar
description: Resolve escolhas de escopo ou design pela conversa, preservando respostas e decisões existentes. Use interview-async para rodadas respondidas em arquivos Markdown.
license: Apache-2.0
---

# Alinhar decisões

Para rodadas respondidas em arquivo Markdown, use
`entrevistar-por-arquivo`. Esta skill conduz o alinhamento pela conversa.

Leia o pedido, os arquivos relevantes, as decisões existentes e a última passagem de contexto.
Separe fatos que as ferramentas podem esclarecer de escolhas que cabem ao usuário.
Investigue os fatos primeiro.

Antes de perguntar, procure respostas nos documentos, na conversa e nas fontes conectadas
disponíveis. Reutilize respostas já estabelecidas com seu escopo e sua origem. Se houver
conflito, explique-o e pergunte apenas o necessário para resolvê-lo. Falta de acesso não é motivo
para exigir que o usuário repita todos os fatos. Não deduza dados pessoais ou consentimento
a partir de exemplos.

Separe a visão final do produto da ordem de entrega. Quando o usuário estiver definindo
a experiência final, explore essa visão sem reduzi-la silenciosamente a um MVP. Discuta etapas
de entrega como uma decisão separada quando necessário, preservando o comportamento de longo
prazo e as exclusões combinadas.

Pergunte apenas sobre escolhas que mudem comportamento, escopo, prioridades ou custo de reversão.
Agrupe perguntas independentes numa rodada curta. Apresente opções concretas e uma recomendação
justificada. Aguarde as respostas necessárias enquanto continua trabalho independente.

Não peça novamente uma escolha já resolvida ou uma autorização já concedida. Use o glossário
do projeto; se um termo divergir da implementação, explique a diferença e alinhe o significado.

Leve as respostas ao plano ou à conversa. Quando uma escolha precisar sobreviver a outra sessão,
atualize a documentação existente com contexto e consequências. Evite registros duplicados.
Uma execução autônoma autorizada pode consultar um representante em modo de leitura para
escolhas dentro da intenção do usuário; quem o consultou preserva a resposta e as evidências.

Pare quando houver definição suficiente para planejar ou executar o pedido. Use `especificar`
para trabalho substancial ou implemente diretamente uma alteração pequena já autorizada.
