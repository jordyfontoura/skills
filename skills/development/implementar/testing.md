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

Numa mudança pequena, rode as verificações relevantes e não acrescente campanha nem etapas
que o projeto não combinou. Relacione cada verificação ao comportamento e ao risco cobertos;
evite suítes sobrepostas que não acrescentem prova. Quando o trabalho combinar verificações
caras, revisão separada ou campanha completa, ordene-as pelo custo e pela chance de invalidar
o candidato: primeiro as rápidas,
como o validador do harness, tipos e lint, as regressões e as jornadas afetadas; depois a revisão
e o tratamento dos achados; por fim, a campanha completa no candidato estabilizado. Antes de
uma campanha cara, rode um caso mínimo que exercite a mesma preparação, fixtures e ambiente,
para que uma falha de preparação apareça logo. Não inicie a
campanha completa enquanto uma revisão ainda pode mudar o candidato. Uma revisão exploratória
pode correr antes, enquanto o código muda. Registre a revisão e as condições de cada resultado.
Quando houver alterações, identifique as provas afetadas e suas dependências; repita essas
provas e preserve as demais enquanto código, critérios, ambiente e entradas relevantes
continuarem aplicáveis. Uma execução pode atender a mais de uma obrigação quando essa relação
for explícita e preservar os controles de cada uma, sem exigir um novo plano para registrá-la.
Comandos obrigatórios continuam obrigatórios até uma mudança autorizada.

## Ler as saídas

Toda saída lida fica no contexto. Use o modo conciso do runner e salve o log longo em arquivo.
Leia o código de saída, as contagens e o trecho de cada falha; busque no log salvo só o que
esse trecho não explicar. Nunca declare aprovação sem código de saída e contagem de testes.
Zero testes executados não é aprovação. No git, comece por `--stat`, `--short` e `--oneline`
e abra o diff completo só dos arquivos que precisar ler.
