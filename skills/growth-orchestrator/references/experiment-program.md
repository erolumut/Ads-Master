# Experiment Program

Run growth as a portfolio of tests: a scored backlog, a steady launch rate, honest designs, and learnings that compound in memory.

## 1. Program metrics
| Metric | Definition | Target logic |
|--------|-----------|--------------|
| Velocity | Experiments launched per month (all agents) | Starter 2 to 4, Growth 4 to 8, Scale 8 to 20, Enterprise 20+ [Practitioner consensus] |
| Completion rate | Concluded / launched | 80%+ (tests that never conclude waste budget) |
| Win rate | Tests that beat control with confidence / concluded | 10% to 30% is common; a much higher rate suggests weak controls or peeking [Practitioner consensus] |
| Learning rate | Concluded tests with a written learning / concluded | 100% |
| Time to decision | Launch to decision, median | Under 4 weeks for in platform tests; 6 to 10 weeks for geo tests |
| Impact shipped | Sum of estimated annualized impact of shipped winners | Reported quarterly |

## 2. Prioritization
### 2.1 ICE (default, fast)
Score 1 to 10 each; ICE = I x C x E (or average; pick one per project and keep it).
| Score | Impact | Confidence | Ease |
|-------|--------|-----------|------|
| 9 to 10 | Moves the North Star by 10%+ | Prior test or strong data in this project | Hours, no dev, no approval chain |
| 6 to 8 | 3% to 10% | Strong external evidence plus some project signal | Days, minor dev |
| 3 to 5 | 1% to 3% | Plausible, mixed evidence | 1 to 2 weeks, dev or creative production |
| 1 to 2 | Under 1% | Opinion | Over 2 weeks, cross team |

### 2.2 RICE (when reach differs a lot between ideas)
RICE = (Reach x Impact x Confidence %) / Effort (person weeks). Reach = users or sessions or spend affected per month. Use for cro and site tests where traffic differs by page.

### 2.3 Portfolio balance
- 60 to 70% of tests in core channels and pages (exploit).
- 20 to 30% adjacent (new audiences, formats, offers).
- 10% big swings (new channel, new pricing, new market).
- At least one incrementality or holdout test per half year on the largest spend line.

## 3. Test design types
| Design | Use when | Tools | Pitfalls |
|--------|---------|-------|----------|
| Platform A/B (split test) | Creative, audience, bidding, landing page within one platform | Meta A/B test, Google Ads Experiments (campaign experiments), TikTok Split Test, LinkedIn A/B test | Measures relative performance within the platform's attribution, not incrementality |
| Conversion lift (holdout at user level) | Is this channel or campaign incremental? | Meta Conversion Lift, Google Conversion Lift, TikTok lift studies (eligibility and minimums apply; verify current thresholds) | Needs enough conversions; platform runs it |
| Geo test (matched markets or synthetic control) | Channel incrementality, budget steps, brand spend, offline effects | GeoLift (open source), Google Meridian geo, custom | Needs geo level sales data and enough regions; contamination across borders |
| Holdout (business level) | Email or SMS flows, retargeting, loyalty | ESP holdout groups, audience exclusions | Keep holdout untouched for the whole window |
| Pre/post with control | When randomization is impossible | Time series models (CausalImpact) | Weakest design; seasonality and other changes confound |
| Site A/B or multivariate | Pages, checkout, forms | Testing tools, server-side flags | Sample ratio mismatch, peeking (cro agent owns) |

## 4. Sample size and duration
### 4.1 Conversion rate tests (two proportions, 95% confidence, 80% power)
```
n per variant ~ 16 x p x (1 - p) / delta^2
p = baseline conversion rate, delta = absolute difference to detect
```
Example: baseline 3% CVR, detect a 20% relative lift (0.6 points): n = 16 x 0.03 x 0.97 / 0.006^2 = about 12,900 visitors per variant.

| Baseline CVR | Relative MDE 10% | 20% | 30% |
|--------------|------------------|-----|-----|
| 1% | ~158,000 | ~39,600 | ~17,600 |
| 3% | ~51,700 | ~12,900 | ~5,700 |
| 5% | ~30,400 | ~7,600 | ~3,400 |
| 10% | ~14,400 | ~3,600 | ~1,600 |
(Approximation; per variant; use a proper calculator for final plans.)

### 4.2 Ad platform CPA tests
- Rule of thumb: about 100 conversions per cell to detect a 20% CPA difference with reasonable confidence; 30 to 50 per cell only detects large differences [Practitioner consensus].
- Duration: at least 7 days to cover weekday cycles; 14 to 28 days typical; avoid peak periods unless testing peak tactics.

### 4.3 Geo tests
- Typical: 4 to 8 weeks treatment, 4+ weeks pre-period, 20+ regions or a synthetic control; budget large enough that the expected effect exceeds noise (run a power analysis in GeoLift before launch).

