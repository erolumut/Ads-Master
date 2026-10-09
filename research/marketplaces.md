# Research Dossier: Marketplaces (Amazon, bol, Trendyol, Hepsiburada and others)

> Research date: 2026-10-08 to 2026-10-09. Scope: selling and advertising on third-party marketplaces: Amazon (Seller Central, Vendor Central, Amazon Ads, DSP basics, Brand Registry, featured offer, FBA, account health, fees, AI shopping), bol.com (Netherlands and Belgium), Trendyol and Hepsiburada (Turkey), and summary coverage of Allegro, Zalando, Etsy, eBay, Walmart Marketplace, noon and Amazon in the Gulf, and TikTok Shop. Topics: channel strategy, listings, reviews, retail media, operations, unit economics, measurement, channel conflict, APIs and MCP servers, and Turkish platform regulation.
>
> Method and limits: 42 web searches (extended mode for 2025 to 2026 facts and niche topics, standard for basics). Direct page fetching was not used, so findings rely on the content of search results from the listed pages. Amazon announces most seller changes inside Seller Central behind a login; many 2026 Amazon details therefore come from secondary sources (agencies, tool vendors, trade press) quoting those notices. Turkish commission and cargo rates come from integrator blogs that disagree with each other; binding rates are in the seller panels. Established mechanics (attribution windows, Vine eligibility, title rules, account health thresholds, competition law basics) are cited from prior knowledge and labeled. Every claim carries an evidence label; single-source items are [Unverified].

## 1. Executive summary

1. Amazon reshaped fees in opposite directions for 2026: US FBA fees rose on average about USD 0.08 per unit from 2026-01-15 with referral fees unchanged, and US FBA prep and labeling services ended on 2026-01-01; in Europe Amazon announced its largest fee cut (average GBP 0.15 or EUR 0.17 per unit, deep referral cuts on low price home, pet and grocery items) effective 2026-01-05 [Official and Secondary, 2025-12 to 2026-01]. Fee models older than January 2026 are stale.
2. The featured offer (Buy Box) lost its performance gate: Amazon removed seller performance as a standalone eligibility requirement from July 2026 (US early July, EU and UK from 2026-07-20, global by end 2026). More offers compete; price, delivery and stock decide more [Secondary, multiple, 2026-07].
3. AI shopping is now a paid ad surface: Sponsored Prompts inside Rufus became paid CPC placements in the US on 2026-03-25, auto-enrolled from Sponsored Products and Sponsored Brands with no prompt-level targeting; Rufus was renamed Alexa for Shopping in the US on 2026-05-13 [Secondary, multiple, 2026]. Listing content quality now feeds both organic AI answers and ad copy that Amazon writes.
4. Amazon Ads moved toward agents and one console: unBoxed 2025 (2025-11-11 to 12) launched Ads Agent, Creative Agent, a unified Campaign Manager for sponsored ads and DSP, Complete TV, and extended AMC lookback from 13 to 25 months; the Amazon Ads MCP Server entered open beta on 2026-02-02 [Official 2025-11; Secondary 2026-02].
5. Measurement shifted under advertisers: view attribution for vCPM ads moved to a "shopping-signal enhanced last-touch" model on 2026-01-01, lowering reported view-attributed conversions; "all views" metrics keep the old method. Sponsored Products click windows are unchanged (7 days sellers, 14 days vendors) [Secondary, multiple, 2026-01].
6. Amazon backed off developer fees: the planned SP-API annual fee (USD 1,400 from 2026-01-31) and GET call usage fees were postponed on 2026-03-09 and cancelled on 2026-05-12 [Secondary, ppc.land, 2026-05].
7. bol kept its model but expanded ad inventory: since a 2026-08-27 update, 6 Sponsored Products positions show on app and mobile web instead of 4; conversions are counted within 14 days of a click and ads only serve for offers in the buy block; Retailer API v10 is current, with endpoint deprecations (Commission Beta unsupported from 2026-03-01) [Official, bol, 2026].
8. Turkish marketplaces operate under a fast-moving legal frame: 10 day prior price rules for price tags (2025-10-11) and discount ads (2026-08-01), ad and discount budget caps for large platforms under Law 7416 with thresholds raised 48.07% in 2026, and a Constitutional Court decision (E.2024/187, K.2026/42, published 2026-06-02) that makes marketplaces liable alongside sellers for defective goods in consumer contracts from 2027-03-02 [Official and law firm sources, 2025 to 2026].
9. Turkish marketplace economics are opaque and inflation-sensitive: Trendyol commissions range about 5% to 27% by category, Hepsiburada about 6% to 25%, sources disagree on whether commission is on VAT-inclusive prices, and Trendyol Express cargo tariffs changed again in September 2026 [Secondary, Contested, 2026]. Hepsiburada (66% owned by Kaspi.kz) grew FY2025 GMV 4.3% in IAS 29 terms vs 41% unadjusted [Official, 2026-02].
10. Agentic tooling now exists across the main marketplaces: Amazon publishes an SP-API developer MCP package, Amazon Ads runs an MCP server, Trendyol published an official Claude Code plugin backed by a Trendyol Developer Tools MCP server, and community MCP servers cover SP-API, Trendyol and Hepsiburada (some read-only) [Official GitHub and Secondary, 2026]. Least privilege and read-only first are mandatory.

## 2. State of the channel in 2026 (with numbers)

