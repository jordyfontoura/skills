# Rubrica de crítica de interface

Base comum para criticar interfaces em qualquer projeto. Percorra as seções nesta ordem, para
que críticas de pessoas ou execuções diferentes sejam comparáveis. Uma seção sem achados
continua registrada como examinada ou não examinada. As diretrizes do projeto e da plataforma
prevalecem sobre esta base quando forem mais específicas.

## 1. Tarefas e fluxos

Para cada tarefa principal, percorra os passos como alguém do público definido. Em cada passo,
pergunte (percurso cognitivo, ou *cognitive walkthrough*):

1. **Intenção:** a pessoa tentará alcançar o resultado certo neste passo?
2. **Visibilidade:** ela perceberá que a ação correta está disponível?
3. **Associação:** ela ligará essa ação ao resultado que deseja?
4. **Retorno:** depois de agir, perceberá que avançou em direção ao objetivo?

Uma resposta "não" indica um achado no passo. Registre também desvios, becos sem saída,
etapas desnecessárias e perda de dados ao voltar ou cancelar.

## 2. Heurísticas de usabilidade

Examine a interface pelas 10 heurísticas de Nielsen:

1. **Visibilidade do estado do sistema:** o sistema informa o que está acontecendo, a tempo.
2. **Correspondência com o mundo real:** usa a linguagem e as convenções do público, não jargão interno.
3. **Controle e liberdade:** há como desfazer, refazer, cancelar e sair de um caminho indesejado.
4. **Consistência e padrões:** termos, ações e aparência se mantêm no produto e seguem convenções da plataforma.
5. **Prevenção de erros:** a interface evita condições propensas a erro ou confirma ações arriscadas.
6. **Reconhecer em vez de lembrar:** opções e informações necessárias ficam visíveis quando úteis.
7. **Flexibilidade e eficiência:** atalhos e personalização ajudam o uso frequente sem atrapalhar iniciantes.
8. **Design estético e minimalista:** nada irrelevante compete com a informação essencial da tarefa.
9. **Reconhecer, diagnosticar e recuperar erros:** mensagens dizem o problema em linguagem clara e como continuar.
10. **Ajuda e documentação:** ajuda pesquisável, voltada à tarefa e próxima do contexto, quando necessária.

"Minimalista" não significa cortar informação necessária. Uma violação aparente pode ser
uma convenção que o público já conhece; nesse caso, não registre o achado sem impacto observado.

## 3. Acessibilidade

Use a WCAG 2.2 nível AA como referência mínima, salvo meta diferente do projeto. Separe o que
a forma de acesso permite examinar:

- **Verificável por inspeção do código ou da tela:** texto alternativo de imagens informativas,
  nomes acessíveis de controles, rótulos ligados a campos, estrutura de títulos e regiões,
  idioma da página, informação que não depende só de cor, contraste calculado a partir dos
  valores reais de cor, foco visível declarado, área de toque (critério 2.5.8) e alternativas
  a gestos de arrastar (2.5.7).
- **Verificável ao operar a interface:** navegação completa por teclado, ordem de foco, foco não
  encoberto por elementos fixos (2.4.11), armadilhas de foco, reflow em 320 px de largura CSS,
  ampliação de texto, mensagens de status, tempo limite e movimento reduzido.
- **Exige ferramenta ou teste específico:** comportamento com leitores de tela, tecnologias
  assistivas reais e auditoria completa de conformidade.

Registre como não examinado o que a forma de acesso não permitiu verificar. Uma inspeção não
declara conformidade com a WCAG.

## 4. Hierarquia visual, layout e consistência

- A ação principal e a informação necessária para a tarefa se destacam na ordem certa.
- Tipografia, espaçamento, alinhamento e contraste organizam grupos relacionados.
- A densidade combina com o conteúdo e o contexto de uso.
- Tokens, componentes e padrões seguem o design system do projeto; variações têm motivo.
- Ícones e símbolos têm significado claro ou rótulo quando não forem convencionais.

