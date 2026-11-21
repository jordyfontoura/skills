# postagem-rede-social

- Modelo: `opus-5.5-medium`
- Variante: `with-skills`

## Usuário, turno 1

Escreve uma postagem pro LinkedIn contando que publiquei como código aberto a minha coleção de skills em português para agentes de código (Claude Code e Codex). Elas cobrem especificar, implementar, revisar e verificar o trabalho, e o agente só age com autorização explícita. O repositório é github.com/jordyfontoura/skills. Quero que desenvolvedores brasileiros testem e mandem sugestões.

## Agente, turno 1

Publiquei como código aberto a minha coleção de skills em português para agentes de código. Elas funcionam no Claude Code e no Codex.

As skills acompanham o trabalho do início ao fim. Com elas, o agente especifica o que precisa ser feito, implementa em partes que dá para verificar, revisa o diff e confere os critérios de aceite. Cada skill diz ao agente o que fazer, o que relatar e onde parar.

Todas seguem a mesma regra: o agente só age com autorização explícita. Se você pede uma revisão, ele revisa e não sai corrigindo o código. Se você pergunta sobre uma ferramenta, ele explica e não instala nada por conta própria.

Quero que desenvolvedores brasileiros testem. Use num projeto seu e me conte o que funcionou, o que atrapalhou e o que está faltando. Você pode mandar sugestões por issue ou pull request no repositório, ou aqui nos comentários.

github.com/jordyfontoura/skills

#ClaudeCode #Codex #OpenSource

---

- **Detalhes que não inventei:** não incluí o motivo de ter criado as skills, quantas são nem a licença. Um motivo concreto costuma aproximar o leitor, por exemplo um problema que você teve com agentes de código. Se quiser, me conta e eu coloco no segundo parágrafo.
- **Exemplos de autorização:** tirei os dois exemplos (revisar sem corrigir, explicar sem instalar) das descrições das próprias skills. Confira se eles representam bem a regra.
