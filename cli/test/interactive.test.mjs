import test from 'node:test';
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

async function wizard(cancel) {
  const workspace = fileURLToPath(new URL('../../work/cli-interactive-tests/', import.meta.url));
  mkdirSync(workspace, { recursive: true });
  const root = mkdtempSync(join(workspace, 'project-'));
  const cli = fileURLToPath(new URL('../dist/index.js', import.meta.url));
  const fixture = new URL('./terminal-fixture.mjs', import.meta.url).href;
  const prompts = [
    ['Quais agentes', ' \r'],
    ['Como você quer escolher', '\r'],
    ['Como pretende trabalhar', ' \r'],
    ['Revise as skills', '\r'],
    ['Deseja papéis opcionais', ' \r'],
    ['Instalar os arquivos acima', cancel ? '\x03' : 'y\r'],
  ];
  return await new Promise((resolve, reject) => {
    const child = spawn(process.execPath, ['--import', fixture, cli, 'init', '--dir', root], { stdio: 'pipe' });
    let output = '';
    let errors = '';
    let step = 0;
    const timer = setTimeout(() => { child.kill(); reject(new Error(`Fluxo não terminou na etapa ${step}: ${output}\n${errors}`)); }, 15000);
    child.stdout.on('data', data => {
      output += data.toString();
      if (output.includes('Abra uma nova sessão') || output.includes('Cancelado.')) child.stdin.end();
      if (step < prompts.length && output.includes(prompts[step][0])) {
        const keys = prompts[step++][1];
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
  assert.equal(result.step, 6);
  assert.ok(existsSync(join(result.root, '.agents/skills/propor/SKILL.md')));
  assert.ok(existsSync(join(result.root, '.agents/skills/escrever-claro/SKILL.md')));
  assert.ok(existsSync(join(result.root, '.codex/agents/planner.toml')));
  assert.match(result.output, /Instalação concluída/);
});

test('cancelar na confirmação depois das perguntas não grava arquivos', async () => {
  const result = await wizard(true);
  assert.equal(result.code, 130, result.output + result.errors);
  assert.equal(result.step, 6);
  assert.match(result.output, /Cancelado/);
  assert.deepEqual(readdirSync(result.root), []);
});
