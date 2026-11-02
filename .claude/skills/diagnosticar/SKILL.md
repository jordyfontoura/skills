---
name: diagnose
description: Reproduz e investiga falhas, instabilidade ou lentidão sem causa conhecida, inclusive após duas tentativas de correção sem sucesso.
license: Apache-2.0
---

# Diagnosticar uma falha

Avalie primeiro o impacto. Se houver dano em curso, priorize uma mitigação dentro da autorização
existente, preservando evidências antes de alterá-las quando possível. Não aguarde a causa
completa para conter um incidente, mas não trate restauração do serviço como causa demonstrada
ou correção definitiva. Sem autorização para mitigar, relate o limite e investigue por meios permitidos.

Encontre um sinal reproduzível do sintoma antes de escolher a correção definitiva: teste, cenário CLI/HTTP,
interação na interface, repetição de uma sequência ou script específico. Confirme que a falha
ocorre pelo motivo esperado. Para instabilidade, registre frequência e condições de ocorrência.
Para desempenho, registre uma medição inicial e o limite esperado antes de alterar o código.

Para regressões, compare com a última revisão conhecida que funcionava e examine mudanças
recentes de código, configuração, dependências e carga. Quando houver histórico e um sinal
confiável, use bisseção em ambiente autorizado sem descartar alterações locais. Proximidade
temporal ou um commit suspeito são pistas, não prova da causa.

Reduza o cenário sem perder o sintoma. Ordene causas possíveis pelas evidências e descreva
uma previsão que permita distinguir cada hipótese. Investigue uma variável por vez, usando
logs direcionados, depurador ou medições. Preserve tentativas sem sucesso para que outra sessão
não as repita. Se faltar acesso para reproduzir, registre a lacuna e busque evidências
independentes, sem adivinhar nem iniciar uma campanha ampla de testes.

Corrija a causa e, quando viável, mantenha um teste de regressão no ponto que a alcança.
Repita o gatilho original e as verificações relevantes do projeto. Remova a instrumentação
temporária e explique por que uma reprodução não pode virar um teste durável, quando for o caso.
Nunca enfraqueça uma verificação para fazê-la passar.
Registre alterações temporárias feitas durante a investigação e como revertê-las. Restaure
apenas as suas mudanças temporárias que não fazem parte da correção, preservando trabalho
alheio e mitigações ainda necessárias. Declare o estado final e qualquer alteração mantida.

Registre sintoma, reprodução, causa demonstrada e tentativas na conversa ou no documento de
trabalho existente. Prove requisitos pelos métodos combinados. Sem prova, não há aprovação.
Relate falhas alheias ao pedido sem ampliar o escopo. Use `handoff` se a investigação continuar.

Informe a causa observada, a reprodução antes e depois, a correção e a incerteza restante.
Não inclua credenciais ou conteúdo privado nos registros e na resposta.

Inspirada em [diagnosing-bugs, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md).
