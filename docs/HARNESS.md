# Usar o harness

O harness é um conjunto de arquivos que o agente pode ler e aplicar. Use a conversa para
trabalho curto. Para trabalho longo, mantenha uma especificação ou passagem de contexto
concisa na documentação do projeto, quando útil. Aponte para registros existentes em vez
de duplicá-los.

## Fluxo de trabalho

Quando quiser revisar a abordagem antes de qualquer alteração, use `propor`. O agente pode
investigar por leitura, mas deve entregar uma proposta concreta na resposta final e aguardar
sua aprovação. Um "pode fazer" posterior libera a execução daquela proposta, sem repetir
a mesma aprovação. Esse modo não é imposto aos demais pedidos.

Leia o pedido e as instruções relevantes. Resolva dúvidas importantes de escopo com
`entrevistar`. Use `especificar` para definir comportamentos e planejar sua entrega; use `implementar`
para entregar partes verificáveis. Use `revisar` para analisar alterações de código e `verificar-aceite` para aceite
independente quando solicitado. Termine com evidências e use `passar-contexto` se outra sessão continuar.

Use `reconciliar` para comparar o trabalho pretendido com implementação e evidências atuais.
Use `conselho` para pareceres independentes sobre uma proposta; siga a governança existente
sem exigir comitê para toda mudança. Aplique `escrever-claro` ao redigir textos para leitores,
incluindo títulos e descrições.

Autorizações anteriores continuam válidas. Explorar não autoriza implementar. Um pedido claro
de implementação não exige nova aprovação para passos rotineiros dentro do escopo.
Relate ferramentas, permissões e evidências ausentes como ausentes.

## Catálogo de skills

Os comandos, os títulos e as instruções ficam em português.
Consulte os [padrões de nomes e idioma](STANDARDS.md) para detalhes.

Para escolher por situação, veja o [guia com exemplos de todas as skills](EXAMPLES.md).

### Desenvolvimento e especificação

Fontes em `skills/development/`.

| Skill | Resultado |
| --- | --- |
| `especificar` | Especificar comportamentos e contratos e planejar sua entrega verificável. |
| `implementar` | Entregar e verificar o trabalho combinado. |
| `diagnosticar` | Reproduzir uma falha e demonstrar sua causa. |
| `revisar` | Avaliar um diff fixo contra requisitos e padrões. |
| `tratar-revisao` | Verificar feedback recebido e aplicar correções autorizadas com evidências. |
| `examinar-arquitetura` | Identificar atrito estrutural em código existente e propor mudanças sustentadas. |
| `verificar-aceite` | Verificar critérios de aceite de forma independente. |
| `prototipar` | Esclarecer uma questão de design com um experimento. |
| `descrever-pr` | Explicar comportamento resultante, provas e riscos de integração. |
| `integrar` | Integrar branches ou concluir merge de PR no destino autorizado e verificar o resultado. |
| `reconciliar` | Comparar requisitos, documentos e implementação para identificar lacunas e trabalho obsoleto. |
| `criticar-interface` | Criticar UI e UX com rubrica fixa, severidade, base e limites declarados. |
| `criticar-interface-em-conselho` | Consolidar críticas independentes de UI e UX, com severidades e divergências. |

`revisar` produz achados; `tratar-revisao` trata feedback existente. `examinar-arquitetura`
examina dificuldades de arquitetura mesmo sem diff. `descrever-pr` escreve a descrição;
`integrar` executa a integração solicitada sem presumir publicação. O apoio de
[direção visual](../skills/development/implementar/interface.md) é compartilhado por `implementar`
e `prototipar`, preservando a identidade e os componentes do projeto.
`criticar-interface` avalia a experiência de uso de uma interface, com ou sem diff, usando a
[rubrica comum](../skills/development/criticar-interface/rubric.md), o design system do projeto e as
diretrizes vigentes da plataforma. `criticar-interface-em-conselho` aplica a mesma rubrica com
avaliadores independentes e segue `conselho` para independência e consolidação.

### Produtividade

Fontes em `skills/productivity/`.

