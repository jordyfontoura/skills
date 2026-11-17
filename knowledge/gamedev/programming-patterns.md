# Padrões de programação de jogos

- **Tipo:** referência de domínio; síntese de fontes, sem valor de regra de arquitetura.
- **Aplicabilidade:** estrutura de laço, entidades, comunicação entre sistemas e otimização
  em jogos, com correspondências no Godot.
- **Origem e revisão:** pesquisa na internet em 16/11/2026. As intenções vêm da edição web de
  *Game Programming Patterns*, de Robert Nystrom, traduzidas aqui; a documentação do Godot é a da versão 4.7.
- **Limites:** um padrão responde a um problema. Sem o problema, ele só acrescenta código.
  As correspondências com o Godot marcadas como interpretação são do harness, não da documentação.

## Como usar

Identifique primeiro o problema: acoplamento, ordem de atualização, custo de memória ou tempo.
Depois procure o padrão que o resolve e leia a coluna de cuidados. Em otimização, meça antes:
o livro condiciona Data Locality e Flyweight a um gargalo confirmado por profiler.

## Sequenciamento

| Padrão | Intenção | Cuidado |
| --- | --- | --- |
| Game Loop | Desacoplar o avanço do tempo de jogo da entrada do usuário e da velocidade do processador. | Está entre os trechos mais sensíveis a desempenho. Em plataformas com laço de eventos próprio, coordene com ele. |
| Update Method | Simular uma coleção de objetos independentes mandando cada um processar um quadro de comportamento por vez. | A ordem de atualização importa. Adicionar ou remover objetos durante a atualização exige cuidado. |
| Double Buffer | Fazer uma série de operações sequenciais parecer instantânea ou simultânea. | A troca precisa ser atômica. Dois buffers custam o dobro de memória. |

### Passo fixo de simulação

Glenn Fiedler, em *Fix Your Timestep!* (2004), descreve o problema e a solução:

- Um passo variável faz a simulação se comportar de modo diferente conforme a taxa de quadros.
- Limitar o passo variável ajuda, mas pode causar uma "espiral da morte" quando a simulação
  não acompanha o tempo real.
- A solução é simular em passos fixos e guardar o tempo de quadro num acumulador: o
  renderizador "produz" tempo e a simulação o "consome" em passos de tamanho fixo.
- O resto do acumulador vira um fator para interpolar entre o estado anterior e o atual
  antes de desenhar, o que elimina o tremor visual.

## Padrões clássicos revisitados

Esses capítulos do livro não têm seção de intenção; o resumo abaixo é do harness.

| Padrão | Ideia | Cuidado |
| --- | --- | --- |
| Command | Uma chamada de método transformada em objeto, útil para remapear entrada, desfazer e repetir. | Instâncias sem estado duplicadas desperdiçam memória; compartilhe-as. |
| Flyweight | Compartilhar entre muitos objetos os dados que não mudam por instância. | Dados compartilhados devem ser imutáveis. Meça antes de trocar uma solução simples. |
| Observer | Avisar interessados sobre um evento sem que o emissor os conheça. | A notificação é síncrona: um observador lento bloqueia o emissor. Observadores esquecidos vazam memória. |
| Prototype | Criar objetos copiando um modelo existente. | Cópia rasa ou profunda é uma decisão difícil; o ganho de código costuma ser pequeno. |
| Singleton | Garantir uma única instância com acesso global. | É estado global: dificulta raciocínio, aumenta acoplamento e atrapalha concorrência. O livro recomenda evitar. |
| State | Trocar o comportamento de um objeto conforme seu estado, com máquinas de estados. | Máquinas de estados finitas ficam difíceis de manter em IA complexa. |

## Comportamento

| Padrão | Intenção | Cuidado |
| --- | --- | --- |
| Bytecode | Dar ao comportamento a flexibilidade dos dados, codificando-o como instruções de uma máquina virtual. | O livro o chama de seu padrão mais complexo. Exige ferramenta de autoria e perde o depurador habitual. |
| Subclass Sandbox | Definir comportamento numa subclasse usando operações fornecidas pela classe base. | A classe base acumula código e se acopla a tudo. Quando crescer demais, mova operações para componentes. |
| Type Object | Permitir criar "classes" novas com uma única classe, em que cada instância representa um tipo de objeto. | Comportamento específico por tipo fica mais difícil, pois o tipo guarda dados em vez de sobrescrever métodos. |

