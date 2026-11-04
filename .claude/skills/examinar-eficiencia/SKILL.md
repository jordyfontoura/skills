---
name: examinar-eficiencia
description: Examina por que o trabalho com o agente está demorando ou gastando muitos tokens e propõe a menor mudança para cada causa, sem reduzir a qualidade. Use quando perguntarem por demora, custo, tokens ou retrabalho de uma sessão. Para lentidão do produto, use `diagnosticar`; para saber em que ponto o trabalho está, `andamento`.
license: Apache-2.0
---

# Examinar a eficiência do trabalho

Responda por que o trabalho demorou ou consumiu muitos tokens e o que mudaria isso. Examine
a sessão indicada pelo usuário; sem indicação, a conversa atual. A pergunta não cancela nem
muda o trabalho em curso; depois da resposta, retome a etapa autorizada.

## Reunir evidências

Use a conversa, os diffs, os resultados de verificações e as métricas que o ambiente expõe,
como uso de tokens, duração de subagentes, custo estimado ou tempo de comandos. Cite a fonte
de cada número. Leia logs locais de sessão, como os arquivos JSONL do agente, somente quando
o usuário pedir explicitamente. Não leia segredos e não reproduza conteúdo privado na resposta.

Contagem de palavras, mensagens, consultas ou chamadas de ferramenta não mede tokens faturados
nem cota da assinatura. Não deduza custo do nome do modelo, do limite do plano ou do total da
sessão. Quando a métrica não estiver exposta, registre-a como desconhecida e descreva apenas
o sinal observado, como "o mesmo arquivo foi lido quatro vezes".

## Procurar as causas

Examine as causas que a evidência sustenta, sem preencher uma lista fixa:

- **Contexto inflado:** releituras do mesmo arquivo, leitura inteira quando um trecho bastava,
  saídas longas de comandos ou buscas amplas sem filtro.
- **Retrabalho:** requisito ambíguo, decisão reaberta, correção desfeita ou prova repetida
  depois de uma edição que a invalidou.
- **Delegação:** subagente para uma consulta curta, perfil de modelo acima da complexidade,
  briefing incompleto que gerou nova rodada ou trabalho repetido pelo coordenador.
- **Verificações:** suíte lenta repetida quando o resultado anterior continuava válido, ou
  execução ampla quando uma verificação focada provava o mesmo ponto.
- **Esperas:** consultas repetidas ao estado de uma tarefa, polling ou tempo limite sem diagnóstico.
- **Ciclos de revisão:** rodadas de correção causadas por critério ausente no início.
- **Escopo:** investigação ou mudanças além do pedido.
- **Instruções:** regra do harness, skill ou configuração que exige passos desnecessários
  para o caso.

Separe o que foi observado do que foi inferido. Um sinal isolado não demonstra a causa;
várias causas podem coexistir. Não transforme um caso isolado em regra geral.

## Propor sem perder qualidade

Para cada causa, proponha a menor mudança que teria reduzido o gasto observado e declare seu
custo ou risco. Prefira mudar o pedido, o briefing ou a ordem dos passos a acrescentar regras.
Nunca proponha remover verificações úteis, provas, aceite independente ou perspectivas de
`conselho` só para economizar. Economia não autoriza mudar escopo, modelo ou provedor escolhidos.

Aplique só mudanças já autorizadas, como ajustar a própria forma de trabalhar no restante
da sessão. Quando a causa estiver numa instrução do harness ou do projeto, apresente a proposta
e use `melhorar-harness` para o procedimento; não edite instruções compartilhadas sem autorização.
Para comparar modelos ou provedores em tarefas equivalentes, siga `delegar`.

## Responder

Ordene os achados pelo impacto estimado. Para cada um, informe:

- evidência e fonte;
- causa, marcada como observada ou inferida;
- menor mudança proposta e seu custo;
- quem pode aplicá-la: o agente, o usuário ou uma mudança autorizada nas instruções.

Termine com o que ficou desconhecido e o que permitiria medir, como métricas não expostas ou
logs não lidos. Entregue a resposta na conversa, sem salvar arquivo por padrão. Uma proposta
não demonstra economia; isso exige comparar execuções equivalentes, quando autorizado.