### 2.1 Amazon fees and operations
- US 2026 fee update effective 2026-01-15: average FBA increase about USD 0.08 per unit (framed by Amazon as under 0.5% of average item price); no new FBA fee types; referral percentages unchanged since January 2024; Low-Price FBA automatic under USD 10; small standard items priced USD 10 to 50 up about USD 0.25 per unit in one analysis [Secondary quoting Official, 2025-12].
- US FBA prep and labeling services ended 2026-01-01; inbound defect charges consolidated; aged inventory surcharges steeper; low inventory level fee extended to Small Bulky and Large Bulky per FNSKU (grocery exempt) [Secondary, 2026].
- A 3.5% fuel and logistics surcharge on US FBA fees from 2026-04-17 appears in a single third-party source [Unverified].
- Europe 2026: average cut of GBP 0.15 or EUR 0.17 per unit; Home products up to EUR 20 from 15% to 8%, Pet clothing and food up to EUR 10 from 15% to 5%, Grocery and vitamins up to EUR 10 from 8% to 5%; FBA parcel fees down an average GBP 0.26; Low-Price FBA eligibility extended; deal fee caps lowered; effective 2026-01-05 (brought forward from 2026-02-01); offsetting increases in storage, return to seller and liquidation fees (net about EUR 0.02 per FBA unit from those lines) [Official, aboutamazon.eu, 2025-12; Secondary for dates].
- FBA capacity: dynamic monthly allocation in cubic feet reported from January 2026; IPI below 400 reportedly triggers restrictions [Secondary, 2026; threshold Unverified].
- US FBM changes reported: SAFE-T claim window 30 days from 2026-01-21; refunds within 4 calendar days from 2026-01-26; custom return instructions field removed August 2026 [Secondary, 2026; Unverified].
- Account Health Rating scale 0 to 1,000 with 200 or above healthy [Secondary, 2025-12].
- Amazon Haul: Amazon said it serves 25 locations with more planned in 2026; invitation only for sellers, mostly factories that hit price points; Amazon Bazaar runs in KSA, UAE and other markets [Official 2025; Secondary 2026].
- Generative AI listing tools: Enhance My Listing (2025-05); Amazon reported over 900,000 sellers used its gen AI listing tools and over 90% acceptance without edits [Official via TechCrunch, 2025-05].
- Events 2026: Prime Day moved to 2026-06-23 to 26 (from July); Prime Big Deal Days 2026-10-06 to 07 [Official, 2026].

### 2.2 Amazon Ads
- unBoxed 2025 (2025-11-11 to 12, Nashville): Ads Agent (plans, launches, optimizes; SQL for AMC), Creative Agent, unified Campaign Manager joining sponsored ads and Amazon DSP, Complete TV (streaming inventory incl. Roku and others through DSP), AMC lookback 25 months (US and CA open beta from 2025-11-11, other locales Q1 2026) [Official, 2025-11]. Netflix inventory named only by one source [Unverified].
- Sponsored Prompts: paid GA in US 2026-03-25; auto-enrolled; Amazon writes prompts from listing and Brand Store content; no prompt targeting or exclusion; reporting blended [Secondary, multiple].
- Alexa for Shopping: Rufus renamed in the US 2026-05-13 [Secondary, multiple; Amazon newsroom not read directly].
- Sponsored Display renamed display ads; new campaigns via the Display flow; existing campaigns continue [Official product page, 2026].
- View attribution change 2026-01-01; "all views" metrics (one source counts 54) preserve the prior method; one vendor estimates 15% to 30% fewer reported view-attributed conversions [Secondary, 2026-01; estimate Unverified].
- AMC: 1P paid features (Amazon Shopping Insights, Flexible Shopping Insights, Retail Purchases, Brand Store Insights, Prime Video Insights) free to query through 2026-12-31; fees afterwards unless opted out [Secondary citing Official, 2026].
- Amazon Ads MCP Server: closed beta from 2025-11, open beta 2026-02-02, for Ads API credential holders; scope reported across SP, SB, display, DSP and AMC [Secondary, 2026].

### 2.3 Benchmarks landscape
- No official Amazon cross-category benchmark set; vendor 2026 numbers: platform ACoS about 29% to 34%, CPC about USD 1.13 to 1.22 (one source: USD 0.89 in 2023 to USD 1.21 early 2026), TACoS 10% to 15% for healthy accounts; category ACoS roughly 18% to 19% (books) up to about 42% (clothing) [Secondary, vendor, 2026].
- Unit session percentage: vendor blogs cite about 10% average with 10% to 15% as good, wide category spread [Secondary, vendor, 2025 to 2026].
- Amazon reportedly launched competitive benchmarks reporting in 18 global markets [Unverified, truncated source].

### 2.4 bol
- Sponsored Products: 6 positions on app and mobile web since 2026-08-27; 14 day click attribution; only buy block offers serve [Official, 2026].
- Display offsite on premium sites and social (Facebook, Instagram, Pinterest) with strict brand rules (no bol logo; "Available at bol" or "Exclusive at bol"; 1080 x 1080 minimum) [Official].
- Retailer API: v10 live, v8 and v9 removed December 2024; deprecated resources supported at least 12 months; Commission Beta endpoint unsupported from 2026-03-01 [Official].
- LVB: new tariffs for 3XS and XXS size classes from 2026-09-09 [Secondary, 2026-09].
- Commission: fixed fee per item plus a category percentage of the VAT-inclusive price; third-party ranges conflict (for example EUR 0.20 to 2.48 plus 4.1% to 20.7% vs 7% to 17%) [Contested, 2026].
- CPC estimates EUR 0.10 to 1.50+ and EUR 0.30 to 0.60 come from blogs without method [Unverified].

### 2.5 Turkey
- Hepsiburada FY2025: GMV TRY 257.5B (IAS 29 restated, up 4.3%; unadjusted TRY 236.5B, up 41.0%); marketplace GMV TRY 176.2B, 68.4% of total; EBITDA down 57.8%; net loss TRY 5.7B; consumer boycotts and lending investments cited [Official, 2026-02-26].
- Kaspi.kz closed the purchase of 65.41% on 2025-01-29 (about USD 1.127B), later 66.35%, plus a TRY 4.17B injection in December 2025 [Official filings, 2025].
- Trendyol commissions about 5% (digital gift cards) to 27% (phone spare parts); dynamic commissions reported in some subcategories in 2026 [Secondary, 2026-07; Unverified].
- Trendyol Express tariffs per a 2026-09-08 list: 0 to 2 desi TRY 81.95 plus VAT, 5 desi TRY 114.10, 10 desi TRY 164.18; older lists lower [Secondary, 2026-09].
- Trendyol ads: product ads (minimum daily budget TRY 10 per official FAQ), store ads, influencer ads with #işbirliği label, Meta collaboration ads [Official FAQ and Secondary].
- Competition Board: Trendyol commitments binding since 2024-10-03 (no forced automated pricing, no equivalent incentives); earlier interim measures on self-preferencing (2021) [Official].
- Turkish e-commerce withholding (stopaj) of 1% on seller payouts since 2025-01-01 [Official, 2024-12, prior knowledge; verify current rate].

