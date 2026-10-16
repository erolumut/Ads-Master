// Player state estimator (pxe 0.1): folds play events into the inputs listed
// in policy-format.md section 3, and nothing else.
//
// applyEvent is a pure reducer: it never mutates the state it is given, it
// never reads the clock (time is the event's `at`, epoch milliseconds), and its
// output is plain JSON, so the state can be saved and restored as is.

import { DEFAULT_K, DEFAULT_LEVEL_K, DEFAULT_RATING, update } from './rating.js';

export const STATE_VERSION = 1;

/** The only names a policy may read, in the order of policy-format.md section 3. */
export const INPUT_NAMES = Object.freeze([
  'fail_streak',
  'attempts_on_level',
  'fast_solve_streak',
  'hint_uses_level',
  'hint_uses_session',
  'median_move_ms',
  'restarts_recent',
  'session_gap_hours',
  'sessions_today',
  'skill_rating',
  'level_rating',
  'rating_gap',
  'quit_rate_recent',
]);

export const EVENT_TYPES = Object.freeze(['session_start', 'level_start', 'level_end', 'hint_used', 'restart']);
export const LEVEL_RESULTS = Object.freeze(['win', 'fail', 'quit']);
export const RESTART_WINDOW_MS = 10 * 60 * 1000;
export const RECENT_ATTEMPTS = 10;
const HOUR_MS = 60 * 60 * 1000;
const DAY_MS = 24 * HOUR_MS;

/**
 * @typedef {'win' | 'fail' | 'quit' | 'restart'} AttemptOutcome
 *
 * @typedef {object} PlayerState
 * @property {number} stateVersion
 * @property {{ k: number, levelK: number }} config
 * @property {number | null} lastAt latest event time seen (ms); never moves backwards
 * @property {number} sessionSeq sessions started since the state was created
 * @property {string | null} day day key of the latest session_start
 * @property {number} sessionsToday
 * @property {number | null} sessionGapHours
 * @property {number} failStreak
 * @property {number} fastSolveStreak
 * @property {string | number | null} levelId
 * @property {boolean} levelCleared true after a win, until another level_start
 * @property {number | null} levelRating
 * @property {number} attemptsOnLevel
 * @property {number} hintUsesLevel
 * @property {number} hintUsesSession
 * @property {number | null} medianMoveMs
 * @property {number[]} restartTimes restart times inside the 10 minute window
 * @property {AttemptOutcome[]} recentOutcomes the last 10 finished attempts, oldest first
 * @property {number} skillRating
 *
 * @typedef {{ [name: string]: number | null }} Inputs
 *
 * @typedef {object} PxeEvent
 * @property {string} type one of EVENT_TYPES
 * @property {number} at epoch milliseconds from the game
 * @property {number} [gapHours] session_start: hours since the previous session ended
 * @property {string | number} [localDay] session_start: the player's local calendar day, such as '2026-10-16'
 * @property {string | number} [levelId] level_start, level_end
 * @property {number | null} [levelRating] level_start: the level's rating from the calibration table
 * @property {string} [result] level_end: 'win', 'fail' or 'quit'
 * @property {number} [durationMs] level_end
 * @property {number} [medianMoveMs] level_end or restart: median time between moves in that attempt
 * @property {number} [medianLevelMs] level_end: the level's median solve time from the calibration table
 */

/** @param {unknown} x @returns {x is number} */
const isFiniteNumber = (x) => typeof x === 'number' && Number.isFinite(x);
/** @param {unknown} x @returns {x is string | number} */
const isId = (x) => (typeof x === 'string' && x.length > 0) || (typeof x === 'number' && Number.isFinite(x));

/**
 * A fresh state for a player who has not played yet.
 * @param {{ initialRating?: number, k?: number, levelK?: number }} [options]
 * @returns {PlayerState}
 */
export function createPlayerState(options = {}) {
  const initialRating = options.initialRating ?? DEFAULT_RATING;
  const k = options.k ?? DEFAULT_K;
  const levelK = options.levelK ?? DEFAULT_LEVEL_K;
  if (!isFiniteNumber(initialRating)) throw new TypeError('initialRating must be a finite number');
  if (!isFiniteNumber(k) || k < 0 || !isFiniteNumber(levelK) || levelK < 0) {
    throw new RangeError('k and levelK must be finite and not negative');
  }
  return {
    stateVersion: STATE_VERSION,
    config: { k, levelK },
    lastAt: null,
    sessionSeq: 0,
    day: null,
    sessionsToday: 0,
    sessionGapHours: null,
    failStreak: 0,
    fastSolveStreak: 0,
    levelId: null,
    levelCleared: false,
    levelRating: null,
    attemptsOnLevel: 0,
    hintUsesLevel: 0,
    hintUsesSession: 0,
    medianMoveMs: null,
    restartTimes: [],
    recentOutcomes: [],
    skillRating: initialRating,
  };
}

