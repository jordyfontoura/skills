---
name: implement
description: Implementa o trabalho combinado em partes verificáveis e relata evidências, lacunas e próxima etapa.
license: Apache-2.0
---

# Implementar o trabalho combinado

Leia o pedido, o plano aplicável, os critérios de aceite, as decisões relevantes e a última
passagem de contexto. Retome a etapa exata. Não reinicie discussões de design resolvidas
nem assuma trabalho sob responsabilidade de outro colaborador.

Inspecione a branch e as alterações locais. Execute as verificações iniciais relevantes
e relate falhas preexistentes. Declare os arquivos ou módulos sob sua responsabilidade quando
o trabalho for compartilhado. Preserve edições alheias e faça mudanças sobrepostas em sequência.

Implemente e comprove uma parte útil por vez. Leia [testing.md](testing.md) ao adicionar testes.
Para interfaces, leia [interface.md](interface.md). Use `address-review` ao tratar feedback
recebido e `integrate` quando o pedido autorizar concluir uma integração entre branches.
Use `diagnose` após duas correções sem sucesso ou quando a causa não estiver clara.
Use `delegate` apenas para uma divisão autorizada; leia o apoio
`workloads.md` da skill `delegate` quando seleção de modelo, trabalho recorrente ou
registro de execução forem relevantes.

Exercite cada critério de aceite pelo método combinado. Relate comandos, observações e
resultados exatos. Scripts não executados, leitura de código e ferramentas indisponíveis
não são evidência de funcionamento. Não enfraqueça um teste nem mude um requisito só para passar.

Se uma descoberta exigir mudar requisito, tarefa ou método de prova, diferencie ajuste técnico
dentro do combinado de mudança de comportamento. Registre a versão substituída, o motivo e
a decisão que autoriza a nova versão no registro oficial, preservando autoria e referências.
Peça decisão apenas quando faltar autorização; substituir um critério não comprova seu aceite.
Identifique quais provas perderam validade e refaça as afetadas, incluindo suas dependências;
não descarte evidências ainda aplicáveis. Relacione resultados às referências dos critérios.

Execute as verificações relevantes antes de declarar a entrega. Faça commits pequenos quando
as convenções permitirem. Explique o comportamento alterado, a verificação e os limites restantes.
Implementação concluída não comprova aceite independente; use `evaluate` quando ele for exigido.
Preserve trabalho inacabado com `handoff`, indicando a próxima etapa e a ação exatas.
