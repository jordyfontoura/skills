# Métricas: postagem-rede-social

Gerado por `scripts/samples.py` a partir dos `run.json`. Os tokens de entrada incluem
as instruções do próprio agente; compare variantes do mesmo modelo.

| Modelo | Variante | Entrada | Em cache | Saída | Raciocínio | Ferramentas | Tempo | Palavras | Skills usadas |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| opus-5.5-medium | without-skills | 10.172 | 4.428 | 707 | 50 | 0 | 11 s | 253 | — |
| opus-5.5-medium | with-skills | 29.628 | 17.157 | 1.599 | 838 | 1 | 19 s | 228 | redigir |
| gpt-6.1-sol-medium | without-skills | 14.612 | 5.504 | 194 | 23 | 0 | 11 s | 104 | — |
| gpt-6.1-sol-medium | with-skills | 35.866 | 0 | 209 | 0 | 1 | 14 s | 90 | redigir |
