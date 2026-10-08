# Experimentation Statistics

> Most tests lose or are flat. Optimizely's analysis of about 127,000 experiments found roughly 1 in 8 (12%) won on the primary metric [Study, 2023-12, self-reported customer data]. With win rates that low, sloppy statistics produce mostly false wins. The rules below keep the program honest.

## 1. Test design essentials

| Element | Rule |
|---------|------|
| Hypothesis | "If we [change], then [primary metric] will [direction] for [segment], because [evidence]." From research, not opinion |
| Primary metric (one) | Closest to money that has enough volume: RPV or orders per visitor (ecommerce), qualified leads per visitor (lead gen), activated signups per visitor (SaaS) |
| Guardrail metrics | Must not get worse: AOV, refund or return rate, lead quality (SQL rate), page speed (LCP), error rate, unsubscribe rate |
| Secondary metrics | Explain the result (add to cart, form start). Never declare a winner on a secondary metric |
| Unit of randomization | User (cookie or logged-in ID). Session-level randomization inflates false positives for user-level metrics |
| Targeting | Only visitors who can see the change (trigger on exposure). Diluted tests need far more traffic |
| Allocation | 50/50 for two arms. Unequal splits need more total traffic |
| Duration | Whole weeks (7, 14, 21, 28 days) to cover weekday cycles; at least 2 business cycles for B2B; cap at about 4 to 6 weeks because cookie churn grows |
| Stop rule | Written before launch: fixed sample size, or a sequential method with planned looks |
| Decision rule | Written before launch: ship, iterate, or kill, given each outcome on primary and guardrails |

Every test gets a row in `ads-master/EXPERIMENTS.md` before launch with hypothesis, primary metric, ICE, design and stop rule.

## 2. Sample size, MDE and power

Definitions:
- Baseline (p): current conversion rate of the primary metric for the targeted population.
- MDE (minimum detectable effect): the smallest relative lift you care to detect. Pick it from economics (what lift pays for the change) and from feasibility (what your traffic can detect).
- Alpha: false positive rate if there is no effect (0.05 two-sided is the default).
- Power: chance of detecting the MDE if it is real (0.80 default).

Visitors needed per arm (two-sided alpha 0.05, power 0.80, computed with the normal approximation):

| Baseline CVR | MDE 5% | MDE 10% | MDE 15% | MDE 20% | MDE 30% | MDE 50% |
|--------------|--------|---------|---------|---------|---------|---------|
| 1% | 637,010 | 163,095 | 74,193 | 42,693 | 19,827 | 7,750 |
| 2% | 315,206 | 80,682 | 36,693 | 21,109 | 9,798 | 3,826 |
| 3% | 207,938 | 53,211 | 24,193 | 13,914 | 6,455 | 2,518 |
| 5% | 122,124 | 31,234 | 14,193 | 8,158 | 3,780 | 1,471 |
| 10% | 57,763 | 14,751 | 6,693 | 3,841 | 1,774 | 686 |
| 20% | 25,583 | 6,510 | 2,943 | 1,683 | 772 | 294 |

