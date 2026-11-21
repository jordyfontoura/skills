# Backup diário

`backup.py` copia as pastas listadas em `config.json` para o disco externo e mantém os
últimos 7 dias. O Agendador de Tarefas do Windows roda o script todo dia às 23h:

```text
python backup.py
```

O script registra o início, as cópias, a remoção de backups antigos e o resultado em
`backup.log`, na mesma pasta de `backup.py`, independentemente do diretório de trabalho
do Agendador. Cada registro contém data, hora e nível (`INFO` ou `ERROR`); erros incluem
o traceback para diagnóstico.

O arquivo gira ao atingir aproximadamente 5 MiB, mantendo até três arquivos anteriores
(`backup.log.1` a `backup.log.3`). O usuário do Agendador precisa ter permissão de escrita
na pasta do script.

O script devolve 0 em caso de sucesso e 1 em caso de falha de cópia, configuração ou
limpeza. Se não conseguir abrir o arquivo de log, registra o erro na saída de erro
padrão e devolve 1 sem iniciar o backup. Nenhum e-mail é enviado.
