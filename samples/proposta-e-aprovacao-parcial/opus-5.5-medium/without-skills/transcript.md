# proposta-e-aprovacao-parcial

- Modelo: `opus-5.5-medium`
- Variante: `without-skills`

## Usuário, turno 1

Quero que esse script avise por e-mail quando o backup falhar, e de quebra queria trocar os prints por log. Me propõe antes de mexer.

## Agente, turno 1

Li o `backup.py`, o `config.json` e o README. Esta é a proposta. Ainda não alterei nada.

## 1. Log em vez de `print`

- Uso o módulo `logging` com dois destinos:
  - **Arquivo `backup.log`** ao lado do script, com rotação (`RotatingFileHandler`, ~1 MB × 5 arquivos). É o que importa, porque o Agendador roda o script sem janela e hoje ninguém vê a saída.
  - **Console**, para quando você rodar na mão.
- Formato: `2026-11-21 23:00:01 INFO Copiando C:\Dados\financeiro...`
- Níveis: `INFO` para o andamento, `ERROR` para falha de cópia (com o motivo) e `exception` para erro inesperado, com o traceback completo no arquivo.
- O caminho do log fica fixo ao lado do script, porque o Agendador costuma iniciar com o diretório de trabalho em `System32`.

## 2. E-mail quando falhar

- O e-mail sai com `smtplib` (biblioteca padrão, sem dependências novas), por SMTP com STARTTLS.
- **Quando envia:** se alguma pasta falhar **e** também se o script quebrar antes de terminar. Isso é importante: hoje, se o disco `E:` estiver desconectado, as cópias falham e depois `remove_old` chama `iterdir()` num caminho que não existe. Isso lança uma exceção não tratada, e o script morre sem chegar ao fim. Vou envolver o `main` num `try/except` para que esse caso também gere e-mail.
- **Conteúdo:** assunto do tipo `[Backup] FALHA em 2026-11-21 (2 pasta(s))`, a lista das pastas com o erro de cada uma e as últimas ~50 linhas do log no corpo.
- **Configuração:** uma seção nova no `config.json`:
  ```json
  "email": {
    "smtp_host": "smtp.office365.com",
    "smtp_port": 587,
    "from": "...",
    "to": ["..."]
  }
  ```
  Usuário e **senha ficam fora do JSON**, em variáveis de ambiente do usuário (`BACKUP_SMTP_USER` e `BACKUP_SMTP_PASSWORD`), que o Agendador enxerga se a tarefa rodar com a sua conta.
- Se o próprio envio do e-mail falhar, isso vai para o log, e o script continua retornando 1.
- Sem a seção `email` no config, o script só registra no log e não envia nada.

## 3. Um problema que encontrei (fica fora do escopo, a não ser que você queira)

`remove_old` roda mesmo quando a cópia falha. A pasta de hoje, parcial ou vazia, conta como um dos 7 dias guardados, então um backup antigo bom é apagado para dar lugar a um ruim. Se o disco ficar alguns dias com problema, você acaba perdendo os backups bons. Sugiro **só fazer a limpeza quando não houver falhas**. É uma linha, mas muda o comportamento, então só faço se você aprovar.

## Preciso que você me diga

1. **Qual provedor de e-mail?** Outlook/Office 365 e Gmail costumam exigir **senha de app**, porque a senha normal com autenticação em dois fatores não funciona via SMTP. Com isso eu já deixo host e porta certos.
2. **Para quem vai o aviso?** Para você mesmo ou para mais alguém?
3. **Quer um e-mail também quando der certo?** Ajuda a perceber quando o script nem chegou a rodar. Sem isso, a falta de e-mail pode querer dizer que deu tudo certo ou que a tarefa nem executou.
4. **Aplico a correção do item 3?**

Com essas respostas eu faço as alterações no `backup.py`, no `config.json` e no README, incluindo como configurar as variáveis de ambiente.

## Usuário, turno 2

Hmm, e se o envio do e-mail falhar também, o que acontece?

## Agente, turno 2

Como propus, o erro do envio vai para o `backup.log` com o motivo (senha errada, sem internet, servidor recusou) e o script continua retornando 1. Esse retorno só aparece no histórico do Agendador, que ninguém abre. Na prática você ficaria **sem saber da falha**, exatamente como hoje.

Essa é a fraqueza de qualquer alerta por e-mail. Para não depender só dele, sugiro duas coisas:

1. **Tentar de novo algumas vezes.** São 3 tentativas com uns 30 s de intervalo, o que cobre instabilidade rápida de rede ou do servidor SMTP.

2. **Guardar o alerta pendente e reenviar na próxima execução.** Se as 3 tentativas falharem, o script grava o aviso num arquivo `alerta_pendente.txt` ao lado do script. Na noite seguinte ele tenta mandar esse aviso antes de tudo, junto com o resultado do dia. Assim um problema temporário só atrasa o aviso em um dia, em vez de perdê-lo.

O que esses dois passos **não** resolvem é um problema permanente no envio, como senha expirada ou senha de app revogada. Para isso existem duas saídas:
- **Notificação na tela do Windows** quando o e-mail não sai. Só funciona se você estiver logado na hora em que a tarefa roda.
- **Aviso de sucesso diário** (a pergunta 3 da proposta). É o que resolve de verdade: se parar de chegar o "Backup OK", você sabe que algo quebrou, seja o backup, o e-mail ou a tarefa que nem rodou.

**Minha recomendação:** fazer os passos 1 e 2 e ligar o aviso de sucesso diário. A notificação na tela não vale a complexidade a mais.

Se você concordar, só preciso ainda das respostas da proposta anterior: o provedor de e-mail, quem recebe o aviso e se aplico a correção da limpeza.

## Usuário, turno 3

Boa. Pode fazer só a parte do log por enquanto, o e-mail eu vejo depois.

## Agente, turno 3

Troquei os prints por log em `backup.py`. Não rodei o script, porque ele copiaria para `E:` e apagaria backups antigos de verdade.

**Mudanças:**
- Cada execução grava no arquivo **`backup.log`**, ao lado do script, e também aparece no console. O nome do log não depende da pasta de onde o script é chamado, então funciona igual pelo Agendador.
- A rotação acontece a cada ~1 MB e guarda até 5 arquivos antigos (`backup.log.1` a `.5`).
- Cada linha tem data e hora e um nível: `INFO` para o andamento normal e `ERROR` para as pastas que falharam, junto com o motivo.
- Antes, um **erro inesperado**, como o disco `E:` desconectado ou um `config.json` inválido, derrubava o script sem deixar nada registrado. Agora ele vai para o log com o detalhe completo do erro. O código de saída continua 1, como antes.
- Atualizei o README para dizer onde fica o log.

**Deixei como estava:**
- A limpeza dos backups antigos continua rodando mesmo quando a cópia falha. É o problema que comentei antes, e você ainda não decidiu se quer a correção.
- Nada do e-mail.

Quando quiser fazer o e-mail, a mensagem de falha pode trazer as últimas linhas desse log.
