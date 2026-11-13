import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, symlinkSync, unlinkSync, writeFileSync } from 'node:fs';
import { dirname, join, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const cli = fileURLToPath(new URL('../dist/index.js', import.meta.url));
const workspace = fileURLToPath(new URL('../../work/cli-knowledge-tests/', import.meta.url));
mkdirSync(workspace, { recursive: true });
const project = () => mkdtempSync(join(workspace, 'project-'));
const run = (root, ...args) => spawnSync(process.execPath, [cli, ...args, '--dir', root], { encoding: 'utf8' });
function markdownFiles(root) {
  return readdirSync(root, { recursive: true }).filter(name => name.endsWith('.md')).map(name => join(root, name));
}
function checkLinks(root) {
  for (const file of markdownFiles(root)) {
    let fence;
    for (const line of readFileSync(file, 'utf8').split('\n')) {
      const marker = line.match(/^\s*(`{3,}|~{3,})/);
      if (marker) { fence = fence ? undefined : marker[1][0]; continue; }
      if (fence) continue;
      const targets = [...line.matchAll(/\]\(([^)]+)\)/g)].map(match => match[1]);
      const reference = line.match(/^\s*\[[^\]]+\]:\s*(\S+)/);
      if (reference) targets.push(reference[1]);
      for (const value of targets) {
        const path = value.replace(/^<|>$/g, '').split(/[?#]/)[0];
        if (!path || /^[a-z]+:/i.test(path)) continue;
        const target = resolve(dirname(file), decodeURIComponent(path));
        assert.ok(!relative(root, target).startsWith('..'), `${file}: ${path}`);
        assert.ok(existsSync(target), `${file}: ${path}`);
        if (target.includes(`${join('knowledge', 'harness')}`)) assert.ok(target.startsWith(join(root, 'knowledge/harness')));
      }
    }
  }
}

test('todas as skills dos dois agentes usam somente a biblioteca compartilhada com links válidos', () => {
  const root = project();
  const result = run(root, 'init', '--agents', 'codex,claude-code', '--skills', 'all', '--yes');
  assert.equal(result.status, 0, result.stderr);
  checkLinks(root);
  assert.ok(markdownFiles(root).every(path => !path.replaceAll('\\', '/').includes('/references/knowledge/')));
  for (const agent of ['.agents', '.claude']) {
    const content = readFileSync(join(root, agent, 'skills/consultar-conhecimento/SKILL.md'), 'utf8');
    assert.match(content, /\.\.\/\.\.\/\.\.\/knowledge\/harness\/README.md/);
  }
  assert.match(result.stdout, /Conhecimento compartilhado: 4 guias e um índice/);
});

test('somente Claude instala a biblioteca na raiz e não cria pastas de skills do Codex', () => {
  const root = project();
  const result = run(root, 'init', '--agents', 'claude-code', '--skills', 'criticar,prototipar', '--yes');
  assert.equal(result.status, 0, result.stderr);
  assert.ok(existsSync(join(root, '.claude/skills/consultar-conhecimento/SKILL.md')));
  assert.equal(existsSync(join(root, '.agents')), false);
  assert.ok(existsSync(join(root, 'knowledge/harness/README.md')));
  checkLinks(root);
});

test('a biblioteca só entra quando necessária e knowledge list não altera o projeto', () => {
  const root = project();
  const listed = run(root, 'knowledge', 'list');
  assert.equal(listed.status, 0, listed.stderr);
  assert.match(listed.stdout, /knowledge\/harness\/ux\/usability.md/);
  assert.match(listed.stdout, /consultar-conhecimento/);
  assert.deepEqual(readdirSync(root), []);
  const dry = run(root, 'init', '--agents', 'codex', '--skills', 'consultar-conhecimento', '--dry-run');
  assert.equal(dry.status, 0, dry.stderr);
  assert.match(dry.stdout, /knowledge\/harness\/README.md/);
  assert.deepEqual(readdirSync(root), []);
  assert.equal(run(root, 'init', '--agents', 'codex', '--skills', 'propor', '--yes').status, 0);
  assert.equal(existsSync(join(root, 'knowledge')), false);
  assert.equal(existsSync(join(root, '.agents/skills/consultar-conhecimento')), false);
});

test('adotar outro agente reutiliza os mesmos guias e preserva conhecimento próprio', () => {
  const root = project();
  mkdirSync(join(root, 'knowledge'));
  writeFileSync(join(root, 'knowledge/README.md'), 'Índice do meu projeto');
  writeFileSync(join(root, 'knowledge/decisions.md'), 'Decisões locais');
  assert.equal(run(root, 'init', '--agents', 'codex', '--skills', 'implementar', '--yes').status, 0);
  const guide = join(root, 'knowledge/harness/ux/usability.md');
  const original = readFileSync(guide);
  const result = run(root, 'init', '--agents', 'claude-code', '--skills', 'criticar', '--yes');
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /idêntico: knowledge\/harness\/ux\/usability.md/);
  assert.deepEqual(readFileSync(guide), original);
  assert.equal(readFileSync(join(root, 'knowledge/README.md'), 'utf8'), 'Índice do meu projeto');
  assert.equal(readFileSync(join(root, 'knowledge/decisions.md'), 'utf8'), 'Decisões locais');
});

test('conflito em guia interrompe a instalação inteira e status informa alterações e ausências', () => {
  const root = project();
  assert.equal(run(root, 'init', '--agents', 'codex', '--skills', 'implementar', '--yes').status, 0);
  const guide = join(root, 'knowledge/harness/ux/usability.md');
  writeFileSync(guide, 'Minha adaptação');
  const result = run(root, 'init', '--agents', 'claude-code', '--skills', 'criticar', '--yes');
  assert.notEqual(result.status, 0);
  assert.match(result.stdout, /conflito: knowledge\/harness\/ux\/usability.md/);
  assert.equal(existsSync(join(root, '.claude')), false);
  assert.equal(readFileSync(guide, 'utf8'), 'Minha adaptação');
  unlinkSync(join(root, 'knowledge/harness/accessibility/interface-criteria.md'));
  const status = run(root, 'status');
  assert.equal(status.status, 0, status.stderr);
  assert.match(status.stdout, /alterado: knowledge\/harness\/ux\/usability.md/);
  assert.match(status.stdout, /ausente: knowledge\/harness\/accessibility\/interface-criteria.md/);
});

test('consulta avulsa disponibiliza o índice completo e seus guias', () => {
  const root = project();
  const result = run(root, 'init', '--agents', 'codex', '--skills', 'consultar-conhecimento', '--yes');
  assert.equal(result.status, 0, result.stderr);
  assert.equal(readdirSync(join(root, '.agents/skills')).length, 1);
  checkLinks(root);
});

test('links simbólicos na pasta knowledge são recusados antes da instalação', () => {
  const root = project();
  const outside = project();
  symlinkSync(outside, join(root, 'knowledge'), process.platform === 'win32' ? 'junction' : 'dir');
  const result = run(root, 'init', '--agents', 'codex', '--skills', 'consultar-conhecimento', '--yes');
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /Link simbólico/);
  assert.deepEqual(readdirSync(outside), []);
  assert.equal(existsSync(join(root, '.agents')), false);
});
