# Research Dossier: Meta Ads (Facebook, Instagram, Threads, WhatsApp, Messenger, Audience Network)

Compiled: 2026-10-08. Owner slug: meta-ads.

Method and limitations: web search across official Meta pages, regulators, SEC filings, trade press and practitioner sources, with every claim tagged by evidence label. Constraints during this build: direct page fetching was blocked by the network environment, and the shared web search budget for the session was exhausted after 18 extended searches (the brief asked for 35+). Official claims were therefore confirmed through multiple independent reports of the same announcement where possible; anything resting on a single secondary source is labeled [Unverified]. Long-standing platform mechanics (learning phase, breakdown effect, auction formula, dedup rules) come from Meta Help Center documentation known before this build and are labeled [Official, long-standing]; they should be re-read during the first Freshness check. A follow-up research pass is recommended for items in "Open questions".

## 1. Executive summary

1. Meta's ad stack is now three layers: Andromeda retrieval (2024-12) narrows tens of millions of ads to a few thousand per request, Lattice ranking models predict outcomes across objectives and surfaces, and GEM (detailed 2025-11) is a foundation model whose knowledge is distilled into the ranking fleet. Meta credited GEM with about +5% conversions on Instagram and +3% on Facebook Feed in Q2 2025 [Official].
2. Because retrieval works on learned representations of the ad itself, creative diversity is the main targeting lever. Practitioners report that similar ads are grouped under one entity, so near-duplicate variations add little reach [Practitioner consensus].
3. Advantage+ is the default for Sales, App and Leads. Advantage+ shopping became Advantage+ sales in early 2025, the API moved to a unified structure in 2025 with legacy ASC and AAC creation phased out across v24 and v25, and the UI build paths were merged around February 2026 with creative enhancements pre-selected [Official for API; Unverified for UI details].
4. Measurement changed twice in 2026: on 2026-01-12 the Ads Insights API stopped returning 7-day view and 28-day view windows; on 2026-03-03 click-through attribution became link-click-only, with other interactions moved to a 1-day engage-through window and the engaged-view video threshold lowered to 5 seconds [Official via trade coverage]. Vendors report reported-conversion drops of 15 to 40% in some accounts [Unverified].
5. Incremental attribution (launched in Ads Manager in 2025) lets advertisers optimize and report on modeled incremental conversions; Meta reported a 46% lift in its tests, while independent reads are mixed (Haus: 43% win rate vs standard in early tests) [Official; Study].
6. Placement control is shrinking: reports from August to September 2026 say ad set level placement exclusions are being removed in many accounts, with placement value rules (down to minus 90%) as the alternative and account-level placement controls as the only true block. No Meta announcement was found as of mid September 2026 [Contested].
7. New inventory: Threads ads opened to all users globally from 2026-01-21 (gradual rollout), with image, video, carousel and Advantage+ catalog formats in the Threads feed; WhatsApp Status ads and Promoted Channels (announced 2025-06-16) were reported rolling out globally from February 2026, with the EU lagging [Official].
8. Signal and privacy: Meta uses Meta AI chat interactions for ad personalization from 2025-12-16 (outside the EU, UK and South Korea at launch); EU users can choose less personalized ads from January 2026 after the DMA decision (EUR 200 million fine in April 2025), and Meta's 2026 filings call that option "less relevant and effective"; health and wellness advertisers lost lower funnel event sharing in tiers from January 2025 [Official].
9. Meta's stated direction is end-to-end automation: a 2025-06 WSJ report described a goal of AI creating, targeting and budgeting ads by the end of 2026, and 2026 product releases (AI reporting, creative generation, Creator Marketing Hub) follow that path [Official statements via press; 2026 items Unverified].
10. Top operators adapt by owning what automation cannot: clean first-party signal (CAPI, CRM stages, values), a high-volume diverse creative pipeline, unit economics-based targets, and a standing incrementality program, while keeping structure simple and edits infrequent [Practitioner consensus].

## 2. State of the channel in 2026

| Dimension | State | Evidence |
|-----------|-------|----------|
| Auction pricing | Ad impressions +11% and average price per ad +9% YoY in Q2 2025; +14% and +10% in Q3 2025 | Meta earnings releases [Official, 2025-07 and 2025-10] |
| Automation | Advantage+ is the default for Sales, App and Leads; audience inputs are suggestions; enhancements pre-selected | Jon Loomer (2025-02), PPC Land (2025), AdNabu (2026) |
| Delivery engine | Andromeda retrieval, Lattice ranking, GEM foundation model, continued model consolidation (about 100 ranking models retired since 2023, about 200 more planned, per earnings commentary) | Meta Engineering (2024-12, 2025-11); secondary summaries [Unverified for counts] |
| Inventory | Facebook, Instagram (Feed, Stories, Reels, Explore, search), Messenger, Audience Network, Threads feed (global since 2026-01), WhatsApp Status and Promoted Channels (global rollout from 2026-02) | CNBC, TechCrunch (2026-01-21); WABetaInfo, BetaNews (2026-02) |
| Threads scale | Over 400 million monthly users reported in 2025; a 500 million figure for mid June 2026 appears in one guide | [Unverified for 500 million] |
| Measurement | 7-day click plus 1-day view default; engage-through 1 day since March 2026; view windows above 1 day removed from the API since January 2026; incremental attribution model available | Trade coverage of Meta announcements [Official, 2026] |
| Regulation | EU DMA less personalized ads option (from 2026-01), EU ban on political and social issue ads (from 2025-10, TTPA), AI chat signals outside EU, UK, South Korea | European Commission (2025-12-08), Meta newsroom, EPIC, Visualping |
| Restricted verticals | Health and wellness data restrictions (Core setup, restricted standard events, full restrictions) since 2025; financial products and services special ad category | Triple Whale, Foley Hoag (2025-01), Twigeo (2025-04), Curve Compliance |
| Creator economy | Partnership ads mainstream; Creator Marketing Hub reported 2026-09-15; Instagram live partnership ads reported from 2026-09-29 | [Unverified, 2026-09] |

