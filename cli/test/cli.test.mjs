import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, symlinkSync, unlinkSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { applyPlan, planInstall } from '../dist/install.js';
import { payload } from '../dist/catalog.js';

const cli = fileURLToPath(new URL('../dist/index.js', import.meta.url));
const workspace = fileURLToPath(new URL('../../work/cli-tests/', import.meta.url));
mkdirSync(workspace, { recursive: true });
const project = () => mkdtempSync(join(workspace, 'project-'));
const run = (root, ...args) => spawnSync(process.execPath, [cli, ...args, '--dir', root], { encoding: 'utf8' });
const files = root => readdirSync(root, { recursive: true }).filter(name => {
  try { return readFileSync(join(root, name)) !== undefined; } catch { return false; }
});

test('o CLI lista todo o catálogo e rejeita entradas inválidas sem criar arquivos', () => {
  const root = project();
  const list = run(root, 'list');
  assert.equal(list.status, 0, list.stderr);
  for (const name of ['implementar', 'fazer-direto', 'planner', 'representative']) assert.ok(list.stdout.includes(name));
  for (const args of [[], ['init', '--yes'], ['init', '--agents', 'codex', '--skills', '../escape', '--yes'],
    ['init', '--agents', 'other', '--skills', 'implementar', '--yes'], ['unknown']]) {
    assert.notEqual(run(root, ...args).status, 0);
    assert.deepEqual(readdirSync(root), []);
  }
});

test('simulação e falta de confirmação não gravam nem criam o projeto', () => {
  const root = join(project(), 'novo');
  const args = ['init', '--agents', 'codex,claude-code', '--skills', 'implementar'];
  const dry = run(root, ...args, '--dry-run');
  assert.equal(dry.status, 0, dry.stderr);
  assert.match(dry.stdout, /Simulação concluída/);
  assert.equal(existsSync(root), false);
  assert.notEqual(run(root, ...args).status, 0);
  assert.equal(existsSync(root), false);
});

test('instala referências completas nos dois agentes, registra origem e é idempotente', () => {
  const root = project();
  const args = ['init', '--agents', 'codex,claude-code', '--skills', 'implementar', '--yes'];
  const result = run(root, ...args);
  assert.equal(result.status, 0, result.stderr);
  for (const agent of ['.agents', '.claude']) {
    const path = join(root, agent, 'skills/implementar');
    assert.ok(existsSync(join(path, 'SKILL.md')));
    assert.ok(existsSync(join(path, 'testing.md')));
    assert.ok(existsSync(join(path, 'references/knowledge/ux/usability.md')));
    // Todos os links locais do pacote apontam para arquivos presentes.
    for (const name of files(path).filter(name => name.endsWith('.md'))) {
      const content = readFileSync(join(path, name), 'utf8');
      for (const match of content.matchAll(/\]\(([^)]+)\)/g)) {
        const target = match[1].replace(/^<|>$/g, '').split('#')[0];
        if (!target || /^[a-z]+:/.test(target)) continue;
        assert.ok(existsSync(resolve(dirname(join(path, name)), decodeURIComponent(target))), `${name}: ${target}`);
      }
    }
  }
  assert.equal(existsSync(join(root, 'AGENTS.md')), false);
  const receipts = readdirSync(join(root, '.harness/receipts'));
  const receipt = JSON.parse(readFileSync(join(root, '.harness/receipts', receipts[0]), 'utf8'));
  assert.match(receipt.source.sha, /^[a-f0-9]{40}$/);
  assert.equal(receipt.source.repository, 'https://github.com/jordyfontoura/skills');
  assert.equal(receipt.files['.agents/skills/implementar/SKILL.md'], createHash('sha256').update(readFileSync(join(root, '.agents/skills/implementar/SKILL.md'))).digest('hex'));
  const before = files(root).map(name => [name, readFileSync(join(root, name), 'utf8')]);
  const repeated = run(root, ...args);
  assert.equal(repeated.status, 0, repeated.stderr);
  assert.match(repeated.stdout, /0 arquivos criados/);
  assert.deepEqual(files(root).map(name => [name, readFileSync(join(root, name), 'utf8')]), before);
});

test('conflitos impedem toda a instalação e preservam as adaptações', () => {
  const root = project();
  mkdirSync(join(root, '.agents/skills/implementar'), { recursive: true });
  const path = join(root, '.agents/skills/implementar/SKILL.md');
  writeFileSync(path, 'Minha adaptação');
  const result = run(root, 'init', '--agents', 'codex', '--skills', 'implementar,propor', '--yes');
  assert.notEqual(result.status, 0);
  assert.match(result.stdout, /conflito:/);
  assert.equal(readFileSync(path, 'utf8'), 'Minha adaptação');
  assert.equal(existsSync(join(root, '.agents/skills/propor')), false);
  assert.equal(existsSync(join(root, '.harness')), false);
});

