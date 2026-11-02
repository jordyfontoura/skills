---
name: architecture-review
description: Analisa código existente para identificar atrito de arquitetura, acoplamento e dificuldades de manutenção ou teste, com propostas sustentadas por pontos de uso. Use mesmo sem diff; não implementa refatorações.
license: Apache-2.0
---

# Examinar a arquitetura existente

Defina a pergunta e o recorte: uma mudança difícil, um módulo, um fluxo ou uma área recorrente
do código. Leia instruções, glossário, decisões e arquitetura documentada. Use as ferramentas
de leitura permitidas; não edite, execute testes que alterem estado ou delegue por invocar esta skill.
`review` examina um diff fixo; `reconcile` compara requisitos e estado. Aqui o objeto é a estrutura
existente e o custo concreto de entendê-la, alterá-la ou testá-la.

## Procurar atrito demonstrável

Siga um fluxo real dos pontos de entrada aos dados, integrações e efeitos. Confira chamadas,
contratos e limites de responsabilidade antes de julgar a organização pelos nomes dos arquivos.
Quando útil e permitido, use histórico de mudanças para localizar áreas recorrentes. Frequência
de edição, tamanho ou quantidade de arquivos são pistas, não defeitos por si sós.

Procure situações em que uma mudança exige conhecer detalhes espalhados, um conceito tem
representações divergentes, responsabilidades se misturam ou uma abstração expõe quase toda
a complexidade que deveria organizar. Verifique se testes conseguem observar contratos úteis
ou dependem de detalhes internos. Cite os pontos de uso e a consequência concreta do atrito.

Não recomende abstrações para uma necessidade imaginada, padrões favoritos ou um limiar de
linhas. Pergunte se remover ou reunir uma camada reduziria a complexidade total ou apenas a
transferiria. Uma interface pequena também pode esconder acoplamento; compare implementação,
chamadores e dependências. Preserve limites de domínio e integrações que tenham motivo real.

## Propor mudanças proporcionais

Apresente poucas oportunidades, cada uma com evidência, consequência, proposta mínima,
contratos a preservar e forma de verificar o benefício. Considere manter o estado atual como
alternativa. Separe atrito observado, hipótese de melhoria e custo ainda desconhecido.
Não prometa ganho de desempenho ou manutenção sem medição ou experiência que o sustente.

Se a proposta contrariar uma decisão anterior, identifique-a e explique a evidência nova que
justificaria reabri-la. Não altere a decisão durante a análise. Priorize pelo trabalho que o
usuário precisa fazer e pelo custo de reversão, não pela ambição da refatoração.

Quando ajudar, represente o fluxo atual e a mudança proposta por um diagrama pequeno. Não
exija HTML, CDN, pontuação inventada ou um relatório separado para toda análise. Uma referência
de fonte é apoio ao julgamento, não prova de um defeito local.

Entregue a recomendação, as áreas examinadas e os limites de acesso ou evidência. Se não houver
oportunidade sustentada, diga isso. Encaminhe escolhas abertas a `interview` e uma refatoração
autorizada a `specify` ou `implement`; esta análise não concede autorização para executá-la.

Inspirada em [improve-codebase-architecture, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md),
adaptada para evidência local e decisões existentes, sem dependências obrigatórias de ferramentas.
