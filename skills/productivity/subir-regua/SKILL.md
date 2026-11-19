---
name: subir-regua
description: Conduz uma melhoria em etapas. Cada etapa repete avaliar e corrigir até cumprir o critério de um avaliador; depois, o próximo avaliador, de outra família ou com meta mais alta, examina a versão inteira. Use quando o usuário pedir `subir-regua` ou o modo `$subir-regua` junto de outra skill. Não autoriza alterações por si.
license: Apache-2.0
---

# Subir a régua

Este modo organiza a progressão; a skill combinada define como avaliar. Com `criticar`, cada
avaliação segue a crítica e suas notas; com `escrever-claro`, a revisão de texto; com
`revisar`, um diff; com um benchmark ou teste, a medida combinada. Sem skill nem medida
indicadas, derive o método do pedido e declare-o antes da primeira etapa.

A ideia é a da subida de encosta (hill climbing): partir da versão atual, aceitar apenas mudanças
que não pioram e, ao atingir o critério de uma etapa, submeter o resultado a uma régua mais
alta. A régua sobe por **troca de avaliador**, como outra família de modelos, ou por **meta
mais alta**, como p95 abaixo de 200 ms e depois de 100 ms.

## Fixar o combinado antes da primeira rodada

Registre na conversa, sem reabrir decisões já tomadas:

- **Objeto e versão inicial:** o que melhorar, com versão recuperável, como um commit.
- **O que preservar:** comportamento, decisões, identidade e restrições que nenhuma etapa muda.
- **Cobertura:** telas, viewports, estados, fluxos, seções ou cenários avaliados em toda etapa.
- **Critério de cada etapa:** por exemplo, `9.00` ou mais em **cada** tela, sem violar pisos
  obrigatórios. Média alta não compensa um item reprovado. Sem limiar combinado, pergunte;
  não crie um por conta própria.
- **Escada:** a sequência de etapas, cada uma com avaliador e critério.
- **Limite de ciclos por etapa:** o do pedido; senão, `max_cycles` da escada; senão, 3.
  O pedido pode fixar limites diferentes para etapas específicas.
- **Autorização:** "melhore" ou "ajuste" autoriza o ciclo de alterações dentro do escopo.
  Pedir apenas avaliação autoriza só as consultas; sem correções, cada etapa termina no
  primeiro relato. Invocar este modo autoriza as consultas aos avaliadores da escada, mas
  não outras delegações, publicações ou mudanças fora do objeto.

### Escolher a escada

Use, em ordem, a sequência do pedido, a escada nomeada no pedido ou `ladders.padrao` da
política local em `.agents/models.toml`. Cada etapa da política declara `provider`, `model`
e `effort`; o formato está em `docs/MODELS.md` do harness. Sem nenhuma dessas fontes,
pergunte pela sequência.

As etapas são uma sequência, não alternativas por indisponibilidade. Não aplique os
`candidates` dos perfis a uma etapa. Confira a disponibilidade real de modelo e esforço
antes de começar; se uma etapa não puder executar como pedida, ela fica pendente e a escada
para nela, salvo nova decisão do usuário.

## Executar um ciclo

1. **Avaliar em contexto novo.** Use `delegar` com o modelo e o esforço da etapa. Entregue
   objeto e versão, critérios, cobertura, decisões, descartes e achados anteriores com seu
   estado: resolvido, persistente ou rejeitado com motivo. Não entregue notas anteriores,
   a expectativa de aprovação nem a defesa de quem implementou.
2. **Conferir os achados.** Quem implementa usa `tratar-revisao`. Um achado sem evidência
   suficiente pode ser rejeitado com motivo registrado; as sugestões são meios a conferir.
3. **Corrigir por prioridade** com `implementar` e repetir as provas afetadas, inclusive as
   de itens já aprovados.
4. **Decidir a referência.** A nova versão substitui a referência apenas se não houver
   regressão: defeito novo em item aprovado, prova objetiva falhando ou violação do que
   deveria ser preservado. Pequena variação de nota não é melhora nem regressão. Se houver
   regressão, recupere a referência anterior e tente outra correção.
5. **Reavaliar a nova versão** com o mesmo avaliador, em outro contexto novo. Não repita a
   avaliação de uma mesma versão para obter nota melhor.

Quem implementa não avalia o próprio trabalho como etapa. Quando avaliador e implementador
forem da mesma família de modelos, a etapa ocorre como pedida, mas o relato registra que a
independência é mais fraca.

## Avançar entre etapas

Quando o critério da etapa for cumprido em toda a cobertura, a versão aprovada vira referência
e a próxima etapa avalia **tudo** desde o início, sem herdar a aprovação anterior. Achados
rejeitados seguem como descartes registrados, e o novo avaliador pode contestá-los com
evidência nova.

Se uma etapa só não passa por causa de um achado rejeitado, apresente a divergência ao
usuário em vez de continuar o ciclo. Não baixe o limiar, não troque o avaliador e não pule
etapas para obter aprovação.

## Parar

Encerre com um destes estados:

- **Concluída:** a última etapa cumpriu o critério.
- **Limite atingido:** a etapa esgotou seus ciclos. A escada para nela, com a meta pendente.
- **Estagnação:** duas correções sem resolver o mesmo defeito, ou sua recorrência. Use
  `diagnosticar` antes de nova tentativa, dentro do limite restante.
- **Etapa pendente:** modelo, esforço, acesso ou decisão indisponível. Continue apenas o
  trabalho independente autorizado.
- **Interrompida:** o usuário mudou ou encerrou o pedido.

A última versão não é automaticamente a melhor; entregue a última referência aprovada.

## Relatar

Mantenha um registro na conversa; para execuções longas, use `passar-contexto`. Uma linha
por ciclo indica etapa, modelo e esforço pedidos e observados, versão avaliada, notas ou
medidas, achados resolvidos, abertos e rejeitados, e a decisão sobre a referência.

No fim, informe o estado de parada, a referência entregue, as notas por etapa, a cobertura,
os avisos de independência e as provas ausentes. Notas de modelos diferentes não formam uma
série comparável. Uma nota que sobe não comprova melhora por si: recomende teste com
pessoas ou `verificar-aceite` quando a decisão depender disso.

## Fundamentos

- [Pan et al., 2024](https://arxiv.org/abs/2407.04549), preprint: em revisão iterativa de
  redações, a nota do avaliador subiu enquanto a nota humana estagnou ou caiu, sobretudo com
  contexto compartilhado entre autor e avaliador. Um avaliador sem o histórico acompanhou as
  pessoas. Daí o contexto novo e a ausência de notas anteriores.
- [Panickssery et al., NeurIPS 2024](https://arxiv.org/abs/2404.13076): modelos avaliam melhor
  os próprios textos do que textos equivalentes para pessoas. Daí a alternância de famílias
  e o aviso de independência.
- [Verga et al., 2024](https://arxiv.org/abs/2404.18796), preprint: avaliadores de famílias
  diferentes mostraram menos viés do que um único avaliador grande.
- [Gao et al., 2022](https://arxiv.org/abs/2210.10760), preprint: otimizar uma medida
  substituta acaba reduzindo a qualidade real, como prevê a lei de Goodhart. Daí a regra da
  referência e o limite de ciclos.
- [Madaan et al., NeurIPS 2023](https://arxiv.org/abs/2303.17651): no Self-Refine, as primeiras
  rodadas concentraram os ganhos. Daí o limite padrão de 3 ciclos por etapa.

Nenhum desses estudos testou esta sequência de etapas. Eles fundamentam as regras sem
medir o ganho do modo.
