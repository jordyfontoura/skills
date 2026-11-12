# Uma skill para cada situação

Escolha pelo que você precisa resolver agora. Cada exemplo pode ser adaptado ao seu projeto;
não é preciso seguir uma sequência nem usar todas as skills.

Os exemplos usam `$nome`. Adapte o prefixo ao seu agente conforme o
[guia de chamadas](../README.md#como-chamar-as-skills). Os links nos títulos levam às instruções
completas de cada skill.

## Entender e decidir

### [`propor`](../skills/productivity/propor/SKILL.md)

Quando você quer avaliar o caminho antes de autorizar alterações. Ajuda a enxergar o escopo
e as consequências da proposta; o agente espera seu aceite antes de executar.

> $propor Quero exportar os relatórios em CSV. Mostre a abordagem antes de alterar arquivos.

### [`entrevistar`](../skills/productivity/entrevistar/SKILL.md)

Quando a ideia ainda tem escolhas abertas. As perguntas ajudam a definir o comportamento
esperado antes que o agente preencha as lacunas por conta própria.

> $entrevistar Quero lembretes de consulta. Me ajude a decidir canais, horários e regras de reenvio.

### [`entrevistar-por-arquivo`](../skills/productivity/entrevistar-por-arquivo/SKILL.md)

Quando você prefere responder com calma em um arquivo Markdown. Preserva perguntas, respostas
e decisões entre rodadas, sem precisar reconstruir tudo pela conversa.

> $entrevistar-por-arquivo Organize as escolhas pendentes dos lembretes em um arquivo Markdown para eu responder depois.

### [`esclarecer`](../skills/productivity/esclarecer/SKILL.md)

Quando a explicação ficou confusa. Retoma o contexto em português claro, sem avançar a tarefa
nem interpretar sua dúvida como aprovação.

> $esclarecer Não entendi por que precisamos de uma fila para enviar os lembretes. Explique usando esse exemplo.

### [`pesquisar-web`](../skills/productivity/pesquisar-web/SKILL.md)

Quando a decisão depende de informação externa. A pesquisa consulta fontes na internet
e distingue o que está documentado do que é hipótese ou recomendação.

> $pesquisar-web Pesquise opções de envio de e-mail transacional. Compare limites, custos e integração com fontes oficiais.

### [`conselho`](../skills/productivity/conselho/SKILL.md)

Quando uma escolha afeta várias áreas, como produto, arquitetura e privacidade. Pareceres em
contextos independentes ajudam a encontrar objeções e alternativas que uma única análise pode perder.

> $conselho Avalie nossa proposta de anexos pelas perspectivas de experiência de uso, arquitetura e privacidade. Preserve divergências.

### [`prototipar`](../skills/development/prototipar/SKILL.md)

Quando experimentar uma interação esclarece mais que descrevê-la. Uma prévia permite testar
a ideia e descobrir ajustes antes de construir a funcionalidade completa.

> $prototipar Crie uma prévia da tela de agendamento com dados simulados para avaliarmos o fluxo no celular.

### [`especificar`](../skills/development/especificar/SKILL.md)

Quando há uma definição relevante ausente ou você quer uma especificação. Explicita
comportamento, contratos e provas da próxima entrega, preservando a visão completa.
Requisitos já suficientes permitem implementar sem passar novamente por esta skill.

> $especificar Especifique a exportação CSV aprovada, incluindo filtros, campos, critérios de aceite e tarefas.

### [`escrever-objetivo`](../skills/productivity/escrever-objetivo/SKILL.md)

Quando você quer preparar uma execução autônoma com limites claros. Entrega uma instrução
pronta para colar, com referências e condição de conclusão; escrever o texto não inicia a execução.

> $escrever-objetivo Prepare um objetivo para concluir a exportação conforme a spec aprovada, com verificações e sem publicar nada.

## Entregar e conferir

### [`implementar`](../skills/development/implementar/SKILL.md)

Quando o trabalho já está combinado e pode ser executado, com ou sem spec em arquivo.
Prioriza uma jornada utilizável e verificável, com registro do que foi alterado, testado
e ainda falta provar. Um plano curto pode ficar na conversa.

> $implementar Adicione a exportação CSV dos resultados filtrados, com as colunas já exibidas na tabela, e confira o arquivo gerado. Não publique.

### [`diagnosticar`](../skills/development/diagnosticar/SKILL.md)

Quando há uma falha sem causa conhecida, principalmente após tentativas frustradas de correção.
Busca uma reprodução e evidências da causa para orientar o reparo.

> $diagnosticar O login falha depois que a sessão expira. Reproduza o problema e investigue a causa.

### [`revisar`](../skills/development/revisar/SKILL.md)

Quando você quer conferir um conjunto definido de alterações. A revisão relaciona possíveis
defeitos ao diff e aos requisitos, para você avaliar o que precisa ser corrigido.

> $revisar Revise o diff desta branch contra a main, considerando os requisitos da exportação CSV.

### [`tratar-revisao`](../skills/development/tratar-revisao/SKILL.md)

Quando já existem comentários de revisão para tratar. Confere cada achado antes de aplicar
correções e explica os itens corrigidos, rejeitados ou pendentes.

> $tratar-revisao Confira os comentários desta revisão e aplique as correções válidas dentro do escopo aprovado.

### [`examinar-arquitetura`](../skills/development/examinar-arquitetura/SKILL.md)

Quando o código está difícil de entender, modificar ou testar, mesmo sem um diff novo.
Localiza o atrito nos pontos de uso e propõe mudanças com motivos concretos, sem refatorar.

> $examinar-arquitetura Analise o acoplamento entre pedidos, pagamentos e notificações e proponha melhorias sustentadas pelo código.

### [`verificar-aceite`](../skills/development/verificar-aceite/SKILL.md)

Quando você precisa saber se a entrega atende aos critérios combinados. A avaliação exige
independência da implementação e provas por critério; conferir o próprio trabalho não basta.

> $verificar-aceite Verifique os critérios da exportação em um contexto independente. Relate o resultado e as provas, sem corrigir o código.

### [`criticar`](../skills/development/criticar/SKILL.md)

Quando você quer um crítico especializado no artefato e no foco do pedido. Os critérios vêm
da intenção, das referências e dos padrões pertinentes. A crítica não altera o produto.
Em UI e UX, usa a rubrica de interface, com severidade e base declaradas. Sempre entrega
nota geral e, quando pertinente, notas por categoria. As notas de qualidade têm duas casas
decimais, como `9.73` ou `7.00`, na escala padrão de 0 a 10, cujo máximo é `10.00`.

> $criticar Critique a tela de agendamento no celular para pacientes que marcam a primeira consulta. Use nosso design system.

Para um jogo, peça que o crítico jogue e indique os aspectos que precisa observar. Uma captura
não comprova cooperação ou resposta dos controles. Referências e âncoras orientam as notas.

> $criticar Use outro contexto para jogar esta build e avaliar cooperação, legibilidade e fidelidade a `definicoes/` e suas referências. Dê a nota geral e notas de game design e estética, com duas casas decimais e justificativas. Registre os passos, as evidências e os limites. Não edite o jogo.

Para várias perspectivas independentes, combine com `conselho`. Todos recebem a mesma versão
e os mesmos critérios; a consolidação preserva divergências e achados de um só avaliador.

> $criticar $conselho Avalie o cadastro antes do lançamento pelas perspectivas de usabilidade, acessibilidade e conteúdo.

O ciclo de correção exige autorização de implementação e uma condição de encerramento.
O crítico não escreve código; quem implementa confere os achados e repete as provas afetadas.

> $implementar Conclua o escopo aprovado. Ao terminar, chame um crítico independente com $criticar, corrija os problemas confirmados no escopo e peça nova crítica, até três rodadas. Encerre com todos os critérios comprovados e sem problemas impeditivos confirmados pelo crítico, ou com as pendências ao atingir o limite. Não mude os requisitos para obter aprovação.

### [`reconciliar`](../skills/development/reconciliar/SKILL.md)

Quando documentos, código e relatos parecem discordar sobre o que está pronto. Compara
requisitos e evidências para separar o que existe, o que falta e o que ficou obsoleto.

> $reconciliar Compare os requisitos da exportação, a implementação e as provas existentes. Liste as lacunas e os registros desatualizados.

### [`descrever-pr`](../skills/development/descrever-pr/SKILL.md)

Quando a mudança precisa de uma descrição que ajude quem vai revisá-la. Explica o problema,
o comportamento resultante e as verificações; esta skill cuida do texto do PR.

> $descrever-pr Escreva o título e a descrição do PR desta branch, incluindo comportamento, verificações e limitações.

### [`integrar`](../skills/development/integrar/SKILL.md)

Quando é hora de juntar o trabalho ao destino autorizado. Confere o estado das branches,
preserva alterações e verifica o resultado integrado, pois branches que passam isoladas podem conflitar.

> $integrar Integre a branch feat/export-csv na main local, preserve alterações alheias e verifique o resultado. Sem push.

## Acompanhar e dividir o trabalho

### [`andamento`](../skills/productivity/andamento/SKILL.md)

Quando você quer uma consulta rápida de andamento. Resume entregas, pendências e bloqueios,
preservando o objetivo e as autorizações do trabalho em curso.

> $andamento O que já foi feito, o que falta e tem algo dependendo de mim?

### [`examinar-eficiencia`](../skills/productivity/examinar-eficiencia/SKILL.md)

Quando o trabalho está demorando ou gastando muitos tokens. Aponta onde o gasto aconteceu, com
evidências, separa causa observada de inferida e propõe a menor mudança para cada uma, sem
cortar verificações úteis.

> $examinar-eficiencia Por que estamos demorando ou gastando tantos tokens para terminar as tarefas? Como podemos melhorar?

### [`passar-contexto`](../skills/productivity/passar-contexto/SKILL.md)

Quando outra sessão vai continuar o trabalho. Preserva a etapa exata, as decisões, as provas
pendentes e a próxima ação, para que a retomada não comece do zero.

> $passar-contexto Prepare a retomada da exportação com branch, arquivos alterados, verificações e próxima etapa.

### [`delegar`](../skills/productivity/delegar/SKILL.md)

Quando uma parte delimitada pode ficar com outro agente. Define responsabilidade, contexto
e resultado esperado, e exige conferir o retorno antes de incorporá-lo.

> $delegar Delegue a documentação da exportação a outro agente enquanto você implementa o código. Delimite os arquivos e confira a entrega.

## Escrever e cuidar das ferramentas

### [`escrever-claro`](../skills/productivity/escrever-claro/SKILL.md)

Quando um texto está genérico, repetitivo ou distante da sua voz. Revisa a linguagem para
deixar a informação clara, preservando fatos, comandos e o tom pretendido.

> $escrever-claro Revise este README para ficar mais direto e natural, preservando os fatos técnicos e os comandos.

### [`configurar-harness`](../skills/harness/configurar-harness/SKILL.md)

Quando o projeto precisa de comandos e orientações de verificação adequados à sua tecnologia.
Ajuda o agente a usar checks reais, em vez de seguir instruções de um template incompatível.

> $configurar-harness Configure os comandos e as orientações de verificação para este projeto, usando as ferramentas que ele já adota.

### [`melhorar-harness`](../skills/harness/melhorar-harness/SKILL.md)

Quando uma dificuldade da sessão revela algo a melhorar nas instruções. Propõe uma mudança
ligada ao problema observado e explica seu custo, sem transformar todo incidente em regra geral.

> $melhorar-harness Nesta sessão repetimos verificações que continuavam válidas. Proponha uma melhoria nas instruções a partir desse caso.

### [`atualizar-harness`](../skills/harness/atualizar-harness/SKILL.md)

Quando um projeto que copiou esta coleção precisa receber atualizações da origem. Compara
versões e preserva adaptações locais, identificando conflitos em vez de sobrescrevê-los.

> $atualizar-harness Atualize as skills copiadas neste projeto a partir de jordyfontoura/skills, preservando nossas adaptações.

### [`conhecer-ferramentas`](../skills/harness/conhecer-ferramentas/SKILL.md)

Quando você quer entender ou preparar as ferramentas de linha de comando do ambiente.
Explica sua utilidade e confere o que está disponível; instalações dependem de autorização.

> $conhecer-ferramentas Verifique se temos rg, fd e jq e explique para que cada um pode ajudar neste projeto. Faça só o inventário, sem instalar.

Para os procedimentos de manutenção e as regras completas do fluxo, consulte o
[HARNESS.md](HARNESS.md).
