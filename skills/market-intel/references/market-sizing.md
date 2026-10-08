# Market Sizing

Size the opportunity (TAM, SAM, SOM) with both top down and bottom up methods, reconcile them, and translate the result into channel headroom the growth-orchestrator can plan against.

All numbers in the worked examples are illustrative inputs to show the method. Replace every input with a sourced figure and record source and date.

## 1. Definitions
| Term | Definition | Question it answers |
|------|-----------|---------------------|
| TAM (total addressable market) | Total annual revenue if every potential customer bought the category at typical price | How big could this category be? |
| SAM (serviceable addressable market) | The part of TAM we can serve with our product, price band, geography, language and channels | How much can our current offer realistically address? |
| SOM (serviceable obtainable market) | The share of SAM we can win in a set period given competition, budget and capacity | What is a credible revenue target? |

## 2. Methods
| Method | How | Best for | Risk |
|--------|-----|----------|------|
| Top down | Start from published category spend, narrow by segment, geography, channel | Mature categories with published data | Inflated by broad definitions; secondary sources often recycle numbers |
| Bottom up | Count buyers x purchase frequency x price | B2B, local, new categories | Count errors; frequency assumptions |
| Value theory | Value created per customer x share captured x customers | New categories without spend data | Highly assumption driven |
| Demand based (search and platform reach) | Search volumes and platform audience sizes converted to buyers | Digital first businesses | Captures only digital demand; zero click effects |
Use at least two methods; if they differ by more than 2x, explain why before using either.

## 3. Worked example: B2B SaaS (bottom up)
Product: scheduling software for dental clinics in one country. Illustrative inputs:
| Input | Value | Source to use |
|-------|-------|---------------|
| Dental clinics in country | 40,000 | Statistical office business counts, professional association |
| Fit filter (2+ chairs, digital records) | 60% | Survey, association data, sample of LinkedIn or directory listings |
| Annual contract value | $2,400 | Our pricing |
| Realistic 3 year share of SAM | 5% | Win rate and sales capacity |

- TAM = 40,000 x $2,400 = $96.0 million per year.
- SAM = 40,000 x 0.60 x $2,400 = $57.6 million per year (24,000 accounts).
- SOM (3 years) = 24,000 x 0.05 = 1,200 clinics, $2.88 million ARR.
- Capacity check: 4 sales reps x 10 closed deals per month x 36 months = 1,440 deals, so 1,200 is feasible; marketing must produce 1,200 / win rate opportunities (at 25% win rate, 4,800 opportunities over 3 years, about 133 per month).

## 4. Worked example: DTC ecommerce (top down plus demand check)
Illustrative inputs:
| Input | Value | Source to use |
|-------|-------|---------------|
| Category retail sales in country | $2.0 billion | Statistical office, industry association, company filings |
| Online share of category | 30% | Ecommerce reports (for Turkey: Ministry of Trade ecommerce data) |
| Our price segment share (premium) | 25% | Price corridor analysis, retailer assortment |
| 3 year obtainable share of SAM | 2% | Competitor benchmarks, budget |

- TAM (online) = 2.0 billion x 0.30 = $600 million.
- SAM = 600 million x 0.25 = $150 million.
- SOM = 150 million x 0.02 = $3.0 million per year by year 3.

Demand check (search only): category keywords 400,000 searches per month x 3% click share to our site (paid plus organic) x 2.5% conversion rate x $60 AOV = $18,000 per month, about $216,000 per year. Search alone covers about 7% of the SOM, so the plan needs demand creation channels (social, creators, marketplaces) and repeat purchase. Hand to growth-orchestrator.

## 5. Worked example: local services (bottom up with capacity)
Illustrative inputs: 1.2 million households in the metro, 15% need the service per year, average job $350, service area covers 50% of households, capacity 6 vans x 4 jobs per day x 250 working days.
- TAM = 1,200,000 x 0.15 x $350 = $63.0 million per year (180,000 jobs).
- SAM = $63.0 million x 0.50 = $31.5 million.
- Capacity = 6 x 4 x 250 = 6,000 jobs = $2.1 million per year, about 6.7% of SAM.
- Insight: growth is capacity limited before it is demand limited; marketing should optimize job value and booking rate, and the business should plan capacity before raising budget.

