# Testing Frameworks and Volume

> Purpose: design creative tests that reach a decision with the budget available, set kill and scale rules, and size production volume to what can actually be read. Channel agents implement campaigns; this module defines what is tested, how much it needs and how it is judged.

## 1. Test types

| Test type | Question | Variable | Hold constant | When |
|-----------|----------|----------|---------------|------|
| Concept test | Which ideas work? | Persona, angle, concept | Offer, landing page | Always the first priority when no winner or diversity is Low |
| Hook test | Which opening wins on a proven body? | First 1 to 3 seconds | Body, CTA | After a concept wins |
| Body test | Which argument or proof converts? | Middle section | Hook, CTA | After hooks plateau |
| Format test | Does the concept travel? | Format (UGC, static, carousel, founder) | Angle | To extend a winning angle |
| Talent test | Does a different face open new pockets? | Creator | Script | Scale tier, to extend winners |
| Offer test | Which offer converts? | Discount, bundle, guarantee | Creative | Coordinate with `growth-orchestrator` and `cro` (affects margin) |
| Length test | 15 vs 30 vs 60s | Length | Concept | When hold curves suggest drop off |
| Landing page test | Does message match lift CVR? | LP variant | Ad | Hand off to `cro` |

One test, one variable family. Concept tests vary concepts. If a concept test also varies offers, you cannot attribute the result.

## 2. Testing lanes (pick per channel and tier)

| Lane | How it works | Pros | Cons | Use when |
|------|-------------|------|------|----------|
| A. In-situ | Launch new ads directly into the scaling ad set or Advantage+ campaign | Real auction conditions, no extra structure | New ads often starved by incumbents; slow reads | Starter; or when new ads reliably get spend |
| B. Dedicated testing campaign | Separate campaign, one ad set per concept (equal budgets) or one ad set with concepts | Forces spend, cleaner concept reads | Results may not transfer to the scaling campaign; extra cost; more structure | Growth and Scale when in-situ starves new ads |
| C. Meta Creative Testing tool | Inside an existing campaign: Meta copies an ad into 2 to 5 variants, splits spend evenly, each person sees one version; set a test budget (Meta suggests up to about 20% of budget) and duration up to 30 days; Highest volume bid strategy only; lifetime budgets unsupported at launch but later observed working; results in Experiments [Practitioner reports of Meta docs, 2025-10 to 2026-01, verify limits] | Even spend split in the real campaign; built in | Few variants per test; settings limits; winner not guaranteed to get spend afterwards | Growth and above, for concept or hook tests in Sales or Leads campaigns |
| D. Meta A/B test (Experiments) | Split audiences between campaign or ad set versions | Clean causal read | Needs budget and time | Big strategic questions (founder vs UGC as a creative strategy) |
| E. TikTok split test or test ad groups | TikTok Ads Manager split test, or ad group per concept | Clean on TikTok | Budget heavy for small accounts | Growth and above on TikTok |
| F. Google assets and Demand Gen | Asset level performance in PMax and Demand Gen; Demand Gen supports A/B experiments; YouTube Brand Lift for brand | Native | Asset reports are directional; limited control | Feed Google with new asset sets; test Demand Gen creative with experiments |
| G. LinkedIn A/B testing | Campaign Manager A/B test for creative | Clean | Expensive clicks | B2B concept tests with clear hypotheses |
| H. Lift or holdout | Conversion lift, geo holdout | Incrementality | Cost, time | Enterprise; hand off to `measurement` |

## 3. Test budget sizing

**Rule of thumb for a CPA read:** each concept needs spend of at least 2 to 3 times target CPA before a kill decision on conversions, and conversions in the range of the evidence ladder (section 5) before a "winner" decision. [Practitioner consensus]

**Formula: how many concepts can we read per week?**

```
concepts_per_week = weekly_test_budget / (target_CPA x k x executions_per_concept)
k = 2 for a kill-or-continue read, 3 to 5 for a winner read
```

Example: Growth tier, $15k/month Meta, test lane 20% = $3,000/month, about $700/week. Target CPA $35. Executions per concept = 2. Kill read k = 2: 700 / (35 x 2 x 2) = 5 concepts per week can get a kill read. Winner reads need more: graduate only the best 1 to 2 for more spend.

