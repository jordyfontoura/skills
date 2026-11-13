import test from 'node:test';
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

async function wizard(cancel, options = {}) {
  const workspace = fileURLToPath(new URL('../../work/cli-interactive-tests/', import.meta.url));
  mkdirSync(workspace, { recursive: true });
  const root = mkdtempSync(join(workspace, 'project-'));
  const cli = fileURLToPath(new URL('../dist/index.js', import.meta.url));
  const fixture = new URL('./terminal-fixture.mjs', import.meta.url).href;
  const prompts = options.prompts ?? [
    ['Quais agentes', ' \r'],
    ['Como você quer escolher', '\r'],
    ['Como pretende trabalhar', ' \r'],
    ['Revise as skills', '\r'],
    ['Deseja papéis opcionais', ' \r'],
    ['Criar uma política de modelos', '\r'],
    ['Instalar os arquivos acima', cancel ? '\x03' : 'y\r'],
  ];
  return await new Promise((resolve, reject) => {
    const child = spawn(process.execPath, ['--import', fixture, cli, ...(options.command ?? ['init']), '--dir', root], { stdio: 'pipe' });
    let output = '';
    let pending = '';
    let errors = '';
    let step = 0;
    const timer = setTimeout(() => { child.kill(); reject(new Error(`Fluxo não terminou na etapa ${step}: ${output}\n${errors}`)); }, 15000);
    child.stdout.on('data', data => {
      output += data.toString();
      pending += data.toString();
      if (output.includes('Abra uma nova sessão') || output.includes('Cancelado.') || output.includes('Política de modelos criada.')) child.stdin.end();
      if (step < prompts.length && pending.includes(prompts[step][0])) {
        const keys = prompts[step++][1];
        pending = '';
        setTimeout(() => child.stdin.write(keys), 10);
      }
    });
    child.stderr.on('data', data => { errors += data.toString(); });
    child.on('error', error => { clearTimeout(timer); reject(error); });
    child.on('close', code => { clearTimeout(timer); resolve({ code, output, errors, step, root }); });
  });
}

test('perguntas reais recomendam skills, incluem papel e só instalam após confirmação', async () => {
  const result = await wizard(false);
  assert.equal(result.code, 0, result.output + result.errors);
  assert.equal(result.step, 7);
  assert.ok(existsSync(join(result.root, '.agents/skills/propor/SKILL.md')));
  assert.ok(existsSync(join(result.root, '.agents/skills/escrever-claro/SKILL.md')));
  assert.ok(existsSync(join(result.root, '.codex/agents/planner.toml')));
  assert.equal(existsSync(join(result.root, '.agents/models.toml')), false);
  assert.match(result.output, /Instalação concluída/);
});

const shared = [
  ['Como definir a política', '\x1b[B\r'],
  ['Informar provedor e modelo', 'y\r'],
  ['ID do provedor', 'external-a\r'],
  ['ID do modelo', 'local/model:a\r'],
  ['Esforço aceito', 'custom\r'],
  ['Adicionar alternativa', 'y\r'],
  ['ID do provedor', 'external-b\r'],
  ['ID do modelo', 'local/model:b\r'],
  ['Esforço aceito', '\r'],
  ['Adicionar alternativa', '\r'],
];

test('models init configura modelo compartilhado, esforço e alternativas na ordem escolhida', async () => {
  const prompts = [...shared, ['Criar models.toml', 'y\r']];
  const result = await wizard(false, { command: ['models', 'init'], prompts });
  assert.equal(result.code, 0, result.output + result.errors);
  assert.equal(result.step, prompts.length);
  const content = readFileSync(join(result.root, '.agents/models.toml'), 'utf8');
  assert.ok(content.indexOf('external-a') < content.indexOf('external-b'));
  assert.match(content, /effort = "custom"/);
  assert.match(content, /effort = "inherit"/);
  assert.equal((content.match(/profile = "default"/g) ?? []).length, 7);
});

test('cancelar nas etapas do configurador nunca grava arquivos', async () => {
  const flow = [...shared, ['Criar models.toml', 'y\r']];
  for (const cancelAt of [0, 2, 4, 5, 7, 10]) {
    const prompts = flow.slice(0, cancelAt + 1).map((step, index) => index === cancelAt ? [step[0], '\x03'] : step);
    const result = await wizard(false, { command: ['models', 'init'], prompts });
    assert.equal(result.code, 130, result.output + result.errors);
    assert.deepEqual(readdirSync(result.root), []);
  }
});

test('o init integra a política personalizada na mesma confirmação de skills e papéis', async () => {
  const prompts = [
    ['Quais agentes', ' \r'], ['Como você quer escolher', '\r'], ['Como pretende trabalhar', ' \r'],
    ['Revise as skills', '\r'], ['Deseja papéis opcionais', ' \r'],
    ['Criar uma política de modelos', '\x1b[B\x1b[B\r'],
    ...shared, ['Instalar os arquivos acima', 'y\r'],
  ];
  const result = await wizard(false, { prompts });
  assert.equal(result.code, 0, result.output + result.errors);
  assert.equal(result.step, prompts.length);
  assert.ok(existsSync(join(result.root, '.agents/skills/propor/SKILL.md')));
  assert.match(readFileSync(join(result.root, '.agents/models.toml'), 'utf8'), /external-a/);
  assert.equal(readdirSync(join(result.root, '.harness/receipts')).length, 1);
});

test('o configurador por perfis permite revisar a associação das sete responsabilidades', async () => {
  const prompts = [
    ['Como definir a política', '\x1b[B\x1b[B\r'],
    ['Quais perfis', '\r'],
    ['Informar provedor e modelo', 'y\r'], ['ID do provedor', 'external\r'],
    ['ID do modelo', 'model-a\r'], ['Esforço aceito', '\r'], ['Adicionar alternativa', '\r'],
    ['Personalizar o perfil base', 'y\r'],
    ...['orchestrator', 'planner', 'implementer', 'reviewer', 'evaluator', 'representative', 'council'].map(role => [`Perfil base de ${role}:`, '\r']),
    ['Criar models.toml', 'y\r'],
  ];
  const result = await wizard(false, { command: ['models', 'init'], prompts });
  assert.equal(result.code, 0, result.output + result.errors);
  assert.equal(result.step, prompts.length);
  const content = readFileSync(join(result.root, '.agents/models.toml'), 'utf8');
  assert.match(content, /\[roles\.planner\.complexity\]/);
  assert.doesNotMatch(content, /\[roles\.(evaluator|council|representative)\.complexity\]/);
  assert.match(content, /\[profiles\.representative\]/);
});

test('cancelar na confirmação depois das perguntas não grava arquivos', async () => {
  const result = await wizard(true);
  assert.equal(result.code, 130, result.output + result.errors);
  assert.equal(result.step, 7);
  assert.match(result.output, /Cancelado/);
  assert.deepEqual(readdirSync(result.root), []);
});
