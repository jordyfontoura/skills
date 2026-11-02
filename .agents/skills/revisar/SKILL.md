---
name: revisar
description: Analisa um diff fixo contra requisitos e padrões em revisões de código ou PRs não triviais. Respeita restrições de execução e relata requisitos ausentes sem impedir a análise disponível.
license: Apache-2.0
---

# Revisar alterações específicas

Use `tratar-revisao` para tratar comentários já recebidos e `examinar-arquitetura` para examinar
atrito estrutural do código existente sem depender de um diff. Este procedimento produz achados
sobre alterações específicas; não aplica correções por conta própria.

Fixe as revisões de base e de destino antes de ler. Diferencie mudanças commitadas de alterações
locais incluídas no pedido; um diff vazio entre commits não pode esconder edições não commitadas.
Use ferramentas de diff e histórico somente quando permitidas. Se o pedido proibir execução,
leia diretamente o diff e os arquivos fornecidos, sem invocar comandos de terminal.

Leia os requisitos e registros aplicáveis, os padrões do projeto, a arquitetura relevante e
as decisões existentes. Consulte requisitos apenas por meios permitidos. Se faltar acesso
ou documentação, declare o limite da comparação e continue a revisão dos padrões e do código.
Não inicie uma entrevista apenas para revisar material fornecido.

Avalie se as alterações atendem aos requisitos e se introduzem problemas de funcionamento
ou violam um padrão documentado. Rastreie o comportamento até seus pontos de uso.
Cite arquivo e linha, requisito ou regra, impacto concreto e correção sugerida.
Separe defeito demonstrado de incerteza. Evite refatorações especulativas e problemas
já cobertos por verificações configuradas.

Uma revisão relata o que o código sustenta; leitura não comprova funcionamento em execução.
Não espere pelo código de outro agente, aplique correções, execute testes, delegue nem atualize
registros, salvo autorização explícita para esse trabalho adicional. Um relatório de leitura
não exige a campanha de testes da implementação. Use `verificar-aceite` separadamente para aceite.

Retorne os achados por impacto, as revisões examinadas e os trechos ou provas não avaliados.
Se não houver achado relevante, diga isso junto dos limites da revisão.
