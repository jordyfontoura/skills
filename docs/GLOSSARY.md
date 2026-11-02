# Glossário

Este arquivo define os termos usados neste harness. Nas explicações, use português brasileiro
e mantenha os nomes de skills, comandos e arquivos como aparecem no projeto. Os termos em
inglês abaixo ajudam a reconhecer esses mesmos conceitos no código e nas ferramentas.

- **Harness**: conjunto de instruções, skills, papéis e orientações de verificação que guia
  o trabalho do agente.
- **Skill**: procedimento reutilizável para uma situação definida, com um resultado esperado.
- **Papel (role)**: responsabilidade específica de um agente, como planejar ou avaliar uma entrega.
- **Especificação (spec)**: descrição do objetivo, escopo, comportamentos e contratos esperados,
  com critérios observáveis. Descrever um comportamento não comprova que ele foi implementado.
- **Plano de entrega (plan)**: abordagem técnica, tarefas, dependências e provas para realizar
  uma mudança. Pode compartilhar um documento com a spec, mas tem finalidade diferente.
- **Fonte oficial**: registro que o projeto adota para consultar requisitos, decisões ou estado
  efetivo. Uma cópia histórica não se torna vigente só por ter sido editada mais recentemente.
- **Tarefa (task)**: parte delimitada do trabalho, com um resultado observável e um responsável
  quando necessário.
- **Critério de aceite (criterion)**: condição que precisa ser demonstrada para considerar uma
  entrega concluída. A prova pode ser um teste, execução, inspeção visual, medição ou avaliação humana.
- **Dependência (dependency)**: trabalho que precisa terminar antes de outro poder avançar.
- **Ordem de execução (order)**: prioridade entre tarefas que já podem começar; não elimina dependências.
- **Evidência (evidence)**: resultado observado de um comando, interação, medição ou avaliação humana.
  Um teste preparado, mas não executado, ainda não é evidência de funcionamento.
- **Revisão (review)**: análise de alterações específicas em relação aos requisitos e padrões.
  Ler o código não demonstra, por si só, que o programa funciona.
- **Avaliação (evaluation)**: verificação independente dos critérios de aceite pelos métodos combinados.
- **Passagem de contexto (handoff)**: registro suficiente para outra sessão retomar o trabalho
  na etapa correta, com o próximo passo e as provas que faltam.
- **Decisão (decision)**: escolha já estabelecida, com seu motivo e suas consequências.
- **Alinhamento assíncrono**: conversa em que o agente prepara perguntas em arquivo, as pessoas
  respondem quando puderem e o agente processa as respostas em outra rodada.
- **Rodada**: conjunto de perguntas que já podem ser respondidas com as decisões e os fatos
  disponíveis. Respostas novas podem liberar perguntas para a rodada seguinte.
- **Bloqueador do alinhamento**: escolha ou evidência importante que falta para alcançar o
  objetivo da conversa. Não é qualquer detalhe que ainda poderia ser discutido.
- **Alinhamento suficiente**: estado em que os pontos importantes para o objetivo foram
  resolvidos e as pendências têm encaminhamento explícito. Não equivale a aprovar implementação.
- **Reconciliação (reconcile)**: comparação entre requisitos, documentos, implementação e evidências
  para distinguir o que está pronto, parcial, ausente, desatualizado ou ainda desconhecido.
- **Conselho (council)**: consulta a especialistas independentes para reunir recomendações,
  divergências e lacunas. Seu poder de aprovação depende das regras explícitas do projeto.
- **Protótipo (prototype)**: experimento para esclarecer uma ideia ou comportamento. Pode usar
  dados fictícios e não comprova que a versão de produção já funciona.
- **Base de referência (baseline)**: versão identificada usada para comparar resultados, como
  um protótipo aprovado ou uma medição anterior.
- **Ambiente (environment)**: contexto em que o programa roda, como a máquina local ou produção.
  Um resultado local não comprova automaticamente o mesmo comportamento em produção.
- **Diff**: conjunto de diferenças entre versões de arquivos.
- **Commit**: registro de uma versão no Git. Não significa que ela foi publicada ou colocada em produção.
- **Branch**: linha de trabalho no Git em que alterações podem ser preparadas antes da integração.
- **Worktree**: diretório de trabalho adicional do mesmo repositório Git, usado para manter
  alterações separadas em outra branch.
- **Objetivo de execução (goal)**: instrução com resultado esperado, escopo e condição de
  conclusão, preparada por `escrever-objetivo` para orientar uma execução autônoma.
- **Provedor (provider)**: ferramenta ou serviço que disponibiliza o modelo e os recursos
  de execução do agente.
- **Veredito**: resultado de uma avaliação. `PASS` significa aprovado; `FAIL`, reprovado;
  `UNPROVED`, sem prova suficiente. O token é preservado e a justificativa fica em português.

Se uma área do projeto usar um termo com significado próprio, registre esse contexto na
definição. Não misture sentidos diferentes nem substitua uma escolha aprovada por uma preferência
de tradução. Acrescente termos conforme forem úteis às conversas, sem tentar catalogar todo o setor.