### 2.6 Other marketplaces
- Allegro: commission caps in some categories and One Fulfillment storage cuts (2026-03-02); minimum CPC increase for sponsored offers (2026-02-16); additional commission for featuring offers on foreign Allegro sites after 30 free days (2026-09-17); 4.2 million international customers [Official help pages, 2026; Secondary 2025].
- Zalando: four-part partner fee structure from 2026-01-01 (base fee, Marketplace Service fee, Payment Service fee, Convenience Incentive) [Secondary, Unverified]; ZEOS fee summary in Partner University [Official, login].
- Etsy: regulatory operating fee increases on 2026-06-22 (France 0.47% to 1.14%); DDP required for non-US sellers shipping to the US from 2026-07-09 [Secondary, 2026].
- eBay: currency conversion fee 3% to 3.25% for US and Canada from 2026-10-14; UK and EU increases in December 2026 [Official help page, 2026].
- Walmart: New-Seller Savings window 2026-02-02 to 2027-01-31 with referral discounts and ad credits (USD 1,000 SEM, USD 500 Walmart Connect, conditional) [Official, 2026].
- noon: UAE referral mostly 10% with AED 1 minimum; FBN storage AED 1.75 per cubic foot in UAE and SAR 2.75 in KSA from 2026-10-01 [Official help, 2026].
- TikTok Shop: Netherlands, Belgium, Austria and Poland opened 2026-06-15, after Spain and Ireland (late 2024) and Germany, France and Italy (2025-03); more than 100,000 European sellers; Sell Across Europe announced May 2026 [Official newsroom 2026-06; Secondary].

## 3. Timeline of changes, January 2025 to October 2026

| Date | Change | Impact | Label |
|------|--------|--------|-------|
| 2025-01-01 | Turkish 1% e-commerce withholding on marketplace payouts | Cash flow for sellers in TR | [Official, 2024-12, prior knowledge] |
| 2025-01 | Amazon title policy: 200 characters, no special characters, no word more than twice | Listing rewrites | [Official, prior knowledge] |
| 2025-01-29 | Kaspi.kz closes purchase of 65.41% of Hepsiburada | Owner change at TR #2 | [Official] |
| 2025-03 | TikTok Shop launches in Germany, France, Italy | New EU social commerce channel | [Official] |
| 2025-03-08 | Turkish intermediary regulation amended: sellers' KEP requirement removed, platforms verify seller identity | Onboarding changes | [Secondary] |
| 2025-05 | Amazon Enhance My Listing (gen AI listing suggestions) | AI listing drafts | [Official via press] |
| 2025-05-07 | Trendyol Go control transfer notified to the Competition Board | Group restructuring | [Official] |
| 2025-05-24 | Turkish Distance Contracts Regulation amendment published (in force 2026-01-01) | Withdrawal and return shipping rules | [Secondary, Contested details] |
| 2025 | Turkish ad budget regulation: sponsorship exclusion 25% to 50% for large platforms | Platform ad budgets | [Secondary, Paksoy] |
| 2025-08-29 | US de minimis suspended for all countries | Cross-border costs | [Official, via offer-strategy research] |
| 2025-10-11 | Turkey price tag lookback 10 days | Price history rules | [Official, via secondary] |
| 2025-11 | SP-API fees announced (USD 1,400 per year from 2026-01-31, usage fees from 2026-04-30) | Developer costs (later cancelled) | [Secondary] |
| 2025-11 | Amazon Ads MCP Server closed beta | Agentic ads access | [Secondary] |
| 2025-11-11 to 12 | unBoxed 2025: Ads Agent, Creative Agent, unified Campaign Manager, Complete TV, AMC 25 month lookback | Workflow and measurement | [Official] |
| 2025-12 | Amazon EU fee cuts announced; US 2026 fee update announced | Fee models | [Official] |
| 2025-12-15 | Some EU FBA parcel and clothing referral cuts start | EU margins | [Secondary, Contested] |
| 2025-12-25 | Turkish Article 12 administrative fines raised 25.49% for 2026 | Compliance cost | [Official] |
| 2026-01-01 | US FBA prep and labeling services end; Amazon view attribution change; Turkish Distance Contracts amendment in force; Zalando fee structure change | Operations and reporting | [Secondary; Zalando Unverified] |
| 2026-01-05 | Amazon EU referral and FBA cuts effective | EU margins | [Official] |
| 2026-01-15 | Amazon US 2026 fees effective | US margins | [Secondary quoting Official] |
| 2026-01-21 | SAFE-T claim window 30 days (US FBM) | Claims process | [Unverified] |
| 2026-01-26 | FBM refunds within 4 calendar days (US) | Operations | [Unverified] |
| 2026-02-02 | Amazon Ads MCP Server open beta | Agent access to ads | [Secondary] |
| 2026-02-02 | Walmart New-Seller Savings 2026 window opens (to 2027-01-31) | US entry incentives | [Official] |
| 2026-02-12 | Turkish Constitutional Court decision E.2024/187, K.2026/42 on marketplace liability | Liability from 2027-03-02 | [Secondary, law firms] |
| 2026-02-16 | Allegro minimum CPC raised for sponsored offers | PL ads costs | [Official] |
| 2026-03-01 | bol Commission Beta endpoint unsupported | Integrations | [Official] |
| 2026-03-02 | Turkish 6563 thresholds raised 48.07%; Allegro fee changes | Obligations scope; PL fees | [Official] |
| 2026-03-09 | SP-API fees postponed indefinitely | Developer costs | [Secondary] |
| 2026-03-25 | Sponsored Prompts paid GA in the US | New CPC surface | [Secondary, multiple] |
| 2026-04-17 | Reported US FBA fuel and logistics surcharge 3.5% | US margins | [Unverified] |
| 2026-05 | TikTok Shop "Sell Across Europe" announced | EU cross-border | [Secondary] |
| 2026-05-12 | SP-API fees cancelled "at this time" | Developer costs | [Secondary] |
| 2026-05-13 | Rufus renamed Alexa for Shopping (US) | Naming, AI shopping | [Secondary, multiple] |
| 2026-06-02 | Constitutional Court decision published (Official Gazette 33268) | Effective 2027-03-02 | [Secondary] |
| 2026-06-15 | TikTok Shop live in Netherlands, Belgium, Austria, Poland | NL and BE competition for bol | [Official] |
| 2026-06-16 | Allegro cheaper heavy parcel delivery to CZ, SK, HU | Cross-border costs | [Official] |
| 2026-06-22 | Etsy regulatory operating fees raised in several countries | Etsy margins | [Secondary] |
| 2026-06-23 to 26 | Prime Day (moved from July) | Event planning | [Official] |
| 2026-07-01 | Turkish Commercial Advertising Regulation amendment published | 10 day discount rule, reviews, influencers | [Official Gazette] |
| 2026-07-06 to 08 | Amazon announces removal of featured offer eligibility gate | Featured offer competition | [Secondary, multiple] |
| 2026-07-09 | Etsy DDP for non-US sellers shipping to US | Cross-border | [Secondary] |
| 2026-07-20 | Featured offer change rollout in EU and UK | EU featured offer | [Secondary] |
| 2026-08-01 | Turkish discount ad 10 day prior price rule in force | Promotions in TR | [Official, via secondary] |
| 2026-08 | Turkish draft regulation on cargo liability and seller data portability | Possible new duties | [Unverified] |
| 2026-08-27 | bol 6 Sponsored Products positions on mobile | More mobile ad inventory | [Official] |
| 2026-09-08 | New Trendyol Express tariff list reported | TR shipping costs | [Secondary] |
| 2026-09-09 | bol LVB tariffs for 3XS and XXS | NL fulfillment costs | [Secondary] |
| 2026-09-10 | noon FBN outbound fee revision | Gulf costs | [Secondary] |
| 2026-09-17 | Allegro commission on featured offers on foreign sites | PL cross-border costs | [Official] |
| 2026-10-01 | noon storage fee increase | Gulf costs | [Official] |
| 2026-10-06 to 07 | Prime Big Deal Days | Event | [Official] |
| 2026-10-14 | eBay US and Canada currency conversion fee 3.25% | eBay margins | [Official] |
| 2026-10-27 | Allegro Ads terms update (Advertising Network service fee definition) | PL ads | [Official] |
| 2026-12-31 | AMC 1P paid features free period ends | AMC costs | [Secondary citing Official] |
| 2027-03-02 | Turkish marketplace liability for defective goods in consumer contracts | TR operations | [Secondary] |

