# Experiments and Testing

> Knowledge as of 2026-10. Google added AI Max experiments (2025), PMax asset experiments (reported generally available 2026-10) and new experimentation tools to explain automated decisions (reported rollout by end of 2026-09). Meridian GeoX became globally available 2026-09-10 and Meridian Studio was announced at GML 2026. Verify availability before planning.

## 1. Which test answers which question

| Question | Test | Built in? | Typical duration |
|---|---|---|---|
| Does a bid strategy, target or setting change perform better? | Custom experiment (Search, Display, some Demand Gen) | Yes | 4 to 8 weeks |
| Does AI Max add incremental conversions? | AI Max experiment | Yes | 4 to 6 weeks |
| Does adding PMax add incremental conversions to Search or Shopping? | PMax uplift experiment | Yes | 6 to 8 weeks |
| Does final URL expansion help PMax? | PMax final URL expansion experiment | Yes | 4 to 6 weeks |
| Do new creatives help PMax? | PMax asset experiment | Yes (reported GA 2026-10) [Unverified] | 4 weeks |
| Which Demand Gen creative or audience wins? | Demand Gen A/B experiment | Yes | 3 to 6 weeks |
| Does an ad copy change help across many ad groups? | Ad variations | Yes | 4 weeks |
| Does the channel cause conversions at all? | Conversion Lift (user or geo based) | Yes, eligibility rules | 2 to 8 weeks |
| Does video lift awareness or consideration? | Brand Lift | Yes, eligibility rules | 1 to 4 weeks |
| Is brand search incremental? | Geo holdout or time-based on/off | DIY or Meridian GeoX | 4 to 8 weeks |
| What is the right channel mix? | MMM (Meridian), calibrated by experiments | Open source and Google tools | Quarterly |

## 2. Test design rules

1. Write the hypothesis before building: "If we [change], then [primary metric] will [direction and size], because [reason]." Append it to `ads-master/EXPERIMENTS.md` with ICE, design and stop rule.
2. One primary metric. For ecommerce: conversion value at or above target ROAS, or profit. For lead gen: qualified conversions or pipeline value, not raw leads.
3. Size the test. Rough rule for a 50/50 split: each arm needs enough conversions to detect the effect. To detect a 10% difference in conversion volume with reasonable confidence, plan for at least about 300 to 400 conversions per arm; for a 20% difference, about 100 per arm [Practitioner rule of thumb; run a proper power calculation for important tests].
4. Duration: at least 2 full conversion cycles plus the learning period, never under 2 weeks, include full weeks.
5. No changes during the test to either arm (budgets, targets, assets) unless applied to both.
6. Split type for custom experiments: search-based split (each search randomly assigned) gives more data; cookie-based split keeps a user in one arm, better for audience or landing page tests. [Official]
7. Avoid peak seasons unless the test is about the season.
8. Stop rules: stop early only for harm (CPA 50% worse after the learning period with at least 50 conversions per arm) or tracking break.
9. Decide in advance what result leads to which action (adopt, reject, extend).

## 3. Custom experiments (Search and others)

Procedure:
1. Campaigns, Experiments, Create, Custom experiment.
2. Select the base campaign, name with the EXPERIMENTS.md ID (E012_AIMax_RunningShoes).
3. Make the change in the trial arm only.
4. Split 50/50, choose search-based or cookie-based.
5. Enable experiment sync if you want changes to the base to copy to the trial (default on for most). Turn it off if you must keep the arms isolated.
6. Run, monitor weekly for tracking issues only.
7. Read results: Google shows the difference and a confidence indication. Apply only when the primary metric is significant and secondary metrics (CPA, ROAS, lead quality) are acceptable.
8. Apply or end. Applying converts the trial changes into the base campaign or replaces it.

## 4. AI Max experiments

- Built-in experiment type that tests AI Max on vs off for an existing Search campaign. [Official, 2025]
- Use before enabling AI Max on a high spend campaign, and after the September 2026 auto-upgrade to decide whether to keep features on.
- Read: incremental conversions and value, CPA and ROAS in the AI Max arm, the share of AI Max matched terms and their quality.
- Adopt rule: incremental conversions with marginal CPA within 1.2x target, or marginal ROAS within 0.8x target, and no compliance problems in generated copy.

## 5. PMax experiments

- Uplift experiment: holds out PMax for a share of users to measure the incremental conversions PMax adds to the account. Judge on account-level conversions and value.
- Final URL expansion experiment: on vs off.
- Asset experiments: test added videos, new images, seasonal vs evergreen creative [Unverified availability, 2026-10].
- Do not judge PMax by PMax-attributed conversions alone. Brand and remarketing overlap inflate them.

## 6. Conversion Lift and Brand Lift

