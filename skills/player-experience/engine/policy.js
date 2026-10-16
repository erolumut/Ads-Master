// Policy validation and evaluation for the player experience engine (pxe 0.1).
//
// validatePolicy() refuses obviously broken files at runtime by applying the
// FAIL checks of policy-format.md section 5. It is a seat belt, not the
// release gate: scripts/pxe_policy_check.py checks a policy before it ships.
// createEngine() honors the runtime guarantees of section 6.

import { fnv1a32 } from './rng.js';
import { INPUT_NAMES, inputs as readStateInputs, isPlayerState } from './state.js';

export const ENGINE_VERSION = '0.1.0';
export const SUPPORTED_PXE_VERSIONS = Object.freeze(['0.1']);

/** Section 3: the only inputs a rule may read. */
export const ALLOWED_INPUTS = INPUT_NAMES;
export const ALLOWED_OPS = Object.freeze(['>=', '>', '<=', '<', '==', '!=']);
/** Section 4: the only actions a rule may return. */
export const ALLOWED_ACTIONS = Object.freeze(['difficulty_offset', 'offer_hint', 'offer_break', 'show_next_goal', 'suggest_mode']);
/** Section 4: refused even if a later version adds them to the allowed list. */
export const FORBIDDEN_ACTIONS = Object.freeze(['force_loss', 'death', 'kill', 'rig', 'score_bonus', 'modify_score', 'bias_pieces', 'harvest']);
/** Section 4: an input or action whose name contains any of these, in any case or separator style, is refused. */
export const FORBIDDEN_NAME_FRAGMENTS = Object.freeze([
  'spend', 'spent', 'purchase', 'payer', 'paying', 'revenue', 'ltv', 'arpu', 'arppu', 'whale', 'iap',
  'ad_value', 'advalue', 'ecpm', 'ad_ready', 'rewarded_ready', 'ad_available', 'ad_fill', 'monetiz', 'price',
  'device_model', 'device_tier', 'device_price', 'country', 'region', 'geo', 'income', 'age', 'gender',
  'health', 'mood', 'vibration', 'battery',
]);

export const SETTINGS = Object.freeze(['auto', 'easy', 'normal', 'hard']);
/** Fixed offsets for the player's own difficulty choice, clamped to the policy range. */
export const SETTING_OFFSETS = Object.freeze({ easy: -1, normal: 0, hard: 1 });
const REQUIRED_KEYS = Object.freeze([
  'pxeVersion', 'policyRevision', 'product', 'audience', 'modes', 'difficulty', 'player',
  'rules', 'returnReasons', 'scores', 'experiment',
]);
const MAX_STEPS_EITHER_WAY = 2;
const ADULT_AGE = 18;
const STRICT_FORBIDDEN_SOURCES = Object.freeze(['streak', 'loss']);
const MIN_READ_DAYS = 28;
const HHMM = /^([01]\d|2[0-3]):[0-5]\d$/;
// Per session counters are kept for this many recent sessions.
const SESSION_MEMORY = 32;