## 4. Best practice consensus

- Fix order: account health, stock, featured offer, listing, reviews, then ads [Practitioner consensus].
- Set ad targets from breakeven ACoS (contribution before ads after all marketplace fees) and control with TACoS [Practitioner consensus].
- Structure campaigns by intent (brand, category, competitor, discovery, launch) and product group; harvest search terms into exact match and isolate them [Practitioner consensus].
- Pause ads on out of stock, no featured offer and low rated ASINs [Practitioner consensus].
- Launch new ASINs with a written TACoS glidepath and early reviews from compliant programs (Vine) [Practitioner consensus].
- Keep 4 to 8 weeks of cover in marketplace warehouses; plan peaks 8 to 12 weeks ahead because of capacity limits [Practitioner consensus].
- Write listings for both search and AI assistants: complete attributes, factual answers to common questions, consistent facts across listing, A+ and Brand Store [Practitioner consensus, 2026].
- Use Brand Analytics Search Query Performance to diagnose the funnel per query [Practitioner consensus].
- Tag every external link to Amazon with Amazon Attribution to earn the Brand Referral Bonus (about 10% on average) [Secondary, 2026].
- Avoid channel conflict through assortment design (exclusive packs) and coordinated calendars rather than reseller price control [Practitioner consensus; competition law].

## 5. Contested topics (both sides)

| Topic | Side A | Side B | Our position |
|-------|--------|--------|--------------|
| Brand defense on own brand terms | Necessary: competitors buy brand terms; SB at top protects shelf; cheap clicks | Wasteful: brand searchers convert organically; cannibalizes organic | Test with holdouts per marketplace; keep where pause loses more than it saves |
| ACoS vs TACoS as the main target | ACoS is controllable per campaign | TACoS reflects total business and halo | ACoS per intent for control, TACoS and CM3 for decisions |
| Does A+ text index for search? | Some sellers report indexing | Others see no effect | Do not rely on A+ for indexing; put Tier 1 terms in title, bullets, backend [Contested] |
| Value of DSP for mid-size sellers | Upper funnel builds branded search and NTB | Hard to measure, minimums high | Test at scale with AMC or lift reads only |
| LVB vs own fulfillment for buy block on bol | LVB favored for promise reliability | Strong own logistics matches it | Choose per SKU on economics and promise |
| Trendyol commission base (VAT-inclusive or exclusive) | Paraşüt: VAT-exclusive base plus VAT on commission | Fenikya: VAT-inclusive | Read the panel's agreement screen; model both |
| Amazon EU fee effective dates | 2025-12-15 for some lines | 2026-01-05 and 2026-02-01 in other reports | Use the dated notice per store |
| Turkish return shipping cost after 2026 | Seller keeps paying (Ministry decision) | Consumer may pay (some blogs) | Seller pays unless counsel confirms otherwise [Contested] |
| Vine billing timing | After 30 days with at least one review | 7 days after first review | Check the enrollment page |
| Featured offer announcement date | 2026-07-06 | 2026-07-08 | Immaterial; rollout dates matter |