## 6. From market size to channel headroom
| Channel | Headroom signal | Where to find it |
|---------|-----------------|------------------|
| Google Search | Search impression share lost to budget and rank; Keyword Planner volume for uncovered topics | Google Ads, Keyword Planner |
| Shopping and PMax | Impression share; Merchant Center market insights | Google Ads, Merchant Center |
| Meta | Estimated audience size and reach for the target geo and age band; frequency at current spend | Ads Manager estimates (ranges) |
| TikTok, Snapchat, Pinterest | Audience estimates in ad tools | Platform planners |
| LinkedIn | Audience counts for ICP (industry, seniority, company size) | Campaign Manager |
| YouTube and CTV | Reach Planner forecasts | Google Ads Reach Planner |
| AI assistants | Prompt coverage and mention rates (no official volumes) | AI visibility benchmark |
Rule: if planned frequency at the proposed budget exceeds about 3 to 5 per week in the core audience on social channels, headroom is limited without new audiences or creative [Practitioner consensus].

## 7. Data sources by market
| Market | Business and household data | Company data |
|--------|-----------------------------|--------------|
| US | Census Bureau (County Business Patterns, Economic Census), BLS Consumer Expenditure Survey | SEC EDGAR filings |
| EU | Eurostat structural business statistics, national statistical offices | National registries |
| UK | ONS | Companies House |
| Turkey | TÜİK, Ministry of Trade ecommerce statistics (eticaret.gov.tr), sector associations | KAP (Public Disclosure Platform) for listed companies |
| Gulf | National statistics offices (for example GASTAT in Saudi Arabia) | Exchange filings |
| Any | Industry associations, analyst reports (paywalled; cite the original), B2B databases for account counts (LinkedIn Sales Navigator, Crunchbase and similar) | Funding and headcount signals |
Statista and similar aggregators: use only to find the original source; cite the original.

## 8. Sanity checks
- Is SOM achievable with the budget? SOM revenue / expected nCAC x AOV relationship must fit the budget envelope (growth-orchestrator).
- Do the top leaders' revenues (public filings) add up to a plausible share of the TAM?
- Do top down and bottom up differ by more than 2x? Explain.
- Are definitions consistent (B2B vs B2C, online vs offline, gross vs net)?
- Are currencies and inflation handled (real terms for Turkey and other high inflation markets)?

## 9. Output: market sizing
1. Summary and decision served (for example market entry, budget ceiling, investor narrative).
2. Definitions used.
3. Method 1 and method 2 with inputs, sources, dates and confidence.
4. TAM, SAM, SOM table with ranges (low, base, high).
5. Reconciliation of methods.
6. Channel headroom summary.
7. Assumptions to validate and how (survey, test campaign, interviews).

## 10. Pitfalls
- One number without a range.
- TAM from a press release with no method.
- Ignoring capacity and cash constraints in SOM.
- Using search volume as the whole market for categories bought offline or through marketplaces.
- Mixing currencies or years.

## 11. Ranges and sensitivity (always present low, base, high)
| Input | Low | Base | High | Why the range |
|-------|-----|------|------|---------------|
| Number of buyers | minus 20% | source value | +10% | Counting method and definitions |
| Adoption or fit share | minus 15 points | estimate | +10 points | Survey uncertainty |
| Price or ACV | discounted price | list price | list price + add ons | Mix and discounts |
| Purchase frequency | minus 25% | estimate | +15% | Behavior variability |
Show which input moves SOM the most; validate that input first (survey, test campaign, sales data).

## 12. Survey based sizing (when no data exists)
1. Survey a representative sample of the target population (panel providers) with screening questions for need, current solution, spend and willingness to pay.
2. Incidence = share who have the need; spend = reported annual spend (cap outliers).
3. TAM = population x incidence x average spend; apply a stated vs actual discount (people overstate intent; a 30% to 50% haircut on purchase intent is common practice) [Practitioner consensus].
4. Report confidence intervals from the sample size.

## 13. Test campaign sizing (digital first)
Run a small paid test (with growth-orchestrator approval) to measure click through and conversion on a landing page for the new segment; combine with platform audience size: obtainable customers ~ reachable audience x expected reach share x CTR x CVR. Use as a lower bound for SOM in the segment.
