// createEngine() and evaluate(): the runtime guarantees of policy-format.md section 6.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { applyEvent, createEngine, createPlayerState, createRng, ENGINE_VERSION, holdoutBucket } from '../index.js';

const EXAMPLE = JSON.parse(readFileSync(new URL('../samples/policy.example.json', import.meta.url), 'utf8'));
const SALT = EXAMPLE.experiment.holdoutSalt;
const variant = (edit) => {
  const p = structuredClone(EXAMPLE);
  edit(p);
  return p;
};
// Buckets pinned with an independent Python FNV-1a: install-1 is bucket 82
// (treatment), install-53 is the first id below 5 (holdout).
const TREATMENT = 'install-1';
const HOLDOUT = 'install-53';
const engine = (policy = EXAMPLE, opts = {}) => createEngine(policy, { installId: TREATMENT, ...opts });

const STRUGGLING = Object.freeze({ fail_streak: 3, attempts_on_level: 2, hint_uses_level: 0 });
const STUCK = Object.freeze({ fail_streak: 0, attempts_on_level: 2, hint_uses_level: 0 });
const CRUISING = Object.freeze({ fast_solve_streak: 3 });

/** UUID shaped ids from a seeded rng, so the share test is reproducible. */
const uuids = (count, seed) => {
  const rng = createRng(seed);
  const hex = (n) => Array.from({ length: n }, () => rng.int(16).toString(16)).join('');
  return Array.from({ length: count }, () => `${hex(8)}-${hex(4)}-4${hex(3)}-${hex(4)}-${hex(12)}`);
};

test('shared modes return no action, whatever the rules, inputs or setting say', () => {
  const sharedRule = variant(() => {});
  const e = engine(sharedRule);
  for (const setting of ['auto', 'easy', 'hard']) {
    const d = e.evaluate(STRUGGLING, 'daily', { setting });
    assert.equal(d.action, null);
    assert.equal(d.outcome, 'shared_mode');
    assert.equal(d.offsetNow, 0, 'same parameters for everyone');
  }
  const unknown = e.evaluate(STRUGGLING, 'ranked');
  assert.equal(unknown.action, null);
  assert.equal(unknown.outcome, 'unknown_mode', 'an undeclared mode is treated as shared');
  assert.equal(e.log().length, 0);
});

test('holdout installs get no actions but are told so; their own setting still applies', () => {
  assert.ok(holdoutBucket(HOLDOUT, SALT) < EXAMPLE.experiment.holdoutPercent);
  const e = engine(EXAMPLE, { installId: HOLDOUT });
  assert.equal(e.holdout, true);
  const d = e.evaluate(STRUGGLING, 'levels');
  assert.deepEqual(
    { action: d.action, ruleId: d.ruleId, holdout: d.holdout, outcome: d.outcome, offsetNow: d.offsetNow },
    { action: null, ruleId: null, holdout: true, outcome: 'holdout', offsetNow: EXAMPLE.difficulty.default },
  );
  assert.equal(e.evaluate(CRUISING, 'practice', { setting: 'hard' }).offsetNow, 1);
  assert.equal(e.log().length, 0);
  const t = engine();
  assert.equal(t.holdout, false);
  assert.equal(t.evaluate(STRUGGLING, 'levels').holdout, false);
});

test('holdout bucket is FNV-1a of installId:holdoutSalt modulo 100 (pinned)', () => {
  assert.equal(holdoutBucket('install-1', 'pxe-holdout-2026'), 82);
  assert.equal(holdoutBucket('install-4', 'pxe-holdout-2026'), 19);
  assert.equal(holdoutBucket('install-53', 'pxe-holdout-2026') < 5, true);
  assert.throws(() => holdoutBucket(/** @type {any} */ (1), SALT), TypeError);
});

test('holdout is stable across policy revisions with the same salt; a new salt redraws it', () => {
  const rev3 = EXAMPLE;
  const rev4 = variant((p) => { p.policyRevision = 4; p.rules[0].when[0].value = 4; });
  const resalted = variant((p) => { p.experiment.holdoutSalt = 'pxe-holdout-2027'; });
  const ids = uuids(400, 11);
  let moved = 0;
  for (const installId of ids) {
    const a = createEngine(rev3, { installId }).holdout;
    assert.equal(createEngine(rev3, { installId }).holdout, a, 'same id, same answer');
    assert.equal(createEngine(rev4, { installId }).holdout, a, `revision bump moved ${installId}`);
    if (createEngine(resalted, { installId }).holdout !== a) moved += 1;
  }
  assert.ok(moved > 0, 'a new salt should start a new holdout');
});