## 6. What top operators do differently

- They model fees from the account and recompute breakeven ACoS after every fee change, per marketplace and SKU.
- They separate ads by intent and judge them on TACoS and contribution, with brand defense proven by holdouts.
- They treat stock and the featured offer as ad prerequisites and pause ads automatically when either fails.
- They build listings as answer sets for shoppers and AI assistants and test them with Manage Experiments.
- They use Search Query Performance weekly to find where they lose shoppers in the funnel.
- They plan events 12 weeks ahead, freeze reference prices to the law, and coordinate DTC, retail and marketplace calendars.
- They run marketplaces country by country and use staggered rollouts to measure cannibalization and halo.
- They keep account health as a daily operations metric with documented root cause analysis.
- They connect data through APIs or MCP servers with read-only scopes and keep writes behind approvals.
- In Turkey, they refresh economics monthly in real terms and treat platform campaigns as contracts with price locks.

## 7. Common expensive mistakes

- Account-wide ACoS targets that hide loss-making product groups.
- Ads on ASINs without stock or featured offer; ranking collapse after stockouts.
- Missing VAT basis alignment (ACoS on gross vs net) when setting targets in EU and Turkey.
- Using pre-2026 fee tables (US prep ended, EU cuts, bol LVB, noon storage, Turkish cargo).
- Comparing 2026 view-attributed ROAS to 2025 without "all views" metrics.
- Review incentives in inserts or emails, review gating, variation merging (suspensions; FTC and EU fines).
- DTC promotions that suppress the Amazon featured offer or trigger 1P price matching.
- Repricers without floor prices starting price wars on Trendyol, Hepsiburada and Amazon.
- Unprepped inbound to US FBA after 2026-01-01.
- Letting AI listing suggestions or Ads Agent changes go live without fact and approval checks.
- Ignoring the Turkish 10 day prior price rule when "discounting" after a price rise.
- Installing unreviewed third-party MCP servers with write access to seller accounts.

## 8. Benchmarks (source, date, caveat)

| Benchmark | Value | Source and date | Caveat |
|-----------|-------|-----------------|--------|
| Amazon platform ACoS | About 29% to 34% | Vendor reports (Autron, others), 2026 | Definitions vary (SP only vs all; median vs mean) |
| Amazon average CPC | About USD 1.13 to 1.22; USD 0.89 (2023) to 1.21 (early 2026) in one series | Vendor reports, 2026 | US-centric; category spread large |
| Amazon TACoS healthy range | 10% to 15% | Vendor guides, 2026 | Rule of thumb, not a target |
| TACoS by lifecycle | Launch 25% to 40%, growth 12% to 20%, maturity 5% to 12% | One vendor report, 2026 | [Unverified] |
| Category ACoS | Books about 18% to 19%; food and grocery about 21%; clothing about 42% | Vendor reports, 2026 | Sources disagree by 10+ points in beauty and health |
| Unit session percentage | About 10% average; 10% to 15% "good" | Vendor blogs, 2025 to 2026 | Price point and category dominate |
| Brand Referral Bonus | About 10% average credit, 14 day window | Secondary, 2026 | Category rates differ |
| Vine cost example | About USD 24 per review (USD 12 product, 30 units) | Secondary, 2026 | Assumes all units review |
| bol CPC | EUR 0.10 to 1.50+, or EUR 0.30 to 0.60 | Blogs, 2026 | [Unverified], no method |
| bol ad spend share | 5% to 15% of revenue | Blog, 2026 | [Unverified] |
| Walmart Sponsored Search CPC | USD 0.30 to 1.50; start USD 0.40 to 0.70 | Blogs, 2026 | [Unverified] |
| Amazon gen AI listing adoption | 900,000+ sellers; 90%+ accepted without edits | Amazon via TechCrunch, 2025-05 | Acceptance is not accuracy |

Agents compare a project against its own history first; benchmarks second.

## 9. Tools, APIs and MCP servers

| Item | Type | Status | Label |
|------|------|--------|-------|
| Amazon SP-API | Official API | Fees cancelled 2026-05-12; Fulfillment Inbound v2024-03-20 current | [Secondary] |
| SP-API dev MCP (`@amazon-sp-api-release/sp-api-dev-mcp`) | Official samples repo | Docs search, live calls, workflow builder | [Official GitHub, via secondary] |
| Amazon Ads API (v3, reporting v3, DSP, AMC API, Attribution API) | Official API | Current | [Official, prior knowledge] |
| Amazon Ads MCP Server | Official MCP (open beta) | Since 2026-02-02 | [Secondary] |
| Amazon Ads Agent | Console AI agent (beta) | Since unBoxed 2025 | [Official] |
| bol Retailer API v10 | Official API | Current; endpoint deprecations | [Official] |
| bol Advertising API | Official API | Version to verify | [Unverified] |
| Trendyol seller APIs and Developer Tools MCP; official Claude Code plugin | Official | 2026 | [Official GitHub] |
| Community Trendyol MCPs (koraynar, bevren, gazi060-design) | Community | Varying write scopes | [Secondary] |
| Read-only Trendyol plus Hepsiburada MCP (acar32furkan-glitch) | Community | GET only | [Secondary] |
| Community SP-API MCPs (ailumia, MarceauSolutions, jay-trivedi, coaxon) | Community | Varying | [Secondary] |
| Allegro REST API, eBay Sell APIs, Walmart Marketplace APIs, Etsy Open API v3, Zalando zDirect, TikTok Shop Partner API | Official APIs | Current | [Prior knowledge] |
| Helium 10, Jungle Scout, Keepa, SmartScout, DataHawk, Perpetua, Pacvue, Skai, Teikametrics, Boloo, Sentos, Dopigo, ikas, ChannelEngine, Channable, Linnworks | Third-party tools | Market | [Practitioner] |

