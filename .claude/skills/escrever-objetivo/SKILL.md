---
name: escrever-objetivo
description: Escreve uma instrução de execução autônoma com escopo delimitado, referências e condição verificável de conclusão.
license: Apache-2.0
---

# Escrever um objetivo de execução

Entregue um texto pronto para colar, compatível com o limite do destino: menos de 4.000 caracteres
quando ele for desconhecido. Escrever o objetivo não inicia uma execução nem autoriza ações externas.

Inclua resultado, repositório, requisitos ou caminhos relevantes, critérios no escopo e como
consultá-los. Nomeie a etapa inicial e a última passagem de contexto. Uma continuação segue
essa etapa sem reabrir escolhas resolvidas. Aponte para requisitos em vez de copiar toda a especificação.

Descreva a condição observável de conclusão: critérios comprovados pelos métodos combinados,
verificações relevantes passando e aceite independente, se exigido. Implementação e avaliação
independente são distintas. Avaliação ou acesso ausentes continuam sem prova.

Declare limites de atuação, arquivos e worktree sob responsabilidade, exclusões e decisões
autorizadas. Use `implementar` para entrega, `delegar` para divisão autorizada e `verificar-aceite`
quando necessário. Respeite ferramentas e modelos escolhidos; não invente configurações
ou capacidades indisponíveis.
Se o destino tiver `.agents/models.toml`, aponte para a política e informe quais responsabilidades
serão usadas e que a seleção segue `delegar` (v1 ou v2), sem copiar a lista inteira para o objetivo.
Na v2, complexidade só muda um perfil por mapa explícito; preserve os perfis próprios de
representante, avaliador e conselho. Escrever o objetivo não altera a política
nem concede delegação. Sem esse arquivo, preserve as escolhas do usuário e do ambiente.

Uma execução autônoma autorizada pode usar o papel `representative`,
quando disponível, para escolhas sustentadas por evidências dentro da intenção
do usuário. Quem o consultou registra a decisão na conversa ou na documentação existente.
Ações fora da autorização ficam pendentes enquanto o trabalho independente continua.
Se o projeto já adota um arquivo de alinhamento, instrua a registrar ali as escolhas reservadas
ao usuário, seguindo `entrevistar-por-arquivo`: pergunta com ID estável, motivo e dependências, sem
preencher a resposta. Aponte para o arquivo no relato de pendências e continue o trabalho
independente autorizado. Não crie outro registro concorrente nem imponha um arquivo a quem
não usa esse fluxo. Quando só restarem bloqueios, preserve a condição de retomada em `passar-contexto`.
Quando a política existir, a consulta usa `roles.representative`. Defina quais escolhas podem
ser delegadas; a presença dessa tabela não concede representação. Preserve a autoria da decisão.
O representante não aprova em nome do usuário uma espera pedida por `propor`, salvo delegação
explícita daquela decisão. Uma dúvida ou aprovação parcial não libera todo o objetivo.

Após duas correções sem sucesso, use `diagnosticar`. Antes de encerrar o contexto, use `passar-contexto`
com o trabalho restante, as provas ausentes e as condições de retomada. Mostre o texto,
a contagem de caracteres e as exclusões. O usuário decide se vai executá-lo.
