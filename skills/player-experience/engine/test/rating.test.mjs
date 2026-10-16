import { test } from 'node:test';
import assert from 'node:assert/strict';
import { DEFAULT_K, DEFAULT_LEVEL_K, expected, update } from '../index.js';

const close = (a, b, eps = 1e-12) => assert.ok(Math.abs(a - b) < eps, `${a} != ${b}`);

test('expected(): equal ratings give 0.5 and a 400 point edge gives 10 to 1 odds', () => {
  assert.equal(expected(1500, 1500), 0.5);
  close(expected(1900, 1500), 10 / 11);
  close(expected(1500, 1900), 1 / 11);
});

test('expected() is symmetric: both sides sum to 1', () => {
  for (const [a, b] of [[1500, 1500], [1200, 1700], [2100, 900], [0, 37.5]]) {
    close(expected(a, b) + expected(b, a), 1);
  }
  assert.ok(expected(1600, 1500) > expected(1500, 1500));
});

test('a win raises the player and lowers the level; a fail does the opposite', () => {
  const win = update(1500, 1500, true);
  assert.equal(win.player, 1500 + DEFAULT_K * 0.5);
  assert.equal(win.level, 1500 - DEFAULT_LEVEL_K * 0.5);
  const fail = update(1500, 1500, false);
  assert.equal(fail.player, 1500 - DEFAULT_K * 0.5);
  assert.equal(fail.level, 1500 + DEFAULT_LEVEL_K * 0.5);
  assert.equal(win.expected, 0.5);
});

test('an upset moves ratings more than an expected result', () => {
  const upsetWin = update(1300, 1700, true).player - 1300;
  const expectedWin = update(1700, 1300, true).player - 1700;
  assert.ok(upsetWin > expectedWin && expectedWin > 0);
  const upsetFail = 1700 - update(1700, 1300, false).player;
  const expectedFail = 1300 - update(1300, 1700, false).player;
  assert.ok(upsetFail > expectedFail && expectedFail > 0);
});

test('the level K is smaller by default and both K values are configurable', () => {
  assert.ok(DEFAULT_LEVEL_K < DEFAULT_K);
  const r = update(1500, 1500, true, { k: 16, levelK: 4 });
  assert.equal(r.player, 1508);
  assert.equal(r.level, 1498);
  // With equal K the sum of both ratings is conserved.
  const eq = update(1432, 1611, false, { k: 20, levelK: 20 });
  close(eq.player + eq.level, 1432 + 1611, 1e-9);
  const frozen = update(1500, 1500, true, { k: 0, levelK: 0 });
  assert.deepEqual([frozen.player, frozen.level], [1500, 1500]);
});

test('ratings refuse non numbers, a non boolean result and negative K', () => {
  assert.throws(() => expected(Number.NaN, 1500), TypeError);
  assert.throws(() => expected(1500, Infinity), TypeError);
  assert.throws(() => update(1500, 1500, /** @type {any} */ (1)), TypeError);
  assert.throws(() => update(1500, 1500, true, { k: -1 }), RangeError);
});
