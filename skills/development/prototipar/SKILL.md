---
name: prototipar
description: Cria um experimento para esclarecer uma interação ou escolha de design quando o usuário pede uma prévia ou ainda não há definição suficiente do comportamento.
license: Apache-2.0
---

# Prototipar uma questão

Identifique a pergunta que o experimento precisa responder. Deduza-a do pedido quando estiver
clara; pergunte apenas se a ambiguidade mudar o experimento. Reutilize a linguagem visual
e as interfaces do projeto quando útil. Escolha o meio mais simples que demonstre a dúvida:
página independente, script pequeno ou simulação isolada.
Para direção visual, estados e acessibilidade de interfaces, leia o apoio
`interface.md` da skill `implementar`, respeitando as simulações próprias do protótipo.

Mantenha o protótipo separado do código de produção, em local permitido para experimentos
ou artefatos. Dê uma forma clara de executar ou visualizar. Acrescente apenas os mecanismos
necessários à pergunta; identifique dados inventados e persistência simulada. Não transforme
exploração numa implementação de produção.

Mostre o comportamento e itere a partir da reação do usuário. Declare o que foi realmente
aberto, acionado ou inspecionado e o que continua hipotético. Aprovações existentes continuam
válidas entre revisões; pergunte de novo apenas se uma mudança de direção exigir uma decisão.

Preserve uma versão aprovada antes de experimentar mais, usando um artefato versionado ou
um commit permitido pelas convenções. Identifique arquivo, revisão e escopo da aprovação.
Separe experimentos não aprovados para que uma iteração não substitua a referência combinada.

Registre os comportamentos que precisam sobreviver à implementação, incluindo navegação,
estados, interações, responsividade e movimento relevantes. Separe simulações deliberadas do
comportamento aceito. Uma interação de arrastar aprovada inclui como posicionar e cancelar,
não só a aparência da tela final. Registre ação e resultado esperados como exemplos de aceite
e compare o fluxo de produção com essa referência antes de declarar fidelidade.

Quando a direção estiver definida, preserve o artefato útil e registre o resultado na conversa
ou na documentação existente. Use `especificar` se ainda faltar uma definição relevante de
comportamento, contrato ou prova. Com definições suficientes, a implementação autorizada
pode continuar com um plano curto, sem nova etapa de especificação.
Converta o comportamento aprovado em critérios com `visual`, `run` ou outro método adequado;
um protótipo não comprova o critério de produção. Liste suas simulações e seus limites.

Inspirada em [prototype, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md).
