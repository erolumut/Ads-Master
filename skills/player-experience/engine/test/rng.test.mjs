// RNG, hash and bag tests. The pinned vectors were computed once with an
// independent Python implementation of the same integer algorithms, so a port
// can check itself against these numbers.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createBag, createRng, fnv1a32, mulberry32Step, seedFromString } from '../index.js';

const TETROMINOES = ['I', 'O', 'T', 'S', 'Z', 'J', 'L'];

test('fnv1a32 matches the published FNV-1a 32 bit test vectors', () => {
  assert.equal(fnv1a32(''), 0x811c9dc5);
  assert.equal(fnv1a32('a'), 0xe40c292c);
  assert.equal(fnv1a32('foobar'), 0xbf9cf968);
});

test('fnv1a32 hashes UTF-8 bytes, so non ASCII ids match other platforms', () => {
  assert.equal(fnv1a32('ç'), 412999503); // bytes C3 A7
  assert.equal(fnv1a32('install-1:3'), 4291781809);
  assert.equal(seedFromString('daily:2026-10-16'), 915013228);
  assert.throws(() => fnv1a32(/** @type {any} */ (42)), TypeError);
});

test('mulberry32 with a fixed seed gives the pinned uint32 sequence', () => {
  const r0 = createRng(0);
  assert.deepEqual(Array.from({ length: 5 }, () => r0.nextUint32()), [1144304738, 1416247, 958946056, 627933444, 2007157716]);
  const r42 = createRng(42);
  assert.deepEqual(Array.from({ length: 5 }, () => r42.nextUint32()), [2581720956, 1925393290, 3661312704, 2876485805, 750819978]);
});

test('a string seed is hashed with seedFromString', () => {
  const fromString = createRng('daily:2026-10-16');
  const fromNumber = createRng(seedFromString('daily:2026-10-16'));
  assert.equal(fromString.seed, 915013228);
  const a = Array.from({ length: 3 }, () => fromString.nextUint32());
  assert.deepEqual(a, [941475185, 704103670, 1965879443]);
  assert.deepEqual(Array.from({ length: 3 }, () => fromNumber.nextUint32()), a);
});

test('the state stays 32 bit: output after 6 million draws matches the oracle', () => {
  // The popular snippet keeps its state as a growing double and diverges at
  // draw 4,917,759; this implementation must not.
  const r = createRng(1);
  let x = 0;
  for (let i = 0; i < 6e6; i += 1) x = r.nextUint32();
  assert.equal(x, 1042850813);
});

test('mulberry32Step is a pure function of the state', () => {
  assert.deepEqual(mulberry32Step(0), mulberry32Step(0));
  const [next, out] = mulberry32Step(0);
  assert.equal(next, 0x6d2b79f5);
  assert.equal(out, 1144304738);
});

test('next() is uint32 / 2^32, always in [0, 1)', () => {
  const a = createRng(9);
  const b = createRng(9);
  for (let i = 0; i < 10000; i += 1) {
    const f = a.next();
    assert.ok(f >= 0 && f < 1);
    assert.equal(f, b.nextUint32() / 4294967296);
  }
});

test('same seed gives the same sequence; different seeds differ', () => {
  const draw = (seed) => {
    const r = createRng(seed);
    return Array.from({ length: 20 }, () => r.int(1000));
  };
  assert.deepEqual(draw(123), draw(123));
  assert.notDeepEqual(draw(123), draw(124));
});

test('int(n) gives the pinned values and stays in range', () => {
  const r = createRng(42);
  assert.deepEqual(Array.from({ length: 10 }, () => r.int(6)), [0, 4, 0, 5, 0, 3, 4, 5, 0, 3]);
  const s = createRng(5);
  for (let i = 0; i < 5000; i += 1) {
    const v = s.int(7);
    assert.ok(Number.isInteger(v) && v >= 0 && v < 7);
  }
  assert.equal(createRng(5).int(1), 0);
});

