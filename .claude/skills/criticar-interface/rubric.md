# Rubrica de crítica de interface

Base comum para criticar interfaces em qualquer projeto. Percorra as seções nesta ordem, para
que críticas de pessoas ou execuções diferentes sejam comparáveis, e registre cada seção como
examinada ou não examinada.

Diretrizes do projeto e da plataforma prevalecem sobre esta base em convenções, estilo e
padrões de componentes. Elas não reduzem dois pisos:

- **Acessibilidade:** WCAG 2.2 nível AA, ou meta mais exigente do projeto, inclusive legal.
- **Escolha da pessoa:** a interface não leva ninguém a decidir contra o próprio interesse.

Uma diretriz do projeto abaixo de um piso é registrada como conflito, e o achado mantém sua severidade.

## Como percorrer

1. Faça uma primeira passada só para entender a interface e as tarefas.
2. Na segunda, aplique as seções. Um problema que viola vários padrões é um achado só, com
   todos os padrões listados, registrado na primeira seção em que aparecer.
3. Separe achados, divergências deliberadas e sugestões de direção, conforme
   "Achado ou preferência".

## 1. Tarefas e fluxos

Inclua as tarefas principais e as de saída: recusar, cancelar, desfazer, excluir e sair.
Percorra cada tarefa e registre desvios, becos sem saída, etapas desnecessárias e perda de
dados ao voltar ou cancelar.

Quando a aprendizagem importar ou a tarefa usar padrões pouco familiares, defina antes a
sequência correta de ações e faça em cada passo as perguntas do percurso cognitivo
(*cognitive walkthrough*):

1. **Intenção:** a pessoa tentará alcançar o resultado certo neste passo?
2. **Visibilidade:** ela perceberá que a ação correta está disponível?
3. **Associação:** ela ligará essa ação ao resultado que deseja?
4. **Retorno:** depois de agir, perceberá que avançou em direção ao objetivo?

Uma resposta "não" indica um achado no passo. Em fluxos convencionais, dispense as perguntas.

## 2. Heurísticas de usabilidade

Examine a interface pelas 10 heurísticas de Nielsen:

1. **Visibilidade do estado do sistema:** o sistema informa o que está acontecendo, a tempo.
2. **Correspondência com o mundo real:** usa a linguagem e as convenções do público, não jargão interno.
3. **Controle e liberdade:** há como desfazer, refazer, cancelar e sair de um caminho indesejado.
4. **Consistência e padrões:** termos, ações e aparência se mantêm no produto e seguem convenções.
5. **Prevenção de erros:** a interface evita condições propensas a erro ou confirma ações arriscadas.
6. **Reconhecer em vez de lembrar:** opções e informações necessárias ficam visíveis quando úteis.
7. **Flexibilidade e eficiência:** atalhos e personalização ajudam o uso frequente sem atrapalhar iniciantes.
8. **Design estético e minimalista:** nada irrelevante compete com a informação essencial da tarefa.
9. **Reconhecer, diagnosticar e recuperar erros:** mensagens dizem o problema em linguagem clara e como continuar.
10. **Ajuda e documentação:** ajuda pesquisável, voltada à tarefa e próxima do contexto, quando necessária.

"Minimalista" não significa cortar informação necessária. Uma violação aparente pode ser uma
convenção que o público já conhece; nesse caso, registre-a só com impacto concreto na tarefa.

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

## 4. Hierarquia visual, layout e consistência

- A ação principal e a informação necessária para a tarefa se destacam na ordem certa.
- Tipografia, espaçamento, alinhamento e proximidade agrupam o que é relacionado e não sugerem
  relações falsas.
- A densidade combina com o conteúdo e o contexto de uso.
- Tokens, componentes, grade e padrões seguem o design system; aparência e imagens seguem o
  guia de marca, quando houver.
- Ícones e símbolos têm significado claro ou rótulo quando não forem convencionais.
- Dados e gráficos representam valores sem distorção, com unidade, legenda próxima, números
  alinhados para comparação e tabelas que permitem ordenar e acompanhar cabeçalhos.

