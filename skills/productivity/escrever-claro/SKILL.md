---
name: unslop
description: Escreve ou revisa textos para leitores, incluindo documentação, títulos, descrições de tarefas e PRs, com linguagem clara e preservação de fatos e voz. Conversa de rotina não exige uma revisão formal separada.
license: Apache-2.0; inclui material MIT descrito em LICENSE-pstack.txt
---

# Escrever com clareza

Textos genéricos e repetitivos dificultam a leitura. Cada frase deve dizer algo específico,
em palavras simples, uma vez.

Aplique ao redigir e editar textos para outras pessoas: títulos e corpo de documentos,
tarefas, PRs, e-mails e mensagens. Títulos e descrições curtos também merecem revisão de clareza.
Conversa de rotina não exige anunciar a skill. Clareza não determina a voz pessoal do usuário;
preserve amostras fornecidas e pergunte apenas quando uma preferência ausente mudar o resultado.

## Como aplicar

1. Leia o texto inteiro ou as instruções de redação. Identifique público, finalidade, idioma e tom.
2. Localize os sinais listados abaixo.
3. Reescreva esses trechos. Se nada restar depois de remover o excesso, apague a frase.
4. Compare com o original: fatos, números, nomes, links e ressalvas importantes continuam presentes
   e corretos.
5. Entregue o artefato pedido. Ao relatar uma edição, resuma mudanças úteis e informações pendentes,
   como alegação sem fonte ou benefício sem medida. Não acrescente comentários de edição dentro
   de um título, descrição ou mensagem destinada a uso direto.

Conclua quando uma segunda leitura não encontrar excesso e nenhuma informação verdadeira tiver sido perdida.

## Adaptar ao tipo de conteúdo

Use os critérios pertinentes ao objetivo do texto; os tipos podem se combinar. Os sinais
abaixo ajudam a revisar, mas não são proibições universais de palavras, tom ou formatação.

- **Técnico:** em documentação, instruções, tarefas e PRs, priorize o que o leitor precisa
  fazer ou verificar. Preserve comandos, contratos, pré-requisitos, ordem das ações e diferenças
  entre comportamento previsto e observado. Um tutorial ensina; uma instrução orienta uma
  tarefa; uma referência descreve; uma explicação apresenta motivos. Não imponha a mesma
  estrutura a todos. Para PRs, siga também `pull-request`.
- **Produto e interface:** em botões, formulários, ajuda e erros, deixe clara a ação, o estado
  ou a recuperação possível. Use termos consistentes com a interface e preserve condições
  importantes. Não encurte removendo o contexto necessário nem use cor ou posição como única
  identificação. Não invente funcionalidades ou resultados para melhorar a mensagem.
- **Comunicação:** em mensagens, e-mails e posts, explicite o propósito e a ação esperada,
  quando houver. Preserve cordialidade, humor, ritmo e marcas da voz quando contribuírem para
  a intenção e forem compatíveis com as preferências recebidas. Ajuste o tom à situação e ao
  público; não transforme toda mensagem em comunicado formal nem fabrique intimidade.
- **Analítico ou acadêmico:** em relatórios, pesquisas e argumentos, preserve fontes, métodos,
  limites e grau de certeza. Diferencie resultado, interpretação e recomendação. Uma ressalva
  como "pode indicar" pode expressar incerteza real; retire apenas a cautela vazia ou redundante.
  Não transforme associação em causa, hipótese em fato ou um resultado isolado em consenso.

## O que preservar

- Sentido, fatos, números, nomes, citações e links.
- Blocos de código, comandos, identificadores e mensagens de erro, caractere por caractere.
- A voz de quem escreveu: vocabulário, humor e tom. Você está editando, não substituindo a autoria.
- Termos da área, mesmo que pareçam difíceis.
- Estrutura útil: lista real, tabela real e sequência de passos.
- Uma ressalva honesta para incerteza. Clareza não é certeza artificial.

Um padrão só é um problema quando nada acrescenta. Preserve um travessão, uma enumeração
ou uma metáfora que um editor humano manteria.

## Sinais a revisar

### Frases sem informação

- **Benefício vago no fim.** "…, melhorando a confiabilidade e garantindo uma boa experiência."
  Declare a consequência medida ou corte.
- **Autoridade anônima.** "Especialistas afirmam", "estudos mostram", "é sabido".
  Identifique a fonte ou remova a alegação.
- **Serve para qualquer produto.** "Uma solução robusta e escalável para equipes modernas."
  Troque por mecanismo, número ou instrução, ou corte.
