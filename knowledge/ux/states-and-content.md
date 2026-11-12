# Hierarquia visual, estados, conteúdo e escolha

- **Tipo:** referência de domínio; os critérios não substituem o procedimento da skill.
- **Aplicabilidade:** interfaces em implementação, prototipação ou crítica, com o design system do projeto.
- **Origem e revisão:** extração do harness em `d3c31c7`, em 12/11/2026.
  As fontes externas não foram reconferidas nesta extração; confirme a versão vigente
  quando ela for decisiva para o julgamento.
- **Limites:** a relevância de estados, temas e localização depende da jornada; convenções e impacto precisam ser conferidos no contexto.

## 4. Hierarquia visual, layout e consistência

- A ação principal e a informação necessária para a tarefa se destacam na ordem certa.
- Tipografia, espaçamento, alinhamento e proximidade agrupam o que é relacionado e não sugerem
  relações falsas.
- A densidade combina com o conteúdo e o contexto de uso.
- Tokens, componentes, grade e padrões seguem o design system; aparência e imagens seguem o
  guia de marca, quando houver.
- Ícones e símbolos têm significado claro ou rótulo quando não forem convencionais.
- Dados e gráficos representam valores sem distorção, com unidade, legenda próxima, números
  alinhados para comparação e tabelas que permitem ordenar e acompanhar cabeçalhos.

Quando o problema vier de um componente ou regra do design system, indique isso na recomendação:
a correção pertence à origem, não só à tela.

## 5. Conteúdo, confiança e escolha

- Rótulos, botões e títulos dizem o que acontece, com termos consistentes.
- Mensagens de erro, confirmação e estados vazios explicam a situação e o próximo passo.
- Ações com consequências diferentes têm nomes diferentes; ações destrutivas deixam claro o efeito.
- Voz e tom seguem o guia de conteúdo, quando houver.
- Textos não prometem o que o produto não cumpre.
- Recusar, cancelar e excluir têm acesso e peso equivalentes a aceitar. A interface não usa:
  - opções pré-marcadas contra o interesse da pessoa;
  - urgência ou escassez falsas;
  - custos revelados tarde;
  - culpa na recusa;
  - pedidos repetidos após uma recusa;
  - consentimento enviesado.

Um padrão que leva a pessoa a escolher contra o próprio interesse causa dano, mesmo que
melhore uma métrica do produto. Para revisar ou reescrever textos, aplique a skill `escrever-claro`.

## 6. Estados, interação e adaptação

- Estados da jornada: carregando, vazio, parcial, sucesso, erro, sem permissão e indisponível.
- Entradas preservadas após erro, quando possível.
- Componentes interativos com estados distinguíveis: repouso, foco, *hover* onde houver
  ponteiro, pressionado, selecionado e desabilitado. Cada ação tem retorno imediato.
- Movimento que explica mudanças de estado, sem atrasar a tarefa.
- Tamanhos de tela e orientação, sem sobreposição nem perda de ações essenciais.
- Tema escuro, alto contraste e tamanho de texto do sistema, quando suportados.
- Conteúdo real e extremos: textos longos, listas vazias ou grandes.
- Em produtos localizados: idioma, direção da direita para a esquerda, formatos locais de data,
  número e moeda, e expansão de textos traduzidos.

## Fontes

- [10 heurísticas de usabilidade, NN/g](https://www.nngroup.com/articles/ten-usability-heuristics/).
- Listas e exemplos adaptados pelo harness; requisitos do projeto e seus guias são consultados no destino.
