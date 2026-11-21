# Pipeline de exportação do Blender para o Godot

- **Tipo:** referência de domínio; descreve opções das ferramentas, não um fluxo obrigatório.
- **Aplicabilidade:** escolha de formato, exportação do Blender e importação de cenas 3D e
  texturas no Godot.
- **Origem e revisão:** pesquisa na internet em 16/11/2026, no manual do Blender 4.5 LTS e
  na documentação do Godot 4.7.
- **Limites:** nomes de opções mudam entre versões; confira a versão em uso. O guia não
  cobre Unity nem Unreal Engine, cuja documentação não pôde ser lida.

## 1. Formato

| Formato | Situação no Godot | Observação |
| --- | --- | --- |
| glTF 2.0 (`.gltf`, `.glb`) | Recomendado. | Padrão aberto da Khronos, também norma ISO/IEC 12113:2022. |
| `.blend` | Suportado. | O Godot chama o exportador glTF do Blender; exige o Blender instalado e não funciona nos editores Android e web. |
| FBX | Suportado. | Importado pela biblioteca ufbx desde o Godot 4.3. |
| OBJ | Limitado. | Sem pivôs, esqueletos, animações, UV2 nem materiais PBR. |
| DAE (Collada) | Antigo. | Para cenas animadas ou complexas, a documentação recomenda glTF. |

Use `.glb` quando quiser um único arquivo e `.gltf` quando quiser as texturas separadas.

## 2. Exportar do Blender

- **Material:** o exportador lê a cor base de um nó Principled BSDF. O glTF aceita o
  modelo metálico-rugoso e materiais sem iluminação.
- **ORM:** o glTF espera metalicidade no canal azul, rugosidade no verde e oclusão no
  vermelho, que podem dividir a mesma imagem. Ligue a textura com um nó Separate RGB e
  marque a imagem como Non-Color.
- **Oclusão assada:** use o grupo de nós `glTF Material Output`, com a entrada `Occlusion`.
- **Normal:** mantenha o nó Normal Map em Tangent Space, o único tipo que o glTF aceita.
- **Eixos:** a opção Y Up exporta na convenção do glTF, com +Y para cima.
- **Modificadores:** Apply Modifiers exporta a malha já avaliada. Quads e n-gons viram
  triângulos na exportação.
- **Animação:** o modo padrão exporta as ações ativas ou guardadas em faixas NLA. O modo NLA
  Tracks exporta cada faixa como uma animação glTF independente.
- **Shape keys:** são exportadas como morph targets.
- **Propriedades personalizadas:** vão para o campo `extras` do objeto no arquivo glTF.

## 3. Sufixos de importação do Godot

O Godot converte nós conforme o sufixo no nome do objeto. O separador pode ser `-`, `$` ou
`_`, sem diferenciar maiúsculas de minúsculas.

| Sufixo | Efeito |
| --- | --- |
| `-noimp` | Remove o nó na importação. |
| `-col` | Acrescenta uma colisão estática com a geometria da própria malha: precisa e lenta. |
| `-convcol` | Como `-col`, com forma convexa. |
| `-colonly` | Remove a malha e deixa só a colisão estática. |
| `-convcolonly` | Como `-colonly`, com forma convexa por decomposição. |
| `-occ` | Acrescenta um oclusor e mantém a malha. |
| `-occonly` | Converte a malha em oclusor. |
| `-navmesh` | Converte a malha em malha de navegação. |
| `-rigid` | Vira um `RigidBody3D`. |
| `-vehicle` e `-wheel` | Viram `VehicleBody3D` e `VehicleWheel3D`. |
| `loop` ou `cycle` | Marca a animação como repetida. No Blender, vai no nome da ação. |
| `-alpha` | Material com transparência alfa. |
| `-vcol` | Material que usa a cor de vértice como albedo. |

A documentação aconselha poucas formas primitivas de colisão em vez de malhas de
triângulos ou convexas.

## 4. Opções de importação de cena

- **Root Type:** tipo do nó raiz; prefira um tipo derivado de `Node3D`.
- **Apply Root Scale:** aplica a escala às malhas e animações, em vez de ao nó raiz.
- **Ensure Tangents:** gera tangentes com MikkTSpace quando a malha não as traz.
- **Generate LODs:** gera versões de menor detalhe para exibir à distância.
- **Create Shadow Meshes:** gera malhas simplificadas para sombras.
- **Light Baking:** com Static Lightmaps, gera a UV2 para assar lightmaps.
- **Animation FPS:** use a mesma taxa do programa de modelagem.

O Godot não grava sobre o arquivo 3D original. Ajustes feitos no editor ficam nas opções
de importação ou numa cena herdada.

## 5. Importar texturas

| Modo | Quando usar |
| --- | --- |
| Lossless | Padrão para 2D; recomendado para pixel art. |
| Lossy | Assets 2D grandes. |
| VRAM Compressed | Padrão para 3D; reduz a memória de 4 a 6 vezes. |
| VRAM Uncompressed | Formatos que não comprimem, como imagens de ponto flutuante. |
| Basis Universal | Arquivos menores, com qualidade inferior à do VRAM Compressed. |

- Com Detect 3D, a textura usada em 3D passa a VRAM Compressed e ganha mipmaps.
- Mapas de normal no estilo DirectX precisam de Normal Map Invert Y.
- Process > Size Limit reduz a textura na importação, útil para dispositivos móveis.

## 6. Esqueletos e animações compartilhadas

- O Godot traz o perfil `SkeletonProfileHumanoid` para mapear ossos de humanoides.
- O perfil espera T-pose, o modelo voltado para +Z, sem transformação no nó e com o eixo
  +Y de cada osso apontando do pai para o filho.
- A opção Overwrite Axis é, segundo a documentação, a mais importante para compartilhar
  animações. Fix Silhouette corrige modelos em A-pose.

## 7. Versionamento

Rastreie binários como `.glb` e texturas com Git LFS, configurado antes do primeiro commit
desses arquivos. A documentação do Godot dá o exemplo `git lfs track "*.glb"`.

## 8. Conferência antes de exportar

1. O modelo cumpre os itens de [modelos 3D prontos para jogo](game-ready-assets.md).
2. Os nomes dos objetos trazem os sufixos de colisão, oclusão e navegação desejados.
3. As ações de animação têm nomes definitivos e as repetidas levam `loop`.
4. Câmeras e luzes de trabalho ficam fora da exportação; a documentação do Godot recomenda
   montar a iluminação no editor.
5. Depois de importar, a escala, a orientação e os materiais foram conferidos numa cena de teste.

## Fontes

[Fontes e referências de exportação 3d](../references.md#exportação-3d).