## 10. Official sources to monitor

| Source | What |
|--------|------|
| Seller Central News and Seller Forums announcements (each store) | Fees, policies, featured offer, programs |
| aboutamazon.com and aboutamazon.eu | Fee announcements, events |
| advertising.amazon.com "What's new" and Ads API release notes | Ad products, attribution, AMC, MCP |
| developer-docs.amazon.com/sp-api and Solution Provider Portal | API changes, fees |
| github.com/amzn/selling-partner-api-samples | Official SP-API tooling and MCP |
| partnerplatform.bol.com, Verkopershulp, retailmedia.bol.com, developers.bol.com | bol fees, ads, API |
| Trendyol Satıcı Paneli announcements, developers.trendyol.com, github.com/Trendyol | Fees, ads, API, tooling |
| Hepsiburada Merchant Portal announcements, investor.hepsiburada.com | Fees, ads, company |
| Resmî Gazete, ticaret.gov.tr, rekabet.gov.tr, anayasa.gov.tr | Turkish rules and decisions |
| help.allegro.com "changes for sellers", Zalando Partner University, eBay and Etsy fee pages, Walmart Seller Center, noon Partners help, TikTok Shop Seller Center and newsroom | Other marketplaces |

## 11. Open questions and watch list

- Sponsored Prompts reporting: when will Amazon break out Alexa for Shopping placements and allow prompt-level controls? Expected pattern of 3 to 6 months after commercial launch is a vendor guess [Unverified].
- Alexa for Shopping outside the US: timing of the rename and Sponsored Prompts in EU stores.
- Featured offer: measurable effect of the July 2026 gate removal on brand owners' Buy Box share; watch through end of 2026.
- US FBA 3.5% fuel and logistics surcharge (2026-04-17): confirm or drop.
- Vine fee change for products under USD 100 (March 2026): confirm or drop.
- AMC paid features pricing from 2027.
- Amazon Ads unified Campaign Manager general availability and DSP minimums.
- bol Advertising API version and any 2026 to 2027 Sponsored Products bidding changes.
- Turkish draft regulation on cargo liability and seller data portability: final text and dates.
- How Trendyol and Hepsiburada adapt onboarding and seller contracts before marketplace liability starts on 2027-03-02.
- Trendyol commission base (VAT-inclusive vs exclusive) and dynamic commissions: confirm from a seller panel.
- Zalando 2026 fee structure details (behind login).
- TikTok Shop Portugal launch date and Sell Across Europe availability date (2026-10-19 reported by one source).
- Amazon Haul seller access: invitation only vs Seller Central interest form.

## 12. Sources

