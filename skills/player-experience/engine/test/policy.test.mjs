// validatePolicy(): the runtime mirror of policy-format.md section 5.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createEngine, createRng, forbiddenFragment, validatePolicy } from '../index.js';

const EXAMPLE = JSON.parse(readFileSync(new URL('../samples/policy.example.json', import.meta.url), 'utf8'));
/** A fresh deep copy of the example, edited by `edit`. */
const variant = (edit) => {
  const p = structuredClone(EXAMPLE);
  edit(p);
  return p;
};
const easeRule = (id, value = -1, maxPerSession = 1) => ({
  id,
  modes: ['levels'],
  when: [{ input: 'fail_streak', op: '>=', value: 2 }],
  then: { action: 'difficulty_offset', value },
  reason: 'struggling',
  explainKey: 'pxe.reason.struggling',
  ...(maxPerSession === null ? {} : { maxPerSession }), // null: no cap
});
/** Asserts the policy is refused with an error matching `pattern`. */
const refused = (policy, pattern) => {
  const r = validatePolicy(policy);
  assert.equal(r.ok, false, 'expected the policy to be refused');
  assert.ok(r.errors.some((e) => pattern.test(e)), `no error matches ${pattern}: ${JSON.stringify(r.errors)}`);
};

test('the example policy is valid, with no errors and no warnings', () => {
  assert.deepEqual(validatePolicy(EXAMPLE), { ok: true, errors: [], warnings: [] });
});

test('an unsupported pxeVersion stops validation at the first error', () => {
  const r = validatePolicy(variant((p) => { p.pxeVersion = '0.2'; delete p.rules; }));
  assert.equal(r.ok, false);
  assert.equal(r.errors.length, 1);
  assert.match(r.errors[0], /pxeVersion "0.2" is not supported/);
  assert.equal(validatePolicy(null).ok, false);
  assert.equal(validatePolicy([]).ok, false);
  assert.equal(validatePolicy('{}').ok, false);
});

