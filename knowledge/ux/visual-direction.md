# Direção visual e tokens

- **Tipo:** referência de domínio; recomendações contextuais, sem autorizar redesign.
- **Aplicabilidade:** criação ou refinamento de interfaces web, nativas e de jogos. Consulte
  quando a direção estiver aberta ou quando for preciso avaliar coerência visual.
- **Origem e revisão:** síntese própria a partir das fontes abaixo, consultadas em 17/11/2026.
  Impeccable em `d41d9860b0`; UI/UX Pro Max em `e59ff376a4`; DTCG no formato 2025.10.
- **Limites:** os playbooks orientam escolhas; não demonstram superioridade estética,
  usabilidade com pessoas nem conformidade de acessibilidade. Paletas por categoria de
  produto são hipóteses de direção, não resultados de pesquisa com o público do projeto.

## Partir da tarefa e da identidade

Uma direção útil relaciona público, tarefa, conteúdo e composição. Uma tela para operar
dados pode priorizar densidade e comparação; uma apresentação pode explorar imagens e
ritmo. A finalidade informa a escolha, sem impor uma estética para toda a categoria.

O design system existente é o ponto de partida: tokens, componentes, conteúdo e padrões
de interação. Refinamento preserva essa identidade; mudança de identidade pertence ao
escopo de redesign. Uma ferramenta externa não decide essa mudança.

Quando a direção estiver aberta, estes elementos ajudam a explicar uma proposta curta:

- Público, tarefa principal e resultado esperado.
- Conteúdo real, extremos de tamanho e estados relevantes.
- O que preservar e quais características se pretende explorar ou evitar, com motivo.
- Hierarquia, densidade, cores, tipografia, espaçamento e movimento pertinentes à tarefa.
- Referências visuais e o aspecto específico aproveitado de cada uma.

Por exemplo, numa tabela financeira, alinhar números e distinguir totais pode ajudar mais
que acrescentar cartões decorativos. Isso é um exemplo contextual, não uma regra para
todo produto financeiro. Consulte [hierarquia, estados e conteúdo](states-and-content.md).

## Traduzir a direção em escolhas reutilizáveis

- **Cor:** distinguir papéis como fundo, superfície, texto, ação, borda e foco. Conferir
  os pares reais de primeiro plano e fundo em cada tema e estado; uma paleta isolada não
  demonstra contraste. Não depender só da cor para comunicar estado.
- **Tipografia:** relacionar escala, peso, entrelinha e largura de leitura à hierarquia e
  à densidade. Conferir acentos, números, idiomas, fallback e ampliação. Verificar licença
  e forma de distribuição das fontes antes de incorporá-las.
- **Espaçamento e composição:** usar relações consistentes para agrupamento, alinhamento e
  ritmo. A densidade precisa acomodar o conteúdo e as entradas da plataforma; espaço vazio
  em excesso também pode dificultar comparação e descoberta.
- **Componentes:** cobrir foco, seleção, desabilitado e demais estados pertinentes. Corrigir
  inconsistências na origem compartilhada quando a causa estiver no token ou componente.
- **Movimento:** explicar mudança ou retorno de uma ação, com alternativa adequada a quem
  reduz movimento. Consulte [movimento e animação](motion.md) quando houver animação.

Tokens são nomes reutilizáveis para decisões visuais. Reaproveite o formato e os nomes
do projeto; papéis semânticos, como `color.text.primary`, expressam o uso esperado melhor
que um nome ligado apenas ao valor. Uma exportação DTCG pode ajudar na troca entre ferramentas,
mas não exige migrar o sistema existente. O formato DTCG 2025.10 é um relatório de grupo
comunitário, não uma recomendação normativa do W3C.

As decisões e os tokens específicos ficam no projeto de destino, junto da fonte já adotada.
`MASTER.md`, `DESIGN.md` ou um arquivo exportado por ferramenta só ajudam quando têm uma
função definida; criar documentos concorrentes não integra o tema ao código. Mapear valores
gerados para tokens existentes e substituir usos avulsos faz parte dessa integração.

## Avaliar coerência sem impor gosto

Cartões repetidos, efeitos e tipografia sem relação com o conteúdo podem indicar uma escolha
genérica. Investigue o efeito na hierarquia, compreensão ou consistência antes de apontar
defeito. Gradientes, fontes comuns ou cantos arredondados não são problemas por si sós.

Compare a interface renderizada com a direção combinada, nos tamanhos, temas e estados em
escopo. Use conteúdo real e extremos. Meça contraste com cores efetivas; capturas não provam
operação por teclado nem acesso com tecnologia assistiva. Consulte os
[critérios por forma de acesso](../accessibility/interface-criteria.md).

## Fontes

- [Impeccable, revisão consultada](https://github.com/pbakaus/impeccable/tree/d41d9860b0):
  descoberta em `shape`, preservação de identidade em `polish` e avaliação em `critique`/`audit`.
- [UI/UX Pro Max, revisão consultada](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/e59ff376a4):
  busca de direção, geração de design system e exportação de tokens. Saídas são recomendações
  a conferir no contexto do projeto.
- [Design Tokens Format Module 2025.10, DTCG](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/):
  formato para intercâmbio de tokens, sem prescrever a estética de um produto.

As ferramentas não foram executadas nesta pesquisa. A síntese não inclui seus catálogos,
scripts ou playbooks e não comprova ganho de qualidade em comparação com o fluxo anterior.
