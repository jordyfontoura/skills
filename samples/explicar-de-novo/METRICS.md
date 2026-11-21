# Métricas: explicar-de-novo

Gerado por `scripts/samples.py` a partir dos `run.json`. Os tokens de entrada incluem
as instruções do próprio agente; compare variantes do mesmo modelo.

| Modelo | Variante | Entrada | Em cache | Saída | Raciocínio | Ferramentas | Tempo | Palavras | Skills usadas |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| opus-5.5-medium | without-skills | 21.759 | 14.524 | 2.313 | 207 | 0 | 28 s | 871 | — |
| opus-5.5-medium | with-skills | 59.815 | 46.907 | 3.215 | 715 | 2 | 44 s | 948 | esclarecer |
| gpt-6.1-sol-medium | without-skills | 44.296 | 36.992 | 1.387 | 112 | 0 | 37 s | 549 | — |
| gpt-6.1-sol-medium | with-skills | 135.780 | 105.088 | 2.196 | 118 | 3 | 59 s | 700 | esclarecer |
