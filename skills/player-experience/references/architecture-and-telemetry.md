# Architecture and Telemetry

> Knowledge as of 2026-10 (research pass 2026-10-16, dossier `research/player-experience.md`). The architecture is a synthesis, not a published standard. The reference implementation is the dependency free JavaScript engine in [../engine](../engine/) (`rng.js`, `rating.js`, `state.js`, `policy.js`; `ENGINE_VERSION` 0.1.0). Tool facts come from search summaries [Reported, 2026-10]. Language notes for Swift and Kotlin are engineering guidance, checked by golden tests rather than by sources.

Gate: integration specs and tracking plans are G1. Shipping the engine in a build is a release through the game repo's own process, with `site-engineer` release QA for web builds. Publishing a policy or a level table to remote config is G3.

## 1. Reference architecture

| Component | Runs | Job |
|-----------|------|-----|
| Game core | Client and server (same code) | Pure `generate(seed, params, engineVersion)`, solver, move log; integer only randomness |
| Telemetry | Client | The six events (section 3); pseudonymous install id; consent gated |
| Player state estimator | Client | Elo skill, rolling window, fail streak, median move time; frustration and boredom as transient flags, never stored profiles |
| Policy engine | Client | Versioned JSON rules mapping state to bounded actions; never touches shared modes |
| Remote config and experiments | Server or CDN | Policy revision, thresholds, level difficulty table; control, treatment and persistent holdout; sample ratio check |
| Offline calibration | Server, batch | Weekly level ratings (Elo or Rasch), bot playtests for new levels |
| Adaptation audit log | Client full, server sampled | Policy version, inputs summary, action, reason code |
| Transparency UI | Client | Difficulty setting, why this level, log, reset |
| Mode gate | Client and server | Ranked and daily ignore the estimator and policy; the server issues seeds and revalidates results with the same engine |

## 2. Data flow

```
 [server] day id, match id ──> seed issue ──┐
                                            v
 [client] game core: generate(seed, params, ENGINE_VERSION) ──> play ──> move log
                │                                                │
                │                       events (consent gated) ──┼──> [server] event store
                v                                                │          │
 [client] state.js estimator (rating.js Elo, fail streak, move time)        │
                │                                                           v
                v                                          [server] weekly calibration
 [client] mode gate ── shared? ── yes ──> no action                (Elo or Rasch, bots)
                │                                                           │
                no                                                          v
                v                                          [server or CDN] remote config:
 [client] policy.js evaluate(state, mode) <── policy JSON, level table <────┘
                │
                v
 bounded action (offset, hint, break, next goal, suggest mode) ──> transparency UI
                │
                └──> audit log (client full; server sample)

 [server] result submit ──> replay move log on the same engine ──> shared board
```

The policy and level table flow down; play events flow up. Raw play never needs to leave the device for adaptation to work; the server needs only consented events for calibration and experiments.

## 3. Events

| Event | Fields | Use |
|-------|--------|-----|
| `session_start` | session id, gap since previous session (`session_gap_hours`), app version, engine version, policy revision, holdout flag | Opens, sessions per week, return reasons |
| `level_start` | mode id, level id, seed, params, engine version, offset applied, level table version, player setting | Funnel; links an attempt to what produced it |
| `level_end` | result (win, fail), attempts on this level, duration, moves used, assisted flag | Pass rate, attempts to pass, first try pass, ratings |
| `hint_used` | level id, attempt index, offered or self requested | Help use, stuck points |
| `restart` | level id, move index | Frustration signal |
| `quit` | level id, move index | Quit rate, walls |

Engine side events worth adding to the tracking plan: `pxe_action` (rule id, action, value, reason, explain key), `pxe_setting_changed` (from, to), `pxe_reset`. Names are proposals; `measurement` owns the tracking plan ([game tracking](../../measurement/references/game-tracking.md)).

Field rules:
- No ad id, no device id, no IP stored, no location, no payment field on any engine event.
- Integers and enums; durations in milliseconds.
- `difficulty_table.py` needs `player_id`, `level`, `result` and optionally `attempts_before`, `duration_ms`, `ts`, all derivable from these events ([calibration](difficulty-measurement-and-calibration.md) section 6.1).

## 4. Privacy by design

| Principle | Implementation | Basis |
|-----------|---------------|-------|
| Pseudonymous id | Random install id generated on first launch; not an ad id, not tied to an account unless the player links one | Dossier architecture |
| Consent gated | No telemetry before consent where consent is required; the engine still adapts on device without telemetry | Apple 5.1.1: consent for collecting usage data "even if such data is considered to be anonymous" [Official, 2026-06] |
| State on device | Estimator state lives on the device; reset clears it | Apple 5.1.2(iii) [Official, 2026-06] |
| Transient flags | Frustration and boredom flags last for the session; never stored as a profile | Dossier principle |
| No sensitive inference | Never infer spend capacity, health, mood or any personal trait | Dossier principle 2; [policy format](policy-format.md) section 4 |
| Minors | Strict tier: profiling off by default, no ad SDK profiling | KIDS Act direction [Reported, 2026-09]; UK Children's Code profiling off by default [Reported] |
| Privacy policy | Names adaptation and the events used | Apple 5.1.1 [Official, 2026-06] |
| Server sample | The audit log sample carries play signals only | Section 3 |