/**
 * True for a value made by createPlayerState or applyEvent.
 * @param {unknown} x
 * @returns {x is PlayerState}
 */
export function isPlayerState(x) {
  return typeof x === 'object' && x !== null && /** @type {{ stateVersion?: unknown }} */ (x).stateVersion === STATE_VERSION;
}

/**
 * Folds one event into the state and returns a new state. Throws a TypeError on
 * a malformed event: a typo in an event name must not silently stop adaptation.
 * @param {PlayerState} state
 * @param {PxeEvent} event
 * @returns {PlayerState}
 */
export function applyEvent(state, event) {
  if (!isPlayerState(state)) throw new TypeError('applyEvent needs a state from createPlayerState');
  checkEvent(event);

  // A device clock can jump backwards; time inside the state never does.
  const at = state.lastAt === null ? event.at : Math.max(event.at, state.lastAt);
  /** @type {PlayerState} */
  const s = {
    ...state,
    config: { ...state.config },
    lastAt: at,
    restartTimes: state.restartTimes.filter((t) => t >= at - RESTART_WINDOW_MS),
    recentOutcomes: state.recentOutcomes.slice(),
  };

  switch (event.type) {
    case 'session_start': {
      s.sessionGapHours = isFiniteNumber(event.gapHours)
        ? event.gapHours
        : state.lastAt === null
          ? null // first session ever: the gap is unknown, not zero
          : (at - state.lastAt) / HOUR_MS; // the previous session's last event stands in for its end
      const day = event.localDay !== undefined ? String(event.localDay) : `utc:${Math.floor(at / DAY_MS)}`;
      s.sessionsToday = day === state.day ? state.sessionsToday + 1 : 1;
      s.day = day;
      s.sessionSeq = state.sessionSeq + 1;
      s.failStreak = 0; // fail_streak counts this session only
      s.hintUsesSession = 0;
      break;
    }
    case 'level_start': {
      enterLevel(s, /** @type {string | number} */ (event.levelId));
      // The calibration table may refresh a level's rating between attempts.
      if (event.levelRating !== undefined) s.levelRating = isFiniteNumber(event.levelRating) ? event.levelRating : null;
      break;
    }
    case 'level_end': {
      enterLevel(s, /** @type {string | number} */ (event.levelId));
      endAttempt(s, /** @type {AttemptOutcome} */ (event.result), event.medianMoveMs);
      if (event.result === 'win') {
        s.failStreak = 0;
        const fast =
          isFiniteNumber(event.medianLevelMs) &&
          event.medianLevelMs > 0 &&
          isFiniteNumber(event.durationMs) &&
          event.durationMs < event.medianLevelMs;
        s.fastSolveStreak = fast ? state.fastSolveStreak + 1 : 0;
        s.levelCleared = true;
        rate(s, true);
      } else if (event.result === 'fail') {
        s.failStreak = s.failStreak + 1;
        s.fastSolveStreak = 0;
        rate(s, false);
      } else {
        // A quit is not a win, so it breaks a fast solve run. It is not a fail
        // either, so fail_streak keeps its count, and it is not skill evidence,
        // so the rating stays put. quit_rate_recent carries the signal.
        s.fastSolveStreak = 0;
      }
      break;
    }
    case 'hint_used': {
      s.hintUsesLevel = state.hintUsesLevel + 1;
      s.hintUsesSession = state.hintUsesSession + 1;
      break;
    }
    case 'restart': {
      // Send `restart` instead of a level_end when the player restarts mid
      // level, then a level_start for the next attempt. The restarted attempt
      // counts as an attempt on the level; it neither adds to nor clears
      // fail_streak, and like a quit it ends a fast solve run.
      endAttempt(s, 'restart', event.medianMoveMs);
      s.restartTimes.push(at);
      s.fastSolveStreak = 0;
      break;
    }
    default:
      break; // unreachable: checkEvent refuses unknown types
  }
  return s;
}

/**
 * The policy inputs, as a plain object holding exactly INPUT_NAMES. A value
 * that is not known yet is null, and a condition on a null input never matches.
 * @param {PlayerState} state
 * @returns {Inputs}
 */
