---
name: andamento
description: Resume o andamento do pedido inteiro, pendências, bloqueios, próxima entrega utilizável e previsão fundamentada de conclusão, ou o motivo de ainda não estimar. Use para consultas rápidas sem mudar o objetivo; `reconciliar` audita requisitos e `passar-contexto` prepara retomada.
license: Apache-2.0
---

# Consultar o andamento

Responda à pergunta com o contexto e os últimos resultados disponíveis. Preserve o objetivo,
as decisões e a etapa autorizada. Uma consulta de andamento não cancela a execução, não muda
prioridades nem concede aprovação para uma ação que estava aguardando decisão.

## Consultar sem desviar

Na mesma conversa, responda quando o ambiente entregar a pergunta ao agente. A skill não
controla filas, pausas ou interrupções da ferramenta e não promete resposta simultânea à
execução. Depois do resumo, continue a etapa que estava em andamento e já autorizada.
Se o trabalho terminou ou aguardava aprovação, acesso ou outra condição de retomada,
informe isso e preserve esse estado; a pergunta não libera a espera nem inicia trabalho novo.

Se a consulta aponta outra conversa, use apenas ferramentas disponíveis de observação,
sem enviar mensagens, reiniciar, cancelar ou assumir o trabalho observado. Confira os efeitos
da leitura: se ela marca resultados como entregues ou altera a coordenação de outra execução,
não consuma esses resultados para montar o resumo. Sem acesso adequado, declare o limite.
Identifique a conversa, a fonte e o momento do último registro consultado; atividade antiga
não comprova o que o agente está fazendo agora.

Use leitura complementar apenas quando necessária para responder à pergunta. Não transforme
uma consulta curta em investigação geral, não espere tarefas terminarem nem consulte seu
estado repetidamente. Durante a consulta, não edite arquivos, crie registros de acompanhamento,
faça commits, delegue ou execute verificações que alterem estado. A continuação do trabalho
original segue suas próprias permissões depois da resposta.

## Mostrar o que ajuda a decidir

Adapte o detalhe à pergunta; estes pontos não exigem seções vazias ou um relatório fixo:

- **Situação atual:** objetivo e etapa, incluindo o que depende de uma ação do usuário.
- **Feito:** entregas e verificações observadas, com referências úteis às evidências.
- **Em andamento:** ação atual conhecida ou último retorno observado de uma parte delegada.
- **Restante até concluir o pedido:** trabalho pendente na ordem das dependências, incluindo
  revisão, testes, aceite e publicação quando exigidos, não apenas o fim da etapa atual.
- **Mudança desde o último resumo:** avanço, descoberta ou regressão relevante, quando houver
  uma referência anterior disponível na conversa.
- **Próxima entrega utilizável:** o que o usuário poderá ver, testar ou usar e o que falta até lá.
- **Previsão:** horizonte do pedido inteiro ou da parte estimável, com base e incertezas explícitas.
- **Impedimentos:** falha ou dependência observada, consequência e condição para destravar.
  Diferencie bloqueio de risco ou dúvida; sem impedimento observado, diga “nenhum bloqueio conhecido”.
- **Próxima ação:** passo concreto que será retomado ou condição que continua aguardando.

Separe o que foi verificado, relatado anteriormente, inferido da atividade e o que é desconhecido.
Algo implementado sem validação deve aparecer com essa ressalva. Uma prova anterior precisa
continuar aplicável à revisão e ao ambiente atuais; edições posteriores podem exigir nova prova.
Não invente percentuais, prazos ou ausência de bloqueios. Uma foto parcial de arquivos em edição
não comprova conclusão nem falha da entrega.

## Estimar o que falta

Quando o usuário perguntar quanto falta, sempre responda com uma previsão fundamentada ou
com o motivo de ainda não haver previsão útil e o marco que permitirá estimar. Nas demais
consultas, inclua-a quando ajudar a decidir se espera ou intervém. Nomeie o ponto de chegada:
etapa atual, próxima entrega utilizável ou condição de conclusão do pedido inteiro.

Use o contexto disponível: restante delimitado, durações observadas com sua fonte ou analogia
com partes comparáveis já executadas. Prefira faixa ou ordem de grandeza, rotulada como
estimativa, com premissas e principais fatores que podem alongá-la. Não exija histórico
estatístico para uma estimativa grosseira, mas identifique o que é julgamento e sua incerteza.
Sem base suficiente, como numa investigação de causa desconhecida, informe o que precisa
ser descoberto antes de estimar. Não rode comandos, delegue nem faça medições só para obter um número.

Considere dependências, provas e possíveis correções. Paralelismo só reduz a duração quando
for real e puder ser sustentado pelas evidências; considere o ramo mais lento e a integração.
Separe trabalho ativo de esperas externas. Sem prazo para uma aprovação ou resposta, declare
essa condição: estimar a parte executável não equivale a estimar o término do pedido inteiro.

Não converta contagem de tarefas heterogêneas em percentual do tempo nem invente probabilidades
de confiança. Uma contagem de critérios comprovados deve dizer o que conta, sem se passar por
percentual de conclusão do pedido. Não dê horário de término sem referência de relógio.
Se uma previsão anterior mudar, explique o fato que a alterou. Para outra conversa, vincule a
previsão ao momento e à fonte do registro observado, sem projetar atividade atual a partir de
dados antigos. Não crie acompanhamento periódico ou novos registros para manter a previsão.

Entregue o resumo na conversa, sem salvar um arquivo por padrão. Para comparar o trabalho
contra requisitos, use `reconciliar`; para preparar retomada
por outra sessão, use `passar-contexto`. Uma explicação que não ficou clara cabe a
`esclarecer`. Não inicie esses procedimentos apenas para responder ao andamento.
