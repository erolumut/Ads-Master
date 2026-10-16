# Player Experience Engine (pxe 0.1 reference)

A small, dependency free engine that reads a [pxe 0.1 policy](../references/policy-format.md) and tells a game, at each level start, whether to adapt for this player and why. Plain ES modules, no build step. Runs in Node 22 and in any browser with ES2022, `TextEncoder` and `structuredClone` (all current browsers). `ENGINE_VERSION` is `0.1.0`.

It is the honest version of adaptive difficulty from [the research dossier](../../../research/player-experience-engine.md) (sections 6 and 7): play signals in, a bounded and explained action out, shared modes untouched, a persistent holdout, an audit log the player can read.

## Files

| File | Job |
|------|-----|
| `rng.js` | `fnv1a32`, `seedFromString`, `createRng` (mulberry32, integer only), `createBag` (bag randomizer) |
| `rating.js` | `expected`, `update`: Elo style rating of a player against a level |
| `state.js` | `createPlayerState`, `applyEvent`, `inputs`: folds play events into the 13 section 3 inputs |
| `policy.js` | `validatePolicy`, `createEngine`, the allowed and forbidden name lists, `holdoutBucket` |
| `index.js` | The public API, re-exported |
| `samples/policy.example.json` | The section 2 example policy, valid |
| `test/*.test.mjs` | `node:test` suite (76 tests) |

## Guarantees

| Policy format section 6 | How the engine keeps it |
|-------------------------|-------------------------|
| 1. No action in a shared mode | `evaluate` returns `action: null`, `outcome: 'shared_mode'` and `offsetNow: 0` for a shared mode, whatever the rules or the player setting say. An undeclared mode is treated as shared (`'unknown_mode'`). `validatePolicy` also refuses a rule that names a shared mode. |
| 2. A fixed setting disables difficulty actions | `easy`, `normal` and `hard` map to offsets -1, 0 and +1, clamped to `minOffset` and `maxOffset`. Difficulty rules are skipped; hint, break, next goal and mode offers still fire within their caps. The adaptive offset is kept, so switching back to `auto` resumes it. |
| 3. Holdout players get no actions | Holdout when `fnv1a32(installId + ':' + experiment.holdoutSalt) % 100 < holdoutPercent`. The salt stays the same across policy revisions, so membership persists through a long read. `evaluate` returns `outcome: 'holdout'` and `holdout: true`; the player's own setting still applies. Keep feeding their events: their state is still estimated and their telemetry still counts. |
| 4. Every action carries rule id, reason and explain key, and is logged | Each returned action has `ruleId`, `reason`, `explainKey` and is appended to `engine.log()` with time, session, mode, value, offset, policy revision and engine version. |
| 5. Offsets clamped; silent easing at most once per session | The offset moves by the rule's step and is clamped to the published range. A step that clamping would cancel is skipped, so the next rule (a hint, a break) gets its turn. At most one easing (negative step) per session id, across all rules. |
| 6. Seeded randomness, identical on every platform | `rng.js` uses only unsigned 32 bit integer operations. The vectors pinned in the tests were computed with an independent Python implementation and reproduced by a JVM port. |

Also guaranteed: `validatePolicy` and `createEngine` refuse any input or action outside the allowed lists or containing a forbidden fragment (section 4), so a policy cannot read spend, ads or device value under any name. The engine copies and freezes the policy at creation, so later edits to the caller's object change nothing. Neither `applyEvent` nor `evaluate` reads the clock or `Math.random` (a test scans the sources).

## Usage

```js
import { readFileSync } from 'node:fs';
import { applyEvent, createEngine, createPlayerState } from './engine/index.js';

const policy = JSON.parse(readFileSync('engine/samples/policy.example.json', 'utf8'));
// Throws on a broken policy: catch it and run the game with no adaptation.
const engine = createEngine(policy, { installId: 'install-1' });
let state = createPlayerState();

const t0 = 1_792_000_000_000; // the game's own clock; the engine never reads one
state = applyEvent(state, { type: 'session_start', at: t0, localDay: '2026-10-16' });

for (let attempt = 0; attempt < 4; attempt += 1) {
  const at = t0 + attempt * 60_000;
  state = applyEvent(state, { type: 'level_start', at, levelId: 'L12', levelRating: 1540 });
  const d = engine.evaluate(state, 'levels'); // once per level start
  console.log(d.action, d.explainKey, d.offsetNow);
  // Build the level with d.offsetNow; show d.explainKey as the "why" line.
  state = applyEvent(state, {
    type: 'level_end', at: at + 50_000, levelId: 'L12', result: 'fail',
    durationMs: 50_000, medianMoveMs: 1_400, medianLevelMs: 80_000,
  });
}
// null null 0
// null null 0
// offer_hint pxe.reason.stuck 0
// difficulty_offset pxe.reason.struggling -1
```

In a browser, load the same files with `<script type="module">` and fetch the policy: `const policy = await (await fetch('/pxe/policy.json')).json();`.

Use a pseudonymous install id that your consent flow covers. Never use an advertising id (IDFA, GAID) as the install id.

