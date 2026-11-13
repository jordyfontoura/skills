# Imagens

`banner.svg` contém o retrato de Jordy Fontoura. O retrato não é licenciado sob a Apache-2.0;
veja a seção "Retrato do autor" em [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).

`skill-usage.svg` e `skill-usage-mobile.svg` apresentam o mesmo retrato de uso, em duas
disposições. São gerados por `python scripts/render_skill_usage.py`, a partir de
[skill-usage.json](../data/skill-usage.json). Exibem frequência relativa, sem contagens visíveis.
Os gráficos usam a paleta neutra do banner e não carregam recursos externos.

O retrato de 13/11/2026 considera 256 outras conversas disponíveis no T3 Code, incluindo
histórico anterior à data de consulta. Cada skill conta uma vez por mensagem; repetições em
mensagens diferentes contam novamente. Pedidos diretos do usuário e declarações de uso do
agente são contados separadamente e podem se sobrepor.

São excluídos catálogos, citações, recomendações, pedidos para editar a própria skill e
instruções embutidas em goals ou automações. Mensagens herdadas de outra conversa não são
contadas novamente, e atividades internas de subagentes ficam de fora. Uso silencioso não
aparece; zero significa ausência de registro segundo esses critérios.

Os rótulos usam os nomes atuais. Nomes históricos são reunidos conforme as renomeações do
[CHANGELOG](../../CHANGELOG.md), inclusive as duas antigas skills de crítica de interface.
O retrato depende das mensagens disponíveis e da identificação das declarações; não é
telemetria de execução nem uma medida da qualidade das skills.