1. 2026 Updates to US Referral and Fulfillment by Amazon Fees. Amazon Seller Forums. https://sellercentral.amazon.com/seller-forums/discussions/t/f3fa3211-820b-4e2e-a023-158a9cf55f99 (2025-12)
2. Amazon Fee Changes 2026. Seller Snap. https://sellersnap.io/amazon-fee-changes-and-updates/ (2026)
3. Amazon FBA Fees 2026, April 17 Surcharge Update. AMZ Prep. https://amzprep.com/amazon-fba-fees/ (2026)
4. Amazon's 2026 Fee Update: 3 Things to Know. Feedvisor. https://feedvisor.com/resources/amazon-trends/amazon-2026-fee-updates/ (2025-12)
5. Update to European Referral and Fulfilment by Amazon fees for 2026. Amazon EU. https://www.aboutamazon.eu/news/empowering-small-business/update-to-european-referral-and-fulfilment-by-amazon-fees-for-2026 (2025-12)
6. EU referral and FBA fee reductions to apply January 5. Amazon Seller Forums. https://sellercentral.amazon.com/seller-forums/discussions/t/a3b6d192-d78f-4b16-add1-e251e8959783 (2025-12)
7. Amazon to Lower Fees for European Sellers. EcommerceBytes. https://www.ecommercebytes.com/2025/12/02/amazon-to-lower-fees-for-european-sellers/ (2025-12-02)
8. Amazon brings forward EU referral and FBA fee cuts to January 5, 2026. ChannelMAX. https://www.channelmax.net/article/amazon-brings-forward-eu-referral-and-fba-fee-cuts-to-january-5-2026-channelmax (2025-12)
9. Amazon cuts Featured Offer eligibility gate starting July 2026. PPC Land. https://ppc.land/amazon-cuts-featured-offer-eligibility-gate-starting-july-2026/ (2026-07)
10. Amazon Featured Offer Eligibility Changes in 2026. BQool. https://blog.bqool.com/amazon-featured-offer-eligibility-changes/ (2026-07)
11. Amazon removes seller-performance gate for the Featured Offer. Nova Analytics. https://novadata.io/resources/news/amazon-featured-offer-eligibility-gate-removed-july-2026 (2026-07)
12. Amazon Policy Tracker 2026. Autopilot Brand. https://www.autopilotbrand.com/resources/amazon-policy-tracker (2026)
13. Amazon FBA Capacity Limits guide 2026. AMZ Prep. https://amzprep.com/amazon-fba-capacity-cut-seller-guide/ (2026)
14. Amazon Haul offers over a million items under USD 10. About Amazon. https://www.aboutamazon.com/news/retail/amazon-haul-ultra-low-prices-under-10 (2025)
15. What Is Amazon Haul? The Complete 2026 Guide for Sellers. SoldScope. https://www.soldscope.com/blog/what-is-amazon-haul (2026)
16. Amazon's newest AI tool is designed to enhance product listings. TechCrunch. https://techcrunch.com/2025/05/08/amazons-newest-ai-tool-is-designed-to-enhance-product-listings (2025-05-08)
17. Amazon upgrades generative AI seller listing assistance. Chain Store Age. https://chainstoreage.com/amazon-upgrades-generative-ai-seller-listing-assistance (2025-05)
18. unBoxed 2025 keynote recap. Amazon Ads. https://advertising.amazon.com/library/news/unboxed-2025-recap (2025-11)
19. Boost advertising efficiency with Ads Agent. Amazon Ads. https://advertising.amazon.com/resources/whats-new/unboxed-2025-introducing-ads-agent (2025-11)
20. Unlock insights with AMC's expanded ad traffic lookback window. Amazon Ads. https://advertising.amazon.com/en-gb/resources/whats-new/unboxed-2025-expanded-ad-traffic-lookback-window (2025-11)
21. Everything Amazon Announced at unBoxed 2025. Pacvue. https://pacvue.com/blog/unboxed-2025-what-amazons-ai-powered-future-means-for-advertisers/ (2025-11)
22. Amazon now lets AMC users query 1P paid features for free until end of 2026. PPC Land. https://ppc.land/amazon-now-lets-amc-users-query-1p-paid-features-for-free-until-end-of-2026/ (2026)
23. Sponsored Display, now part of display ads. Amazon Ads. https://advertising.amazon.com/solutions/products/sponsored-display (2026)
24. Amazon tightens view attribution as ROAS reporting splits. PPC Land. https://ppc.land/amazon-tightens-view-attribution-as-roas-reporting-splits/ (2026-01)
25. Amazon quietly tightened attribution. Code3. https://code3.com/resources/amazon-quietly-tightened-attribution-and-its-changing-how-dsp-performance-is-measured/ (2026)
26. Advertising in the age of Rufus: Sponsored Product Prompts. Acadia. https://acadia.io/advertising-in-the-age-of-rufus-breaking-down-sponsored-product-prompts (2026-03)
27. Alexa for Shopping (Amazon Rufus): complete guide. Perpetua. https://perpetua.io/blog-alexa-for-shopping-amazon-rufus-the-complete-guide-for-brands-and-sellers/ (2026)
28. Alexa for Shopping (formerly Amazon Rufus) 2026. AMALYTIX. https://www.amalytix.com/en/knowledge/ai/amazon-rufus-guide-2026/ (2026)
29. Amazon Advertising's MCP Server enters open beta. W Media Research. https://wmediaresearch.com/2026/02/06/amazon-advertisings-mcp-server-enters-open-beta-what-does-it-mean-for-the-industry/ (2026-02-06)
30. Amazon Ads MCP Server debuts. Futurum Group. https://futurumgroup.com/insights/amazon-ads-mcp-server-debuts-streamlining-ai-managed-campaign-execution/ (2026)
31. Amazon introduces fees for third-party developer API access in 2026. PPC Land. https://ppc.land/amazon-introduces-fees-for-third-party-developer-api-access-in-2026/ (2025-11)
32. Amazon drops SP-API fees after developer pushback. PPC Land. https://ppc.land/amazon-drops-sp-api-fees-after-developer-pushback/ (2026-05)
33. selling-partner-api-samples. Amazon on GitHub. https://github.com/amzn/selling-partner-api-samples (2026)
34. Amazon Attribution. Amazon Ads. https://advertising.amazon.com/solutions/products/amazon-attribution (2026)
35. Amazon Brand Referral Bonus 2026: Complete Guide. SellerMetrics. https://sellermetrics.app/amazon-brand-referral/ (2026)
36. Amazon Advertising Benchmarks 2026. Autron. https://autron.ai/blog/amazon-advertising-benchmarks-2026 (2026)
37. Average ACOS by Amazon Category: 2026 Benchmarks. Eightx. https://eightx.co/blog/average-acos-by-amazon-category (2026)
38. The best Amazon CPC benchmarks for 2026. keywords.am. https://keywords.am/blog/amazon-cpc-benchmarks/ (2026)
39. Amazon Vine Program: The Ultimate Guide. BQool. https://blog.bqool.com/amazon-vine-program/ (2026)
40. Amazon Vine Program ROI in 2026. Velocity Sellers. https://www.velocitysellers.com/2026/05/23/amazon-vine-program-roi-critique/ (2026-05-23)
41. Amazon Prime Day 2026 date. About Amazon. https://aboutamazon.com/news/retail/amazon-prime-day-2026-date (2026)
42. Prime Big Deal Days 2026. About Amazon. https://www.aboutamazon.com/news/retail/prime-big-deal-days-best-deals-savings-2026 (2026)
43. More visibility for your Sponsored Products on mobile. bol Partner Platform. https://partnerplatform.bol.com/en/nadp/more-visibility-on-mobile (2026-08-27)
44. How sponsored products works. bol Leveranciersplatform. https://leveranciers.bol.com/en/need-help/advertising-via-bol/how-sponsored-products-works/ (2026)
45. Display Offsite. bol Retail Media. https://retailmedia.bol.com/en/offsite-display/ (2026)
46. Retailer API release schedule. bol. https://api.bol.com/retailer/public/Retailer-API/release-planning.html (2026)
47. Deprecation: Commission Beta Endpoint. bol developers. https://developers.bol.com/en/news/deprecation-commission-beta-endpoint/ (2026-01)
48. New LVB tariffs for small sizes from 9 September 2026. Maximus. https://www.maximusnl.com/post/nieuwe-lvb-tarieven-voor-kleine-formaten-per-9-september-2026 (2026-09)
49. Commissies bol.com 2026. Boloo. https://www.boloo.co/blog/commissies-bol-com (2026)
50. Trendyol Komisyon Oranları 2026. Sentos. https://www.sentos.com.tr/trendyol-komisyon-oranlari/ (2026-07)
51. 2026 Trendyol Komisyon Oranları. Paraşüt. https://www.parasut.com/blog/trendyol-magaza-komisyon-oranlari (2026)
52. Trendyol Kargo Ücretleri 2026. Sentos. https://www.sentos.com.tr/trendyol-kargo-ucretleri-ve-kargo-entegrasyonu/ (2026-09)
53. Trendyol Influencer Pazarlama SSS. Trendyol. https://tms.trendyol.com/sss (2026)
54. Trendyol'da Reklam Vermek 2026. Ticimax. https://www.ticimax.com/blog/trendyol-reklam-verme (2026)
55. Hepsiburada Komisyon Oranları 2026. Paraşüt. https://www.parasut.com/blog/hepsiburada-komisyon-oranlari (2026)
56. Hepsiburada Announces Fourth Quarter and Full Year 2025 Financial Results. GlobeNewswire. https://www.globenewswire.com/news-release/2026/02/26/3246201/0/en/Hepsiburada-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results.html (2026-02-26)
57. Hepsiburada announces the closing of the change of control. StockTitan. https://www.stocktitan.net/news/HEPS/hepsiburada-announces-the-closing-of-the-change-of-control-zp2hpk3iq61n.html (2025-01)
58. Kaspi.kz injects extra USD 100M in Hepsiburada. AIM Group. https://aimgroup.com/2025/12/17/kaspi-kz-injects-extra-100m-in-hepsiburada/ (2025-12-17)
59. Trendyol commitments accepted by the Competition Authority. Mondaq. https://www.mondaq.com/turkey/antitrust-eu-competition/1552398/trendyolun-sundu%C4%9Fu-taahh%C3%BCtler-rekabet-kurumu-taraf%C4%B1ndan-uygun-bulundu (2024-10)
60. Recent developments in Turkish e-commerce law. Paksoy. https://paksoy.av.tr/en/2025/06/recent-developments-in-turkish-e-commerce-law/ (2025-06)
61. Announcement on the update of monetary thresholds under Law 6563. Ticaret Bakanlığı. https://ticaret.gov.tr/duyurular/6563-sayili-elektronik-ticaretin-duzenlenmesi-hakkinda-kanun-kapsaminda-parasal-esik-degerlerin-guncellenmesine-iliskin-aciklama (2026-03-02)
62. Constitutional Court decision on e-commerce platform liability. Esin Attorney Partnership. https://www.esin.av.tr/tr/2026/06/25/anayasa-mahkemesinden-e-ticaret-sektoru-icin-onemli-iptal-karari/ (2026-06-25)
63. AYM E.2024/187 K.2026/42 analysis. Av. Mete Şahin. https://www.avukatmetesahin.com/post/aym-e-2024-187-k-2026-42-e-ticaret-pazar-yeri-sorumlulugu (2026)
64. Ticari Reklam Yönetmeliği amendment. Resmî Gazete. https://www.resmigazete.gov.tr/eskiler/2026/07/20260701-9.htm (2026-07-01)
65. Türkiye amendments to the Commercial Advertising and Unfair Commercial Practices Regulation. CMS. https://cms.law/en/tur/legal-updates/turkiye-launches-new-era-of-digital-advertising-with-amendments-to-the-commercial-advertising-and-unfair-commercial-practices-regulation (2026-07)
66. E-Ticaret Panorama: draft regulation. Sentos. https://www.sentos.com.tr/e-ticaret-panorama-yonetmelik-taslagi-agustos-2026-2/ (2026-08)
67. trendyol-integration-developer-tool. Trendyol on GitHub. https://github.com/Trendyol/trendyol-integration-developer-tool (2026)
68. trendyol-mcp (read-only Trendyol and Hepsiburada). GitHub. https://github.com/acar32furkan-glitch/trendyol-mcp (2026)
69. Changes for sellers in the coming months. Allegro help. https://help.allegro.com/en/sell/a/changes-for-sellers-in-the-coming-months-6MEOVaK1Yf9 (2026)
70. We have introduced the changes for sellers announced for March 2. Allegro help. https://help.allegro.com/en/sell/a/we-have-introduced-the-changes-for-sellers-announced-for-march-2-LRX2qelRjIg (2026-03)
71. Allegro has 4.2 million international customers. Ecommerce News EU. https://ecommercenews.eu/allegro-has-4-2-million-international-customers/ (2025)
72. ZEOS fee summary. Zalando Partner University. https://partner.zalando.com/university/article/zeos-fee-summary (2026)
73. Zalando Partner Program fees guide 2026. Marqetir. https://marqetir.com/fees/zalando-fees (2026)
74. Etsy ups regulatory operating fees. Value Added Resource. https://www.valueaddedresource.net/etsy-ups-regulatory-operating-fees/ (2026-06)
75. eBay raises currency conversion fees. Value Added Resource. https://valueaddedresource.net/ebay-raises-currency-conversion-fees (2026-09)
76. Selling fees. eBay. https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822 (2026)
77. New-Seller Savings 2026. Walmart Marketplace. https://marketplace.walmart.com/new-seller-savings-2026/ (2026)
78. Fulfilled by noon (FBN) fees in UAE. noon Partners. https://helpcenter.noon.partners/en/category/fulfilled-by-noon-fbn/fulfilled-by-noon-fbn-fees-in-uae (2026)
79. Fulfilled by noon (FBN) fees in KSA. noon Partners. https://support.noon.partners/portal/en/kb/articles/fulfilled-by-noon-fbn-fees-in-ksa (2026)
80. TikTok Shop expands across Europe. TikTok Newsroom. https://newsroom.tiktok.com/tiktok-shop-expands-across-europe?lang=en-150 (2026-06)
81. TikTok Shop opens 4 EU markets and a Sell Across Europe tool. Nova Analytics. https://novadata.io/resources/news/tiktok-shop-europe-4-countries-sell-across-europe-june-2026 (2026-06)
82. Top Amazon MCP Servers for Ads and Seller Data (2026). Marketplace Ad Pros. https://marketplaceadpros.com/guides/top-amazon-mcp-servers-2026/ (2026)
83. Hepsiburada BuyBox rules and tips. Sentos. https://www.sentos.com.tr/hepsiburada-buybox-nasil-alinir-kurallar-ve-ipuclari/ (2026)
84. Trendyol Buybox guide. Sentos. https://www.sentos.com.tr/trendyol-buybox-nedir-nasil-kazanilir/ (2026)