| Skill | Resultado |
| --- | --- |
| `esclarecer` | Reformular um ponto confuso em português claro, usando o glossário do projeto. |
| `conselho` | Consolidar pareceres independentes, divergências e recomendações. |
| `delegar` | Delegar trabalho delimitado e conferir o resultado. |
| `passar-contexto` | Preservar próxima etapa, evidências e trabalho restante. |
| `entrevistar` | Resolver escolhas abertas de escopo e design pela conversa. |
| `entrevistar-por-arquivo` | Conduzir perguntas em arquivo e consolidar decisões em rodadas assíncronas. |
| `propor` | Explicar a abordagem e aguardar aprovação antes de executar. |
| `andamento` | Consultar andamento, pendências e bloqueios preservando o objetivo e as autorizações. |
| `pesquisar-web` | Pesquisar na internet e fundamentar conclusões com fontes, evidências e limites. |
| `escrever-claro` | Escrever ou revisar textos claros, preservando fatos e voz. |
| `escrever-objetivo` | Escrever uma instrução de execução delimitada com conclusão verificável. |

### Manutenção do harness

Fontes em `skills/harness/`.

| Skill | Resultado |
| --- | --- |
| `configurar-harness` | Configurar verificações adequadas às tecnologias do projeto. |
| `melhorar-harness` | Melhorar o harness a partir de dificuldades observadas na sessão. |
| `atualizar-harness` | Trazer atualizações da origem preservando adaptações locais. |
| `conhecer-ferramentas` | Explicar ferramentas CLI, inventariar o ambiente e preparar faltantes no escopo autorizado. |

Use `$esclarecer` ou pergunte "Como assim?" para retomar uma explicação.
A skill recupera o contexto e usa o [glossário](GLOSSARY.md), preservando nomes de comandos
e skills. Ela não avança a tarefa nem trata uma dúvida como aprovação.

Para consultar o andamento, use, por exemplo:

> `$andamento Como está? O que já fez, o que falta e tem algo dependendo de mim?`

O agente responde com o estado conhecido, as provas disponíveis, os impedimentos e a próxima
ação. Depois, continua a etapa que já estava em execução e autorizada. Se estava aguardando
uma decisão, continua aguardando: uma pergunta de andamento não conta como aprovação.
`andamento` faz uma consulta curta; `reconciliar` audita o trabalho contra requisitos e `passar-contexto`
prepara o contexto para outra sessão retomar.

Na mesma conversa, o momento e o efeito da entrega da pergunta dependem do ambiente: a skill
não controla filas ou interrupções. Para observar outra execução sem lhe enviar mensagens,
use uma conversa separada com ferramentas de leitura, quando disponíveis. Algumas marcam o
resultado final de um agente filho como entregue ao lê-lo, como `t3_thread_read` no T3 Code;
não consuma resultados de outra coordenação para obter um resumo.
A observação externa reflete os registros disponíveis, com sua fonte e momento, e pode estar
desatualizada. O comportamento da interface ao enviar uma pergunta durante a execução ainda
precisa ser verificado; a existência de uma ferramenta de leitura não prova ausência de efeitos.

Para pedir uma proposta, por exemplo:

> `$propor Quero agrupar as skills por finalidade. Mostre a estrutura e os grupos antes de alterar.`

Nesse caso, a resposta apresenta a organização sugerida e suas consequências; o agente não
move arquivos, cria branches ou começa a solução enquanto aguarda. Para pedidos simples,
não é necessário produzir o plano detalhado de `especificar`.

## Pesquisa na internet

Para ferramentas CLI, use `conhecer-ferramentas` e o [guia de ferramentas](TOOLS.md). Uma pergunta explicativa
ou um inventário não autoriza instalação. Quando a preparação já estiver explicitamente
autorizada, a skill executa o lote pertinente sem pedir a mesma aprovação novamente.

`esclarecer`, `pesquisar-web` e `conselho` adaptam suas orientações à situação dentro do próprio `SKILL.md`:
tipo de dúvida, tipo de evidência necessária e tipo de decisão, respectivamente. Essas divisões
ajudam a escolher a abordagem; não são etapas ou seções obrigatórias em toda resposta.

