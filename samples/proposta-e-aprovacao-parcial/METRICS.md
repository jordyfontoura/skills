# Métricas: proposta-e-aprovacao-parcial

Gerado por `scripts/samples.py` a partir dos `run.json`. Os tokens de entrada incluem
as instruções do próprio agente; compare variantes do mesmo modelo.

| Modelo | Variante | Entrada | Em cache | Saída | Raciocínio | Ferramentas | Tempo | Palavras | Skills usadas |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| opus-5.5-medium | without-skills | 74.543 | 63.239 | 4.923 | 801 | 6 | 56 s | 1.025 | — |
| opus-5.5-medium | with-skills | 153.763 | 136.845 | 6.138 | 820 | 8 | 69 s | 1.351 | implementar, propor |
| gpt-6.1-sol-medium | without-skills | 254.284 | 231.424 | 3.617 | 52 | 6 | 108 s | 313 | — |
| gpt-6.1-sol-medium | with-skills | 325.434 | 238.464 | 4.494 | 148 | 7 | 127 s | 344 | implementar, propor |
