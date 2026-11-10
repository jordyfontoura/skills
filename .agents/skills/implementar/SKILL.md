---
name: implementar
description: Implementa o trabalho combinado em partes verificáveis e relata evidências, lacunas e próxima etapa.
license: Apache-2.0
---

# Implementar o trabalho combinado

Leia o pedido, os critérios, as decisões relevantes e o plano e a passagem de contexto,
quando existirem. Em arquivos longos, localize por busca (`rg -n`) e leia o trecho; não releia
inteira uma saída já salva. Requisitos claros permitem começar sem spec, tarefas com IDs ou consulta
a um planejador. Use um plano curto na conversa quando ajudar; `especificar` resolve apenas
definições relevantes ausentes. Retome a etapa exata. Não reinicie discussões de design resolvidas
nem assuma trabalho sob responsabilidade de outro colaborador.

Inspecione a branch e as alterações locais. Execute as verificações iniciais relevantes
e relate falhas preexistentes. Se o brief trouxer o resultado de base para a mesma revisão e
o mesmo ambiente, reaproveite-o e rode só as verificações focadas na sua mudança. Declare os arquivos ou módulos sob sua responsabilidade quando
o trabalho for compartilhado. Preserve edições alheias e faça mudanças sobrepostas em sequência.

Implemente e comprove uma parte útil por vez, priorizando uma jornada que o usuário possa
exercitar pela entrada normal, com integração real entre os componentes próprios necessários.
Numa entrega em fases, comece pela jornada representativa do plano e amplie os casos específicos.
Use dados de teste adequados; aprovação humana da fixture só é obrigatória quando combinada.
Preserve o escopo completo e registre o que ainda falta, sem transformar a primeira jornada
em conclusão do produto. Uma pendência bloqueia somente o trabalho que depende dela, salvo
ordem ou portão explícito; avance trabalho independente autorizado sem antecipar aceite.
Leia [testing.md](testing.md) ao adicionar testes, ordenar verificações ou ler suas saídas.
Para interfaces, leia [interface.md](interface.md). Use `tratar-revisao` ao tratar feedback
recebido e `integrar` quando o pedido autorizar concluir uma integração entre branches.
Use `diagnosticar` após duas correções sem sucesso, quando a causa não estiver clara ou quando
variantes do mesmo defeito reaparecerem, mesmo com cada correção passando.
Use `delegar` apenas para uma divisão autorizada; leia o apoio
`workloads.md` da skill `delegar` quando seleção de modelo, trabalho recorrente ou
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

Agrupe correções relacionadas antes de revisar o conjunto integrado. Ajustes técnicos dentro
do combinado seguem para implementação e prova, sem nova especificação ou delegação por hábito.
Encerre a entrega quando o comportamento combinado estiver comprovado e as verificações
exigidas passarem. Melhorias opcionais ficam separadas; falhas de requisitos continuam abertas.
Relate mudanças de estado com resultado, evidência e próxima ação, sem repetir o histórico
nem criar trabalho documental apenas para ocupar a espera por agentes ou processos.

Execute as verificações relevantes, na ordem de [testing.md](testing.md), antes de declarar a entrega. Faça commits pequenos quando
as convenções permitirem. Explique o comportamento alterado, a verificação e os limites restantes.
Implementação concluída não comprova aceite independente; use `verificar-aceite` quando ele for exigido.
Preserve trabalho inacabado com `passar-contexto`, indicando a próxima etapa e a ação exatas.
