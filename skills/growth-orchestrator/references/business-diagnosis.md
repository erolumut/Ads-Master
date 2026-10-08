# Business Diagnosis

Find the one constraint that limits growth right now, decide which agents to activate, and set the first priorities. A diagnosis is done when you can say: "The binding constraint is X, shown by Y, and the next 30 days are about Z."

## 1. Inputs and data checklist
| Input | Source | Minimum | Ideal |
|-------|--------|---------|-------|
| Business facts | PROJECT_BRIEF.md sections 1 to 5 | Model, offer, AOV, margin, budget | Plus LTV, cohort data, seasonality |
| Revenue truth | Shopify, backend, CRM export | 90 days daily orders or deals | 24 months monthly, new vs returning |
| Spend by channel | Platform exports in data/imports/ | 90 days | 24 months |
| Conversion definitions | MEASUREMENT.md | Primary conversion per channel | Value rules, dedupe keys |
| Funnel data | GA4 or analytics | Sessions, conversion rate by source | Funnel steps by device |
| Market context | COMPETITORS.md, market-intel output | Top 3 competitors | Share of search, AI share of voice |

State in the output: which of these exist, which are missing, and the date range used.

## 2. The six binding constraints
Growth is limited by one of six things at a time. Diagnose in this order because earlier ones invalidate later analysis.

| # | Constraint | Typical evidence | First agents |
|---|-----------|------------------|--------------|
| 1 | Measurement | Platform conversions differ from backend by more than 20%, no server-side events, no consent mode in EU, leads not tied to revenue | measurement |
| 2 | Economics | Contribution margin under about 30% with paid acquisition as main channel, breakeven ROAS above 3.5, LTV to CAC under 1.5, payback longer than cash allows | growth-orchestrator (pricing, AOV, bundles), market-intel (price corridor), cro (AOV levers) |
| 3 | Conversion | Site CVR well under the project's own past or peer range, checkout drop off high, mobile CVR under half of desktop, form completion low | cro, measurement |
| 4 | Creative and offer | CTR and hook rates falling, frequency rising, one or two ads carry the account, no clear offer differentiation | creative-strategy, market-intel |
| 5 | Demand and reach | Impression share high and still volume flat, search volume for category small or falling, audience saturation at current spend | channel agents (new channels), seo, ai-search-optimization, brand investment |
| 6 | Capacity | Cannot fulfil, sales team cannot follow up leads within an hour, no one to produce creative or approve changes | human; the plan must slow down |

Rule: if constraint 1 is present, it is the binding constraint regardless of the others.

## 3. Diagnostic tree
```
Is revenue truth reconciled with platform data within 20%?
  no  -> MEASUREMENT is binding. Activate measurement. Pause scaling advice.
  yes -> Is contribution margin per first order >= acquisition cost (or payback within target)?
          no  -> ECONOMICS is binding. Work AOV, margin, pricing, LTV levers before more spend.
          yes -> Is site or funnel conversion at or above own baseline and peer range?
                  no  -> CONVERSION is binding. Activate cro. Hold budget flat until CVR fixed.
                  yes -> Are CTR, hook rate and frequency healthy, with 3+ winning concepts?
                          no  -> CREATIVE/OFFER is binding. Activate creative-strategy, market-intel.
                          yes -> Does more budget hold marginal CPA under target?
                                  yes -> Under-investment. Scaling plan.
                                  no  -> DEMAND/REACH is binding. New channel test, brand, SEO, AI search.
Throughout: if the team cannot act on output within a week, CAPACITY is binding.
```

## 4. Stage model
| Stage | Signs | Focus | Channel count |
|-------|-------|-------|---------------|
| Pre product market fit | Under ~20 customers per month, high churn or returns, unclear message | Learning: message tests, cheap traffic for signal, customer interviews | 1 |
| Early traction | Repeatable sales from one channel, CAC unknown or volatile | Measurement, unit economics, one channel to profitable scale | 1 to 2 |
| Scaling | CAC known, LTV visible, budget growing monthly | Marginal returns, creative volume, second and third channel, brand starts | 2 to 5 |
| Mature or plateau | Growth under market rate, rising CAC | Incrementality, new markets or products, brand, retention | 4 to 7+ |