Separe problemas que afetam a tarefa de preferências estéticas. Uma preferência entra como
sugestão de direção, nunca como achado.

## 5. Conteúdo e textos da interface

- Rótulos, botões e títulos dizem o que acontece, com termos consistentes.
- Mensagens de erro, confirmação e estados vazios explicam a situação e o próximo passo.
- Ações com consequências diferentes têm nomes diferentes; ações destrutivas deixam claro o efeito.
- Textos não prometem o que o produto não cumpre.

Para revisar ou reescrever esses textos, aplique a skill `escrever-claro`.

## 6. Estados e adaptação

- Estados relevantes à jornada: carregando, vazio, parcial, sucesso, erro, sem permissão e
  indisponível.
- Entradas do usuário preservadas após erro, quando possível.
- Tamanhos de tela, orientação e modos combinados (por exemplo, claro e escuro), sem sobreposição
  nem perda de ações essenciais.
- Conteúdo real e extremos: textos longos, listas vazias ou grandes, nomes em outros idiomas.

## 7. Convenções da plataforma

Quando a interface pertence a uma plataforma ou design system com diretrizes próprias, como
Apple Human Interface Guidelines, Material Design ou um guia interno, compare com a versão vigente
dessas diretrizes. Registre qual documento e versão foram consultados. Divergências deliberadas
do projeto não são achados se a decisão estiver registrada e não causar problema de uso observado.

## Severidade

Atribua uma nota de 0 a 4 a cada achado, combinando frequência (quantas pessoas e com que
regularidade encontram o problema), impacto (quanto atrapalha concluir a tarefa) e persistência
(se continua atrapalhando depois de conhecido):

| Nota | Significado | Prioridade |
| --- | --- | --- |
| 0 | Não é problema de uso. | Não registrar como achado. |
| 1 | Cosmético. | Corrigir se houver tempo. |
| 2 | Menor. | Baixa prioridade. |
| 3 | Maior. | Alta prioridade. |
| 4 | Catastrófico: impede a tarefa ou causa dano. | Corrigir antes de lançar. |

Uma barreira que impede um grupo de pessoas de concluir a tarefa, como um controle inoperável
por teclado, recebe nota 4 mesmo que afete uma parcela pequena do público.

## Formato do achado

| Campo | Conteúdo |
| --- | --- |
| Local | Tela, elemento ou `arquivo:linha`; liste todas as ocorrências de um achado repetido. |
| Observação | O que a interface faz, descrito de forma verificável. |
| Padrão | Passo do percurso, heurística, critério da WCAG, regra do design system ou da plataforma. |
| Impacto | Quem é afetado, em qual tarefa, e o que acontece. |
| Severidade | Nota de 0 a 4 e o motivo pela frequência, impacto e persistência. |
| Evidência | `observado` na interface renderizada ou em uso; `inferido` do código ou de capturas; `hipótese` a confirmar. |
| Recomendação | O padrão esperado, a lacuna atual e uma mudança concreta para fechá-la. |

## Fontes

- [10 heurísticas de usabilidade, Nielsen Norman Group](https://www.nngroup.com/articles/ten-usability-heuristics/)
  (revisão de 2024). Os resumos acima são próprios.
- [Escala de severidade, Nielsen Norman Group](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/).
- [Percurso cognitivo, Nielsen Norman Group](https://www.nngroup.com/articles/cognitive-walkthroughs/).
- [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/), recomendação de 12 de dezembro de 2024.
- [Duan et al., CHI 2024](https://arxiv.org/abs/2403.13139): numa avaliação de 51 interfaces,
  o GPT-4 teve precisão menor que a de especialistas humanos. Os erros mais comuns foram regras
  aplicadas sem considerar o contexto, achados repetidos por elemento, achados descartados
  reapresentados sob outra diretriz, correções vagas e leitura visual incorreta sem a interface
  renderizada. Feedback ancorado em diretrizes explícitas foi mais útil. As regras de consistência
  da skill respondem a esses erros. Essa aplicação é uma escolha do harness, sem medição de ganho.
