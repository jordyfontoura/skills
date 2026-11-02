# Changelog

Mudanças relevantes para quem usa ou adota a coleção. O formato segue o
[Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/). As versões seguem o
[SemVer](https://semver.org/lang/pt-BR/); na série 0.x, uma versão MINOR pode quebrar
compatibilidade.

## [0.1.0] - 2026-11-01

### Adicionado

- Primeira versão pública, com 26 skills e 3 papéis em português.
- Plugin `jordyfontoura-skills` no marketplace `jordyfontoura`, para Claude Code e Codex.
  O Codex não recebe os papéis pelo plugin.
- `.agents/models.example.toml`, uma política de modelos que herda o ambiente.

### Mudado

- Skills e papéis citam outras skills e papéis pelo nome, sem links entre pastas. Cada skill
  funciona copiada sozinha.
- A origem passa a ser [jordyfontoura/skills](https://github.com/jordyfontoura/skills).

### Origem

Esta versão começa um histórico novo. Ela corresponde à revisão abaixo do repositório privado
anterior, `jordyfontoura/harness`, que fica arquivado. A árvore publicada difere dela apenas
por esta seção do CHANGELOG.

- Revisão anterior: `jordyfontoura/harness@c647efa3b0fc88e94b8afa32a80ddf67de9c7c0a`.

### Renomeações anteriores à publicação

Projetos que adotaram versões antigas por cópia podem encontrar estes nomes:

- `retro` passou a se chamar `improve-harness`.
- `pera-ai` passou a se chamar `clarify`.
- O modo assíncrono de `interview` (`interview/async.md`) virou a skill `interview-async`.
- `alinhamento.template.md`, em `interview-async`, passou a se chamar `alignment.template.md`.
