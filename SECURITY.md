# Segurança

## Relatar uma vulnerabilidade

Use o [relato privado de vulnerabilidades do GitHub](https://github.com/jordyfontoura/skills/security/advisories/new).
Não abra uma issue pública. Inclua a skill ou o arquivo afetado, o agente e a versão usados,
os passos para reproduzir e o efeito observado.

Considere vulnerabilidade, entre outros casos:

- Instruções numa skill ou num papel que levem o agente a ler segredos, enviar dados para fora
  do projeto ou executar ações sem a autorização pedida.
- Texto oculto, como comentários HTML ou caracteres invisíveis, que mude o comportamento do agente.
- Componentes executáveis no plugin, como hooks, servidores MCP ou binários.

## Modelo de ameaça

As skills são instruções em Markdown que o agente segue com as permissões que você concedeu a
ele. Elas não substituem as permissões, confirmações e sandboxes do Claude Code, do Codex ou de
outra ferramenta. Mantenha as confirmações ativas para comandos com efeitos externos.

O plugin contém apenas skills, papéis e manifestos. O `check.py` recusa hooks, servidores MCP
ou LSP, binários e caracteres invisíveis, e a CI roda essa verificação em cada PR.

Algumas skills podem levar o agente a agir fora do repositório quando você autoriza:

| Skill | Efeito possível |
| --- | --- |
| `integrate` | Push, merge e abertura de PR. |
| `toolbox` | Instalação de ferramentas de linha de comando. |
| `setup-harness` | Configuração de comandos, CI e instruções do projeto. |
| `delegate`, `council`, `evaluate` | Início de outros agentes, que podem receber contexto do projeto. |
| `research` | Acesso à internet. |
| `update-harness` | Leitura da origem desta coleção na rede. |

## Atualizações

Uma atualização do plugin muda as instruções que seus agentes seguem. Trate-a como uma
atualização de código: leia o [CHANGELOG](CHANGELOG.md) ou o diff antes. No Claude Code, a
atualização automática de marketplaces de terceiros vem desligada por padrão. Para fixar uma
versão, adicione o marketplace com uma tag, por exemplo `jordyfontoura/skills#v0.1.0`.