/**
 * @typedef {import('./state.js').PlayerState} PlayerState
 * @typedef {import('./state.js').Inputs} Inputs
 *
 * @typedef {{ input: string, op: string, value: number }} Condition
 * @typedef {{ action: string, value?: number, mode?: string }} RuleAction
 * @typedef {{ id: string, modes: string[], when: Condition[], then: RuleAction, reason: string, explainKey: string, maxPerSession?: number }} Rule
 * @typedef {{ id: string, shared: boolean }} Mode
 * @typedef {object} Policy
 * @property {string} pxeVersion
 * @property {number} policyRevision
 * @property {string} product
 * @property {{ minimumAge: number, minorsTier: string }} audience
 * @property {Mode[]} modes
 * @property {{ steps: number[], default: number, minOffset: number, maxOffset: number }} difficulty
 * @property {{ settings: string[], explain: boolean, log: boolean, reset: boolean }} player
 * @property {Rule[]} rules
 * @property {{ id: string, source: string, maxPerDay: number, quietHours: string[] }[]} returnReasons
 * @property {{ modifyAfterFact: boolean, assistedRunsLabeled?: boolean, assistedRunsOnSharedBoards: boolean }} scores
 * @property {{ holdoutPercent: number, readAfterDays?: number, primary: string[], guardrails?: string[] }} experiment
 *
 * @typedef {{ ok: boolean, errors: string[], warnings: string[] }} Validation
 *
 * @typedef {'action' | 'no_match' | 'holdout' | 'shared_mode' | 'unknown_mode'} Outcome
 * @typedef {object} Decision
 * @property {string | null} action
 * @property {string | null} ruleId
 * @property {string | null} reason
 * @property {string | null} explainKey
 * @property {number | null} value the rule's declared offset step, for difficulty_offset
 * @property {string | null} targetMode for suggest_mode
 * @property {number} offsetNow the difficulty offset to build the next level with (always 0 in a shared mode)
 * @property {boolean} holdout true when this install is in the persistent holdout
 * @property {Outcome} outcome why the decision is what it is
 *
 * @typedef {object} LogEntry
 * @property {number | null} at time of the latest event in the state
 * @property {string} sessionId
 * @property {string} mode
 * @property {string} ruleId
 * @property {string} reason
 * @property {string} explainKey
 * @property {string} action
 * @property {number | null} value
 * @property {string | null} targetMode
 * @property {number} offsetNow
 * @property {number} policyRevision
 * @property {string} engineVersion
 *
 * @typedef {{ rules: Record<string, number>, easings: number }} SessionCounters
 * @typedef {{ engineVersion: string, policyRevision: number, offset: number, sessions: { id: string, rules: Record<string, number>, easings: number }[], log: LogEntry[] }} SavedEngine
 */

/** @param {unknown} x @returns {x is number} */
const isFiniteNumber = (x) => typeof x === 'number' && Number.isFinite(x);
/** @param {unknown} x @returns {x is string} */
const isNonEmptyString = (x) => typeof x === 'string' && x.trim().length > 0;
/** @param {unknown} x @returns {x is Record<string, unknown>} */
const isObject = (x) => typeof x === 'object' && x !== null && !Array.isArray(x);
/** @param {string} s */
const normalizeName = (s) => s.toLowerCase().replace(/[^a-z0-9]/g, '');
const NORMALIZED_FRAGMENTS = FORBIDDEN_NAME_FRAGMENTS.map((f) => ({ fragment: f, key: normalizeName(f) }));
const NORMALIZED_FORBIDDEN_ACTIONS = new Set(FORBIDDEN_ACTIONS.map(normalizeName));

/**
 * The forbidden fragment a name contains, or null. "AdValue", "ad-value" and
 * "ad_value" all contain "ad_value".
 * @param {string} name
 * @returns {string | null}
 */
export function forbiddenFragment(name) {
  const key = normalizeName(name);
  const hit = NORMALIZED_FRAGMENTS.find((f) => key.includes(f.key));
  return hit ? hit.fragment : null;
}

/**
 * Holdout bucket in [0, 100): FNV-1a 32 of the UTF-8 string
 * `${installId}:${policyRevision}`, modulo 100. Stable for one install and one
 * policy revision; a new revision draws a new holdout.
 * @param {string} installId
 * @param {number} policyRevision
 * @returns {number}
 */
export function holdoutBucket(installId, policyRevision) {
  return fnv1a32(`${installId}:${policyRevision}`) % 100;
}

/**
 * Structural checks mirroring policy-format.md section 5. Never throws.
 * @param {unknown} policy
 * @returns {Validation}
 */
export function validatePolicy(policy) {
  /** @type {string[]} */
  const errors = [];
  /** @type {string[]} */
  const warnings = [];
  const done = () => ({ ok: errors.length === 0, errors, warnings });

  if (!isObject(policy)) {
    errors.push('policy must be a JSON object');
    return done();
  }
  if (typeof policy.pxeVersion !== 'string' || !SUPPORTED_PXE_VERSIONS.includes(policy.pxeVersion)) {
    // Field meanings may differ in an unknown version, so nothing else is read.
    errors.push(`pxeVersion ${JSON.stringify(policy.pxeVersion)} is not supported (supported: ${SUPPORTED_PXE_VERSIONS.join(', ')})`);
    return done();
  }
  for (const key of REQUIRED_KEYS) {
    if (!(key in policy)) errors.push(`missing ${key}`);
  }
  if (!Number.isInteger(policy.policyRevision) || /** @type {number} */ (policy.policyRevision) < 0) {
    errors.push('policyRevision must be an integer, zero or more');
  }
  if (!isNonEmptyString(policy.product)) errors.push('product must be a non empty string');

  checkAudience(policy.audience, errors);
  const modes = checkModes(policy.modes, errors);
  const range = checkDifficulty(policy.difficulty, errors);
  checkPlayer(policy.player, errors);
  checkRules(policy.rules, modes, range, errors, warnings);
  checkReturnReasons(policy.returnReasons, policy.audience, errors);
  checkScores(policy.scores, errors);
  checkExperiment(policy.experiment, errors, warnings);
  return done();
}

