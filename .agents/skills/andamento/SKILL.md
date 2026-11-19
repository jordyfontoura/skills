---
name: andamento
description: Resume o andamento do pedido inteiro, pendências, bloqueios e próxima entrega utilizável, sempre com uma faixa de tempo estimada até a conclusão. Use para consultas rápidas sem mudar o objetivo; `passar-contexto` prepara a retomada por outra sessão.
license: Apache-2.0
---

# Consultar o andamento

Responda na conversa, sem salvar arquivo, com o que o contexto e os últimos resultados mostram.
A consulta é de leitura: não muda o objetivo nem as prioridades e não vale como aprovação.
Depois do resumo, retome a etapa que já estava autorizada. Se o trabalho aguardava uma decisão
ou um acesso, ele continua aguardando.

Cubra o pedido inteiro até sua condição de conclusão, não só a etapa atual, com o detalhe
que a pergunta pede:

- o que foi entregue e verificado, e o que está em andamento;
- o que falta, na ordem das dependências, incluindo revisão, testes, aceite e publicação exigidos;
- o que depende do usuário e os impedimentos observados, ou "nenhum bloqueio conhecido";
- a próxima entrega que o usuário poderá ver, testar ou usar, e a próxima ação.

Separe o que foi verificado, relatado antes, inferido e desconhecido. Uma prova anterior só
vale se ainda se aplica à revisão e ao ambiente atuais.

Toda resposta de andamento deve trazer uma faixa de tempo restante até concluir o goal ou
pedido inteiro, mesmo quando o usuário perguntar apenas "como está?". Informe limite inferior,
superior e unidade, como "entre 30 e 60 minutos", incluindo as verificações e entregas exigidas.
Uma estimativa da próxima etapa pode complementar essa faixa, mas não substituí-la.

Fundamente a faixa no escopo restante, no progresso observado e nas dependências conhecidas.
Com pouco contexto, dê uma faixa preliminar mais ampla, declare a baixa confiança, as hipóteses
e o que permitirá refiná-la; não substitua a faixa por "não é possível estimar". Não apresente
a estimativa como prazo garantido. Atualize-a quando novas evidências mudarem a previsão.
Esperas sem prazo, como uma aprovação, ficam como condição explícita fora da faixa: estime
o trabalho restante após a liberação, sem sugerir que esse seja o prazo total de calendário.
Se o pedido já estiver concluído, informe "0 a 0 minutos restantes" e a evidência de conclusão.
Use o que já está no contexto: não rode comandos, meça nem delegue só para obter um número,
e não converta contagem de tarefas em percentual.

Para outra conversa, use só ferramentas de observação e informe a fonte e o momento do último
registro. Algumas leituras marcam o resultado de um agente como entregue; não consuma resultados
de outra coordenação para montar o resumo.
