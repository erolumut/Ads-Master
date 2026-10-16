import { test } from 'node:test';
import assert from 'node:assert/strict';
import { applyEvent, createPlayerState, INPUT_NAMES, inputs } from '../index.js';

const MIN = 60 * 1000;
const T = 1_792_000_000_000; // a fixed epoch ms; the engine never reads the clock
const ev = (type, at, extra = {}) => ({ type, at, ...extra });
/** Folds events left to right. */
const play = (events, state = createPlayerState()) => events.reduce(applyEvent, state);

test('a fresh state exposes exactly the section 3 inputs with honest starting values', () => {
  const values = inputs(createPlayerState());
  assert.deepEqual(Object.keys(values), [...INPUT_NAMES]);
  assert.deepEqual(values, {
    fail_streak: 0,
    attempts_on_level: 0,
    fast_solve_streak: 0,
    hint_uses_level: 0,
    hint_uses_session: 0,
    median_move_ms: null,
    restarts_recent: 0,
    session_gap_hours: null,
    sessions_today: 0,
    skill_rating: 1500,
    level_rating: null,
    rating_gap: null,
    quit_rate_recent: null,
  });
});

test('scripted session: every input after a fixed event sequence', () => {
  const afterFirstSession = play([
    ev('session_start', T, { localDay: '2026-10-16' }),
    ev('level_start', T + 1 * MIN, { levelId: 'L1', levelRating: 1500 }),
    ev('level_end', T + 2 * MIN, { levelId: 'L1', result: 'fail', durationMs: 60000, medianMoveMs: 1200, medianLevelMs: 90000 }),
    ev('level_start', T + 2.5 * MIN, { levelId: 'L1', levelRating: 1500 }),
    ev('restart', T + 3 * MIN, { medianMoveMs: 1500 }),
    ev('level_start', T + 3 * MIN, { levelId: 'L1', levelRating: 1500 }),
    ev('hint_used', T + 4 * MIN),
    ev('level_end', T + 5 * MIN, { levelId: 'L1', result: 'win', durationMs: 80000, medianMoveMs: 900, medianLevelMs: 90000 }),
    ev('level_start', T + 6 * MIN, { levelId: 'L2', levelRating: 1600 }),
    ev('level_end', T + 7 * MIN, { levelId: 'L2', result: 'quit', durationMs: 30000, medianMoveMs: 2000, medianLevelMs: 120000 }),
  ]);
  // Fail on an even level: 1500 + 32 * (0 - 0.5) = 1484. Then a win on the
  // 1500 level from 1484: 1484 + 32 * (1 - 1 / (1 + 10 ^ (16 / 400))).
  const rating = 1484 + 32 * (1 - 1 / (1 + 10 ** (16 / 400)));
  assert.deepEqual(inputs(afterFirstSession), {
    fail_streak: 0, // the win cleared it; the quit left it alone
    attempts_on_level: 1, // L2: one finished attempt (the quit)
    fast_solve_streak: 0, // the fast win on L1 counted, the quit broke the run
    hint_uses_level: 0, // reset when L2 started
    hint_uses_session: 1,
    median_move_ms: 2000, // from the last finished attempt
    restarts_recent: 1, // the restart at minute 3 is inside 10 minutes of minute 7
    session_gap_hours: null, // first session ever, no gap given
    sessions_today: 1,
    skill_rating: rating,
    level_rating: 1600,
    rating_gap: 1600 - rating,
    quit_rate_recent: 0.25, // fail, restart, win, quit
  });

  const nextSession = applyEvent(afterFirstSession, ev('session_start', T + 20 * MIN, { localDay: '2026-10-16' }));
  const v = inputs(nextSession);
  assert.equal(v.sessions_today, 2);
  assert.equal(v.session_gap_hours, 13 / 60); // from the last event (minute 7) to minute 20
  assert.equal(v.restarts_recent, 0); // 17 minutes old now
  assert.equal(v.hint_uses_session, 0);
  assert.equal(v.attempts_on_level, 1); // level counters survive a new session
});