## 5. Model specific diagnostics
### Ecommerce
| Metric | How | Red flag |
|--------|-----|----------|
| New vs returning revenue share | Backend | Returning above 70% while acquisition budget rises (paid may be harvesting existing customers) |
| aMER | New customer revenue / total marketing spend | Below first order breakeven ROAS without LTV support |
| 60 to 90 day repeat rate | Cohorts | Under 15% for consumables (weak LTV lever) [Practitioner consensus] |
| Discount dependency | Share of orders with code | Above 50% outside peaks |
| Return rate | Backend | Above category norm; it changes contribution margin |
| Top product concentration | Revenue share of top 5 SKUs | Above 70% concentrates risk in ads and feeds |

### Lead gen and local services
| Metric | How | Red flag |
|--------|-----|----------|
| Lead to SQL rate by channel | CRM | Paid social leads converting at under half of search leads with equal CPL |
| Speed to lead | CRM timestamps | Median over 1 hour |
| Call answer rate | Call tracking | Under 80% in business hours |
| Cost per closed won | CRM + spend | Unknown (no offline conversion import) |
| Spam and duplicate share | CRM | Over 10% of leads |

### B2B SaaS
| Metric | How | Red flag |
|--------|-----|----------|
| Pipeline per $ by channel | CRM opportunity source | Only last touch available |
| Trial or demo to paid | Product + CRM | Falling while volume rises |
| CAC payback | Finance | Over 18 months for SMB motion |
| Net revenue retention | Finance | Under 100% (acquisition fills a leaking bucket) |
| Sales cycle length | CRM | Longer than attribution windows used for bidding |

### App
| Metric | How | Red flag |
|--------|-----|----------|
| D1, D7, D30 retention | MMP or analytics | D7 falling as spend grows |
| Cost per paying user | MMP + store | Rising faster than ARPPU |
| Attribution coverage | SKAN or AdAttributionKit, Android | Large share of unattributed installs |
| Payback on D30 to D90 revenue | Cohorts | Longer than cash runway allows |

### Marketplace or publisher
| Metric | How | Red flag |
|--------|-----|----------|
| Liquidity (share of listings or searches that transact) | Internal | Spending on demand where supply is thin |
| Side constraint | Supply vs demand growth | Spending on the unconstrained side |
| Revenue per visit (publisher) | Analytics + ad server | Paid traffic cost above RPV |

## 6. Quick health score (0 to 5 per area)
| Area | 0 | 3 | 5 |
|------|---|---|---|
| Measurement | No reconciliation | Reconciled monthly, gaps known | Server-side, offline conversions, lift tests |
| Economics | Margin unknown | Breakeven known | Targets by channel from LTV and payback |
| Conversion | No funnel data | Funnel tracked | Testing program with wins |
| Creative | One ad carries spend | Monthly refresh | Weekly concept testing system |
| Demand | One channel, flat | 2 to 3 channels | Brand, search, social and AI visibility growing |
| Operations | Ad hoc | Weekly review | Full heartbeat with priorities and experiments |

Lowest score with the earliest position in section 2 = binding constraint.

## 7. Agent activation from the diagnosis
Use SKILL.md "Agent activation rules", then add diagnosis specific activations:
| Diagnosis | Activate or prioritize |
|-----------|------------------------|
| Measurement binding | measurement (weekly), all paid agents in "protect" mode (no scaling) |
| Economics binding | growth-orchestrator pricing and AOV plan, cro (AOV tests), market-intel (price corridor) |
| Conversion binding | cro weekly, measurement funnel tracking |
| Creative binding | creative-strategy weekly, market-intel monthly ad library review |
| Demand binding | one new channel test, seo, ai-search-optimization, brand budget |

## 8. Diagnosis output (sections)
1. Summary: binding constraint, evidence, next 30 days in 5 lines.
2. Data used and gaps.
3. Unit economics snapshot (contribution margin, breakeven ROAS, nCAC, LTV to CAC, payback).
4. Health score table.
5. Stage and model diagnostics with red flags.
6. Agents to activate and HEARTBEAT.md proposal.
7. First 5 priorities.
8. Delegation plan for the first wave.
9. Questions for the human (only those that change the plan).

## 9. Common diagnostic mistakes
- Treating platform ROAS as profit. It is attributed revenue, often including returning customers and view-through credit.
- Diagnosing creative when the checkout broke. Always check the site and tracking first.
- Using benchmarks before the project's own trend. Benchmarks vary by vertical, geo and season.
- Calling a plateau "saturation" without a budget step test or a response curve.
- Ignoring capacity. A plan the team cannot execute is not a plan.
