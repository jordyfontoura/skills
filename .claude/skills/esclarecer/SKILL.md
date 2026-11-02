---
name: esclarecer
description: Reformula a explicação anterior em português claro quando o usuário diz que não entendeu, pergunta como assim ou pede para retomar o raciocínio. Esclarece a conversa sem executar novas ações.
license: Apache-2.0
---

# Pera aí, explica de novo

Retome o ponto que não ficou claro. Leia a mensagem anterior e o contexto necessário para
entender a dúvida. Se ela aponta um trecho, concentre a resposta nele. Não repita a mesma
explicação apenas trocando palavras nem peça que o usuário explique tudo de novo.

Explique em português brasileiro, salvo pedido de outro idioma. Comece pelo que faltou para
entender o ponto, recuperando contexto apenas quando necessário. Use palavras familiares e,
quando ajudar, um exemplo do próprio projeto. Prefira frases curtas e uma ideia por frase.
Ajuste o detalhe à pergunta, sem
transformar uma dúvida pontual em uma aula sobre o sistema inteiro.

Escolha a forma da explicação pelo tipo de dúvida; combine formas quando necessário, sem
transformá-las em seções obrigatórias:

- **Termo ou conceito:** dê o significado no contexto e um exemplo concreto. Não recomece
  a história do projeto para explicar uma palavra.
- **Mecanismo ou fluxo:** mostre a ordem dos passos, quem age em cada um e o que entra e sai.
  Diferencie o comportamento previsto do que foi observado; explicar não autoriza executar.
- **Decisão ou consequência:** explicite o motivo, as alternativas relevantes e o que muda
  em cada uma, preservando escolhas já estabelecidas.
- **Status ou correção:** separe o que foi feito, proposto, verificado e ainda está pendente.
  Corrija uma explicação errada sem apresentar uma hipótese como causa comprovada.

Consulte o glossário do projeto, quando existir, como `docs/GLOSSARY.md`. Sem glossário,
prefira os termos definidos no contexto da área discutida. Mantenha o mesmo nome para o mesmo conceito; explique um termo
técnico na primeira vez em que ele for necessário. Preserve nomes de skills, comandos,
arquivos e APIs, explicando o significado ao lado em vez de inventar uma tradução executável.
Se não houver glossário, esclareça o termo na resposta sem depender de criar um arquivo.

Separe o que já aconteceu, o que é uma proposta e o que ainda falta confirmar. Se a explicação
anterior estava errada, corrija o erro de forma direta. Não simplifique removendo condições,
incertezas ou consequências que mudam o sentido. Uma analogia só ajuda se deixar seus limites
claros e não introduzir outra abstração difícil de entender.

Entregue a explicação reformulada. Quando houver uma escolha pendente, mostre concretamente
o que muda em cada caminho e retome somente essa escolha. Pergunte apenas se ainda faltar
uma informação que muda a resposta; não termine automaticamente com um teste de compreensão.

Esta skill esclarece o trabalho em andamento. Use ferramentas apenas para ler o contexto
necessário, quando o acesso estiver permitido. Não altere arquivos, delegue, avance de etapa
ou trate uma pergunta como nova aprovação. Preserve decisões já tomadas.
Se um termo recorrente merecer registro, proponha uma definição; só altere o glossário quando
essa manutenção estiver autorizada, sem transformar um significado local em regra universal.

Inspirada em [wait-what, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills%2Fproductivity%2Fwait-what%2FSKILL.md).
