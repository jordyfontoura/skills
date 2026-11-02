# Uma skill para cada situação

Escolha pelo que você precisa resolver agora. Cada exemplo pode ser adaptado ao seu projeto;
não é preciso seguir uma sequência nem usar todas as skills.

Os exemplos usam `$nome`. Adapte o prefixo ao seu agente conforme o
[guia de chamadas](../README.md#como-chamar-as-skills). Os links nos títulos levam às instruções
completas de cada skill.

## Entender e decidir

### [propose](../skills/productivity/propose/SKILL.md)

Quando você quer avaliar o caminho antes de autorizar alterações. Ajuda a enxergar o escopo
e as consequências da proposta; o agente espera seu aceite antes de executar.

> $propose Quero exportar os relatórios em CSV. Mostre a abordagem antes de alterar arquivos.

### [interview](../skills/productivity/interview/SKILL.md)

Quando a ideia ainda tem escolhas abertas. As perguntas ajudam a definir o comportamento
esperado antes que o agente preencha as lacunas por conta própria.

> $interview Quero lembretes de consulta. Me ajude a decidir canais, horários e regras de reenvio.

### [interview-async](../skills/productivity/interview-async/SKILL.md)

Quando você prefere responder com calma em um arquivo Markdown. Preserva perguntas, respostas
e decisões entre rodadas, sem precisar reconstruir tudo pela conversa.

> $interview-async Organize as escolhas pendentes dos lembretes em um arquivo Markdown para eu responder depois.

### [clarify](../skills/productivity/clarify/SKILL.md)

Quando a explicação ficou confusa. Retoma o contexto em português claro, sem avançar a tarefa
nem interpretar sua dúvida como aprovação.

> $clarify Não entendi por que precisamos de uma fila para enviar os lembretes. Explique usando esse exemplo.

### [research](../skills/productivity/research/SKILL.md)

Quando a decisão depende de informação externa. A pesquisa consulta fontes na internet
e distingue o que está documentado do que é hipótese ou recomendação.

> $research Pesquise opções de envio de e-mail transacional. Compare limites, custos e integração com fontes oficiais.

### [council](../skills/productivity/council/SKILL.md)

Quando uma escolha afeta várias áreas, como produto, arquitetura e privacidade. Pareceres em
contextos independentes ajudam a encontrar objeções e alternativas que uma única análise pode perder.

> $council Avalie nossa proposta de anexos pelas perspectivas de experiência de uso, arquitetura e privacidade. Preserve divergências.

### [prototype](../skills/development/prototype/SKILL.md)

Quando experimentar uma interação esclarece mais que descrevê-la. Uma prévia permite testar
a ideia e descobrir ajustes antes de construir a funcionalidade completa.

> $prototype Crie uma prévia da tela de agendamento com dados simulados para avaliarmos o fluxo no celular.

### [specify](../skills/development/specify/SKILL.md)

Quando o trabalho precisa de uma definição verificável. Converte o comportamento esperado
em critérios, tarefas e dependências, para que implementação e aceite tenham a mesma referência.

> $specify Especifique a exportação CSV aprovada, incluindo filtros, campos, critérios de aceite e tarefas.

### [write-goal](../skills/productivity/write-goal/SKILL.md)

Quando você quer preparar uma execução autônoma com limites claros. Entrega uma instrução
pronta para colar, com referências e condição de conclusão; escrever o texto não inicia a execução.

> $write-goal Prepare um objetivo para concluir a exportação conforme a spec aprovada, com verificações e sem publicar nada.

## Entregar e conferir

### [implement](../skills/development/implement/SKILL.md)

Quando o trabalho já está combinado e pode ser executado. Orienta a entrega em partes
verificáveis, com registro do que foi alterado, testado e ainda falta provar.

> $implement Implemente a exportação CSV conforme a spec aprovada e registre as verificações realizadas.

### [diagnose](../skills/development/diagnose/SKILL.md)

Quando há uma falha sem causa conhecida, principalmente após tentativas frustradas de correção.
Busca uma reprodução e evidências da causa para orientar o reparo.

> $diagnose O login falha depois que a sessão expira. Reproduza o problema e investigue a causa.

### [review](../skills/development/review/SKILL.md)

Quando você quer conferir um conjunto definido de alterações. A revisão relaciona possíveis
defeitos ao diff e aos requisitos, para você avaliar o que precisa ser corrigido.

> $review Revise o diff desta branch contra a main, considerando os requisitos da exportação CSV.

### [address-review](../skills/development/address-review/SKILL.md)

Quando já existem comentários de revisão para tratar. Confere cada achado antes de aplicar
correções e explica os itens corrigidos, rejeitados ou pendentes.

> $address-review Confira os comentários desta revisão e aplique as correções válidas dentro do escopo aprovado.

### [architecture-review](../skills/development/architecture-review/SKILL.md)

Quando o código está difícil de entender, modificar ou testar, mesmo sem um diff novo.
Localiza o atrito nos pontos de uso e propõe mudanças com motivos concretos, sem refatorar.

> $architecture-review Analise o acoplamento entre pedidos, pagamentos e notificações e proponha melhorias sustentadas pelo código.

### [evaluate](../skills/development/evaluate/SKILL.md)

Quando você precisa saber se a entrega atende aos critérios combinados. A avaliação exige
independência da implementação e provas por critério; conferir o próprio trabalho não basta.

> $evaluate Verifique os critérios da exportação em um contexto independente. Relate o resultado e as provas, sem corrigir o código.

### [reconcile](../skills/development/reconcile/SKILL.md)

Quando documentos, código e relatos parecem discordar sobre o que está pronto. Compara
requisitos e evidências para separar o que existe, o que falta e o que ficou obsoleto.

> $reconcile Compare os requisitos da exportação, a implementação e as provas existentes. Liste as lacunas e os registros desatualizados.

### [pull-request](../skills/development/pull-request/SKILL.md)

Quando a mudança precisa de uma descrição que ajude quem vai revisá-la. Explica o problema,
o comportamento resultante e as verificações; esta skill cuida do texto do PR.

> $pull-request Escreva o título e a descrição do PR desta branch, incluindo comportamento, verificações e limitações.

### [integrate](../skills/development/integrate/SKILL.md)

Quando é hora de juntar o trabalho ao destino autorizado. Confere o estado das branches,
preserva alterações e verifica o resultado integrado, pois branches que passam isoladas podem conflitar.

> $integrate Integre a branch feat/export-csv na main local, preserve alterações alheias e verifique o resultado. Sem push.

## Acompanhar e dividir o trabalho

### [progress](../skills/productivity/progress/SKILL.md)

Quando você quer uma consulta rápida de andamento. Resume entregas, pendências e bloqueios,
preservando o objetivo e as autorizações do trabalho em curso.

> $progress O que já foi feito, o que falta e tem algo dependendo de mim?

### [handoff](../skills/productivity/handoff/SKILL.md)

Quando outra sessão vai continuar o trabalho. Preserva a etapa exata, as decisões, as provas
pendentes e a próxima ação, para que a retomada não comece do zero.

> $handoff Prepare a retomada da exportação com branch, arquivos alterados, verificações e próxima etapa.

### [delegate](../skills/productivity/delegate/SKILL.md)

Quando uma parte delimitada pode ficar com outro agente. Define responsabilidade, contexto
e resultado esperado, e exige conferir o retorno antes de incorporá-lo.

> $delegate Delegue a documentação da exportação a outro agente enquanto você implementa o código. Delimite os arquivos e confira a entrega.

## Escrever e cuidar das ferramentas

### [unslop](../skills/productivity/unslop/SKILL.md)

Quando um texto está genérico, repetitivo ou distante da sua voz. Revisa a linguagem para
deixar a informação clara, preservando fatos, comandos e o tom pretendido.

> $unslop Revise este README para ficar mais direto e natural, preservando os fatos técnicos e os comandos.

### [setup-harness](../skills/harness/setup-harness/SKILL.md)

Quando o projeto precisa de comandos e orientações de verificação adequados à sua tecnologia.
Ajuda o agente a usar checks reais, em vez de seguir instruções de um template incompatível.

> $setup-harness Configure os comandos e as orientações de verificação para este projeto, usando as ferramentas que ele já adota.

### [improve-harness](../skills/harness/improve-harness/SKILL.md)

Quando uma dificuldade da sessão revela algo a melhorar nas instruções. Propõe uma mudança
ligada ao problema observado e explica seu custo, sem transformar todo incidente em regra geral.

> $improve-harness Nesta sessão repetimos verificações que continuavam válidas. Proponha uma melhoria nas instruções a partir desse caso.

### [update-harness](../skills/harness/update-harness/SKILL.md)

Quando um projeto que copiou esta coleção precisa receber atualizações da origem. Compara
versões e preserva adaptações locais, identificando conflitos em vez de sobrescrevê-los.

> $update-harness Atualize as skills copiadas neste projeto a partir de jordyfontoura/skills, preservando nossas adaptações.

### [toolbox](../skills/harness/toolbox/SKILL.md)

Quando você quer entender ou preparar as ferramentas de linha de comando do ambiente.
Explica sua utilidade e confere o que está disponível; instalações dependem de autorização.

> $toolbox Verifique se temos rg, fd e jq e explique para que cada um pode ajudar neste projeto. Faça só o inventário, sem instalar.

Para os procedimentos de manutenção e as regras completas do fluxo, consulte o
[HARNESS.md](HARNESS.md).
