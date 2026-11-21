# explicar-de-novo

- Modelo: `gpt-6.1-sol-medium`
- Variante: `with-skills`

## Usuário, turno 1

Quero que todo PR do meu projeto rode os testes sozinho e me avise no Telegram quando quebrar, sem gastar nada. Como eu faria? Só me explica as opções, não precisa criar nada.

## Agente, turno 1

Você precisa de uma **integração contínua (CI)**: a cada PR aberto ou atualizado, um serviço executa os testes e, se falharem, manda uma mensagem pelo bot do Telegram.

A melhor opção depende de onde seu código está:

| Opção | Como funciona | Quando fica grátis |
|---|---|---|
| **GitHub Actions** | Executa os testes nos PRs do GitHub e chama o Telegram quando falham. | Repositórios públicos têm execução gratuita em runners padrão. Privados dependem da franquia do plano. |
| **GitLab CI/CD** | Executa uma pipeline a cada merge request e envia o alerta. | Dentro da cota gratuita e das condições da conta, ou usando uma máquina sua. |
| **Runner próprio** | Uma máquina sua executa os testes, conectada ao GitHub, GitLab ou outro servidor de CI. | Sem cobrança pelos minutos de uma máquina hospedada, mas há custos de energia, manutenção e disponibilidade. |

**Se seu projeto estiver no GitHub, eu começaria com GitHub Actions + bot do Telegram.** O fluxo seria:

1. Configurar o evento de PR para executar a cada abertura e novo commit.
2. Preparar o ambiente, instalar dependências e rodar o comando de testes do projeto.
3. Quando os testes falharem, enviar ao Telegram uma mensagem com o PR, o commit e o link dos logs.
4. Opcionalmente, exigir que os testes passem antes de permitir o merge, conforme os recursos disponíveis no seu plano.

Para o Telegram, você criaria um bot pelo **@BotFather**, iniciaria uma conversa com ele ou o adicionaria a um grupo e obteria o identificador desse chat. O CI chamaria o método [`sendMessage` da Bot API](https://core.telegram.org/bots/api#sendmessage). **Alertas comuns por essa API não precisam de assinatura nem de um servidor dedicado.** O token fica guardado nos segredos do CI.

Há um detalhe importante se você recebe **PRs de forks**: o GitHub normalmente não disponibiliza segredos nesses testes. Para continuar recebendo alertas, a solução é um segundo workflow confiável, acionado ao término dos testes, que apenas consulta o resultado e envia a mensagem. Ele não deve executar código do PR com acesso ao token.

Para manter o custo em zero:

- Use runners Linux padrão e fique dentro da franquia se o repositório for privado.
- Cancele execuções antigas quando chegar outro commit no mesmo PR.
- Defina tempo máximo e retenção curta dos arquivos de resultados.
- Confira as cotas e os controles de cobrança atuais antes de ativar consumo pago.

**Minha recomendação:** use o CI da plataforma onde o projeto já está e envie o alerta diretamente ao Telegram. É a combinação com menos manutenção; em repositório privado, a viabilidade gratuita depende de quantos minutos seus testes consomem.

## Usuário, turno 2

pera, não entendi. explica de novo?

## Agente, turno 2

A ideia é: **toda vez que você abrir ou atualizar um PR, uma máquina executa os testes e avisa no Telegram se algum falhar.** Você configura isso uma vez.

Imagine que você mudou a tela de login:

1. Você abre o PR com essa mudança.
2. O serviço baixa o código e executa os testes que seu projeto já tem.
3. Um teste detecta que o login parou de funcionar.
4. Você recebe no Telegram: “Os testes do PR #42 falharam”, com um link para ver o erro.

Você precisa de duas peças:

- **Um serviço para executar os testes.** Se o código está no GitHub, o mais simples costuma ser o **GitHub Actions**. Se está no GitLab, existe o **GitLab CI/CD**.
- **Um bot do Telegram para entregar o aviso.** O serviço de testes envia a mensagem por esse bot. Para esse uso comum, o Telegram não cobra.

A parte do **“sem gastar nada”** depende de onde os testes rodam:

- **Projeto público no GitHub:** os computadores padrão do GitHub Actions podem executar os testes gratuitamente.
- **Projeto privado:** existe uma franquia gratuita. Se os testes consumirem mais que ela, será preciso limitar as execuções ou contratar mais capacidade.
- **Seu próprio computador:** também pode executar os testes, mas precisa ficar ligado e você assume energia e manutenção.

**Se você usa GitHub, minha recomendação é começar com GitHub Actions e um bot do Telegram**, conferindo a franquia se o projeto for privado. Isso automatiza os testes existentes; criar os testes, caso ainda não existam, seria uma etapa separada.