As adaptações usam como referências a [orientação de escrita acessível do W3C](https://www.w3.org/WAI/tips/writing/),
os [métodos de busca da Cochrane](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04)
e o [estudo de conformidade em agentes de Choi et al.](https://arxiv.org/abs/2506.01332).
O W3C trata de conteúdo web; a Cochrane, de revisões de intervenções; o estudo, de debates
simulados sobre temas controversos. A aplicação ao harness é uma escolha de projeto, sem
prova de ganho neste ambiente. Esses contextos não impõem requisitos a toda conversa ou busca.

Use `pesquisar-web` quando quiser uma resposta fundamentada em fontes externas consultadas:

> `$pesquisar-web Pesquise como melhorar a skill escrever-claro e quais critérios usar para diferentes tipos de conteúdo.`

A skill exige busca online e leitura das fontes relevantes, com links próximos das conclusões.
Se faltar acesso à internet, o agente declara a pesquisa ausente ou parcial em vez de responder
de memória como se tivesse pesquisado. Guias e opiniões são distinguidos de resultados medidos.
A pesquisa não amplia a autorização para editar arquivos ou implementar suas recomendações.
`escrever-claro` continua podendo revisar textos sem pesquisa externa quando isso for suficiente ao pedido.

## Consultas ao conselho

O `conselho` prioriza profundidade, cobertura e independência dos pareceres. Sua composição e
investigação seguem a decisão e seus riscos. O coordenador organiza opções, critérios,
restrições, revisão e evidências com suas origens. Os especialistas recebem esse objeto comum
e perguntas claras, sem conhecer o parecer um do outro antes da primeira análise. Cada um
investiga as fontes por conta própria e confere as premissas que sustentam seu parecer.

Por exemplo, para melhorar `especificar`, a pergunta de produto pode ser "A intenção humana é
preservada quando o requisito muda?" e a de engenharia, "Cada requisito chega a uma prova
sem duplicar registros?". Essas perguntas orientam o foco; os especialistas podem reler o
catálogo, ampliar a busca e examinar riscos além do resumo recebido, dentro da autorização.
Um parecer individual pedido pelo usuário é identificado como tal, com seus limites de cobertura.

O retorno inclui achados relevantes, benefícios, riscos, incertezas e recomendações com suas
evidências. Não se limita a poucos achados para encurtar o relatório. Novas rodadas aprofundam
evidências, divergências ou consequências não resolvidas. Uma mudança exige examinar efeitos
no conjunto da proposta, ampliando a reavaliação quando necessário e preservando provas válidas.
Modelo e esforço seguem a política local e o pedido.

Ao conferir o procedimento, use estes cenários:

| Entrada | Comportamento esperado |
| --- | --- |
| Decisão com riscos de produto e engenharia. | Escolher perspectivas pela cobertura necessária, sem reduzir a composição para economizar consultas. |
| Usuário pede um parecer individual. | Respeitar a quantidade e declarar seus limites, sem inventar consenso ou cobertura multidisciplinar. |
| Conflito entre produto e engenharia sobre uma proposta. | Perguntas distintas sobre o mesmo objeto e critérios; preservar divergência, sem decidir por maioria. |
| Correção de uma frase de permissão após um parecer. | Examinar seus efeitos no conjunto, ampliar a reavaliação se necessário e manter provas ainda válidas. |
| Resumo do coordenador omite uma exceção relevante na fonte. | Investigar a origem e contestar a premissa; sem acesso, a conclusão dependente fica sem prova. |
| Um sinal de risco ainda tem pouca evidência. | Registrá-lo como incerteza e indicar investigação pertinente, sem descartá-lo para reduzir a lista de achados. |

Para avaliar qualidade, compare tarefas e critérios equivalentes, registrando cobertura,
achados relevantes preservados ou perdidos, evidências e incertezas. Observe e informe tempo,
retrabalho e uso quando expostos, respeitando limites explícitos do usuário. Reduzir custo
não é um objetivo do conselho nem um critério para limitar especialistas, investigação ou rodadas.
Contagem de consultas ou palavras não mede tokens faturados nem cota da assinatura.
Verificações estruturais e leitura dos cenários não comprovam a qualidade real dos pareceres;
isso exige execuções comparáveis autorizadas, conforme
[as orientações de comparação](../skills/productivity/delegar/workloads.md).

## Alinhamento assíncrono

Use `$entrevistar-por-arquivo` com um pedido como: "Quero alinhar esta ideia respondendo em um arquivo.
Prepare as perguntas e processe minhas respostas quando eu avisar." O agente investiga os
fatos disponíveis, prepara uma rodada em português e indica onde responder. Você salva suas
respostas no arquivo e diz "respondi". O agente consolida decisões e acrescenta perguntas
relevantes, respeitando as dependências.

O [procedimento](../skills/productivity/entrevistar-por-arquivo/SKILL.md) cobre respostas parciais, mudanças
de opinião, preservação do texto humano e conflitos de edição. Há um
[modelo copiável](../skills/productivity/entrevistar-por-arquivo/alignment.template.md); adapte-o ao formato
existente. Os arquivos criados pertencem ao projeto de destino, sem banco ou serviço.

O alinhamento é suficiente quando as escolhas importantes para o objetivo estão resolvidas
e as incertezas têm encaminhamento explícito. Isso não exige detalhar todo o produto nem
autoriza automaticamente a implementação. Sem um gatilho externo já autorizado, salvar
o arquivo não aciona o agente sozinho; avise-o para processar a rodada.

## Papéis dos agentes

Os papéis ficam em `.agents/roles/`. `planner` planeja sem implementar. `evaluator` verifica
requisitos de forma independente e não corrige o produto. `representative` escolhe entre
alternativas sustentadas por evidências dentro de uma execução autônoma autorizada.
A existência de um papel não autoriza delegação; respeite ferramentas e permissões da sessão.

## Política de modelos

Defina provedor, modelo, esforço e alternativas em [`.agents/models.toml`](../.agents/models.toml).
O [guia de modelos](MODELS.md) explica as responsabilidades e o fluxo com representante.
A configuração deste repositório registra preferências pessoais em perfis da versão 2,
com seleção por papel e mapas explícitos de complexidade. O guia traz um exemplo neutro
com `inherit` para adoção; políticas locais da versão 1 continuam válidas sem migração.
`delegar`, `conselho`, `verificar-aceite` e `escrever-objetivo` consultam a política quando ela existe no destino.
O agente verifica a seleção na ferramenta real; o arquivo não muda a conversa aberta nem
autoriza delegação ou ações novas. `$propor` mantém a espera humana, salvo delegação explícita.

## Adotar em outro projeto

As rotas de instalação, o bloco para o `AGENTS.md` do projeto e a cópia manual estão em
[ADOPTING.md](ADOPTING.md).

## Atualizar um projeto que já adotou o harness

A origem desta coleção é [jordyfontoura/skills](https://github.com/jordyfontoura/skills).
As skills já copiadas continuam funcionando sem conexão com a origem. Quem instalou pelo
plugin atualiza pelo gerenciador de plugins do agente, conforme o [README](../README.md#atualizar).

Inclua `atualizar-harness` entre as skills adotadas e peça, por exemplo:

> `$atualizar-harness Atualize as skills deste projeto a partir de jordyfontoura/skills,
> preservando nossas adaptações e informando conflitos.`

A skill fixa uma revisão da origem, compara o conjunto instalado, preserva personalizações
e verifica referências e cópias dos provedores. Ela não substitui o código do produto nem
reconfigura CI, permissões ou hooks por padrão. Mudanças conflitantes precisam de uma decisão;
diferenças locais não são automaticamente descartadas como versões antigas.

Para cópias editáveis, `main` é o canal estável padrão; escolha `nightly` para experimentar
novidades. Por exemplo: `$atualizar-harness Atualize as skills a partir da branch nightly de
jordyfontoura/skills, preservando nossas adaptações.` A skill preserva o canal registrado nas
próximas atualizações, salvo pedido de outra referência. Uma tag fixa uma versão específica.
O canal experimental descrito aqui usa cópias editáveis; os comandos de plugin do README
continuam usando a instalação estável.

Na adoção ou atualização, registre na documentação de manutenção do destino a origem, o canal
ou referência fixa, a versão, o SHA incorporado e os componentes adotados. Preserve esse
registro nas próximas atualizações.
Se a atualização for parcial, identifique os componentes pendentes em vez de registrar
uma versão global incorreta. Não é necessário um serviço ou agendador para usar esse fluxo.

## Manter este repositório

O fluxo de edição, geração das cópias, validação e versões está em
[CONTRIBUTING.md](../CONTRIBUTING.md).
