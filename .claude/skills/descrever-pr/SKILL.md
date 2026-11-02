---
name: descrever-pr
description: Escreve ou atualiza a descrição de um PR com comportamento resultante, provas e riscos de integração quando ela é solicitada ou preparada.
license: Apache-2.0
---

# Escrever a descrição de um PR

Use `tratar-revisao` para feedback recebido e `integrar` para integração autorizada entre
branches ou merge de PR. Escrever a descrição continua sendo uma tarefa distinta dessas ações.

Escreva para quem não acompanhou a conversa. Siga o modelo de PR do repositório, quando houver.
Comece pelo problema concreto e pelo comportamento resultante; inclua um exemplo de antes
e depois quando ele ajudar. Aponte para os requisitos, o plano ou a decisão relevante.

Para mudanças simples, use uma descrição curta e as evidências. Para mudanças maiores,
separe comportamento, validação e risco apenas quando ajudar a leitura. Explique escolhas
importantes, efeitos de compatibilidade e o que uma reversão não restauraria. Identifique
os pontos de uso ou os dados afetados em vez de alegar baixo risco sem justificativa.

Inclua verificações exatas, resultados úteis observados, provas dos critérios e estado da
avaliação quando aplicável. Separe entrega da tarefa e aceite da especificação. Relate provas
ausentes e falhas; não declare que executou um comando apenas preparado. Use `revisar` para
a revisão de código exigida e `verificar-aceite` para aceite em execução quando necessário.

Use o glossário e `escrever-claro` para textos substanciais. Omita histórico da conversa e alternativas
descartadas, salvo quando explicarem o design final. Preparar uma descrição não autoriza
publicar, integrar nem enviar mensagens; siga a autorização existente para a ação solicitada.