### 2.1 How delivery works now and what it implies

| Stage | System | Implication for operators |
|-------|--------|---------------------------|
| Eligibility | Hard controls (location, minimum age, language, custom audience exclusions), policy, special ad category limits | The only targeting that is absolute in Advantage+ audience |
| Retrieval | Andromeda: deep retrieval model on NVIDIA Grace Hopper and MTIA, tens of millions of ads narrowed to a few thousand per request, model complexity up 10,000x [Official, 2024-12] | Creative content decides which users an ad is retrieved for; diverse concepts open new pockets; near-duplicates share an entity [Practitioner consensus] |
| Ranking | Lattice unified ranking across objectives and surfaces; GEM trained on thousands of GPUs, knowledge transferred via distillation and other post-training methods [Official, 2025-11] | Fragmented accounts do not get "their own model"; they only dilute signal |
| Auction | Total value = bid x estimated action rate + ad quality [Official, long-standing] | Signal quality and creative quality are bidding inputs |
| Calibration and serving | Secondary sources describe UTIS calibration and an adaptive ranking runtime [Unverified] | Watch Meta Engineering posts for confirmation |

Third-party descriptions of Andromeda efficiency gains conflict (one cites 100x faster feature extraction with 3x inference throughput, another 10x inference efficiency); only the recall and quality figures were consistent with Meta's post [Contested].

### 2.2 Automation roadmap and how operators adapt

- Direction: Meta leadership has described a future where the advertiser states a goal and budget and Meta's AI handles creative, targeting and optimization; a June 2025 WSJ report put an end-of-2026 target on full automation of ad creation and targeting [Official statements reported by press, 2025-06].
- 2025 to 2026 steps that fit the roadmap: Advantage+ default for Sales, App and Leads; creative enhancements pre-selected; generative backgrounds, image expansion, video generation from images, text variations, translations; AI reporting connections; creator discovery with AI [Official and Unverified mix, see timeline].
- What remains with the operator: business inputs (offer, price, margin, LTV), signal (CAPI, values, CRM stages), creative raw material and brand guardrails, legal controls, budget level, measurement truth and experiments.
- Adaptation plays: (1) move effort from targeting to signal and creative pipelines; (2) treat every automation toggle as a hypothesis to test with A/B tests rather than a default to reject or accept; (3) keep brand and claims guardrails written down so generative features can be reviewed quickly; (4) shift reporting from platform ROAS to business outcomes and incrementality.

### 2.3 Measurement shifts in 2026

| Change | Before | After | What breaks |
|--------|--------|-------|-------------|
| Insights API view windows (2026-01-12) | 7d_view and 28d_view queryable | Empty data for those windows; historical re-pulls not possible | BI pipelines, year-over-year comparisons of view-through |
| Click-through definition (2026-03-03) | Any click (likes, comments, profile taps, expansions) could earn click-through credit | Only link clicks earn click-through; other interactions go to engage-through (1 day); engaged-view threshold 5s instead of 10s | Click-only reports drop; social-heavy creatives look worse in click columns |
| Incremental attribution (2025) | Standard attribution only | Standard or incremental model per ad set | Reported conversions lower by design under incremental; stakeholder education needed |
Operator response: annotate reports on both dates, rebuild pipelines, compare backend year over year instead of platform conversions, and run lift tests to set targets.

### 2.4 Regional notes

| Region | Note | Label |
|--------|------|-------|
| EU | Less personalized ads choice since 2026-01 after DMA non-compliance decision (EUR 200 million fine, April 2025); Commission monitoring uptake; Meta says the option is less effective | [Official] |
| EU | No political, electoral or social issue ads from October 2025 (TTPA) | [Official] |
| EU | WhatsApp ads delayed (Irish DPC), rolling in later than other regions | [Official via press] |
| EU, UK, South Korea | AI chat signals for ads not applied at launch | [Official, 2025-10] |
| Turkey | Location fee for ads delivered to Turkey reported at 5% from 2025 alongside other DST countries; VAT handling depends on business tax setup; KVKK consent and transfer rules; platform access risk (Instagram blocked about 9 days in August 2024, Threads suspended April 2024) | [Unverified for fee and VAT; Official news for 2024 blocks] |
| Turkey | Messaging-first behavior makes click to WhatsApp and Instagram Direct strong lead paths | [Practitioner consensus] |

## 3. Timeline of changes, January 2025 to October 2026