## Desacoplamento

| Padrão | Intenção | Cuidado |
| --- | --- | --- |
| Component | Permitir que uma entidade abranja vários domínios sem acoplá-los entre si. | A comunicação entre componentes fica mais complexa, e cada um acrescenta uma indireção. |
| Event Queue | Desacoplar o momento em que um evento é enviado do momento em que é processado. | Uma fila central é uma variável global. O mundo pode mudar antes do processamento. Tratadores que enviam eventos podem criar laços. |
| Service Locator | Dar um ponto global de acesso a um serviço sem acoplar os usuários à classe concreta. | Use com parcimônia; defina o que acontece quando o serviço está ausente. Prefira passar o objeto quando for prático. |

Se a necessidade é só desacoplar quem recebe a mensagem, o livro indica Observer ou Command
como soluções mais simples que uma fila.

## Otimização

| Padrão | Intenção | Cuidado |
| --- | --- | --- |
| Data Locality | Acelerar o acesso à memória organizando os dados para aproveitar o cache da CPU. | Só aplique com falhas de cache confirmadas como gargalo. Chamadas virtuais e ponteiros trabalham contra. |
| Dirty Flag | Evitar trabalho desnecessário adiando-o até que o resultado seja preciso. | O trabalho adiado pode causar uma pausa visível. Toda alteração no dado primário precisa marcar a flag. |
| Object Pool | Melhorar desempenho e uso de memória reutilizando objetos de um conjunto fixo. | Dimensione o conjunto. Objetos reutilizados não são limpos sozinhos e podem reter referências. |
| Spatial Partition | Localizar objetos com eficiência guardando-os numa estrutura organizada por posição. | Só compensa com muitos objetos e consultas frequentes. Objetos em movimento exigem reorganizar a estrutura. |

## Correspondências no Godot

Sustentadas pela documentação do Godot 4.7:

- **Game Loop e Update Method:** o motor chama `_process(delta)` a cada quadro desenhado e
  `_physics_process(delta)` em taxa fixa, 60 vezes por segundo por padrão. Use o segundo para
  o que envolve o motor de física.
- **Passo fixo com interpolação:** a interpolação de física é opcional e vem desativada. Ela
  interpola entre a transformação anterior e a atual, com saída atrasada de um a dois ticks.
  A documentação recomenda fixar a taxa de ticks no projeto em vez de adaptá-la ao hardware.
- **Observer:** sinais. A documentação os indica para reagir a algo, não para iniciar comportamento.
- **Singleton:** autoloads. A documentação os reserva para sistemas que controlam os próprios
  dados, precisam de acesso global e existem isoladamente.
- **Object Pool:** a documentação sugere reutilizar objetos em C# para reduzir pausas do
  coletor de lixo.

Interpretação do harness, sem confirmação na documentação lida:

- **Component:** a composição por cenas e nós cumpre papel semelhante.
- **Type Object e Flyweight:** um `Resource` compartilhado entre instâncias guarda dados de tipo.
- **Spatial Partition:** o motor já particiona o espaço para física e renderização; escreva
  a sua estrutura só para consultas próprias que o motor não atende.

## Fontes

Consultadas em 16/11/2026.

- Robert Nystrom, [*Game Programming Patterns*](https://gameprogrammingpatterns.com/contents.html),
  edição web gratuita; um capítulo por padrão.
- Glenn Fiedler, [*Fix Your Timestep!*](https://gafferongames.com/post/fix_your_timestep/), 10/06/2004.
- Godot 4.7: [processamento ocioso e de física](https://docs.godotengine.org/en/stable/tutorials/scripting/idle_and_physics_processing.html),
  [interpolação de física](https://docs.godotengine.org/en/stable/tutorials/physics/interpolation/physics_interpolation_introduction.html),
  [organização de cenas](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html) e
  [otimização de CPU](https://docs.godotengine.org/en/stable/tutorials/performance/cpu_optimization.html).
