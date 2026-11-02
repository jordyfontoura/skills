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

Use os scripts, o executor de tarefas e a CI existentes quando disponíveis. Mantenha os
comandos executáveis diretamente no repositório. Num projeto de documentação, use checagens
proporcionais de estrutura, links e metadados. Não adicione ferramentas de aplicação apenas
por causa do harness.
Use `conhecer-ferramentas` para inventariar ferramentas e preparar faltantes quando essa instalação fizer
parte do pedido; isso não torna o catálogo de CLIs uma dependência obrigatória do projeto.

Atualize o índice de comandos em `AGENTS.md` e as instruções de CI e preparação relevantes.
Mantenha configurações de provedor no próprio provedor; procedimentos compartilhados ficam
na fonte canônica adotada pelo projeto. Não instale hooks, serviço em segundo plano ou banco de tarefas sem pedido
explícito. Preserve a preferência existente do projeto sobre hooks.

Documente limites úteis de arquitetura e pré-requisitos. Nunca copie segredos para worktrees
nem sobrescreva configurações alheias. Prepare worktrees com comandos reais do projeto e
copie somente arquivos autorizados pelo usuário.

Execute os comandos configurados. Corrija falhas dentro do escopo e relate pré-requisitos
ausentes, sem remover uma checagem útil. Explique o que foi verificado, o que falta e como
rodar as verificações sem um agente.
