# ASO Audit Checklist (scored)

> Knowledge as of 2026-10. Score every item Pass, Partial or Fail with evidence (screen, export, file and date). An item without evidence is a Fail. Items that do not apply (for example Play items for an iOS only app, tags outside the US) are N/A and leave the denominator. The scoring rubric is at the end; [AI surfaces in the stores](ai-surfaces-in-the-stores.md) section 10 uses the same rubric for its AI surface items, which count as section J here.

Severity weights: Critical 5, High 3, Medium 2, Low 1. Pass earns the full weight, Partial half, Fail 0.

## A. App Store search and metadata (iOS)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | Name, subtitle and keyword field use the budget with no repeated words, no category name, no "app" | Search coverage | App Store Connect, `aso_metadata_check.py` | High | Placement procedure ([App Store](app-store-search-and-metadata.md) section 3) |
| A2 | No competitor names or unowned trademarks in any indexed field | Rejection, takedown | Checker with `--competitors` | Critical | Remove; `paid_only` in term map |
| A3 | Keyword field within 100 characters and bytes for every locale | Silent truncation or rejection | Checker byte warning | Medium | Trim |
| A4 | Every target term coverable across the three fields | Coverage | Checker coverage lines | High | Rework placement |
| A5 | Description is the plain fact sheet: jobs, pricing model, limits, privacy summary; no stuffing; consistent with App entity facts | People and AI readers | Read vs PRODUCT_FACTS App entity | High | Rewrite (section 5) |
| A6 | Primary category matches where the top terms are winnable | Relevance and browse | Category vs term map | Medium | Category change set |
| A7 | Promotional text current (no expired offer) | Trust, consumer law | Product page | Medium | Update (G3) |

## B. Google Play listing

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Title, icon and developer name free of rank, price, promo terms, emoji and all caps | Metadata policy | Checker, visual check | Critical | Rewrite |
| B2 | Short description states the outcome with the second term | Conversion and search | Play Console | High | Rewrite |
| B3 | Full description covers clusters in natural sentences, key text in the top half, no repetition warning | Search, Ask Play | Checker repetition warning | High | Rewrite |
| B4 | Android vitals (crash, ANR) under bad behavior thresholds | Discoverability | Android vitals, 28 days | Critical | App team |
| B5 | Excessive partial wake locks under the threshold | Discovery exclusion risk from 2026-03-01 [Unverified] | Android vitals | High | App team |
| B6 | Target API requirement met | Updates blocked otherwise | Play Console | Critical | App team |

## C. Keyword research and tracking

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | `term_map.csv` exists per spec, updated in the last 30 days, relevance judged by a human | Decisions need a map | File, dates | High | Build it |
| C2 | Ranks tracked for all live and candidate terms per storefront | Reads | ASO tool export | High | Set up tracking |
| C3 | `metadata_changelog.csv` with exact previous text for every change | Reads and rollbacks | File | High | Reconstruct from version history; start now |
| C4 | Last 3 change sets read at day 14 and 28 against control terms | Learning | Change log, journal | Medium | Adopt the protocol |
| C5 | Apple Ads search terms and Play search terms feed the term map | Real query data | Term map sources | Medium | Monthly import |

## D. Store creative and conversion

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Conversion by source at or above own trailing 8 weeks; peer benchmark noted | The multiplier on every source | App Store Connect, Play Console | High | Diagnosis ([Creative](store-creative-and-conversion.md) section 6) |
| D2 | First 3 screenshots show the outcome, differentiator with proof, second job | Search result decision | Visual review | High | Brief and test |
| D3 | Screenshots localized for the top revenue storefronts | Conversion | Visual review per storefront | Medium | Locale waves |
| D4 | Captions under 50 characters, legible at search size, claims approved | Conversion, compliance | Checker, compliance log | Medium | Rewrite |
| D5 | 2026 header and search result assets evaluated (specs checked in the console) | New first impression surface | Asset Library | Low | Brief and PPO |
| D6 | Icon distinct among the top 10 results for core terms | Tap rate | Grid comparison | Medium | Icon test |

## E. Experiments, CPP and CSL

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | A PPO or Play experiment closed in the last 90 days, sized in advance | Learning velocity | EXPERIMENTS.md | Medium | Test calendar |
| E2 | CPP and CSL registry current; every page linked by an ad group, a link or a keyword | Pages without traffic waste effort | `cpp_registry.csv` | Medium | Prune or wire |
| E3 | Keyword linked CPPs only for terms in the keyword space; no competitor brands | Organic visibility, policy | Registry vs keyword field | High | Fix assignments |
| E4 | Play custom store listings for top search clusters and key countries | Conversion | Play Console | Medium | Build |
| E5 | Winners applied to the default page | Value capture | Default page vs results | Medium | Apply (G3) |

