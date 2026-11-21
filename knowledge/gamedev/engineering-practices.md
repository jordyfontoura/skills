# Práticas de engenharia em jogos com Godot

- **Tipo:** referência de domínio; recomendações contextuais, não uma política do projeto.
- **Aplicabilidade:** desempenho, organização de cenas e código, dados, entrada, persistência
  e versionamento em projetos Godot. Os princípios de medição valem para outros motores.
- **Origem e revisão:** pesquisa na internet em 16/11/2026, na documentação do Godot 4.7.
- **Limites:** síntese de páginas oficiais; nomes de opções podem mudar entre versões. Duas
  páginas usadas estão marcadas pela própria documentação como possivelmente desatualizadas
  (preferências de dados e MultiMesh). Decisões do projeto prevalecem sobre este guia.

## 1. Desempenho

### Medir antes de otimizar

- Meça com profiler e deixe a medição guiar cada mudança.
- Ataque o maior gargalo, meça de novo e repita.
- O projeto pesa mais que o polimento: algoritmos e estruturas de dados ruins não se
  corrigem depois com ajustes pequenos.
- O gargalo pode estar na GPU, e um profiler de CPU pode não mostrá-lo. O tempo de quadro é
  definido pelo mais lento dos dois.
- O tempo de desenvolvimento é limitado, e código otimizado costuma ser mais difícil de ler.
  Otimize onde importa.

### CPU

- Inicie e pare o profiler embutido manualmente; ele reduz a velocidade do projeto.
- Para medir um trecho à mão, use `Time.get_ticks_usec()` e repita a função mil vezes ou
  mais para obter uma média.
- Todo nó tem custo. Remover um nó da árvore com `Node.remove_child(node)` pode render mais
  que pausá-lo ou escondê-lo.
- Para volumes muito grandes, as APIs de servidor dispensam a árvore de cena.
- GDScript privilegia facilidade. C# é rápido, mas pode pausar no coletor de lixo. C++ é o
  mais rápido e o mais trabalhoso de distribuir.
- Na física, use formas de colisão simples. A documentação recomenda 60 Hz para movimento em
  tempo real; reduzir a taxa economiza CPU e causa tremor e atraso de entrada.

### GPU e 3D

- Reduza chamadas de desenho e trocas de estado. Reutilize materiais e shaders.
- Use o mínimo de objetos transparentes. Eles são desenhados de trás para frente e não
  aproveitam o Z-buffer. Dê à parte transparente uma superfície e um material próprios.
- Em dispositivos móveis, evite concentrar vértices em áreas pequenas da tela e use LOD.
- Para saber se o limite é a taxa de preenchimento, desligue o V-Sync e compare o FPS numa
  janela grande e numa muito pequena.
- Texturas 3D são comprimidas em VRAM por padrão. Desative essa compressão em pixel art.
- Considere iluminação pré-calculada, principalmente em dispositivos móveis.
- Use MultiMesh para milhares de objetos idênticos, como grama. A visibilidade vale para o
  conjunto inteiro; divida-o por áreas quando precisar de descarte por região.
- Reduza a taxa de animação de malhas distantes ou ocultas, com `VisibleOnScreenEnabler3D`.
- Teste cedo e com frequência no dispositivo mais fraco que o jogo precisa atender.

## 2. Cenas e código

- Projete cenas sem dependências externas. Quando uma cena precisar do contexto, injete-o:
  conecte um sinal, chame um método, atribua um `Callable`, uma referência ou um `NodePath`.
- Irmãos conhecem só a própria hierarquia; um ancestral intermedeia a comunicação entre eles.
- Estrutura inicial sugerida: um nó `Main` com os filhos `World` (o jogo) e `GUI` (a
  interface). Troque os filhos de `World` para mudar de fase.
- Use um autoload só para um sistema que controla os próprios dados, precisa de acesso
  global e existe isoladamente.
- Cena para um conceito específico do jogo; script com `class_name` para uma ferramenta
  reutilizável. Cenas montam hierarquias de nós mais rápido que scripts.
- Nem tudo precisa ser nó. `Object` é o mais leve e exige liberar memória à mão;
  `RefCounted` se libera sozinho; `Resource` serializa e aparece no Inspector.
- A tipagem estática detecta erros sem executar, melhora o autocompletar e, segundo a
  documentação, melhora o desempenho do GDScript. Os avisos `UNTYPED_DECLARATION` e
  `INFERRED_DECLARATION` ajudam a exigi-la.
- `as` devolve `null` em silêncio quando o tipo não confere. Use `is` ou `assert()` quando a
  conversão precisar ser garantida.

## 3. Dados e carregamento

- `Array` itera rápido e insere ou remove bem no fim; no início é lento. `Dictionary` é o
  mais rápido para buscar, inserir e apagar por chave; buscar por valor é lento.
- Defina as propriedades de um nó antes de adicioná-lo à árvore, pois alguns setters
  executam código lento. A posição global é exceção: só existe depois de entrar na árvore.
- `preload` carrega junto com o script; `load()` carrega no ponto da chamada. Use uma
  variável quando o recurso puder mudar ou precisar ser liberado.
- Fases estáticas servem a jogos pequenos. Em jogos médios e grandes, carregue e descarregue
  partes dinamicamente e divida as cenas em partes menores.

## 4. Laço, física e entrada

- `_process(delta)` roda a cada quadro desenhado; `_physics_process(delta)` roda em taxa
  fixa. Multiplique velocidades por `delta`.
- A interpolação de física suaviza o movimento entre ticks. Em jogos de reflexo rápido, o
  atraso de um a dois ticks pode pesar: desative-a ou aumente a taxa de ticks.
- Use `_input()` para eventos pontuais, como pular, e `Input.is_action_pressed()` em
  `_physics_process` para entrada contínua, como andar.
- Declare ações no InputMap, com nomes em snake_case, em vez de testar teclas diretamente.

## 5. Projeto e versionamento

- Agrupe os assets perto das cenas que os usam, como em `characters/player/`.
- Use snake_case em pastas e arquivos e PascalCase em nomes de nós. Scripts C# seguem o
  nome da classe.
- Mantenha recursos de terceiros em `addons/`.
- O sistema de arquivos empacotado do Godot diferencia maiúsculas de minúsculas; Windows e
  macOS, por padrão, não. Nomes em minúsculas evitam erros que só aparecem no jogo exportado.
- Um arquivo `.gdignore` vazio numa pasta impede a importação do conteúdo.
- No Git, ignore `.godot/` e `*.translation`. O `.gitattributes` gerado pelo Godot força
  finais de linha LF.
- Configure o Git LFS antes de commitar binários grandes, por exemplo com
  `git lfs track "*.glb"`.

## 6. Persistência

- O tutorial oficial marca os nós a salvar com o grupo `Persist`. Cada nó oferece um método
  `save()` que devolve um dicionário, gravado como uma linha JSON em `user://`.
- JSON não guarda `Vector2`, `Vector3`, `Color` nem classes próprias sem conversão.
  `FileAccess.store_var` é a alternativa binária.
- Nós aninhados exigem carregar os pais antes dos filhos.
- Para configurações do usuário, use `ConfigFile`.

## 7. Assets de terceiros

Registre origem, autor e licença de cada asset, conforme as
[fontes de assets](asset-sources.md). Para estruturar sistemas, consulte os
[padrões de programação](programming-patterns.md).

## Fontes

[Fontes e referências de engenharia em godot](../references.md#engenharia-em-godot).