Quando o problema vier de um componente ou regra do design system, indique isso na recomendação:
a correção pertence à origem, não só à tela.

## 5. Conteúdo, confiança e escolha

- Rótulos, botões e títulos dizem o que acontece, com termos consistentes.
- Mensagens de erro, confirmação e estados vazios explicam a situação e o próximo passo.
- Ações com consequências diferentes têm nomes diferentes; ações destrutivas deixam claro o efeito.
- Voz e tom seguem o guia de conteúdo, quando houver.
- Textos não prometem o que o produto não cumpre.
- Recusar, cancelar e excluir têm acesso e peso equivalentes a aceitar. A interface não usa:
  - opções pré-marcadas contra o interesse da pessoa;
  - urgência ou escassez falsas;
  - custos revelados tarde;
  - culpa na recusa;
  - pedidos repetidos após uma recusa;
  - consentimento enviesado.

Um padrão que leva a pessoa a escolher contra o próprio interesse causa dano, mesmo que
melhore uma métrica do produto. Para revisar ou reescrever textos, aplique a skill `escrever-claro`.

## 6. Estados, interação e adaptação

- Estados da jornada: carregando, vazio, parcial, sucesso, erro, sem permissão e indisponível.
- Entradas preservadas após erro, quando possível.
- Componentes interativos com estados distinguíveis: repouso, foco, *hover* onde houver
  ponteiro, pressionado, selecionado e desabilitado. Cada ação tem retorno imediato.
- Movimento que explica mudanças de estado, sem atrasar a tarefa.
- Tamanhos de tela e orientação, sem sobreposição nem perda de ações essenciais.
- Tema escuro, alto contraste e tamanho de texto do sistema, quando suportados.
- Conteúdo real e extremos: textos longos, listas vazias ou grandes.
- Em produtos localizados: idioma, direção da direita para a esquerda, formatos locais de data,
  número e moeda, e expansão de textos traduzidos.

## 7. Convenções da plataforma

Compare com as diretrizes vigentes da plataforma ou do sistema de componentes em uso, como
Apple Human Interface Guidelines, Material Design, Fluent ou um guia interno. Confira:

- **Entrada:** toque, ponteiro, teclado, controle ou voz; densidade e alvos adequados a ela.
- **Navegação do sistema:** voltar, gestos e menus. Na web: botão voltar do navegador, URLs que
  preservam o estado, links e botões com papéis distintos, preenchimento automático e zoom.
- **Janelas e áreas:** áreas seguras, teclado virtual, redimensionamento e várias janelas.
- **Recursos do sistema:** permissões pedidas no contexto de uso, notificações, atalhos,
  menus de contexto, arrastar e soltar.

Registre a URL, a data de consulta e a versão do sistema operacional, SDK ou biblioteca adotada.
Uma divergência deliberada e registrada pelo projeto entra em "Divergências deliberadas e riscos",
salvo impacto concreto na tarefa ou violação de um piso.

## Achado ou preferência

Um comentário é achado quando aponta:

- uma regra verificável, como heurística, critério WCAG, token, componente, guia de marca,
  grade ou especificação da plataforma; ou
- um princípio com mecanismo explícito, como proximidade que sugere relação falsa entre dois
  grupos.

O impacto pode atingir a tarefa, a compreensão, a confiança percebida ou a coerência do produto.
Um juízo sem regra nem mecanismo, como "parece datado", é sugestão de direção. Uma decisão
registrada do projeto, que não viola piso e cujo impacto ainda é incerto, vai para
"Divergências deliberadas e riscos". Nesse item, registre o risco e o teste que o confirmaria.

## Severidade

A nota descreve a consequência se o achado se confirmar. A certeza fica no campo Base, e o
esforço de correção não altera a nota. Combine:

- **frequência**, medida no grupo afetado;
- **impacto** na tarefa;
- **persistência**, isto é, se o problema continua atrapalhando depois de conhecido.