/** @param {unknown} audience @param {string[]} errors */
function checkAudience(audience, errors) {
  if (!isObject(audience)) {
    errors.push('audience must be an object');
    return;
  }
  if (!isFiniteNumber(audience.minimumAge) || audience.minimumAge < 0) {
    errors.push('audience.minimumAge must be a number, zero or more');
  } else if (audience.minimumAge < ADULT_AGE && audience.minorsTier !== 'strict') {
    errors.push(`audience.minimumAge is under ${ADULT_AGE}, so audience.minorsTier must be "strict"`);
  }
}

/**
 * @param {unknown} modes
 * @param {string[]} errors
 * @returns {Map<string, boolean>} mode id to shared
 */
function checkModes(modes, errors) {
  /** @type {Map<string, boolean>} */
  const byId = new Map();
  if (!Array.isArray(modes) || modes.length === 0) {
    errors.push('modes must be a non empty array');
    return byId;
  }
  modes.forEach((mode, i) => {
    if (!isObject(mode) || !isNonEmptyString(mode.id)) {
      errors.push(`modes[${i}] needs a non empty id`);
      return;
    }
    if (byId.has(mode.id)) errors.push(`mode "${mode.id}" is declared twice`);
    if (typeof mode.shared !== 'boolean') errors.push(`mode "${mode.id}": shared must be true or false`);
    // A mode with no clear answer is treated as shared: it never adapts.
    byId.set(mode.id, mode.shared !== false);
  });
  return byId;
}

/**
 * @param {unknown} difficulty
 * @param {string[]} errors
 * @returns {{ steps: number[], min: number, max: number } | null}
 */
function checkDifficulty(difficulty, errors) {
  if (!isObject(difficulty)) {
    errors.push('difficulty must be an object');
    return null;
  }
  const { steps, minOffset, maxOffset } = difficulty;
  const def = difficulty.default;
  let ok = true;
  if (!Array.isArray(steps) || steps.length === 0 || !steps.every(Number.isInteger)) {
    errors.push('difficulty.steps must be a non empty array of integers');
    ok = false;
  }
  for (const [name, v] of /** @type {[string, unknown][]} */ ([['minOffset', minOffset], ['maxOffset', maxOffset], ['default', def]])) {
    if (!Number.isInteger(v)) {
      errors.push(`difficulty.${name} must be an integer`);
      ok = false;
    }
  }
  if (!ok) return null;
  const min = /** @type {number} */ (minOffset);
  const max = /** @type {number} */ (maxOffset);
  const stepList = /** @type {number[]} */ (steps);
  if (min > 0 || max < 0 || min > max) errors.push('difficulty needs minOffset <= 0 <= maxOffset');
  if (min < -MAX_STEPS_EITHER_WAY || max > MAX_STEPS_EITHER_WAY) {
    errors.push(`difficulty offsets are wider than ${MAX_STEPS_EITHER_WAY} steps either way`);
  }
  for (const [name, v] of /** @type {[string, number][]} */ ([['minOffset', min], ['maxOffset', max], ['default', def]])) {
    if (!stepList.includes(v)) errors.push(`difficulty.${name} ${v} is not one of difficulty.steps`);
  }
  if (/** @type {number} */ (def) < min || /** @type {number} */ (def) > max) {
    errors.push('difficulty.default must lie between minOffset and maxOffset');
  }
  return { steps: stepList, min, max };
}

/** @param {unknown} player @param {string[]} errors */
function checkPlayer(player, errors) {
  if (!isObject(player)) {
    errors.push('player must be an object');
    return;
  }
  const settings = Array.isArray(player.settings) ? player.settings : [];
  const missing = SETTINGS.filter((s) => !settings.includes(s));
  if (missing.length > 0) errors.push(`player.settings is missing ${missing.join(', ')}`);
  for (const flag of ['explain', 'log', 'reset']) {
    if (player[flag] !== true) errors.push(`player.${flag} must be true`);
  }
}

