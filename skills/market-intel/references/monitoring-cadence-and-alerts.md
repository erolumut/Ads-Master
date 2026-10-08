# Monitoring Cadence and Alerts

What to watch, how often, which thresholds trigger an alert, and how alerts become actions. Good monitoring is quiet most of the time and loud when it matters.

## 1. Monitoring matrix
| Signal | Source | Starter | Growth | Scale | Enterprise | Owner of response |
|--------|--------|---------|--------|-------|------------|-------------------|
| Competitor ad volume and new concepts | Meta Ad Library, TikTok, LinkedIn, Google Transparency Center | Quarterly | Monthly | Weekly | Weekly + API (EU) | creative-strategy |
| Auction entrants and overlap | Google and Microsoft Auction Insights | Monthly | Biweekly | Weekly | Weekly | google-ads, microsoft-ads |
| Brand bidding | Auction Insights (brand campaign), SERP checks | Monthly | Weekly | Weekly | Daily automated | google-ads |
| Prices and promotions | Manual capture, Merchant Center, trackers | Quarterly | Monthly (weekly in peaks) | Weekly (daily in peaks) | Daily | growth-orchestrator, cro |
| Offers and pricing pages | Page change monitor | Quarterly | Monthly | Daily alerts | Daily alerts | growth-orchestrator |
| Organic rankings on money keywords | Rank tracker, GSC | Monthly | Weekly | Weekly | Daily | seo |
| AI visibility (prompts) | AI visibility tool or manual panel | Quarterly | Monthly | Monthly (weekly priority prompts) | Weekly | ai-search-optimization |
| Reviews and ratings (ours and theirs) | Review sites, app stores, marketplaces | Quarterly | Monthly | Weekly | Weekly | growth-orchestrator, cro |
| Share of search | Google Trends, Keyword Planner | Quarterly | Monthly | Monthly | Monthly | growth-orchestrator |
| Social and community mentions | Listening tool, Reddit | Quarterly | Monthly | Weekly | Daily | creative-strategy |
| Company moves (funding, hiring, launches, leadership) | News alerts, press pages, job boards | Quarterly | Quarterly | Monthly | Monthly | growth-orchestrator |
| Category demand | Google Trends, Keyword Planner | Quarterly | Monthly | Monthly | Monthly | growth-orchestrator |

## 2. Alert thresholds (defaults; tune per project and record in memory once confirmed)
| Alert | Threshold | Severity |
|-------|-----------|----------|
| New auction competitor | Overlap rate above 10% on a core campaign, not seen in the prior 4 weeks | High |
| Competitor aggression | Position above rate +10 points week over week on core terms | Medium |
| Brand bidding detected | Any competitor or reseller in brand Auction Insights or SERP checks | High |
| Competitor creative surge | New ads in 7 days more than 2x their 4 week average | Medium |
| Competitor promo | Discount of 20% or more, or new free shipping or guarantee | High in peaks, Medium otherwise |
| Price undercut | Competitor effective price on a hero SKU more than 10% below ours | High |
| Pricing page change | Any change in plans, prices or packaging (SaaS) | High |
| Ranking loss | Money keyword drops out of top 3, or 5+ money keywords drop 3+ positions in a week | High |
| AI visibility drop | Mention or recommendation rate down 10 points on priority prompts vs last period | Medium |
| New AI competitor | A brand not in COMPETITORS.md appears in 20%+ of answers | Medium |
| Review rating shift | Our average drops 0.2 points in 30 days, or a competitor gains 0.3 | Medium |
| Negative review spike | 1 to 2 star reviews more than 2x the 4 week average | High |
| Share of search change | Our share down 2 points over a quarter | Medium |
| Market entry | Competitor ads appearing in a new market we serve | Medium |

## 3. Alert to action workflow
1. Detect (scheduled check or tool alert).
2. Verify within 24 hours (second source, screenshot, capture date).
3. Write a journal entry tagged `alert`: what changed, evidence, likely impact, recommended response, owner slug.
4. If severity is High, flag it in the next daily or weekly review and add a "Handoffs requested" line for the owner agent.
5. Log the outcome (what was done, did it matter) to tune thresholds; if an alert type leads to no action three times in a row, loosen or remove it.

Alert journal template:
```
# Alert: <competitor> <what changed>
Date: YYYY-MM-DD HH:MM | Agent: market-intel | Tags: alert
## What happened
- <observation with source, URL, capture date>
## Why it matters
- <inference and expected impact on our KPIs>
## Data (source and date range)
- <evidence>
## Action items
- [ ] <response> (owner: <slug>)
## Related files
```

