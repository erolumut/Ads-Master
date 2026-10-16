# Policy File and Conformance Checks

> Knowledge as of 2026-10. How to write `monetization-policy.json`, the tracking plan events it needs and the store declarations file, and how to run and read `monetization_check.py` and `monetization_conformance.py`. The contract itself (modes, typed grants, the six types, the runbook) is in [Monetization contract](monetization-contract.md); this module is the working procedure around it. Both scripts use the Python standard library only and exit 0 (pass), 1 (fail) or 2 (could not run), and both end with a "This check cannot cover:" line that lists what still needs a human or another check.

## 1. Where the files live

| File | Project location | Owner | Checked by |
|------|-----------------|-------|------------|
| `monetization-policy.json` | The product repo (imported by the code) and a copy at `ads-master/data/monetization-policy.json` | This agent drafts; the human approves; the product repo ships | `monetization_check.py`, `monetization_conformance.py` |
| Tracking plan | `ads-master/tracking-plan.json` or next to the analytics module (measurement format) | `measurement`; this agent adds the monetization events | `monetization_conformance.py`; measurement's `tracking_plan_check.py` for payloads and code |
| Store declarations, one per store | `ads-master/data/store-declarations/<store>.json` | `store-submission` records what was answered in each console; this agent checks it | `monetization_conformance.py` |
| `GAME_ECONOMY.md` | `ads-master/GAME_ECONOMY.md` | This agent with the human | Read in reviews |

`<skill>` below is `skills/game-monetization` in this repo or `.claude/skills/game-monetization` in a project install.

## 2. Writing the policy file

Start from `<skill>/scripts/samples/daily-social-policy.json` (daily social product) or `<skill>/scripts/samples/progression-policy.json` (level based puzzle), or from `ads-master/data/monetization-policy.example.json` in a workspace. Schema: `<skill>/scripts/monetization-policy.schema.json`.

Order that avoids rework:
1. `product`: id, platforms, audience (`minimumAge`, `kidsMode`), regions. The audience decides the minors rules, so get it from PROJECT_BRIEF section 11 before anything else.
2. `stores`: one entry per place the product sells (`web` with Stripe, `apple`, `google`, an embed such as `discord`).
3. `modes`: every mode with its kind; every ranked mode with `countedAttemptsPerDay` and its `boards` (group or everyone). Declare derived boards (streaks, season tables) here too.
4. `currencies.virtual`: usually empty for ranked products; one soft currency for progression games.
5. `catalog`: SKUs with typed grants, integer minor unit prices, store product ids for every store.
6. `offers` and `placements`: point, mode, caps, format rules.
7. `consent`, `storeDeclarations`, `killSwitch`.
8. `contractVersion: "0.1"`, `policyRevision`: 1 and up.

## 3. monetization_check.py (the policy on its own)

```
python3 -I <skill>/scripts/monetization_check.py ads-master/data/monetization-policy.json
```

| It fails when | Typical fix |
|---------------|-------------|
| A required key is missing, an id is duplicated, a reference does not exist | Add the key, rename the duplicate, declare the mode, SKU, store, board or currency |
| A ranked mode lacks `countedAttemptsPerDay` or `boards` | Declare them (an integer or `"unlimited"`) |
| A ranked mode offer or placement grants something play changing | Move it to practice or progression, or change the grant to cosmetic, access or pass |
| A grant writes to a ranked board and is not a round, or a round writes wider than who receives it | Restrict `writesTo` to the group boards |
| A social offer grants to the buyer only | `grantsTo: group` or `everyone` |
| Rewarded without grants, opt in or grant on completion; interstitial without grace, cooldown or session cap; banner outside menus or loading; interstitial or app open in kids mode | Add the rule or move the placement |
| Price escalation, or sibling offers at one mode and point selling the same grants at different prices | One price per grant set per moment |
| Countdown copy with minors in the audience | `countdown: false` |
| Moves, time or booster offers without `maxPerAttempt` | Add the cap |
| Catalog gaps: missing store product id, a non integer price, a subscription without a period | Fill the field |
| Random items without odds, odds not summing to 1, `lootBoxes` false, minors, Belgium | Remove the random item or meet every requirement |
| Purchasable currency without a real money price shown | `showRealMoneyPrice: true` and the UI to match |
| Ads without consent first; store declarations disagreeing with the file | Fix the consent order or the declarations |