/**
 * Checks an input or action name against section 4.
 * @param {string} kind 'input' or 'action'
 * @param {unknown} name
 * @param {readonly string[]} allowed
 * @param {string} where
 * @param {string[]} errors
 * @returns {boolean} true when the name is allowed
 */
function checkName(kind, name, allowed, where, errors) {
  if (!isNonEmptyString(name)) {
    errors.push(`${where}: ${kind} must be a non empty string`);
    return false;
  }
  const fragment = forbiddenFragment(name);
  if (fragment !== null) {
    errors.push(`${where}: ${kind} "${name}" is forbidden (contains "${fragment}")`);
    return false;
  }
  if (kind === 'action' && NORMALIZED_FORBIDDEN_ACTIONS.has(normalizeName(name))) {
    errors.push(`${where}: action "${name}" is forbidden`);
    return false;
  }
  if (!allowed.includes(name)) {
    errors.push(`${where}: ${kind} "${name}" is not an allowed ${kind}`);
    return false;
  }
  return true;
}

/**
 * @param {unknown} rules
 * @param {Map<string, boolean>} modes
 * @param {{ steps: number[], min: number, max: number } | null} range
 * @param {string[]} errors
 * @param {string[]} warnings
 */
function checkRules(rules, modes, range, errors, warnings) {
  if (!Array.isArray(rules)) {
    errors.push('rules must be an array');
    return;
  }
  const ids = new Set();
  let uncappedEasings = 0;
  let raises = 0;
  rules.forEach((rule, i) => {
    if (!isObject(rule)) {
      errors.push(`rules[${i}] must be an object`);
      return;
    }
    const where = isNonEmptyString(rule.id) ? `rule "${rule.id}"` : `rules[${i}]`;
    if (!isNonEmptyString(rule.id)) errors.push(`${where}: id must be a non empty string`);
    else if (ids.has(rule.id)) errors.push(`${where}: id is used twice`);
    else ids.add(rule.id);

    if (!Array.isArray(rule.modes) || rule.modes.length === 0) {
      errors.push(`${where}: modes must name at least one mode`);
    } else {
      for (const m of rule.modes) {
        if (typeof m !== 'string' || !modes.has(m)) errors.push(`${where}: mode ${JSON.stringify(m)} is not declared`);
        else if (modes.get(m)) errors.push(`${where}: mode "${m}" is shared, and shared modes never adapt`);
      }
    }

    if (!Array.isArray(rule.when)) {
      errors.push(`${where}: when must be an array of conditions`);
    } else {
      rule.when.forEach((cond, j) => {
        const at = `${where} when[${j}]`;
        if (!isObject(cond)) {
          errors.push(`${at}: must be an object`);
          return;
        }
        checkName('input', cond.input, ALLOWED_INPUTS, at, errors);
        if (typeof cond.op !== 'string' || !ALLOWED_OPS.includes(cond.op)) {
          errors.push(`${at}: op ${JSON.stringify(cond.op)} is not one of ${ALLOWED_OPS.join(' ')}`);
        }
        if (!isFiniteNumber(cond.value)) errors.push(`${at}: value must be a number`);
      });
    }

    const then = rule.then;
    if (!isObject(then)) {
      errors.push(`${where}: then must be an object with an action`);
    } else if (checkName('action', then.action, ALLOWED_ACTIONS, where, errors)) {
      if (then.action === 'difficulty_offset') {
        if (!Number.isInteger(then.value)) {
          errors.push(`${where}: difficulty_offset needs an integer value`);
        } else if (range) {
          const v = /** @type {number} */ (then.value);
          if (v < range.min || v > range.max) {
            errors.push(`${where}: difficulty_offset value ${v} is outside minOffset ${range.min} to maxOffset ${range.max}`);
          } else if (!range.steps.includes(v)) {
            errors.push(`${where}: difficulty_offset value ${v} is not one of difficulty.steps`);
          }
          if (v < 0 && rule.maxPerSession !== 1) uncappedEasings += 1;
          if (v > 0) raises += 1;
        }
      }
      if (then.action === 'suggest_mode') {
        if (typeof then.mode !== 'string' || !modes.has(then.mode)) {
          errors.push(`${where}: suggest_mode needs a declared mode`);
        } else if (modes.get(then.mode)) {
          errors.push(`${where}: suggest_mode may not point at shared mode "${then.mode}"`);
        }
      }
    }

    if (!isNonEmptyString(rule.reason)) errors.push(`${where}: reason is missing`);
    if (!isNonEmptyString(rule.explainKey)) errors.push(`${where}: explainKey is missing`);
    if (rule.maxPerSession !== undefined && (!Number.isInteger(rule.maxPerSession) || /** @type {number} */ (rule.maxPerSession) < 1)) {
      errors.push(`${where}: maxPerSession must be an integer, 1 or more`);
    }
  });
  if (uncappedEasings > 1) {
    errors.push(`${uncappedEasings} easing rules (negative difficulty_offset) lack maxPerSession 1`);
  }
  if (rules.length > 0 && raises === 0) {
    warnings.push('no raising rule: an engine that only eases can bore skilled players');
  }
}

