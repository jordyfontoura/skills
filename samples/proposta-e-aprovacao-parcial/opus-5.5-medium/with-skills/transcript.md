# proposta-e-aprovacao-parcial

- Modelo: `opus-5.5-medium`
- Variante: `with-skills`

## Usuário, turno 1

Quero que esse script avise por e-mail quando o backup falhar, e de quebra queria trocar os prints por log. Me propõe antes de mexer.

## Agente, turno 1

Li `backup.py`, `config.json` e o `README.md`. Segue a proposta. Ainda não mudei nada.

## O que entendi

- Quando o backup falhar, você quer receber um e-mail.
- Os `print` passam a ser log. Hoje o script roda pelo Agendador sem janela, então ninguém vê essa saída.
- O que o script copia e como ele faz isso continua igual.

## 1. Log no lugar dos `print`

- Uso o módulo `logging`, que já vem com o Python, sem instalar nada.
- O log vai para o arquivo `backup.log`, na mesma pasta do script. Uso o caminho do próprio script, não a pasta atual, porque o Agendador costuma rodar com a pasta atual em `C:\Windows\System32`.
- Um arquivo novo é aberto à meia-noite e os 30 mais recentes ficam guardados (`TimedRotatingFileHandler`), para o log não crescer sem limite.
- O log também aparece no console quando você roda o script na mão.
- Cada linha sai com data, hora e nível, por exemplo:
  `2026-11-21 23:00:02 ERROR Falha ao copiar C:\Dados\contratos: [WinError 3] ...`
- Os níveis ficam assim: `INFO` para copiando e concluído, `WARNING` para a remoção de backup antigo, `ERROR` para falhas. Quando o script quebrar de vez, o log guarda o traceback completo (`logger.exception`).

## 2. E-mail quando falhar

Usaria o módulo `smtplib`, que também já vem com o Python. O e-mail sairia em **dois casos**:

1. **Alguma pasta não foi copiada**, que é o caso que o script já trata hoje.
2. **O script quebrou antes de terminar.** Exemplos: o disco `E:` não está conectado, o `config.json` está com erro ou falta permissão no destino. Hoje esses erros derrubam o script sem passar pela lista de falhas. Se eu cuidasse só do caso 1, justamente a falha mais provável (disco desconectado) **não mandaria e-mail**.

O e-mail traria o assunto `[Backup] FALHA em 2026-11-21`, as pastas que falharam com o erro de cada uma e o caminho do `backup.log`.

**Configuração:** os dados do servidor de e-mail entram no `config.json`:

```json
"email": {
  "smtp_host": "smtp.exemplo.com",
  "smtp_port": 587,
  "user": "...",
  "to": ["..."]
}
```

A **senha não entra no arquivo**. Ela fica numa variável de ambiente (`BACKUP_SMTP_PASSWORD`) configurada no Windows para o usuário que roda a tarefa.

Se o próprio envio do e-mail falhar, isso vai para o log como `ERROR` e o script continua devolvendo 1. Um problema no e-mail não esconde a falha do backup.

## 3. Um problema que encontrei e proponho corrigir junto

`remove_old` roda **mesmo quando houve falha**. Se o disco tiver problemas por vários dias, o script continua apagando os backups antigos bons e guardando só cópias incompletas. Proponho **não apagar backups antigos quando houver falha no dia**. É uma linha. Se preferir, deixo isso fora deste pedido.

## Arquivos que mudam

- `backup.py`: logging, envio de e-mail, captura de erros gerais e a correção acima.
- `config.json`: novo bloco `email`.
- `README.md`: onde fica o log, como definir a variável da senha e como testar.

## Como eu verificaria

- Rodar com uma pasta de origem que não existe: o log mostra `ERROR`, o script devolve 1 e o e-mail é enviado.
- Rodar com um destino que não existe, simulando o disco desconectado: aparece o traceback no log e o e-mail é enviado.
- Rodar com tudo certo: o log mostra só `INFO`, nenhum e-mail sai e o script devolve 0.
- Para testar o e-mail sem enviar de verdade, uso um servidor SMTP falso local. O envio real só com sua autorização.

## O que preciso de você

1. **Qual provedor de e-mail vai enviar?** Isso muda o host, a porta e a forma de login. Com o Gmail funciona usando uma senha de app. No Outlook.com acredito que o login simples por SMTP foi desativado para contas pessoais, mas precisaria confirmar. Se for isso mesmo, seria melhor usar outra conta para enviar ou um serviço como SendGrid ou Brevo.
2. **Quem recebe o e-mail?**
3. **Posso incluir a correção do `remove_old`?**
4. Uma opção, se você quiser: mandar também um e-mail curto de "backup OK" uma vez por semana, para você perceber se a tarefa parar de rodar. Eu deixaria de fora por enquanto.

