---
name: conselho
description: Consulta especialistas independentes para explorar melhorias, refinar propostas ou resolver escolhas importantes quando houver pedido de comitê ou análise multidisciplinar. Retorna evidências, divergências e recomendação.
license: Apache-2.0
---

# Consultar especialistas

Identifique a pergunta, as restrições combinadas e o objeto da consulta: uma decisão, proposta
ou estado atual. Fixe a versão ou os materiais em análise. Leia as regras de comitê e as
instruções de especialistas existentes.
Sem proposta pronta, use o estado atual e a pergunta como objeto comum da consulta. Peça o
melhor argumento para manter esse estado, melhorias sustentadas e critérios de escolha;
não invente uma proposta aprovada nem trate a exploração como autorização para implementar.
Uma dúvida factual comum raramente exige conselho; investigue diretamente ou use `entrevistar`
para uma escolha que cabe ao usuário.

Adapte a pergunta comum à situação, sem exigir um formato diferente de relatório para cada caso:

- **Explorar melhorias:** examine o estado atual, o que preservar e as poucas mudanças de
  maior utilidade. Não peça apenas argumentos favoráveis a mudar.
- **Comparar alternativas:** forneça as mesmas opções e critérios a cada especialista.
  Peça que avaliem todas e indiquem em quais condições cada uma é preferível, em vez de
  atribuir a cada agente a defesa de uma opção.
- **Criticar uma proposta definida:** examine seus requisitos, consequências e evidências
  na versão fixada. Sugira alternativas quando resolverem uma preocupação concreta,
  sem reabrir decisões estabelecidas só para produzir divergência.

Selecione perspectivas necessárias para cobrir a decisão e seus riscos, como produto,
comunidade, acessibilidade, arquitetura ou privacidade. Explique sua relevância. Reutilize instruções
aplicáveis sem transferir a governança de um projeto para trabalhos alheios.
O conselho é consultivo, salvo regra explícita de aprovação neste projeto.
Escolha a quantidade de consultas pelas perspectivas necessárias, sem preencher uma lista fixa
de especialistas. Priorize profundidade, cobertura e independência; não reduza a composição
ou a investigação para economizar chamadas ou tokens. Declare a pergunta de cada perspectiva,
mantendo opções e critérios comuns. Essas perguntas orientam a análise sem impedir que um
especialista identifique riscos além delas. Preserve a quantidade e as perspectivas pedidas
pelo usuário. Se ele pedir uma única consulta, respeite e identifique o parecer como individual.
Um modelo citado no pedido define o modelo das consultas, não sua quantidade.

## Preparar as evidências

Organize a decisão pendente, as opções, as restrições, a revisão fixada e as evidências
disponíveis, com caminhos ou links para as fontes originais. A investigação do coordenador
é um ponto de partida; preparar a consulta não exige outro agente nem um arquivo novo.
Separe fatos conferidos, interpretações e lacunas, incluindo evidências contrárias à proposta.

Cada especialista investiga as fontes de forma independente, confere as premissas que sustentam
seu parecer e procura omissões ou evidências contrárias. Pode reler materiais já consultados,
ampliar a busca e examinar o contexto adjacente dentro do escopo autorizado. A seleção do
coordenador não limita a investigação nem substitui esse julgamento. Se uma premissa decisiva
não puder ser conferida, declare o limite; um resumo compartilhado não comprova validação
independente da fonte.

## Obter pareceres independentes