Warnings (offers without caps, rewarded without a daily cap, app open ads) do not fail the run but go in the report.

## 4. The tracking plan events the policy needs

The tracking plan uses the measurement format (`skills/measurement/references/tracking-plan-as-code.md`): `{"events": {name: {"props": {prop: {"type": ...}}}}}` with the types `id`, `num`, `bool`, `enum` and `route`, and no free string type.

| Policy item | Events required (fail if missing) | Identity properties that must carry the item's values | Also on each event |
|-------------|-----------------------------------|------------------------------------------------------|--------------------|
| Offer | `offer_shown`, `offer_accepted`, `offer_declined` | `sku`, `mode_id`, `point`; `offer_id` when the plan declares it | `contract_version`, `policy_revision`; `product` recommended |
| Rewarded placement | `ad_requested`, `ad_shown`, `ad_rewarded` | `placement_id`, `mode_id`, `point` | Same |
| Other placement | `ad_shown` | `placement_id`, `mode_id`, `point` | Same |
| Catalog item | `purchase_completed`, `purchase_refunded` | `sku` | Same |

Recommended (warning when missing): `purchase_started`, `purchase_failed`, `entitlement_granted`, `entitlement_revoked` when there is a catalog; `ad_failed`, `ad_revenue`, `consent_updated` when there are placements.