| Nota | Significado |
| --- | --- |
| 0 | Não é problema de uso. Usado ao reavaliar achados alheios; não registre achado próprio com 0. |
| 1 | Cosmético: perceptível, sem atraso nem erro na tarefa. |
| 2 | Menor: causa hesitação ou pequeno atraso; a pessoa se recupera sozinha, sem perda. |
| 3 | Maior: causa erro, atraso significativo ou abandono para parte do público; recuperar-se exige esforço ou ajuda. |
| 4 | Catastrófico: impede uma tarefa em escopo para algum grupo, ou causa perda de dados, dinheiro, privacidade ou segurança. |

Por política deste harness, uma barreira de acessibilidade que impede uma tarefa em escopo
recebe 4, mesmo que afete uma parcela pequena do público.

## Formato do achado

| Campo | Conteúdo |
| --- | --- |
| ID | Identificador curto e estável, como `CI-03`, para descartes, rodadas e novas versões. |
| Local | Tela, elemento ou `arquivo:linha`; liste todas as ocorrências. |
| Observação | O que a interface faz, descrito de forma verificável. |
| Padrões | Passo do percurso, heurística, critério WCAG com número e nível, regra do projeto ou da plataforma. |
| Impacto | Quem é afetado, em qual tarefa, e o que acontece. |
| Severidade | Nota de 0 a 4 e o motivo pela frequência, impacto e persistência. |
| Base | `observado`, quando visível ou medido no material examinado, inclusive em capturas; `inferido`, quando deduzido do código ou um comportamento não exercitado; `hipótese`, quando depende da reação das pessoas. Cite o material: captura, valor medido ou passos. |
| Recomendação | O padrão esperado, a lacuna atual e uma mudança concreta para fechá-la, indicando a origem quando for o design system. |

Exemplos de calibração, adapte ao caso:

- `CI-01`, severidade 3, base `observado` (passos 1–4 no app de teste): o botão "Continuar"
  do checkout fica desabilitado sem indicar o campo pendente. Viola as heurísticas 1 e 9.
  Quem não percebe o CEP vazio fica sem caminho e pode abandonar a compra. Recomendação:
  manter o botão ativo, mostrar o erro no campo e levar o foco até ele.
- `CI-02`, severidade 1, base `observado` (captura `cadastro.png`): os títulos das seções usam
  dois pesos diferentes. Viola a regra de tipografia do design system. O impacto é na coerência
  visual, sem atraso na tarefa. Recomendação: usar o token de título do design system.

## Fontes

- [10 heurísticas de usabilidade, Nielsen Norman Group](https://www.nngroup.com/articles/ten-usability-heuristics/)
  (revisão de 2024). Os resumos acima são próprios.
- [Escala de severidade, Nielsen Norman Group](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/).
  As definições das notas 1 a 3 e a regra de barreiras são escolhas deste harness.
- [Avaliação heurística, Nielsen Norman Group](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/).
- [Percurso cognitivo, Nielsen Norman Group](https://www.nngroup.com/articles/cognitive-walkthroughs/).
- [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/), recomendação de 12 de dezembro de 2024, e
  [WCAG2ICT](https://www.w3.org/TR/wcag2ict-22/), nota informativa para software que não é web.
- [Duan et al., CHI 2024](https://arxiv.org/abs/2403.13139): na comparação com especialistas
  humanos, o GPT-4 teve precisão menor (0,60 contra 0,83) e recall um pouco maior. Os erros mais
  comuns foram:
  - regras aplicadas sem considerar o contexto;
  - achados repetidos por elemento;
  - achados descartados reapresentados sob outra diretriz;
  - correções vagas;
  - leitura visual incorreta sem a interface renderizada.

  A utilidade das sugestões caiu ao longo das iterações de uma mesma interface. As regras de
  consistência respondem a esses erros. Essa aplicação é uma escolha do harness, sem medição de ganho.
