# Backup diário

`backup.py` copia as pastas listadas em `config.json` para o disco externo e mantém os
últimos 7 dias. O Agendador de Tarefas do Windows roda o script todo dia às 23h:

```text
python backup.py
```

O script devolve 1 quando alguma pasta falha, mas ninguém vê a saída: ele roda sem janela.
