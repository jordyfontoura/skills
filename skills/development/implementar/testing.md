# Escolher provas úteis

Leia ao escolher o método de um critério de aceite, adicionar testes ou ordenar verificações.

## Relacionar evidência e critério

- `test`: execute uma asserção automatizada de comportamento por uma interface pública.
  Use para cálculos, estado, permissões e regressões que precisam de proteção repetível.
- `run`: percorra o fluxo em execução e registre entradas, ações e saída observada.
- `visual`: inspecione capturas novas nos tamanhos combinados; preserve as imagens
  e descreva o que realmente foi examinado.
- `measure`: registre medição, condições, amostragem e limite esperado.
- `manual`: identifique a avaliação humana necessária e mantenha o resultado sem prova
  até que ela seja fornecida.

Teste passando não comprova aparência, e leitura de código não comprova execução.
Escolha o método pela consequência da falha. Uma edição reversível de texto raramente
exige teste novo; um risco de perda de dados exige mais que uma captura de tela.
Não altere silenciosamente um método aprovado. Ferramenta ou observação ausentes são prova ausente.

## Escolher o ponto de verificação

Um teste observa função pública, CLI, endpoint HTTP ou interação renderizada. Escolha o ponto
mais externo que alcance o critério mantendo execução prática e determinística.
Use testes mais específicos para lógica com muitos casos. Declare os limites dessa escolha
quando forem relevantes.

Resultados esperados vêm do requisito, de exemplo resolvido ou de referência independente,
nunca da repetição da implementação. Evite simulações internas e estado privado que façam
testes de comportamento falhar em refatorações inofensivas. Substitua sistemas externos lentos
ou incontroláveis quando útil; use componentes reais próprios para provar a integração.

## Criar uma regressão útil

Para um bug, reproduza primeiro e confirme que o sinal falha pelo motivo correto.
Mantenha a reprodução rápida o suficiente para orientar a correção. Converta-a em cobertura
quando existir um ponto estável de teste, corrija a causa e repita regressão e gatilho original.
Nos demais trabalhos, siga a sequência combinada do projeto, sem impor testes sempre antes ou sempre depois.

Nunca enfraqueça nem remova uma verificação só para passar. Se um teste contrariar um requisito
aprovado, explique a contradição e corrija o teste explicitamente. Registre comando e resultado
útil junto do requisito ou dos registros existentes. Scripts e asserções não executados
não são evidências.

## Ordenar a execução

Ordene as verificações pelo custo e pela chance de invalidar o candidato: primeiro as rápidas,
como o validador do harness, tipos e lint, as regressões e as jornadas afetadas; depois a revisão
e o tratamento dos achados; por fim, a campanha completa no candidato estabilizado. Não inicie a
campanha completa enquanto uma revisão ainda pode mudar o candidato. Uma revisão exploratória
pode correr antes, enquanto o código muda. Um resultado vale para a revisão em que foi obtido;
reaproveite-o enquanto ela não mudar. Uma execução atende a mais de uma obrigação só quando
preserva os controles de cada uma e essa combinação consta do plano. Comandos obrigatórios
continuam obrigatórios até uma mudança autorizada.
