# Escolher e observar o trabalho

Use esta referência para trabalho recorrente, seleção de capacidades e comparações autorizadas de modelos.

Para escolher CLIs ou conferir sua disponibilidade, use `conhecer-ferramentas`. Aproveite ferramentas já
disponíveis e compatíveis com o ambiente; não instale uma alternativa apenas porque foi citada
no catálogo. Preparar o ambiente exige o escopo e a autorização correspondentes.

## Antes de chamar um modelo

Confira pré-requisitos que possam impedir a tarefa: entradas, ferramentas, acesso e permissão.
Reutilize evidências recentes. Para trabalho recorrente, compare antes uma versão, cursor ou
hash da entrada. Sem novidade ou lote autorizado incompleto, não há trabalho para iniciar.
Avance o cursor de processamento só após sucesso; trabalho parcial precisa continuar retomável.

Registre uma dependência indisponível com o erro observado e a condição de retomada.
Evite repetir tentativas sem mudança. Retome com novas entradas, evidência de disponibilidade
ou uma investigação delimitada explicitamente autorizada. Não altere agendas ou contas fora do escopo.

| Observação | Próxima ação |
| --- | --- |
| Ferramenta ou modelo não inicia | Relate a capacidade indisponível e o erro. Respeite restrições de provedor. |
| Fonte ou acesso necessário ausente | Identifique o acesso que falta, sem contornar autorização. |
| Compilação ou máquina falha antes da execução | Diagnostique o ambiente. |
| Entrada inalterada e nenhum lote incompleto | Relate ausência de trabalho. |
| Ferramentas funcionam, mas o resultado falha no aceite | Reproduza e corrija ou diagnostique a saída. |
| Confirmação de salvamento perdida | Leia o estado resultante antes de repetir a alteração. |

Um tempo limite excedido não demonstra sozinho a causa. Várias causas podem coexistir.

## Relacionar trabalho e prova

Use capacidades disponíveis adequadas à consequência do erro. Respeite provedor, modelo
e esforço escolhidos; declare configurações que a ferramenta não pode fornecer.
Quando existir `.agents/models.toml`, resolva papel e complexidade seguindo `delegar`:
na v2, o perfil base só muda por mapa explícito; na v1, combine os campos e alternativas antigos.
Tipos como visual, escrita e operação orientam capacidades e provas, sem reordenar candidatos.
A escolha explícita do pedido atual prevalece. Não confunda
indisponibilidade com resultado incorreto nem use a política para ampliar permissões.

| Trabalho | Prova |
| --- | --- |
| Edição mecânica ou extração | Compare o resultado exato com a fonte. |
| Código ou integração | Execute regressões no ponto público relevante. |
| Diagnóstico ou arquitetura | Diferencie hipóteses por reprodução e evidência independente. |
| Coordenação | Distribua arquivos distintos e faça edições sobrepostas em sequência. |
| Visual ou navegador | Exija as ferramentas relevantes e inspecione o resultado real. |
| Escrita | Preserve fatos, público e voz; o usuário avalia a adequação da voz. |
| Pesquisa ou classificação | Preserve fontes, versões de dados e instruções, e incerteza. |
| Operação | Confira o estado no ambiente escolhido e preserve um caminho de recuperação. |

Forneça objetivo, decisões, revisão das entradas, arquivos sob responsabilidade, ações permitidas
e exemplos de aceite. Na retomada, preserve a próxima etapa e o lote incompleto.

## Registro de execução

Para uma entrega delegada substancial ou experimento de modelo, preserve um registro conciso
junto dos registros existentes ou na conversa. Dispense a formalidade em respostas curtas de rotina.

```text
Objetivo e revisão das entradas:
Motivo da seleção e capacidades necessárias:
Papel, versão, perfil efetivo; complexidade, origem e mudança aplicada (quando houver):
Alternativa por indisponibilidade e erro observado (quando houver):
Modelo/esforço pedidos; configurações informadas ou observadas; desconhecimentos:
Resultado: entregue | saída incorreta | capacidade indisponível | acesso ausente |
  falha de ambiente | sem trabalho | incerto
Evidências, limites e correções restantes:
Tempo e uso: fonte observada ou desconhecido
Próxima ação exata ou condição de retomada:
```

Relate correções e rodadas de revisão reais. Não deduza custo de limites de assinatura,
esforço de nomes de modelo, identidade do nome de um papel nem uso da tarefa do total
da sessão. Mantenha segredos fora dos registros.

## Comparações delimitadas

Compare modelos apenas dentro da autorização. Fixe entradas representativas, exemplos
de aceite e ações permitidas antes de iniciar. Mantenha ferramentas, escopo e esforço
comparáveis; registre diferenças entre provedores e configurações indisponíveis.

Julgue saídas pelos exemplos fixados, incluindo tempo de revisão e correção. Um resultado
bem-sucedido não estabelece taxa de sucesso. O usuário decide preferências de voz ou design.
Tokenizadores, preços e uso desconhecido de cache limitam comparações de custo. Preserve
falhas de inicialização. Um experimento não muda padrões de modelo nem prova aceite independente.
