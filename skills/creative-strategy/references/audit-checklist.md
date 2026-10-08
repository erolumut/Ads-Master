# Creative System Audit Checklist

> Purpose: score the whole creative system (research, strategy, diversity, production, testing, analytics, operations, compliance) and find the weakest stage. Run on onboarding and quarterly. Save as `ads-master/outputs/creative-strategy/YYYY-MM-DD_creative-strategy_creative-audit.md`.

## How to score

Each item: Pass = full points, Partial = half, Fail = 0. Severity sets the points: Critical 5, High 3, Medium 2, Low 1. Record evidence (file, screenshot reference, export and date range) for every item. Items that cannot be verified score 0 and are listed under "Data needed".

## A. Research and insight (max 18)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | A VOC bank with verbatim quotes exists and is under 90 days old | Concepts need real language | `outputs/creative-strategy/*voc-bank*`, `AUDIENCE.md` VOC section | Critical | Run research sprint |
| A2 | At least 3 source types mined (reviews, community, calls or tickets, search) | Avoid one-source bias | VOC bank sources section | High | Add missing sources |
| A3 | Objections are listed with how each is answered in ads | Objections block conversion | VOC bank, live ads mapping | High | Build objection matrix and concepts |
| A4 | Competitor angle map from ad libraries in last 90 days | White space and sophistication stage | Output file or `COMPETITORS.md` | Medium | Ad library review |
| A5 | Post-purchase or onboarding survey running | Ongoing VOC | Ask human, survey tool | Medium | Draft survey |
| A6 | Search query language mined | High intent wording | Search terms export analyzed | Medium | Mine search terms and GSC |
| A7 | Personas documented with awareness levels | Planning grid needs them | `AUDIENCE.md` | Low | Propose AUDIENCE.md updates |

## B. Strategy and concept quality (max 16)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Live concepts cover at least 3 of 5 awareness levels | Broad delivery reaches all levels | Tag live ads by awareness | Critical | Add unaware and problem aware concepts |
| B2 | At least 2 to 3 personas represented in live ads (per main ad set) | Audience pockets | Tag live ads | High | Persona concepts |
| B3 | Each live concept traces to a source | No invented pains | Concept registry | High | Backfill sources or retire |
| B4 | No single angle above 40% of live concepts | Diversity | Tag live ads | Medium | Rebalance slate |
| B5 | Market sophistication stage diagnosed and reflected (mechanism or identity angles in stage 3 to 5 markets) | Generic claims fail in mature markets | Angle map | Medium | Mechanism and identity concepts |
| B6 | Offer and risk reversal stated where price or trust is the top objection | Conversion | Live ads review | Low | Add guarantee or offer framing |

## C. Diversity and Andromeda readiness (max 15)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Last 10 launches: share passing the "new concept" test is at least 40% (or 60%+ when diversity is Low) | Iterations add little reach | Apply test to launch list | Critical | Shift production to concepts |
| C2 | Meta Creative diversity rating is not Low on main ad sets (where shown) | Visual sameness signal | Ads Manager | High | New visual worlds and formats |
| C3 | No concept above 60% of spend for 30+ days without a successor in testing | Concentration risk and fatigue | Concept rollup | High | Adjacent concepts in test |
| C4 | At least 3 distinct on-camera people live (Growth and above) | Talent diversity | Tag ads | Medium | Recruit creators |
| C5 | Advantage+ creative enhancement settings reviewed per ad in last 30 days | Brand and product fidelity | Ad settings review | Medium | Settings review via meta-ads |

## D. Production and formats (max 16)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | 9:16 video exists for every main concept on Meta and TikTok | Reels, Stories, TikTok inventory | Asset list | Critical | Produce 9:16 masters |
| D2 | Hooks shot as separate modules; raw footage retained | Iteration speed | Production folder | High | Modular production |
| D3 | Captions burned in; safe zones respected | Muted viewing, UI overlap | Spot check 10 ads | High | Re-export |
| D4 | Statics and carousels present alongside video | Format diversity, Feed inventory | Live ads | Medium | Static program |
| D5 | YouTube assets pass ABCD check (where YouTube runs) | Google guidance | ABCD review | Medium | Re-cut with brand early, CTA |
| D6 | Google RSA and PMax assets complete and refreshed in 90 days (where Google runs) | Asset strength and freshness | Asset report | Low | Copy refresh with google-ads |

