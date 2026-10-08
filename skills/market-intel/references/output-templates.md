# Output Templates (market-intel)

Templates for every market-intel deliverable. Save as `ads-master/outputs/market-intel/YYYY-MM-DD_market-intel_<description>.md`.

Standard header and footer for every deliverable:
```
# <Title>
Date: YYYY-MM-DD | Agent: market-intel | Markets: <codes> | Languages: <codes>
## Summary (5 lines max)
## Decision served
<decision> for <owner slug> by <date>
## Data used
| Source | Market | Capture date or range | Confidence |
## What changed since last delivery
```
```
## Recommendations
| # | Observation | Inference | Recommendation | Owner | Expected impact | Test (EXPERIMENTS.md) |
## Proposals for approval (COMPETITORS.md, AUDIENCE.md, BRAND.md edits)
## Handoffs requested
```

## 1. Competitive baseline (`_competitive-baseline.md`)
```
## Competitor set
| Competitor | Type (direct, search, AI, alternative) | Domain | Markets | Threat (H, M, L) | Why |
## Landscape at a glance
| Competitor | Price band | Offer headline | Main channels | Ad activity | Search strength | AI visibility | Review rating (count) |
## Positioning map (axes and placement notes)
## Gaps we can own
## Top 10 recommendations by owner
## Appendix: competitor profile cards
```

## 2. Ad library teardown (`_ad-library-teardown-<competitor>.md`)
```
## Census
| Library | Market | Active ads | New in 30 days | Concepts | Share older than 60 days | Formats |
## Top concepts (by longevity, variants, EU reach)
| Concept | Angle | Format | Hook (verbatim) | Offer | Running days | Variants | EU reach | Landing page |
## Angle and format distribution
| Angle | Count | Share |
## Landing page notes (top 3)
## What they are not saying (gaps vs our VoC)
## Recommendations (creative-strategy, channel agents, cro)
```

## 3. Search competition (`_search-competition.md`)
```
## Auction map (official)
| Competitor domain | Overlap rate | Position above rate | Top of page rate | Outranking share | Trend (8 weeks) |
## Brand bidding
| Competitor | Where seen | Copy | Evidence | Recommended response |
## Paid copy and offers by competitor
## Organic gaps
| Topic or keyword | Volume (source) | Intent | Competitor ranking | Our ranking | AI Overview present | Priority |
## Backlink and SERP feature gaps
## Traffic mix estimates (confidence labeled)
```

## 4. AI visibility benchmark (`_ai-visibility-benchmark.md`)
```
## Method
Prompts: <n> | Engines: <list> | Runs per prompt: <n> | Location and language | Account state | Dates
## Benchmark
| Brand | Mention rate | Recommendation rate | Avg position | Citation share | Sentiment | Accuracy issues |
## By engine
| Engine | Us mention | Top competitor | Top competitor rate |
## By prompt type
| Prompt type | Us | Leader |
## Top cited domains
| Domain | Citations | Type | Our presence | Competitor presence | Action |
## Wrong facts found
| Engine | Prompt | Statement | Correct fact | Source to fix |
```

## 5. Offer and pricing matrix (`_offer-pricing-matrix.md`)
```
## Offer matrix
| Competitor | Product or plan | List price | Effective price | Discount mechanic | Shipping | Financing | Trial | Guarantee | Bonus | Proof | Capture date | URL |
## Price index (hero SKUs or plans)
| SKU or plan | Our price | Median competitor | Index | Flag |
## Promo calendar (last 12 months)
| Competitor | Dates | Depth | Mechanic | Channels |
## Margin impact notes (for growth-orchestrator)
```

## 6. Positioning map (`_positioning-map.md`)
```
## Axes and why buyers use them (VoC evidence)
## Placement
| Brand | Axis 1 value | Axis 2 value | Evidence |
## White space and crowded zones
## Positioning statement check (alternatives, unique attributes, value, best fit, category)
## Messaging comparison
| Element | Us | A | B | Gap |
```

## 7. Voice of customer (`_voc-<segment>.md`)
```
## Sample
| Source | Items | Date range | Market | Our or competitor |
## Themes
| Theme | Code | Mentions | Share | Verbatims (2 to 3) | Segment |
## Language bank (20 to 40 exact phrases)
| Phrase | Theme | Source | Date |
## Competitor weakness map
| Competitor | Top complaints | Share | Verbatim |
## Questions buyers ask
## Proof gaps
```

## 8. Demand (`_demand-<topic>.md`)
```
## Demand size
| Topic | Monthly volume (source, range) | Intent mix | CPC range | AI Overview frequency | Confidence |
## Trend (5 years, 12 months) and rising queries
## Seasonality index
| Period | Index | Moving holiday notes |
## Share of search
| Month | Us | A | B | C |
## Demand by channel
```

## 9. Market sizing (`_market-sizing-<market>.md`)
```
## Definitions
## Method 1: <name> (inputs, sources, dates)
## Method 2: <name>
## Results
| Measure | Low | Base | High |
| TAM | | | |
| SAM | | | |
| SOM (<years>) | | | |
## Reconciliation
## Channel headroom
## Assumptions to validate
```

## 10. Win and loss (`_win-loss-<quarter>.md`)
```
## Sample
| Won | Lost | Interviews | Period | Interviewer |
## Win reasons
| Reason | Count | Share | Verbatim |
## Loss reasons
| Reason | Count | Share | Verbatim | Competitor won |
## CRM loss reasons vs interview reasons
## Battlecard updates
## Recommendations (messaging, offer, product, sales)
```

## 11. Monthly movement summary (`_monthly-movement.md`)
```
## Headline (3 most important changes)
## Ads
## Search and SEO
## AI visibility
## Offers and prices
## Reviews and sentiment
## Demand and share of search
## Company moves
## Alerts this month and outcomes
| Alert | Date | Severity | Action taken | Result |
## Recommended actions
| Action | Owner | Severity | Deadline |
## Proposed COMPETITORS.md edits
```

## 12. Market entry intel (`_market-entry-<geo>.md`)
```
## Market snapshot (size, growth, online share, payments, language)
## Local competitors and international entrants
## Channel landscape (search share, social platforms, marketplaces, AI assistant ads availability)
## Price levels and offer norms
## Demand by channel and seasonality
## Legal and cultural notes (to verify with the growth-orchestrator geo module and counsel)
## Recommendations for growth-orchestrator
```

## 13. Launch intel (`_launch-intel-<product>.md`)
```
## Positioning map for the new product's category
## Price corridor
## Competitor claims and proof
## Demand signals (search, social, marketplaces)
## VoC pains the product solves (verbatims)
## Angles to test first (owner creative-strategy)
## Risks (claims, crowded positions)
```

## 14. Competitor profile card (quarterly, one per competitor)
```
| Field | Content |
| Company, domains, markets | |
| Positioning statement (inferred) | |
| Products and price points | |
| Offer headline | |
| Channel footprint | |
| Ad activity (volume, longevity, angles) | |
| Search footprint | |
| AI visibility | |
| Review profile | |
| Public company signals (funding, hiring) | |
| Recent moves (90 days) | |
| Threat level and why | |
| Counter strategy | |
```

## 15. Writing rules
- Change first, static facts in appendices.
- Every number: source, date, market, confidence.
- Observation, inference, recommendation on separate lines or columns.
- Verbatims exact and anonymized.
- Each recommendation has an owner slug.
