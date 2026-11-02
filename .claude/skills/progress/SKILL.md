---
name: progress
description: Resume o andamento do trabalho, o que falta e os bloqueios sem mudar seu objetivo. Use para consultas rápidas durante a execução; reconcile audita requisitos e handoff prepara retomada por outra sessão.
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
- **Restante:** trabalho pendente na ordem das dependências, incluindo provas ausentes.
- **Impedimentos:** falha ou dependência observada, consequência e condição para destravar.
  Diferencie bloqueio de risco ou dúvida; sem impedimento observado, diga “nenhum bloqueio conhecido”.
- **Próxima ação:** passo concreto que será retomado ou condição que continua aguardando.

Separe o que foi verificado, relatado anteriormente, inferido da atividade e o que é desconhecido.
Algo implementado sem validação deve aparecer com essa ressalva. Uma prova anterior precisa
continuar aplicável à revisão e ao ambiente atuais; edições posteriores podem exigir nova prova.
Não invente percentuais, prazos ou ausência de bloqueios. Uma foto parcial de arquivos em edição
não comprova conclusão nem falha da entrega.

Entregue o resumo na conversa, sem salvar um arquivo por padrão. Para comparar o trabalho
contra requisitos, use `reconcile`; para preparar retomada
por outra sessão, use `handoff`. Uma explicação que não ficou clara cabe a
`clarify`. Não inicie esses procedimentos apenas para responder ao andamento.
