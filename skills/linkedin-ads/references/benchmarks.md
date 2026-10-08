# Benchmarks

> Rule: compare the project with its own history first, with its own CRM economics second, and with external benchmarks last. LinkedIn benchmarks vary widely by region, industry, seniority targeted, audience size, format and season. Every number below carries source, date and caveat. Numbers marked [Unverified] could not be re-checked during the 2026-10 build and are planning placeholders until replaced by account data or a re-verified source.

## 1. Strategic research figures (stable, widely cited)

| Figure | Value | Source | Date | Caveat |
|--------|-------|--------|------|--------|
| Share of B2B buyers in market per quarter | About 5% (95% out of market) | John Dawes, Ehrenberg-Bass, for the LinkedIn B2B Institute | 2021 | Depends on purchase cycle; compute your own (see [B2B strategy](b2b-strategy-playbooks.md)) [Study, 2021] |
| Brand vs activation guidance in B2B | Substantial brand share, indicative near half | Binet and Field, "The 5 Principles of Growth in B2B Marketing", LinkedIn B2B Institute | 2019 | Based on effectiveness award entries; category and stage dependent [Study, 2019] |
| Buying group size | 6 to 10 stakeholders | Gartner research, widely cited | Various | Varies by deal size and industry [Study] |

## 2. Platform performance ranges (planning placeholders)

| Metric | Range used for planning | Basis | Label |
|--------|------------------------|-------|-------|
| Sponsored Content CTR (single image, feed) | About 0.4% to 0.7% | LinkedIn guidance as commonly quoted and practitioner reports | [Unverified] |
| Video view rate and completion | Highly format and length dependent | No reliable cross account figure confirmed | [Unverified] |
| Lead gen form completion rate (opens to submits) | Often cited around 10% to 15% | LinkedIn marketing materials and practitioner reports | [Unverified] |
| CPC, North America, Sponsored Content | Often $5 to $15, higher for senior roles and narrow ABM | Practitioner reports | [Practitioner consensus] [Unverified] |
| CPM, North America | Often $30 to $100+ | Practitioner reports | [Practitioner consensus] [Unverified] |
| CPL with lead gen forms | Often $50 to $250+ depending on offer and seniority | Practitioner reports | [Practitioner consensus] [Unverified] |
| Thought Leader Ads vs company page ads | Higher engagement and lower cost per engagement reported | LinkedIn statements and practitioner tests | [Practitioner consensus] [Unverified] for magnitude |
| Conversation and message ads open rates | Historically high open rates claimed | LinkedIn materials | [Unverified]; judge on cost per qualified lead |

Do not set targets from section 2. Set targets from economics (section 4) and account history.

## 3. Benchmark studies to re-verify before quoting
| Source type | What it offers | How to use |
|------------|----------------|-----------|
| LinkedIn Marketing Solutions benchmark and B2B Institute publications | Platform averages, effectiveness research | Quote with date and note platform authorship |
| B2B attribution vendors' LinkedIn benchmark reports (for example Dreamdata and similar) | Cross account CPC, CTR and pipeline influence with disclosed samples | Check sample size, industries, date, attribution method |
| Agency benchmark reports | CPC, CPL by industry | Check sample and recency; often small samples |
| Analyst research (Gartner, Forrester) | Buying behavior, committee size | Strategic, not tactical |

## 4. Economics based targets (preferred over benchmarks)
```
max cost per SQL   = first year gross profit x SQL to won rate x payback share
max CPL            = max cost per SQL x lead to SQL rate
max CPC            = max CPL x landing page or form conversion rate
max CPM            = max CPC x CTR x 1000
```
Worked example: first year gross profit $30,000, SQL to won 20%, payback share 40% gives max cost per SQL $2,400. Lead to SQL 15% gives max CPL $360. Form completion from click 12% gives max CPC $43. At 0.5% CTR, max CPM about $216. If actual CPMs in the ICP are $60, the channel has room; if CPMs are $250, fix CTR and conversion first. Illustrative only.

## 5. Internal baselines to build
| Baseline | How | Use |
|----------|-----|-----|
| CTR by format and audience type | 90 days, ad level | Creative screening |
| CPM by audience type (ABM, ICP cold, retargeting) | 90 days | Bid and budget planning |
| Form completion by form and offer | 90 days | Form design |
| Lead to SQL by campaign, offer, audience code | 180 days CRM | Quality |
| Cost per SQL and pipeline per dollar by program | Quarterly | Budget allocation |
| ICP match % (Demographics) | Monthly | Targeting quality |
| Company list match rate | Per upload | ABM quality |
| Time to opportunity from first LinkedIn touch | 12 months CRM | Patience for demand creation |

## 6. Benchmark hygiene
1. Every external figure in a deliverable shows source, date, sample and caveat.
2. Figures older than 24 months are context only.
3. Platform authored figures are labeled as such.
4. Compare like for like: same region, seniority, format and objective.
5. Report ranges when results per segment are under 100.
6. When the account differs from a benchmark, explain with account facts (audience size, seniority, offer, creative).
7. Replace each placeholder in section 2 with account data within 60 days and log the replacement in the journal.

## 7. Quick significance check for CTR or conversion rate tests
```python
from math import sqrt
def z(conv_a, n_a, conv_b, n_b):
    pa, pb = conv_a / n_a, conv_b / n_b
    p = (conv_a + conv_b) / (n_a + n_b)
    return (pa-pb) / sqrt(p * (1-p) * (1/n_a + 1/n_b))
# CTR test: 60 clicks of 10,000 impressions vs 40 of 10,000
print(round(z(60, 10000, 40, 10000), 2))  # about 2.0, borderline at 95%
```
Use cost per qualified result for final decisions; CTR significance only screens creative.
