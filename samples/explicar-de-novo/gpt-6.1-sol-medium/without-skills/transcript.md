# explicar-de-novo

- Modelo: `gpt-6.1-sol-medium`
- Variante: `without-skills`

## Usuário, turno 1

Quero que todo PR do meu projeto rode os testes sozinho e me avise no Telegram quando quebrar, sem gastar nada. Como eu faria? Só me explica as opções, não precisa criar nada.

## Agente, turno 1

Se seu projeto está no GitHub, eu usaria **GitHub Actions para rodar os testes em cada PR e um bot do Telegram para avisar quando falharem**. Para um projeto pequeno, isso geralmente cabe no plano gratuito.

O fluxo seria:

1. Alguém abre um PR ou envia novos commits.
2. O GitHub instala as dependências e executa o comando de testes do projeto.
3. O resultado aparece no PR.
4. Se os testes falharem, uma etapa envia uma mensagem pelo bot do Telegram, com o nome do PR e um link para os logs.

Você criaria o bot pelo **@BotFather**, iniciaria uma conversa com ele e guardaria o token nas configurações de *Secrets* do repositório. O envio usa a API do Telegram, sem precisar contratar um serviço de notificações.

Estas são as opções principais:

| Opção | Quando faz sentido | Custo e limitações |
|---|---|---|
| **GitHub Actions + Telegram** | Código no GitHub; configuração mais simples | Runners padrão são gratuitos em repositórios públicos. Privados têm franquia de uso no plano gratuito. |
| **GitLab CI/CD + Telegram** | Projeto já está no GitLab | Mesma ideia, com cota de computação e possíveis requisitos para usar os runners compartilhados. |
| **Runner próprio + Telegram** | Você já tem um computador ou servidor disponível | Evita consumir minutos hospedados, mas depende da máquina ligada, energia e manutenção. Executar código de PRs exige cuidado com isolamento. |

**Para manter o custo em zero**, use um runner Linux padrão, cancele execuções antigas quando entrarem novos commits e configure o limite de gastos para impedir cobrança além da franquia, conforme as opções da plataforma. “Plano gratuito” não significa uso ilimitado em projetos privados.

Há um detalhe importante se você recebe **PRs de forks**: por segurança, o GitHub normalmente não entrega os secrets ao workflow desses PRs. Nesse caso, os testes rodam sem segredos e um segundo workflow pode enviar o aviso ao concluir, sem executar código do PR. Evite liberar o token para código de colaboradores externos.

Minha recomendação: **use o CI da plataforma onde seu código já está**. No GitHub, Actions com aviso apenas em caso de falha é o caminho mais direto. Você também pode tornar os testes uma verificação obrigatória antes do merge, se seu plano e repositório permitirem.

## Usuário, turno 2

pera, não entendi. explica de novo?

## Agente, turno 2

Claro. Você precisa de duas peças:

- **Um robô que roda seus testes:** se seu projeto está no GitHub, o GitHub Actions faz isso. Sempre que alguém abrir ou atualizar um PR, ele executa os testes e mostra se passaram ou falharam.
- **Um bot que manda a mensagem:** quando os testes falharem, o Actions pede ao bot do Telegram para te avisar.

Fica assim:

**PR aberto ou atualizado → testes rodam → falhou? Mensagem no Telegram.**

Para isso, você configura uma vez quais comandos rodam os testes e qual bot envia o aviso. Depois funciona sozinho.

**Dá para fazer sem pagar?** Sim, dentro dos limites gratuitos. No GitHub, repositórios públicos têm execução gratuita nas máquinas padrão; os privados têm uma quantidade de minutos incluída por mês. O bot do Telegram é gratuito.

Se seu código já está no GitLab, ele tem uma opção parecida. Usar seu próprio computador também é possível, mas ele precisaria ficar ligado.

**Eu escolheria GitHub Actions + Telegram se seu projeto estiver no GitHub.**
