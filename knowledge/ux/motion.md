# Movimento e animação de interfaces

- **Tipo:** referência de domínio; critérios de acessibilidade e recomendações contextuais.
- **Aplicabilidade:** movimento em interfaces web, nativas e de jogos. A seção de GSAP é
  específica da web; outras plataformas usam suas APIs e convenções.
- **Origem e revisão:** síntese própria das fontes catalogadas, consultadas em 17/11/2026;
  WCAG 2.2, documentação GSAP v3 e Impeccable em `d41d9860b0`.
- **Limites:** orientações e exemplos não substituem medição no dispositivo-alvo, testes
  com pessoas ou auditoria completa. Nenhuma biblioteca foi executada nesta pesquisa.

## Definir a função do movimento

O movimento pode explicar uma mudança de estado, orientar a atenção ou dar retorno a uma
ação. Identifique qual informação ele comunica, seu gatilho e o resultado final esperado.
Uma duração fixa não serve para toda tarefa: distância, frequência e possibilidade de
interrupção influenciam a escolha. Movimento decorativo não deve atrasar a ação principal.

Uma animação interrompida por nova ação precisa chegar a um estado coerente. Confira cliques
repetidos, cancelamento, troca de tela e redimensionamento. Evite tornar conteúdo e controles
essenciais dependentes de uma animação de entrada terminar.

## Preservar informação e acesso

Em movimento reduzido, mantenha o retorno da ação e a informação de estado: por exemplo,
troque um deslocamento amplo por uma mudança imediata de estado com texto de confirmação.
Não remova o único sinal de carregamento ou conclusão. Na web, consulte
`prefers-reduced-motion`; em aplicações nativas e jogos, considere as preferências e os
controles disponíveis na plataforma.

Os critérios WCAG têm condições e níveis distintos:

- **2.2.2, A:** movimento, piscar ou rolagem que começam automaticamente, duram mais de
  cinco segundos e aparecem junto de outro conteúdo precisam permitir pausar, parar ou
  ocultar, salvo quando essenciais. Informação atualizada automaticamente em paralelo
  precisa de controle de pausa, parada, ocultação ou frequência, salvo quando essencial;
  essa parte não tem o limite de cinco segundos.
- **2.3.1, A:** conteúdo não pode piscar mais de três vezes em qualquer intervalo de um
  segundo, a menos que esteja abaixo dos limiares de flash geral e vermelho. Uma captura
  isolada não permite examinar frequência nem esses limiares.
- **2.3.3, AAA:** animação de movimento disparada por interação pode ser desativada, salvo
  quando essencial à função ou informação. Não rotule esse critério como AA; respeitar
  movimento reduzido também pode ser requisito próprio do projeto.

Consulte [acessibilidade por forma de acesso](../accessibility/interface-criteria.md) para
relacionar cada observação ao critério e à meta. Reduzir movimento não substitui controles
de pausa nem demonstra atendimento aos critérios sobre flashes.

## Escolher o mecanismo pelo projeto

Reutilize a biblioteca e os recursos da plataforma. Na web, transições CSS e Web Animations
API podem atender casos simples. Uma sequência sincronizada, controle de linha do tempo ou
animação ligada à rolagem pode justificar avaliar GSAP. A existência de animação, sozinha,
não exige uma dependência nova.

Quando possível, prefira animar `transform` e `opacity` a propriedades que recalculam layout
a cada quadro. Isso não garante fluidez: quantidade de elementos, pintura, imagens e trabalho
em JavaScript continuam relevantes. Meça no contexto-alvo antes de atribuir ganho de desempenho.

### GSAP em projetos web

- Conferir a versão instalada e as APIs da documentação correspondente.
- Usar `gsap.matchMedia()` para condições de tamanho e movimento reduzido, preservando a
  informação em ambos os caminhos. Mudanças de preferência precisam recompor o estado.
- Associar a criação das animações ao ciclo de vida da tela ou componente. Usar a reversão
  do contexto ou de `matchMedia` e limpar efeitos externos, listeners e temporizadores próprios.
- Verificar se rolagem, foco, conteúdo e ações continuam operáveis durante a animação e
  após desmontagem, remontagem e mudança de breakpoint.
- Conferir a licença vigente antes da adoção. GSAP usa licença própria, com usos permitidos
  sem cobrança e restrições, incluindo certos construtores visuais de animação concorrentes
  do Webflow. Disponibilidade gratuita não significa licença MIT ou Apache-2.0.

## Conferir o resultado em execução

Percorra a mesma ação com movimento normal e reduzido. Inclua interrupção, repetição,
cancelamento e saída da tela quando pertinentes. Observe estado final, retorno e foco.
Inspecione tamanhos e temas em escopo e, se desempenho for requisito, registre dispositivo,
condições, medição e limite esperado. Uma gravação ajuda a examinar a sequência; não substitui
a operação da interface nem prova, sozinha, conformidade sobre flashes.

## Fontes

[Fontes e referências de movimento](../references.md#movimento).
