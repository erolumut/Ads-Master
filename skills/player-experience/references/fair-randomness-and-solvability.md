# Fair Randomness and Solvability

> Knowledge as of 2026-10 (research pass 2026-10-16, dossier `research/player-experience-engine.md`). Algorithms (mulberry32, FNV-1a, bag randomizers) are standard public methods described here as engineering, not as findings. Claims about named games carry their dossier labels. The Block Blast decompile claims are unverified.

Gate: generator specs, solver specs and seed rules are G1 drafts for the game repo. Changing a live generator, a bag rule or the engine version that produces shared content is G3 and needs a new `engineVersion`.

## 1. The rule

Randomness in a game is a promise: the pieces, cards or boards a player gets are not chosen against them. The engine keeps the promise in four ways.

1. **Seeded.** Every random draw comes from a seeded generator. The same seed, parameters and engine version give the same sequence on every platform.
2. **Bounded.** Bag style or history aware generators cap droughts, so no player waits forever for the piece that saves them.
3. **Solvable.** Every board the game serves is solvable, proven by a solver before it reaches a player.
4. **Not steered.** No in run draw is chosen from the player's monetization state, ad readiness or predicted value, and nothing is steered toward a loss.

## 2. Seeded RNG

### 2.1 Generator

The reference engine uses mulberry32: a 32 bit state, integer only arithmetic, small and fast, identical output in JavaScript, Swift and Kotlin when written with explicit 32 bit unsigned math. The reference is `rng.js` in [../engine](../engine/) (`ENGINE_VERSION` 0.1.0).

```js
// mulberry32: integer only, 32 bit unsigned state
function mulberry32(seed) {
  let a = seed >>> 0;
  return function next() {
    a = (a + 0x6D2B79F5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return (t ^ (t >>> 14)) >>> 0;   // 0 to 4294967295
  };
}
```

Rules for the generator:

| Rule | Why |
|------|-----|
| Integer outputs; map to a range with integer math (rejection sampling for an unbiased `n` way choice) | Floating point differs across platforms and compilers |
| Never `Math.random()`, `Date.now()` or a device clock inside the game core | Breaks replay and fairness |
| One generator per stream (pieces, board, rewards), each seeded separately | A change in one stream does not shift the others |
| Tests: a fixed seed produces a recorded golden sequence on every port | Cross platform parity |

### 2.2 Seeds from strings with FNV-1a

Seeds are derived, never stored as magic numbers. FNV-1a (32 bit) hashes a string into a seed:

```js
function fnv1a32(str) {
  let h = 0x811C9DC5;                 // offset basis
  for (const ch of new TextEncoder().encode(str)) {
    h ^= ch;
    h = Math.imul(h, 0x01000193) >>> 0; // FNV prime
  }
  return h >>> 0;
}
```

| Content | Seed string (example shape) | Who issues it |
|---------|-----------------------------|---------------|
| Daily puzzle | `product:daily:<server day id>:<engineVersion>` | Server |
| Ranked match | `product:ranked:<match id>:<engineVersion>` | Server |
| Level N of the path | `product:level:<N>:<engineVersion>` | Client or server, same result |
| Practice run | `product:practice:<install id>:<run counter>` | Client |
| Stream inside a run | `<run seed string>:pieces`, `<run seed string>:board` | Derived |

Hash the UTF-8 bytes, not the platform's native string units, so every port gets the same seed.

### 2.3 engineVersion pinning

| Rule | Why |
|------|-----|
| `generate(seed, params, engineVersion)` is pure | The same inputs give the same board everywhere |
| Every run records its seed, params and engine version | Replays and disputes are settled by recomputation |
| A run is never replayed under another engine version | A generator change produces a different board |
| A shared mode pins one engine version for its whole period (day, match, season) | Everyone plays the same thing |
| Changing the generator, the bag or the solver bumps the version | Old runs stay reproducible |
| The level table keys on engine version | A regenerated level is a new level ([calibration](difficulty-measurement-and-calibration.md)) |

## 3. Bag randomizers and drought caps

A pure independent draw can starve a player of the one piece they need for a long run. Players experience this as unfair even when it is random.

| Generator | How it works | Drought behavior | Note |
|-----------|-------------|------------------|------|
| Independent draw | Each piece drawn uniformly | Unbounded droughts possible | Feels unfair at the tail |
| 7 bag (falling block games) | Shuffle all piece types, deal them out, reshuffle | Bounded by bag size | Widely used; sources are fan wikis only [Unverified] |
| History aware | Reroll a draw if it repeats one of the last k pieces | Shortens droughts, softer than a bag | Tune k |
| Weighted bag | A bag with some types repeated | Bounded; changes the mix | The weights are a published difficulty parameter |

