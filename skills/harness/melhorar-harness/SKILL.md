---
name: improve-harness
description: Propõe uma melhoria concreta no harness a partir de dificuldades observadas, quando solicitado ou após erros repetidos. Não altera instruções compartilhadas sem autorização.
license: Apache-2.0
---

# Melhorar o harness a partir da sessão

Use a conversa, o diff relevante, os resultados das verificações e os registros existentes
para estabelecer o ocorrido. Separe a dificuldade observada da hipótese sobre sua causa.
Não inspecione transcrições privadas ou segredos para reconstruir uma sessão.

Para cada proposta, explique o incidente, a menor mudança que o evitaria e seu custo.
Prefira conectar uma verificação existente a acrescentar outra regra. Problemas de navegação
podem precisar de uma referência; erros mecânicos recorrentes, de uma checagem determinística;
decisões de julgamento, de um padrão curto. Remova orientação desatualizada ou duplicada
quando ela for a causa. Não transforme um caso isolado em política para todos os projetos.

Apresente apenas propostas que teriam mudado o resultado observado. Falta de verificações
é um achado, não autorização para alterar o harness. Aplique mudanças já autorizadas; nos
demais casos, apresente a proposta concreta para escolha do usuário. Não instale bloqueios
automáticos. Use `setup-harness` para configurar verificações dentro do escopo autorizado.

Se as skills vierem de um plugin, não edite o cache instalado: ele é substituído a cada versão.
Proponha a mudança nas instruções do projeto, como `AGENTS.md` ou `CLAUDE.md`, ou, com
autorização, uma issue ou PR na origem com o mesmo cenário.

Para verificar uma mudança de instruções, preserve um cenário do problema observado: pedido,
estado inicial, materiais necessários e resultado esperado. Use a conversa ou o documento de
trabalho existente, retirando dados privados. Inclua, quando relevante, um caso em que a skill
não deve agir; não invente uma falha anterior para justificar a mudança.

Quando viável e autorizado, execute o mesmo cenário antes e depois, em contextos novos com
entradas, ferramentas e configurações comparáveis. Use `delegate` se a prova exigir outro
agente e essa delegação estiver autorizada. Julgue o resultado e as ações observáveis, não
a repetição de palavras da skill ou um caminho único de ferramentas. Preserve tentativas,
limites e diferenças do ambiente nos registros existentes.

Se a comparação anterior ou a execução não forem possíveis, declare a lacuna. Leitura dos
cenários e validação de estrutura não demonstram mudança de comportamento. Uma execução
isolada não estabelece taxa de acerto; siga `evaluate` para critérios variáveis e aceite
independente, quando exigidos. Não crie serviço de avaliação ou uma suíte extensa por padrão.

Registre achados úteis na conversa ou na documentação existente. Preserve escolhas duráveis
com contexto e consequências, sem duplicar registros. Verifique uma mudança aplicada pelo
método pertinente e pelos comandos do projeto; uma proposta, sozinha, não é prova.

Inspirada em [retro, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md).
