# Backup diário

`backup.py` copia as pastas listadas em `config.json` para o disco externo e mantém os
últimos 7 dias. O Agendador de Tarefas do Windows roda o script todo dia às 23h:

```text
python backup.py
```

O script devolve 1 quando alguma pasta falha ou quando ocorre um erro inesperado (por
exemplo, disco `E:` desconectado).

## Log

Como o script roda sem janela, tudo é registrado em `backup.log`, na mesma pasta do
script (independe da pasta atual do Agendador). O arquivo vira um novo à meia-noite e os
30 anteriores são mantidos como `backup.log.AAAA-MM-DD`. Rodando à mão, as mesmas linhas
aparecem no console.

Níveis usados:

- `INFO`: início, cada pasta copiada e conclusão.
- `WARNING`: remoção de backups antigos.
- `ERROR`: falha ao copiar uma pasta, ou erro inesperado (com traceback completo).
