# Fontes e referências do harness

Catálogo das fontes externas e inspirações usadas nas skills, na documentação e nos guias.
Consulte a seção pertinente quando precisar conferir a origem ou a fundamentação de uma
orientação. A execução de uma skill não exige a leitura deste catálogo inteiro.

As datas e versões abaixo são as registradas nos materiais de origem. A centralização não
representa uma nova consulta às fontes externas. Quando a data ou a versão não estiver
registrada, ela permanece desconhecida; confirme a fonte vigente se for decisiva para a tarefa.
Aplicabilidade e limites próprios de cada guia continuam junto dele. As fontes não concedem
autorizações nem transformam escolhas do harness em resultados comprovados.

Links operacionais, como acesso a ferramentas e acervos de assets, continuam nos guias.
Avisos de licença distribuídos com material adaptado são preservados junto desse material.

## Usabilidade

Aplicação: guias `ux/usability.md` e `ux/states-and-content.md`. Extração do harness em
`d3c31c7`, em 12/11/2026; fontes externas não reconferidas nessa extração.

- [10 heurísticas de usabilidade, NN/g](https://www.nngroup.com/articles/ten-usability-heuristics/)
  (revisão de 2024 citada na origem). Os resumos são próprios do harness.
- [Percurso cognitivo, NN/g](https://www.nngroup.com/articles/cognitive-walkthroughs/).

## Estados e conteúdo

Aplicação: guia `ux/states-and-content.md`.

- Fundamentação nas [heurísticas de usabilidade](#usabilidade), catalogadas acima.
- Listas e exemplos adaptados pelo harness; requisitos do projeto e seus guias são consultados no destino.

## Convenções de plataforma

Aplicação: guia `ux/platform-conventions.md`.

- Inventário adaptado do harness em `d3c31c7`.
- Consulte as fontes primárias da plataforma em uso, como Apple Human Interface Guidelines,
  Material Design ou Fluent, e registre URL, versão e data da consulta.

## Direção visual

Aplicação: guias `ux/visual-direction.md` e `ux/motion.md` e convivência com ferramentas
externas descrita em `docs/HARNESS.md`. Fontes consultadas em 17/11/2026.

- [Impeccable, revisão consultada](https://github.com/pbakaus/impeccable/tree/d41d9860b0):
  descoberta em `shape`, preservação de identidade em `polish` e avaliação em `critique`/`audit`.
  Também inspira relacionar movimento à tarefa e preservar retorno em movimento reduzido.
- [UI/UX Pro Max, revisão consultada](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/e59ff376a4):
  busca de direção, geração de design system e exportação de tokens. Saídas são recomendações
  a conferir no contexto do projeto.
- [Design Tokens Format Module 2025.10, DTCG](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/):
  formato para intercâmbio de tokens, sem prescrever a estética de um produto.

As ferramentas não foram executadas nesta pesquisa. A síntese não inclui seus catálogos,
scripts ou playbooks e não comprova ganho de qualidade em comparação com o fluxo anterior.

## Movimento

Aplicação: guia `ux/motion.md`. Fontes consultadas em 17/11/2026.

- Critérios WCAG 2.2: 2.2.2, 2.3.1 e 2.3.3, catalogados em [acessibilidade](#acessibilidade).
- [Desempenho de animações CSS e JavaScript, MDN](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/CSS_JavaScript_animation_performance).
- [gsap.matchMedia(), documentação v3](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/).
- [Licença GSAP](https://gsap.com/community/standard-license/), termos consultados nesta revisão;
  conferir novamente quando a adoção depender deles.
- Impeccable em `d41d9860b0`, catalogado em [direção visual](#direção-visual).

## Acessibilidade

Aplicação: guias `accessibility/interface-criteria.md` e `ux/motion.md`. A base foi extraída
do harness em `d3c31c7`, em 12/11/2026, sem reconferir as fontes externas nessa extração.

- Revisão de movimento em 17/11/2026: explicações W3C dos critérios
  [2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html),
  [2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html) e
  [2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html).
- [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/), recomendação de 12 de dezembro de 2024 citada na origem.
- [WCAG2ICT, W3C](https://www.w3.org/TR/wcag2ict-22/), orientação para software que não é web.

## Padrões de programação de jogos

Aplicação: guia `gamedev/programming-patterns.md`.

Consultadas em 16/11/2026.

- Robert Nystrom, [*Game Programming Patterns*](https://gameprogrammingpatterns.com/contents.html),
  edição web gratuita; um capítulo por padrão.
- Glenn Fiedler, [*Fix Your Timestep!*](https://gafferongames.com/post/fix_your_timestep/), 10/06/2004.
- Godot 4.7: processamento ocioso e de física, interpolação de física, organização de cenas
  e otimização de CPU, catalogados em [engenharia em Godot](#engenharia-em-godot).

## Engenharia em Godot

Aplicação: guias `gamedev/engineering-practices.md`, `gamedev/programming-patterns.md`,
`3d-modeling/game-ready-assets.md` e `3d-modeling/export-pipeline.md`, nas partes pertinentes.

Documentação do Godot 4.7, consultada em 16/11/2026.

- Desempenho: [otimização geral](https://docs.godotengine.org/en/stable/tutorials/performance/general_optimization.html),
  [CPU](https://docs.godotengine.org/en/stable/tutorials/performance/cpu_optimization.html),
  [GPU](https://docs.godotengine.org/en/stable/tutorials/performance/gpu_optimization.html),
  [3D](https://docs.godotengine.org/en/stable/tutorials/performance/optimizing_3d_performance.html) e
  [MultiMesh](https://docs.godotengine.org/en/stable/tutorials/performance/using_multimesh.html).
- Boas práticas: [organização de cenas](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html),
  [cenas e scripts](https://docs.godotengine.org/en/stable/tutorials/best_practices/scenes_versus_scripts.html),
  [alternativas a nós](https://docs.godotengine.org/en/stable/tutorials/best_practices/node_alternatives.html),
  [preferências de dados](https://docs.godotengine.org/en/stable/tutorials/best_practices/data_preferences.html),
  [preferências de lógica](https://docs.godotengine.org/en/stable/tutorials/best_practices/logic_preferences.html),
  [organização de projeto](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html) e
  [controle de versão](https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html).
- Scripts e entrada: [tipagem estática](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html),
  [processamento ocioso e de física](https://docs.godotengine.org/en/stable/tutorials/scripting/idle_and_physics_processing.html),
  [interpolação de física](https://docs.godotengine.org/en/stable/tutorials/physics/interpolation/physics_interpolation_introduction.html) e
  [exemplos de entrada](https://docs.godotengine.org/en/stable/tutorials/inputs/input_examples.html).
- Persistência: [salvar jogos](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html).
- Modelos 3D: [considerações de exportação de modelos](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/model_export_considerations.html),
  [StandardMaterial3D](https://docs.godotengine.org/en/stable/tutorials/3d/standard_material_3d.html),
  [importação de imagens](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_images.html),
  [limitações de renderização 3D](https://docs.godotengine.org/en/stable/tutorials/3d/3d_rendering_limitations.html),
  [LOD de malhas](https://docs.godotengine.org/en/stable/tutorials/3d/mesh_lod.html),
  [descarte por oclusão](https://docs.godotengine.org/en/stable/tutorials/3d/occlusion_culling.html) e
  [retargeting de esqueletos](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/retargeting_3d_skeletons.html).
- Importação de cenas: [formatos disponíveis](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html),
  [personalização de tipos de nó](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/node_type_customization.html) e
  [configuração de importação](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html).

## Game design

Aplicação: guia `gamedev/game-design.md`.

Consultadas em 16/11/2026.

- Robin Hunicke, Marc LeBlanc e Robert Zubek, [*MDA: A Formal Approach to Game Design and Game Research*](https://users.cs.northwestern.edu/~hunicke/MDA.pdf).
  O artigo relata oficinas da GDC de 2001 a 2004.
- Daniel Cook, [*Loops and Arcs*](https://lostgarden.com/2012/04/30/loops-and-arcs/), 30/04/2012, e
  [*The Chemistry of Game Design*](https://www.gamedeveloper.com/design/the-chemistry-of-game-design), 19/07/2007.
- Sid Meier, [*Interesting Decisions*](https://www.gdcvault.com/play/1015756/Interesting), GDC 2012.
- Jenova Chen, [*Flow in Games*](https://www.jenovachen.com/flowingames/designfig.htm), 2006.
- Martin Jonasson e Petri Purho, [*Juice It or Lose It*](https://www.gdcvault.com/play/1016487/Juice-It-or-Lose), GDC Europe 2012.
- Maddy Thorson, [*Celeste & Forgiveness*](https://www.maddymakesgames.com/articles/celeste_and_forgiveness/index.html).
- Matt Allmer, [*The 13 Basic Principles of Gameplay Design*](https://www.gamedeveloper.com/design/the-13-basic-principles-of-gameplay-design), 27/02/2009.
- Liz England, [*The Door Problem*](https://lizengland.com/blog/2014/04/the-door-problem/), 21/04/2014.
- [*The Level Design Book*](https://book.leveldesignbook.com/process/overview), visão geral do processo.
- [*Game Accessibility Guidelines*](https://gameaccessibilityguidelines.com/) e seu
  [nível básico](https://gameaccessibilityguidelines.com/basic/).

## Assets de terceiros

Aplicação: guia `gamedev/asset-sources.md`.

Consultadas em 16/11/2026.

- Kenney: [suporte e licença](https://kenney.nl/support).
- Quaternius: [licença QAL v1.0](https://quaternius.com/license.html).
- itch.io: [listagem de assets](https://itch.io/game-assets).
- CraftPix: [licenças de arquivos](https://craftpix.net/file-licenses/).
- KayKit: [página de assets](https://kaylousberg.com/game-assets) e [perfil no itch.io](https://kaylousberg.itch.io/).
- OpenGameArt: [artigo da Wikipedia](https://en.wikipedia.org/wiki/OpenGameArt.org), fonte
  secundária com aviso de desatualização.
- Poly Haven: [licença](https://polyhaven.com/license).
- ambientCG: [licença](https://docs.ambientcg.com/license/).
- Fab: [licenças e preços](https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab).
- Sketchfab: [modelos gratuitos](https://sketchfab.com/features/free-3d-models).
- Godot: [o que é a Asset Library](https://docs.godotengine.org/en/stable/community/asset_library/what_is_assetlib.html),
  documentação da versão 4.7.
- Sonniss: [licença do pacote GDC](https://sonniss.com/gdc-bundle-license/).
- Freesound: [FAQ](https://freesound.org/help/faq/).
- Pixabay: [resumo da licença](https://pixabay.com/service/license-summary/).
- Incompetech: [licenças](https://incompetech.com/music/royalty-free/licenses/).
- Mixamo: [FAQ da comunidade Adobe](https://community.adobe.com/t5/mixamo-discussions/mixamo-faq-licensing-royalties-ownership-eula-and-tos/td-p/13234775),
  de 29/09/2022.
- game-icons.net: [página inicial](https://game-icons.net/).
- PixelLab: [termos de serviço](https://www.pixellab.ai/termsofservice).

## Modelos 3D

Aplicação: guia `3d-modeling/game-ready-assets.md`.

Consultadas em 16/11/2026.

- Khronos, [especificação glTF 2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html),
  lida no [texto-fonte](https://raw.githubusercontent.com/KhronosGroup/glTF/main/specification/2.0/Specification.adoc).
- Khronos 3D Commerce, [diretrizes de criação de assets em tempo real](https://github.com/KhronosGroup/3DC-Asset-Creation/blob/main/asset-creation-guidelines/RealtimeAssetCreationGuidelines.md),
  versão 2.0.0, de agosto de 2025. As seções completas estão em elaboração e não trazem números.
- Godot 4.7: exportação, materiais, imagens, renderização, LOD, oclusão, retargeting e
  otimização de GPU, catalogados em [engenharia em Godot](#engenharia-em-godot).
- Unity 6.6, [criação de modelos para desempenho ideal](https://docs.unity.com/en-us/engine/current/manual/assets-and-media/asset-types/models/creating-dccassets/modeling-optimized-characters).
- Blender 4.5 LTS, exportador glTF 2.0, catalogado em [exportação 3D](#exportação-3d).
- Não acessadas: a wiki do Polycount (densidade de texel e mapas de normal) e a documentação
  do Unreal Engine.

## Exportação 3D

Aplicação: guia `3d-modeling/export-pipeline.md`.

Consultadas em 16/11/2026.

- Blender 4.5 LTS, [exportador glTF 2.0](https://docs.blender.org/manual/en/4.5/addons/import_export/scene_gltf2.html).
- Khronos, [página do glTF](https://www.khronos.org/gltf/).
- Godot 4.7: formatos, tipos de nó, importação, exportação de modelos, imagens, retargeting
  e controle de versão, catalogados em [engenharia em Godot](#engenharia-em-godot).

## melhorar-harness

Aplicação: skill `melhorar-harness`.

Inspirada em [retro, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md).

## diagnosticar

Aplicação: skill `diagnosticar`.

Inspirada em [diagnosing-bugs, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md).

## prototipar

Aplicação: skill `prototipar`.

Inspirada em [prototype, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md).

## tratar-revisao

Aplicação: skill `tratar-revisao`.

Inspirada em [receiving-code-review, do Superpowers](https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md),
adaptada para escopo explícito, decisões existentes e continuidade de itens independentes.

## integrar

Aplicação: skill `integrar`.

Inspirada em [finishing-a-development-branch, do Superpowers](https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md),
sem menu fixo ou autorização implícita para publicar e limpar ambientes.

## entrevistar-por-arquivo

Aplicação: skill `entrevistar-por-arquivo`.

Este modo se inspira na organização de escolhas por dependência da
[grilling, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills%2Fproductivity%2Fgrilling%2FSKILL.md),
adaptada para respostas em arquivo e encerramento por suficiência.

## escrever-claro

Aplicação: skill `escrever-claro`.

Adaptada de [unslop e technical-writing, do pstack](https://github.com/cursor/plugins/tree/main/pstack/skills),
de Lauren Tan, sob licença MIT. O aviso de copyright e a permissão estão em
`LICENSE-pstack.txt`, distribuído junto da skill.

## Construção de interfaces

Aplicação: apoio `interface.md` de `implementar`.

Inspiração de direção visual: [frontend-design, da Anthropic](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md).
As orientações são adaptadas ao projeto, sem impor a estética da referência.

## Fluxo de trabalho

Aplicação: fundamentação descrita em `docs/HARNESS.md`.

A pesquisa consultada em 04/11/2026 dá apoio delimitado:

- [Geração de testes orientada por contratos, Google/SpecOps 2026](https://arxiv.org/html/2608.17177v2):
  houve melhora na detecção de bugs com custo adicional de tokens. O experimento trata de
  testes sobre bugs históricos; não valida um fluxo obrigatório completo de SDD.
- [Artefatos de especificação em PRs, ESEM 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84):
  o estudo observacional não encontrou proteção contra defeitos ou retrabalho. A medida era
  principalmente referência a issues e tickets, sem observar adoção direta das ferramentas SDD.
- [SDD prescrito e praticado, preprint](https://arxiv.org/html/2608.25202v4): profissionais
  relataram benefícios e custos de planejamento e revisão, com uso seletivo. Os relatos não
  isolam causalidade nem separam os ganhos das melhorias dos modelos.
- [Experimento de harness para aplicações longas, Anthropic](https://www.anthropic.com/research/harness-design-long-running-apps):
  o autor simplificou a coordenação ao mudar de modelo e preservou planejamento e avaliação.
  É um experimento interno, não uma validação universal nem uma receita de configuração.

## Avaliação de interfaces

Aplicação: fundamentação descrita em `docs/HARNESS.md`.

O método de interface parte da [avaliação heurística](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/)
e da [escala de severidade da NN/g](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/),
que fundamentam a inspeção e a reavaliação por vários avaliadores. As definições de 1 a 3,
os pisos, a regra de barreiras e a mediana são escolhas deste harness. O
[resumo de 33 estudos da MeasuringU](https://measuringu.com/evaluator-effect/), fonte
secundária, relata concordância mediana de 27% entre dois avaliadores humanos.
Na comparação de [Duan et al., CHI 2024](https://arxiv.org/abs/2403.13139), o GPT-4 teve
precisão menor que especialistas humanos (0,60 contra 0,83) e recall um pouco maior. Os erros
incluíram regras fora de contexto, duplicatas, descartes reapresentados, correções vagas e
leitura visual incorreta sem interface renderizada; a utilidade caiu nas iterações. As regras
de `criticar` respondem a esses erros, sem medição de ganho nem garantia de que os resultados
se apliquem a outros modelos.

## Avaliação iterativa

Aplicação: fundamentação descrita em `docs/HARNESS.md`.

As regras de `subir-regua` partem destes estudos, nenhum deles com esta sequência de etapas.
Em revisão iterativa de redações, [Pan et al., 2024](https://arxiv.org/abs/2407.04549),
preprint, observaram a nota do avaliador subir enquanto a nota humana estagnava ou caía,
sobretudo com contexto compartilhado entre autor e avaliador; um avaliador sem o histórico
acompanhou as pessoas. Daí o contexto novo e a ausência de notas anteriores.
[Panickssery et al., NeurIPS 2024](https://arxiv.org/abs/2404.13076), mostraram que modelos
avaliam melhor os próprios textos do que textos equivalentes para pessoas, e
[Verga et al., 2024](https://arxiv.org/abs/2404.18796), preprint, que avaliadores de famílias
diferentes têm menos viés do que um único avaliador grande; daí a alternância de famílias e
o aviso de independência. [Gao et al., 2022](https://arxiv.org/abs/2210.10760), preprint,
viram a otimização de uma medida substituta acabar reduzindo a qualidade real, como prevê a
lei de Goodhart; daí a regra da referência e o limite de ciclos. No Self-Refine,
[Madaan et al., NeurIPS 2023](https://arxiv.org/abs/2303.17651), as primeiras rodadas
concentraram os ganhos, o que sustenta o padrão de 3 ciclos por etapa.

## Estimativas de duração

Aplicação: fundamentação descrita em `docs/HARNESS.md`.

Essa é uma convenção do harness para tornar a consulta mais útil. A
[NN/g](https://www.nngroup.com/articles/designing-for-waits-and-interruptions/) recomenda
mostrar etapas feitas e restantes quando uma estimativa razoável não está disponível.
Um [estudo exploratório de workshop](https://arxiv.org/html/2604.00010v1) encontrou dificuldades
de modelos ao prever sua própria duração; suas tarefas predominantemente curtas não validam
previsões durante goals longos. As fontes motivam cautela, não comprovam calibração local.

## Pesquisa e conselho

Aplicação: fundamentação descrita em `docs/HARNESS.md`.

As adaptações usam como referências
os [métodos de busca da Cochrane](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04)
e o [estudo de conformidade em agentes de Choi et al.](https://arxiv.org/abs/2506.01332).
A Cochrane trata de revisões de intervenções; o estudo, de debates
simulados sobre temas controversos. A aplicação ao harness é uma escolha de projeto, sem
prova de ganho neste ambiente. Esses contextos não impõem requisitos a toda conversa ou busca.