Fico aguardando sua decisão para começar.

## Usuário, turno 2

Hmm, e se o envio do e-mail falhar também, o que acontece?

## Agente, turno 2

Nesse caso o script **não quebra e não esconde a falha**, mas o aviso fica restrito ao próprio computador:

1. Ele tenta enviar de novo, até 3 vezes com uns 30 segundos entre cada tentativa. Isso cobre instabilidades rápidas de rede ou do servidor.
2. Se as três falharem, grava no `backup.log` um `ERROR` com o motivo (senha errada, servidor fora do ar, sem internet etc.).
3. O script termina com código 1. O Agendador de Tarefas mostra esse resultado como **0x1** na coluna "Resultado da última execução".

O problema é que **nada disso chega até você**. Se ninguém abrir o log ou o Agendador, a falha passa despercebida. É o mesmo ponto cego de hoje, só que mais raro.

O que eu acrescentaria, do mais simples ao mais completo:

- **Aviso local que dá para ver.** Quando o e-mail falhar, o script cria um arquivo `BACKUP_FALHOU.txt` na sua Área de Trabalho com o resumo do erro. Custa quase nada e aparece na próxima vez que você usar o PC. Na execução seguinte que der certo, ele apaga o arquivo.
- **E-mail semanal de "backup OK".** É a opção 4 da proposta. Ela também resolve este caso: se o e-mail parar de funcionar, você **deixa de receber** o aviso semanal e percebe a falta. Também pega situações em que o script nem chega a rodar (PC desligado, tarefa desativada), que nenhum aviso de falha consegue pegar.
- **Monitor externo do tipo "dead man's switch"** (Healthchecks.io, por exemplo). O script avisa um serviço a cada execução bem-sucedida, e o serviço te alerta quando o aviso não chega. É o mais confiável, mas adiciona uma dependência externa. Para um backup doméstico acho exagero.

**Minha recomendação:** as 3 tentativas, mais o arquivo na Área de Trabalho, mais o e-mail semanal de "OK". Com isso, até o caso em que tudo falha acaba aparecendo para você.

A proposta continua esperando sua decisão. Faltam também as respostas às perguntas anteriores: qual provedor envia o e-mail, quem recebe e se posso incluir a correção do `remove_old`.

## Usuário, turno 3

Boa. Pode fazer só a parte do log por enquanto, o e-mail eu vejo depois.

## Agente, turno 3

Troquei os `print` por log, mas **ainda não testei**. Nesta sessão não tenho ferramenta para executar comandos, então não consegui rodar o script.

**O que mudou**

- **`backup.py`**: os `print` agora usam o módulo `logging`.
  - O log vai para `backup.log`, na pasta do script, e também aparece no console quando você roda à mão.
  - À meia-noite começa um arquivo novo, e os 30 anteriores ficam guardados.
  - Cada linha começa com data e hora, por exemplo `2026-11-21 23:00:02 ERROR ...`.
  - Níveis: `INFO` para início, cópias e conclusão; `WARNING` para a remoção de backup antigo; `ERROR` para falhas.
  - Um erro inesperado, como o disco `E:` desconectado ou o `config.json` inválido, agora vai para o log com o traceback completo, e o script termina com código 1. Antes ele também terminava com 1, mas a mensagem só aparecia na tela, que ninguém vê.
- **`README.md`**: nova seção explicando onde fica o log, como funciona a troca diária de arquivo e o que cada nível significa.

Ficaram de fora, como combinado, o e-mail e a correção do `remove_old`, que ainda apaga backups antigos mesmo quando o backup do dia falha.

**Para conferir, rode `python backup.py` nestes três cenários:**

1. **Tudo certo:** só linhas `INFO` (e `WARNING` se houver backup antigo para apagar), e o script termina com 0.
2. **Uma pasta de origem que não existe** no `config.json`: uma linha `ERROR Falha ao copiar ...` e a mensagem final de falha, terminando com 1.
3. **Destino que não existe** (por exemplo, o disco desconectado): `ERROR Backup interrompido por erro inesperado.` seguido do traceback, terminando com 1.

Em todos, as mesmas linhas devem aparecer no console e em `backup.log`, mesmo se você rodar o script a partir de outra pasta. Para ver o código de saída no PowerShell, rode `$LASTEXITCODE` logo depois. Se quiser, me manda a saída que eu confiro.
