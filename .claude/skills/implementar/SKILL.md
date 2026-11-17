---
name: implementar
description: Implementa o trabalho combinado em partes verificáveis e relata evidências, lacunas e próxima etapa.
license: Apache-2.0
---

# Implementar o trabalho combinado

Entregue o comportamento combinado e comprove-o pelos métodos combinados. Comece por uma
jornada que o usuário possa exercitar pela entrada normal, com integração real entre os
componentes próprios, e amplie a partir dela; numa entrega em fases, pela jornada
representativa do plano. A primeira jornada não conclui o produto: registre o que falta do escopo.

Uma pendência bloqueia só o trabalho que depende dela, salvo ordem ou portão explícito.
Dados de teste sintéticos dispensam aprovação humana, salvo quando ela for combinada.
Em trabalho compartilhado, declare os arquivos sob sua responsabilidade e preserve edições
alheias. Se o brief trouxer o resultado de base das verificações para a mesma revisão e o
mesmo ambiente, reaproveite-o e rode só as verificações focadas na sua mudança.

Leia [testing.md](testing.md) ao adicionar testes, ordenar verificações ou ler suas saídas.
Para interfaces, leia [interface.md](interface.md) e consulte os guias de
[usabilidade](../../../knowledge/ux/usability.md),
[hierarquia, estados e conteúdo](../../../knowledge/ux/states-and-content.md),
[acessibilidade](../../../knowledge/accessibility/interface-criteria.md) e
[plataforma](../../../knowledge/ux/platform-conventions.md) conforme a tarefa.

Um ajuste técnico dentro do combinado não reabre a especificação. Uma mudança de requisito,
tarefa ou método de prova entra no registro oficial com a versão substituída, o motivo e a
decisão que a autoriza, e invalida as provas que dependiam dela. Após duas correções sem
sucesso, ou quando variantes do mesmo defeito reaparecerem, use `diagnosticar`.

Encerre quando o comportamento combinado estiver comprovado e as verificações exigidas
passarem. Relate comandos e resultados exatos, ligados aos critérios, e os limites restantes;
script não executado e leitura de código não são evidência de funcionamento. Implementação
concluída não é aceite independente.
