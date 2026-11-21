# harness

Coleção pessoal de skills reutilizáveis, papéis e práticas de engenharia.
Este arquivo traz o que o repositório não mostra sozinho. Os procedimentos ficam nas skills,
escolhidas pela descrição de cada uma.

## Comandos

- Gerar cópias dos provedores após editar fontes: `python scripts/sync.py`.
- Validar arquivos e cópias dos provedores: `python scripts/check.py` (Python 3.11+).
- Testar o validador: `python -m unittest discover -s scripts`.
- Preparar o CLI: `npm ci --prefix cli`; compilar: `npm run build --prefix cli`.
- Verificar o CLI após o build: `npm run typecheck --prefix cli` e `npm test --prefix cli`.
- Não há aplicação web. O CLI opcional fica em `cli/`; veja `cli/README.md`.

## Convenções

- Edite as fontes em `skills/<grupo>/<nome>/` e os papéis em `.agents/roles/`. As cópias em
  `.agents/skills/` e `.claude/skills/` são geradas por `sync.py`.
- Crie branches de trabalho a partir de `nightly` e direcione os PRs para `nightly`, com commits
  pequenos no padrão Conventional Commits. `main` recebe promoções estáveis integrais e hotfixes;
  reintegre hotfixes em `nightly`. Veja o fluxo em `CONTRIBUTING.md`.
  Não force um push nem use `--no-verify`.
- Use nomes de skills em português, demais identificadores em inglês e textos de leitura em
  português, conforme `docs/STANDARDS.md`. Aplique `redigir` a documentos, títulos,
  descrições e mensagens.
- Quando o usuário pedir `propor`, apresente a abordagem e aguarde aprovação antes de executar,
  mesmo que haja uma autorização genérica anterior.
- Delegar exige autorização. Para escolher modelo por papel, consulte `knowledge/agents/model-selection.md` e
  `docs/MODELS.md`; a política não autoriza delegação nem muda o modelo da conversa aberta.
- Relate comandos e resultados observados. Implementação concluída não é aceite independente.

## Limites

- Não enfraqueça nem remova uma verificação útil para fazê-la passar.
- Não leia segredos nem arquivos `.env`. Use `.env.example` para nomes de variáveis.
- Altere instruções compartilhadas e configurações de provedor somente no escopo autorizado.
- Permaneça neste repositório, salvo autorização para trabalhar em outro.
- Edite com ferramentas de arquivo; salve código executável de várias linhas antes de rodá-lo.
- Execute verificações explicitamente. Não instale hooks automáticos nem serviço de gestão de tarefas.

## Índice

- [Harness](docs/HARNESS.md): procedimentos, catálogo e adoção.
- [Arquitetura](docs/ARCHITECTURE.md): fontes e limites entre provedores.
- [Padrões](docs/STANDARDS.md): convenções de nomes, idioma e revisão.
- [Glossário](docs/GLOSSARY.md): vocabulário compartilhado.
- [Modelos](docs/MODELS.md): perfis, complexidade, alternativas e representante.
- [Conhecimento](knowledge/README.md): referências por domínio ou tema, consultadas conforme a tarefa.
