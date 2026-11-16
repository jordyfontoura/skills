<!-- Gerado de knowledge/3d-modeling/game-ready-assets.md; edite a fonte no harness. -->

# Modelos 3D prontos para jogo

- **Tipo:** referência de domínio; recomendações contextuais, não um orçamento técnico.
- **Aplicabilidade:** modelagem, UVs, materiais, rig e otimização de modelos 3D para
  renderização em tempo real, com foco em glTF e Godot.
- **Origem e revisão:** pesquisa na internet em 16/11/2026: especificação glTF 2.0,
  diretrizes Khronos 3D Commerce 2.0.0, documentação do Godot 4.7 e manual do Unity 6.6.
- **Limites:** nenhuma fonte lida fixa orçamento de triângulos, densidade de texel ou
  margem entre ilhas de UV; esses números dependem da plataforma e do projeto. O trecho
  sobre densidade de texel é prática corrente, sem fonte conferida.

## 1. Escala, eixos e origem

- Modele em escala real. No glTF, as distâncias são em metros.
- O glTF usa sistema destro com +Y para cima; a frente do asset aponta para +Z. O Godot
  também é destro com Y para cima, e a câmera olha para -Z.
- No Blender, +Z é para cima e a frente do modelo aponta para -Y. O exportador converte os eixos.
- As diretrizes da Khronos recomendam a origem no centro da base do objeto, em 0,0,0.
- Aplique as transformações do objeto antes de exportar.

## 2. Geometria

- Use a geometria necessária para a silhueta e a deformação, sem excesso. Menos polígonos
  rendem mais.
- O motor conta mais vértices que o programa de modelagem: vértices se dividem em costuras
  de UV e arestas duras.
- O exportador glTF do Blender converte quads e n-gons em triângulos. O Godot também
  triangula na importação, mas o resultado pode ser imprevisível com n-gons; a documentação
  recomenda um modificador Triangulate aplicado na exportação.
- Em dispositivos móveis, evite concentrar muitos vértices numa área pequena da tela.

## 3. UVs

- Mantenha as UVs entre 0 e 1 quando a textura for exclusiva do modelo.
- Para lightmaps, o Godot gera o segundo canal de UV na importação quando a malha é
  marcada para iluminação estática.
- **Densidade de texel** (prática corrente, sem fonte conferida): mantenha uma proporção
  parecida de pixels de textura por metro entre os objetos de uma mesma cena, para que
  nenhum pareça borrado ao lado de outro. Defina o valor no projeto.

## 4. Materiais e texturas

O glTF usa o modelo PBR metálico-rugoso, com estes canais:

| Textura | Canal | Codificação |
| --- | --- | --- |
| Cor base | RGB | sRGB; o alfa é linear. |
| Oclusão | R | Linear; 0 é totalmente ocluído. |
| Rugosidade | G | Linear. |
| Metalicidade | B | Linear. |
| Normal | RGB para XYZ | Espaço tangente, linear. |

- Oclusão, rugosidade e metalicidade podem dividir uma única imagem (ORM).
- Metalicidade costuma ser branca (metal) ou preta (não metal).
- O Godot exige mapas de normal no estilo OpenGL, com X+, Y+ e Z+. Mapas no estilo DirectX
  precisam do eixo Y invertido; a importação tem a opção Normal Map Invert Y.
- O Godot usa só os canais vermelho e verde do mapa de normal. No glTF, o azul não deve
  ser menor ou igual a 0,5.
- Quando o modelo não traz tangentes, o glTF manda calculá-las com o algoritmo MikkTSpace;
  o Godot faz isso na importação. Asse os mapas de normal com a mesma base tangente.
- Guarde os originais em formato sem perdas, como PNG, e deixe a compressão para a importação.

Tamanho e memória, segundo a documentação do Godot:

- A maioria dos jogos 3D atuais usa texturas de 2048×2048 em média.
- GPUs móveis costumam se limitar a 4096×4096; acima de 8192×8192, dispositivos antigos
  podem não dar suporte.
- A compressão em VRAM reduz o uso de memória de 4 a 6 vezes e é o padrão para 3D.
- Mipmaps são recomendados em 3D e aumentam a memória em cerca de 33%.

## 5. Transparência

- A ordenação de objetos transparentes usa a origem do nó, não cada polígono, e pode falhar
  em malhas grandes ou cruzadas.
