# Técnicas de game design

- **Tipo:** referência de domínio; vocabulário e técnicas para analisar e ajustar um jogo.
- **Aplicabilidade:** concepção, análise e ajuste de mecânicas, ritmo, dificuldade, resposta
  ao jogador e escopo, em qualquer motor.
- **Origem e revisão:** pesquisa na internet em 16/11/2026. O artigo do MDA foi lido na
  íntegra; das palestras da GDC foram lidas apenas as páginas de descrição.
- **Limites:** são modelos e relatos de profissionais, não evidência experimental. Nenhum
  deles prevê diversão; o que valida uma escolha é o teste com jogadores do público pretendido.

## 1. MDA: mecânicas, dinâmicas e estéticas

Hunicke, LeBlanc e Zubek dividem um jogo em três camadas ligadas por causa e efeito:

- **Mecânicas:** os componentes do jogo, no nível de dados e algoritmos; as ações e os
  controles oferecidos ao jogador.
- **Dinâmicas:** o comportamento das mecânicas em execução, reagindo às entradas do jogador
  e umas às outras ao longo do tempo.
- **Estéticas:** as respostas emocionais desejadas no jogador.

O designer parte das mecânicas e chega às estéticas; o jogador percorre o caminho inverso.
Comece o projeto pela experiência desejada e derive dela as dinâmicas e as mecânicas.

Em vez de "divertido", o artigo propõe nomear o tipo de experiência:

| Estética | O jogo como |
| --- | --- |
| Sensação | prazer dos sentidos |
| Fantasia | faz de conta |
| Narrativa | drama |
| Desafio | percurso de obstáculos |
| Companheirismo | estrutura social |
| Descoberta | território desconhecido |
| Expressão | descoberta de si |
| Submissão | passatempo |

A lista não é fechada: nos exemplos, o artigo também usa "competição".

Para ajustar um jogo, modele as dinâmicas. O artigo analisa o Monopoly: quem lidera acumula
recursos e pune os outros com eficácia crescente, um ciclo de realimentação que tira a
tensão da partida. As correções sugeridas atuam nas mecânicas, como ajudar quem está atrás
ou dificultar o avanço de quem está à frente. O ajuste final vem de testes repetidos.

## 2. Loops, arcos e habilidades

Daniel Cook distingue dois formatos de conteúdo:

- **Loop:** o modelo mental do jogador motiva uma ação, o sistema responde e o modelo se
  atualiza, reiniciando o ciclo. Loops constroem domínio pela repetição.
- **Arco:** um loop interrompido, do qual o jogador sai em seguida. Arcos entregam um
  conteúdo que não foi feito para repetir, como uma cena de história.

Em *The Chemistry of Game Design*, o mesmo autor descreve o "átomo de habilidade": ação,
simulação, retorno e modelagem. Cada átomo é uma habilidade que o jogador adquire, e os
átomos se encadeiam. O jogador abandona um átomo quando para de ver valor em praticá-lo;
mapear a cadeia mostra onde isso acontece.

Sid Meier, na GDC 2012, caracteriza a jogabilidade como uma série de decisões interessantes.
A página consultada não traz a definição de decisão interessante.

## 3. Flow e dificuldade

Jenova Chen aplica a jogos o conceito de flow: a experiência se rompe quando se afasta
demais do equilíbrio, por ansiedade ou por tédio. Ele critica o ajuste automático de
dificuldade que tenta adivinhar o estado do jogador e defende dar ao jogador escolhas que
regulam o desafio dentro do próprio jogo.

## 4. Resposta, "juice" e tolerância

"Juice" é o conjunto de pequenos efeitos que torna uma ação satisfatória. Na palestra
*Juice It or Lose It* (GDC Europe 2012), Martin Jonasson e Petri Purho aplicam esses
truques, um a um, a um jogo simples.

Maddy Thorson lista as técnicas de tolerância usadas em Celeste. Todas ampliam janelas de
tempo ou de posição em favor do jogador:

