---
name: melhorar-harness
description: Analisa o histórico de conversas do projeto para encontrar erros frequentes, gasto alto de tokens e de tempo e atrito na estrutura do harness, e entrega um relatório HTML com dados medidos e propostas de melhoria. Use quando pedirem para melhorar o harness, examinar eficiência, custo ou erros recorrentes, ou após erros repetidos. Não altera instruções compartilhadas sem autorização.
license: Apache-2.0
---

# Melhorar o harness a partir do histórico

Responda, com dados medidos, onde o trabalho com os agentes neste projeto falha, demora ou
gasta demais, e qual a menor mudança no harness que evitaria cada caso. O resultado é um
relatório HTML com os dados, os achados e as propostas. Propor não autoriza aplicar.

## Medir o histórico

Invocar esta skill autoriza ler os registros locais de conversas deste projeto, no período
analisado: 30 dias, salvo pedido diferente. Não leia conversas de outros projetos, segredos
nem arquivos `.env`. Rode o coletor [history.py](history.py), que acompanha esta skill e usa
só a biblioteca padrão do Python 3.11+:

```text
python <pasta desta skill>/history.py collect --project . --days 30 --data <dados.json>
```

Grave os dados e o relatório fora do versionamento, numa pasta ignorada do projeto ou numa
pasta temporária. O coletor lê as conversas do Claude Code e do Codex cujo diretório de
trabalho é o projeto ou um worktree dele; use `--worktree` para worktrees já removidos. Ele
mede, por conversa e no total: pedidos, tempo em turnos, tokens por tipo, custo registrado,
chamadas e erros de ferramenta, skills usadas, arquivos relidos, comandos repetidos,
compactações e interrupções.

Sem Python ou sem registros de um agente suportado, diga o que faltou e analise só a conversa
atual, sem números estimados. Todo número do relatório vem dos dados coletados ou de um
comando citado. Contagem de mensagens ou de chamadas não mede tokens; tokens processados não
medem custo nem cota; e o custo registrado cobre só as conversas em que o agente o grava.

## Encontrar as causas

Os dados indicam onde olhar; a causa está na conversa. Parta dos maiores valores, como as
conversas mais caras, os erros com mais ocorrências e as skills presentes nas conversas mais
longas, e abra os registros dessas conversas, pelo caminho em `path`, para ver o que aconteceu.
Leia o trecho necessário, não a conversa inteira. Uma skill presente numa conversa cara não
demonstra que ela causou o gasto.

Examine as causas que a evidência sustenta, sem preencher uma lista fixa:

- **Erros recorrentes:** o mesmo comando ou ferramenta falhando do mesmo modo em várias
  conversas, como sintaxe do shell errado, caminho inexistente ou verificação desconhecida.
- **Contexto inflado:** releituras do mesmo arquivo, saídas longas, buscas amplas ou
  instruções sempre carregadas que o caso não usa.
- **Retrabalho:** requisito ambíguo, decisão reaberta, correção desfeita, interrupções ou
  rodadas de revisão causadas por critério ausente no início.
- **Delegação:** subagente para consulta curta, modelo acima da complexidade ou briefing
  incompleto que gerou nova rodada.
- **Verificações e esperas:** suíte lenta repetida com resultado ainda válido, polling ou
  tempo limite sem diagnóstico.
- **Estrutura do harness:** skills que se sobrepõem ou se contradizem, uma skill que exige
  passos desnecessários para o caso, orientação desatualizada ou duplicada, ou um pedido
  recorrente que nenhuma skill atende.

Para a estrutura, siga um pedido real do histórico da descrição que o acionou até as
instruções que o agente carregou, em vez de julgar pelas quantidades. Tamanho, número de
skills e frequência de uso são pistas, não defeitos.

Marque cada causa como observada, quando o registro a mostra, ou inferida. Um sinal isolado
não demonstra a causa, e um caso isolado não vira política para todos os projetos.

## Propor

Apresente apenas propostas que teriam mudado um resultado observado. Para cada uma, dê a
evidência com sua fonte, a causa, a menor mudança que a evitaria e o custo ou risco dessa
mudança. Prefira conectar uma verificação existente a acrescentar uma regra. Problemas de
navegação podem precisar de uma referência; erros mecânicos recorrentes, de uma checagem
determinística; decisões de julgamento, de um padrão curto. Considere manter o estado atual
e, quando houver indício de custo ou obsolescência, simplificar ou retirar um componente.

Não proponha remover verificações úteis, provas, aceite independente ou perspectivas de
`conselho` só para economizar. Economia não autoriza mudar escopo, modelo ou provedor
escolhidos. Uma proposta não demonstra a melhoria: sem execuções comparadas, o ganho é hipótese.

## Entregar o relatório

Grave os achados num JSON e gere o relatório:

```json
{
  "summary": "Resumo em uma ou duas frases.",
  "findings": [{
    "title": "Achado", "impact": "Quanto pesou, com o número medido",
    "evidence": "O que os dados e a conversa mostram", "source": "Tabela, conversa ou comando",
    "cause": "Causa", "cause_kind": "observada",
    "proposal": "Menor mudança", "cost": "Custo ou risco", "owner": "Quem pode aplicar"
  }],
  "unknowns": ["O que não foi possível medir e o que permitiria medir."]
}
```

```text
python <pasta desta skill>/history.py render --data <dados.json> --findings <achados.json> --out <relatorio.html>
```

Ordene os achados pelo impacto medido; `cause_kind` é `observada` ou `inferida`. Não copie
para o relatório trechos privados das conversas além do necessário para identificar o caso.
Se os dados não sustentarem nenhuma melhoria, entregue o relatório com a lista vazia e diga
isso. Na conversa, informe o caminho do relatório, o período, as fontes lidas e os achados
principais em poucas linhas.

## Aplicar e verificar

Aplique mudanças já autorizadas; nas demais, aguarde a escolha do usuário. Falta de
verificações é um achado, não autorização para alterar o harness. Não instale bloqueios
automáticos. Use `configurar-harness` para configurar verificações no escopo autorizado.
Se as skills vierem de um plugin, não edite o cache instalado, substituído a cada versão:
proponha a mudança nas instruções do projeto ou, com autorização, uma issue ou PR na origem.

Para verificar uma mudança de instruções, preserve um cenário do problema observado: pedido,
estado inicial, materiais e resultado esperado, sem dados privados. Inclua, quando relevante,
um caso em que a skill não deve agir. Quando viável e autorizado, execute o mesmo cenário
antes e depois, em contextos novos e comparáveis, mudando um componente por vez; use `delegar`
se a prova exigir outro agente. Julgue o resultado e as ações observáveis, não a repetição de
palavras da skill. Se a comparação não for possível, declare a lacuna: leitura e validação
de estrutura não demonstram mudança de comportamento, e uma execução isolada não estabelece
taxa de acerto. Rodar o coletor de novo após um período comparável mostra a tendência, não a causa.