- Para texturas quase todas opacas ou quase todas transparentes, como folhagem, prefira
  Alpha Scissor.
- Separe a parte transparente numa superfície com material próprio.

## 6. Rig e animação

- Limite a quatro as influências de ossos por vértice. O glTF guarda quatro por conjunto de
  atributos, e o Unity recomenda o mesmo máximo.
- Prefira uma única malha com skin por personagem. Segundo o Unity, duas podem quase dobrar
  o tempo de renderização.
- Menos ossos custam menos. No Unity, 15 ossos a mais num rig de 30 custam cerca de 50%
  mais operações.
- Exporte o esqueleto na pose de repouso. Para compartilhar animações entre humanoides no
  Godot, use T-pose, o modelo voltado para +Z e nomes de ossos em inglês comum; o
  mapeamento automático reconhece os ossos pelo nome.
- Exporte só os ossos de deformação; a documentação do Godot avisa que os demais causam
  sombreamento incorreto.
- Use na importação a mesma taxa de quadros da animação original. Acima de 30 FPS há
  pouco ganho.

## 7. LOD, oclusão e colisão

- O Godot gera níveis de detalhe na importação, com a biblioteca meshoptimizer. Não é
  preciso modelar LODs à mão na maioria dos casos.
- A geração automática pode causar defeitos, principalmente em malhas com skin. Nesses
  casos, desative-a para a malha ou use intervalos de visibilidade com LODs feitos à mão.
- O descarte por oclusão rende mais em interiores com muitos cômodos pequenos. Só malhas
  com material opaco entram no cálculo dos oclusores.
- Para colisão, prefira poucas formas primitivas a malhas de triângulos ou convexas.
  Marque as malhas de colisão com os sufixos descritos no
  [pipeline de exportação](export-pipeline.md).

## 8. Antes de entregar o modelo

1. A escala está em metros e as transformações foram aplicadas.
2. A origem está no ponto esperado, em geral o centro da base.
3. A malha não tem n-gons que possam triangular mal.
4. As UVs estão entre 0 e 1 e sem sobreposição indesejada.
5. Os mapas seguem os canais do glTF e o normal está no estilo OpenGL.
6. Cada vértice tem no máximo quatro influências e o esqueleto está na pose de repouso.
7. A origem e a licença de texturas e modelos de terceiros estão registradas, conforme as
   [fontes de assets](../gamedev/asset-sources.md).

## Fontes

Consultadas em 16/11/2026.

- Khronos, [especificação glTF 2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html),
  lida no [texto-fonte](https://raw.githubusercontent.com/KhronosGroup/glTF/main/specification/2.0/Specification.adoc).
- Khronos 3D Commerce, [diretrizes de criação de assets em tempo real](https://github.com/KhronosGroup/3DC-Asset-Creation/blob/main/asset-creation-guidelines/RealtimeAssetCreationGuidelines.md),
  versão 2.0.0, de agosto de 2025. As seções completas estão em elaboração e não trazem números.
- Godot 4.7: [considerações de exportação de modelos](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/model_export_considerations.html),
  [StandardMaterial3D](https://docs.godotengine.org/en/stable/tutorials/3d/standard_material_3d.html),
  [importação de imagens](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_images.html),
  [limitações de renderização 3D](https://docs.godotengine.org/en/stable/tutorials/3d/3d_rendering_limitations.html),
  [LOD de malhas](https://docs.godotengine.org/en/stable/tutorials/3d/mesh_lod.html),
  [descarte por oclusão](https://docs.godotengine.org/en/stable/tutorials/3d/occlusion_culling.html),
  [retargeting de esqueletos](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/retargeting_3d_skeletons.html) e
  [otimização de GPU](https://docs.godotengine.org/en/stable/tutorials/performance/gpu_optimization.html).
- Unity 6.6, [criação de modelos para desempenho ideal](https://docs.unity.com/en-us/engine/current/manual/assets-and-media/asset-types/models/creating-dccassets/modeling-optimized-characters).
- Blender 4.5 LTS, [exportador glTF 2.0](https://docs.blender.org/manual/en/4.5/addons/import_export/scene_gltf2.html).
- Não acessadas: a wiki do Polycount (densidade de texel e mapas de normal) e a documentação
  do Unreal Engine.