test('forbidden inputs are refused in any case or separator style', () => {
  for (const name of ['payer_score', 'PayerScore', 'ad-value', 'adValue', 'eCPM_bucket', 'deviceTier', 'player_age', 'rewardedReady', 'country', 'LTV', 'is_whale', 'monetization_segment', 'battery_low']) {
    refused(variant((p) => { p.rules[0].when.push({ input: name, op: '>=', value: 1 }); }), /forbidden \(contains/);
  }
  assert.equal(forbiddenFragment('Ad.Available'), 'ad_available');
  assert.equal(forbiddenFragment('fail_streak'), null);
});

test('an input outside section 3 is refused even with an innocent name', () => {
  refused(variant((p) => { p.rules[0].when[0].input = 'boredom_score'; }), /not an allowed input/);
  refused(variant((p) => { p.rules[0].when[0].input = 'Fail_Streak'; }), /not an allowed input/); // exact names only
});

test('forbidden and unknown actions are refused', () => {
  for (const name of ['force_loss', 'score_bonus', 'biasPieces', 'Death', 'rig', 'harvest']) {
    refused(variant((p) => { p.rules[1].then = { action: name }; }), /action .* is forbidden/);
  }
  refused(variant((p) => { p.rules[1].then = { action: 'offer_revive_for_ad_value' }; }), /forbidden \(contains "ad_value"\)/);
  refused(variant((p) => { p.rules[1].then = { action: 'show_offer' }; }), /not an allowed action/);
});

test('suggest_mode must point at a declared, non shared mode', () => {
  const suggest = (mode) => variant((p) => { p.rules[1].then = { action: 'suggest_mode', mode }; });
  assert.equal(validatePolicy(suggest('practice')).ok, true);
  refused(suggest('daily'), /may not point at shared mode "daily"/);
  refused(suggest('ranked'), /needs a declared mode/);
});

test('a rule naming a shared mode, an undeclared mode or no mode is refused', () => {
  refused(variant((p) => { p.rules[0].modes.push('daily'); }), /mode "daily" is shared/);
  refused(variant((p) => { p.rules[0].modes = []; }), /modes must name at least one mode/);
  refused(variant((p) => { delete p.rules[0].modes; }), /modes must name at least one mode/);
  refused(variant((p) => { p.rules[0].modes = ['ranked']; }), /"ranked" is not declared/);
  refused(variant((p) => { delete p.modes[1].shared; }), /shared must be true or false/);
});

test('difficulty offsets must stay inside the published range and two steps', () => {
  refused(variant((p) => { p.rules[0].then.value = -2; }), /outside minOffset -1 to maxOffset 1/);
  refused(variant((p) => { p.difficulty.minOffset = -3; p.difficulty.steps.unshift(-3); }), /wider than 2 steps/);
  refused(variant((p) => { p.difficulty.maxOffset = 3; p.difficulty.steps.push(3); }), /wider than 2 steps/);
  refused(variant((p) => { p.rules[0].then.value = -0.5; }), /integer value/);
  refused(variant((p) => { p.difficulty.default = 2; }), /default must lie between/);
  refused(variant((p) => { p.difficulty.minOffset = 1; }), /minOffset <= 0 <= maxOffset/);
});

test('more than one easing rule without maxPerSession 1 is refused; one is allowed', () => {
  assert.equal(validatePolicy(variant((p) => { p.rules[0].maxPerSession = 2; })).ok, true);
  assert.equal(validatePolicy(variant((p) => { p.rules.push(easeRule('ease_b')); })).ok, true);
  refused(
    variant((p) => { p.rules[0].maxPerSession = 2; p.rules.push(easeRule('ease_b', -1, null)); }),
    /2 easing rules .* lack maxPerSession 1/,
  );
});

test('a rule needs an id, a reason, an explain key and valid conditions', () => {
  refused(variant((p) => { delete p.rules[0].reason; }), /reason is missing/);
  refused(variant((p) => { p.rules[0].explainKey = ' '; }), /explainKey is missing/);
  refused(variant((p) => { p.rules[1].id = p.rules[0].id; }), /id is used twice/);
  refused(variant((p) => { p.rules[0].when[0].op = '=>'; }), /op "=>" is not one of/);
  refused(variant((p) => { p.rules[0].when[0].value = '3'; }), /value must be a number/);
  refused(variant((p) => { p.rules[0].maxPerSession = 0; }), /maxPerSession must be an integer, 1 or more/);
});

test('player controls must all be offered', () => {
  refused(variant((p) => { p.player.settings = ['auto', 'easy', 'normal']; }), /missing hard/);
  refused(variant((p) => { p.player.settings = ['easy', 'normal', 'hard']; }), /missing auto/);
  for (const flag of ['explain', 'log', 'reset']) {
    refused(variant((p) => { p.player[flag] = false; }), new RegExp(`player.${flag} must be true`));
  }
});

test('scores may never change after the fact or let assisted runs onto shared boards', () => {
  refused(variant((p) => { p.scores.modifyAfterFact = true; }), /modifyAfterFact must be false/);
  refused(variant((p) => { p.scores.assistedRunsOnSharedBoards = true; }), /assistedRunsOnSharedBoards must be false/);
});

test('the experiment needs a whole holdout percent from 1 to 20, a salt and a primary metric', () => {
  for (const pct of [0, 21, 2.5, '5']) {
    refused(variant((p) => { p.experiment.holdoutPercent = pct; }), /holdoutPercent must be a whole number from 1 to 20/);
  }
  refused(variant((p) => { delete p.experiment.holdoutSalt; }), /holdoutSalt must be a non empty string/);
  refused(variant((p) => { p.experiment.holdoutSalt = ''; }), /holdoutSalt must be a non empty string/);
  refused(variant((p) => { p.experiment.primary = []; }), /primary must name at least one metric/);
});

test('minors get the strict tier and no streak or loss return reasons', () => {
  refused(variant((p) => { p.audience.minorsTier = 'standard'; }), /minorsTier must be "strict"/);
  assert.equal(validatePolicy(variant((p) => { p.audience = { minimumAge: 18, minorsTier: 'standard' }; })).ok, true);
  for (const source of ['streak', 'loss']) {
    refused(variant((p) => { p.returnReasons.push({ id: 'r', source, maxPerDay: 1, quietHours: ['21:00', '09:00'] }); }), /not allowed in the strict tier/);
  }
});

test('return reasons need maxPerDay and quiet hours', () => {
  refused(variant((p) => { delete p.returnReasons[0].maxPerDay; }), /maxPerDay must be an integer/);
  refused(variant((p) => { delete p.returnReasons[0].quietHours; }), /quietHours must be two "HH:MM" times/);
  refused(variant((p) => { p.returnReasons[0].quietHours = ['9pm', '9am']; }), /quietHours/);
  assert.equal(validatePolicy(variant((p) => { p.returnReasons = []; })).ok, true);
});

test('a missing section is refused', () => {
  for (const key of ['modes', 'difficulty', 'player', 'rules', 'returnReasons', 'scores', 'experiment', 'audience']) {
    refused(variant((p) => { delete p[key]; }), new RegExp(`missing ${key}`));
  }
});

test('warnings: a short read and a policy that only eases', () => {
  const short = validatePolicy(variant((p) => { p.experiment.readAfterDays = 14; }));
  assert.equal(short.ok, true);
  assert.match(short.warnings.join(), /readAfterDays is under 28/);
  const onlyEases = validatePolicy(variant((p) => { p.rules.pop(); }));
  assert.equal(onlyEases.ok, true);
  assert.match(onlyEases.warnings.join(), /no raising rule/);
});

test('fuzz: validatePolicy never throws, and every policy it accepts runs without throwing', () => {
  /** Every path from the root to a node, such as ['rules', 0, 'when', 0, 'op']. */
  const paths = [];
  const walk = (node, path) => {
    if (path.length > 0) paths.push(path);
    if (node && typeof node === 'object') {
      for (const key of Array.isArray(node) ? node.keys() : Object.keys(node)) walk(node[key], [...path, key]);
    }
  };
  walk(EXAMPLE, []);
  const junk = [null, 0, -1, 1.5, 3, '', 'x', 'daily', 'levels', true, false, [], {}, [null], [0], { id: 'x' }, '__delete__'];
  const rng = createRng(31337);
  const probes = [{}, { fail_streak: 9, attempts_on_level: 9, hint_uses_level: 0, fast_solve_streak: 9, rating_gap: 500 }];
  let accepted = 0;
  for (let i = 0; i < 4000; i += 1) {
    const p = structuredClone(EXAMPLE);
    const mutations = 1 + rng.int(3);
    for (let m = 0; m < mutations; m += 1) {
      const path = paths[rng.int(paths.length)];
      let parent = p;
      for (const key of path.slice(0, -1)) parent = parent && typeof parent === 'object' ? parent[key] : undefined;
      if (!parent || typeof parent !== 'object') continue;
      const value = junk[rng.int(junk.length)];
      const key = path[path.length - 1];
      if (value === '__delete__') delete parent[key];
      else parent[key] = structuredClone(value);
    }
    const r = validatePolicy(p);
    assert.equal(typeof r.ok, 'boolean');
    if (!r.ok) continue;
    accepted += 1;
    const e = createEngine(p, { installId: 'install-1' });
    for (const mode of [...new Set(p.modes.map((m) => m.id)), 'nope']) {
      for (const setting of ['auto', 'easy', 'hard']) {
        for (const probe of probes) e.evaluate(probe, mode, { setting, sessionId: `s${i}` });
      }
    }
  }
  assert.ok(accepted > 50, `only ${accepted} mutated policies were accepted; the fuzz is not reaching the engine`);
});

test('sparse arrays (a policy built in code) are refused, not crashed on later', () => {
  refused(variant((p) => { delete p.rules[1]; }), /rules\[1\] must be an object/);
  refused(variant((p) => { delete p.modes[0]; }), /modes\[0\] needs a non empty id/);
  refused(variant((p) => { delete p.rules[1].when[0]; }), /when\[0\]: must be an object/);
  refused(variant((p) => { p.experiment.primary = new Array(1); }), /primary must name at least one metric/);
  refused(variant((p) => { delete p.returnReasons[0].quietHours[1]; }), /quietHours/);
});