test('fail_streak counts fails this session; a win or a new session clears it, quit and restart do not', () => {
  const fails = [1, 2, 3].map((i) => ev('level_end', T + i * MIN, { levelId: 'A', result: 'fail' }));
  let s = play([ev('session_start', T), ...fails]);
  assert.equal(inputs(s).fail_streak, 3);
  s = play([ev('level_end', T + 4 * MIN, { levelId: 'A', result: 'quit' }), ev('restart', T + 5 * MIN)], s);
  assert.equal(inputs(s).fail_streak, 3);
  assert.equal(inputs(play([ev('level_end', T + 6 * MIN, { levelId: 'A', result: 'win' })], s)).fail_streak, 0);
  assert.equal(inputs(applyEvent(s, ev('session_start', T + 60 * MIN))).fail_streak, 0);
});

test('fast_solve_streak counts wins under the level median and breaks on anything else', () => {
  const win = (i, durationMs, medianLevelMs = 60000) =>
    ev('level_end', T + i * MIN, { levelId: `L${i}`, result: 'win', durationMs, medianLevelMs });
  let s = play([ev('session_start', T), win(1, 30000), win(2, 59999), win(3, 10000)]);
  assert.equal(inputs(s).fast_solve_streak, 3);
  assert.equal(inputs(applyEvent(s, win(4, 60000))).fast_solve_streak, 0); // not under the median
  assert.equal(inputs(applyEvent(s, ev('level_end', T + 5 * MIN, { levelId: 'L5', result: 'win', durationMs: 1000 }))).fast_solve_streak, 0); // no median: no evidence
  assert.equal(inputs(applyEvent(s, ev('restart', T + 6 * MIN))).fast_solve_streak, 0);
  s = applyEvent(s, ev('session_start', T + 90 * MIN));
  assert.equal(inputs(s).fast_solve_streak, 3, 'not session scoped');
});

test('attempts and hints reset on a new level and on a replay after a win', () => {
  let s = play([
    ev('session_start', T),
    ev('level_start', T + 1, { levelId: 7 }),
    ev('hint_used', T + 2),
    ev('level_end', T + 3, { levelId: 7, result: 'fail' }),
    ev('level_start', T + 4, { levelId: 7 }),
    ev('level_end', T + 5, { levelId: 7, result: 'fail' }),
    ev('level_start', T + 6, { levelId: 7 }),
  ]);
  assert.equal(inputs(s).attempts_on_level, 2, 'finished attempts before this one');
  assert.equal(inputs(s).hint_uses_level, 1);
  s = play([ev('level_end', T + 7, { levelId: 7, result: 'win' })], s);
  assert.equal(inputs(s).attempts_on_level, 3, 'still readable at level end');
  const replay = applyEvent(s, ev('level_start', T + 8, { levelId: 7 }));
  assert.equal(inputs(replay).attempts_on_level, 0);
  assert.equal(inputs(replay).hint_uses_level, 0);
  assert.equal(inputs(replay).hint_uses_session, 1);
});

test('restarts_recent uses event time only and the clock never runs backwards', () => {
  let s = play([
    ev('session_start', T),
    ev('restart', T + 1 * MIN),
    ev('restart', T + 2 * MIN),
    ev('restart', T + 9 * MIN),
  ]);
  assert.equal(inputs(s).restarts_recent, 3);
  s = applyEvent(s, ev('hint_used', T + 11.5 * MIN));
  assert.equal(inputs(s).restarts_recent, 2, 'the minute 1 restart left the window');
  // A device clock set back by an hour does not resurrect old restarts or shrink time.
  s = applyEvent(s, ev('restart', T - 60 * MIN));
  assert.equal(s.lastAt, T + 11.5 * MIN);
  assert.equal(inputs(s).restarts_recent, 3);
});