## 4. Tooling options
| Need | Options | Notes |
|------|---------|-------|
| Page changes (pricing, offers) | Visualping, Distill, ChangeTower and similar | Respect robots rules and site terms; low frequency checks |
| Rankings | Semrush or Ahrefs position tracking, other rank trackers | Fix location and device |
| Auction data | Google Ads and Microsoft Ads reports or API (via connectors) | Official |
| Ad libraries | Manual saved searches; Meta Ad Library API for EU delivered ads; licensed third party ad intelligence tools | Check terms for any scraping based tool |
| Mentions | Google Alerts, listening tools | |
| AI visibility | AI visibility platforms or manual panel | Same prompts every period |
| Reviews | Platform notifications for own profiles; manual checks for competitors; licensed review data tools | |
| Scheduling | `/loop` in a session, Claude Code Routines or scheduled triggers, CI jobs that run a headless check and commit outputs | Human chooses; agents never change accounts |

## 5. Monthly movement summary (the main recurring deliverable)
Sections:
1. Headline: the 3 most important competitor or market changes this month.
2. Ads: per competitor new concepts, volume change, notable angles and offers (with links).
3. Search: auction changes, brand bidding, ranking movements, AI Overview changes.
4. AI visibility: mention and recommendation rates vs last month, new competitors in answers, cited sources.
5. Offers and prices: changes, promo calendar update, price index.
6. Reviews and sentiment: ratings, new themes.
7. Demand: category trend, share of search.
8. Company moves: launches, funding, hiring, partnerships.
9. Recommended actions by owner, with severity.
10. Proposed edits to COMPETITORS.md.

## 6. Peak period mode
Four weeks before and during BFCM, Ramadan, 11.11 or the category's peak:
- Prices and promotions: daily capture for hero SKUs.
- Ad libraries: twice weekly for top 3 competitors.
- Auction Insights: daily on core campaigns.
- Alerts go straight to the daily check (ads-review daily) for the affected channel agents.

## 7. Pitfalls
- Monitoring everything, acting on nothing.
- Alerts without capture dates and evidence.
- Thresholds never tuned, so the team stops reading alerts.
- Automated collection that breaks platform terms.
- Treating a single day's change as a trend outside peak periods.

## 8. Monitoring plan template (store as an output and refresh quarterly)
```
# Monitoring plan: <project>, <quarter>
| Signal | Competitors or terms | Source or tool | Frequency | Threshold | Alert owner | Response owner |
|--------|----------------------|----------------|-----------|-----------|-------------|----------------|
| Brand bidding | brand terms list | Auction Insights, SERP checks (3 cities, mobile and desktop) | weekly | any new competitor | market-intel | google-ads |
| Hero SKU prices | 10 SKUs x 4 competitors | manual capture or tracker | weekly (daily in peaks) | 10% undercut | market-intel | growth-orchestrator |
| Pricing pages | 5 competitor URLs | page monitor | daily | any change | market-intel | growth-orchestrator |
| Ad volume | top 5 competitors | Meta Ad Library, TikTok, LinkedIn | monthly | 2x new ads vs 4 week average | market-intel | creative-strategy |
| AI visibility | 40 prompts | AI visibility tool | monthly | minus 10 points | market-intel | ai-search-optimization |
Peak mode dates: <start> to <end>
```

## 9. Example: one month of alerts and outcomes (illustrative, not real data)
| Date | Alert | Severity | Action | Outcome | Threshold change |
|------|-------|----------|--------|---------|------------------|
| 2026-09-03 | New competitor in brand Auction Insights (overlap 14%) | High | Brand campaign impression share raised; trademark ad text complaint filed | Overlap fell to 4% in 2 weeks | none |
| 2026-09-10 | Competitor A new ads 3x average | Medium | Teardown; 2 new angles found | Angles briefed to creative-strategy | none |
| 2026-09-17 | Competitor B pricing page change | High | Plan comparison updated | No conversion impact | none |
| 2026-09-24 | Review rating dip 0.1 | Low | No action | Recovered | raise threshold to 0.2 (already default) |
Use the outcome column to prune alerts that never lead to action.

## 10. Scheduling safely
- Scheduled checks only read data and write journal entries and outputs; they never change accounts.
- Keep API keys in the environment or a secrets manager, never in `ads-master/`.
- Rate limit automated checks (at most daily for page monitors, weekly for most others).
- A failed scheduled check writes a journal entry tagged `alert` with the failure reason, so silence is never mistaken for "no change".