/**
 * @param {unknown} reasons
 * @param {unknown} audience
 * @param {string[]} errors
 */
function checkReturnReasons(reasons, audience, errors) {
  if (!Array.isArray(reasons)) {
    errors.push('returnReasons must be an array (it may be empty)');
    return;
  }
  const strict = isObject(audience) && audience.minorsTier === 'strict';
  reasons.forEach((reason, i) => {
    if (!isObject(reason)) {
      errors.push(`returnReasons[${i}] must be an object`);
      return;
    }
    const where = isNonEmptyString(reason.id) ? `return reason "${reason.id}"` : `returnReasons[${i}]`;
    if (!isNonEmptyString(reason.id)) errors.push(`${where}: id is missing`);
    if (!isNonEmptyString(reason.source)) errors.push(`${where}: source is missing`);
    else if (strict && STRICT_FORBIDDEN_SOURCES.includes(reason.source)) {
      errors.push(`${where}: source "${reason.source}" is not allowed in the strict tier`);
    }
    if (!Number.isInteger(reason.maxPerDay) || /** @type {number} */ (reason.maxPerDay) < 0) {
      errors.push(`${where}: maxPerDay must be an integer, zero or more`);
    }
    const qh = reason.quietHours;
    if (!Array.isArray(qh) || qh.length !== 2 || !qh.every((t) => typeof t === 'string' && HHMM.test(t))) {
      errors.push(`${where}: quietHours must be two "HH:MM" times`);
    }
  });
}

/** @param {unknown} scores @param {string[]} errors */
function checkScores(scores, errors) {
  if (!isObject(scores)) {
    errors.push('scores must be an object');
    return;
  }
  if (scores.modifyAfterFact !== false) errors.push('scores.modifyAfterFact must be false');
  if (scores.assistedRunsOnSharedBoards !== false) errors.push('scores.assistedRunsOnSharedBoards must be false');
}

/** @param {unknown} experiment @param {string[]} errors @param {string[]} warnings */
function checkExperiment(experiment, errors, warnings) {
  if (!isObject(experiment)) {
    errors.push('experiment must be an object');
    return;
  }
  const pct = experiment.holdoutPercent;
  // The holdout hash has 100 buckets, so only whole percents can be honored.
  if (!Number.isInteger(pct) || /** @type {number} */ (pct) < 1 || /** @type {number} */ (pct) > 20) {
    errors.push('experiment.holdoutPercent must be a whole number from 1 to 20');
  }
  const primary = experiment.primary;
  if (!Array.isArray(primary) || primary.length === 0 || !primary.every(isNonEmptyString)) {
    errors.push('experiment.primary must name at least one metric');
  }
  if (!isFiniteNumber(experiment.readAfterDays) || experiment.readAfterDays < MIN_READ_DAYS) {
    warnings.push(`experiment.readAfterDays is under ${MIN_READ_DAYS} or missing`);
  }
}

/**
 * @template T
 * @param {T} value
 * @returns {T}
 */
function deepFreeze(value) {
  if (typeof value === 'object' && value !== null && !Object.isFrozen(value)) {
    Object.freeze(value);
    for (const v of Object.values(value)) deepFreeze(v);
  }
  return value;
}

/**
 * @param {Condition} cond
 * @param {Inputs} values
 * @returns {boolean}
 */
