// Drift guards: the engine must match policy-format.md, and must never read the
// clock or an unseeded random source.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import {
  ALLOWED_ACTIONS,
  ALLOWED_INPUTS,
  ALLOWED_OPS,
  ENGINE_VERSION,
  FORBIDDEN_ACTIONS,
  FORBIDDEN_NAME_FRAGMENTS,
  forbiddenFragment,
  INPUT_NAMES,
} from '../index.js';

const ENGINE_DIR = new URL('../', import.meta.url);
const DOC = readFileSync(new URL('../../references/policy-format.md', import.meta.url), 'utf8');
/** The text of one numbered section of the doc. */
const section = (n) => DOC.split(new RegExp(`^## ${n}\\. `, 'm'))[1].split(/^## \d+\. /m)[0];
const ticks = (text) => [...text.matchAll(/`([^`]+)`/g)].map((m) => m[1]);

test('the allowed inputs are exactly the section 3 table, in order', () => {
  const names = section(3)
    .split('\n')
    .filter((line) => /^\| `[a-z_]+` \|/.test(line))
    .map((line) => ticks(line)[0]);
  assert.equal(names.length, 13);
  assert.deepEqual([...INPUT_NAMES], names);
  assert.equal(ALLOWED_INPUTS, INPUT_NAMES);
  const ops = ticks(section(3).split('Operators:')[1].split('\n')[0]);
  assert.deepEqual([...ALLOWED_OPS], ops);
});

test('forbidden fragments and actions, and allowed actions, match section 4', () => {
  const paragraphs = section(4).split(/\n\s*\n/);
  const fragmentsPara = paragraphs.find((p) => p.includes('one of:'));
  const actionsPara = paragraphs.find((p) => p.includes('Allowed actions:'));
  assert.deepEqual([...FORBIDDEN_NAME_FRAGMENTS], ticks(fragmentsPara.split('one of:')[1].split('Only names')[0]));
  const allowedPart = actionsPara.split('Allowed actions:')[1].split('Any other action')[0].replace(/\([^)]*\)/g, '');
  assert.deepEqual([...ALLOWED_ACTIONS], ticks(allowedPart));
  assert.deepEqual([...FORBIDDEN_ACTIONS], ticks(actionsPara.split('even if someone adds them:')[1]));
});

test('no allowed name trips a forbidden fragment or a forbidden action', () => {
  for (const name of [...ALLOWED_INPUTS, ...ALLOWED_ACTIONS]) {
    assert.equal(forbiddenFragment(name), null, name);
    assert.ok(!FORBIDDEN_ACTIONS.includes(name), name);
  }
});

test('the sample policy is the section 2 example', () => {
  const block = section(2).match(/```json\n([\s\S]*?)```/)[1];
  const sample = JSON.parse(readFileSync(new URL('samples/policy.example.json', ENGINE_DIR), 'utf8'));
  assert.deepEqual(sample, JSON.parse(block));
});

test('engine sources never read the clock or an unseeded random source', () => {
  const files = readdirSync(ENGINE_DIR).filter((f) => f.endsWith('.js'));
  assert.ok(files.length >= 5, files.join());
  for (const file of files) {
    // Strip comments so the documentation that names these calls does not count.
    const code = readFileSync(new URL(file, ENGINE_DIR), 'utf8')
      .replace(/\/\*[\s\S]*?\*\//g, '')
      .replace(/\/\/.*$/gm, '');
    for (const banned of [/Math\.random\s*\(/, /Date\.now\s*\(/, /new\s+Date\s*\(/, /performance\.now\s*\(/, /crypto\.getRandomValues/]) {
      assert.ok(!banned.test(code), `${file} uses ${banned}`);
    }
  }
});

test('ENGINE_VERSION is 0.1.0 and matches package.json', () => {
  assert.equal(ENGINE_VERSION, '0.1.0');
  const pkg = JSON.parse(readFileSync(new URL('package.json', ENGINE_DIR), 'utf8'));
  assert.equal(pkg.version, ENGINE_VERSION);
  assert.equal(pkg.type, 'module');
  assert.equal(pkg.dependencies, undefined, 'no dependencies');
});

test('the Python checker samples agree with the engine validator', async () => {
  const { readFile } = await import('node:fs/promises');
  const { validatePolicy } = await import('../policy.js');
  const base = new URL('../../scripts/samples/', import.meta.url);
  const good = JSON.parse(await readFile(new URL('policy-valid.json', base), 'utf8'));
  const bad = JSON.parse(await readFile(new URL('policy-bad.json', base), 'utf8'));
  assert.equal(validatePolicy(good).ok, true, JSON.stringify(validatePolicy(good).errors));
  assert.equal(validatePolicy(bad).ok, false);
});