How "carry the value" is judged (mirrors measurement's `check_value`):

| Property type | Accepts the policy value when |
|---------------|-------------------------------|
| `enum` | The value is in `values` (the strongest form: coverage is proven per item) |
| `id` | The value matches `[A-Za-z0-9_.:-]`, 1 to 64 characters (a SKU or placement id with a space fails) |
| `num` | The value is a number within `min` and `max` (used for `policy_revision`; a policy revision above `max` fails) |
| `bool`, `route` | Never for identity values |
| anything else | Fails: not a tracking plan type |

`contract_version` must be an `id` or `enum` so `"0.1"` stays a string; a `num` type fails because 0.10 would read as 0.1.

Prefer `enum` for `sku`, `placement_id` and `offer_id`: the check then proves coverage item by item and warns when the plan lists values the policy no longer has (stale SKUs). With `id` types the check can only prove that the values are well formed.

When two offers share the same SKU, mode and point, the data cannot tell them apart; add an `offer_id` property to the offer events (the check warns).

## 5. The store declarations file

One file per store, recorded from the live console by `store-submission` (or the human) after each submission or form change. It states what the store forms were told, which is what players and regulators see.

```json
{
  "product": "example-daily",
  "store": "google",
  "recordedAt": "2026-10-12",
  "containsAds": true,
  "inAppPurchases": true,
  "lootBoxes": false,
  "ageRatingInputs": {
    "advertising": true,
    "randomItems": false,
    "digitalPurchases": true,
    "madeForKids": false,
    "minimumTargetAge": 13
  }
}
```

| Field | Meaning | Compared with |
|-------|---------|---------------|
| `product` | Optional; must equal the policy's product id (otherwise exit 2: wrong pairing) | `product.id` |
| `store` | Optional; must be a store id in the policy. When present, catalog based answers are judged for the items sold in that store | `stores`, `catalog[].stores` |
| `containsAds` | The "contains ads" answer or label | Ad placements in the policy and `storeDeclarations.containsAds` |
| `inAppPurchases` | The in-app purchases answer or label | Catalog items (sold in that store) and `storeDeclarations.inAppPurchases` |
| `lootBoxes` | The loot box answer or label (for example the UK "Contains loot boxes" listing label) | Random items and `storeDeclarations.lootBoxes` |
| `ageRatingInputs.advertising` | The age rating or content form's advertising answer | Ad placements |
| `ageRatingInputs.randomItems` | The random items or loot box answer in the questionnaire (Apple lists loot boxes in its age rating values [Official, 2026-10]) | Random items |
| `ageRatingInputs.digitalPurchases` | The purchases of digital goods answer | Catalog items |
| `ageRatingInputs.madeForKids` | Kids Category or a target audience that is designed for children | `audience.kidsMode` |
| `ageRatingInputs.minimumTargetAge` | The youngest age in the store's target audience answer | `audience.minimumAge` (a younger store audience fails: the minors rules were checked against the wrong audience) |
| Other `ageRatingInputs` keys | Recorded (simulated gambling, user generated content, social features) | Not cross checked; listed as NOTE lines |

Exact question wording differs per store and changes (Apple added a social media question required from September 2026 [Official, 2026-10]); record the answer under the closest key and keep the console's own wording in `SUBMISSION.md`.

## 6. monetization_conformance.py (the artefacts against each other)

```
python3 -I <skill>/scripts/monetization_conformance.py \
  --policy ads-master/data/monetization-policy.json \
  --tracking-plan ads-master/tracking-plan.json \
  --declarations ads-master/data/store-declarations/google.json \
  --declarations ads-master/data/store-declarations/apple.json
```

| Exit | Meaning |
|------|---------|
| 0 | The policy passes `monetization_check.py`, every offer, placement and SKU has event coverage with version properties, and every declarations file agrees with the policy |
| 1 | At least one FAIL line |
| 2 | Could not run: unreadable JSON, an unsupported contract version, a policy without `contractVersion`, a plan without an `events` object, a declarations file for another product, a missing argument |

It fails when:
1. The policy fails `monetization_check.py` (it loads the checker from its own folder and reports the first failure; run the checker for all of them).
2. An offer, a placement or a catalog item lacks event coverage (section 4).
3. A required event lacks `contract_version` or `policy_revision`, or their types cannot carry the policy's values.
4. A declared `product` property cannot carry the product id.
5. A declarations file disagrees with the policy content (ads present but `containsAds` false, catalog items but `inAppPurchases` false, random items but `lootBoxes` false), with `storeDeclarations`, or with the policy through its age rating answers; a required boolean is missing; or the store is not in the policy.

Warnings: recommended events missing, no `product` property, stale enum values, offers the data cannot tell apart, labels declared true while the policy has none (over declared in both files), no age rating answers. NOTE lines: store specific differences that are correct (a store that sells no catalog items), answers recorded but not cross checked.

## 7. Run order and where to wire it

| Moment | Run | Who |
|--------|-----|-----|
| Every policy draft | `monetization_check.py` | This agent |
| Before a change request leaves this agent | Both scripts | This agent |
| Every release that touches monetization or tracking | Both scripts in the product repo's CI (validate only), plus measurement's `tracking_plan_check.py --code` and a payload sample | site-engineer, the product repo |
| After any store form change | `monetization_conformance.py` with the new declarations file | store-submission records, this agent runs |
| Monthly economy review | Both scripts on the live files | This agent |

Start in warn mode for two weeks if the product repo has never run them, then make failures blocking (the same rollout measurement uses for its tracking plan check).

## 8. What neither script can see

From their "This check cannot cover" lines: whether the code follows the file (each product's conformance test does, contract section 9), derived boards the file does not declare, live prices and product ids in the store consoles, the wording on screen (offers, odds, labels), tax and merchant of record duties, whether the consoles still hold the recorded answers, whether the code emits the declared events, and laws that changed after the files were written. A check that could not run is never a pass.

## 9. Product repo conformance test (contract section 9)

The scripts check files. The product repo proves behavior with its own tests:

| Test | Proves |
|------|--------|
| Policy loads and passes `monetization_check.py`; governed constants equal the policy | The code imports the policy instead of copying it |
| No board accepts an attempt beyond `countedAttemptsPerDay` after any purchase, reward, admin grant or encore | The ranked rule holds in code |
| A group round writes only to the named group boards; the global board query excludes encore plays | The Encore cannot lift anyone globally |
| Grants are idempotent; a refund revokes; a renewal does not grant twice | The ledger works |
| No ad call with consent denied | Consent order |
| The kill switch stops every offer and placement | Remote control works |
| Every placement and SKU emits the section 6 events with `policy_revision` | The plan matches the code |

## 10. Reading a failure quickly

| Output line begins with | Look at |
|-------------------------|---------|
| `the policy fails monetization_check.py` | Run the checker; fix the policy first |
| `event '<name>' is not in the tracking plan` | Add the event to the plan (measurement owns the plan; send the handoff) |
| `<event>: no '<prop>' property` | Add the property to that event |
| `offer <id>: <event>.<prop> cannot carry` | Add the value to the enum or fix the policy id |
| `declarations <store>: <field> is false but the policy has` | The store form under declares; fix the console answer (G3) or the policy |
| `declarations <store>: <field> is <x> but policy.storeDeclarations` | Decide which file is right; the content hint names the likely one |
| `could not run` | Fix the input; nothing was checked |