| Date | Change | Source | Label |
|------|--------|--------|-------|
| 2025-01 | Health and wellness data restrictions begin (lower funnel events, URL parameters) | Foley Hoag, Triple Whale | [Official] |
| 2025-01 | "Credit" special ad category broadened to financial products and services | Meta Help Center (pre-build knowledge) | [Unverified exact scope] |
| 2025 (early) | Detailed targeting exclusions removed | Secondary 2026 guides | [Unverified exact date] |
| 2025-02 | Advantage+ shopping renamed Advantage+ sales; streamlined creation test with Advantage+ on by default for Sales, App, Leads | Jon Loomer, Meta business page | [Official] |
| 2025-04 | Threads ads opened to advertisers globally (low delivery) | PPC Land, Social Media Today | [Official] |
| 2025 (H1) | Incremental attribution reaches Ads Manager; Meta reports 46% lift in tests | Jon Loomer, Social Media Today, Birch | [Official] |
| 2025-05-29 | Marketing API unified Advantage+ structure announced | PPC Land | [Official] |
| 2025-06 (early) | WSJ reports Meta aims to fully automate ad creation and targeting by end of 2026 | WSJ via secondary | [Official statement reported by press] |
| 2025-06-16 | WhatsApp Updates tab: Status ads, Promoted Channels, channel subscriptions announced | Meta Newsroom | [Official] |
| 2025-07 | Meta says it will stop political, electoral and social issue ads in the EU from October 2025 (TTPA) | Meta announcement (pre-build knowledge) | [Official] |
| 2025-07-01 | WhatsApp Business Platform per-message pricing | Meta (pre-build knowledge) | [Official] |
| 2025-07 to 2025-10 | Q2 and Q3 2025 earnings: GEM, Lattice and Andromeda credited for conversion gains | Earnings releases, Meta Engineering | [Official] |
| 2025-08-15 | Threads video ads (1.91:1 to 9:16) | Secondary guides | [Unverified exact date] |
| 2025-09 | Click to message ads in WhatsApp Status | Secondary guides | [Unverified] |
| 2025-10 | Creative testing tool in Ads Manager (2 to 5 ads, even split) | AdManage, Revel (2025-10-17), Jon Loomer | [Official via practitioners] |
| 2025-10 | Threads image carousel ads | Secondary guide | [Unverified] |
| 2025-10-01 to 10-07 | Privacy policy notice: Meta AI interactions to personalize ads from 2025-12-16 | EPIC, Visualping | [Official] |
| 2025-10-16 | Developer blog notice of attribution window removal in Insights API | Seresa, Dataslayer | [Official via secondary] |
| 2025-11-10 | GEM engineering post | Meta Engineering | [Official] |
| 2025-12-08 | European Commission acknowledges Meta commitment to less personalized ads choice from January 2026 | European Commission | [Official] |
| 2025-12-16 | AI chat signals used for ad personalization (not EU, UK, South Korea) | PPC Land, EPIC | [Official] |
| 2026-01 | EU less personalized ads choice rolls out | European Commission, Meta 10-Q | [Official] |
| 2026-01-12 | Insights API stops returning 7d_view and 28d_view windows | Dataslayer, Seresa, PPC Land | [Official via secondary] |
| 2026-01-21 | Threads ads rolling out to all users worldwide | CNBC, TechCrunch | [Official] |
| 2026-02 | WhatsApp Promoted Channels and Status ads rolling out globally | WABetaInfo, BetaNews | [Official via press] |
| 2026-02 | Unified Advantage+ creation flow; all creative enhancements pre-selected for new Sales, Leads, App campaigns | AdNabu, 1ClickReport | [Unverified] |
| 2026-02-13 | Developer announcement on automation-first setup (single secondary source) | Secondary guide | [Unverified] |
| 2026-03 | Control to cap existing customer budget share (single source) | Secondary guide | [Unverified] |
| 2026-03-03 | Link-click-only click-through attribution; engage-through 1 day; engaged-view 5s | Leafsignal, Mintec, Digital Applied, Good Morning Co | [Official via trade coverage] |
| 2026-04 | Updated incremental attribution model, 25% average increase (single source) | Secondary guide | [Unverified] |
| 2026-04 to 05 | IAB NewFronts: Reels trending ads, creator discovery tools, Threads video ads | ALM Corp | [Unverified details] |
| 2026-07 | Instagram Explore and Messenger Stories removed as selectable placements | Secondary guides | [Unverified] |
| 2026-07 | Q2 2026 10-Q repeats that EU less personalized ads are "less relevant and effective" | SEC EDGAR, Cittago | [Official] |
| 2026-08 | WhatsApp campaign management inside Ads Manager, Status placement (single source) | Secondary guide | [Unverified] |
| 2026-08-03 | GEM training infrastructure follow-up (MFU 20 to 25%, training FLOPs 4x in 12 months) | AI wiki citing Meta | [Unverified] |
| 2026-08-21 to 08-25 | Ad set placement exclusions removed in many accounts; value rules suggested | Jon Loomer, Common Thread Collective, AdRise Lab, Blackfire | [Contested] |
| 2026-09 | Creative Diversity rating in Ads Manager; Meta AI recurring reports into Google Workspace; click to WhatsApp 7-day free window | AdsUploader, Franklin Marketing, Good Morning Co | [Unverified] |
| 2026-09-15 | Creator Marketing Hub (Creator Marketplace plus Partnership Ads Hub) | AdsUploader | [Unverified] |
| 2026-09-16 | California synthetic performer disclosure law signed | AdsUploader | [Unverified details] |
| 2026-09-22 | Threads ads no longer require matching Instagram username; Meta status page Ads Delivery incident | Melissa newsletter, AdsUploader | [Unverified] |
| 2026-09-29 | Instagram live video partnership ads generally available | AdsUploader | [Unverified] |