test('papéis incluem apoio, modelos existentes são preservados e instruções são apenas sugeridas', () => {
  const root = project();
  mkdirSync(join(root, '.agents'));
  writeFileSync(join(root, '.agents/models.toml'), 'Minha política');
  writeFileSync(join(root, 'AGENTS.md'), 'Minhas instruções');
  const result = run(root, 'init', '--agents', 'codex,claude-code', '--skills', 'none', '--roles', 'all', '--models', '--yes');
  assert.equal(result.status, 0, result.stderr);
  for (const role of ['planner', 'evaluator', 'representative']) {
    assert.ok(existsSync(join(root, `.codex/agents/${role}.toml`)));
    assert.ok(existsSync(join(root, `.claude/agents/${role}.md`)));
  }
  for (const name of ['especificar', 'delegar', 'verificar-aceite', 'implementar']) assert.ok(existsSync(join(root, `.agents/skills/${name}/SKILL.md`)));
  assert.equal(readFileSync(join(root, '.agents/models.toml'), 'utf8'), 'Minha política');
  assert.equal(readFileSync(join(root, 'AGENTS.md'), 'utf8'), 'Minhas instruções');
  const empty = project();
  assert.equal(run(empty, 'init', '--agents', 'codex', '--skills', 'none', '--models', '--yes').status, 0);
  const policy = readFileSync(join(empty, '.agents/models.toml'), 'utf8');
  assert.match(policy, /provider = "inherit"/);
  assert.doesNotMatch(policy, /claude-opus|gpt-6/);
});

test('status identifica arquivos ausentes e alterados e preserva recibos anteriores em adoções parciais', () => {
  const root = project();
  assert.match(run(root, 'status').stdout, /Nenhuma instalação/);
  assert.equal(run(root, 'init', '--agents', 'codex', '--scenarios', 'sessions', '--yes').status, 0);
  const file = join(root, '.agents/skills/andamento/SKILL.md');
  writeFileSync(file, 'Adaptação');
  unlinkSync(join(root, '.agents/skills/implementar/testing.md'));
  assert.equal(run(root, 'init', '--agents', 'codex', '--skills', 'propor', '--yes').status, 0);
  assert.equal(readdirSync(join(root, '.harness/receipts')).length, 2);
  const status = run(root, 'status');
  assert.equal(status.status, 0, status.stderr);
  assert.match(status.stdout, /alterado: .agents\/skills\/andamento\/SKILL.md/);
  assert.match(status.stdout, /ausente: .agents\/skills\/implementar\/testing.md/);
  assert.match(status.stdout, /íntegro: .agents\/skills\/propor\/SKILL.md/);
  assert.equal(readFileSync(file, 'utf8'), 'Adaptação');
});

test('links simbólicos no destino são rejeitados antes da escrita', () => {
  const root = project();
  const outside = project();
  symlinkSync(outside, join(root, '.agents'), process.platform === 'win32' ? 'junction' : 'dir');
  const result = run(root, 'init', '--agents', 'codex', '--skills', 'propor', '--yes');
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /Link simbólico/);
  assert.deepEqual(readdirSync(outside), []);
});

test('uma mudança após a prévia não é sobrescrita e desfaz arquivos criados pela operação', async () => {
  const root = project();
  const plan = await planInstall(root, { agents: ['codex'], skills: ['implementar'], roles: [], models: false });
  const last = plan.entries.at(-1);
  const conflict = join(root, last.path);
  mkdirSync(dirname(conflict), { recursive: true });
  writeFileSync(conflict, 'Alteração concorrente');
  await assert.rejects(applyPlan(plan), /EEXIST/);
  assert.equal(readFileSync(conflict, 'utf8'), 'Alteração concorrente');
  assert.deepEqual(files(root), [last.path.replaceAll('/', process.platform === 'win32' ? '\\' : '/')]);
});

test('todo o payload leva as mesmas cópias geradas e todas as recomendações existem', () => {
  const root = fileURLToPath(new URL('../../', import.meta.url));
  for (const [path, content] of Object.entries(payload.files)) {
    const source = path === '.agents/models.toml' ? '.agents/models.example.toml' : path;
    assert.equal(content, readFileSync(join(root, source), 'utf8').replaceAll('\r\n', '\n'), path);
  }
  for (const scenario of ['approval', 'direct', 'sessions', 'reviews', 'decisions', 'acceptance', 'interface']) {
    const result = run(project(), 'init', '--agents', 'codex', '--scenarios', scenario, '--dry-run');
    assert.equal(result.status, 0, result.stderr);
  }
});