- **Sentimento no lugar de fato.** "Funciona maravilhosamente", "uma solução elegante".
  Diga o que faz.
- **Fecho entusiasmado.** "Uma iniciativa empolgante para o futuro." Termine no último fato
  ou na próxima ação.

### Vocabulário pronto

- **Palavras de modelo.** Em inglês: delve, crucial, pivotal, robust, seamless, comprehensive,
  leverage, utilize, enhance, foster, streamline, underscore, landscape, realm, tapestry,
  testament. Revise também additionally, furthermore e moreover abrindo frases repetidamente.
  Prefira palavras simples ou remova.
- **Verbo enfeitado.** "Serve como", "atua como", "se destaca como", "conta com".
  Use "é" ou "tem" quando bastar.
- **Negação seguida de afirmação.** "Não é apenas X, é Y." Diga Y.
- **Três por hábito.** Não imponha três adjetivos ou itens para dar sensação de completude.
- **Sinônimos para o mesmo objeto.** Não alterne "ferramenta", "solução" e "plataforma" sem motivo.
- **Intervalo falso.** "Do primeiro acesso à publicação" sem nada intermediário. Liste o que existe.
- **Metáforas vazias.** Paradigma, ecossistema, norte, alicerce e termos semelhantes precisam
  comunicar algo concreto; substitua-os quando só enfeitarem.
- **Código personificado.** "O analisador aceita com prazer", "a função sabe".
  Descreva o comportamento.
- **Aforismos e fragmentos retóricos.** "Simples. Rápido. Confiável." ou "Por que isso importa?"
  Declare o significado literal.

### Enchimento

- **Conectores longos.** "A fim de" vira "para"; "devido ao fato de que" vira "porque";
  "neste momento" vira "agora"; "é importante notar que" pode desaparecer.
- **Ressalvas empilhadas.** "Poderia talvez potencialmente" vira "pode", ou a condição exata.
- **Advérbio com verbo fraco.** "Melhora significativamente o desempenho" vira uma medida
  ou verbo concreto, como "reduz o tempo pela metade".
- **Passiva que esconde o agente.** "O arquivo é atualizado" vira "o hook atualiza o arquivo".
  Preserve a passiva quando o responsável for desconhecido ou irrelevante.
- **Frase densa.** Uma ideia por frase; divida o que obriga a reler.
- **Compressão excessiva.** Restaure artigos, verbos e definições de siglas. Setas não devem
  substituir a explicação de um raciocínio.

### Formatação decorativa

- **Travessões e parênteses em excesso.** Use vírgulas ou frases separadas para observações.
- **Dois-pontos como suspense.** "O resultado: mais velocidade." Reserve-os para introduzir
  listas, exemplos ou citações.
- **Negrito espalhado.** Não destaque todos os termos nem use rótulos que repetem o texto.
- **Títulos e listas numa resposta curta.** Três parágrafos podem dispensar seções.
- **Maiúsculas Em Cada Palavra Do Título.** Use maiúscula inicial conforme uma frase.
- **Emojis** em títulos, listas e commits: remova quando forem decoração.
- **Aspas tipográficas** em texto técnico: prefira aspas retas.

### Sobras de conversa

- **Aberturas e despedidas.** "Com certeza!", "Ótima pergunta", "Espero ter ajudado":
  corte quando nada acrescentarem.
- **Concordar ou elogiar antes de responder.** Responda.
- **Narrar o trabalho dentro do documento.** "Primeiro, vou analisar…":
  apresente o resultado.
- **Avisos sobre ser um modelo ou sobre limite de conhecimento.** Use apenas quando forem o assunto.

## Atenção ao português

Revise "vale ressaltar", "vale destacar", "é importante notar que", "além disso" abrindo
frases em sequência e "em suma" antes de repetir o que já foi dito. Diga o fato diretamente.

Revise "robusto", "crucial", "fundamental", "essencial", "abrangente", "inovador",
"no cenário atual", "mergulhar em" e "desempenha um papel" quando substituírem informação.
"Realizar a implementação" pode virar "implementar".

Corte gerúndios de benefício sem prova, como "…, garantindo…" e "…, permitindo…".
Aplique o mesmo cuidado a contrastes "não apenas… mas também", travessões decorativos,
títulos com maiúsculas em todas as palavras e fechos como "Fico à disposição".

Adaptada de [unslop e technical-writing, do pstack](https://github.com/cursor/plugins/tree/main/pstack/skills),
de Lauren Tan, sob licença MIT. O aviso de copyright e a permissão estão em
[LICENSE-pstack.txt](LICENSE-pstack.txt).
