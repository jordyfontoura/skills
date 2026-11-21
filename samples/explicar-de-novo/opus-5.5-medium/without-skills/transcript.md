# explicar-de-novo

- Modelo: `opus-5.5-medium`
- Variante: `without-skills`

## Usuário, turno 1

Quero que todo PR do meu projeto rode os testes sozinho e me avise no Telegram quando quebrar, sem gastar nada. Como eu faria? Só me explica as opções, não precisa criar nada.

## Agente, turno 1

Dá pra fazer isso de graça. Você precisa de duas coisas: um serviço de CI que rode os testes em cada PR e um bot do Telegram que mande a mensagem quando eles falharem.

## 1. Onde rodar os testes (CI)

**GitHub Actions** é a opção mais simples se o código está no GitHub.
- Repositório público: minutos ilimitados.
- Repositório privado: cerca de 2.000 minutos por mês no plano Free. Para a maioria dos projetos pessoais isso sobra.
- Você cria um arquivo `.github/workflows/tests.yml` com o gatilho `on: pull_request`, que instala as dependências e roda os testes.

**Outras opções:**
- **GitLab CI**: 400 minutos por mês no plano Free (pode ter mudado, vale conferir). Você também pode registrar um runner na sua própria máquina e aí o tempo é ilimitado.
- **Runner self-hosted** (no GitHub ou no GitLab): roda no seu PC ou num servidor seu, de graça e sem limite. A desvantagem é que a máquina precisa ficar ligada. Em repositório público é arriscado, porque qualquer pessoa pode abrir um PR com código que vai rodar na sua máquina.

## 2. Como avisar no Telegram

**Passo comum a todas as opções:** no Telegram, fale com o **@BotFather**, use o comando `/newbot` e guarde o **token**. Depois mande uma mensagem para o seu bot e descubra o seu **chat_id** em `https://api.telegram.org/bot<TOKEN>/getUpdates`. Coloque os dois como **secrets** do repositório (no GitHub fica em Settings → Secrets and variables → Actions). Assim eles nunca aparecem no código.

Depois disso, há três jeitos de mandar a mensagem:

**a) Um passo no final do próprio workflow (recomendo este)**
Adicione um passo com `if: failure()` que chama a API do Telegram com um `curl` para `sendMessage`. A mensagem pode levar o título do PR, o autor e o link do run. É só um `curl`, sem depender de nada externo.

**b) Uma action pronta do Marketplace**
Por exemplo, `appleboy/telegram-action`. Você passa o token, o chat_id e o texto. É menos código, mas você passa a depender de terceiros. Se usar, fixe a versão pelo SHA do commit.

**c) Sem escrever código no CI**
Use um app de integração que liga o GitHub ao Telegram. Existem bots que recebem os webhooks do GitHub e repassam as notificações. É prático, mas você tem menos controle sobre o que é enviado, e esse serviço passa a ter acesso aos eventos do seu repositório.

## Cuidado com PRs de forks

Se o repositório for público e receber PRs de forks, os workflows disparados por `pull_request` **não têm acesso aos secrets**. Os testes rodam normalmente, mas o aviso no Telegram falha. Há dois jeitos de resolver:
- **Workflow separado com `workflow_run`** (o mais seguro): ele dispara quando o workflow de testes termina, roda no contexto do seu repositório e tem acesso aos secrets.
- **`pull_request_target`**: só use se não fizer checkout do código do PR. Rodar código de terceiros com acesso aos seus secrets é uma brecha de segurança conhecida.

Se todos os PRs vêm de branches do próprio repositório, nada disso afeta você.

## Recomendação

Use **GitHub Actions + um passo com `curl` e `if: failure()`**. Não custa nada, é um arquivo só, umas 20 a 30 linhas de YAML, e não depende de serviço externo além do Telegram.

Se quiser, eu monto o workflow para a sua stack. Basta me dizer a linguagem e o comando que roda os testes.

## Usuário, turno 2

pera, não entendi. explica de novo?

## Agente, turno 2

Claro, vou mais devagar e sem jargão.

## A ideia em uma frase

Você quer que, **toda vez que alguém abrir um PR, um computador rode seus testes sozinho e, se algo quebrar, mande uma mensagem no seu Telegram**.

## As 3 peças

**1. Quem roda os testes: GitHub Actions**
Se o projeto está no GitHub, ele já tem esse "robô" embutido e de graça. Você coloca um arquivo de configuração no projeto dizendo "quando abrirem um PR, rode os testes". Pronto, a partir daí o GitHub faz isso sozinho.

**2. Quem manda a mensagem: um bot do Telegram**
No Telegram você conversa com o **@BotFather**, que cria um bot para você em 1 minuto. Ele te dá uma senha do bot (o *token*). Você também descobre o número da sua conversa (o *chat_id*), para o bot saber para quem mandar.

**3. A ligação entre os dois**
No mesmo arquivo de configuração do passo 1, você adiciona uma regra: **"se os testes falharem, mande uma mensagem pelo bot"**. O token e o chat_id ficam guardados num cofre do GitHub (os *secrets*), e não no código.

## Na prática, fica assim

1. Alguém abre um PR.
2. O GitHub roda os testes.
3. Se passarem, nada acontece.
4. Se falharem, chega no seu Telegram: *"❌ Testes quebraram no PR #12, veja aqui: [link]"*.

## Custa algo?

Não. É grátis em repositório público, e em repositório privado o plano gratuito dá cerca de 2.000 minutos por mês, o que costuma sobrar.

## Aquele aviso sobre forks

Pode ignorar por enquanto. Ele só importa se o projeto for público e **outras pessoas** mandarem PRs. Se é só você (ou seu time) trabalhando no mesmo repositório, não se preocupe com isso.

Ficou mais claro? Se quiser, me diz em que linguagem é o projeto e eu te mostro como fica esse arquivo.