function conditionHolds(cond, values) {
  const x = values[cond.input];
  if (!isFiniteNumber(x)) return false; // unknown inputs never match, whatever the op
  switch (cond.op) {
    case '>=': return x >= cond.value;
    case '>': return x > cond.value;
    case '<=': return x <= cond.value;
    case '<': return x < cond.value;
    case '==': return x === cond.value;
    case '!=': return x !== cond.value;
    default: return false;
  }
}

/**
 * @param {PlayerState | Inputs} stateOrInputs
 * @returns {Inputs}
 */
function readInputs(stateOrInputs) {
  if (isPlayerState(stateOrInputs)) return readStateInputs(stateOrInputs);
  if (!isObject(stateOrInputs)) throw new TypeError('evaluate() needs a player state or an inputs object');
  /** @type {Inputs} */
  const out = {};
  for (const name of ALLOWED_INPUTS) {
    const v = stateOrInputs[name];
    out[name] = isFiniteNumber(v) ? v : null;
  }
  return out;
}

/**
 * Creates an engine bound to one validated policy and one install.
 * Throws when the policy is invalid; catch it and run the game without
 * adaptation (every mode behaves as shared).
 * @param {unknown} policy parsed policy JSON
 * @param {{ installId: string, setting?: string, saved?: SavedEngine }} options
 */
