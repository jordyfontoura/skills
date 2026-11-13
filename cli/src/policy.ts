export interface Candidate { provider: string; model: string; effort: string }
export interface PolicyRole { when: string; profile: string; complexity?: Partial<Record<'simple' | 'hard', string>> }
export interface PolicyV2 {
  version: 2;
  profiles: Record<string, { candidates: Candidate[] }>;
  roles: Record<string, PolicyRole>;
}
const fixedRoles = new Set(['representative', 'evaluator', 'council']);
function table(value: unknown, location: string): asserts value is Record<string, unknown> {
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw new Error(`${location}: deve ser uma tabela`);
}
function fields(value: Record<string, unknown>, allowed: string[], required: string[], location: string) {
  if (Object.keys(value).some(key => !allowed.includes(key))) throw new Error(`${location}: campos desconhecidos`);
  if (required.some(key => !Object.hasOwn(value, key))) throw new Error(`${location}: campos ausentes`);
}
function identifier(value: unknown, location: string): asserts value is string {
  if (typeof value !== 'string' || value !== value.trim() || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(value)) throw new Error(`${location}: nome inválido`);
}
function text(value: unknown, location: string, trimmed = true): asserts value is string {
  // Mesmos espaços de str.strip() no Python; String.trim() trata BOM e U+0085 de outro modo.
  const strip = (input: string) => input.replace(/^[\u0009-\u000d\u001c-\u0020\u0085\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+|[\u0009-\u000d\u001c-\u0020\u0085\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+$/g, '');
  if (typeof value !== 'string' || !strip(value) || (trimmed && value !== strip(value))) {
    throw new Error(`${location}: deve ser texto não vazio${trimmed ? ', sem espaços nas extremidades' : ''}`);
  }
  for (const char of value) {
    const point = char.codePointAt(0)!;
    if (point >= 0xd800 && point <= 0xdfff) throw new Error(`${location}: caractere Unicode inválido`);
  }
}
export function validatePolicyV2(value: unknown): asserts value is PolicyV2 {
  table(value, 'política');
  if (value.version !== 2) throw new Error('política.version: o gerador aceita somente a versão 2; arquivos v1 existentes são preservados');
  fields(value, ['version', 'profiles', 'roles'], ['version', 'profiles', 'roles'], 'política');
  table(value.profiles, 'profiles');
  const profiles = value.profiles;
  if (!Object.keys(profiles).length) throw new Error('profiles: deve conter ao menos um perfil');
  for (const [name, profile] of Object.entries(profiles)) {
    const location = `profiles.${name}`;
    identifier(name, location);
    table(profile, location);
    fields(profile, ['candidates'], ['candidates'], location);
    if (!Array.isArray(profile.candidates) || !profile.candidates.length) throw new Error(`${location}.candidates: deve conter uma lista não vazia`);
    const seen = new Set<string>();
    for (const [index, candidate] of profile.candidates.entries()) {
      const at = `${location}.candidates[${index}]`;
      table(candidate, at);
      fields(candidate, ['provider', 'model', 'effort'], ['provider', 'model', 'effort'], at);
      for (const key of ['provider', 'model', 'effort']) text(candidate[key], `${at}.${key}`);
      if ((candidate.provider === 'inherit') !== (candidate.model === 'inherit')) throw new Error(`${at}: provider e model devem ser herdados ou definidos juntos`);
      if (index > 0 && candidate.model === 'inherit') throw new Error(`${at}: uma alternativa deve identificar provider e model concretos`);
      const key = JSON.stringify([candidate.provider, candidate.model, candidate.effort]);
      if (seen.has(key)) throw new Error(`${location}: alternativa repetida`);
      seen.add(key);
    }
  }
  table(value.roles, 'roles');
  if (!Object.keys(value.roles).length) throw new Error('roles: deve conter ao menos uma responsabilidade');
  const reference = (profile: unknown, at: string) => {
    identifier(profile, at);
    if (!Object.hasOwn(profiles, profile)) throw new Error(`${at}: perfil sem configuração`);
  };
  for (const [name, role] of Object.entries(value.roles)) {
    const at = `roles.${name}`;
    identifier(name, at);
    table(role, at);
    fields(role, ['when', 'profile', 'complexity'], ['when', 'profile'], at);
    text(role.when, `${at}.when`, false);
    reference(role.profile, `${at}.profile`);
    if (Object.hasOwn(role, 'complexity')) {
      if (fixedRoles.has(name)) throw new Error(`${at}: papel não aceita mapa de complexidade`);
      table(role.complexity, `${at}.complexity`);
      fields(role.complexity, ['simple', 'hard'], [], `${at}.complexity`);
      for (const [level, profile] of Object.entries(role.complexity)) reference(profile, `${at}.complexity.${level}`);
    }
  }
}
export function serializePolicy(policy: PolicyV2): string {
  validatePolicyV2(policy);
  const quote = (value: string) => JSON.stringify(value).replace(/\u007f/g, '\\u007f');
  const lines = [
    '# Política de modelos para delegações autorizadas, gerada pelo CLI.',
    '# Não altera a conversa aberta nem autoriza delegação ou representação.',
    '# IDs e esforços são preferências declaradas; sua disponibilidade não foi verificada.',
    '# inherit mantém o ambiente. Alternativas são consideradas na ordem indicada.',
    'version = 2', '',
  ];
  for (const [name, profile] of Object.entries(policy.profiles)) {
    lines.push(`[profiles.${name}]`, 'candidates = [');
    for (const candidate of profile.candidates) lines.push(`  { provider = ${quote(candidate.provider)}, model = ${quote(candidate.model)}, effort = ${quote(candidate.effort)} },`);
    lines.push(']', '');
  }
  for (const [name, role] of Object.entries(policy.roles)) {
    lines.push(`[roles.${name}]`, `when = ${quote(role.when)}`, `profile = ${quote(role.profile)}`);
    if (role.complexity) {
      lines.push(`[roles.${name}.complexity]`);
      for (const [level, profile] of Object.entries(role.complexity)) lines.push(`${level} = ${quote(profile)}`);
    }
    lines.push('');
  }
  return lines.join('\n');
}
