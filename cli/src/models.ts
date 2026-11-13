import { lstat, readFile } from 'node:fs/promises';
import { basename, extname } from 'node:path';
import * as p from '@clack/prompts';
import { payload } from './catalog.js';
import { type Candidate, type PolicyV2, serializePolicy, validatePolicyV2 } from './policy.js';
import { answer, Cancelled } from './prompts.js';
import { applyPlan, planInstall } from './install.js';

export const policyNotice = 'Esta política orienta delegações autorizadas. Não altera a conversa aberta nem autoriza delegação ou representação. IDs e esforços não foram verificados no provedor.';
const labels: Record<string, string> = {
  simple: 'Trabalho simples', default: 'Trabalho habitual', hard: 'Trabalho difícil',
  orchestrator: 'Coordenação', evaluator: 'Aceite independente e conselho', representative: 'Representação de decisões',
};
const inherited = (): Candidate => ({ provider: 'inherit', model: 'inherit', effort: 'inherit' });
export function createPolicy(layout: 'shared' | 'profiles'): PolicyV2 {
  const policy = structuredClone(payload.modelTemplate);
  const names = layout === 'shared' ? ['default'] : ['simple', 'default', 'hard', 'orchestrator', 'evaluator', 'representative'];
  policy.profiles = Object.fromEntries(names.map(name => [name, { candidates: [inherited()] }]));
  for (const [name, role] of Object.entries(policy.roles)) {
    role.profile = layout === 'profiles' && names.includes(name) ? name : 'default';
    if (name === 'council' && layout === 'profiles') role.profile = 'evaluator';
    if (layout === 'profiles' && ['planner', 'implementer', 'reviewer'].includes(name)) role.complexity = { simple: 'simple', hard: 'hard' };
  }
  validatePolicyV2(policy);
  return policy;
}
const requiredText = (value: string | undefined) => value?.trim() ? undefined : 'Informe um valor.';
async function askCandidate(fallback: boolean): Promise<Candidate> {
  const custom = fallback || await answer(p.confirm({ message: 'Informar provedor e modelo deste candidato?', active: 'Sim', inactive: 'Herdar ambiente', initialValue: true }));
  const provider = custom ? await answer(p.text({ message: 'ID do provedor na ferramenta de delegação', validate: value => requiredText(value) ?? (value?.trim() === 'inherit' ? 'Use a opção de herdar o ambiente.' : undefined) })) : 'inherit';
  const model = custom ? await answer(p.text({ message: 'ID do modelo nessa ferramenta', validate: value => requiredText(value) ?? (value?.trim() === 'inherit' ? 'Um provedor definido exige um modelo definido.' : undefined) })) : 'inherit';
  const effort = await answer(p.text({ message: 'Esforço aceito pela ferramenta (ou inherit)', defaultValue: 'inherit', placeholder: 'inherit',
    validate: value => value && !value.trim() ? 'Informe um esforço ou pressione Enter para herdar.' : undefined }));
  return { provider: provider.trim(), model: model.trim(), effort: effort.trim() };
}
export async function configureModels(): Promise<string> {
  p.log.info(policyNotice);
  const mode = await answer(p.select<'neutral' | 'shared' | 'profiles'>({ message: 'Como definir a política de modelos?', showInstructions: false, options: [
    { value: 'neutral', label: 'Herdar o ambiente em todas as responsabilidades' },
    { value: 'shared', label: 'Definir um modelo compartilhado' },
    { value: 'profiles', label: 'Separar modelos por perfis de trabalho' },
  ] }));
  if (mode === 'neutral') return payload.files['.agents/models.toml'];
  const policy = createPolicy(mode);
  const chosen = mode === 'shared' ? ['default'] : await answer(p.multiselect({
    message: 'Quais perfis deseja personalizar? Os demais herdam o ambiente.', showInstructions: false, required: false,
    options: Object.keys(policy.profiles).map(name => ({ value: name, label: labels[name] ?? name, hint: name })), initialValues: ['default'],
  }));
  for (const name of chosen) {
    p.log.info(`Perfil: ${labels[name] ?? name} (${name})`);
    const candidates: Candidate[] = [];
    let more = true;
    while (more) {
      const candidate = await askCandidate(candidates.length > 0);
      policy.profiles[name].candidates = [...candidates, candidate];
      try { validatePolicyV2(policy); }
      catch (error) { p.log.warn((error as Error).message); continue; }
      candidates.push(candidate);
      more = await answer(p.confirm({ message: 'Adicionar alternativa por indisponibilidade?', active: 'Sim', inactive: 'Não', initialValue: false }));
    }
  }
  if (mode === 'profiles' && await answer(p.confirm({ message: 'Personalizar o perfil base de cada responsabilidade?', active: 'Sim', inactive: 'Manter associações sugeridas', initialValue: false }))) {
    p.log.info('planner, implementer e reviewer mantêm os mapas simple/hard. Aceite, conselho e representação não recebem mapas de complexidade.');
    for (const [name, role] of Object.entries(policy.roles)) {
      role.profile = await answer(p.select({ message: `Perfil base de ${name}: ${role.when}`, showInstructions: false,
        initialValue: role.profile, options: Object.keys(policy.profiles).map(profile => ({ value: profile, label: labels[profile] ?? profile, hint: profile })) }));
    }
  }
  return serializePolicy(policy);
}
export async function modelsExist(root: string): Promise<boolean> {
  const plan = await planInstall(root, { agents: [], skills: [], roles: [], models: true });
  if (plan.conflicts.length) throw new Error('O destino de models.toml não é um arquivo regular.');
  return plan.entries.some(entry => entry.path === '.agents/models.toml' && entry.state === 'preserve');
}
export interface ModelsOptions { root: string; interactive: boolean; neutral?: boolean; config?: string; print?: boolean; dryRun?: boolean; yes?: boolean }
export async function runModels(options: ModelsOptions): Promise<void> {
  if (options.config !== undefined && options.neutral) throw new Error('Use --neutral ou --config, sem combinar os dois.');
  if (!options.print && await modelsExist(options.root)) {
    console.log('models.toml existente: preservado, não validado. Políticas v1 e v2 continuam intactas. Use --print para consultar uma proposta sem gravar.');
    return;
  }
  let content: string;
  if (options.config !== undefined) {
    if (extname(options.config).toLowerCase() !== '.json' || basename(options.config).startsWith('.env')) throw new Error('--config exige um arquivo .json de política.');
    if (!(await lstat(options.config)).isFile()) throw new Error('--config exige um arquivo regular, sem link simbólico.');
    const policy: unknown = JSON.parse(await readFile(options.config, 'utf8'));
    validatePolicyV2(policy);
    content = serializePolicy(policy);
  } else if (options.neutral || (options.print && !options.interactive)) {
    content = payload.files['.agents/models.toml'];
  } else if (options.interactive) {
    content = await configureModels();
  } else throw new Error('Sem terminal interativo, informe --neutral ou --config arquivo.json.');
  if (options.print) { process.stdout.write(content); return; }
  console.log(`\n${policyNotice}\n\nPrévia de .agents/models.toml:\n\n${content}`);
  const plan = await planInstall(options.root, { agents: [], skills: [], roles: [], models: true }, content);
  if (plan.conflicts.length) throw new Error('Destino inválido. Nenhum arquivo foi alterado.');
  if (plan.entries.some(entry => entry.state === 'preserve')) { console.log('models.toml surgiu durante a prévia: preservado, não validado.'); return; }
  if (options.dryRun) { console.log('Simulação concluída. Nenhum arquivo foi alterado.'); return; }
  if (!options.yes) {
    if (!options.interactive) throw new Error('Para gravar sem perguntas, confirme a política com --yes.');
    if (!await answer(p.confirm({ message: 'Criar models.toml com a política acima?', active: 'Sim', inactive: 'Não', initialValue: false }))) throw new Cancelled();
  }
  await applyPlan(plan);
  console.log('Política de modelos criada. Para conferir os arquivos, use o comando status.');
}