export function inputs(state) {
  if (!isPlayerState(state)) throw new TypeError('inputs() needs a state from createPlayerState');
  const now = state.lastAt;
  const outcomes = state.recentOutcomes;
  return {
    fail_streak: state.failStreak,
    attempts_on_level: state.attemptsOnLevel,
    fast_solve_streak: state.fastSolveStreak,
    hint_uses_level: state.hintUsesLevel,
    hint_uses_session: state.hintUsesSession,
    median_move_ms: state.medianMoveMs,
    restarts_recent: now === null ? 0 : state.restartTimes.filter((t) => t >= now - RESTART_WINDOW_MS).length,
    session_gap_hours: state.sessionGapHours,
    sessions_today: state.sessionsToday,
    skill_rating: state.skillRating,
    level_rating: state.levelRating,
    rating_gap: state.levelRating === null ? null : state.levelRating - state.skillRating,
    quit_rate_recent: outcomes.length === 0 ? null : outcomes.filter((o) => o === 'quit').length / outcomes.length,
  };
}

/**
 * Starts tracking a level. Same level, not yet cleared: keep its counters.
 * A different level, or a replay after a win: start the counters from zero.
 * @param {PlayerState} s mutable working copy
 * @param {string | number} levelId
 */
function enterLevel(s, levelId) {
  if (levelId === s.levelId && !s.levelCleared) return;
  if (levelId !== s.levelId) s.levelRating = null;
  s.levelId = levelId;
  s.levelCleared = false;
  s.attemptsOnLevel = 0;
  s.hintUsesLevel = 0;
}

/**
 * Records one finished attempt. attempts_on_level counts finished attempts, so
 * at a level_start it reads "tries before this one".
 * @param {PlayerState} s
 * @param {AttemptOutcome} outcome
 * @param {number | undefined} medianMoveMs
 */
function endAttempt(s, outcome, medianMoveMs) {
  s.attemptsOnLevel += 1;
  if (isFiniteNumber(medianMoveMs) && medianMoveMs >= 0) s.medianMoveMs = medianMoveMs;
  s.recentOutcomes.push(outcome);
  if (s.recentOutcomes.length > RECENT_ATTEMPTS) s.recentOutcomes.shift();
}

/**
 * Moves the player's rating after a win or a fail on a rated level. The level
 * side of the update is not kept: level ratings come from offline calibration.
 * @param {PlayerState} s
 * @param {boolean} won
 */
function rate(s, won) {
  if (s.levelRating === null) return;
  s.skillRating = update(s.skillRating, s.levelRating, won, s.config).player;
}

/**
 * @param {unknown} event
 * @returns {asserts event is PxeEvent}
 */
function checkEvent(event) {
  if (typeof event !== 'object' || event === null) throw new TypeError('event must be an object');
  const e = /** @type {Record<string, unknown>} */ (event);
  const type = e.type;
  if (typeof type !== 'string' || !EVENT_TYPES.includes(type)) {
    throw new TypeError(`unknown event type ${JSON.stringify(type)}`);
  }
  if (!isFiniteNumber(e.at) || e.at < 0) throw new TypeError(`${type}: at must be epoch milliseconds`);
  /** @param {string} key */
  const optionalNonNegative = (key) => {
    if (e[key] !== undefined && (!isFiniteNumber(e[key]) || /** @type {number} */ (e[key]) < 0)) {
      throw new TypeError(`${type}: ${key} must be a finite number, zero or more`);
    }
  };
  if (type === 'session_start') {
    optionalNonNegative('gapHours');
    if (e.localDay !== undefined && !isId(e.localDay)) throw new TypeError('session_start: localDay must be a non empty string or a number');
  }
  if (type === 'level_start' || type === 'level_end') {
    if (!isId(e.levelId)) throw new TypeError(`${type}: levelId must be a non empty string or a number`);
  }
  if (type === 'level_start' && e.levelRating !== undefined && e.levelRating !== null && !isFiniteNumber(e.levelRating)) {
    throw new TypeError('level_start: levelRating must be a finite number or null');
  }
  if (type === 'level_end') {
    if (typeof e.result !== 'string' || !LEVEL_RESULTS.includes(e.result)) {
      throw new TypeError(`level_end: result must be one of ${LEVEL_RESULTS.join(', ')}`);
    }
    optionalNonNegative('durationMs');
    optionalNonNegative('medianMoveMs');
    optionalNonNegative('medianLevelMs');
  }
  if (type === 'restart') optionalNonNegative('medianMoveMs');
}