## 4. Best practice consensus

| Area | Consensus | Label |
|------|-----------|-------|
| Structure | Consolidate into few campaigns and ad sets; split only for different events, economics, geos, legal categories or tests | [Practitioner consensus] aligned with Meta Performance 5 guidance |
| Automation | Advantage+ audience, placements and campaign budget on by default; hard controls for legal must-haves | [Official recommendation] |
| Creative | Concept diversity (persona, motivator, format, messenger) over micro-variants; weekly new concepts scaled to spend | [Practitioner consensus] backed by Andromeda design |
| Signal | Pixel plus CAPI with dedup, high EMQ, values, CRM stages for lead gen | [Official] |
| Learning | About 50 optimization events per ad set per week; batch significant edits | [Official, long-standing] |
| Bidding | Highest volume to start; value optimization when values vary and volume allows; cost per result goal or ROAS goal for controlled scale | [Official behaviors, practitioner thresholds] |
| Measurement | Triangulate platform, backend (MER, new customer CAC) and incrementality tests | [Practitioner consensus] |
| Lead gen | Higher intent forms, qualifying questions, conversion leads optimization with CRM feedback, fast follow-up | [Official plus practitioner] |
| Breakdowns | Do not exclude segments based on breakdown CPA (breakdown effect) | [Official] |

## 5. Contested topics

| Topic | Side A | Side B | Working stance |
|-------|--------|--------|----------------|
| Full Advantage+ vs manual control | Automation wins on liquidity and learning; manual setups underperform at most budgets | Manual controls protect brand, regulated targeting and lead quality; Advantage+ over-serves existing customers and cheap placements | Advantage+ on by default; turn off a lever only with a documented reason; validate with A/B tests and backend |
| Testing in separate campaigns vs in the scaling ad set | Separate tests give fair spend and clean reads | Tests outside the main auction context do not predict scaling performance and cost learning | Use the creative testing tool when available; BAU testing at Starter |
| Incremental attribution | Meta reports 46% lift; aligns delivery with causal value | Haus early tests show a 43% win rate; fewer reported conversions confuse stakeholders; tracking gaps bias it | Test via A/B on mature accounts, judge on backend |
| Engage-through window | Fixed 1-day window (Mintec) | Toggleable (Seresa) | Check the account's attribution settings |
| Placement exclusions removal | Announced on 2026-08-21 (one source) | Observed from 2026-08-25 without announcement; Help Center still described manual placements as of 2026-09-17 | Treat as rolling account-level change; use account-level controls for hard blocks |
| Health category workarounds | Custom events with different names keep optimization | Renaming restricted events violates policy | Do not rename; appeal misclassification; adapt plan |
| Value of lookalikes and interests | Still useful as suggestions for new accounts | Irrelevant after learning; noise | Use only as early suggestions |
| Frequency thresholds | Hard caps (e.g. 3) prevent fatigue | Frequency alone is not a problem without CTR and CPA decline | Use frequency with trend signals |
| Retargeting budgets | Retargeting has the best ROAS | Retargeting is the most over-credited spend | Keep 5 to 15% unless a holdout proves more |

## 6. What top operators do differently

1. Treat creative as a production system: weekly concept quotas by spend tier, a concept registry, coverage grids across personas and motivators, and creator partnerships with usage rights.
2. Invest in signal engineering: CAPI with high EMQ, profit-aware values where approved, CRM stage events, offline sales, messaging outcomes.
3. Run fewer, larger ad sets and change them less often; batch edits weekly.
4. Use cost per result goals or ROAS goals with budgets far above expected spend at Scale, letting spend follow efficiency.
5. Calibrate targets with incrementality factors from lift and geo tests, and report MER and new customer CAC next to platform ROAS.
6. Watch existing customer share and use new customer controls when growth is the goal.
7. Date-check every anomaly against platform changes before reacting.
8. Keep account health as infrastructure: verified business, 2FA, backup payment, clean policy history.

## 7. Common expensive mistakes

| Mistake | Typical cost | Fix |
|---------|-------------|-----|
| Optimizing lead gen to raw leads | High junk rate, wasted sales time | Conversion leads, CRM stages, cost per SQL |
| Scaling on platform ROAS while MER drops | Paying for non-incremental conversions | Backend reconciliation, lift tests |
| Fragmented accounts (dozens of interest ad sets) | Learning limited, auction overlap, higher CPM | Consolidation |
| Creative volume without diversity | No new reach, fatigue | Concept grid |
| Over-editing | Constant learning resets | Weekly batching |
| Cutting placements or ages from breakdowns | Higher total CPA | Value rules with backend data |
| Unreviewed generative enhancements | Claims violations, off-brand ads | Review at launch |
| Misreading attribution changes as performance drops | Wrong budget cuts | Date checks |
| Circumventing restrictions | Permanent bans | Fix and appeal |
| Ignoring speed to lead in messaging and forms | Low close rates | SLA under 5 minutes |

