---
name: esclarecer
description: Reexplica a mensagem anterior pelo padrão de explicação clara quando o usuário diz que não entendeu, pergunta como assim ou pede para retomar o raciocínio. Esclarece a conversa sem executar novas ações.
license: Apache-2.0
---

# Pera aí, explica de novo

Retome o ponto que não ficou claro. Leia a mensagem anterior e o contexto necessário para
entender a dúvida. Se ela aponta um trecho, concentre a resposta nele. Não peça que o
usuário explique tudo de novo.

Reexplique seguindo o [padrão de explicação clara](../../../knowledge/writing/clear-explanation.md).
Responda em português brasileiro, salvo pedido de outro idioma. Comece pelo que faltou para
entender o ponto. Mude a forma da explicação, com outro exemplo, outra ordem ou outro tipo
de explicação; repetir a anterior trocando palavras não esclarece.

Consulte o glossário do projeto, quando existir, como `docs/GLOSSARY.md`. Sem glossário,
esclareça o termo na resposta, sem depender de criar um arquivo. Se um termo recorrente
merecer registro, proponha uma definição; só altere o glossário quando essa manutenção
estiver autorizada.

Quando houver uma escolha pendente, mostre concretamente o que muda em cada caminho e
retome somente essa escolha. Pergunte apenas se ainda faltar uma informação que muda a
resposta; não termine automaticamente com um teste de compreensão.

Esta skill esclarece o trabalho em andamento. Use ferramentas apenas para ler o contexto
necessário, quando o acesso estiver permitido. Não altere arquivos, delegue, avance de etapa
ou trate uma pergunta como nova aprovação. Preserve decisões já tomadas.

Inspirada em [wait-what, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills%2Fproductivity%2Fwait-what%2FSKILL.md).
