<!-- Gerado de knowledge/accessibility/interface-criteria.md; edite a fonte no harness. -->

# Acessibilidade por forma de acesso

- **Tipo:** referência de domínio; os critérios não substituem o procedimento da skill.
- **Aplicabilidade:** WCAG 2.2 e WCAG2ICT para interfaces, conforme plataforma e meta adotadas.
- **Origem e revisão:** extração do harness em `d3c31c7`, em 12/11/2026.
  As fontes externas não foram reconferidas nesta extração; confirme a versão vigente
  quando ela for decisiva para o julgamento.
- **Limites:** a lista não cobre toda a norma; inspeção parcial e ferramentas automáticas não declaram conformidade.

## 3. Acessibilidade

Os itens abaixo são exemplos frequentes, não uma lista completa. Numa auditoria, percorra
todos os critérios dos níveis da meta. Indique número e nível do critério em cada achado.
Separe o que a forma de acesso permite examinar:

- **No código ou na árvore de acessibilidade:** texto alternativo (1.1.1, A); estrutura,
  títulos e rótulos ligados a campos (1.3.1 e 3.3.2, A); idioma (3.1.1, A); nome, função,
  estado e valor dos controles (4.1.2, A); nome acessível contendo o rótulo visível
  (2.5.3, A); mensagens de status anunciadas (4.1.3, AA).
- **Na tela renderizada ou em capturas:** informação que não depende só de cor (1.4.1, A);
  contraste de texto (1.4.3, AA) e de componentes, ícones e indicadores de foco (1.4.11, AA);
  foco visível (2.4.7, AA); tamanho aparente de alvos (2.5.8, AA). Contraste e medidas tirados
  de capturas são aproximados. Confirme-os com os valores reais de cor e tamanho.
- **Operando a interface:** teclado completo e sem armadilhas (2.1.1 e 2.1.2, A); ordem de foco
  (2.4.3, A); foco não encoberto (2.4.11, AA); reflow (1.4.10, AA); texto ampliado (1.4.4, AA);
  conteúdo em *hover* ou foco (1.4.13, AA); orientação (1.3.4, AA); alternativas a gestos
  complexos e a arrastar (2.5.1, A; 2.5.7, AA); tempo limite (2.2.1, A); dados não pedidos
  de novo (3.3.7, A); autenticação sem teste cognitivo (3.3.8, AA).
- **Com tecnologia assistiva ou ferramenta:** leitores de tela, controle por voz, ampliadores
  e auditorias. Ferramentas automáticas detectam só parte das falhas; um resultado limpo não
  prova conformidade.

Movimento reduzido é boa prática ou nível AAA (2.3.3); não o registre como falha AA. Com apenas
capturas, marque como não examinados os itens de código e de operação. A conformidade vale para
páginas e processos completos; uma inspeção de telas escolhidas não a declara.

Em software que não é web, aplique os critérios conforme a WCAG2ICT. Os pixels CSS correspondem
às unidades independentes de densidade da plataforma. O reflow é avaliado no menor tamanho que a
plataforma permite, e o idioma e o tamanho de texto podem vir do sistema. Some as diretrizes e os
inspetores de acessibilidade da plataforma. Para alvos de toque, siga o critério mais exigente
entre o 2.5.8 e a plataforma, mas registre como falha WCAG apenas o que descumprir o 2.5.8.

## Fontes

- [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/), recomendação de 12 de dezembro de 2024 citada na origem.
- [WCAG2ICT, W3C](https://www.w3.org/TR/wcag2ict-22/), orientação para software que não é web.