## 5. Stop rules (write them before launch)
| Rule | Default |
|------|---------|
| Harm stop | Primary metric 30%+ worse than control with at least half the planned sample, or a guardrail broken (tracking, policy, brand) |
| Winner call | Planned sample reached, confidence 95% (or posterior probability 95% in Bayesian tools), effect at or above MDE, no sample ratio mismatch |
| Max duration | 2x planned duration; then conclude "no detectable difference" |
| No peeking decisions | Look daily for harm only; decide at planned sample |

## 6. Experiment lifecycle
1. **Idea**: from diagnosis, VoC, competitors, data, agent findings. Write "If we ..., then ..., because ...".
2. **Score**: ICE or RICE; add to EXPERIMENTS.md as `backlog`.
3. **Design**: use `ads-master/templates/EXPERIMENT_BRIEF.md`: design type, variants, split, primary metric, guardrails, MDE and sample, budget, stop rules.
4. **Approve**: human approves any test that spends money, pauses a channel, or changes the site.
5. **Run**: status `running`; no other changes to the tested entities.
6. **Conclude**: result with confidence; status `won`, `lost` or `inconclusive`.
7. **Learn**: one sentence learning. If it confirms a pattern seen before, propose a memory entry.
8. **Ship or kill**: winners roll out via change request; losers documented so they are not retried without a new reason.

## 7. EXPERIMENTS.md conventions
- IDs: E001, E002 ... sequential across agents.
- Agent column: the slug that owns execution; portfolio tests (channel tests, geo holdouts, budget steps) owned by growth-orchestrator.
- ICE column: "8/6/7" format.
- Status values: backlog, designed, waiting approval, running, won, lost, inconclusive, shipped, killed.
- Each agent updates only its own rows. The orchestrator reviews the whole table weekly and flags rows stuck for 3+ weeks.

## 8. Test ideas by lever (seed list)
| Lever | Test | Typical owner |
|-------|------|---------------|
| Offer | Bundle vs single, free shipping threshold, guarantee framing | cro, market-intel |
| Creative | New concept vs iteration, founder vs UGC, static vs video | creative-strategy |
| Bidding | tROAS vs max conversion value, POAS values vs revenue values | google-ads, meta-ads |
| Structure | Consolidated vs split campaigns | channel agents |
| Channel | New channel at MVB with geo holdout | growth-orchestrator |
| Budget | +20% step with geo control | growth-orchestrator, measurement |
| Landing page | Message match page vs generic | cro |
| Lead quality | Qualifying question vs none; offline conversion bidding | cro, measurement |
| Retention | Post purchase flow vs none (holdout) | other-channels (email and SMS) |
| Brand | Video reach in half the regions | growth-orchestrator, measurement |

## 9. Filled example (EXPERIMENTS.md row and brief summary)
| ID | Date | Agent | Hypothesis | Primary metric | ICE | Design | Stop rule | Status |
|----|------|-------|------------|----------------|-----|--------|-----------|--------|
| E014 | 2026-10-08 | growth-orchestrator | If we add TikTok at $6k per month with 6 native concepts, then new customers rise by 80 per month at an incremental CPA under $55, because TikTok reaches under 30 buyers that Meta frequency data shows we under reach | Incremental new customers (geo split) | 7/5/6 | Geo split: 50% of regions treated, 8 weeks, GeoLift power check first | Stop if CPA over $120 after $6k spend with no improving trend; max 12 weeks | designed |

Brief summary: variants = treatment regions (TikTok on) vs control regions (TikTok off); guardrails = MER and Meta CPA in treatment regions; MDE = 8% lift in new customers in treated regions (power analysis); budget $12k over 8 weeks.

## 10. Statistics notes
- Sample ratio mismatch (SRM): if a planned 50/50 split delivers 52/48 or worse on large samples, check with a chi square test before trusting the result; SRM usually means a bug in assignment or tracking.
- Bayesian tools report "probability to beat control"; treat 95% as the decision bar and still respect the planned sample.
- Multiple variants: each extra variant needs its own sample; with 4 variants, expect roughly 2x the duration of an A/B test to keep power [Practitioner consensus].
- Novelty effects: creative and page tests often fade after launch; confirm winners with a second read 2 to 4 weeks after rollout.

## 11. Incrementality test calendar (half year template)
| Quarter | Test | Channel | Design | Owner | Read date |
|---------|------|---------|--------|-------|-----------|
| Q1 | Conversion lift on largest channel | e.g. Meta | Platform lift study | measurement | week 6 |
| Q1 | Retargeting holdout | All retargeting | Audience holdout 20% | measurement | week 8 |
| Q2 | Budget step with geo control | e.g. Google PMax | Geo split | growth-orchestrator | week 8 |
| Q2 | Brand search holdout (if no competitor bidding) | Google brand | Regions or hours | google-ads | week 4 |

## 12. Common mistakes
- Testing many things at once in one cell, then not knowing what worked.
- Calling winners on small samples (and then failing to replicate).
- Reading platform A/B tests as proof of incrementality.
- Running tests across peak and non peak periods.
- Not recording losers, so the same idea is retried every quarter.
- Changing budgets or creative in the control during the test.