test('holdout share is close to holdoutPercent over 10,000 install ids', () => {
  const ids = uuids(10000, 2026);
  for (const pct of [5, 20]) {
    const share = ids.filter((id) => holdoutBucket(id, SALT) < pct).length / ids.length;
    // Binomial sd at 5% is 0.22 points, at 20% 0.40 points; allow about 4 sd.
    const tolerance = pct === 5 ? 0.01 : 0.016;
    assert.ok(Math.abs(share - pct / 100) < tolerance, `share ${share} for ${pct}%`);
  }
  for (const installId of ids.slice(0, 200)) {
    assert.equal(createEngine(EXAMPLE, { installId }).holdout, holdoutBucket(installId, SALT) < 5);
  }
});

test('the first matching rule in file order wins', () => {
  assert.equal(engine().evaluate(STRUGGLING, 'levels').ruleId, 'ease_after_fails');
  const hintFirst = variant((p) => { p.rules = [p.rules[1], p.rules[0], p.rules[2]]; });
  assert.equal(engine(hintFirst).evaluate(STRUGGLING, 'levels').ruleId, 'offer_hint_when_stuck');
  // A rule only applies in the modes it names: practice has no hint rule.
  assert.equal(engine().evaluate(STUCK, 'practice').outcome, 'no_match');
});

test('a fixed setting maps to fixed offsets and disables difficulty actions; offers still fire', () => {
  const e = engine();
  const expectations = { easy: -1, normal: 0, hard: 1 };
  for (const [setting, offset] of Object.entries(expectations)) {
    const d = e.evaluate(STRUGGLING, 'levels', { setting, sessionId: `s-${setting}` });
    assert.equal(d.action, 'offer_hint', `${setting}: the easing rule is skipped, the offer is not`);
    assert.equal(d.offsetNow, offset);
  }
  assert.equal(e.evaluate(CRUISING, 'levels', { setting: 'hard', sessionId: 's-x' }).outcome, 'no_match');
  // Back on auto the adaptive offset was never touched.
  assert.equal(e.offset(), 0);
  const auto = e.evaluate(STRUGGLING, 'levels', { sessionId: 's-auto' });
  assert.deepEqual([auto.action, auto.offsetNow], ['difficulty_offset', -1]);
  assert.equal(e.evaluate({}, 'levels', { setting: 'normal', sessionId: 's-auto' }).offsetNow, 0);
  assert.equal(e.offset(), -1, 'a fixed setting does not overwrite the adaptive offset');
  // The default setting given at creation applies when evaluate passes none.
  assert.equal(engine(EXAMPLE, { setting: 'hard' }).evaluate({}, 'levels').offsetNow, 1);
});

test('fixed offsets are clamped to the published range', () => {
  const raiseOnly = variant((p) => {
    p.difficulty.minOffset = 0;
    p.rules = p.rules.filter((r) => r.id !== 'ease_after_fails');
  });
  const e = engine(raiseOnly);
  assert.equal(e.evaluate({}, 'levels', { setting: 'easy' }).offsetNow, 0);
  assert.equal(e.evaluate({}, 'levels', { setting: 'hard' }).offsetNow, 1);
});

test('maxPerSession caps a rule per session id; a new session starts fresh', () => {
  const e = engine();
  const hints = Array.from({ length: 4 }, () => e.evaluate(STUCK, 'levels', { sessionId: 'a' }).action);
  assert.deepEqual(hints, ['offer_hint', 'offer_hint', 'offer_hint', null]);
  assert.equal(e.evaluate(STUCK, 'levels', { sessionId: 'b' }).action, 'offer_hint');
  assert.equal(e.evaluate(STUCK, 'levels', { sessionId: 'a' }).action, null, 'session a is still capped');
});

