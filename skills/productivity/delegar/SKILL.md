---
name: delegar
description: Delega trabalho autorizado e delimitado com responsabilidade clara, ferramentas disponíveis e conferência do resultado.
license: Apache-2.0
---

# Delegar trabalho delimitado

Delegue apenas quando autorizado e quando houver uma parte independente, com dependências
satisfeitas, resultado e responsabilidade claros. Faça pequenas edições diretamente quando
explicá-las custar tanto quanto executá-las. Preserve os limites de permissão: revisão de
código não autoriza execução, edição nem novas delegações.

Num coordenador com contexto grande ou já compactado, essa conta muda: cada leitura, edição
ou saída de teste fica no contexto e é paga de novo em todas as chamadas seguintes. Nesse
caso, envie implementação, testes e leituras longas a contextos novos. O coordenador guarda
decisões, integração e estado. Um pedido explícito para trabalhar no próprio contexto prevalece.

Explique o ganho esperado da divisão: trabalho independente em paralelo, investigação com
saída volumosa, uma avaliação que precise de independência ou a preservação do contexto do
coordenador. Não delegue apenas por haver um papel configurado nem para repetir uma análise
já suficiente. Planejamento rotineiro e reparos delimitados podem permanecer com quem já tem
o contexto, enquanto ele for pequeno, respeitando o pedido.

## Escolher trabalho e ferramentas

Se o destino tiver `.agents/models.toml`, consulte a política e o guia local, quando houver, antes de
selecionar o modelo. Identifique a responsabilidade: `orchestrator`, `planner`, `implementer`,
`reviewer`, `evaluator`, `representative` ou `council`, conforme a tarefa, ou uma responsabilidade
adicional configurada pelo projeto. A escolha explícita do usuário no pedido atual prevalece.
Sem política local, preserve a seleção do ambiente e do usuário. A resolução não exige scripts:

- `version = 1`: combine `defaults` com os campos do papel e considere `fallbacks` em ordem.
  Complexidade não altera essa seleção.
- `version = 2`: leia `roles.<papel>.profile` e os `candidates` ordenados desse perfil. Quando
  o papel declarar `complexity.simple` ou `complexity.hard`, use o perfil indicado para esse nível.
  Sem mapa aplicável, mantenha o perfil base. `default` sempre usa o perfil base. O pedido pode
  fixar o nível; caso contrário, quem delega o classifica pelo trabalho, usando `default` sem
  motivo concreto para outra escolha. Registre a origem e se o nível mudou o perfil.
  `representative`, `evaluator` e `council` não aceitam mapas; não aplique a eles a complexidade
  da implementação. Outros papéis podem ter mapas para novos contextos autorizados.
- Uma versão, papel, perfil, campo ou nível desconhecido exige esclarecimento. Não invente
  vínculos por nomes iguais, misture formatos ou substitua referências ausentes. A v2 não tem
  `defaults` nem seleção direta nos papéis; candidatos exigem provedor, modelo e esforço,
  sem duplicação. Só o primeiro pode herdar provedor e modelo, sempre juntos.

Confira o candidato principal na ferramenta. Considere alternativas somente quando ele estiver
indisponível, na ordem de `candidates` (v2) ou `fallbacks` (v1), dentro da autorização atual. Uma falha na qualidade
do resultado não autoriza troca de modelo. Se nenhuma opção configurada puder executar,
relate a indisponibilidade; não invente substitutos. `inherit` preserva configurações herdadas
e não é o nome de um modelo. A política não troca o modelo da conversa nem autoriza delegar.

Leia requisitos e evidências relevantes. Confira acesso, ferramentas e modelos disponíveis
antes de iniciar. Respeite a escolha de provedor e modelo do usuário. Use somente configurações
suportadas e declare opções indisponíveis. Não diga que um modelo herdado foi o modelo pedido
nem troque de provedor sem informar.

Considere a consequência do erro ao propor uma seleção: trabalho mecânico pode justificar
um modelo mais leve; diagnóstico difícil, arquitetura e avaliação podem exigir raciocínio
maior ou ferramentas específicas. Use `simple` para trabalho mecânico delimitado e `hard`
para diagnóstico difícil ou arquitetura com consequências relevantes, quando houver mapa.
Essa classificação não substitui a política nem troca um candidato `inherit` por outro modelo.
Sem política, respeite as escolhas do usuário
e do ambiente, sem registro fixo de modelos nesta skill.
Leia [workloads.md](workloads.md) para trabalho recorrente, registros e comparações autorizadas.

## Preparar a tarefa

Inclua resultado esperado, requisitos, revisão das entradas, arquivos para ler, responsabilidade
por arquivos ou análise de leitura, ações permitidas, exclusões, provas exigidas e lacunas.
Informe modelo e esforço somente quando selecionados ou observados. Peça resultado, arquivos
alterados, evidências e incerteza restante.
Inclua responsabilidade, versão, perfil efetivo, complexidade e sua origem, se ela mudou
a seleção, e eventual alternativa usada. Na v1, dispense os campos que não existem.

Reutilize evidências já coletadas, com revisão, trechos relevantes e caminhos ou links de origem.
Separe fatos conferidos, interpretações e lacunas. Delimite a pergunta e o resultado necessário
em vez de pedir uma nova investigação geral a cada agente. Preserve a possibilidade de conferir
fontes e questionar premissas; fornecer um resumo não comprova que o agente validou a origem.
Para pareceres de `conselho`, a preparação é um ponto de partida: siga a prioridade de qualidade,
cobertura e investigação independente definida na skill, inclusive quando exigir novas leituras
ou ampliar a análise. Não limite o conselho ao resumo ou às conclusões do coordenador.

Para edições, diga ao agente que ele não está sozinho e precisa preservar mudanças alheias.
Distribua arquivos distintos ou use ambientes de trabalho isolados suportados; faça edições
em arquivos compartilhados em sequência. Preserve uma base recuperável. Enquanto o agente ou
processo executa, não duplique seu trabalho: guarde o identificador e a forma de receber o
resultado, avance trabalho independente e relate só mudanças de estado.

## Conferir o retorno

Verifique achados contra a fonte na revisão fixada. Um revisor em modo de leitura devolve
achados com referências; não aguarda implementação nem executa comandos proibidos.

Para uma entrega, inspecione o diff e confira o resultado registrado de cada prova: comando,
revisão e resultado observado. Dizer "concluído" não é evidência. Rode de novo só o que
faltar, estiver inconsistente ou tiver sido invalidado por mudanças posteriores. O aceite
independente, quando exigido, continua executando as próprias verificações.
Integre sem reverter trabalho alheio.
Devolva trabalho incompleto com uma tarefa menor. Após duas correções sem sucesso ou quando
variantes do mesmo defeito reaparecerem, use `diagnosticar`.

Quando útil, mantenha um registro conciso na conversa ou no documento de trabalho existente.
Separe configurações pedidas, configurações informadas pela ferramenta e fatos observados.
Uso não informado continua desconhecido.

Peça retornos concisos com achados, provas e limites, apontando para os registros existentes.
Conferir a origem não exige repetir toda a investigação: retome só o que faltar, estiver
inconsistente ou tiver sido invalidado.