If target CPA is high (B2B SaaS at $400 per SQL), CPA reads are not affordable for many concepts. Use the proxy ladder: hook rate, hold rate, CTR, cost per landing page view, cost per lead (any lead), then qualified pipeline on the few concepts that pass. Document which proxy is used and why.

**Share of spend on testing (planning ranges):**

| Tier | Test spend share | Notes |
|------|------------------|-------|
| Starter | 0% to 20% (often in-situ only) | Prioritize fewer, very different concepts |
| Growth | 10% to 20% | Test lane or Creative Testing tool |
| Scale | 10% to 25% | Always on test lane, weekly launches |
| Enterprise | 10% to 20% plus lift studies | Per market or product pods |

These are planning heuristics [Practitioner consensus]. Final allocation is a `growth-orchestrator` decision.

## 4. Kill, iterate, scale rules (defaults; tune to account history)

Compute percentiles from the account's own last 90 days of ads with at least 5,000 impressions, per placement group.

| Signal at read point | Decision |
|----------------------|----------|
| Spend at or above 2x target CPA, 0 conversions, and CTR below account median | Kill |
| Spend at or above 3x target CPA, CPA above 1.5x target | Kill (unless lead quality data says otherwise) |
| Hook rate bottom quartile after 5,000+ impressions | Kill the execution; keep the concept if the angle has evidence; re-hook |
| Hook rate top half, hold rate bottom quartile | Iterate body: pacing, payoff by second 8 |
| Hook and hold fine, CTR bottom quartile | Iterate CTA, offer clarity, end card |
| CTR top half, CVR bottom quartile | Send to `cro` with LP; test message matched LP; do not kill the concept yet |
| CPA at or below target with evidence ladder met | Winner: graduate to scaling, start iteration ladder |
| CPA within 10% to 30% above target, strong upstream metrics | Near miss: iterate hook and offer framing, retest |

Do not judge before 3 to 7 days unless the kill thresholds are clearly met: delivery systems ramp, and early days are noisy. Avoid editing ads during the read (edits can reset learning).

## 5. Evidence ladder (statistical sanity)

Creative tests are almost always underpowered on CPA. Be honest about it.

**How many conversions to detect a CPA difference?** For two ads with equal spend, the log of the conversion count ratio has variance of about 1/c1 + 1/c2. At 95% confidence and 80% power, conversions needed per ad are approximately:

| True CPA difference | Conversions per ad (approx.) |
|---------------------|------------------------------|
| 2x (one ad half the CPA) | about 33 |
| 1.5x | about 95 |
| 1.3x | about 230 |
| 1.2x | about 470 |

Derivation: c = 2 x ((1.96 + 0.84) / ln(ratio))^2. Implication: most creative tests can only detect big differences. Big differences come from concepts, not iterations. That is another reason to test concepts first.

**Ladder of confidence for declaring a winner:**

| Level | Requirement | Use |
|-------|------------|-----|
| Signal | Upstream metrics top quartile (hook, hold, CTR) with 5,000+ impressions | Keep running, give it budget |
| Directional winner | CPA at or below target with 10 to 20 conversions | Graduate with monitoring |
| Confident winner | CPA at or below target with 30+ conversions, stable over 2 weeks | Build iteration ladder, invest in production |
| Proven | Wins across 2+ executions or re-tests, or in a lift test | Write to memory |

**Proportions (CTR, CVR) confidence interval (Wilson):**

```
p_hat = x / n, z = 1.96
center = (p_hat + z^2/(2n)) / (1 + z^2/n)
half = z * sqrt(p_hat*(1-p_hat)/n + z^2/(4n^2)) / (1 + z^2/n)
CI = center +/- half
```

If two ads' CVR intervals overlap heavily, you do not have a winner.

**Multiple comparisons:** testing 10 concepts at once means one will look best by chance. Require the winner to beat the account baseline (not just the other test ads) and to hold for a second week.

**Novelty effect:** new ads sometimes perform well in week 1 and decay. Judge winners on at least 7 to 14 days.

**Python helper (run with `python3 -I`):**