Rule of thumb (Lehr's rule for proportions): conversions needed per arm is roughly 16 x (1 - p) / MDE squared. For a 10% relative MDE that is about 1,600 conversions per arm at low baselines; for 20% about 400; for 5% about 6,400.

Feasibility check (do this before every test):
```
weeks_needed = (visitors_per_arm x number_of_arms) / weekly_eligible_visitors
If weeks_needed > 6: increase MDE (bolder change), move the test to a higher-traffic page or template, use a higher-volume primary metric with a guardrail on revenue, or do not A/B test (section 10).
```

## 3. Before launch: QA and A/A
1. Functional QA on all target devices and browsers, plus in-app browsers for social traffic.
2. Confirm assignment is sticky (same user sees the same variant across pages and sessions).
3. Confirm exposure event fires once per user per test with `experiment_id` and `variant_id`.
4. Confirm primary and guardrail metrics are recorded for both arms.
5. Check page speed parity (LCP, CLS) between arms.
6. Run an A/A test when adopting a new tool or major implementation change: expect no significant difference and no SRM. Repeated A/A tests should show about 5% "significant" results at alpha 0.05.

## 4. Sample ratio mismatch (SRM)

SRM: the observed split differs from the configured split more than chance allows. It means the assignment or data pipeline is broken and the result cannot be trusted.

- Frequency: about 6% of experiments at Microsoft showed SRM in the KDD 2019 study (Fabijan et al.); LinkedIn reported about 10% of triggered experiments used to suffer SRM [Study, 2019].
- Test: chi-square goodness of fit on visitor counts per arm. Flag when p < 0.001 (some teams use 0.0005).
- Example: 50,000 vs 48,900 visitors on a 50/50 split gives chi-square 12.2, p about 0.0005: SRM. Do not analyze; find the cause.

Common causes (taxonomy from Fabijan et al. 2019):
| Stage | Examples |
|-------|----------|
| Assignment | Bad hashing, changing allocation mid-test, users reassigned after login |
| Execution | Variant redirects lose visitors (redirect tests), variant slower so tracking fires less, bot filtering differs, crashes in one arm |
| Log processing | Bot filters, deduplication bugs, consent mode differences between arms |
| Analysis | Wrong start date, segment filters applied after exposure, triggering condition depends on the treatment |
| Interference | Another test or campaign targets one arm, caching serves one variant more |

Redirect (split URL) tests are especially SRM-prone; prefer same-URL server-side rendering.

## 5. Peeking and stopping rules

Checking a fixed-horizon test daily and stopping at the first p < 0.05 inflates the false positive rate far beyond 5% (to roughly 20% to 30% or more with many looks) [Study, Johari et al. 2017; Evan Miller 2010].

Options:
| Method | How | Use when |
|--------|-----|----------|
| Fixed horizon | Compute sample size, do not decide before it is reached (monitoring for bugs and SRM is fine) | Default, simple |
| Group sequential (alpha spending, O'Brien-Fleming) | Plan 3 to 5 interim looks with stricter thresholds early | Want early stopping for big wins or harm |
| Always-valid sequential (mSPRT, Optimizely Stats Engine, GrowthBook sequential) | Valid at any look; wider intervals | Teams that will peek anyway |
| Bayesian with expected loss threshold | Stop when expected loss of shipping is below a threshold set before launch | Decision-focused teams; not immune to peeking bias [Contested] |

Always stop early for harm: if a guardrail shows a large, significant degradation (or SRM appears), stop and investigate.

## 6. Frequentist vs Bayesian

| Aspect | Frequentist (fixed or sequential) | Bayesian |
|--------|-----------------------------------|----------|
| Output | p-value, confidence interval | Probability to beat control, credible interval, expected loss |
| Interpretation | Harder for stakeholders | Intuitive ("93% chance B is better") |
| Error control | Explicit false positive rate | Depends on prior and decision rule; can be calibrated |
| Peeking | Requires sequential methods | Less sensitive but not immune [Contested] |
| Priors | None | Weak priors by default; informative priors need justification |

Position for this agent: method matters less than discipline. Pre-register the metric, sample size or stopping rule, and decision threshold. Report the effect size with an interval, not only "winner". Vendor defaults differ (for example GrowthBook Bayesian by default with frequentist and sequential options; Optimizely sequential frequentist Stats Engine; VWO Bayesian SmartStats) [Unverified current defaults, check tool docs].

## 7. False positive risk and Twyman's law

False positive risk (FPR): share of "significant" wins that are not real. It depends on the prior win rate (Kohavi, Deng, Vermeer, "A/B Testing Intuition Busters", KDD 2022) [Study, 2022].
```
FPR = (alpha/2 x (1 - prior)) / (alpha/2 x (1 - prior) + power x prior)
```
| Prior win rate | alpha 0.05, power 0.8 | alpha 0.10, power 0.8 |
|----------------|----------------------|----------------------|
| 10% | 22% | 36% |
| 12% | 19% | 31% |
| 20% | 11% | 20% |
| 33% | 6% | 11% |

Kohavi estimated about 37.8% of significant results would be false positives under Optimizely's default settings given its 12% win rate [Practitioner, 2023]. Implications:
- Use alpha 0.05 or lower for important decisions; replicate surprising wins.
- Twyman's law: any result that looks too good (for example +40% on a minor copy change) is probably a bug. Check SRM, tracking, bots and segment anomalies before celebrating.

## 8. Variance reduction (CUPED) and metric choice

CUPED (Controlled-experiment Using Pre-Experiment Data; Deng, Xu, Kohavi, Walker, WSDM 2013) adjusts each user's metric by their pre-experiment value, reducing variance and required sample size [Study, 2013]. Gains are large for returning users with history (logged-in SaaS, repeat buyers), small for new anonymous visitors (no pre-period data), which is most paid traffic.

Supported natively in several platforms (GrowthBook, Statsig, Optimizely and others) [Unverified per vendor, check docs]. Adjustment formula:
```
Y_adj = Y - theta x (X - mean(X)),  theta = cov(X, Y) / var(X)
X = same metric in the pre-period for each user (0 for users with no history)
```

Revenue metrics (RPV, AOV) are heavy-tailed: a few large orders swing results.
- Cap (winsorize) revenue per user at the 99th or 99.5th percentile of the pre-period distribution, decided before launch.
- Use RPV as primary for ecommerce when traffic allows; it captures both CVR and AOV effects. Expect RPV to need more traffic than CVR.
- Report CVR and AOV as diagnostics.

## 9. Multiple comparisons, segments, novelty and interactions

| Issue | Rule |
|-------|------|
| Many variants | Each extra arm adds a comparison. With k variants vs control, use Holm or Bonferroni (alpha / k) or a platform correction. Optimizely reports tests with more variations have higher expected impact, so multi-arm tests are worth it when traffic allows [Study, 2023] |
| Many metrics | One primary metric decides. Use Benjamini-Hochberg for exploratory metric sets |
| Segment slicing | Post hoc segment wins (for example "mobile Safari users in Germany") are hypotheses for a new test, not results. Pre-register up to 2 segments (for example device) if needed |
| Novelty and primacy | Returning users may react to change itself. Plot daily lift; if it decays steadily, extend the test or analyze new users only |
| Winner's curse | Significant estimates are biased upward, especially in underpowered tests. Discount expected impact (for example by 30% to 50%) in forecasts [Practitioner consensus] |
| Concurrent tests | Interactions are usually small; run overlapping tests on different page areas. Make tests mutually exclusive only when they change the same element or flow |
| Seasonality and promos | Avoid launching during major promotions unless the test is about the promotion; results may not generalize |
| Bots and AI agents | Exclude known bots; AI agent traffic is growing (Clarity and others report AI crawler activity). Check for abnormal sessions with zero engagement |

## 10. Low traffic protocol (no A/B test possible)

Decision tree:
```
Weekly conversions on the primary metric per arm >= 100 and test fits in 6 weeks at a useful MDE?
  YES -> A/B test.
  NO  -> Can you test on a higher-traffic template (all PDPs), a higher-volume metric with a revenue guardrail, or a bolder change (MDE 30%+)?
        YES -> A/B test with that design.
        NO  -> Is the change low risk and supported by strong research (usability defect, missing information, broken flow)?
              YES -> Ship it (just do it), monitor with before/after guardrails.
              NO  -> Validate with qualitative methods (5-user tests, five-second tests, preference tests, surveys), then ship with before/after guardrails or hold.
```

Before/after with guardrails protocol:
1. Baseline: collect at least 4 full weeks (8 preferred) of the primary metric and guardrails before the change. Note campaigns, promos, price changes, seasonality.
2. Comparison series: pick an unchanged comparison (other pages, other geo, other product line, or the same weeks last year). This turns a naive before/after into a difference in differences.
3. Ship one change at a time where possible; log the exact date and time in `ads-master/journal/`.
4. Measure 4 weeks after. Compare (after minus before) for changed pages vs comparison series.
5. Decision: keep if the primary metric moved in the expected direction and no guardrail degraded beyond a preset threshold (for example lead quality down more than 10%, AOV down more than 5%). Revert if guardrails break.
6. Label the result as "pre/post, not causal" in EXPERIMENTS.md.

Other low traffic options: geo split (turn on in some regions), time-based switchback (alternate weeks; only for changes without carryover), multi-armed bandit for short-lived promos (optimizes, does not prove), qualitative validation, and pooling learnings across pages.

## 11. Multi-armed bandits
- Use for short-lived decisions where learning does not matter (promo banner, headline during a 2-week sale).
- Do not use for learning or long-term decisions; bandits bias effect estimates and handle delayed conversions poorly.
- Contextual bandits (allocation by segment) are now offered by major platforms (Optimizely released contextual multi-armed bandits in April 2026) [Official, Optimizely release notes 2026-04]. Keep a holdout to measure total impact.

## 12. Analysis checklist (every readout)
1. SRM check passed.
2. Test ran its planned duration or met its sequential stopping rule.
3. Primary metric: effect size, interval, p-value or probability, and practical significance vs MDE.
4. Guardrails: no significant harm.
5. Daily trend: no novelty decay, no anomalies.
6. Segments: pre-registered only; others listed as hypotheses.
7. Sanity: no tracking changes, outages, promo changes mid-test.
8. Decision: ship, iterate, kill. Expected annualized impact with winner's curse discount.
9. Learning: what this says about the customer, written for the next test.
10. Update EXPERIMENTS.md status, result and learning columns; journal entry if other agents should know.

## 13. Calculator script (standard library only)

Save as `ads-master/outputs/cro/abstats.py` only when the human wants a local copy; otherwise run inline.
```python
from math import sqrt, ceil, erfc
from statistics import NormalDist
import random
N = NormalDist()

def sample_size_per_arm(baseline, mde_rel, alpha=0.05, power=0.80):
    p1, p2 = baseline, baseline * (1 + mde_rel)
    za, zb = N.inv_cdf(1 - alpha / 2), N.inv_cdf(power)
    pbar = (p1 + p2) / 2
    num = (za * sqrt(2 * pbar * (1 - pbar)) + zb * sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return ceil(num / (p2 - p1) ** 2)

def srm_check(n_a, n_b, expected_share_a=0.5):
    total = n_a + n_b
    ea, eb = total * expected_share_a, total * (1 - expected_share_a)
    chi2 = (n_a - ea) ** 2 / ea + (n_b - eb) ** 2 / eb
    return chi2, erfc(sqrt(chi2 / 2))          # flag SRM if p < 0.001

def two_prop_ztest(conv_a, n_a, conv_b, n_b):
    pa, pb = conv_a / n_a, conv_b / n_b
    pooled = (conv_a + conv_b) / (n_a + n_b)
    z = (pb - pa) / sqrt(pooled * (1 - pooled) * (1 / n_a + 1 / n_b))
    se = sqrt(pa * (1 - pa) / n_a + pb * (1 - pb) / n_b)
    return (pb - pa) / pa, (pb - pa - 1.96 * se, pb - pa + 1.96 * se), 2 * (1 - N.cdf(abs(z)))

def prob_b_beats_a(conv_a, n_a, conv_b, n_b, draws=200_000, seed=7):
    rng, wins, loss = random.Random(seed), 0, 0.0
    for _ in range(draws):
        a = rng.betavariate(1 + conv_a, 1 + n_a - conv_a)
        b = rng.betavariate(1 + conv_b, 1 + n_b - conv_b)
        wins += b > a
        loss += max(a - b, 0)
    return wins / draws, loss / draws           # P(B>A), expected loss of shipping B

print(sample_size_per_arm(0.03, 0.10))           # 53211
print(srm_check(50_000, 48_900))                 # (12.23..., 0.00047) -> SRM
print(two_prop_ztest(600, 20_000, 680, 20_000))  # (+13.3%, CI of abs diff, p = 0.023)
print(prob_b_beats_a(600, 20_000, 680, 20_000))  # (~0.988, ~7e-06)
```
Outputs above were verified when this module was written. Use the testing platform's stats engine as the system of record; use this script to plan and to sanity check.

## 14. Test plan and readout templates

Test plan (`ads-master/outputs/cro/YYYY-MM-DD_cro_test-plan-<id>.md`):
```
ID (matches EXPERIMENTS.md): | Page or flow: | Owner: cro | Tool:
Hypothesis (If/then/because) with evidence links:
Variants: control | B (describe, link to diff or mockup) | C
Primary metric: | Guardrails (with harm thresholds): | Secondary:
Population and trigger: | Unit: user | Allocation:
Baseline: | MDE: | Alpha: | Power: | Visitors per arm: | Planned duration (whole weeks):
Stopping rule: | Decision rule:
QA checklist done (date): | Launch approval (human, date):
```
Readout (`..._cro_test-readout-<id>.md`): result table per metric with interval, SRM p-value, daily lift chart description, decision, expected annual impact (discounted), learning, next test.
