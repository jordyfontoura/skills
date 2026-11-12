---
name: criticar
description: Critica a qualidade de um artefato ou experiência, como jogo, interface ou texto, com critérios especializados, evidências e prioridades. Use para pedir um crítico independente ou compor uma crítica com conselho. Não corrige; para diff use `revisar` e para aceite use `verificar-aceite`.
license: Apache-2.0
---

# Criticar um artefato ou experiência

Fixe o objeto e a versão, o público, a intenção, o foco pedido, as referências e as ações
permitidas. Consulte decisões, críticas anteriores e descartes antes de perguntar. Preserve
o escopo e as escolhas estabelecidas; especializar a crítica não autoriza redefinir o produto.
Para escolher entre propostas, use `conselho`; para atrito estrutural de código, use
`examinar-arquitetura`; para reescrever texto, use `escrever-claro`.

## Escolher o método e os critérios

Declare a especialização pertinente ao pedido e os critérios desta crítica antes do exame:

- **UI e UX**, inclusive a interface de jogos: leia [interface.md](interface.md) e sua
  [rubrica](interface-rubric.md). Preserve as sete seções, a escala e os pisos da rubrica.
- **Outros aspectos**, como game design, direção de arte ou argumentação de um texto: derive
  os critérios do pedido, das referências, das regras do projeto e de princípios do domínio
  com mecanismo explícito. Para clareza de texto, consulte `escrever-claro` sem reescrever.
  Identifique a origem e os limites dos critérios propostos; não apresente uma rubrica criada
  para o caso como padrão validado. Consulte fontes externas com `pesquisar-web` quando um
  julgamento depender delas; sem consulta, declare a origem não conferida.

Combine os métodos quando o objeto exigir. Uma rubrica de interface não cobre sozinha
cooperação, ritmo de jogo ou coerência de um argumento. Pergunte apenas se uma definição
ausente mudar o julgamento; nos demais casos, declare suposições razoáveis.

## Preservar a independência

Uma crítica pontual pode ocorrer no contexto atual se ele não produziu o objeto. Quem fez o
trabalho não apresenta sua autocrítica como independente. Num pedido de crítico independente
ou num ciclo produtor-crítico autorizado, use `delegar` para uma consulta em contexto novo.
Forneça objeto, versão, critérios, acesso, achados anteriores e decisões, sem usar a defesa
ou a autoavaliação do implementador como evidência.

Respeite o modelo explicitamente escolhido. Havendo política local, a consulta crítica usa
`roles.council` conforme `delegar`, inclusive quando individual; esse papel não exige painel.
Sem política, preserve as seleções do ambiente e do usuário. Configuração não comprova execução.
Se não houver contexto independente ou ferramenta adequada, declare a crítica pendente ou
limitada, sem simular outro especialista.

Para várias perspectivas solicitadas, leia [panel.md](panel.md) e siga `conselho` para compor
e executar as consultas. O coordenador organiza o painel uma única vez. Como crítico delegado,
faça apenas sua análise, sem abrir novos agentes ou conselhos.

## Examinar e fundamentar

Examine a forma mais fiel disponível para cada critério: jogue, navegue, leia ou opere o
artefato conforme autorizado. Capturas sustentam aparência, mas não demonstram sozinhas
controles, persistência, cooperação ou áudio. Código lido não comprova execução.
Use ambiente de teste e respeite os limites de ações com efeitos reais. Registre passos,
condições e materiais examinados; capacidade ou acesso ausentes continuam sendo limites.

Cada achado precisa de localização, observação, critério ou mecanismo, impacto, prioridade,
base e recomendação concreta. Use IDs estáveis e distinga `observado`, `inferido` e `hipótese`,
citando a evidência. Na UI, use o formato e a severidade da rubrica. Nos demais domínios,
justifique a prioridade pela consequência e pelo alcance, sem impor a escala de UI.
Um juízo sem critério nem mecanismo fica em sugestões de direção. Não confunda uma reação
prevista do público com comportamento observado em pessoas.

Agrupe ocorrências do mesmo problema. Preserve descartes do usuário, salvo evidência nova
declarada. Numa nova versão, marque achados anteriores como resolvidos, persistentes ou
regressões e identifique os novos. Aponte também o que funciona e deve resistir às correções.

## Notas e ciclos de correção

Dê notas apenas quando pedidas. Use as dimensões, escala e âncoras combinadas; referências
comentadas ajudam a calibrar a nota. Se faltar uma definição decisiva para um limiar de
aprovação, esclareça antes de pontuar. Ligue cada nota a evidências e explique sua incerteza.
Nota de qualidade geral e severidade de um problema são medidas distintas.

A crítica não edita o produto. Um ciclo só prossegue quando a implementação e as novas
avaliações estiverem autorizadas. Antes da primeira rodada, fixe critérios, eventual limiar,
regra de avaliação e condição de parada, incluindo o limite de rodadas quando combinado.
Modelo, notas e número de rodadas vêm do pedido, sem padrões universais.

Quem implementa confere o feedback com `tratar-revisao`, corrige por prioridade com
`implementar` e repete as provas afetadas. As sugestões são meios a conferir para atingir
o requisito; não ganham autoridade por terem vindo do crítico. Preserve versões recuperáveis
e evidências para comparar melhora e regressões. Cada nova crítica avalia a versão resultante;
não repita avaliações da mesma versão apenas até obter uma nota favorável.

Não baixe o limiar nem troque o crítico para obter aprovação. Após duas correções sem sucesso
ou recorrência do mesmo defeito, use `diagnosticar`. Encerre ao cumprir os critérios ou atingir
a condição de parada, relatando notas, problemas e provas ausentes. Se uma decisão ou acesso
ficar pendente, continue apenas o trabalho independente autorizado. A última versão não é
automaticamente a melhor. Notas não substituem provas técnicas nem `verificar-aceite`.

## Retornar

Entregue contexto, versão, especialização, critérios e formas de acesso; achados por prioridade
com evidências; o que preservar; divergências deliberadas e sugestões separadas; cobertura,
limites e provas recomendadas. Inclua notas e conclusão pelo limiar somente quando combinadas.
Num painel, preserve divergências e autoria dos achados. Sem problema relevante, diga isso
com a cobertura examinada, sem fabricar críticas nem declarar qualidade que não pôde verificar.
