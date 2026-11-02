---
name: interview-async
description: Conduz rodadas de perguntas respondidas em arquivos Markdown, preservando respostas e consolidando decisões até os pontos importantes estarem definidos. Use interview para alinhamento pela conversa.
license: Apache-2.0
---

# Alinhamento assíncrono por arquivo

Use este modo quando o usuário quiser responder perguntas em Markdown, no seu tempo, e
retomar com o agente depois. Aplique os critérios de `interview`: investigar fatos disponíveis,
preservar escolhas já feitas e perguntar só o que muda o resultado. Escreva as rodadas em
português brasileiro, salvo pedido diferente, usando o vocabulário do projeto.

## Preparar o alinhamento

Leia os documentos, decisões e perguntas existentes antes de criar arquivos. Reutilize o
formato que o projeto já adota. Se não houver, copie e preencha o
[modelo](alignment.template.md) na documentação do projeto, por exemplo em
`docs/alignment/<tema>.md`. O caminho é uma sugestão, não uma estrutura obrigatória.
Substitua as perguntas de exemplo por perguntas reais antes de apresentar o arquivo.

Declare o objetivo da conversa, o que fica fora e qual próxima etapa as respostas devem
destravar. Diferencie a visão final do produto da ordem de implementação. Pergunte o que
precisa ser decidido para esse objetivo, sem tentar detalhar antecipadamente todo o sistema.
Registre fatos com suas fontes; uma preferência humana não é um fato descoberto pelo agente.

Organize as escolhas pelas suas dependências. A rodada atual contém perguntas cujos
pré-requisitos já estão definidos. Deixe temas dependentes numa lista curta com o motivo da
espera. Se descobrir um ciclo, formule a escolha conjunta necessária para desfazê-lo em vez
de esperar que perguntas bloqueadas se resolvam sozinhas.

Priorize as perguntas de maior consequência: comportamento central, limites importantes,
riscos e decisões difíceis de reverter. Mantenha a rodada confortável de responder; algo
como três a cinco perguntas costuma bastar, mas não é um limite obrigatório. Não inclua
uma questão só para preencher uma categoria de um checklist.

## Formular perguntas sem preencher respostas

Mantenha IDs estáveis, como `P001`, seguindo os existentes quando houver. Nunca renumere nem
reutilize IDs. Para cada pergunta, registre o motivo, dependências, alternativas reais e a
recomendação do agente em campo separado, com sua justificativa e limites.

Use enunciados neutros. Aceite resposta livre e propostas fora das opções. Não molde a pergunta
para que qualquer "sim" pareça concordância. Um "sim" só resolve uma pergunta se o referente
for inequívoco; uma recomendação alterada não herda a aceitação da versão anterior.

O usuário escreve no campo `Resposta`. O agente não o preenche, reescreve, corrige nem apaga.
Não aplique edição de estilo ao texto humano original. Uma síntese fica em outro campo,
ligada à resposta. Preserve autoria e data quando disponíveis, sem inventá-las ou exigir
que o usuário preencha metadados para conseguir participar.

Explique como retomar: salvar o arquivo e avisar "respondi" ou chamar `interview` de novo.
Sem um gatilho externo já autorizado, o agente não acompanha edições sozinho. Não instale
monitoramento, agendamento ou uma dependência de infraestrutura para viabilizar este modo.

## Processar uma rodada

1. Releia o arquivo salvo e as decisões relevantes. Compare com o estado anteriormente lido,
   quando disponível, e processe as respostas novas ou alteradas.
2. Preserve respostas em branco como pendentes. Processe respostas parciais sem bloquear as
   independentes. "Não sei" mantém uma lacuna; "adiar" registra uma pendência e sua consequência,
   sem autorizar uma escolha padrão. Uma ambiguidade relevante pede esclarecimento vinculado
   à pergunta original, sem assumir a alternativa preferida do agente.
3. Sintetize escolhas explícitas em decisões ligadas às perguntas de origem, com motivo,
   consequências e pendências. Distinga recomendação, resposta, decisão e autorização para
   executar. Resposta recebida não significa aprovação geral de um plano ou implementação.
4. Se uma resposta mudou, preserve o histórico conhecido e indique qual decisão substitui a
   anterior. Marque perguntas e decisões dependentes para reavaliar. Não invente o texto antigo
   se ele não estiver disponível; registre a mudança observada e a lacuna.
5. Recalcule o que ficou destravado. Acrescente apenas perguntas relevantes ainda sem resposta,
   reutilizando as existentes quando possível. Explique qualquer reabertura de uma decisão
   pelo novo fato, mudança de preferência ou contradição que a motivou.
6. Resuma no chat o que foi incorporado, quais IDs precisam de resposta e onde responder.
   Não duplique a rodada inteira no chat se ela já está no arquivo.

Se houver um decisor delegado autorizado, registre suas respostas com essa atribuição e
dentro do escopo recebido. Nunca as apresente como texto ou aprovação do usuário. Pareceres
de `council` podem informar recomendações; não substituem automaticamente quem decide.

## Editar sem perder trabalho humano

Mantenha perguntas respondidas acessíveis por seus IDs; não apague nem mova respostas a cada
rodada. Ao mudar um enunciado ou recomendação já respondido, preserve a versão vinculada à
resposta e crie a revisão necessária. Convide o usuário a acrescentar uma mudança datada ao
rever uma resposta, mas aceite também edições diretas sem tentar restaurar conteúdo por conta própria.

Releia o arquivo imediatamente antes de editar. Faça alterações pontuais nos campos do agente
e use o conteúdo observado como condição da edição. Se o trecho mudou, releia e concilie;
não sobrescreva o arquivo inteiro a partir de uma cópia antiga. Preserve conteúdo fora do
formato esperado e esclareça somente o que impedir a interpretação.

Isso reduz conflitos, mas não é uma trava: um editor com alterações não salvas pode gravar
uma versão antiga depois. Se houver conflito, preserve as duas versões conhecidas e peça a
resolução específica. Em trabalho com vários agentes, um único responsável edita o arquivo;
os demais devolvem sugestões sem escrever nele.

## Saber quando parar

Ao fim de cada rodada, pergunte ao próprio trabalho: resta alguma escolha importante que
bloqueia o objetivo declarado? Registre dependências e incertezas de modo explícito. Quando
não houver bloqueadores, proponha "alinhamento suficiente para <próxima etapa>" e resuma as
decisões e os itens que podem ficar para depois. Não gere mais perguntas apenas porque seria
possível detalhar o produto. Não encerre por um número fixo de rodadas nem adote padrões por silêncio.

Uma pendência importante adiada continua bloqueante até existir uma decisão explícita sobre
como tratá-la ou limitar o escopo. Se uma escolha depende de pesquisa, diga qual evidência falta
em vez de pedir a mesma preferência novamente. Trabalho independente pode continuar se autorizado.

Use o registro para retomar sem repetir a entrevista. Quando houver um documento de decisões
oficial, consolide ali as escolhas autorizadas e mantenha links de origem no alinhamento,
sem criar duas cópias concorrentes da decisão vigente. Preserve as respostas históricas.
`specify` pode usar esse resultado para planejar; não é uma etapa obrigatória do modo assíncrono.
Autorizações anteriores continuam válidas dentro do escopo, mas o pedido de alinhar uma ideia
não autoriza por si só implementá-la.

Este modo se inspira na organização de escolhas por dependência da
[grilling, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills%2Fproductivity%2Fgrilling%2FSKILL.md),
adaptada para respostas em arquivo e encerramento por suficiência.
