# Backup diário

`backup.py` copia as pastas listadas em `config.json` para o disco externo e mantém os
últimos 7 dias. O Agendador de Tarefas do Windows roda o script todo dia às 23h:

```text
python backup.py
```

O script devolve 1 quando alguma pasta falha ou quando ocorre um erro inesperado.
Como ele roda sem janela, tudo é registrado em `backup.log`, ao lado do script
(rotação automática: até ~1 MB por arquivo, mantendo `backup.log.1` a `backup.log.5`).
Erros inesperados ficam no log com o traceback completo.
