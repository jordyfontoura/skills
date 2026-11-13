import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

test('o pacote real instala e roda pelo npm exec sem fontes TypeScript ou Python no consumidor', () => {
  const packageRoot = fileURLToPath(new URL('../', import.meta.url));
  const workspace = fileURLToPath(new URL('../../work/cli-package-tests/', import.meta.url));
  mkdirSync(workspace, { recursive: true });
  const root = mkdtempSync(join(workspace, 'consumer-'));
  const npm = process.env.npm_execpath;
  assert.ok(npm, 'Execute pelo npm test');
  const pack = spawnSync(process.execPath, [npm, 'pack', '--ignore-scripts', '--json', '--pack-destination', root], { cwd: packageRoot, encoding: 'utf8' });
  assert.equal(pack.status, 0, pack.stderr);
  const packed = JSON.parse(pack.stdout);
  // npm 10/11 retornam uma lista; npm 12 indexa os pacotes pelo nome.
  const artifact = Array.isArray(packed) ? packed[0] : packed['@jordyfontoura/skills'];
  const names = artifact.files.map(file => file.path);
  for (const name of ['dist/index.js', 'dist/catalog.js', 'dist/install.js', 'payload.json', 'LICENSE']) assert.ok(names.includes(name), name);
  assert.ok(!names.some(name => name.endsWith('.py') || name.endsWith('.ts') || name.startsWith('test/') || name.includes('node_modules/')));
  writeFileSync(join(root, 'package.json'), JSON.stringify({ private: true }));
  const install = spawnSync(process.execPath, [npm, 'install', join(root, artifact.filename), '--no-audit', '--no-fund'], { cwd: root, encoding: 'utf8' });
  assert.equal(install.status, 0, install.stderr);
  // npm exec usa o mecanismo do npx; offline impede buscar um homônimo no registro.
  const target = join(root, 'project');
  const result = spawnSync(process.execPath, [npm, 'exec', '--offline', '--', 'skills', 'init', '--agents', 'codex,claude-code', '--skills', 'implementar', '--roles', 'planner', '--dir', target, '--yes'], { cwd: root, encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /Instalação concluída/);
  assert.match(readFileSync(join(target, '.agents/skills/implementar/SKILL.md'), 'utf8'), /Implementar/);
  assert.ok(readdirSync(join(target, '.codex/agents')).includes('planner.toml'));
  assert.ok(readdirSync(join(target, '.claude/agents')).includes('planner.md'));
});