## 8. Benchmarks

| Metric or effect | Value | Source | Date | Sample and caveat | Label |
|-----------------|-------|--------|------|-------------------|-------|
| Ad impressions YoY | +11% (Q2 2025), +14% (Q3 2025) | Meta earnings | 2025-07, 2025-10 | Global, all formats | [Official] |
| Average price per ad YoY | +9% (Q2 2025), +10% (Q3 2025) | Meta earnings | 2025-07, 2025-10 | Global average | [Official] |
| Andromeda | +6% recall, +8% ads quality on selected segments | Meta Engineering | 2024-12 | Meta internal | [Official] |
| GEM | About +5% conversions Instagram, +3% Facebook Feed (Q2 2025) | Meta Engineering | 2025-11 | Meta internal | [Official] |
| Lattice extension | Nearly 4% more conversions on Facebook Feed and Reels (Q2 2025) | Earnings via secondary | 2025 | Meta internal | [Official via secondary] |
| Incremental attribution | 46% lift vs BAU; earlier tests above 20% | Meta via Jon Loomer, Social Media Today | 2025 | Meta tests | [Official] |
| Incremental attribution, independent | 43% win rate vs standard | Haus | 2025 | Early tests, small sample | [Study] |
| Incremental ROAS vs platform | 1.90x cold, 3.64x retargeting vs 8x platform | Cassandra (via search summary) | 2025 to 2026 | Vendor method | [Study, vendor] |
| Opportunity Score adopters | Median 12% lower cost per result | Meta via Social Media Today | 2024 to 2025 | Meta analysis | [Official] |
| March 2026 click attribution change | Reported click-through conversions down 15 to 40% | Vendor blogs | 2026-03 | WooCommerce samples | [Unverified] |
| January 2026 view window removal | Reported conversions down 15 to 30% for 7-day view users | Vendor blogs | 2026-01 | Estimates | [Unverified] |
| Threads CPM | 30 to 40% below Instagram | Single guide | 2026 | Unclear sample | [Unverified] |
| Threads in Advantage+ placements | 11.7% lower CPA | Single guide | 2026 | Unclear source | [Unverified] |
| Advantage+ sales ROAS | +22% often quoted | Many blogs | n/a | Not traced to primary | [Unverified] |
Caveat for all: benchmarks vary by vertical, geo, season and attribution setting; compare against the account's own history first.

## 9. Tools, APIs and MCP servers

| Tool | Type | Use | Notes |
|------|------|-----|-------|
| Marketing API (Graph API) | Official | Read insights, manage campaigns (writes need approval) | Versions released several times per year; v24 and v25 removed legacy ASC and AAC creation |
| Conversions API, CAPI Gateway, Signals Gateway | Official | Server-side events | Gateway hosted in advertiser cloud or via partners |
| Ads Library and Ads Library API (`ads_archive`) | Official | Competitive research; political and social issue ads globally; EU ads with DSA fields | Identity confirmation needed for API |
| Facebook Business SDKs (Python, Node, PHP, Java, Ruby) | Official | Scripts | github.com/facebook/facebook-python-business-sdk |
| Robyn, GeoLift | Official open source | MMM and geo experiments | GitHub facebookexperimental and facebookincubator |
| Pipeboard Meta Ads MCP | Community MCP | Read insights and objects, some writes | Verify current features and auth model |
| GoMarble facebook-ads-mcp-server | Community MCP | Read-focused | Verify |
| Connectors (Supermetrics, Funnel, Windsor.ai, Porter Metrics, Fivetran, Airbyte) | Vendor | ETL to warehouse or sheets | Read only |
| Creative analytics (Motion, Atria, Foreplay, Superads, Triple Whale) | Vendor | Concept-level analysis, swipe files | Vendor metrics definitions differ |
| Attribution and incrementality (Northbeam, Triple Whale, Rockerbox, Haus, Measured, Recast, WorkMagic) | Vendor | Cross-channel truth, lift tests | Owned by measurement agent |
| Automation (Ads Manager rules, Birch, Madgicx) | Native and vendor | Alerts and rules | Rules are standing changes requiring approval |
| Meta AI reporting into Google Workspace | Official (reported) | Recurring analysis | [Unverified, 2026-09] |

## 10. Official sources to monitor

| Source | URL | Frequency |
|--------|-----|-----------|
| Graph API changelog | https://developers.facebook.com/docs/graph-api/changelog | Monthly and before API work |
| Meta for Developers blog | https://developers.facebook.com/blog/ | Monthly |
| Meta for Business news | https://www.facebook.com/business/news | Weekly |
| Business Help Center | https://www.facebook.com/business/help | Before launches |
| Advertising Standards | https://transparency.meta.com/policies/ad-standards/ | Monthly and before regulated launches |
| Meta Engineering (ML applications) | https://engineering.fb.com/ | Quarterly |
| Meta Newsroom | https://about.fb.com/news/ | Weekly |
| Investor relations and SEC filings | https://investor.atmeta.com/ and https://www.sec.gov/ | Quarterly |
| Meta Status | https://metastatus.com/ | On anomalies |
| EU DMA page | https://digital-markets-act.ec.europa.eu/ | Quarterly |