test('int(n) rejection path matches the oracle (half of all words rejected for n = 2^31 + 1)', () => {
  // Raw words for seed 7 start 50271532, 266108690, 4195786334 (rejected),
  // 3002305430 (rejected), 2239590375 (rejected), 1741702388, ...
  const r = createRng(7);
  assert.deepEqual(Array.from({ length: 5 }, () => r.int(2 ** 31 + 1)), [50271532, 266108690, 1741702388, 2002453909, 1030470827]);
});

test('int(n) is close to uniform (chi square, 6 buckets, 60,000 draws)', () => {
  const r = createRng(2026);
  const counts = new Array(6).fill(0);
  const n = 60000;
  for (let i = 0; i < n; i += 1) counts[r.int(6)] += 1;
  const exp = n / 6;
  const chi2 = counts.reduce((sum, c) => sum + (c - exp) ** 2 / exp, 0);
  assert.ok(chi2 < 20.5, `chi square ${chi2.toFixed(2)} (5 degrees of freedom, p 0.001 cut 20.5)`);
});

test('createRng and int refuse values a port could not represent', () => {
  assert.throws(() => createRng(-1), RangeError);
  assert.throws(() => createRng(1.5), RangeError);
  assert.throws(() => createRng(2 ** 32), RangeError);
  assert.throws(() => createRng(/** @type {any} */ (undefined)), RangeError);
  const r = createRng(1);
  assert.throws(() => r.int(0), RangeError);
  assert.throws(() => r.int(2.5), RangeError);
  assert.throws(() => r.int(2 ** 32 + 1), RangeError);
});

test('bag: the first two bags for seed 42 match the oracle', () => {
  const bag = createBag(TETROMINOES, createRng(42));
  const first = Array.from({ length: 7 }, () => bag.next());
  const second = Array.from({ length: 7 }, () => bag.next());
  assert.deepEqual(first, ['T', 'L', 'I', 'O', 'J', 'Z', 'S']);
  assert.deepEqual(second, ['L', 'S', 'Z', 'O', 'I', 'J', 'T']);
});

test('bag never repeats an item within a bag: every bag is a permutation', () => {
  const bag = createBag(TETROMINOES, createRng(99));
  for (let b = 0; b < 200; b += 1) {
    const dealt = Array.from({ length: TETROMINOES.length }, () => bag.next());
    assert.equal(new Set(dealt).size, TETROMINOES.length, `bag ${b} repeated an item: ${dealt.join('')}`);
    assert.deepEqual(dealt.slice().sort(), TETROMINOES.slice().sort());
  }
});

test('bag caps droughts: no item waits more than 2n minus 2 draws', () => {
  const n = TETROMINOES.length;
  const bag = createBag(TETROMINOES, createRng(7));
  /** @type {Map<string, number>} */
  const last = new Map();
  let worst = 0;
  for (let i = 0; i < 70000; i += 1) {
    const item = bag.next();
    if (last.has(item)) worst = Math.max(worst, i - /** @type {number} */ (last.get(item)) - 1);
    last.set(item, i);
  }
  assert.ok(worst <= 2 * n - 2, `worst gap ${worst}`);
});

test('bag shuffles lazily, reports what is left, and copies its input', () => {
  const items = ['a', 'b', 'c'];
  const rng = createRng(3);
  const bag = createBag(items, rng);
  assert.equal(bag.size, 3);
  assert.equal(bag.remaining(), 0); // nothing shuffled yet, no rng consumed
  assert.equal(rng.nextUint32(), createRng(3).nextUint32());
  items.push('d'); // later edits to the caller's array do not leak in
  const dealt = [bag.next(), bag.next(), bag.next()];
  assert.equal(bag.remaining(), 0);
  assert.deepEqual(dealt.slice().sort(), ['a', 'b', 'c']);
  assert.throws(() => createBag([], createRng(1)), TypeError);
  assert.throws(() => createBag(['x'], /** @type {any} */ ({})), TypeError);
});
