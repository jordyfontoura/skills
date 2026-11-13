# harness

Coleção pessoal de skills reutilizáveis, papéis e práticas de engenharia.
Este é o ponto de entrada do agente. Mantenha-o curto; procedimentos ficam nas skills e na documentação.

## Comandos

- Gerar cópias dos provedores após editar fontes: `python scripts/sync.py`.
- Validar arquivos e cópias dos provedores: `python scripts/check.py` (Python 3.11+).
- Testar o validador: `python -m unittest discover -s scripts`.
- Preparar o CLI: `npm ci --prefix cli`; compilar: `npm run build --prefix cli`.
- Verificar o CLI após o build: `npm run typecheck --prefix cli` e `npm test --prefix cli`.
- Estado local: `git status --short`, `git log -5 --oneline`.
- Não há aplicação web. O CLI opcional fica em `cli/`; veja `cli/README.md`.

## Trabalho

1. Leia o pedido, os arquivos relevantes, as decisões e a última passagem de contexto.
   Retome sua etapa exata; preserve escopo e autorizações estabelecidos.
   Use `reconciliar` para comparar documentos, pendências e implementação.
2. Trabalhe por entregas úteis e verificáveis, com plano curto quando necessário.
   Use `especificar` quando houver incerteza relevante sobre comportamento, contratos ou
   dependências; tamanho do trabalho, sozinho, não exige uma nova especificação.
   Use `entrevistar` para escolhas abertas de escopo ou design. Preserve definições existentes.
   Planejamento rotineiro fica na conversa; consultar `planner` exige necessidade e delegação autorizada.
   Use `entrevistar-por-arquivo` para rodadas em arquivos Markdown, preservando respostas humanas.
   Quando o usuário pedir `propor`, apresente a abordagem na resposta final e aguarde aprovação
   antes de executar; uma autorização genérica anterior não elimina essa espera solicitada.
3. Use `implementar` para entregar partes pequenas e verificáveis. Declare responsabilidade por
   arquivos ao delegar; não sobrescreva mudanças de outro colaborador. Corrija dentro dos
   contratos existentes sem reiniciar o planejamento; revise o conjunto e repita as provas afetadas.
   Quando o pedido priorizar execução direta, use `fazer-direto` no lugar das etapas habituais
   de processo, preservando as Regras e as provas expressamente exigidas.
4. Prove os requisitos pelos métodos combinados e relate comandos e resultados observados.
   Prova ausente continua ausente. Implementação e aceite independente são distintos.
5. Use `passar-contexto` quando outra sessão precisar retomar. Indique próxima etapa e provas pendentes.
   Mantenha trabalho curto na conversa; use documentos existentes para contexto durável.
6. Use `delegar` para divisões autorizadas e `verificar-aceite` para aceite independente.
   Use ferramentas disponíveis e relate limites reais de modelos e provedores.
   Consulte `.agents/models.toml` e `docs/MODELS.md` para selecionar por papel e complexidade;
   a política não autoriza delegação nem muda o modelo da conversa aberta.
   Use `conselho` para análise multidisciplinar solicitada, seguindo as regras existentes.
7. Aplique `escrever-claro` ao redigir ou editar documentos, títulos, descrições e mensagens.
   Preserve fatos e voz pretendida.
8. Use `esclarecer` para esclarecer uma explicação. Retome o contexto em português e use
   `docs/GLOSSARY.md`; uma dúvida não autoriza novas ações.

## Regras

- Nunca enfraqueça, ignore nem remova uma verificação útil só para passar. Corrija a causa.
- Não leia segredos nem arquivos `.env`. Use `.env.example` para nomes de variáveis.
- Altere instruções compartilhadas e configurações de provedor somente no escopo autorizado.
- Permaneça neste repositório, salvo autorização para trabalhar em outro.
- Edite com ferramentas de arquivo; salve código executável de várias linhas antes de rodá-lo.
- Crie branches de trabalho a partir de `nightly` e direcione os PRs para `nightly`, com commits
  pequenos no padrão Conventional Commits. `main` recebe promoções estáveis integrais e hotfixes;
  reintegre hotfixes em `nightly`. Veja o fluxo em `CONTRIBUTING.md`.
  Nunca force um push nem use `--no-verify`.
- Pergunte por escolhas não resolvidas; não reinicie uma entrevista já concluída.
- Execute verificações explicitamente. Não instale hooks automáticos ou serviço de gestão de tarefas.
- Use nomes de skills em português, demais identificadores em inglês e textos de leitura em
  português, conforme `docs/STANDARDS.md`.
- Use `atualizar-harness` para atualizar a coleção em outro projeto sem sobrescrever suas adaptações.

## Índice

- [Harness](docs/HARNESS.md): procedimentos, catálogo e adoção.
- [Arquitetura](docs/ARCHITECTURE.md): fontes e limites entre provedores.
- [Padrões](docs/STANDARDS.md): convenções de nomes, idioma e revisão.
- [Glossário](docs/GLOSSARY.md): vocabulário compartilhado.
- [Modelos](docs/MODELS.md): perfis, complexidade, alternativas e representante.
- [Conhecimento](knowledge/README.md): referências por domínio ou tema, consultadas conforme a tarefa.
- `skills/<grupo>/<nome>/`: fontes de desenvolvimento, produtividade e manutenção do harness.
- `.agents/skills/` e `.claude/skills/`: cópias de uso; `.agents/roles/`: papéis canônicos.

Na compactação, preserve objetivo, etapa, branch, arquivos sob responsabilidade, decisões,
evidências e próxima ação exata. Não invente IDs de tarefa, resultados ou uso de modelos.
