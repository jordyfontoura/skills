import { readFileSync } from 'node:fs';

export type Agent = 'codex' | 'claude-code';
export type Role = 'planner' | 'evaluator' | 'representative';
export interface Skill { name: string; group: string; description: string; related: string[] }
export interface Source { repository: string; sha: string; version: string; dirty: boolean; contentHash: string }
export interface Payload { schemaVersion: number; source: Source; skills: Skill[]; roles: Role[]; files: Record<string, string> }
export const payload: Payload = JSON.parse(readFileSync(new URL('../payload.json', import.meta.url), 'utf8'));
if (payload.schemaVersion !== 1) throw new Error('Versão de catálogo não suportada.');

export const scenarios = [
  { value: 'approval', label: 'Avaliar a abordagem antes de alterar', skills: ['propor', 'entrevistar'] },
  { value: 'direct', label: 'Executar direto quando eu pedir', skills: ['fazer-direto'] },
  { value: 'sessions', label: 'Retomar trabalhos entre sessões', skills: ['passar-contexto', 'andamento'] },
  { value: 'reviews', label: 'Trabalhar com PRs e revisões', skills: ['revisar', 'tratar-revisao', 'descrever-pr', 'integrar'] },
  { value: 'decisions', label: 'Definir requisitos e pesquisar decisões', skills: ['especificar', 'pesquisar-web', 'conselho', 'delegar'] },
  { value: 'acceptance', label: 'Delegar e verificar o aceite independentemente', skills: ['verificar-aceite', 'delegar', 'escrever-objetivo'] },
  { value: 'interface', label: 'Experimentar e avaliar interfaces', skills: ['criticar', 'prototipar'] },
];
export const roleDescriptions: Record<Role, string> = {
  planner: 'Definir comportamento e planejar entregas',
  evaluator: 'Verificar o aceite em contexto independente',
  representative: 'Decidir dentro de autorização expressa de representação',
};
export const roleSkills: Record<Role, string[]> = {
  planner: ['especificar', 'delegar'],
  evaluator: ['verificar-aceite', 'delegar', 'implementar'],
  representative: ['delegar'],
};
const available = new Set(payload.skills.map(skill => skill.name));
for (const name of [...scenarios.flatMap(s => s.skills), ...Object.values(roleSkills).flat()]) {
  if (!available.has(name)) throw new Error(`Recomendação aponta para skill ausente: ${name}`);
}
export function recommend(choices: string[]): string[] {
  return [...new Set(['implementar', 'escrever-claro', 'esclarecer',
    ...scenarios.filter(s => choices.includes(s.value)).flatMap(s => s.skills)])];
}
export function selectSkills(skills: string[], roles: Role[]): string[] {
  return [...new Set([...skills, ...roles.flatMap(role => roleSkills[role])])].sort();
}
export function instructions(skills: string[]): string {
  const selected = new Set(skills);
  const lines = ['## Fluxo com as skills', ''];
  const rules: Record<string, string> = {
    propor: 'Quando eu pedir `propor`, apresente a abordagem e aguarde aprovação antes de alterar.',
    implementar: 'Use `implementar` para entregas verificáveis e relate comandos e resultados observados.',
    revisar: 'Use `revisar` para analisar um diff contra requisitos e riscos aplicáveis.',
    'verificar-aceite': 'Use `verificar-aceite` quando for exigido aceite em contexto independente.',
    delegar: 'Delegue apenas trabalho autorizado; configurar papéis não autoriza consultas.',
    'passar-contexto': 'Use `passar-contexto` quando outra sessão precisar retomar o trabalho.',
    'escrever-claro': 'Aplique `escrever-claro` ao redigir textos para leitores.',
  };
  for (const [name, rule] of Object.entries(rules)) if (selected.has(name)) lines.push(`- ${rule}`);
  lines.push('- Preserve as instruções, convenções e permissões do projeto.');
  return lines.join('\n');
}
