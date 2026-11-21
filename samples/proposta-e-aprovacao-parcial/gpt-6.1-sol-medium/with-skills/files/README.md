# Backup diário

`backup.py` copia as pastas listadas em `config.json` para o disco externo e mantém os
últimos 7 dias. O Agendador de Tarefas do Windows roda o script todo dia às 23h:

```text
python backup.py
```

O script grava o andamento em `logs/backup.log`, na pasta do próprio script, mesmo
quando o Agendador o executa sem janela ou a partir de outro diretório. O usuário
que executa a tarefa precisa ter permissão de escrita nessa pasta.

O log usa UTF-8 e inclui data, hora, nível (`INFO` ou `ERROR`) e detalhes das
exceções. Ao atingir aproximadamente 5 MiB, o arquivo é rotacionado, mantendo até
3 arquivos anteriores (`backup.log.1` a `backup.log.3`).

O script devolve `0` quando conclui com sucesso e `1` quando alguma cópia falha ou
ocorre um erro de configuração ou limpeza. Esses erros ficam registrados no log.
Se não for possível criar ou abrir o log, a execução é interrompida antes do backup;
o erro é enviado à saída de erro padrão do Python.

Não há envio de e-mail nesta versão.