On device is not an exemption: the AI Act applies to on device systems, and consent and disclosure still apply ([ethics](ethics-law-and-store-rules.md)).

## 5. Porting to Swift and Kotlin

The engine is written so a port reproduces the same sequence bit for bit: unsigned 32 bit integer arithmetic only, floats only in `next()` (uint32 divided by 2^32, exact in IEEE 754 doubles).

| Concern | JavaScript (reference) | Swift | Kotlin |
|---------|------------------------|-------|--------|
| 32 bit wrap | `>>> 0`, `Math.imul` | `UInt32` with wrapping operators `&+`, `&*` | `Int` arithmetic wraps; use `ushr` for unsigned shifts, or `UInt` |
| Unsigned right shift | `>>>` | `>>` on `UInt32` | `ushr` |
| String to bytes | `TextEncoder` (UTF-8) | `Array(str.utf8)` | `str.encodeToByteArray()` (UTF-8); mask bytes with `and 0xFF` |
| Integer in [0, n) | Rejection sampling in `int(n)` | Same algorithm, not `arc4random_uniform` | Same algorithm, not `kotlin.random` |
| Shuffle | Fisher Yates as in `createBag` | Same loop, same rng calls | Same loop, same rng calls |
| Version | `ENGINE_VERSION` constant | Same string constant | Same string constant |

Porting procedure:
1. Port `rng.js` first. Generate golden vectors from the reference: `fnv1a32` of a fixed list of strings, the first outputs of `createRng` for fixed seeds, `int(n)` sequences for several n, bag deals.
2. Assert the port reproduces every vector exactly. Run the vectors in CI on every platform.
3. Port `rating.js`, `state.js`, `policy.js`; replay a recorded event log through both and compare the action stream.
4. Use the platform's native random generator nowhere in game logic.
5. Any mismatch is a release blocker for shared modes: two platforms would serve different dailies.

Run the reference tests with `node --test` on the engine's test folder (see the skill's Scripts section).

## 6. Remote config delivery and caching

| Item | Delivery | Cache rule |
|------|----------|-----------|
| Policy JSON | Remote config or CDN, versioned by `policyRevision` | Keep the last good policy on device; on fetch failure use it; with no policy, take no actions |
| Level table | Same, versioned | Keep last good; a level absent from the table gets no difficulty action |
| Experiment assignment | Computed on device from the install id hash (format section 6) | No network needed |
| Kill switch | A config flag that disables every action | Checked before each evaluation |

Firebase Remote Config on the web has a minimum fetch interval of 12 hours by default [Reported, 2026-10]: a rollback may take that long to reach every client unless the app fetches on start with a shorter interval for this key. Plan rollbacks with the real propagation time.

Validate the fetched policy on device against the format (version supported, offsets in range) before use; on failure, keep the previous one and log it. The server side gate is `pxe_policy_check.py` before publish ([policy design](adaptive-policy-design.md) section 8).

## 7. Mode gate and server revalidation

| Rule | Client | Server |
|------|--------|--------|
| Shared modes listed in the policy with `shared: true` | `evaluate(state, mode)` returns no action | Rejects a result that carries an offset or assisted flag for a shared board |
| Seeds for shared modes | Received, never generated locally | Issued from the day id or match id, logged |
| Engine version for a shared period | Pinned | Pinned; a client on another version is asked to update before playing |
| Results | Sent with the move log | Replayed on the same engine; impossible results rejected |
| Assisted runs | Labeled | Never written to a shared board |
| Scores | Never changed after the fact | Never changed after the fact |

The mode gate is code in both places, not a convention: a modified client cannot make a shared mode adaptive, because the server replays every shared result.

## 8. Minimal first version (web puzzle game)

From the dossier:
1. The six events.
2. Elo for player and level.
3. Four rules: offer a hint or break after K fails on one level; offer a harder level after a fast solve streak; clamp the offset to one step; never lower silently more than once per session.
4. The transparency UI (setting, why this level, log, reset).
5. One experiment tool with a persistent holdout.
6. A weekly level table.

Everything else (churn models, bandits, bot playtests) comes after the first holdout read ([player modeling](player-modeling-and-churn.md) section 6).

## 9. Integration checklist

- [ ] Game core pure; seeds from strings; `ENGINE_VERSION` logged on every attempt.
- [ ] Golden vectors pass on every platform.
- [ ] Mode gate enforced on client and server; shared results replayed.
- [ ] Events consent gated; no ad, device or location ids on engine events.
- [ ] Policy and level table cached with last good fallback and a kill switch.
- [ ] Holdout assignment on device; holdout events still sent.
- [ ] Audit log on device; server sample configured.
- [ ] Transparency UI reachable from pause and fail screens.
- [ ] Privacy policy names adaptation.
