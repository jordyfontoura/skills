---
name: toolbox
description: Explica e seleciona ferramentas CLI, inventaria o ambiente e prepara as faltantes quando a instalação estiver autorizada. Perguntas explicativas e inventários não autorizam instalar ou configurar.
license: Apache-2.0
---

# Conhecer e preparar ferramentas

Identifique a intenção: explicar uma ferramenta, conferir o ambiente ou preparar ferramentas
para uma tarefa. Leia [tools.md](tools.md) apenas nas partes relevantes. Não transforme uma
pergunta explicativa em instalação nem tente instalar todo o catálogo.

## Explicar e escolher

Relacione a ferramenta à tarefa, ao sistema operacional e às opções já disponíveis. Explique
o que ela resolve, suas limitações e um exemplo concreto. Diferencie CLI, recurso nativo do
agente, servidor MCP e extensão. Respeite a preferência do usuário e as ferramentas exigidas
pelo ambiente; uma CLI não autoriza contornar restrições do provedor.

O catálogo é referência, não inventário vivo nem prova de disponibilidade. Para versões,
pacotes ou requisitos atuais, confira a documentação oficial e o gerenciador apropriado.
Só explicar não exige varrer a máquina inteira ou executar comandos que alterem estado.

## Inventariar sem alterar

Confira apenas as ferramentas pertinentes. No Windows, comece por `Get-Command`; em sistemas
compatíveis, use `command -v`. Confirme caminho resolvido, versão e escopo de instalação
quando disponíveis. Uma ausência no PATH não prova que o programa não está instalado:
considere instalações locais e o gerenciador já adotado antes de duplicá-lo.

Separe presença, executável funcional e capacidade testada. Uma CLI pode responder à versão
e ainda depender de navegador, índice, autenticação ou modelos. Um inventário não configura
esses recursos, baixa pacotes nem inicia serviços. Não leia segredos, arquivos `.env` ou
configurações completas que possam expor credenciais para detectar uma ferramenta.

## Preparar dentro da autorização

Antes de mudar o ambiente, identifique pacote exato e fonte oficial, versão compatível,
gerenciador, escopo local ou do usuário, dependências e efeitos em PATH, índices ou downloads.
Reutilize o que funciona; não atualize, substitua ou remova instalações por padrão. Considere
que ferramentas globais de um gerenciador de Node podem pertencer à versão ativa do runtime.

Confira a autorização existente. Se ela já cobre as ferramentas e os efeitos necessários,
prossiga sem pedir a mesma aprovação. Caso contrário, apresente o lote concreto, os efeitos
e a prova planejada, obtenha aprovação e aguarde antes de executar a parte dependente.
Silêncio ou aprovação de uma explicação não autorizam instalar. Um representante só pode
decidir isso se aquela decisão estiver explicitamente dentro da representação concedida.

Use o gerenciador existente e os procedimentos oficiais, registrando os comandos reais.
Não altere políticas de execução, verificações de instalação, hooks ou permissões para
fazer um comando passar. Se uma etapa for bloqueada, diagnostique: confirme se a ferramenta
já funciona ou explique a dependência que falta, sem conceder uma liberação global por conveniência.

Instalar uma CLI não inclui instalar suas skills, extensões, hooks, serviços ou servidores MCP.
Navegadores, modelos grandes e indexação de dados têm efeitos próprios: explicite-os no lote
quando forem necessários. Use diretórios e coleções delimitados ao escopo autorizado; preserve
índices e configurações existentes, inclusive os de outros projetos.

## Provar e registrar

Repita a descoberta e a versão após instalar. Quando autorizado, faça um teste funcional mínimo
com entradas conhecidas, sem mutações fora do escopo. Preserve evidências, feche sessões e
servidores temporários que você abriu, e informe qualquer recurso que permaneça configurado.

Relate o que já existia, o que instalou ou configurou, versões e origem, teste e resultado,
e o que continua ausente ou não verificado. Uma segunda execução com o ambiente adequado
deve reutilizá-lo, sem reinstalar. Use a conversa ou o documento de adoção existente; não crie
um serviço de inventário. `setup-harness` configura os comandos do projeto; esta skill prepara
as ferramentas necessárias, sem torná-las dependências obrigatórias das demais skills.