Use `delegar` para consultas autorizadas. Respeite modelos escolhidos e capacidades reais
da ferramenta; esta skill não fixa provedor, modelo, esforço nem tamanho de comitê.
Se houver `.agents/models.toml`, resolva `roles.council` seguindo `delegar`: na v2, use seu
perfil sem substituição por complexidade; na v1, preserve campos e alternativas. Isso vale
para cada consulta, salvo escolha explícita do usuário para um especialista.
Execute cada perspectiva independente em seu próprio contexto. Várias perspectivas num único
contexto continuam sendo um parecer individual; vários contextos com o mesmo modelo podem
fornecer pareceres separados. Declare a composição escolhida e sua relevância.
Dê a cada especialista a mesma versão do objeto, as opções, os critérios e as restrições, com
as evidências relevantes e sua pergunta específica. Por exemplo, numa mudança de especificação,
produto examina se ela preserva a intenção humana durante mudanças; engenharia examina se
liga cada requisito a uma prova sem duplicar registros. Ambos podem questionar as premissas
e avaliar todas as opções. Não forneça o veredito de outro especialista antes dos primeiros
pareceres. Preserve o limite de somente leitura; não peça implementação, mudança de decisões
nem abertura de novos agentes.

Peça que cada especialista retorne:

- O argumento mais forte a favor da proposta ou de manter o estado atual, pela sua perspectiva.
- Benefícios, riscos e pessoas afetadas, ligados a trechos da proposta ou evidências.
- Achados relevantes com fonte, consequência e classificação: impedimento, ressalva tratável
  ou fato ausente. Registre também sinais iniciais e incertezas, distinguindo-os de defeitos provados.
- Recomendação, alternativas ou mitigação, e evidências que poderiam mudar o parecer.

Escreva com clareza, sem limitar a profundidade ou a quantidade de achados para encurtar o
parecer. Não exija elogios, número mínimo de sugestões ou plano de implementação em toda
consulta. Uma conclusão curta é válida quando sustentada pela investigação, não uma meta.

Um impedimento precisa de conflito concreto com um requisito combinado ou mecanismo de dano
sustentado. Uma implementação imaginada não é defeito demonstrado. Separe achados de pesquisa,
inferências do especialista e desconhecimentos. Identifique alegações factuais não verificadas;
não invente citações, pesquisa com usuários ou estimativas numéricas para fortalecer um parecer.

Se não for possível executar contextos independentes, declare o limite e entregue uma análise
ou uma consulta não realizada. Perspectivas escritas por um único agente não são especialistas
independentes e não devem ser apresentadas como conselho concluído.

## Consolidar sem inventar concordância

Compare os pareceres contra o mesmo objeto e as mesmas restrições. Preserve divergências
importantes, objeções sem resposta e lacunas; maioria não resolve uma disputa factual.
Abra novas rodadas quando evidências, divergências ou consequências não resolvidas exigirem
aprofundamento, preservando os pareceres originais. Não fixe um limite de rodadas por economia.
Encerre quando a cobertura for suficiente para a decisão e os pontos restantes não mudarem a
recomendação; se faltar prova decisiva, indique como obtê-la em vez de repetir opiniões.
Quando o objeto mudar, envie a alteração, sua revisão e os achados anteriores, e reexamine
seus efeitos no conjunto da proposta. Amplie a reavaliação sempre que houver interações ou
consequências fora do trecho alterado. Preserve decisões e provas cuja validade se mantenha.

Retorne perspectivas consultadas, limites reais de execução, concordâncias, divergências,
impedimentos, ressalvas e provas ausentes. Recomende prosseguir, revisar ou obter evidências
específicas, com razões e próximos passos concretos. Aplique regras de aprovação existentes
somente à versão avaliada; não invente um veto universal do comitê.
Explique quais sugestões recomenda incorporar ou descartar e por quê, ligando-as às evidências
disponíveis ou marcando-as como inferências. Concordância apoiada na mesma premissa não
verificada mantém essa premissa como desconhecida; não a transforma em prova.

Pareceres não aprovam por si só mudanças no produto nem substituem uma decisão humana
reservada pelo projeto. Quem consultou o conselho preserva achados úteis na conversa ou nos
documentos existentes e age dentro da autorização. Use `verificar-aceite` para aceite da implementação.
Observe e informe tempo e uso quando disponíveis, respeitando limites explícitos do usuário.
Reduzir custo não é um objetivo do conselho nem uma medida da qualidade dos pareceres.
