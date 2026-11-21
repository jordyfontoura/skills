# Métricas: pesquisar-antes-de-decidir

Gerado por `scripts/samples.py` a partir dos `run.json`. Os tokens de entrada incluem
as instruções do próprio agente; compare variantes do mesmo modelo.

| Modelo | Variante | Entrada | Em cache | Saída | Raciocínio | Ferramentas | Tempo | Palavras | Skills usadas |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| opus-5.5-medium | without-skills | 28.068 | 16.362 | 3.152 | 251 | 4 | 38 s | 754 | — |
| opus-5.5-medium | with-skills | 104.398 | 81.341 | 4.330 | 284 | 12 | 64 s | 921 | pesquisar-web |
| gpt-6.1-sol-medium | without-skills | 225.774 | 180.608 | 1.859 | 81 | 5 | 63 s | 661 | — |
| gpt-6.1-sol-medium | with-skills | 353.352 | 275.328 | 2.376 | 97 | 7 | 84 s | 792 | pesquisar-web |
