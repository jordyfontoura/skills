---
name: reconcile
description: Compara requisitos, documentos e implementação para identificar o que existe, falta ou ficou obsoleto. Use em auditorias de estado ou pendências, em vez de revisão de um diff fixo.
license: Apache-2.0
---

# Conferir o estado do trabalho

Comece pela pergunta e pelo escopo: funcionalidade, pendências, versão ou projeto inteiro.
Leia instruções aplicáveis, decisões estabelecidas e última passagem de contexto. Identifique
requisitos, implementação, branches e evidências pelas ferramentas de leitura disponíveis.
Informe revisão, ambiente e fontes examinadas; não presuma que uma mudança local foi publicada.

## Comparar intenção e evidências

Use decisões explícitas para estabelecer o requisito atual. Uma mudança aprovada pode substituir
um plano anterior; a data mais recente de um arquivo não basta. Preserve contradições abertas
em vez de escolher a versão que faz o trabalho parecer concluído.

Identifique a fonte oficial de requisitos e estado e diferencie registro vigente de histórico.
Se status, checkboxes e evidências divergirem, relate a diferença e procure sua origem antes
de concluir que a entrega falhou. Associe provas aos critérios por suas referências; intervalos
ou resumos ambíguos precisam de conferência, especialmente após cópia ou migração.

Rastreie cada requisito relevante até a implementação e seus pontos de uso. Diferencie:

- Implementado e verificado por provas aplicáveis à revisão e ao ambiente examinados.
- Implementado ou parcialmente implementado, com prova ausente ou lacuna concreta.
- Ausente do escopo examinado.
- Substituído ou duplicado, com a decisão ou o substituto que demonstra isso.
- Desconhecido porque faltam fontes, acesso ou evidências de execução.

Trate estados de tarefas e relatos de conclusão como alegações a verificar. Nome de teste
ou suíte sem relação passando não provam o comportamento. Falta de acesso não prova ausência.
Para evidências de outra revisão, explique aplicabilidade e limites. Não conte cópias
importadas, forks ou tarefas duplicadas como entregas independentes.

## Relatar as diferenças úteis

Entregue um inventário conciso de requisitos, estado observado, referências e provas ausentes.
Priorize próximos passos por dependências e impacto reais. Identifique trabalho concluído
que não deve ser repetido e registros obsoletos que podem ser encerrados, com justificativa.

A auditoria é de leitura por padrão. Não edite documentos, cancele tarefas, integre branches
nem execute verificações que alterem estado apenas para conferir o trabalho. Se o usuário
autorizar atualizações, preserve decisões históricas e autoria, altere apenas os registros
combinados e verifique o resultado. Encaminhe um diff fixo a `review`, aceite em execução
a `evaluate` e falhas sem causa a `diagnose`. Reconciliação não comprova aceite independente.