- **Coyote time:** aceitar o pulo logo depois de sair da plataforma.
- **Buffer de pulo:** aceitar o pulo apertado pouco antes de tocar o chão.
- **Gravidade reduzida no ápice** do pulo.
- **Correção de quina** no pulo e no dash.
- **Janela ampla** para o pulo na parede.

A autora diz que o estúdio não inventou essas técnicas.

## 5. Princípios de apresentação

Matt Allmer adapta os doze princípios da animação em treze princípios de jogabilidade:
ponto focal, antecipação, anúncio de mudança, eventos e comportamentos críveis, eventos
sobrepostos, física, som, ritmo, espaçamento, design linear ou por componentes, jogador,
comunicação e apelo. Use a lista para revisar uma proposta antes de apresentá-la.

## 6. Escopo: o problema da porta

Liz England usa uma porta para mostrar o custo de um recurso que parece simples. Como o
jogador sabe que ela abre? Ela tranca? Como se comporta com inimigos e no modo cooperativo?
Design, arte, áudio, programação, produção e testes tocam a mesma porta. Antes de prometer
um recurso, faça as perguntas da porta e liste as disciplinas envolvidas.

## 7. Processo de fases

O *Level Design Book* ordena o trabalho de uma fase em: pré-produção, combate (quando
houver), layout, blockout, scripting, iluminação, arte de ambiente e lançamento. O blockout
é um rascunho jogável e deve ser testado antes de receber arte.

## 8. Acessibilidade

As *Game Accessibility Guidelines* organizam as diretrizes em três níveis (básico,
intermediário e avançado) e seis categorias (motora, cognitiva, visão, audição, fala e
geral). O nível básico reúne medidas fáceis de implementar e de amplo alcance. Segundo o
site, as quatro reclamações mais frequentes são: remapeamento de controles, tamanho do
texto, daltonismo e apresentação das legendas.

Do nível básico:

- Permitir remapear os controles e ajustar a sensibilidade.
- Usar um tamanho de fonte padrão legível e alto contraste entre texto e fundo.
- Não transmitir informação essencial apenas por cor ou apenas por som.
- Oferecer legendas para toda fala importante.
- Separar os volumes de efeitos, fala e música.
- Oferecer várias opções de dificuldade.
- Salvar todas as configurações.

Para critérios de interface, consulte a
[acessibilidade por forma de acesso](../accessibility/interface-criteria.md).

## Fontes

Consultadas em 16/11/2026.

- Robin Hunicke, Marc LeBlanc e Robert Zubek, [*MDA: A Formal Approach to Game Design and Game Research*](https://users.cs.northwestern.edu/~hunicke/MDA.pdf).
  O artigo relata oficinas da GDC de 2001 a 2004.
- Daniel Cook, [*Loops and Arcs*](https://lostgarden.com/2012/04/30/loops-and-arcs/), 30/04/2012, e
  [*The Chemistry of Game Design*](https://www.gamedeveloper.com/design/the-chemistry-of-game-design), 19/07/2007.
- Sid Meier, [*Interesting Decisions*](https://www.gdcvault.com/play/1015756/Interesting), GDC 2012.
- Jenova Chen, [*Flow in Games*](https://www.jenovachen.com/flowingames/designfig.htm), 2006.
- Martin Jonasson e Petri Purho, [*Juice It or Lose It*](https://www.gdcvault.com/play/1016487/Juice-It-or-Lose), GDC Europe 2012.
- Maddy Thorson, [*Celeste & Forgiveness*](https://www.maddymakesgames.com/articles/celeste_and_forgiveness/index.html).
- Matt Allmer, [*The 13 Basic Principles of Gameplay Design*](https://www.gamedeveloper.com/design/the-13-basic-principles-of-gameplay-design), 27/02/2009.
- Liz England, [*The Door Problem*](https://lizengland.com/blog/2014/04/the-door-problem/), 21/04/2014.
- [*The Level Design Book*](https://book.leveldesignbook.com/process/overview), visão geral do processo.
- [*Game Accessibility Guidelines*](https://gameaccessibilityguidelines.com/) e seu
  [nível básico](https://gameaccessibilityguidelines.com/basic/).
