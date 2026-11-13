#!/usr/bin/env node
import { existsSync } from 'node:fs';
import { parseArgs } from 'node:util';
import { resolve } from 'node:path';
import * as p from '@clack/prompts';
import { type Agent, type Role, payload, scenarios, roleDescriptions, recommend, selectSkills, instructions } from './catalog.js';
import { applyPlan, installationStatus, planInstall } from './install.js';
import { answer, Cancelled } from './prompts.js';
import { configureModels, modelsExist, policyNotice, runModels } from './models.js';

const help = `@jordyfontoura/skills — adoção guiada de skills e papéis

Uso: npx @jordyfontoura/skills [init|list|status] [opções]
     npx @jordyfontoura/skills models init [opções]
     npx @jordyfontoura/skills knowledge list

  --agents codex,claude-code   Agentes de destino
  --skills nome,outro         Skills escolhidas; all ou none
  --scenarios approval,...    Situações que geram recomendações (veja list)
  --roles planner,evaluator   Papéis opcionais; all ou none
  --models                   Criar política neutra se não existir
  --neutral                  Em models init: criar política que herda o ambiente
  --config arquivo.json      Em models init: gerar a partir de uma política JSON v2
  --print                    Em models init: imprimir apenas TOML, sem gravar
  --dir caminho              Projeto de destino (padrão: pasta atual)
  --dry-run                  Mostrar a instalação sem gravar arquivos
  --yes                      Confirmar uma seleção explícita sem perguntas
  --help                     Mostrar ajuda
  --version                  Mostrar versão do conteúdo

O CLI preserva arquivos existentes. Não misture cópias e plugin das mesmas skills.
Papéis só são executados quando houver autorização para delegar.
`;
function choices<T extends string>(value: string[] | undefined, allowed: readonly T[], option: string): T[] | undefined {
  if (value === undefined) return undefined;
  const names = [...new Set(value.flatMap(item => item.split(',')).map(item => item.trim()).filter(Boolean))];
  if (names.length === 1 && names[0] === 'all') return [...allowed];
  if (names.length === 1 && names[0] === 'none') return [];
  if (!names.length || names.some(name => !allowed.includes(name as T))) {
    throw new Error(`Valor inválido em ${option}. Opções: ${allowed.join(', ')}.`);
  }
  return names as T[];
}
async function main() {
  const { values, positionals } = parseArgs({ allowPositionals: true, options: {
    agents: { type: 'string', multiple: true }, skills: { type: 'string', multiple: true },
    scenarios: { type: 'string', multiple: true }, roles: { type: 'string', multiple: true },
    dir: { type: 'string' }, models: { type: 'boolean' },
    'dry-run': { type: 'boolean' }, yes: { type: 'boolean' },
    help: { type: 'boolean' }, version: { type: 'boolean' },
    neutral: { type: 'boolean' }, config: { type: 'string' }, print: { type: 'boolean' },
  } });
  if (values.help) { console.log(help); return; }
  if (values.version) { console.log(payload.source.version); return; }
  const command = positionals[0] ?? 'init';
  const root = resolve(values.dir ?? process.cwd());
  const interactive = Boolean(process.stdin.isTTY && process.stdout.isTTY && !values.yes);
  if (command === 'models' && positionals.length === 2 && positionals[1] === 'init') {
    if (['agents', 'skills', 'scenarios', 'roles', 'models'].some(key => values[key as keyof typeof values] !== undefined)) throw new Error('models init não instala skills ou papéis; use init para isso.');
    await runModels({ root, interactive, neutral: values.neutral, config: values.config, print: values.print, dryRun: values['dry-run'], yes: values.yes });
    return;
  }
  if (command === 'knowledge' && positionals.length === 2 && positionals[1] === 'list') {
    if (Object.keys(values).some(key => key !== 'dir')) throw new Error('knowledge list não aceita opções de instalação.');
    for (const guide of payload.knowledge) console.log(`${guide.path} — ${guide.title}\n  Skills: ${guide.skills.join(', ') || 'nenhuma'}`);
    return;
  }
  if (positionals.length > 1 || !['init', 'list', 'status'].includes(command)) throw new Error('Comando inválido. Use init, list, status ou models init; veja --help.');
  if (values.neutral || values.config !== undefined || values.print) throw new Error('--neutral, --config e --print são opções de models init.');
  if (command === 'list') {
    for (const skill of payload.skills) console.log(`${skill.name} [${skill.group}] — ${skill.description}`);
    console.log('\nSituações:');
    for (const scenario of scenarios) console.log(`${scenario.value}: ${scenario.label} → ${scenario.skills.join(', ')}`);
    console.log('\nPapéis:');
    for (const role of payload.roles) console.log(`${role}: ${roleDescriptions[role]}`);
    return;
  }
  if (command === 'status') { console.log((await installationStatus(root)).join('\n')); return; }
  let agents = choices(values.agents, ['codex', 'claude-code'] as const, '--agents');
  let skills = choices(values.skills, payload.skills.map(s => s.name), '--skills');
  const situations = choices(values.scenarios, scenarios.map(s => s.value), '--scenarios');
  if (situations !== undefined) skills = [...new Set([...(skills ?? []), ...recommend(situations)])];
  let roles = choices(values.roles, payload.roles, '--roles');
  if (!interactive && (!agents || !skills)) throw new Error('Sem terminal interativo, informe --agents e --skills (ou --scenarios). Use --dry-run ou --yes.');
  if (interactive) {
    p.intro('@jordyfontoura/skills');
    p.log.info('Use ↑/↓ para navegar, espaço para marcar, Enter para confirmar e Esc para cancelar.');
    agents ??= await answer(p.multiselect<Agent>({ message: 'Quais agentes você usa neste projeto?',
      options: [{ value: 'codex', label: 'Codex' }, { value: 'claude-code', label: 'Claude Code' }],
      showInstructions: false,
      initialValues: [existsSync(resolve(root, '.codex')) || existsSync(resolve(root, 'AGENTS.md')) ? 'codex' : undefined,
        existsSync(resolve(root, '.claude')) ? 'claude-code' : undefined].filter(Boolean) as Agent[], required: true }));
    if (skills === undefined) {
      const mode = await answer(p.select({ message: 'Como você quer escolher?', showInstructions: false, options: [
        { value: 'recommended', label: 'Receber recomendações pelas minhas práticas' },
        { value: 'manual', label: 'Escolher diretamente no catálogo' },
        { value: 'plugin', label: 'Usar o plugin completo', hint: 'exibir instruções' },
      ] }));
      if (mode === 'plugin') {
        console.log(agents.includes('claude-code') ? '\nclaude plugin marketplace add jordyfontoura/skills\nclaude plugin install jordyfontoura-skills@jordyfontoura' : '');
        console.log(agents.includes('codex') ? '\ncodex plugin marketplace add jordyfontoura/skills\ncodex plugin add jordyfontoura-skills@jordyfontoura' : '');
        p.outro('Instruções exibidas. Nenhum arquivo foi alterado.'); return;
      }
      let initial: string[] = [];
      if (mode === 'recommended') {
        const selected = await answer(p.multiselect({ message: 'Como pretende trabalhar? (opcional)', showInstructions: false, options: scenarios.map(s => ({ value: s.value, label: s.label })), required: false }));
        initial = recommend(selected);
      }
      skills = await answer(p.multiselect({ message: 'Revise as skills. Você pode marcar ou desmarcar qualquer uma.',
        showInstructions: false,
        options: [...payload.skills].sort((a, b) => Number(initial.includes(b.name)) - Number(initial.includes(a.name)))
          .map(s => ({ value: s.name, label: s.name, hint: s.description })),
        initialValues: initial, required: false }));
    }
    roles ??= await answer(p.multiselect<Role>({ message: 'Deseja papéis opcionais? Instalar não autoriza delegação.',
      showInstructions: false, options: payload.roles.map(role => ({ value: role, label: role, hint: roleDescriptions[role] })), required: false }));
  }
  agents ??= [];
  roles ??= [];
  skills ??= [];
  if (!agents.length) throw new Error('Escolha ao menos um agente.');
  const selected = selectSkills(skills, roles);
  let wantModels = Boolean(values.models);
  let modelsContent: string | undefined;
  if (interactive && !values.models && (roles.length || selected.some(name => ['delegar', 'conselho', 'verificar-aceite'].includes(name)))) {
    if (await modelsExist(root)) console.log('models.toml existente: preservado, não validado.');
    else {
      const option = await answer(p.select({ message: 'Criar uma política de modelos para delegações? (opcional)', showInstructions: false, options: [
        { value: 'skip', label: 'Não criar agora' },
        { value: 'neutral', label: 'Criar neutra: herdar o ambiente' },
        { value: 'custom', label: 'Configurar modelos e perfis agora' },
      ] }));
      wantModels = option !== 'skip';
      if (option === 'custom') modelsContent = await configureModels();
    }
  }
  if (!selected.length && !wantModels) throw new Error('Escolha ao menos uma skill, papel ou --models.');
  const added = selected.filter(name => !skills.includes(name));
  if (added.length) console.log(`\nSkills de apoio incluídas: ${added.join(', ')}`);
  const related = [...new Set(payload.skills.filter(s => selected.includes(s.name)).flatMap(s => s.related))].filter(name => !selected.includes(name));
  if (related.length) console.log(`Outras skills citadas (opcionais, não instaladas): ${related.join(', ')}`);
  const plan = await planInstall(root, { agents, skills: selected, roles, models: wantModels }, modelsContent);
  console.log(`\nProjeto: ${root}\nSkills: ${selected.join(', ') || 'nenhuma'}\nPapéis: ${roles.join(', ') || 'nenhum'}`);
  const guides = plan.entries.filter(entry => entry.path.startsWith('knowledge/harness/'));
  if (guides.length) console.log(`Conhecimento compartilhado: ${guides.filter(entry => entry.path !== 'knowledge/harness/README.md').length} guias e um índice em knowledge/harness/, usados pelos agentes selecionados.`);
  console.log('Se já usa o plugin, evite instalar cópias das mesmas skills; --skills none permite escolher apenas papéis.');
  for (const entry of plan.entries) console.log(`${{ create: 'criar', same: 'idêntico', preserve: 'preservar' }[entry.state]}: ${entry.path}`);
  for (const path of plan.conflicts) console.log(`conflito: ${path}`);
  const modelEntry = plan.entries.find(entry => entry.path === '.agents/models.toml');
  if (modelEntry?.state === 'create') console.log(`\n${policyNotice}\n\nPrévia de .agents/models.toml:\n\n${modelEntry.content}`);
  if (modelEntry?.state === 'preserve') console.log('models.toml existente: preservado, não validado.');
  if (plan.conflicts.length) throw new Error('Há arquivos diferentes no destino. Nenhum arquivo foi alterado. Use atualizar-harness para preservar adaptações.');
  if (values['dry-run']) { console.log('\nSimulação concluída. Nenhum arquivo foi alterado.'); return; }
  if (!values.yes) {
    if (!interactive) throw new Error('Para gravar sem perguntas, confirme a seleção com --yes.');
    if (!await answer(p.confirm({ message: 'Instalar os arquivos acima?', active: 'Sim', inactive: 'Não', initialValue: false }))) throw new Cancelled();
  }
  const count = await applyPlan(plan);
  console.log(`\nInstalação concluída: ${count} arquivos criados. Arquivos existentes preservados.`);
  if (selected.length) console.log(`\nBloco sugerido para AGENTS.md ou CLAUDE.md (adapte às regras existentes):\n\n${instructions(selected)}`);
  console.log('\nAbra uma nova sessão do agente. Para conferir os arquivos, use o comando status.');
}
main().catch(error => {
  if (error instanceof Cancelled) { p.cancel('Cancelado. Nenhum arquivo foi alterado.'); process.exitCode = 130; }
  else { console.error(`Erro: ${(error as Error).message}`); process.exitCode = 1; }
});
