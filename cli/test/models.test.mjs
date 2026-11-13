import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, symlinkSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { payload } from '../dist/catalog.js';
import { createPolicy } from '../dist/models.js';
import { serializePolicy, validatePolicyV2 } from '../dist/policy.js';

const cli = fileURLToPath(new URL('../dist/index.js', import.meta.url));
const workspace = fileURLToPath(new URL('../../work/cli-models-tests/', import.meta.url));
mkdirSync(workspace, { recursive: true });
const project = () => mkdtempSync(join(workspace, 'project-'));
const run = (root, ...args) => spawnSync(process.execPath, [cli, 'models', 'init', ...args, '--dir', root], { encoding: 'utf8' });
const fixture = JSON.parse(readFileSync(new URL('./fixtures/policy-cases.json', import.meta.url), 'utf8'));
function applyCase(case_) {
  const policy = structuredClone(fixture.base);
  for (const change of case_.changes) {
    let target = policy;
    for (const key of change.path.slice(0, -1)) target = target[key];
    if (change.delete) delete target[change.path.at(-1)];
    else target[change.path.at(-1)] = structuredClone(change.value);
  }
  return policy;
}

test('TypeScript aceita e recusa os mesmos casos de contrato compartilhados com Python', () => {
  for (const case_ of fixture.cases) {
    const policy = applyCase(case_);
    if (case_.valid) assert.doesNotThrow(() => validatePolicyV2(policy), case_.name);
    else assert.throws(() => validatePolicyV2(policy), undefined, case_.name);
  }
});

test('os geradores e a serialização TOML preservam valores e passam no validador Python', () => {
  const generated = ['shared', 'profiles'].map(layout => ({ name: layout, policy: createPolicy(layout) }));
  const custom = createPolicy('profiles');
  custom.profiles.default.candidates = [
    { provider: 'tool-a', model: 'model-a', effort: 'custom' },
    { provider: 'tool-b', model: 'local/model:v1', effort: 'inherit' },
  ];
  custom.profiles.council = structuredClone(custom.profiles.evaluator);
  custom.roles.council.profile = 'council';
  generated.push({ name: 'perfil separado para conselho e alternativas ordenadas', policy: custom });
  const cases = [...fixture.cases.filter(c => c.valid).map(c => ({ name: c.name, policy: applyCase(c) })), ...generated];
  const input = cases.map(c => ({ ...c, toml: serializePolicy(c.policy) }));
  input.push({ name: 'neutra exata', policy: payload.modelTemplate, toml: payload.files['.agents/models.toml'] });
  const checker = fileURLToPath(new URL('../../scripts/check_cli_policy.py', import.meta.url));
  const result = spawnSync('python', [checker], { input: JSON.stringify(input), encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr || result.error?.message);
  assert.match(result.stdout, /políticas aceitas/);
  for (const { policy } of generated) {
    assert.equal(Object.keys(policy.roles).length, 7);
    for (const name of ['evaluator', 'representative', 'council']) assert.equal(policy.roles[name].complexity, undefined);
  }
});

test('models init cria o exemplo neutro sem pedir agente ou skills e registra origem', () => {
  const root = project();
  const result = run(root, '--neutral', '--yes');
  assert.equal(result.status, 0, result.stderr);
  assert.equal(readFileSync(join(root, '.agents/models.toml'), 'utf8'), payload.files['.agents/models.toml']);
  assert.ok(existsSync(join(root, '.harness/receipts')));
  assert.equal(existsSync(join(root, '.agents/skills')), false);
  const again = run(root, '--neutral', '--yes');
  assert.equal(again.status, 0, again.stderr);
  assert.match(again.stdout, /preservado, não validado/);
  assert.equal(readdirSync(join(root, '.harness/receipts')).length, 1);
});

test('JSON personalizado gera perfis sem depender de nomes de provedores conhecidos', () => {
  const parent = project();
  const root = join(parent, 'destino');
  const policy = createPolicy('profiles');
  policy.profiles.default.candidates = [{ provider: 'external-driver', model: 'local/model:v2', effort: 'external-effort' }];
  const config = join(parent, 'policy.json');
  writeFileSync(config, JSON.stringify(policy));
  const result = run(root, '--config', config, '--yes');
  assert.equal(result.status, 0, result.stderr);
  const content = readFileSync(join(root, '.agents/models.toml'), 'utf8');
  assert.equal(content, serializePolicy(policy));
  assert.match(result.stdout, /não foram verificados/);
});

test('simulação, impressão e falta de confirmação não criam nem o diretório de destino', () => {
  const root = join(project(), 'destino');
  const printed = run(root, '--neutral', '--print');
  assert.equal(printed.status, 0, printed.stderr);
  assert.equal(printed.stdout, payload.files['.agents/models.toml']);
  assert.equal(run(root, '--neutral', '--dry-run').status, 0);
  assert.notEqual(run(root, '--neutral').status, 0);
  assert.notEqual(run(root, '--yes').status, 0);
  assert.equal(existsSync(root), false);
});

test('arquivos existentes são mantidos byte a byte, inclusive v1, comentários e conteúdo inválido', () => {
  for (const content of [Buffer.from('# Comentário local\r\nversion = 1\r\n[defaults]\r\nprovider = "inherit"\r\nmodel = "inherit"\r\neffort = "inherit"\r\n[roles.implementer]\r\nwhen = "Implementar."\r\nfallbacks = []\r\n'),
    Buffer.from('# Personalização local\r\n' + payload.files['.agents/models.toml'].replaceAll('\n', '\r\n')),
    Buffer.from('\ufeff# Outra política\r\nversion = 2\r\n'), Buffer.from([0, 255, 1])]) {
    const root = project();
    mkdirSync(join(root, '.agents'));
    const path = join(root, '.agents/models.toml');
    writeFileSync(path, content);
    const result = run(root, '--yes');
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /preservado, não validado/);
    const printed = run(root, '--neutral', '--print');
    assert.equal(printed.status, 0, printed.stderr);
    assert.equal(printed.stdout, payload.files['.agents/models.toml']);
    assert.deepEqual(readFileSync(path), content);
    assert.equal(existsSync(join(root, '.harness')), false);
  }
});

test('políticas inválidas são recusadas antes de qualquer escrita', () => {
  for (const case_ of fixture.cases.filter(c => !c.valid)) {
    const parent = project();
    const root = join(parent, 'destino');
    const config = join(parent, 'policy.json');
    writeFileSync(config, JSON.stringify(applyCase(case_)));
    const result = run(root, '--config', config, '--yes');
    assert.notEqual(result.status, 0, case_.name);
    assert.equal(existsSync(root), false, case_.name);
  }
});

test('models init recusa links no destino e combinações ambíguas de opções', () => {
  const root = project();
  const outside = project();
  symlinkSync(outside, join(root, '.agents'), process.platform === 'win32' ? 'junction' : 'dir');
  assert.notEqual(run(root, '--neutral', '--yes').status, 0);
  assert.deepEqual(readdirSync(outside), []);
  for (const args of [['--neutral', '--config', 'policy.json'], ['--agents', 'codex'], ['--config', '.env']]) {
    const empty = project();
    assert.notEqual(run(empty, ...args, '--yes').status, 0);
    assert.deepEqual(readdirSync(empty), []);
  }
});
