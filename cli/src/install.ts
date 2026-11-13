import { createHash } from 'node:crypto';
import { lstat, mkdir, open, readFile, readdir, rmdir, unlink } from 'node:fs/promises';
import { dirname, join, parse, relative, resolve, sep } from 'node:path';
import { type Agent, type Role, type Source, payload } from './catalog.js';

export interface Selection { agents: Agent[]; skills: string[]; roles: Role[]; models: boolean }
interface Receipt { schemaVersion: number; source: Source; selection: Selection; files: Record<string, string> }
export interface Entry { path: string; content: string; state: 'create' | 'same' | 'preserve' }
export interface Plan { root: string; entries: Entry[]; conflicts: string[] }
const hash = (text: string) => createHash('sha256').update(text).digest('hex');
const receiptPattern = /^\.harness\/receipts\/[a-f0-9]{64}\.json$/;

function allowed(path: string): boolean {
  if (path.includes('\\') || path.split('/').some(part => part === '..' || part === '.' || !part || part === '.env' || part.startsWith('.env.'))) return false;
  return /^\.(agents|claude)\/skills\/[a-z0-9-]+\/.+/.test(path)
    || /^\.(claude|codex)\/agents\/[a-z0-9-]+\.(md|toml)$/.test(path)
    || path === '.agents/models.toml';
}
async function stat(path: string) {
  try { return await lstat(path); }
  catch (error) { if ((error as NodeJS.ErrnoException).code === 'ENOENT') return undefined; throw error; }
}
// Não siga links do destino: nem uma pasta de agente nem o projeto podem redirecionar a escrita.
async function safePath(root: string, path: string): Promise<string> {
  if (!allowed(path) && !receiptPattern.test(path) && path !== '.harness/receipts') {
    throw new Error(`Caminho de instalação inválido: ${path}`);
  }
  const target = resolve(root, ...path.split('/'));
  const rel = relative(root, target);
  if (rel.startsWith(`..${sep}`) || rel === '..') throw new Error(`Caminho fora do projeto: ${path}`);
  const anchor = parse(target).root;
  let current = anchor;
  const parts = target.slice(anchor.length).split(sep);
  for (const [index, part] of parts.entries()) {
    current = join(current, part);
    const info = await stat(current);
    if (info?.isSymbolicLink()) throw new Error(`Link simbólico não permitido: ${current}`);
    if (info && index < parts.length - 1 && !info.isDirectory()) throw new Error(`Pasta inválida: ${current}`);
  }
  return target;
}
export async function planInstall(root: string, selection: Selection): Promise<Plan> {
  root = resolve(root);
  const files: Record<string, string> = {};
  for (const name of selection.skills) {
    const prefix = `.agents/skills/${name}/`;
    for (const [path, content] of Object.entries(payload.files)) {
      if (!path.startsWith(prefix)) continue;
      if (selection.agents.includes('codex')) files[path] = content;
      if (selection.agents.includes('claude-code')) files[path.replace('.agents/', '.claude/')] = content;
    }
  }
  for (const role of selection.roles) for (const agent of selection.agents) {
    const path = agent === 'codex' ? `.codex/agents/${role}.toml` : `.claude/agents/${role}.md`;
    files[path] = payload.files[path];
  }
  if (selection.models) files['.agents/models.toml'] = payload.files['.agents/models.toml'];
  const entries: Entry[] = [];
  const conflicts: string[] = [];
  for (const [path, content] of Object.entries(files).sort(([a], [b]) => a.localeCompare(b))) {
    if (typeof content !== 'string') throw new Error(`Conteúdo ausente no pacote: ${path}`);
    const target = await safePath(root, path);
    const info = await stat(target);
    if (info && !info.isFile()) { conflicts.push(path); continue; }
    if (info && path === '.agents/models.toml') {
      entries.push({ path, content, state: 'preserve' });
    } else if (info && await readFile(target, 'utf8') !== content) {
      conflicts.push(path);
    } else entries.push({ path, content, state: info ? 'same' : 'create' });
  }
  // Recibos imutáveis permitem adoções parciais sem reescrever registros de outra instalação.
  const receipt: Receipt = { schemaVersion: 1, source: payload.source, selection,
    files: Object.fromEntries(entries.filter(e => e.state !== 'preserve').map(e => [e.path, hash(e.content)])) };
  if (Object.keys(receipt.files).length) {
    const content = JSON.stringify(receipt, null, 2) + '\n';
    const path = `.harness/receipts/${hash(content)}.json`;
    const target = await safePath(root, path);
    const info = await stat(target);
    if (info && (!info.isFile() || await readFile(target, 'utf8') !== content)) conflicts.push(path);
    else entries.push({ path, content, state: info ? 'same' : 'create' });
  }
  return { root, entries, conflicts };
}
export async function applyPlan(plan: Plan): Promise<number> {
  if (plan.conflicts.length) throw new Error('Instalação interrompida: há arquivos diferentes no destino.');
  const created: string[] = [];
  const directories: string[] = [];
  try {
    for (const entry of plan.entries) {
      // Reconfira após a confirmação; não sobrescreva alterações feitas durante a prévia.
      const path = await safePath(plan.root, entry.path);
      if (entry.state === 'preserve') continue;
      if (entry.state === 'same') {
        if (await readFile(path, 'utf8') !== entry.content) throw new Error(`Arquivo mudou durante a prévia: ${entry.path}`);
        continue;
      }
      const missing: string[] = [];
      let directory = dirname(path);
      while (!await stat(directory)) { missing.push(directory); directory = dirname(directory); }
      for (const dir of missing.reverse()) {
        await mkdir(dir);
        directories.push(dir);
      }
      const handle = await open(path, 'wx');
      created.push(path);
      try { await handle.writeFile(entry.content, 'utf8'); }
      finally { await handle.close(); }
    }
    return created.length;
  } catch (error) {
    for (const path of created.reverse()) await unlink(path);
    for (const path of directories.reverse()) await rmdir(path).catch(() => {});
    throw error;
  }
}
export async function installationStatus(root: string): Promise<string[]> {
  root = resolve(root);
  const directory = await safePath(root, '.harness/receipts');
  if (!await stat(directory)) return ['Nenhuma instalação registrada neste projeto.'];
  const records = new Map<string, Set<string>>();
  const sources = new Set<string>();
  for (const name of (await readdir(directory)).sort()) {
    const path = `.harness/receipts/${name}`;
    if (!receiptPattern.test(path)) throw new Error(`Recibo inválido: ${name}`);
    const content = await readFile(await safePath(root, path), 'utf8');
    if (`${hash(content)}.json` !== name) throw new Error(`Recibo alterado: ${name}`);
    const receipt = JSON.parse(content) as Receipt;
    if (receipt.schemaVersion !== 1 || !receipt.files || !receipt.source) throw new Error(`Formato de recibo inválido: ${name}`);
    sources.add(`${receipt.source.version} · base ${receipt.source.sha}${receipt.source.dirty ? ' · conteúdo de build local' : ''}`);
    for (const [file, digest] of Object.entries(receipt.files)) {
      if (!allowed(file) || !/^[a-f0-9]{64}$/.test(digest)) throw new Error(`Registro inválido: ${file}`);
      const values = records.get(file) ?? new Set<string>();
      values.add(digest);
      records.set(file, values);
    }
  }
  const lines = [...sources].map(source => `Origem: ${source}`);
  for (const [file, digests] of records) {
    const path = await safePath(root, file);
    const info = await stat(path);
    const state = !info ? 'ausente' : info.isFile() && digests.has(hash(await readFile(path, 'utf8'))) ? 'íntegro' : 'alterado';
    lines.push(`${state}: ${file}`);
  }
  lines.push('Para atualizar preservando adaptações, use a skill atualizar-harness com os recibos deste projeto.');
  return lines;
}
