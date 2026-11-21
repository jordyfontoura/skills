---
name: criticar
description: Critica a qualidade de um artefato ou experiência com critérios especializados, evidências, prioridades e nota obrigatória com duas casas decimais. Use para pedir um crítico independente ou compor uma crítica com conselho; inclui notas por categoria quando pertinentes. Não corrige; para diff use `revisar` e para aceite use `verificar-aceite`.
license: Apache-2.0
---

# Criticar um artefato ou experiência

Avalie o objeto pedido com critérios declarados e evidências, sem corrigi-lo. Fixe objeto e
versão, público, intenção, foco, referências e ações permitidas, consultando decisões, críticas
anteriores e descartes antes de perguntar. Especializar a crítica não autoriza redefinir o
produto. Para escolher entre propostas, use `conselho`; para reescrever texto, `redigir`.

## Escolher o método e os critérios

Declare a especialização e os critérios antes do exame, combinando métodos quando o objeto exigir:

- **UI e UX**, inclusive a interface de jogos: leia [interface.md](interface.md) e siga a
  rubrica, com seus pisos, as sete seções e a escala de severidade.
- **Game design:** [mecânicas, ritmo, dificuldade e resposta ao jogador](../../../knowledge/gamedev/game-design.md).
- **Assets 3D para jogos:** [geometria, materiais, rig e requisitos de uso](../../../knowledge/3d-modeling/game-ready-assets.md).
- **Outros aspectos**, como direção de arte ou argumentação de um texto: critérios derivados
  do pedido, das referências, das regras do projeto e de princípios do domínio com mecanismo
  explícito. Para clareza de texto, consulte `redigir` sem reescrever.

Informe a origem e os limites dos critérios; uma rubrica criada para o caso não é padrão
validado. Use `consultar-conhecimento` para localizar outros guias e leia só os necessários.
Quando um julgamento depender de fonte externa, consulte-a com `pesquisar-web` ou declare a
origem não conferida. Pergunte apenas se uma definição ausente mudar o julgamento; nos demais
casos, declare suposições razoáveis.

## Preservar a independência

Quem produziu o objeto não apresenta sua autocrítica como independente. Uma crítica pontual
pode ocorrer no contexto atual se ele não produziu o objeto. Para um crítico independente ou
um ciclo produtor-crítico autorizado, use `delegar` com um contexto novo e forneça objeto,
versão, critérios, acesso, achados anteriores e decisões, sem a defesa nem a autoavaliação
de quem implementou.

Respeite o modelo escolhido. Havendo política local, a consulta usa `roles.council` conforme
`delegar`, mesmo com um só crítico. Sem contexto independente ou ferramenta adequada, declare
a crítica pendente ou limitada, sem simular outro especialista. Como crítico delegado, faça
só a sua análise, sem abrir novos agentes ou conselhos.

Quando o pedido incluir conselho, painel ou várias perspectivas independentes, leia
[panel.md](panel.md).

## Examinar e fundamentar

Examine a forma mais fiel disponível para cada critério: jogue, navegue, leia ou opere o
artefato, conforme autorizado, em ambiente de teste e dentro dos limites de ações com efeitos
reais. Para aparência, prefira a interface renderizada em uso, depois capturas, depois código.
Para acessibilidade, use também código, árvore de acessibilidade e tecnologia assistiva.
Medidas vêm do código, de estilos computados ou do arquivo de design; estimativas de captura
são aproximadas. Capturas não demonstram controles, persistência, cooperação ou áudio, e
código lido não comprova execução. Inspeção não substitui testes com o público, incluindo
pessoas com deficiência: indique as hipóteses de alto impacto ou incerteza que os exigem.
Registre passos, condições e materiais examinados; capacidade ou acesso ausentes são limites.

Fora da UI, cada achado traz localização, observação, critério ou mecanismo, impacto,
prioridade justificada pela consequência e pelo alcance, base e recomendação concreta, sem
a escala de UI; na UI, valem o formato e a severidade da rubrica. Em todo domínio, use IDs estáveis e marque a base como `observado`, `inferido`
ou `hipótese`, citando a evidência. Uma reação prevista do público não é comportamento
observado em pessoas.

Agrupe ocorrências do mesmo problema. Preserve descartes do usuário, salvo evidência nova
declarada. Numa nova versão, marque achados anteriores como resolvidos, persistentes ou
regressões e identifique os novos. Aponte também o que funciona e deve resistir às correções.

## Notas e ciclos de correção

Toda crítica realizada entrega uma nota geral de qualidade, na escala combinada ou, sem ela,
de 0 a 10. Escreva as notas com ponto e exatamente duas casas decimais: `9.73`, `7.00`, `0.00`;
o máximo da escala padrão é `10.00`. Havendo dimensões distintas relevantes, inclua notas por
categoria, como game design e estética, ou usabilidade e acessibilidade, respeitando as
categorias pedidas.

Fixe critérios e âncoras antes do exame, usando os combinados ou declarando os adotados.
Ligue cada nota às evidências, aos pontos fortes e aos problemas que a justificam e explique
a relação da nota geral com as categorias e os pesos. Não suponha média aritmética, e uma
nota alta não compensa uma exigência descumprida. As duas casas são formato, não precisão
estatística: declare cobertura e incerteza. Em exame parcial, a nota vale para a parte
examinada; sem material suficiente, declare a crítica não realizada em vez de dar nota.
Nota de qualidade e severidade são medidas distintas, e a severidade de UI continua de 0 a 4.
Não crie um limiar de aprovação por conta própria.

A crítica não edita o produto. Um ciclo de correção só prossegue com a implementação e as
novas avaliações autorizadas. Antes da primeira rodada, fixe critérios, limiar eventual, regra
de avaliação e condição de parada, com limite de rodadas quando combinado. Quem implementa
confere o feedback com `tratar-revisao`, corrige por prioridade e repete as provas afetadas:
as sugestões do crítico são meios a conferir, não requisitos. Cada nova crítica avalia a
versão resultante. Não repita a avaliação da mesma versão até obter nota favorável, não baixe
o limiar e não troque o crítico para aprovar; numa sequência de críticos ou metas crescentes,
use `subir-regua`, em que a troca ocorre depois da aprovação da etapa. Preserve versões recuperáveis para comparar;
a última não é automaticamente a melhor. Encerre ao cumprir os critérios ou atingir a condição
de parada, relatando notas, problemas e provas ausentes. Notas não substituem provas técnicas
nem `verificar-aceite`.

## Retornar

Responda em português, salvo pedido diferente, com:

- contexto, versão, especialização, critérios e formas de acesso;
- achados por prioridade, com evidências;
- o que preservar, e as divergências deliberadas e sugestões de direção, separadas dos achados;
- cobertura, limites e provas recomendadas;
- nota geral e notas por categoria pertinentes, com justificativas. A conclusão pelo limiar
  só existe quando ele foi combinado.

Num painel, preserve divergências e autoria dos achados. Sem problema relevante, diga isso
com a cobertura examinada.
