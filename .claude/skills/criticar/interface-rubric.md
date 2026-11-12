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

Percorra as tarefas principais e de saída. Aplique os critérios de
[usabilidade](references/knowledge/ux/usability.md), incluindo o percurso cognitivo quando a
aprendizagem ou padrões pouco familiares importarem.

## 2. Heurísticas de usabilidade

Examine as dez heurísticas no mesmo guia de usabilidade, respeitando convenções do público.
Uma violação aparente precisa de impacto concreto na tarefa.

## 3. Acessibilidade

Use os [critérios por forma de acesso](references/knowledge/accessibility/interface-criteria.md).
Numa auditoria, percorra todos os critérios dos níveis da meta. Indique número e nível em
cada achado e registre como não examinados os itens que o acesso não permite verificar.
Uma inspeção parcial não declara conformidade; o piso desta rubrica continua obrigatório.

## 4. Hierarquia visual, layout e consistência

Compare com os critérios de [hierarquia, estados e conteúdo](references/knowledge/ux/states-and-content.md)
e o design system do projeto. Quando o problema vier de um componente ou regra compartilhada,
a recomendação aponta a origem, não apenas a tela.

## 5. Conteúdo, confiança e escolha

Examine os critérios de conteúdo e padrões enganosos do mesmo guia. Preserve o piso de
escolha da pessoa. Para revisar ou reescrever textos, aplique `escrever-claro`.

## 6. Estados, interação e adaptação

Exercite os estados e extremos pertinentes descritos no guia de hierarquia, estados e
conteúdo. Registre a cobertura e os limites de simulações, capturas e operação.

## 7. Convenções da plataforma

Use o [inventário de plataforma](references/knowledge/ux/platform-conventions.md) e confira
as diretrizes vigentes. Registre URL, data da consulta e versão do sistema, SDK ou biblioteca.
Uma divergência deliberada do projeto entra em "Divergências deliberadas e riscos", salvo
impacto concreto na tarefa ou violação de um piso.

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

- [Escala de severidade, Nielsen Norman Group](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/).
  As definições das notas 1 a 3 e a regra de barreiras são escolhas deste harness.
- [Avaliação heurística, Nielsen Norman Group](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/).
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
