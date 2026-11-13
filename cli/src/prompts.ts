import * as p from '@clack/prompts';

export class Cancelled extends Error {}
export async function answer<T>(promise: Promise<T>): Promise<Exclude<T, symbol>> {
  const value = await promise;
  if (p.isCancel(value)) throw new Cancelled();
  return value as Exclude<T, symbol>;
}