Rules:
1. Write the drought cap as a number in the generator spec ("piece type X appears at least once in every M draws").
2. Test it: run many seeds and assert the maximum gap observed never exceeds the cap.
3. Bag rules and weights are parameters of the level or mode, chosen before the run starts, and logged with the run.
4. In shared modes the bag and weights are identical for everyone (they come from the mode's params).

## 4. Guaranteed solvable boards

| Step | What |
|------|------|
| 1 | Generate with the seed and params |
| 2 | Run the solver on the generated board (search based, exhaustive or MCTS; it proves a solution exists, it does not measure felt difficulty) |
| 3 | If unsolvable, derive the next seed deterministically (`seed string + ":retry:<n>"`) and repeat |
| 4 | Record the final seed and retry count; the client regenerates the same board from it |
| 5 | For daily and ranked content, the server runs steps 1 to 4 before publishing and stores the result |
| 6 | For streams revealed over time (pieces dealt during a run), prove that from every reachable state at least one legal continuation exists for the stream as generated, or declare the mode as one where a dead end is part of the game and say so in the rules |

The difficulty of a solvable board is measured separately, by outcomes and human like bots ([calibration](difficulty-measurement-and-calibration.md) section 4). Solvable is a floor, not a difficulty rating.

## 5. Why rigged piece streams are out

### 5.1 What the claim was

A viral video (2026-10) claimed a decompile of Block Blast shows difficulty and loss timing driven by each player's predicted ad value, including a "death algorithm" that makes the next turn unwinnable when an expensive rewarded ad is ready. These claims are unverified: one creator, relayed by AdExchanger (2026-10-15) and MetaFilter (2026-10-14), with no code, no independent test and no studio response [Reported, 2026-10]. Do not repeat them as fact. Whatever the truth, the spend and ad linked version is high legal risk under the AI Act Art 5, consumer law and Apple 2.3.1, 5.6 and 5.1.2(iii) ([ethics, law and store rules](ethics-law-and-store-rules.md)).

### 5.2 What the evidence actually supports

The strongest causal result is Ascarza, Netzer and Runge (IJRM 2025): a 12 week randomized field experiment with 300,000+ players and a holdout, where players at higher churn risk received easier puzzles through more favorable piece allocation. Engagement and long run retention rose; purchases in the specific round fell, but total spending rose in the short and long run [Reported, 2026-10]. The Columbia summary reports ad revenue +21% [Reported, verify].

So piece allocation was used to help, and helping worked. The question is not whether allocation may ever change, but how.

| Allowed (an easier difficulty, disclosed) | Out (a rigged stream) |
|-------------------------------------------|------------------------|
| A difficulty step selects a different published bag or weight set before the run starts | Draws changed mid run to cause or delay a loss |
| The trigger is a play signal (fail streak, rating gap) under a policy rule with a reason code | The trigger is spend, ad readiness, ad value, device value or location |
| The player can see it ("eased after 3 tries") and switch it off with a fixed setting | Hidden, undocumented, unswitchable |
| Private and practice modes only | Shared modes (daily, ranked, races, group boards) |
| Logged with the run (seed, params, offset) and reproducible | Not reproducible from seed and params |
| Every board still solvable | A board made unwinnable on purpose |
| Measured against a persistent holdout | No holdout |

Ascarza et al. show the direction (help at risk players) and the method (randomized, with a holdout). The engine adds what the paper summary does not cover: disclosure, a player switch, and the rule that the change happens through a published parameter, not a hidden steer.

### 5.3 Test for a rigged stream

The dossier describes the fair test nobody has published for Block Blast: log many seeded games and compare piece distributions between ad watching and non ad watching accounts. Run the same test on your own game:

1. Sample runs from players who watch rewarded ads and players who never do, in the same mode and engine version.
2. Regenerate each run's stream from its logged seed and params.
3. Assert every observed stream equals the regenerated one (no hidden steer).
4. Compare distributions between the groups at the same offset; they must be identical.
5. File the result in the audit log. A mismatch is an incident.

## 6. Daily seeds identical for all

| Rule | Why |
|------|-----|
| The server issues the day id and the seed; the device clock never decides "today" | No peeking at tomorrow, no replaying yesterday as today |
| Same seed, same params, same engine version for every player | Results are comparable; shares and boards are fair |
| The policy engine returns no action in the daily mode | Shared modes never adapt ([policy format](policy-format.md) section 1) |
| Practice replays of past days are a non shared mode | They may adapt; they never write to a shared board |
| The server revalidates submitted results by replaying the move log on the same engine | A modified client cannot post an impossible score |
| An assisted run never enters a shared board | Scores are true |

Day id and tick rules: [game-liveops daily loops](../../game-liveops/references/daily-loops-and-streaks.md) section 2.2.

## 7. Checklist before a generator ships

- [ ] Generator is integer only and seeded; golden sequence test passes on every port.
- [ ] Seeds derived with FNV-1a from documented strings; UTF-8 bytes.
- [ ] `engineVersion` bumped for any change to generator, bag, weights or solver.
- [ ] Drought cap written and tested over many seeds.
- [ ] Solver proves every served board solvable; retries are deterministic.
- [ ] No input to any draw outside seed and published params.
- [ ] Shared modes ignore the policy; server issues seeds and revalidates.
- [ ] Rigged stream test (section 5.3) scheduled monthly.
