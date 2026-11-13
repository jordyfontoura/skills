---
name: configurar-harness
description: Configura comandos, verificações e orientações de provedores para as tecnologias reais do projeto, dentro do escopo autorizado.
license: Apache-2.0
---

# Configurar o harness

Leia manifestos, arquivos de dependências fixadas, CI e instruções existentes para encontrar
os comandos reais de instalação, execução, formatação, lint, tipos e testes. Preserve
verificações úteis. Se uma escolha de tecnologia impedir a configuração, pergunte por ela
em vez de inventar um sistema de dependências.

Reconheça a rota de adoção do harness: plugin, cópias manuais ou CLI. Nas instalações pelo
CLI, preserve a biblioteca única em `knowledge/harness/`, compartilhada por Codex e Claude
Code, e os links das skills para ela. Consulte os recibos em `.harness/receipts/` para
identificar os componentes adotados; confira o conteúdo atual antes de concluir que ele
permanece igual ao registrado. Preserve os outros documentos de conhecimento do projeto.

Se configurar modelos fizer parte do pedido, use o comando `models init` do CLI adotado,
quando disponível, ou o exemplo neutro da coleção. O configurador cria apenas arquivos
ausentes; `--print` permite consultar uma proposta sem gravar. Preserve `.agents/models.toml`
existente, inclusive políticas v1, comentários e escolhas locais. Uma migração exige escopo
expresso. A validação estrutural não comprova disponibilidade de modelo ou esforço, não
altera a conversa aberta nem autoriza delegação. Não instale o CLI apenas por usar esta skill.

Use os scripts, o executor de tarefas e a CI existentes quando disponíveis. Mantenha os
comandos executáveis diretamente no repositório. Num projeto de documentação, use checagens
proporcionais de estrutura, links e metadados. Não adicione ferramentas de aplicação apenas
por causa do harness. Teste o validador com fixtures mínimas criadas pelo próprio teste,
separadas da verificação do repositório real, mantendo os casos que devem falhar, como links
quebrados. Valide a documentação real na própria árvore do repositório. Não mantenha listas
parciais de arquivos copiados para fazer a documentação passar nos testes.
Use `conhecer-ferramentas` para inventariar ferramentas e preparar faltantes quando essa instalação fizer
parte do pedido; isso não torna o catálogo de CLIs uma dependência obrigatória do projeto.

Atualize o índice de comandos em `AGENTS.md`, com a ordem de execução: validador do harness e
checagens rápidas antes das suítes longas. Atualize também as instruções de CI e preparação relevantes.
Mantenha configurações de provedor no próprio provedor; procedimentos compartilhados ficam
na fonte canônica adotada pelo projeto. Não instale hooks, serviço em segundo plano ou banco de tarefas sem pedido
explícito. Preserve a preferência existente do projeto sobre hooks.

Documente limites úteis de arquitetura e pré-requisitos. Prepare worktrees com comandos reais
do projeto, copiando só arquivos autorizados pelo usuário e nunca segredos; não sobrescreva configurações alheias.

Execute os comandos configurados. Corrija falhas dentro do escopo e relate pré-requisitos
ausentes, sem remover uma checagem útil. Explique o que foi verificado, o que falta e como
rodar as verificações sem um agente.
