# explicar-de-novo

- Modelo: `opus-5.5-medium`
- Variante: `with-skills`

## Usuário, turno 1

Quero que todo PR do meu projeto rode os testes sozinho e me avise no Telegram quando quebrar, sem gastar nada. Como eu faria? Só me explica as opções, não precisa criar nada.

## Agente, turno 1

# Testes automáticos em PR com aviso no Telegram, sem custo

O jeito mais simples é usar **GitHub Actions** com um **bot do Telegram**. Os dois são gratuitos para esse uso.

## Opção 1: GitHub Actions com bot do Telegram (recomendada)

**Como funciona:**
1. Todo PR aberto ou atualizado dispara um workflow, um arquivo `.yml` em `.github/workflows/`.
2. O workflow instala as dependências e roda os testes.
3. Se algum passo falhar, um passo final com `if: failure()` faz uma chamada HTTP simples (`curl`) à API do Telegram e manda uma mensagem com o nome do PR, o autor e o link do log.

**Do lado do Telegram:**
- Você cria um bot pelo **@BotFather** e recebe um *token*.
- Você manda uma mensagem para o bot e descobre seu *chat_id* pela URL `https://api.telegram.org/bot<TOKEN>/getUpdates`.
- O token e o chat_id ficam guardados como **Secrets** do repositório (Settings → Secrets and variables → Actions), nunca escritos no código.

**Custo:**
- **Repositório público:** minutos ilimitados, grátis.
- **Repositório privado:** o plano Free tem uma cota mensal de minutos (historicamente 2.000/mês). Isso costuma sobrar para projetos pequenos e médios. Esses limites mudam de vez em quando, então vale conferir a página de billing do GitHub.
- **Telegram Bot API:** grátis.

**Cuidado:** em PRs vindos de **forks**, o GitHub não passa os Secrets ao workflow, por segurança. Os testes rodam normalmente, mas a notificação falha. Existe o evento `pull_request_target`, que contorna isso, mas ele é perigoso: pode expor seus secrets a código de terceiros. Se só você e seu time abrem PRs, isso não importa.

## Opção 2: GitLab CI

A ideia é a mesma: um `.gitlab-ci.yml` roda os testes, e um job com `when: on_failure` chama o Telegram. O plano gratuito tem uma cota de minutos bem menor que a do GitHub (algumas centenas por mês). Só faz sentido se o projeto já estiver no GitLab.

## Opção 3: Runner próprio (self-hosted)

Você instala o runner do GitHub ou do GitLab no seu próprio computador ou servidor. Assim os minutos não são contados, ou seja, é grátis sem limite. Por outro lado:
- A máquina precisa estar ligada.
- É **arriscado em repositório público**, porque qualquer PR executaria código na sua máquina.

Só vale a pena se a cota gratuita não bastar.

## Opção 4: Sem escrever o passo de notificação

Existem bots e apps de terceiros que ligam o GitHub ao Telegram e avisam sobre falhas de CI. Dá menos trabalho, mas você tem menos controle sobre a mensagem e dá acesso ao repositório a um serviço externo. Também existe uma *action* pronta no Marketplace (ex.: `appleboy/telegram-action`) que substitui o `curl`. Funciona, mas o `curl` direto é tão simples quanto e não depende de terceiros.

## Recomendação

Use a **Opção 1**: GitHub Actions, com notificação via `curl` só quando falhar. Para completar, ative a **proteção de branch** (Settings → Branches) exigindo que os testes passem antes do merge. Assim um PR quebrado não entra nem se você deixar o aviso passar.

Se quiser, depois posso montar o workflow, adaptado à linguagem e ao comando de testes do seu projeto.

## Usuário, turno 2

pera, não entendi. explica de novo?

## Agente, turno 2

Resumindo: dá para fazer isso de graça usando duas coisas que você provavelmente já tem, o **GitHub** e o **Telegram**. Na resposta anterior eu usei muitos termos técnicos de uma vez. Vou contar como uma história.

**O que acontece na prática, depois de configurado:**

1. Você, ou outra pessoa, abre um PR no GitHub.
2. O GitHub percebe isso sozinho. Num computador dele, ele baixa seu código e roda os testes, o mesmo comando que você rodaria no terminal (`npm test`, `pytest` etc.).
3. Se os testes passam, nada acontece. O PR só ganha um ✅ verde.
4. Se algum teste falha, o GitHub manda uma mensagem para um "robô" seu no Telegram. Você recebe algo como: *"❌ Testes falharam no PR #12 – Ajusta login"*, com um link para ver o erro.

**O que você precisa preparar, uma vez só:**

- **No Telegram:** criar um robô (bot) conversando com o **@BotFather**, a conta oficial do Telegram para isso. Ele te dá uma senha do robô, chamada *token*. Depois você descobre o número da sua conversa com o robô (*chat_id*), para o robô saber para quem mandar.
- **No GitHub:** colocar um arquivo de instruções no projeto, na pasta `.github/workflows/`. É uma receita do tipo "quando abrir PR, rode os testes; se falhar, avise no Telegram". Esse recurso do GitHub se chama **GitHub Actions**.
- **Guardar a senha do robô com segurança:** o token não vai escrito no arquivo. Ele fica num cofre do próprio GitHub chamado **Secrets**, nas configurações do repositório.

**Por que não custa nada:**

- O Telegram não cobra pelos robôs.
- O GitHub Actions é grátis sem limite em repositório público. Em repositório privado, existe uma cota mensal gratuita de tempo de execução que costuma sobrar para projetos pequenos. Vale conferir o valor atual no GitHub, porque esse limite muda de vez em quando.

**As outras opções que citei** são variações da mesma ideia. O **GitLab** tem um recurso equivalente, caso seu projeto esteja lá. Também dá para rodar os testes no seu próprio computador em vez do da plataforma, mas aí ele precisa ficar ligado, e não recomendo. Para o seu caso, o caminho GitHub + Telegram é o mais simples.

**Uma ressalva que só importa em projeto aberto a desconhecidos:** se alguém de fora fizer uma cópia do seu projeto (um *fork*) e abrir um PR a partir dela, os testes rodam, mas o aviso no Telegram não sai. É uma proteção do GitHub para estranhos não terem acesso à senha do robô. Se só você ou seu time abrem PRs, isso não afeta nada.
