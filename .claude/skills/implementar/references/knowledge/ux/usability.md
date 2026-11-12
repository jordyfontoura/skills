<!-- Gerado de knowledge/ux/usability.md; edite a fonte no harness. -->

# Usabilidade, tarefas e fluxos

- **Tipo:** referência de domínio; os critérios não substituem o procedimento da skill.
- **Aplicabilidade:** interfaces web, nativas e de jogos, conforme o público e suas tarefas.
- **Origem e revisão:** extração do harness em `d3c31c7`, em 12/11/2026.
  As fontes externas não foram reconferidas nesta extração; confirme a versão vigente
  quando ela for decisiva para o julgamento.
- **Limites:** heurísticas e percurso cognitivo orientam a inspeção; não comprovam reação do público.

## 1. Tarefas e fluxos

Inclua as tarefas principais e as de saída: recusar, cancelar, desfazer, excluir e sair.
Percorra cada tarefa e registre desvios, becos sem saída, etapas desnecessárias e perda de
dados ao voltar ou cancelar.

Quando a aprendizagem importar ou a tarefa usar padrões pouco familiares, defina antes a
sequência correta de ações e faça em cada passo as perguntas do percurso cognitivo
(*cognitive walkthrough*):

1. **Intenção:** a pessoa tentará alcançar o resultado certo neste passo?
2. **Visibilidade:** ela perceberá que a ação correta está disponível?
3. **Associação:** ela ligará essa ação ao resultado que deseja?
4. **Retorno:** depois de agir, perceberá que avançou em direção ao objetivo?

Uma resposta "não" indica um achado no passo. Em fluxos convencionais, dispense as perguntas.

## 2. Heurísticas de usabilidade

Examine a interface pelas 10 heurísticas de Nielsen:

1. **Visibilidade do estado do sistema:** o sistema informa o que está acontecendo, a tempo.
2. **Correspondência com o mundo real:** usa a linguagem e as convenções do público, não jargão interno.
3. **Controle e liberdade:** há como desfazer, refazer, cancelar e sair de um caminho indesejado.
4. **Consistência e padrões:** termos, ações e aparência se mantêm no produto e seguem convenções.
5. **Prevenção de erros:** a interface evita condições propensas a erro ou confirma ações arriscadas.
6. **Reconhecer em vez de lembrar:** opções e informações necessárias ficam visíveis quando úteis.
7. **Flexibilidade e eficiência:** atalhos e personalização ajudam o uso frequente sem atrapalhar iniciantes.
8. **Design estético e minimalista:** nada irrelevante compete com a informação essencial da tarefa.
9. **Reconhecer, diagnosticar e recuperar erros:** mensagens dizem o problema em linguagem clara e como continuar.
10. **Ajuda e documentação:** ajuda pesquisável, voltada à tarefa e próxima do contexto, quando necessária.

"Minimalista" não significa cortar informação necessária. Uma violação aparente pode ser uma
convenção que o público já conhece; nesse caso, registre-a só com impacto concreto na tarefa.

## Fontes

- [10 heurísticas de usabilidade, NN/g](https://www.nngroup.com/articles/ten-usability-heuristics/)
  (revisão de 2024 citada na origem). Os resumos são próprios do harness.
- [Percurso cognitivo, NN/g](https://www.nngroup.com/articles/cognitive-walkthroughs/).