test('without a session id the player state supplies one, so caps follow real sessions', () => {
  const T = 1_792_000_000_000;
  let s = applyEvent(createPlayerState(), { type: 'session_start', at: T });
  s = applyEvent(s, { type: 'level_start', at: T + 1, levelId: 'L1', levelRating: 1500 });
  s = applyEvent(s, { type: 'level_end', at: T + 2, levelId: 'L1', result: 'fail' });
  s = applyEvent(s, { type: 'level_start', at: T + 3, levelId: 'L1' });
  s = applyEvent(s, { type: 'level_end', at: T + 4, levelId: 'L1', result: 'fail' });
  s = applyEvent(s, { type: 'level_start', at: T + 5, levelId: 'L1' });
  const e = engine();
  const first = e.evaluate(s, 'levels');
  assert.equal(first.action, 'offer_hint', 'two finished attempts, no hint yet: offer one');
  assert.equal(e.log()[0].sessionId, 'session:1');
  assert.equal(e.log()[0].at, T + 5);
  s = applyEvent(s, { type: 'level_end', at: T + 6, levelId: 'L1', result: 'fail' });
  s = applyEvent(s, { type: 'level_start', at: T + 7, levelId: 'L1' });
  assert.equal(e.evaluate(s, 'levels').ruleId, 'ease_after_fails', 'third fail: ease once');
  s = applyEvent(s, { type: 'level_end', at: T + 8, levelId: 'L1', result: 'fail' });
  s = applyEvent(s, { type: 'level_start', at: T + 9, levelId: 'L1' });
  assert.equal(e.evaluate(s, 'levels').ruleId, 'offer_hint_when_stuck', 'no second easing this session');
});

test('silent easing happens at most once per session, across different easing rules', () => {
  const twoEasings = variant((p) => {
    p.difficulty.minOffset = -2;
    p.rules.splice(1, 0, {
      id: 'ease_on_rating_gap',
      modes: ['levels'],
      when: [{ input: 'rating_gap', op: '>=', value: 200 }],
      then: { action: 'difficulty_offset', value: -1 },
      reason: 'too_hard',
      explainKey: 'pxe.reason.too_hard',
      maxPerSession: 1,
    });
  });
  const e = engine(twoEasings);
  const hard = { fail_streak: 3, rating_gap: 250 };
  assert.equal(e.evaluate(hard, 'levels', { sessionId: 's1' }).ruleId, 'ease_after_fails');
  const second = e.evaluate(hard, 'levels', { sessionId: 's1' });
  assert.equal(second.outcome, 'no_match', 'ease_on_rating_gap would be a second silent easing');
  assert.equal(second.offsetNow, -1);
  assert.equal(e.evaluate(hard, 'levels', { sessionId: 's2' }).offsetNow, -2, 'next session may ease again');
});

test('offsets are clamped, and a step that clamping would cancel yields to the next rule', () => {
  const withBreak = variant((p) => {
    p.rules.push({
      id: 'break_when_cruising',
      modes: ['levels'],
      when: [{ input: 'fast_solve_streak', op: '>=', value: 3 }],
      then: { action: 'offer_break' },
      reason: 'long_run',
      explainKey: 'pxe.reason.long_run',
    });
  });
  const e = engine(withBreak);
  const raised = e.evaluate(CRUISING, 'levels', { sessionId: 's1' });
  assert.deepEqual([raised.action, raised.value, raised.offsetNow], ['difficulty_offset', 1, 1]);
  const atMax = e.evaluate(CRUISING, 'levels', { sessionId: 's2' });
  assert.deepEqual([atMax.action, atMax.offsetNow], ['offer_break', 1], 'already at maxOffset: no silent no-op');
  // Same at the bottom: once at minOffset the easing rule gives way to the hint.
  const f = engine();
  f.evaluate(STRUGGLING, 'levels', { sessionId: 's1' });
  const atMin = f.evaluate(STRUGGLING, 'levels', { sessionId: 's2' });
  assert.deepEqual([atMin.action, atMin.offsetNow], ['offer_hint', -1]);
  assert.ok(f.log().every((entry) => entry.offsetNow >= -1 && entry.offsetNow <= 1));
});

test('every returned action carries its rule id, reason and explain key and is logged', () => {
  const e = engine();
  e.evaluate(STRUGGLING, 'shared_or_not', {}); // unknown mode: not logged
  e.evaluate(STRUGGLING, 'daily'); // shared: not logged
  e.evaluate({}, 'levels'); // no match: not logged
  const d = e.evaluate(STRUGGLING, 'levels', { sessionId: 'abc' });
  assert.deepEqual(d, {
    action: 'difficulty_offset',
    ruleId: 'ease_after_fails',
    reason: 'struggling',
    explainKey: 'pxe.reason.struggling',
    value: -1,
    targetMode: null,
    offsetNow: -1,
    holdout: false,
    outcome: 'action',
  });
  assert.ok(Object.isFrozen(d));
  const log = e.log();
  assert.deepEqual(log, [
    {
      at: null, // a plain inputs object carries no event time
      sessionId: 'abc',
      mode: 'levels',
      ruleId: 'ease_after_fails',
      reason: 'struggling',
      explainKey: 'pxe.reason.struggling',
      action: 'difficulty_offset',
      value: -1,
      targetMode: null,
      offsetNow: -1,
      policyRevision: 3,
      engineVersion: ENGINE_VERSION,
    },
  ]);
  log.push(/** @type {any} */ ({}));
  assert.equal(e.log().length, 1, 'log() returns a copy');
  assert.ok(Object.isFrozen(e.log()[0]));
  const suggest = engine(variant((p) => { p.rules[1].then = { action: 'suggest_mode', mode: 'practice' }; }));
  const s = suggest.evaluate(STUCK, 'levels');
  assert.deepEqual([s.action, s.targetMode, s.value], ['suggest_mode', 'practice', null]);
});

