---
name: verificar-aceite
description: Verifica critérios de aceite de forma independente e relata evidências sem implementar correções.
license: Apache-2.0
---

# Verificar o aceite

Leia requisitos, tarefas, critérios, decisões, revisão fixada e achados anteriores.
Julgue apenas o escopo aprovado e os requisitos aplicáveis. Você precisa ser independente
da implementação; verificar o próprio trabalho não comprova aceite independente.

Use a versão autorizada vigente na fonte oficial do projeto, preservando a referência às
substituições. Uma mudança de critério ou método exige conferir a aplicabilidade das provas;
resultado de uma versão anterior não aprova automaticamente a nova. Relacione o resultado
às referências dos critérios existentes, sem criar outro registro concorrente de estado.

Quando a delegação estiver autorizada, use um contexto novo com o papel `evaluator`,
quando disponível. Forneça revisão fixada, passos de prova, instruções de execução
e limites de permissão. Siga `delegar` e relate configurações reais de modelo e ferramentas,
quando expostas. Se não puder executar um contexto independente adequado, declare o aceite
como não comprovado.
Se existir uma política em `.agents/models.toml`, quem inicia a avaliação resolve
`roles.evaluator` seguindo `delegar`: perfil próprio na v2, campos e alternativas na v1,
sem substituição pela complexidade da implementação. Respeite a seleção explícita do pedido.
Configurar esse papel não comprova que o modelo executou nem permite dispensar a independência ou as provas.

Um pedido só de análise de código pertence a `revisar`. Não execute além das permissões.
Para avaliação em execução, exercite cada critério pelo método declarado e rode as verificações
exigidas na revisão fixada, na ordem do apoio `testing.md` da skill `implementar`: rápidas e
jornadas afetadas antes da campanha completa. Inclua caminhos relevantes de falha e examine testes alterados em busca de asserções
enfraquecidas. Não edite código, testes, configuração ou critérios, nem delegue correções.

Para trabalho interativo ou integrado, percorra a jornada real coberta pelos critérios:
comece pela entrada normal, alcance a funcionalidade e conclua a ação esperada. Use os
controles reais e confira o resultado visível e a persistência relevante. Um teste isolado
de componente ou uma chamada direta de API não comprovam, sozinhos, o fluxo da interface.
Escolha estados e tamanhos de tela a partir do escopo combinado, sem inventar requisitos.

Repita falhas relatadas pelo gatilho original, incluindo navegação ou transições que quebraram.
Compare comportamentos de protótipos aprovados quando houver exigência de fidelidade.
Registre revisão, ambiente, entradas e passos para não confundir a prova com outra versão.
Se faltar acesso à execução, identifique a jornada não testada; checagens estáticas não a aprovam.

Para critérios instáveis ou dependentes de modelo, combine repetições proporcionais ao risco,
condições comparáveis e uma regra de aceite antes de executar. Registre o resultado de cada
tentativa e o total realizado, incluindo falhas; não repita apenas até obter um sucesso.
Uma passagem não demonstra estabilidade, e uma amostra pequena não estabelece taxa geral
de acerto. Reinicie o estado entre tentativas quando isso fizer parte do cenário, sem apagar
evidências. Não imponha repetições a critérios determinísticos simples.

Se o requisito não definir confiabilidade ou repetições, diferencie o comportamento observado
da estabilidade ainda não comprovada; esclareça apenas quando essa escolha mudar o aceite.
Não invente um limite, altere o critério depois dos resultados nem aprove a propriedade ausente.

Retorne a revisão avaliada e o resultado de cada critério: aprovado, reprovado ou sem prova,
com comandos ou observações exatos. Relate esperado e observado, reprodução, escopo da
correção e acesso ausente. Use `PASS` apenas com provas para todos os critérios exigidos;
caso contrário, use `FAIL` ou `UNPROVED`, conforme o caso, explicando em português.

Mantenha o resultado na conversa ou no documento de avaliação existente. Preserve falhas
anteriores ao registrar nova avaliação. Corrigir pertence a outro contexto; um resultado
novo exige prova nova.