| Study | Measures | Notes |
|---|---|---|
| Conversion Lift based on users | Incremental conversions from exposed vs holdout users | YouTube, Demand Gen, Display; eligibility depends on budget and expected conversions |
| Conversion Lift based on geography | Incremental conversions by geo holdouts | Works when user-level measurement is limited; needs enough geos |
| Brand Lift | Ad recall, awareness, consideration, favorability, purchase intent via surveys | Video campaigns; minimum spend thresholds apply |
| Search Lift | Increase in brand searches after video exposure | Video campaigns, eligibility rules |

Thresholds: Google lowered the minimum budget for some incrementality studies in 2025 (widely reported at around 5,000 USD using Bayesian methods) [Unverified exact figure]. Check the current thresholds in the Lift measurement setup screen; contact your Google rep if the option is not visible.

Do not run migration tools or copy and paste campaigns that are part of a running lift study (Google's VAC to Demand Gen guidance warns about this) [Official, 2025].

## 7. Geo holdout (DIY) for brand, PMax or YouTube

1. Choose a matched set of regions (states, DMAs, provinces). Use at least 10 to 20 geos per arm for stability, or synthetic control methods.
2. Pre-period: 8 to 12 weeks of daily data to confirm the arms move together (correlation above 0.9 on the KPI).
3. Treatment: turn off (or increase) the channel in test geos only. Keep everything else stable.
4. Duration: 4 to 8 weeks plus a cool-down for lagged conversions.
5. Analysis: difference in differences or synthetic control on backend conversions (not platform conversions).
6. Tools: Meridian GeoX (globally available from 2026-09-10 [Official via trade press]), open-source GeoLift (Meta), or a measurement partner. Hand off design and analysis to measurement.

## 8. Meridian (MMM)

- Google's open-source Bayesian MMM, generally available since 2025-01 [Official, 2025-01]. Repository: github.com/google/meridian.
- Use when: about 2 years of weekly data (at least 18 months), several channels with spend variation, Enterprise or upper Scale tier.
- Calibrate with lift tests (priors from experiments).
- 2026 additions: Meridian GeoX global (2026-09-10) and Meridian Studio, an enterprise MMM product on Google Cloud announced at GML 2026 [Official, 2026-05].
- MMM projects belong to measurement and growth-orchestrator. The google-ads agent supplies clean spend and conversion data by campaign type and consumes the response curves for budget proposals.

## 9. Ad and creative testing inside campaigns

| Method | Use | Read |
|---|---|---|
| RSA asset report | Remove low performing assets | Performance label and conversions per asset after at least 5,000 impressions |
| Two RSAs with different angles | Message test in one ad group | Conversion rate per impression, at least 100 conversions combined |
| Ad variations | Same text change across many ads | Built-in report |
| Demand Gen A/B | Creative or audience test | Built-in report |
| PMax asset groups | Different angles per asset group | Asset group performance, beware different traffic mixes |

## 10. Logging and learning

For each test, append to `ads-master/EXPERIMENTS.md`:
```
| E014 | 2026-10-13 | google-ads | If we enable AI Max search term matching on US_EN_SRCH_NB_Running-Shoes, then conversion value will rise 10% at ROAS >= 350%, because 28% of queries are 6+ words and not covered by keywords | Conversion value at ROAS >= 350% | 7/6/8 | AI Max experiment 50/50 | Stop if ROAS < 250% after 50 conversions per arm | running | | |
```
After the test: update status, result (with numbers and the data source), and the learning. If the learning is confirmed (one valid test or two data points), add it to `ads-master/memory/google-ads.md`.

## 11. Testing roadmap by tier

| Tier | Tests per quarter | Priorities |
|---|---|---|
| Starter | 1 | Bid strategy move (Max clicks to Max conversions), landing page test via cro |
| Growth | 2 to 3 | AI Max experiment, PMax structure test, RSA angle tests |
| Scale | 4 to 6 | PMax uplift, brand incrementality geo test, Demand Gen Conversion Lift, NCA value test |
| Enterprise | 6+ | Full incrementality program, Meridian calibration, market-level holdouts |

## 12. Common experiment mistakes

| Mistake | Consequence | Prevention |
|---|---|---|
| Ending the test after the first good week | False positives | Fix duration and minimum conversions in the stop rule |
| Editing the base campaign mid-test with sync off | Arms diverge for reasons other than the change | Freeze both arms or apply changes to both |
| Judging PMax or AI Max on their own attributed conversions | Counting moved conversions as new | Use account-level totals and experiment arms |
| Testing in peak season, applying in normal season | Result does not transfer | Test in representative periods |
| Primary metric is raw leads | Optimizes toward junk | Use qualified leads or pipeline value |
| Too many simultaneous tests on overlapping traffic | Interference | One test per traffic pool at a time |
| Not logging the result | Repeat failed ideas | EXPERIMENTS.md row closed with result and learning |
| Ignoring conversion lag | Trial arm looks worse because conversions are still arriving | Wait one full lag cycle after the end date before reading |