test('reset() returns the offset to default and clears counters; the log is kept', () => {
  const e = engine();
  e.evaluate(STRUGGLING, 'levels', { sessionId: 's1' });
  assert.equal(e.offset(), -1);
  e.reset();
  assert.equal(e.offset(), 0);
  const again = e.evaluate(STRUGGLING, 'levels', { sessionId: 's1' });
  assert.equal(again.ruleId, 'ease_after_fails', 'counters were cleared');
  assert.equal(e.log().length, 2);
});

test('save() and options.saved carry offset, caps and log across app launches', () => {
  const a = engine();
  a.evaluate(STRUGGLING, 'levels', { sessionId: 's1' });
  a.evaluate(STUCK, 'levels', { sessionId: 's1' });
  const saved = JSON.parse(JSON.stringify(a.save()));
  const b = engine(EXAMPLE, { saved });
  assert.equal(b.offset(), -1);
  assert.deepEqual(b.log(), a.log());
  assert.notEqual(b.evaluate(STRUGGLING, 'levels', { sessionId: 's1' }).ruleId, 'ease_after_fails', 'cap survived');
  // A newer policy with a narrower range clamps the restored offset.
  const narrow = variant((p) => {
    p.policyRevision = 4;
    p.difficulty.minOffset = 0;
    p.rules = p.rules.filter((r) => r.id !== 'ease_after_fails');
  });
  assert.equal(engine(narrow, { saved }).offset(), 0);
  assert.throws(() => engine(EXAMPLE, { saved: /** @type {any} */ ({ offset: 'x' }) }), /engine.save/);
});

test('evaluate never mutates the player state, and unknown inputs never match', () => {
  const T = 1_792_000_000_000;
  const s = applyEvent(createPlayerState(), { type: 'session_start', at: T });
  const before = structuredClone(s);
  engine().evaluate(s, 'levels');
  assert.deepEqual(s, before);
  const notEqualRule = variant((p) => {
    p.rules.unshift({
      id: 'break_on_slow_moves',
      modes: ['levels'],
      when: [{ input: 'median_move_ms', op: '!=', value: 0 }],
      then: { action: 'offer_break' },
      reason: 'slow',
      explainKey: 'pxe.reason.slow',
    });
  });
  assert.equal(engine(notEqualRule).evaluate({ median_move_ms: null }, 'levels').outcome, 'no_match');
  assert.equal(engine(notEqualRule).evaluate({ median_move_ms: '5' }, 'levels').outcome, 'no_match');
  assert.equal(engine(notEqualRule).evaluate({ median_move_ms: 5 }, 'levels').action, 'offer_break');
});

test('createEngine refuses a broken policy, a missing install id and an unknown setting', () => {
  const broken = variant((p) => { p.rules[0].when[0].input = 'payer_score'; });
  assert.throws(
    () => engine(broken),
    (err) => err instanceof Error && Array.isArray(err.errors) && /payer_score/.test(err.errors.join()),
  );
  assert.throws(() => createEngine(EXAMPLE, /** @type {any} */ ({})), /installId/);
  assert.throws(() => engine(EXAMPLE, { setting: 'expert' }), /setting must be one of/);
  assert.throws(() => engine().evaluate({}, 'levels', { setting: 'Auto' }), /setting must be one of/);
});

test('the engine keeps its own frozen copy of the policy', () => {
  const p = structuredClone(EXAMPLE);
  const e = engine(p);
  p.rules[0].when[0].value = 0; // editing the caller's object afterwards
  p.modes[0].shared = false;
  assert.equal(e.evaluate({ fail_streak: 1 }, 'levels').outcome, 'no_match');
  assert.equal(e.evaluate(STRUGGLING, 'daily').outcome, 'shared_mode');
  assert.equal(e.policyRevision, 3);
  assert.equal(e.engineVersion, ENGINE_VERSION);
});