### Persisting across launches

The player state is plain JSON: store it as is. The engine holds the adaptive offset, the per session caps and the log; `engine.save()` returns plain JSON, and `createEngine(policy, { installId, saved })` restores it. Restoring keeps a session's caps after an app restart, and clamps the offset if a newer policy publishes a narrower range. A malformed `saved` value throws; start fresh in that case. Persist the player state and the engine together (or pass your own session ids): a fresh player state restarts its session counter, and old caps saved under the same session id would then hold back a new session.

`engine.reset()` is the player's reset: the offset goes back to `difficulty.default` and every counter clears. The log is kept, so the player can still see what happened before. To also forget the skill estimate, replace the player state with `createPlayerState()`.

## Events and inputs

Every event carries `type` and `at` (epoch milliseconds from the game). `at` never moves the state's time backwards: an earlier `at` (a device clock set back) is treated as the latest time seen. A malformed event throws a `TypeError`, so a typo in an event name cannot silently stop adaptation.

| Event | Fields | Effect |
|-------|--------|--------|
| `session_start` | `gapHours?`, `localDay?` | New session: clears `fail_streak` and `hint_uses_session`. `session_gap_hours` is `gapHours`, else the time since the last event, else null (first session). `sessions_today` counts by `localDay` (the player's calendar day, such as `'2026-10-16'`), else by UTC day; pass `localDay` always or never. |
| `level_start` | `levelId`, `levelRating?` | A new level, or a replay after a win, resets `attempts_on_level` and `hint_uses_level`. `levelRating` sets `level_rating`. |
| `level_end` | `levelId`, `result`, `durationMs?`, `medianMoveMs?`, `medianLevelMs?` | One finished attempt. Win: clears `fail_streak`, adds to `fast_solve_streak` when `durationMs < medianLevelMs` (else resets it), updates `skill_rating`. Fail: adds to `fail_streak`, resets `fast_solve_streak`, updates `skill_rating`. Quit: resets `fast_solve_streak` only. |
| `hint_used` | none | Adds to `hint_uses_level` and `hint_uses_session`. |
| `restart` | `medianMoveMs?` | Send instead of a `level_end` when the player restarts mid level, then a `level_start`. Counts as a finished attempt, adds to `restarts_recent`, resets `fast_solve_streak`. |

Choices worth knowing:

- `attempts_on_level` counts finished attempts, so at a level start it reads "tries before this one". With the example policy a struggling player gets a hint offer at the start of the third try and one easing at the start of the fourth, as the usage output shows.
- A quit or a restart is not a fail, so `fail_streak` keeps its count, and not a win, so it breaks a fast solve run. Easing stays generous; raising needs an unbroken run.
- `quit_rate_recent` is quits divided by the last 10 finished attempts (restarts count as attempts, not as quits).
- An input that is not known yet (`median_move_ms` before any attempt, `rating_gap` on an unrated level) is null, and a condition on a null input never matches, whatever the operator.
- Quits and unrated levels do not move `skill_rating`. The level side of each update is discarded: level ratings come from the offline calibration table.

## How evaluate decides

`engine.evaluate(state, modeId, { setting, sessionId })` takes a player state (or a plain object of input values) and returns a frozen decision: `{ action, ruleId, reason, explainKey, value, targetMode, offsetNow, holdout, outcome }`.

1. Undeclared or shared mode: no action, `offsetNow` 0.
2. Holdout install: no action, `offsetNow` is the fixed setting's offset or `difficulty.default`.
3. Rules are tried in file order. A rule is skipped when it does not list the mode, when its `maxPerSession` is used up for this session id, or when any condition fails. A difficulty rule is also skipped under a fixed setting, when clamping would leave the offset unchanged, or when it would be a second easing this session.
4. The first rule left is applied, counted, logged and returned. None left: `outcome: 'no_match'`.

`sessionId` defaults to the player state's session counter, so caps follow real sessions. With a plain inputs object, pass `sessionId` yourself: otherwise every call shares `'session:0'` and per session caps never reset. Call `evaluate` once per decision point: a returned action counts against its caps.

## Randomness and ratings

- `fnv1a32(str)`: FNV-1a 32 bit over the UTF-8 bytes. `h = 2166136261`; for each byte `h = (h XOR byte) * 16777619 mod 2^32`.
- `createRng(seed)`: mulberry32. The seed is an integer in [0, 2^32) or a string hashed with `seedFromString`. `nextUint32()` is the raw word, `next()` is `nextUint32() / 2^32`, and `int(n)` draws words until one is below `2^32 minus (2^32 mod n)` and returns it mod n (no modulo bias). The internal state is reduced to 32 bits on every step; the widely copied snippet lets it grow as a double and diverges from the true sequence at draw 4,917,759.
- `createBag(items, rng)`: shuffles a copy (Fisher Yates: for i from n minus 1 down to 1, j = `rng.int(i + 1)`, swap), deals each entry once, reshuffles when empty. The shuffle happens on the `next()` that finds the bag empty. An item never waits more than 2n minus 2 draws. Repeat an entry to weight it.
- `expected(P, L) = 1 / (1 + 10^((L minus P) / 400))`. `update(P, L, won, { k = 32, levelK = 8 })` returns `P + k(S minus E)` and `L minus levelK(S minus E)` with S = 1 for a win.

## Porting to Swift or Kotlin

1. Keep the integer RNG identical. Use unsigned 32 bit arithmetic with wrapping multiply and add. JS `Math.imul` is a wrapping multiply, `>>>` is a logical shift, `>>> 0` reads the word as unsigned.
2. Hash the UTF-8 bytes. Keep install ids, salts and seed strings ASCII: JS replaces an unpaired surrogate with U+FFFD while Java and Kotlin write `?`.
3. Take every modulo on the unsigned value. On the JVM `Int % 100` of a hash above 2^31 is negative: `install-1` gives bucket -14 instead of 82, which would put that install in the holdout. Use `(h.toLong() and 0xFFFFFFFFL) % 100`.
4. Copy the exact `int(n)` rejection rule, the Fisher Yates loop direction and the lazy reshuffle; each changes which words are consumed.
5. Holdout string: install id, a colon, `experiment.holdoutSalt`.
6. Ratings use floating point `pow`. They are not part of the bit for bit guarantee: expect agreement to about 1e-9, so a threshold set exactly on a computed rating could resolve differently on another platform.
7. Pin the engine version. A port reports `ENGINE_VERSION` 0.1.0 only after it passes the vectors below and the behavior tests, and shared modes must run the same engine version for every player.

Kotlin (not compiled here; the equivalent Java ran on the JVM and matched every vector below):

```kotlin
class Mulberry32(seed: Long) {
    private var state = seed.toInt()
    fun nextUInt32(): Long {
        state += 0x6D2B79F5
        var t = (state xor (state ushr 15)) * (state or 1)
        t = t xor (t + ((t xor (t ushr 7)) * (t or 61)))
        return (t xor (t ushr 14)).toLong() and 0xFFFFFFFFL
    }
}

fun fnv1a32(s: String): Long {
    var h = 0x811c9dc5.toInt()
    for (b in s.toByteArray(Charsets.UTF_8)) { h = (h xor (b.toInt() and 0xFF)) * 16777619 }
    return h.toLong() and 0xFFFFFFFFL
}
```

Swift ([Unverified]: not compiled here; check it against the vectors):

```swift
struct Mulberry32 {
    var state: UInt32
    mutating func nextUInt32() -> UInt32 {
        state &+= 0x6D2B79F5
        var t = (state ^ (state >> 15)) &* (state | 1)
        t ^= t &+ ((t ^ (t >> 7)) &* (t | 61))
        return t ^ (t >> 14)
    }
}

func fnv1a32(_ s: String) -> UInt32 {
    var h: UInt32 = 0x811c9dc5
    for b in s.utf8 { h = (h ^ UInt32(b)) &* 16777619 }
    return h
}
```

Vectors (all checked in `test/rng.test.mjs` and `test/engine.test.mjs`):

| Call | Result |
|------|--------|
| `fnv1a32('')`, `('a')`, `('foobar')` | 2166136261, 3826002220, 3214735720 (the published FNV values) |
| `fnv1a32('daily:2026-10-16')` | 915013228 |
| `createRng(0)`, first 5 words | 1144304738, 1416247, 958946056, 627933444, 2007157716 |
| `createRng(42)`, first 5 words | 2581720956, 1925393290, 3661312704, 2876485805, 750819978 |
| `createRng(1)`, word 6,000,000 | 1042850813 |
| `createRng(42)`, `int(6)` × 10 | 0, 4, 0, 5, 0, 3, 4, 5, 0, 3 |
| `createRng(7)`, `int(2^31 + 1)` × 5 | 50271532, 266108690, 1741702388, 2002453909, 1030470827 |
| `createBag(['I','O','T','S','Z','J','L'], createRng(42))`, two bags | TLIOJZS, LSZOIJT |
| `holdoutBucket('install-1', 'pxe-holdout-2026')` | 82 |

## What it deliberately cannot do

- Read spend, purchases, ad readiness, ad value, device model or price, location or any personal trait. The input list is closed and forbidden fragments are refused at load.
- Change a score, decide a win or a loss, or bias pieces. Its only outputs are an offset inside the published range and offers (hint, break, next goal, another non shared mode).
- Adapt a shared mode, or let a setting change one.
- Learn: there are no models, only the rules in the file. Learned models come after randomized logged data exists, and stay inside the same bounds.
- Send anything. No network, no storage, no clock, no notifications. Return reasons are validated but scheduling them is lifecycle work.
- Replace the release gate. `validatePolicy` is a runtime seat belt for the section 5 FAIL checks plus the structure the engine needs. Run `scripts/pxe_policy_check.py` before a policy ships.

## Tests

```bash
cd skills/player-experience/engine && node --test
# or, from the repo root:
node --test 'skills/player-experience/engine/test/*.test.mjs'
```

Node 22 does not expand a directory argument, so `node --test skills/player-experience/engine/test/` fails before running anything; use one of the forms above.