## 11. Open questions and watch list

1. Scope and permanence of ad set placement exclusion removal (2026-08); whether Meta documents it and whether value rules gain a zero-bid option.
2. Exact current labels and mechanics of new customer controls (existing customer budget cap vs new customer goals) after the 2026 unification.
3. Conversion leads optimization eligibility thresholds in 2026.
4. Whether the April 2026 incremental attribution update exists as described and how it changes eligibility (cost goals).
5. WhatsApp Status ads availability by country, especially EU and Turkey, and the reported Ads Manager integration (2026-08).
6. Threads ad formats (video carousels, catalog video) and the September 2026 username rule change.
7. Creator Marketing Hub features and partnership ads API support.
8. Whether Meta ships an official MCP server or agent API for ad accounts (reported Meta AI reporting connections in 2026-09).
9. Turkey: location fee rate, VAT handling, Threads availability status.
10. Meta's end-of-2026 automation goal: whether Advantage+ will remove more manual levers (audience, budget split, creative control) in Q4 2026 or Q1 2027.
11. Q3 2026 earnings (late October 2026) for impressions, price per ad and automation commentary.
12. Learning phase thresholds: whether Meta has lowered event requirements for some campaign types.

## 12. Sources

1. Meta Andromeda: Supercharging Advantage+ automation with the next-gen personalized ads retrieval engine. Engineering at Meta. https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/ (2024-12-02)
2. Meta's Generative Ads Model (GEM): The Central Brain Accelerating Ads Recommendation AI Innovation. Engineering at Meta. https://engineering.fb.com/2025/11/10/ml-applications/metas-generative-ads-model-gem-the-central-brain-accelerating-ads-recommendation-ai-innovation/ (2025-11-10)
3. AI Innovation in Meta's Ads Ranking Driving Advertiser Performance. Meta for Business. https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance (n.d., about 2025)
4. Meta Advantage+ shopping / sales campaigns. Meta for Business. https://www.facebook.com/business/ads/meta-advantage/advantage-plus-shopping-ads (accessed 2026-10)
5. Helping You Find More Channels and Businesses on WhatsApp. Meta Newsroom. https://about.fb.com/news/2025/06/helping-you-find-more-channels-businesses-on-whatsapp/ (2025-06-16)
6. Meta Newsroom post on WhatsApp Updates tab. X. https://x.com/MetaNewsroom/status/1934597815927181539 (2025-06-16)
7. Why the Commission's Decision Undermines the Goals of the DMA. Meta Newsroom. https://about.fb.com/news/2025/07/why-the-commissions-decision-undermines-the-goals-of-the-dma/ (2025-07)
8. Meta commits to give EU users choice on personalised ads under the DMA. European Commission. https://digital-markets-act.ec.europa.eu/meta-commits-give-eu-users-choice-personalised-ads-under-dma-2025-12-08_en (2025-12-08)
9. Meta Platforms Form 10-K FY2025. SEC EDGAR. https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm (2026-01)
10. Meta Platforms Form 10-Q Q1 2026. SEC EDGAR. https://www.sec.gov/Archives/edgar/data/0001326801/000162828026028526/meta-20260331.htm (2026-04)
11. Meta Platforms Form 10-Q Q2 2026. SEC EDGAR. https://www.sec.gov/Archives/edgar/data/0001326801/000162828026050705/meta-20260630.htm (2026-07)
12. Meta to begin rolling out Threads ads globally. CNBC. https://www.cnbc.com/2026/01/21/meta-ads-global-threads.html (2026-01-21)
13. Threads rolls out ads to all users worldwide. TechCrunch. https://techcrunch.com/2026/01/21/threads-rolls-out-ads-to-all-users-worldwide (2026-01-21)
14. Meta Announces Global Expansion of Threads Ads. Social Media Today. https://www.socialmediatoday.com/news/meta-announces-global-expansion-of-threads-ads/810151/ (2026-01)
15. Meta finally brings Threads ads to every user after yearlong testing phase. PPC Land. https://ppc.land/meta-finally-brings-threads-ads-to-every-user-after-yearlong-testing-phase/ (2026-01)
16. Meta expands advertising formats on Threads with catalog ads. PPC Land. https://ppc.land/meta-expands-advertising-formats-on-threads-with-catalog-ads/ (2025)
17. Meta expands Threads advertising globally, new ad formats on offer. Mi-3. https://www.mi-3.com.au/22-01-2026/meta-expands-threads-advertising-globally-new-ad-formats-offer (2026-01-22)
18. WhatsApp is rolling out Promoted Channels and Status Ads globally. WABetaInfo. https://wabetainfo.com/whatsapp-is-rolling-out-promoted-channels-and-status-ads-globally/ (2026-02)
19. WhatsApp rolls out Promoted Channels and ads in Status globally. BetaNews. https://betanews.com/article/whatsapp-rolls-out-promoted-channels-and-ads-in-status-globally/ (2026-02)
20. No WhatsApp ads in EU until 2026, DPC says. Silicon Republic. https://www.siliconrepublic.com/business/whatsapp-ads-eu-2026-dpc-data (2025)
21. Advantage+ Sales, App, and Leads Campaigns are Coming. Jon Loomer Digital. https://www.jonloomer.com/advantage-plus-sales-app-leads-campaigns/ (2025-02)
22. Meta Tests Streamlined Advantage+ Campaign Setup. Adweek. https://www.adweek.com/media/meta-tests-streamlined-advantage-campaign-setup/ (2025)
23. Meta launches unified API structure for Advantage+ campaigns. PPC Land. https://ppc.land/meta-launches-unified-api-structure-for-advantage-campaigns/ (2025-05)
24. Meta deprecates legacy campaign APIs for Advantage+ structure. PPC Land. https://ppc.land/meta-deprecates-legacy-campaign-apis-for-advantage-structure/ (2025)
25. Meta Advantage+ Sales Campaigns: Complete 2026 Guide. AdNabu. https://blog.adnabu.com/facebook/meta-advantage-plus-sales-campaigns/ (2026)
26. Advantage+ app campaigns: default-on setup versus sunset of legacy AAC. UA Ledger. https://ualedger.com/blog/posts/follow-up-meta-advantage-plus-rollout (2026)
27. Meta restricts attribution windows and data retention in Ads Insights API. PPC Land. https://ppc.land/meta-restricts-attribution-windows-and-data-retention-in-ads-insights-api/ (2025)
28. Meta Ads Attribution Window Removed: How to Track Conversions Now. Dataslayer. https://www.dataslayer.ai/blog/meta-ads-attribution-window-removed-january-2026 (2026-01)
29. Meta Killed Its 28-Day View Attribution Window on January 12, 2026. Seresa. https://seresa.io/blog/attribution-measurement/meta-killed-its-28-day-view-attribution-window-on-january-12-2026 (2026)
30. What Meta's March 2026 attribution update means for your reporting and performance. Leafsignal. https://www.leafsignal.com/blog/meta-march-2026-attribution-update (2026-03)
31. Meta Rewired Conversion Attribution in March 2026. Mintec. https://mintec.co/blog/meta-ads-attribution-engage-through-2026/ (2026-03)
32. Meta's Attribution Change: Why Reported Conversions Dip. Digital Applied. https://www.digitalapplied.com/blog/meta-ads-click-through-attribution-change-2026-what-changed (2026-03)
33. Meta attribution changes 2026: engage-through, explained. Good Morning Co. https://goodmorningco.com/blog/meta-attribution-changes-engage-through (2026-03)
34. Meta's Engage-Through Window Is Toggleable. Seresa. https://seresa.io/blog/attribution-measurement/metas-engage-through-window-is-toggleable-most-woocommerce-stores-dont-know (2026)
35. Meta Announces Incremental Conversions Attribution Setting. Jon Loomer Digital. https://www.jonloomer.com/qvt/incremental-conversions/ (2025)
36. Meta Shares More Info on Incremental Attribution Tracking. Social Media Today. https://www.socialmediatoday.com/news/meta-updates-information-incremental-attribution-conversion-tracking/759205/ (2025)
37. Is Meta Incremental? Haus. https://www.haus.io/blog/is-meta-incremental (2025)
38. Meta is changing its attribution settings. Haus. https://www.haus.io/blog/meta-is-changing-its-attribution-settings-heres-what-you-need-to-know (2025)
39. We Tested Meta's New Incremental Attribution Setting on $1M in Ad Spend. Seer Interactive. https://www.seerinteractive.com/insights/we-tested-metas-new-incremental-attribution-setting-on-1m-in-ad-spend.-heres-how-it-works (2025)
40. Incremental Attribution on Meta: What It Measures and Where It Falls Short. WorkMagic. https://www.workmagic.io/blog/incremental-attribution-meta (2025 to 2026)
41. Meta's Incremental Attribution Guide. Birch. https://bir.ch/blog/meta-incremental-attribution (2025 to 2026)
42. Meta's Health and Wellness Restrictions. Triple Whale. https://www.triplewhale.com/blog/meta-health-and-wellness-brands (2025)
43. Meta's New Advertising Rules: Key Considerations for Health and Wellness Businesses. Foley Hoag. https://foleyhoag.com/news-and-insights/blogs/security-privacy-and-the-law/2025/january/meta-s-new-advertising-rules-key-considerations-for-health-and-wellness-businesses/ (2025-01)
44. Unpacking Meta's Data Restrictions, part two. Twigeo. https://www.twigeo.com/2025/04/08/unpacking-metas-data-restrictions-the-latest-insights-part-two/ (2025-04-08)
45. Meta Restricted Purchase Events for Health and Wellness. Curve Compliance. https://www.curvecompliance.com/ad-account-rescue/meta-health-and-wellness-purchase-events-restricted (2025 to 2026)
46. How Meta's Data Restrictions Impact Healthcare Advertising Strategies. Cardinal Digital Marketing. https://www.cardinaldigitalmarketing.com/healthcare-resources/blog/meta-announces-major-changes-healthcare-advertising/ (2025)
47. 2026 Health Advertising Policies on Social Media. Accelerated Digital Media. https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/ (2026)
48. Meta plans to use AI chat data for ad targeting starting December. PPC Land. https://ppc.land/meta-plans-to-use-ai-chat-data-for-ad-targeting-starting-december/ (2025-10)
49. Advocates Urge FTC to Halt Meta's Plan to Use AI Chatbot Data for Ads. EPIC. https://epic.org/press-release-advocates-urge-ftc-to-halt-metas-plan-to-use-ai-chatbot-data-for-ads/ (2025)
50. Meta Publishes Upcoming Update to Privacy Policy to Use AI Interactions For Ads. Visualping. https://visualping.io/blog/meta-ai-privacy-policy (2025-10)
51. Meta Launches Opportunity Score to All Advertisers. Social Media Today. https://www.socialmediatoday.com/news/meta-launches-opportunity-score-all-advertisers/750231/ (2024 to 2025)
52. Meta Opportunity Score Explained. Birch. https://bir.ch/blog/meta-opportunity-score (2025)
53. Meta's Creative Testing Tool: Setup, Strategy, and Results. Jon Loomer Digital. https://www.jonloomer.com/meta-creative-testing/ (2025-10)
54. How Meta's Updated Creative Testing Tool Can Benefit Your Brand. Revel Marketing Partners. https://www.revelmarketingpartners.com/blogposts/2025/10/17/how-metas-updated-creative-testing-tool-can-benefit-your-brand (2025-10-17)
55. Facebook Ads A/B Testing: Complete Guide. AdManage. https://admanage.ai/blog/facebook-ads-ab-testing (2026)
56. Meta Is Removing Placement Controls From Ad Sets. Jon Loomer Digital. https://www.jonloomer.com/meta-removing-placement-controls-ad-sets/ (2026-08)
57. Meta Is Removing Ad Placement Controls: What Ecommerce Brands Must Do. Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/meta-is-removing-ad-placement-controls-what-ecommerce-brands-must-do-before-q4 (2026-08 to 09)
58. Meta Removed Placement Controls From Ad Sets. Value Rules Are Not a Replacement. AdRise Lab. https://adriselab.com/blog/meta-placement-controls-removed-value-rules-2026 (2026-09)
59. Meta Removing Placement Controls: What Changed and When. Blackfire Marketing. https://blackfiremarketing.co.uk/blog/meta-ad-placement-controls-removed (2026-09)
60. Every Meta Ads Change in 2026 (Updated Weekly). Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026 (2026)
61. Meta Ads Updates (September 2026). AdsUploader. https://adsuploader.com/blog/meta-ads-updates (2026-09)
62. Meta Ads Weekly Update: 7 September 2026. Franklin Marketing. https://franklinmarketing.com.au/blogs/meta-ads-weekly-update-7-september-2026 (2026-09-07)
63. What changed in Meta ads for authors in 2026. Market with Melissa. https://marketwithmelissa.substack.com/p/meta-ads-changes-september-2026 (2026-09)
64. What Meta Announced at IAB NewFronts 2026. ALM Corp. https://almcorp.com/blog/meta-iab-newfronts-2026-reels-trending-ads-creator-discovery-threads-video-ads/ (2026-05)
65. Meta less personalised ads: its filings say. Cittago. https://cittago.com/blog/meta-less-personalised-ads-eu-filings-2026/ (2026-09)
66. Meta rewrites its EU ad model as regulators tighten the screws. eMarketer. https://www.emarketer.com/content/meta-rewrites-its-eu-ad-model-regulators-tighten-screws (2025-12)
67. Meta agrees to offer less-personalized ad option for EU users. Anadolu Agency. https://www.aa.com.tr/en/europe/meta-agrees-to-offer-less-personalized-ad-option-for-eu-users/3765367 (2025-12)
68. AutoML for Large Capacity Modeling of Meta's Ranking Systems. arXiv. https://arxiv.org/pdf/2311.07870 (2023-11)
69. How Meta's Ads Algorithm Works in 2026: Lattice, UTIS and Andromeda. Greg Hal. https://greghal.no/en/blog/meta-ads-algorithm-2026-complete-guide/ (2026)
70. Meta Advantage+: Andromeda, Lattice and GEM Explained. Moburst. https://www.moburst.com/blog/meta-advantage-andromeda-lattice-and-gem-explained/ (2026)
71. Andromeda Meta Ads: The Creative Strategy Guide for 2026. Atria. https://www.tryatria.com/blog/andromeda-meta-ads (2026)
72. Meta's Andromeda: The Next Era of Ad Optimization. Foxwell Digital. https://www.foxwelldigital.com/blog/what-is-andromeda-from-meta-understanding-metas-next-gen-ad-retrieval-engine (2025)
73. Robyn. Meta Open Source. https://github.com/facebookexperimental/Robyn (living)
74. GeoLift. Meta Open Source. https://github.com/facebookincubator/GeoLift (living)
75. Marketing API documentation. Meta for Developers. https://developers.facebook.com/docs/marketing-api/ (living)
76. Graph API changelog. Meta for Developers. https://developers.facebook.com/docs/graph-api/changelog (living)
77. Conversions API documentation. Meta for Developers. https://developers.facebook.com/docs/marketing-api/conversions-api/ (living)
78. Meta Advertising Standards. Meta Transparency Center. https://transparency.meta.com/policies/ad-standards/ (living)