## E. Testing system (max 16)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | A defined testing lane exists (in-situ, test campaign, or Creative Testing tool) | New ads need spend to be read | Account structure via channel agent | Critical | Design lane |
| E2 | Written kill, iterate and scale rules exist | Consistent decisions | Testing doc, EXPERIMENTS.md | High | Adopt rules from testing module |
| E3 | Test budget can read the planned volume (formula) | Underfunded tests teach nothing | Compute concepts_per_week | High | Cut volume or raise test budget |
| E4 | Every test has a hypothesis and stop rule in EXPERIMENTS.md | Learning discipline | EXPERIMENTS.md | Medium | Backfill rows |
| E5 | Winners declared only at evidence ladder thresholds | Avoid false winners | Decision log | Medium | Apply ladder |
| E6 | Graduation of winners validated for 7 days in scaling | Lane transfer risk | Decision log | Low | Add validation step |

## F. Analytics and naming (max 16)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | 90%+ of live ad names parse with the naming regex | Concept rollups need it | Run regex on export | Critical | Rename going forward; map legacy |
| F2 | Concept level report produced weekly | Decisions at concept level | Output files | High | Weekly report template |
| F3 | Hook rate, hold rate, outbound CTR as saved custom metrics | Stage diagnosis | Ads Manager columns | Medium | Create custom metrics |
| F4 | Backend or CRM outcomes joined to ad IDs (utm_content ad ID) | Platform CPA can mislead | MEASUREMENT.md, UTM check | High | Hand off to measurement |
| F5 | Fatigue leading indicators monitored weekly | Act before CPA rises | Report | Medium | Fatigue watch section |
| F6 | Learnings by angle, persona, format recorded | Compounding knowledge | Memory file, tracker | Low | Pattern analysis monthly |

## G. Operations and creators (max 10)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Brief template used for every production | Quality and speed | Recent briefs | High | Adopt templates |
| G2 | Creator registry with usage rights and expiry dates | Legal and continuity | Registry | High | Build registry |
| G3 | Weekly creative cadence (analysis, briefs, launches) running | Velocity | Calendar, outputs | Medium | Install cadence |
| G4 | Production cost per winner tracked | Efficiency | Tracker | Low | Add cost column |
| G5 | Spark codes and partnership permissions tracked with expiry | Winners not cut off | Registry | Low | Track expiry |

## H. Compliance (max 18)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | No AI-generated testimonials or synthetic customers in live ads | FTC rule, trust, policy | Review live ads | Critical | Remove; replace with real proof |
| H2 | All claims on approved list or substantiated | Legal and policy | `BRAND.md`, claims log | Critical | Rewrite or get substantiation |
| H3 | Creator ads disclose material connections in the content | FTC Endorsement Guides | Review creator ads | High | Add disclosure |
| H4 | AI media disclosure approach defined (platform labels, EU deep fake disclosure where relevant) | EU AI Act Article 50, platform rules | Compliance doc | High | Define and apply |
| H5 | Music and stock licensed for ads | Takedowns, claims | License records | Medium | Replace or license |

## Scoring rubric

| Section | Max |
|---------|-----|
| A Research and insight | 18 |
| B Strategy and concept quality | 16 |
| C Diversity and Andromeda readiness | 15 |
| D Production and formats | 16 |
| E Testing system | 16 |
| F Analytics and naming | 16 |
| G Operations and creators | 10 |
| H Compliance | 18 |
| Total | 125 |

Normalize: score % = points / (125 minus points of items marked not applicable) x 100.

| Score | Grade | Meaning | Priority |
|-------|-------|---------|----------|
| 85% to 100% | A | Top tier creative system | Optimize hit rate and cost per winner |
| 70% to 84% | B | Solid, some gaps | Fix the lowest section first |
| 50% to 69% | C | Creative is limiting growth | Research sprint, naming, testing lane within 30 days |
| Under 50% | D | No system | Start with A1, F1, E1, H1 and H2, then rebuild |

Override rule: any failed Critical item in section H blocks new launches until fixed, regardless of total score. Any failed Critical in A, C, E or F makes that section the top priority.

## Audit report structure

1. Summary: score, grade, top 3 issues, expected impact.
2. Data used: exports and date ranges.
3. Section scores table.
4. Findings: each failed or partial item with evidence and fix.
5. 30/60/90 day plan.
6. Change list for approval.
7. Handoffs requested.