```python
import math
def wilson(x, n, z=1.96):
    if n == 0: return (0, 0)
    p = x / n
    d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d
    h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return (c-h, c+h)

def cpa_ratio_ci(conv_a, spend_a, conv_b, spend_b, z=1.96):
    # ratio of conversion rates per dollar (b vs a); >1 means B is cheaper per conversion
    if min(conv_a, conv_b) == 0: return None
    r = (conv_b/spend_b) / (conv_a/spend_a)
    se = math.sqrt(1/conv_a + 1/conv_b)
    return (r*math.exp(-z*se), r, r*math.exp(z*se))

print(wilson(42, 3100))
print(cpa_ratio_ci(18, 900, 31, 950))
```

Reading the example: 31 vs 18 conversions at similar spend looks like B is 63% more efficient, but the 95% interval runs from about 0.91 to 2.92. That is a directional winner, not a confident one.

## 6. Iteration ladder (after a winner)

| Rung | What changes | Count | Expected |
|------|-------------|-------|----------|
| 1 | Hooks (visual, text, verbal) on the same body | 3 to 5 | Extends life, finds better opener |
| 2 | First frame and thumbnail | 2 to 3 | Lifts hook rate |
| 3 | Body: different proof, objection or demo | 2 to 3 | Lifts CVR |
| 4 | Length cuts | 2 | Placement fit |
| 5 | Format translation (video to static, carousel) | 1 to 3 | New placements, partly new pockets |
| 6 | New talent reading the same script | 2 to 3 | New audience pockets (moves toward a new concept) |
| 7 | New persona with the same angle | 1 to 2 | This is a new concept; log it as one |

Rungs 1 to 4 are iterations (low diversity value). Rungs 6 and 7 move toward new concepts.

## 7. Production mix: concepts vs iterations

| Situation | New concepts share of production | Iterations share |
|-----------|-------------------------------|-----------------|
| No current winner | 80% to 100% | 0% to 20% |
| Diversity rating Low or 1 concept takes over 60% of spend | 60% to 80% | 20% to 40% |
| Healthy: 3+ winning concepts, diversity Medium or High | 30% to 50% | 50% to 70% |
| Peak season (protect winners, refresh hooks) | 20% to 30% | 70% to 80% |

[Practitioner consensus, adapted to Andromeda era guidance]

## 8. Volume by tier (planning)

| Tier | New concepts per month | Total new ads per month (concepts x executions + iterations) | Launch cadence |
|------|----------------------|----------------------------------------------------------|----------------|
| Starter | 2 to 4 | 4 to 10 | Every 2 weeks |
| Growth | 4 to 12 | 10 to 40 | Weekly |
| Scale | 12 to 40 | 40 to 150 | Weekly, two launch days |
| Enterprise | 40 to 150+ | 150 to 600+ | Continuous, per market |

Cap volume by what the test budget can read (section 3). Launching 50 ads that each get $20 teaches nothing.

## 9. Graduation mechanics (inputs for channel agents)

- On Meta, graduate the winning ad using the existing post (same post ID) so social proof carries over, where the setup allows.
- Graduate to the scaling ad set with the iteration ladder queued, not alone.
- Watch the graduated ad for 7 days: performance in scaling often differs from the test lane. If it fails, keep it in the test lane learnings, not in memory.
- On TikTok, Spark Ads keep engagement on the original post; graduate the Spark post.

## 10. EXPERIMENTS.md row template

```
| E0xx | 2026-10-08 | creative-strategy | If we launch 5 new unaware and problem aware concepts for runners and parents, then new customer CPA falls 15%, because live ads only cover product aware buyers | New customer CPA (backend) | 7/5/6 | Concept test, Meta Creative Testing tool, 5 ads, 20% budget, 14 days | Kill per rules at 2x CPA with 0 conv; winner at CPA <= target with 15+ conv | running | | |
```

## 11. Common testing mistakes

| Mistake | Fix |
|---------|-----|
| Testing 10 hook variants of one concept as if they were 10 concepts | Concepts first; hooks after a winner |
| Calling winners on 3 conversions | Evidence ladder |
| Changing offer and creative at once | One variable family |
| Killing high CTR, low CVR ads | Send to `cro`; test LP match |
| Editing ads mid read | Duplicate instead, after the read |
| Using a test campaign whose winners never transfer | Validate graduation for 7 days; consider in-situ or the Creative Testing tool |
| Tests with no stop rule | Every EXPERIMENTS.md row has a stop rule |
