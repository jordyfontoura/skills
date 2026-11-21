# Amostras

Respostas reais de agentes a cenários fixos, com e sem as skills deste repositório. Elas ficam
versionadas para que o diff de um PR mostre o efeito de uma mudança nas skills. A leitura é
de quem revisa: nenhuma amostra aprova ou reprova uma mudança sozinha.

## Estrutura

```text
samples/
  models.toml                    modelos usados; o nome vira a pasta do resultado
  <cenário>/
    scenario/
      scenario.toml              skills que o cenário exercita e se há acesso à internet
      turns/01.md, 02.md, ...    mensagens do usuário, em ordem
      workspace/                 opcional: arquivos que existem quando a conversa começa
    METRICS.md                   tabela com o consumo de cada execução
    <modelo>/
      without-skills/            execução sem skill nenhuma do repositório
      with-skills/               execução com as skills do repositório
        transcript.md            a conversa inteira
        run.json                 modelo, skills acionadas, métricas e hash das entradas
        files/                   arquivos que o agente criou ou alterou
```

Compare `without-skills` e `with-skills` lado a lado para ver se a skill ajuda. Leia o diff de
`with-skills` num PR para ver o que a mudança alterou.

## Gerar

Requer Python 3.11 ou mais recente e os CLIs `claude` e `codex` autenticados. As execuções
consomem a cota das suas assinaturas.

```text
python scripts/samples.py run              gera só as ausentes ou desatualizadas
python scripts/samples.py run --dry-run    lista o que seria gerado
python scripts/samples.py run --scenario postagem-rede-social --model opus-5.5-medium
python scripts/samples.py run --all        gera tudo de novo
python scripts/samples.py check            acusa amostras desatualizadas, sem chamar modelos
```

Cada amostra guarda um hash das suas entradas, e o comando só gera de novo quando ele muda:

- `without-skills` depende do cenário e do modelo.
- `with-skills` depende também das skills listadas em `scenario.toml` e dos arquivos do
  repositório que elas referenciam. Com `skills = []`, depende de todas as skills e de `knowledge/`.

Use `--all` para procurar efeitos de uma mudança em cenários de outras skills. A CI roda
`check` nos PRs para `main`.

## Criar um cenário

1. Crie `samples/<nome>/scenario/scenario.toml` com `skills = ["<skill>"]`. Acrescente
   `web = true` se o cenário depender de busca na internet; sem isso, os agentes rodam sem ela.
2. Escreva as mensagens em `scenario/turns/`, uma por arquivo. Escreva o pedido como você o
   faria numa conversa, sem citar a skill: assim a amostra também mostra se a descrição da
   skill faz o agente acioná-la. `run.json` registra as skills acionadas.
3. Se a conversa partir de arquivos existentes, coloque-os em `scenario/workspace/`.
4. Rode `python scripts/samples.py run --scenario <nome>` e inclua o resultado no commit.

Num cenário com vários turnos, todos são executados de novo a cada geração, na mesma sessão.

## Como a execução é isolada

Cada execução acontece numa pasta temporária, com as skills da pasta pessoal fora de alcance:

- **Claude Code:** `--setting-sources project` ignora as skills e as instruções pessoais. Em
  `with-skills`, o repositório entra como plugin por `--plugin-dir`. O agente lê e edita
  arquivos, mas não tem terminal. Busca e leitura de páginas só existem com `web = true`.
  A execução falha se uma skill pessoal aparecer ou se o plugin não carregar.
- **Codex:** as skills de `~/.agents/skills` e `~/.codex/skills` são desativadas só naquela
  execução. Em `with-skills`, `.agents/skills/` e `knowledge/` são copiados para a pasta
  temporária. O agente roda com o sandbox `workspace-write`. A busca nativa fica desligada
  sem `web = true`, e o recurso de apps, que também oferece busca, fica sempre desligado.
  O `config.toml` pessoal continua valendo, porque o sandbox depende dele; servidores MCP
  configurados ali ficam disponíveis nas duas variantes.

As skills embutidas nos CLIs e nos plugins de cada provedor continuam disponíveis nas duas
variantes. O `AGENTS.md` de `~/.codex`, quando existe, também vale para as duas.

## Limites

- Cenários com `web = true` variam mais: os resultados de busca mudam com o tempo e cada
  provedor usa a própria ferramenta de busca.
- Os CLIs não permitem fixar a temperatura. Duas execuções iguais produzem textos diferentes;
  parte de todo diff é variação do modelo.
- Os tokens de entrada incluem as instruções do próprio agente, e o tempo varia entre
  execuções. Compare variantes do mesmo modelo e desconfie de diferenças pequenas.
- `estimated_cost_usd` aparece só nas execuções do Claude e segue o preço da API, não o da
  assinatura.
- A amostra depende da versão do CLI, registrada em `run.json`.