export function createEngine(policy, options) {
  const check = validatePolicy(policy);
  if (!check.ok) {
    const error = new Error(`invalid pxe policy: ${check.errors.join('; ')}`);
    /** @type {Error & { errors?: string[] }} */ (error).errors = check.errors;
    throw error;
  }
  if (!isObject(options) || !isNonEmptyString(options.installId)) {
    throw new TypeError('createEngine needs options.installId (a stable pseudonymous install id)');
  }
  const defaultSetting = options.setting ?? 'auto';
  checkSetting(defaultSetting);

  // Own frozen copy: a caller editing its object later cannot change behavior.
  const p = /** @type {Policy} */ (deepFreeze(structuredClone(policy)));
  const modesById = new Map(p.modes.map((m) => [m.id, m.shared]));
  const { minOffset, maxOffset } = p.difficulty;
  /** @param {number} x */
  const clamp = (x) => Math.min(maxOffset, Math.max(minOffset, x));
  const holdout = holdoutBucket(options.installId, p.policyRevision) < p.experiment.holdoutPercent;

  let offset = p.difficulty.default;
  /** @type {Map<string, SessionCounters>} */
  let sessions = new Map();
  /** @type {LogEntry[]} */
  let log = [];
  if (options.saved !== undefined) restore(options.saved);

  /** @param {string} sessionId @returns {SessionCounters} */
  function countersFor(sessionId) {
    let c = sessions.get(sessionId);
    if (!c) {
      c = { rules: {}, easings: 0 };
      sessions.set(sessionId, c);
      while (sessions.size > SESSION_MEMORY) sessions.delete(/** @type {string} */ (sessions.keys().next().value));
    }
    return c;
  }

  /** @param {SavedEngine} saved */
  function restore(saved) {
    if (!isObject(saved) || !Number.isInteger(saved.offset) || !Array.isArray(saved.sessions) || !Array.isArray(saved.log)) {
      throw new TypeError('options.saved is not a value returned by engine.save()');
    }
    offset = clamp(saved.offset); // a newer policy may publish a narrower range
    sessions = new Map();
    for (const s of saved.sessions) {
      if (!isObject(s) || !isNonEmptyString(s.id) || !isObject(s.rules) || !Number.isInteger(s.easings)) {
        throw new TypeError('options.saved has a malformed session entry');
      }
      sessions.set(s.id, { rules: { ...s.rules }, easings: s.easings });
    }
    log = saved.log.map((entry) => Object.freeze({ ...entry }));
  }

  /**
   * @param {Outcome} outcome
   * @param {number} offsetNow
   * @returns {Readonly<Decision>}
   */
  const none = (outcome, offsetNow) =>
    Object.freeze({ action: null, ruleId: null, reason: null, explainKey: null, value: null, targetMode: null, offsetNow, holdout, outcome });

  return Object.freeze({
    engineVersion: ENGINE_VERSION,
    policyRevision: p.policyRevision,
    /** True when this install is in the persistent holdout for this policy revision. */
    holdout,

    /**
     * Decides what, if anything, to do at a decision point (normally a level
     * start). Call it once per decision point: a returned action counts
     * against its caps and is logged.
     * @param {PlayerState | Inputs} state
     * @param {string} modeId
     * @param {{ setting?: string, sessionId?: string }} [opts]
     * @returns {Readonly<Decision>}
     */
    evaluate(state, modeId, opts = {}) {
      const setting = opts.setting ?? defaultSetting;
      checkSetting(setting);
      // Guarantee 1: shared modes get the same parameters for everyone. An
      // undeclared mode is treated the same way.
      if (!modesById.has(modeId)) return none('unknown_mode', 0);
      if (modesById.get(modeId)) return none('shared_mode', 0);

      // Guarantee 2: the player's own choice always wins over adaptation.
      const fixed = setting !== 'auto';
      const fixedOffset = fixed ? clamp(SETTING_OFFSETS[/** @type {'easy' | 'normal' | 'hard'} */ (setting)]) : 0;
      // Guarantee 3: holdout players never adapt; their chosen setting still applies.
      if (holdout) return none('holdout', fixed ? fixedOffset : p.difficulty.default);

      const values = readInputs(state);
      const sessionId = opts.sessionId ?? (isPlayerState(state) ? `session:${state.sessionSeq}` : 'session:0');
      if (!isNonEmptyString(sessionId)) throw new TypeError('sessionId must be a non empty string');
      const counters = countersFor(sessionId);

      // First eligible rule in file order wins. A rule is skipped (and the next
      // one tried) when its cap is used up, when it is a difficulty step under
      // a fixed setting, when clamping would leave the offset where it is, or
      // when it would be a second silent easing this session.
      for (const rule of p.rules) {
        if (!rule.modes.includes(modeId)) continue;
        const used = counters.rules[rule.id] ?? 0;
        if (rule.maxPerSession !== undefined && used >= rule.maxPerSession) continue;
        if (!rule.when.every((c) => conditionHolds(c, values))) continue;

        const { action } = rule.then;
        /** @type {number | null} */
        let value = null;
        if (action === 'difficulty_offset') {
          if (fixed) continue;
          value = /** @type {number} */ (rule.then.value);
          const next = clamp(offset + value); // guarantee 5: clamped to the published range
          if (next === offset) continue;
          const easing = next < offset;
          if (easing && counters.easings >= 1) continue; // guarantee 5: one silent easing per session
          offset = next;
          if (easing) counters.easings += 1;
        }
        counters.rules[rule.id] = used + 1;

        const offsetNow = fixed ? fixedOffset : offset;
        const targetMode = action === 'suggest_mode' ? /** @type {string} */ (rule.then.mode) : null;
        // Guarantee 4: every action carries its rule id, reason and explain key, and is logged.
        log.push(
          Object.freeze({
            at: isPlayerState(state) ? state.lastAt : null,
            sessionId,
            mode: modeId,
            ruleId: rule.id,
            reason: rule.reason,
            explainKey: rule.explainKey,
            action,
            value,
            targetMode,
            offsetNow,
            policyRevision: p.policyRevision,
            engineVersion: ENGINE_VERSION,
          }),
        );
        return Object.freeze({
          action,
          ruleId: rule.id,
          reason: rule.reason,
          explainKey: rule.explainKey,
          value,
          targetMode,
          offsetNow,
          holdout,
          outcome: /** @type {Outcome} */ ('action'),
        });
      }
      return none('no_match', fixed ? fixedOffset : offset);
    },

    /** The adaptive offset (what `auto` would use in a non shared mode). */
    offset: () => (holdout ? p.difficulty.default : offset),

    /** A copy of the audit log, oldest first. */
    log: () => log.slice(),

    /** Player reset: offset back to the default and every counter cleared. The log is kept. */
    reset() {
      offset = p.difficulty.default;
      sessions = new Map();
    },

    /** Plain JSON to persist across app launches; pass it back as options.saved. */
    save() {
      return {
        engineVersion: ENGINE_VERSION,
        policyRevision: p.policyRevision,
        offset,
        sessions: [...sessions].map(([id, c]) => ({ id, rules: { ...c.rules }, easings: c.easings })),
        log: log.map((entry) => ({ ...entry })),
      };
    },
  });
}

/** @param {unknown} setting */
function checkSetting(setting) {
  if (typeof setting !== 'string' || !SETTINGS.includes(setting)) {
    throw new TypeError(`setting must be one of ${SETTINGS.join(', ')}`);
  }
}