test('sessions_today follows the local day the game passes, with a UTC day fallback', () => {
  let s = play([
    ev('session_start', T, { localDay: '2026-10-16', gapHours: 30 }),
    ev('session_start', T + 60 * MIN, { localDay: '2026-10-16' }),
  ]);
  assert.equal(inputs(s).sessions_today, 2);
  assert.equal(play([ev('session_start', T + 120 * MIN, { localDay: '2026-10-17' })], s).sessionsToday, 1);
  const first = applyEvent(createPlayerState(), ev('session_start', T, { gapHours: 30 }));
  assert.equal(inputs(first).session_gap_hours, 30, 'a gap the game passes wins');
  const dayMs = 24 * 60 * MIN;
  const midnight = Math.ceil(T / dayMs) * dayMs;
  s = play([ev('session_start', midnight - MIN), ev('session_start', midnight - 1)]);
  assert.equal(inputs(s).sessions_today, 2);
  assert.equal(inputs(applyEvent(s, ev('session_start', midnight))).sessions_today, 1);
});

test('quit_rate_recent is the share of quits in the last 10 finished attempts', () => {
  const ends = Array.from({ length: 12 }, (_, i) =>
    ev('level_end', T + i, { levelId: 'Q', result: i < 4 ? 'quit' : 'fail' }),
  );
  const s = play([ev('session_start', T), ...ends]);
  // Attempts 0 to 3 were quits; the window holds attempts 2 to 11: two quits.
  assert.equal(inputs(s).quit_rate_recent, 0.2);
  assert.equal(s.recentOutcomes.length, 10);
});

test('ratings move only on wins and fails of a rated level', () => {
  let s = play([ev('session_start', T), ev('level_start', T + 1, { levelId: 'R', levelRating: 1500 })]);
  assert.equal(inputs(applyEvent(s, ev('level_end', T + 2, { levelId: 'R', result: 'quit' }))).skill_rating, 1500);
  assert.equal(inputs(applyEvent(s, ev('level_end', T + 2, { levelId: 'R', result: 'win' }))).skill_rating, 1516);
  s = play([ev('level_start', T + 3, { levelId: 'unrated' }), ev('level_end', T + 4, { levelId: 'unrated', result: 'fail' })], s);
  assert.equal(inputs(s).skill_rating, 1500);
  assert.equal(inputs(s).rating_gap, null);
  const custom = play([ev('level_start', T, { levelId: 'R', levelRating: 1500 }), ev('level_end', T, { levelId: 'R', result: 'win' })], createPlayerState({ initialRating: 1500, k: 10 }));
  assert.equal(custom.skillRating, 1505);
});

test('applyEvent is pure and its state survives a JSON round trip', () => {
  const s0 = play([ev('session_start', T), ev('level_start', T + 1, { levelId: 'P', levelRating: 1400 }), ev('restart', T + 2)]);
  const snapshot = structuredClone(s0);
  const s1 = applyEvent(s0, ev('level_end', T + 3, { levelId: 'P', result: 'fail', medianMoveMs: 700 }));
  assert.deepEqual(s0, snapshot, 'input state untouched');
  assert.notEqual(s1, s0);
  const revived = JSON.parse(JSON.stringify(s1));
  assert.deepEqual(inputs(revived), inputs(s1));
  assert.deepEqual(applyEvent(revived, ev('hint_used', T + 4)), applyEvent(s1, ev('hint_used', T + 4)));
});

test('malformed events are refused loudly', () => {
  const s = createPlayerState();
  assert.throws(() => applyEvent(s, ev('level_ended', T)), /unknown event type/);
  assert.throws(() => applyEvent(s, { type: 'hint_used' }), /at must be/);
  assert.throws(() => applyEvent(s, ev('level_start', T)), /levelId/);
  assert.throws(() => applyEvent(s, ev('level_end', T, { levelId: 'x', result: 'won' })), /result/);
  assert.throws(() => applyEvent(s, ev('level_end', T, { levelId: 'x', result: 'win', durationMs: -5 })), /durationMs/);
  assert.throws(() => applyEvent(s, ev('session_start', T, { gapHours: Number.NaN })), /gapHours/);
  assert.throws(() => applyEvent(s, ev('level_start', T, { levelId: 'x', levelRating: '1500' })), /levelRating/);
  assert.throws(() => applyEvent(/** @type {any} */ ({}), ev('hint_used', T)), /createPlayerState/);
  assert.throws(() => inputs(/** @type {any} */ (null)), TypeError);
});