## F. Ratings and reviews

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | Prompts use system APIs after success moments, never sentiment gated or incentivized | Policy, law, rating | Code review with the app team | Critical | Fix triggers |
| F2 | Reply coverage 100% of 1 to 2 stars within 72 hours; urgent themes within 24 | Trust, rating updates | `review_themes.py` replies section | High | Reply process |
| F3 | `review_themes.py` run weekly; rising negative themes routed | Early warning, summaries | Journal | High | Weekly loop |
| F4 | Review summary text (Apple, Play) recorded monthly and compared with themes | Visible to every visitor | Memory history | Medium | Monthly capture |
| F5 | Rating 4.0 or higher on core storefronts, no 0.2 drop in the last 7 days | Conversion | Store consoles | High | Rating crisis play |

## G. Featuring, events and promotional content

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Event and promotional content calendar for the next quarter | Discovery, reactivation | Calendar | Medium | Plan |
| G2 | Nominations submitted at least 3 weeks ahead (6 to 8 for launches) | Editorial consideration | App Store Connect | Medium | Calendar |
| G3 | Every event has a deep link and a read after it ends | Value of the tap | Event settings, journal | Medium | Fix |

## H. Localization

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | Locales match market scores; top markets at L3 or higher | Reach | Locale list vs score table | Medium | Waves |
| H2 | Native keyword research per locale, not translation | Relevance | Term map per locale | High | Research |
| H3 | Cross-localization assumptions verified with a canary term | Wasted keyword space | Memory record | Low | Canary test |

## I. Compliance

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | Every claim in store text and assets has a CLAIMS.md ID and a compliance verdict | Rejection, law | Compliance log | Critical | Review |
| I2 | Pricing and "free" wording matches the paywall in every market | Consumer law | Paywall vs listing | High | Fix |
| I3 | No text addressed to AI systems, no hidden text | Manipulation | Read all fields | Critical | Remove |
| I4 | Change requests with approvals exist for the last 5 submissions | Control | Journal, actions log | High | Enforce |

## J. AI surfaces readiness

Score the items in [AI surfaces in the stores](ai-surfaces-in-the-stores.md) section 10 (tags against the term map, summaries against themes, Ask Play answers against the fact sheet) and, when the app team is engaged, the checklist in [On-device assistants](on-device-assistants.md). Add their weighted totals to this audit as section J.

## Audit report template

```
# ASO audit: <app>, <stores and storefronts>, <date>
Data used: <exports and connectors, date ranges>; Freshness check: <date>
Tier and maturity: <tier>, <new, running, plateau, scaling>
Score: <overall %>, grade <A to F>; section scores A to J
Critical fails (first)
Top 5 fixes (impact x confidence x ease)
Findings by section (item, result, evidence, fix)
Quick wins (under 1 week)
30, 60, 90 day plan
Change requests (G3 lines)
Handoffs requested
Data gaps and [Unverified] items
```

## Quick audit (30 minutes, cold start)

With store access and one export only, score these first and list the rest as data gaps: A2, A5, B1, B4, D1, D2, F1, F2, F5, I1.

## Evidence log template

| Item | Result | Evidence (file, screen, report) | Date range | Notes |
|------|--------|----------------------------------|-----------|-------|
| D1 | Partial | App Store Connect sources export: search conversion 31% vs 34% 8 week median | 2026-09-14 to 2026-10-11 | Browse share up during featuring |

## Scoring example

Section F with F1 (Critical 5, Pass), F2 (High 3, Partial), F3 (High 3, Fail), F5 (High 3, Pass), F4 N/A: earned = 5 + 1.5 + 0 + 3 = 9.5; possible = 5 + 3 + 3 + 3 = 14; section score 68%.

## Scoring rubric

1. Section score = sum of earned weights / sum of possible weights for applicable items (Pass = weight, Partial = half, Fail = 0).
2. Overall score = sum of earned weights across all sections / sum of possible weights (sections count by their items; no extra section weights).
3. Grades:

| Overall | Grade | Meaning |
|---------|-------|---------|
| 90% to 100% | A | Top tier store presence; focus on tests, new markets and AI surfaces |
| 75% to 89% | B | Solid; fix High items within 30 days |
| 60% to 74% | C | Leaking organic growth; fix Critical and High items before new markets |
| 40% to 59% | D | Foundations missing (term map, change log, compliance); fix before any test |
| under 40% | F | Rebuild: metadata, creative, ratings process |

4. Override: any Critical item at Fail caps the grade at C and goes first in the report, whatever the total.
