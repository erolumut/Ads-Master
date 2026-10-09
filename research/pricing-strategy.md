# Research Dossier: Pricing Strategy (Commercial Pricing Consultant)

> Research date: 2026-10-09. Scope: price level and positioning, competitive price benchmarking, cost to serve and margin waterfall (Netherlands and Turkey focus, EU context), minimum basket and delivery policy, price architecture and pack sizes, value based pricing and willingness to pay, channel price corridors (DTC, retail, marketplace, wholesale) and competition law limits, price changes and inflation pricing, elasticity and price tests, dynamic and personalized pricing rules, SaaS and B2B pricing, pricing tools and APIs.
>
> Method and limits: 32 web searches (extended mode for 2026 facts, rates and niche topics; standard mode for established research). Direct page fetching (WebFetch) failed with DNS errors in the research environment, so 2025 to 2026 findings rely on the content of search results from the listed pages (official PDFs and pages where they surfaced, trade bodies, law firms, vendor and press coverage), not full page reads. Classic academic and legal sources are cited from prior knowledge and marked so. Every claim carries an evidence label; anything single sourced or conflicting is marked [Unverified] or [Contested]. The offer-strategy dossier (`research/offer-strategy.md`, 2026-10-08) covers incentive mechanics, promo calendars and much of pricing law; this dossier links to it rather than repeating it.

## 1. Executive summary

1. Cost to serve per order, not cost per unit, decides whether low price consumables can be sold DTC. Dutch box parcels cost about EUR 6.65 to 7.40 ex VAT for small and mid volume business senders in 2026 (PostNL business rates), letterbox parcels EUR 4.40 to 4.55 (PostNL, rising mid year), and fixed payment fees such as iDEAL (EUR 0.29 at Stripe) add a fixed cost per order [Official, 2026]. Single bar or single item orders usually lose money even when a delivery fee is charged, which makes the minimum basket an arithmetic result, not a marketing choice.
2. Carrier surcharges are now material and volatile: DHL eCommerce Netherlands applied a fuel surcharge of 22.75% in July, 23.50% in August and 28.00% in September 2026, linked to CBS diesel prices [Official, 2026-09]. Base rate quotes without surcharges understate cost by a quarter.
3. The EU Court of Justice clarified on 2026-04-09 (C-62/25) that flat handling or delivery charges applying only below a minimum order amount do not have to be included in the selling price under the Price Indication Directive, provided they are avoidable and clearly stated before checkout [Official, via Thuiswinkel.org 2026-04-22]. This legitimizes "small order fee" designs that are displayed clearly.
4. Price realization remains the weak link of pricing programs: Simon-Kucher's Global Pricing Study 2025 (over 2,200 respondents, 28 countries) reported average realization of planned increases down to 43%, and only about half of companies with indexation clauses enforce them [Study, 2025-06]. Bain found list price increases matched or exceeded input cost increases at 55% of companies [Study, 2025].
5. AI in pricing is moving from analysis to agents, slowly: McKinsey's AI in Pricing survey (November 2025, n = 419) found gen AI use at roughly 10 to 30% of pricing organizations and agentic AI under 10%, expected to reach 20 to 45%, led by market intelligence and cost tracking [Study, 2026-04]. Vendors followed: Competera launched an agentic store level pricing assistant (2026-02-19) and Pricefx launched Pricefx Agents with its Accelerate conference on 2026-10-13 to 15 [Vendor, 2026].
6. Left digit bias is real and underexploited: scanner data on about 3,500 products in 25 US chains show consumers react to a 1 cent increase above a 99 ending like a 15 to 25 cent increase, and retailers forgo 1 to 4% of potential gross profit by underreacting (Strulov-Shlain, Review of Economic Studies) [Study]. Decoys and choice overload, by contrast, are weak in realistic settings [Study].
7. Quantity surcharges (bigger pack costs more per unit) appear in roughly 10 to 34% of multi-size products across studies while most shoppers assume bigger is cheaper; regulators and media are spotlighting them (New Zealand coverage 2026-09; UK Price Marking Order reform 2026-04-06) [Study and Official]. Shrinkflation disclosure laws now exist in France (2024-07-01) and Austria (2026-04-01), and a German court found Mondelez's Milka downsizing misleading (reported 2026-05) [Official and Press].
8. Turkey requires an inflation operating rhythm: CPI was 29.73% year on year in September 2026 (first time under 30% in 57 months; food 27.62%), USD/TRY about 49.17 on 2026-10-06, and the Ministry of Trade imposed about TRY 2.6B in administrative fines across about 360,000 firms in the first nine months of 2026, including TRY 399.5M for excessive pricing [Official via press, 2026-10]. Price changes need a documented cost index; discount advertising uses the prior 10 day lowest price from 2026-08-01 [Official via secondary].
9. Resale price maintenance remains the line pricing advice must not cross: EU fines on Gucci, Chloé and Loewe (EUR 157.4M, 2025-10-14), Italy's Morellato (2026-03-17, online price monitoring used to police discounts) and Turkish Competition Board tire sector decision on 2026-06-04 (Brisa TRY 1.019B, RPM among the issues) [Official and press]. Channel conflict is solved with own channel corridors and exclusive assortments.
10. SaaS pricing is shifting to hybrid and AI credits: 37% of 230 companies use hybrid pricing (heading toward 47%), 29% already have AI credits or tokens, and investors prefer hybrid, outcome and usage models over seats (Growth Unhinged 2026) [Study, 2026]. Personalized pricing based on personal data faces disclosure in the EU and restrictions in several US states, with the EU Digital Fairness Act proposal still pending (planned late 2026; 77% of consultation respondents supported restricting it) [Official].

## 2. State of the domain in 2026 (with numbers)

### 2.1 Cost to serve inputs, Netherlands

| Item | 2026 figure | Source | Label |
|------|-------------|--------|-------|
| PostNL business domestic parcel by annual volume | EUR 7.40 (100 to 250), 7.35 (250 to 500), 7.30 (500 to 1,000), 7.00 (1,000 to 2,500), 6.85 (2,500 to 5,000), 6.65 (5,000 to 10,000); custom above 10,000; ex VAT | PostNL Zakelijke Pakkettarieven 2026 | [Official] |
| PostNL brievenbuspakje+ online franking | EUR 4.40 (January 2026); EUR 4.55 (tariff book from 2026-07-12) | PostNL tariff folder and tariff book | [Official] |
| Small sender letterbox rate (under 500 per year) | EUR 4.40 to 4.55 reported | Thuiswerkadvies | [Unverified] |
| Consumer parcel rates | EUR 6.95 to 8.25 depending on source | Blogs | [Contested]; consumer, not business |
| Sendcloud start rates | From EUR 2.99 PostNL, EUR 3.67 DHL, EUR 3.38 DPD | Sendcloud | [Vendor] |
| Sendcloud platform fees | Subscription EUR 0 to 799 plus EUR 0.08 to 0.12 per label (reports differ) | Reviews | [Unverified] |
| DHL eCommerce NL fuel surcharge | 29.50% (May), 26.50% (June), 22.75% (July), 23.50% (August), 28.00% (September 2026) | dhlecommerce.nl | [Official] |
| DHL Freight NL fuel surcharge (road freight, not parcels) | 31.50% (October 2026) | dhl.com | [Official]; do not confuse |
| DHL eCommerce domestic extras | Wadden Islands EUR 6.00, manual handling EUR 3.95, energy surcharge (amount not confirmed) | QLS | [Unverified] |

### 2.2 Cost to serve inputs, Turkey

| Item | 2026 figure | Source | Label |
|------|-------------|--------|-------|
| Yurtiçi Kargo list 0 to 1 desi same city | About TRY 154 to 209 (Sentos); TRY 167 (0 desi) and 226.50 (1 desi) (Kargonomi) | Third party lists | [Unverified, conflicting] |
| Aras Kargo list 1 desi | TRY 163.26 (Sentos, updated 2026-07-17); TRY 149.54 ex KDV in city from 2026-01-01 (Kargonomi) | Third party lists | [Unverified] |
| Trendyol contracted cargo, 1 to 5 desi | Yurtiçi TRY 112.77 to 142.91; Aras TRY 83.93 to 111.70 | Dopigo, Kargo Entegratör | [Unverified] |
| Reason sources differ | KDV included vs excluded; 2025 vs 2026 lists; contracted vs list | Analysis of sources | [Practitioner consensus] |

### 2.3 Payment fees

| Provider | 2026 figure | Label |
|----------|-------------|-------|
| Stripe NL | Standard EEA cards 1.5% + EUR 0.25; premium EEA cards 2.8% + EUR 0.25; iDEAL (iDEAL Wero) EUR 0.29, +2% if currency conversion | [Official] |
| Stripe iDEAL guide | Wero available to Dutch shoppers in late 2026; iDEAL Wero fully transitions to Wero by 2028 | [Official] |
| Mollie | iDEAL EUR 0.29 (most sources) vs EUR 0.32 (a June 2026 verified listing); EU consumer cards 1.8% + EUR 0.25; commercial EEA 2.9% + EUR 0.25; non-EEA 3.25% + EUR 0.25 | [Contested] |
| Adyen | Interchange++ with about 0.60% markup and EUR 0.10 to 0.13 per transaction; iDEAL about EUR 0.22; minimum invoice reported EUR 100 to 1,000; chargeback up to EUR 25 | [Unverified] |
| iyzico | Single payment about 1.95% most cited (range 1.19% to 2.99% + TRY 0.25); 12 installments about 3.45% | [Unverified] |
| PayTR | Single payment 1.49% to 2.89% most cited; settlement terms change effective cost | [Unverified] |

### 2.4 Marketplace fees (summary)

| Marketplace | 2026 change or figure | Label |
|-------------|----------------------|-------|
| Amazon EU | From 2026-01-05: grocery and gourmet 8% to 5% up to EUR 10; vitamins and supplements 5% in that tier; Low-Price FBA extended to most categories up to EUR 20 (about EUR 0.45 lower per unit for newly eligible items); home 15% to 8% up to EUR 20; pet 15% to 5% up to EUR 10; clothing 5% up to EUR 15 and 10% EUR 15 to 20 (from 2025-12-15); FBA parcel fees down about EUR 0.32 on average in five markets; average fee cut about EUR 0.17 per unit | [Official] |
| Amazon EU | 1.5% surcharge on FBA fulfilment fees from 2026-04-17; small increases to storage and returns fees | [Unverified, third party] |
| bol.com | Fixed fee per item EUR 0.20 (under EUR 10), 0.40 (EUR 10 to 20), 0.85 (over EUR 20), EUR 2.48 for large electronics over EUR 20; category commission about 4% to 21% (12.4% often cited); commission ex VAT with 21% VAT on top | [Unverified, conflicting sources] |
| Trendyol | Supermarket and food 10% to 15% (Paraşüt, 2026-01-14 rates) or 15.25% for snacks (Sentos, Ideasoft); service fee described as 3.49% or TRY 6.99 to 10.99 per shipment | [Unverified, conflicting] |

### 2.5 VAT

- Netherlands 21% standard, 9% reduced for most food [Official, prior knowledge].
- Turkey 20% standard, 10% and 1% reduced; basic food at 1% since 2022; classification of snacks and protein bars not confirmed in this research [Unverified].

### 2.6 Retail margins

- Agency sources cite conventional grocery retailer margins of 25 to 35% of shelf price, convenience 35 to 45%, mass 20 to 30% [Unverified]. A CPG guide cites 30 to 45% [Unverified]. New Zealand dry grocery suppliers claimed 35 to 41% (2023) [Unverified]. Public grocer gross margins sit at 22 to 28% on total sales (Kroger, Publix, Shoprite) and are not comparable to single branded snack margins [Press and filings].
- No verified Dutch retailer margin figures were found; Dutch supermarkets are known for hard supplier negotiations and buying alliances [Press]. The method therefore asks the brand for its actual sell-in price.

### 2.7 Pricing practice and evidence

- Simon-Kucher GPS 2025: realization 43%, indexation 53% (half enforce) [Study, 2025-06].
- Bain commercial and revenue growth agenda 2025: list increases matched input costs at 55%; reps with data driven guidance almost twice as confident in realizing increases [Study, 2025].
- McKinsey AI in Pricing survey, November 2025, n = 419, article 2026-04-07 [Study].
- Left digit: Strulov-Shlain (REStud) [Study]; 99 ending rigidity (UChicago thesis 2024) [Study, unreviewed].
- Quantity surcharges and inattention: Binkley and Bejnarowicz; URI survey 76.6% of 400 households assume larger is cheaper per unit; median large pack sales fall only 14.4% during surcharges [Study, older]; New Zealand coverage 2026-09 [Press on study].
- Contingent free shipping lifts basket size and merchandise profit vs unconditional free shipping (Chen and Ngwe, HBS 2019) [Study].

### 2.8 Turkey macro and enforcement

- CPI September 2026: 29.73% y/y, 1.84% m/m, 24.32% year to date, 12 month average 31.49%; food 27.62%, transport 35.10%, housing and energy 39.99%; core (B) 29%; PPI 27.38% [Official via press, 2026-10-05].
- USD/TRY 49.03 (2026-10-01) to 49.17 (2026-10-06), free market quotes [Press].
- Ministry of Trade: about 360,000 firms and 44 million products inspected in nine months; about TRY 2.6B fines; internal trade TRY 724.7M across 6,072 parties including TRY 399.5M for excessive pricing; consumer protection about TRY 984M [Press, 2026-10]. Haksız Fiyat Değerlendirme Kurulu fined 1,258 businesses TRY 389.4M for excessive increases by May 2026 [Press].
- E-commerce law administrative fines raised 25.49% for 2026 [Press].
- Competition Board: tire sector decision 2026-06-04 (Brisa TRY 1.019B; RPM, regional and customer restrictions investigated); earlier RPM decisions (Seher Gıda settlement TRY 173.8M; Eti, Haribo, Kent, Şölen) [Press and law firms].

### 2.9 Pricing law signals relevant to price level work

- CJEU C-62/25 (2026-04-09) on delivery and handling charges below minimum order [Official via trade body].
- EU Digital Fairness Act: not tabled as of 2026-10-09; planned end of 2026; consultation: 77% support for restricting personalized pricing based on personal data, 79% (of those wanting action) for banning drip pricing; consumer authorities split on a general personalization restriction (33% support) [Official consultation summary].
- Shrinkflation: France since 2024-07-01; Austria 2026-04-01 to 2030-06-30 (notice for 60 days when unit price rises more than 3% due to quantity reduction; fines up to EUR 2,500 per product, EUR 10,000 total); Germany court rulings; Italy delayed after Commission objections; Turkey handles under consumer law [Official summaries and press, 2026].
- Turkey prior price rules (10 days) and UK, US personalized and drip pricing rules: see offer-strategy dossier.

## 3. Timeline of changes, January 2025 to October 2026

| Date | Change | Impact on pricing work | Label |
|------|--------|------------------------|-------|
| 2025-01-01 | Minnesota all-in pricing law | Headline prices include mandatory fees | [Official, via offer-strategy] |
| 2025-04-06 | UK DMCC unfair practices regime (drip pricing blacklisted) | Total price upfront | [Official] |
| 2025-06 | Simon-Kucher Global Pricing Study 2025 published | 43% realization benchmark | [Study] |
| 2025-07-08 | FTC click to cancel rule vacated | Subscription price change rules rely on states and ROSCA | [Official] |
| 2025-09 | Simon-Kucher Growth Blueprint redefines pricing power as precision | Practice framing | [Practitioner] |
| 2025-10-11 | Turkey price tag prior price lookback 30 to 10 days | Turkish reference prices | [Official via secondary] |
| 2025-10-14 | EU fines Gucci, Chloé, Loewe EUR 157.4M for RPM | Channel corridor limits | [Official] |
| 2025-10-24 | DFA consultation closes | Personalization and drip pricing direction | [Official] |
| 2025-11 | McKinsey AI in Pricing survey fielded (n = 419) | AI adoption benchmark | [Study] |
| 2025-11-10 | New York Algorithmic Pricing Disclosure Act in force | Personalized price disclosure | [Official] |
| 2025-12-02 | Amazon announces 2026 EU fee cuts | Marketplace pack economics | [Official] |
| 2025-12-15 | Amazon EU clothing referral cuts effective | Fees | [Official] |
| 2026-01-01 | PostNL 2026 business parcel rates; Aras list update; Colorado all-in pricing | Cost basis | [Official and Unverified] |
| 2026-01-05 | Amazon EU grocery 5% up to EUR 10; Low-Price FBA to EUR 20 | Fees for low price items | [Official] |
| 2026-01-08 | New York AG letter to Instacart on algorithmic pricing | Price test risk | [Official] |
| 2026-01-14 | Trendyol standard commission rates used by Paraşüt analysis | Turkish marketplace fees | [Unverified] |
| 2026-02-19 | Competera AI Pricing Assistant (store level, agentic) | Tools | [Vendor] |
| 2026-03-17 | Italy AGCM fines Morellato (online discount caps via monitoring) | Monitoring limits | [Official] |
| 2026-04-01 | Austria Anti-Deceptive Packaging Act in force | Pack changes | [Official summary] |
| 2026-04-06 | UK Price Marking Order reforms | Unit pricing scope | [Official, via offer-strategy] |
| 2026-04-07 | McKinsey "B2B pricing: navigating the next phase of the AI revolution" | AI in pricing | [Study] |
| 2026-04-09 | CJEU C-62/25 judgment on delivery costs below minimum order | Delivery policy display | [Official via trade body] |
| 2026-04-17 | Amazon FBA 1.5% fulfilment fee surcharge reported | Fees | [Unverified] |
| 2026-04 to 05 | Growth Unhinged 2026 SaaS monetization survey fielded | SaaS benchmarks | [Study] |
| 2026-05 | Mondelez Milka shrinkflation ruling reported in Germany | Pack changes | [Press] |
| 2026-05 | DHL eCommerce NL fuel surcharge 29.50% | Carrier cost | [Official] |
| 2026-06-04 | Turkish Competition Board tire sector decision (Brisa TRY 1.019B) | RPM risk in Turkey | [Press] |
| 2026-06-30 | Shopify Scripts sunset | Discount logic moves to Functions | [Official, via offer-strategy] |
| 2026-07-01 | EU EUR 3 duty per item type on low value parcels; Connecticut all-in pricing | Cross-border landed cost | [Official] |
| 2026-07-12 | PostNL tariff book: letterbox parcel EUR 4.55 online | Cost basis | [Official] |
| 2026-07-17 | Aras Kargo list update (per Sentos) | Turkish cost | [Unverified] |
| 2026-08-01 | Turkey 10 day prior price rule for discount ads | Repricing and promo timing | [Official via secondary] |
| 2026-09 | DHL eCommerce NL fuel surcharge 28.00% | Carrier cost | [Official] |
| 2026-09 | New Zealand quantity surcharge research coverage | Unit price scrutiny | [Press on study] |
| 2026-09-22 | Pricefx announces Accelerate 2026 with Pricefx Agents in production | Tools | [Vendor] |
| 2026-10-01 | Maryland surveillance pricing law (food retail) | Personalized pricing | [Official, via offer-strategy] |
| 2026-10-05 | TÜİK: CPI 29.73% y/y for September 2026 | Turkish repricing | [Official via press] |
| 2026-10-06 | USD/TRY about 49.17 | FX input | [Press] |
| 2026-10 | Ministry of Trade nine month enforcement report (TRY 2.6B fines) | Unfair price risk | [Press] |
| 2026-10-13 to 15 | Pricefx Accelerate conference | Watch for agent releases | [Vendor] |
| 2026 Q4 (planned) | Digital Fairness Act proposal | Personalization, drip pricing, "from" prices | [Official plan] |
| Late 2026 | Wero available to Dutch shoppers via Stripe | Payment fee mix | [Official] |
| 2028 | iDEAL Wero fully transitions to Wero | Payment fee mix | [Official] |

## 4. Best practice consensus

| Practice | Why | Evidence |
|----------|-----|----------|
| Build the margin waterfall per basket size before setting prices | Fixed costs per order dominate small baskets | Carrier and PSP rate structures [Official]; practitioner consensus |
| Normalize competitor prices per unit and per value unit, separating promo from regular | Raw prices mislead | Unit pricing law (Directive 98/6/EC); practitioner consensus |
| Use value for the ceiling, cost for the floor, competition for the comparison | Avoids cost plus underpricing and competitor following | Pricing literature [Practitioner consensus] |
| Design price ladders with falling per unit price and rising contribution per order | Trust and economics | Quantity surcharge research [Study] |
| Respect left digits; choose endings by positioning | Measurable demand effects | Strulov-Shlain; Anderson and Simester [Study] |
| Set thresholds from economics and align them with ladder rungs | Contingent free shipping lifts baskets; dead zones erode contribution | Chen and Ngwe; Lewis et al. [Study] |
| Manage channel conflict with assortment, not reseller price control | RPM is a hardcore infringement | EU, Italy, Turkey decisions [Official] |
| Index prices in inflation markets with documented cost evidence | Margin erosion and unfair price enforcement | TÜİK data; Ministry of Trade enforcement [Official] |
| Use lawful price test designs and contribution metrics | Trust and validity | NY AG Instacart letter; EU disclosure [Official] |
| Grandfather and communicate increases | Churn and legal exposure | Practitioner consensus; subscription law |

## 5. Contested topics (both sides)

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Charm (99) endings for premium brands | Left digit effects lift demand broadly | Round prices signal quality and fit hedonic purchases (Wadhwa and Zhang 2015) | Endings follow positioning; never cross a left digit for small gains |
| Free delivery thresholds | Lift basket size and profit (Chen and Ngwe; Groningen dataset) | Padding and returns, dead zones (Shehu et al. 2020; single shop reports) | Economic floor from script, align with hero rung, test with returns guardrail |
| Retailer margin assumptions | Planning ranges (25 to 35%) are good enough | Ranges are unsourced and vary widely (22% to 45%) | Always use the actual sell-in price |
| Visitor level price tests | Fastest causal answer | Trust, feed mismatch, disclosure laws, Instacart backlash | Prefer pack, time, geo designs |
| Price monitoring of resellers | Information is lawful and useful | Monitoring has featured in RPM cases (Morellato) | Information only; never linked to supply or pressure |
| Credits for AI SaaS | Flexible, aligns cost and value | Confusing, bill shock (Zylo report, Unverified), described as a bridge | Hybrid base fee plus credits with clear examples |
| Usage based adoption rates | 38% to 42% adoption in 2026 | 18% in another report | Definitions differ; use own segment data |
| Mollie iDEAL fee | EUR 0.29 | EUR 0.32 | Check the live page or dashboard |
| Dynamic pricing tools for SMB | Automation saves time and margin | Auto-repricing errors and legal display risks | Recommend bounds; human approves any automatic action |

## 6. What top operators do differently

- They compute contribution per order across basket sizes and ladder rungs, and know the share of orders below the minimum viable basket.
- They price DTC next to retail with a written corridor for their own channels and DTC exclusive packs, so retail buyers see a different assortment, not a lower price.
- They state every cost with its "as of" date, refuse to compute with missing costs, and keep margin_on_price and markup_on_cost separate.
- They review carrier surcharges monthly and design packs for cheaper carrier formats (letterbox).
- They benchmark effective (promo weighted) competitor prices, not just regular prices.
- They reprice in Turkey on a cost index with a band, keep an evidence file, and time discounts around the 10 day rule.
- They choose price endings by positioning and avoid small left digit crossings.
- They present the owner with options, consequences and the downside case, and log decisions.

## 7. Common expensive mistakes

1. Selling single units DTC at a retail-like price: negative contribution after carrier and fixed payment fees.
2. Free delivery thresholds below the minimum viable basket, or thresholds a few euros above the hero price.
3. DTC multi-packs priced 20 to 30% below the retail shelf per unit on the same product, provoking retailer retaliation.
4. Margin sheets on VAT inclusive prices, or confusing margin and markup.
5. Base carrier rates without fuel and energy surcharges.
6. Competitor comparisons mixing promo and regular prices or ignoring per 100 g unit prices on shelf.
7. MAP or "minimum price" emails to EU or Turkish resellers.
8. Shrinkflation without disclosure in France or Austria.
9. Old Turkish cost bases after FX and inflation moves; frequent small increases followed by discounts.
10. Visitor level list price tests with feed mismatches.

## 8. Benchmarks (source, date, caveat)

| Benchmark | Value | Source, date | Sample | Caveat |
|-----------|-------|--------------|--------|--------|
| Average price realization | 43% | Simon-Kucher GPS, 2025-06 | Over 2,200 respondents, 28 countries, 39 industries | Survey, self reported |
| Contract indexation use | 53% (half enforce consistently) | Simon-Kucher, 2025-06 | Same | Same |
| List increase covered input cost increase | 55% of companies | Bain, 2025 | Survey | Self reported |
| Gen AI in pricing today | 10 to 30% of respondents | McKinsey, survey 2025-11 | 419 | B2B focus |
| Left digit effect | 1 cent over 99 ending read as 15 to 25 cents; 1 to 4% gross profit forgone | Strulov-Shlain, REStud | 3,500 products, 25 US chains | US grocery |
| Mean price elasticity | about -2.6 | Bijmolt et al. 2005 (prior knowledge) | 1,851 elasticities | Brand level, older |
| Price lever | 1% price = about 11% operating profit | Marn and Rosiello 1992 (prior knowledge) | Large companies | Old, average |
| Quantity surcharge prevalence | 10 to 34% of multi-size products | Multiple studies, NZ 2026 coverage | Store surveys | Older US data |
| SaaS hybrid pricing | 37% (toward 47%) | Growth Unhinged, 2026 | 230 companies | Survey |
| AI credits in SaaS pricing | 29% | Growth Unhinged, 2026 | 230 | Survey |
| Median AI gross margin target | 50% | Growth Unhinged, 2026 | 230 | Survey |
| Dutch online spend H1 2026 | EUR 17.1B flat; transactions +3% to 170.4M | Thuiswinkel Market Monitor via Emerce, 2026 | Market | Smaller baskets |
| Grocery retailer margin on shelf | 25 to 35% (cited) | Agency blog | n/a | [Unverified] |
| Turkey CPI | 29.73% y/y | TÜİK, 2026-10-05 | National | Monthly change |

## 9. Tools, APIs and MCP servers

| Tool | Type | Access | Notes |
|------|------|--------|-------|
| Prisync | Price monitoring (SMB, Shopify) | REST API v2, OpenAPI spec; API +20% on plan | Shopify app from USD 49; plans USD 99 to 399 reported |
| Price2Spy | Price monitoring | REST API (api.price2spy.com/rest/v1, Swagger); credentials via support; date range filters | Plan prices vary by source |
| Omnia Retail | Monitoring and dynamic pricing, EU | SMB from EUR 399 per month; enterprise custom | |
| Minderest | Monitoring | Custom | |
| Competera | Enterprise pricing optimization | Custom; agentic assistant 2026-02 | |
| DataWeave | Price and digital shelf | Custom | |
| Pricefx | Price management (B2B and B2C) | Custom; Pricefx Agents; connect enterprise LLMs | |
| Keepa | Amazon price history | Token API; community MCP servers on GitHub | |
| Apify actors | Scraping wrapped as MCP | Usage priced | Terms and breakage risk |
| Shopify Markets and catalogs | Rounding per market; fixed prices per market; B2B catalogs and price lists | Admin and GraphQL | Rounding settings admin only per community report |
| Google Merchant Center price competitiveness | Benchmark prices | Merchant API | Via commerce-feeds |
| Survey tools | Sawtooth, Conjointly, Qualtrics, Displayr | Paid | Conjoint, Van Westendorp |

No confirmed official MCP server from a price monitoring vendor as of 2026-10.

## 10. Official sources to monitor

- PostNL tariffs: postnl.nl/tarieven (business rate PDFs, tariff books).
- DHL eCommerce NL fuel surcharge index (monthly).
- Stripe, Mollie, Adyen, iyzico, PayTR pricing pages.
- aboutamazon.eu fee announcements; Seller Central fee pages; bol.com Verkoopaccount Tarieven; Trendyol and Hepsiburada seller panels.
- curia.europa.eu (C-62/25 and new price indication cases); EUR-Lex; European Commission DFA page.
- European Commission competition press releases; rekabet.gov.tr; ACM; CMA.
- TÜİK (CPI, monthly), TCMB (FX), ticaret.gov.tr, Resmî Gazete.
- Belastingdienst VAT; GİB KDV lists.
- Simon-Kucher, McKinsey, Bain pricing publications; Growth Unhinged.
- Vendor changelogs: Prisync, Price2Spy, Omnia, Competera, Pricefx; Shopify changelog.

## 11. Open questions and watch list

- Digital Fairness Act proposal text (late 2026): personalized pricing restrictions, "from" price bans, drip pricing ban.
- Whether more EU states adopt shrinkflation disclosure (Italy's rule delayed).
- Wero rollout effect on Dutch payment fees and checkout mix.
- PostNL letterbox parcel moving into the parcel network and future pricing.
- Amazon EU FBA surcharge confirmation; bol.com 2027 fee changes.
- Turkish disinflation path and whether the 10 day rule evolves; Competition Board RPM decisions in e-commerce.
- Agentic pricing tools (Pricefx, Competera) offering official MCP or API access for assistants.
- Snack and protein bar VAT classification in Turkey.
- Verified Dutch grocery retailer margins for branded snacks.

## 12. Sources

1. Zakelijke Pakkettarieven 2026, PostNL, https://www.postnl.nl/api/assets/blt43aa441bfc1e29f2/blt1ea4757b14457356/zakelijke-pakkettarieven-2026.pdf, 2026-01.
2. Tarieven voor post en pakketten vanaf januari 2026, PostNL, https://www.postnl.nl/api/assets/blt43aa441bfc1e29f2/blt90874f5ca0857405/def-tarievenfolder-2026.pdf, 2026-01.
3. Tarieven en diensten 12 juli 2026, PostNL, https://www.postnl.nl/api/assets/blt43aa441bfc1e29f2/blt5e65605bca8690e0/tarievenboekje-12-juli-2026.pdf, 2026-07.
4. PostNL maakt nieuwe postzegeltarieven bekend per 12 juli 2026, PostNL newsroom, https://newsroom.postnl.nl/nl-NL/266213-postnl-maakt-nieuwe-postzegeltarieven-bekend-per-12-juli-2026/, 2026.
5. PostNL maakt snelle post fors duurder, Accountancy Vanmorgen, https://www.accountancyvanmorgen.nl/2026/05/28/postnl-maakt-snelle-post-fors-duurder/, 2026-05-28.
6. PostNL tarieven 2026, Thuiswerkadvies, https://thuiswerkadvies.nl/blogs/postnl-tarieven-snelle-post-2026/, 2026.
7. Fuel surcharge index per month, DHL eCommerce NL, https://www.dhlecommerce.nl/en/business/support/shipping/fuel-surcharge, 2026-09.
8. DHL Surcharges 2026, QLS, https://knowledge.qls.nl/en/dhl-surcharges-2026, 2026.
9. DHL Freight surcharges Netherlands, DHL, https://www.dhl.com/nl-en/home/freight/help-center-for-european-road-and-rail/dhl-freight-surcharges.html, 2026-10.
10. Kortingen op verzendkosten, Sendcloud, https://www.sendcloud.com/nl/2025-campaign/, 2025 to 2026.
11. Yurtiçi Kargo Ücretleri 2026, Sentos, https://www.sentos.com.tr/yurtici-kargo-ucretleri-guncel-liste/, 2026.
12. Aras Kargo Ücretleri 2026, Sentos, https://www.sentos.com.tr/aras-kargo-ucretleri-guncel-liste/, 2026-07.
13. 2026 Yurtiçi Kargo Ücretleri, Kargonomi, https://www.kargonomi.com.tr/blog/yurtici-kargo-ucretleri-2026/, 2026.
14. Aras Kargo Ücretleri 2026, Kargonomi, https://www.kargonomi.com.tr/blog/aras-kargo-ucretleri/, 2026.
15. Trendyol Kargo Ücretleri 2026, Dopigo, https://www.dopigo.com/trendyol-kargo-ucretleri/, 2026.
16. Trendyol Kargo Fiyatları Ağustos 2026, Kargo Entegratör, https://kargoentegrator.com/blog/trendyol-kargo-fiyatlari-2026/, 2026-08.
17. Pricing and fees (Netherlands), Stripe, https://stripe.com/en-nl/pricing, 2026.
18. Local payment methods pricing, Stripe, https://stripe.com/en-nl/pricing/local-payment-methods, 2026.
19. iDEAL payments for businesses, Stripe, https://stripe.com/resources/more/ideal-an-in-depth-guide, 2026.
20. Mollie Pricing 2026, paymentgatewaycost.com, https://paymentgatewaycost.com/mollie-pricing/, 2026-06.
21. Mollie Review 2026, comparepsp.com, https://comparepsp.com/providers/mollie/, 2026.
22. Guide to Adyen Pricing 2026, Finexer, https://blog.finexer.com/adyen-pricing/, 2026.
23. Sanal POS Komisyon Oranları 2026, Moyduz, https://www.moyduz.com/blog/sanal-pos-komisyon-oranlari-2026, 2026.
24. iyzico POS Komisyon Oranları 2026, poskomisyonlari.com, https://poskomisyonlari.com/pos-firmalari/iyzico-pos-komisyon-oranlari, 2026.
25. PayTR 2026 Komisyon Oranları, eticaretradari.com, https://eticaretradari.com/odeme/paytr/, 2026.
26. Update to European Referral and FBA fees for 2026, About Amazon EU, https://www.aboutamazon.eu/news/empowering-small-business/update-to-european-referral-and-fulfilment-by-amazon-fees-for-2026, 2025-12.
27. Amazon to Lower Fees for European Sellers, EcommerceBytes, https://www.ecommercebytes.com/2025/12/02/amazon-to-lower-fees-for-european-sellers/, 2025-12-02.
28. Amazon Seller Fees Europe 2026, Acumen, https://acumenibc.com/amazon-seller-fees-europe-2026/, 2026.
29. Commissies Bol.com 2026, Boloo, https://www.boloo.co/blog/commissies-bol-com, 2026.
30. Bol.com Commissie Tarieven 2026, Winkelfactuur, https://winkelfactuur.nl/nl/blog/bol-com-commissie-tarieven-2026/, 2026.
31. 2026 Trendyol Komisyon Oranları, Paraşüt, https://www.parasut.com/blog/trendyol-magaza-komisyon-oranlari, 2026-01.
32. Trendyol Komisyon Oranları 2026, Sentos, https://www.sentos.com.tr/trendyol-komisyon-oranlari/, 2026.
33. Global Pricing Study 2025, Simon-Kucher, https://www.simon-kucher.com/en/insights/global-pricing-study-2025, 2025-06.
34. Choosing your route to growth, GPS 2025 brochure, Simon-Kucher, https://www.simon-kucher.com/sites/default/files/media-document/2025-06/COR_GPS_2025_Brochure_Digital_Final.pdf, 2025-06.
35. The Growth Blueprint Issue 1, Simon-Kucher, https://growthblueprint.simon-kucher.com/sites/default/files/2025-09/The_Growth_Blueprint_Issue_1_vF.pdf, 2025-09.
36. The AI advantage in B2B pricing, McKinsey, https://www.mckinsey.com/featured-insights/charts/the-ai-advantage-in-b2b-pricing, 2026-04.
37. Commercial Excellence Agenda 2025, Bain, https://www.bain.com/insights/expanding-profit-margin-through-intelligent-pricing-commercial-excellence-agenda-2025/, 2025.
38. More than a Penny's Worth: Left-Digit Bias and Firm Pricing, Review of Economic Studies, https://www.restud.com/more-than-a-pennys-worth-left-digit-bias-and-firm-pricing/, 2019 to 2023.
39. Retailers underestimate the power of penny pricing, Chicago Booth Review, https://www.chicagobooth.edu/review/retailers-underestimate-power-penny-pricing, 2020.
40. Thesis on 99 ending price rigidity, University of Chicago, https://knowledge.uchicago.edu/records/1xm6v-zwn75, 2024-06.
41. The supermarket surcharge you may not know you are paying, Victoria University of Wellington, https://www.wgtn.ac.nz/news/2026/09/the-supermarket-surcharge-you-may-not-know-youre-paying, 2026-09.
42. Quantity surcharge study (Binkley and Bejnarowicz), AgEcon Search, https://ageconsearch.umn.edu/record/20226/files/sp04ch03.pdf, older.
43. Shipping Fees and Product Assortment in Online Retail (Chen and Ngwe), Harvard Business School, https://www.hbs.edu/ris/Publication%20Files/19-034_b2382177-a462-447e-86f8-690d1ea7af18.pdf, 2019.
44. The 2026 State of B2B SaaS and AI Monetization, Growth Unhinged, https://www.growthunhinged.com/p/the-state-of-b2b-monetization-in-2026, 2026.
45. Pricing in 2026: what 230 companies say, OpenMeter, https://openmeter.io/blog/monetization-benchmarks-2026, 2026.
46. Food brand pricing strategy, eightx, https://eightx.co/blog/food-brand-pricing-strategy, 2025 to 2026.
47. Food snack brand scaling retail distribution, ATTN Agency, https://www.attnagency.com/blog/food-snack-brand-scaling-retail-distribution, 2025 to 2026.
48. Supermarket cut has doubled since the 90s, suppliers claim, Newshub, https://newshub.co.nz/home/new-zealand/2023/08/revealed-cut-supermarkets-make-on-products-has-more-than-doubled-since-90s-suppliers-claim.html, 2023-08.
49. Hof van Justitie schept duidelijkheid over verzendkosten en drempelbedragen, Thuiswinkel.org, https://www.thuiswinkel.org/nieuws/hof-van-justitie-schept-duidelijkheid-over-verzendkosten-en-drempelbedragen/, 2026-04-22.
50. Eindejaarspiek 2026, Emerce, https://www.emerce.nl/achtergrond/minder-omzet-per-pakket-borg-capaciteit-marge-eindejaarspiek, 2026.
51. Gratis verzending boven drempelbedrag en deelretour, WebwinkelKeur, https://www.webwinkelkeur.nl/gratis-verzending-boven-drempelbedrag-en-deelretour/, 2025.
52. DFA public consultation factual summary report, European Commission (Table.Media copy), https://table.media/assets/europe/public_consultation_on_the_digital_fairness_act_factual_summary_report.pdf, 2026.
53. Digital Fairness Act and Digital Omnibus 2026, Taylor Wessing, https://www.taylorwessing.com/en/interface/2025/predictions-2026/digital-fairness-act-and-digital-omnibus, 2025-12.
54. Digital Fairness Act Unpacked: Unfair Pricing Practices, Lexology, https://www.lexology.com/library/detail.aspx?g=fbcc8e4d-b37e-4419-99a7-4a522a89cf7d, 2026.
55. Austria: New Labeling Rules Require Disclosure of Shrinkflation, Library of Congress, https://www.loc.gov/item/global-legal-monitor/2026-05-14/austria-new-labeling-rules-require-disclosure-of-shrinkflation, 2026-05-14.
56. Spotlight on shrinkflation: Austria's Anti-Deceptive Packaging Law, Schoenherr, https://www.schoenherr.eu/content/spotlight-on-shrinkflation-austria-s-anti-deceptive-packaging-law-now-in-effect, 2026.
57. Mondelez court case: is shrinkflation illegal now?, FoodNavigator, https://www.foodnavigator.com/Article/2026/05/26/mondelez-court-case-is-shrinkflation-illegal-now/, 2026-05-26.
58. Shrinkflation regulations France, Hungary, Romania, Sagentia, https://sagentia.com/blog/france-hungary-romania-and-south-korea-tackle-shrinkflation/, 2025.
59. Rekabet Kurumu lastik sektörü cezası, Ekovitrin, https://www.ekovitrin.com/rekabet-kurumundan-lastik-sektorune-tarihi-ceza-36-milyar-tl/amp, 2026-06.
60. Seher Gıda RPM kararı, Sibel Öztürk Law, https://sibelozturk.av.tr/yazi/alicilarin-yeniden-satis-fiyatinin-belirlenmesiyle-ilgili-olarak-rekabet-kurulunun-icim-sut-markasiy, 2025.
61. e-ticarette 2026 cezalar, Bigpara, https://bigpara.hurriyet.com.tr/haberler/genel-haberler/e-ticarette-yeni-donem-2026da-cezalar-el-yakacak_ID1622508/, 2026.
62. Fahiş fiyat ve stokçuluğa 9 ayda 2,6 milyar lira ceza, Sanayi Gazetesi, https://sanayigazetesi.com.tr/fahis-fiyat-ve-stokculuga-9-ayda-26-milyar-lira-ceza/, 2026-10.
63. Ticaret Bakanlığı fahiş fiyat denetimi 389,4 milyon lira ceza, Ekotürk, https://www.ekoturk.com/haberler/ticaret-bakanligindan-fahis-fiyat-denetimi-3894-milyon-lira-ceza/, 2026-05.
64. Enflasyon rakamları Eylül 2026, Alomaliye, https://www.alomaliye.com/2026/10/05/enflasyon-rakamlari-tufe-eylul-2026/amp/, 2026-10-05.
65. TÜİK Eylül 2026 enflasyon verileri, Haber3, https://www.haber3.com/ekonomi/tuik-eylul-2026-enflasyon-verilerini-acikladi-tufe-2973-yi-ufe-2738-oldu-haberi-6266094, 2026-10.
66. Eylül ayı enflasyon rakamları açıklandı, Takvim, https://www.takvim.com.tr/ekonomi/2026/10/04/tuik-eylul-ayi-enflasyon-rakamlarini-acikladi, 2026-10.
67. Dolar bugün kaç TL, 6 Ekim 2026, hisse.net, https://www.hisse.net/haber/dolar-bugun-kac-tl-6-ekim-2026-dolar-ve-euro-serbest-piyasa-fiyat-listesi-100349, 2026-10-06.
68. Prisync API, Prisync, https://prisync.com/api, 2026.
69. Prisync AI dynamic pricing app, Shopify App Store, https://apps.shopify.com/prisync-ai-dynamic-pricing, 2026.
70. Price2Spy API reference guide, Price2Spy, https://price2spy.com/api/documentation/api-reference-guide.html, 2026.
71. Price2Spy API 2.1 released, Price2Spy, https://www.price2spy.com/blog/price2spy-api-2-1-released/, older.
72. Competera store level AI pricing assistant, Competera, https://competera.ai/resources/articles/retail%E2%80%99s-first-store-level-pricing-optimization-and-ai-powered-pricing-assistant-announced-by-competera, 2026-02-19.
73. Pricefx Accelerate 2026, Business Wire via Morningstar, https://www.morningstar.com/news/business-wire/20260922544186/pricefx-accelerate-2026-showcases-ai-powered-pricing-in-action, 2026-09-22.
74. Keepa MCP, GitHub cosjef, https://github.com/cosjef/Keepa_MCP, 2025 to 2026.
75. Keepa pricing in 2026, Trends MCP, https://www.trendsmcp.ai/blog/keepa-pricing, 2026.
76. Rounding prices, Shopify Help Center, https://help.shopify.com/en/manual/markets/pricing/rounding, 2026.
77. Catalogs, Shopify developer docs, https://shopify.dev/apps/internationalization/catalogs, 2026.
78. 12 Best Prisync Alternatives 2026, Yieldigo, https://www.yieldigo.com/blog/blog-prisync-competitors/, 2026.
79. Albert Heijn zet leveranciers onder druk, MKB Servicedesk, https://www.mkbservicedesk.nl/juridisch/geschillen-procederen/albert-heijn-zet-leveranciers-onder-druk, older.
80. Competitor price monitor MCP server, Apify, https://apify.com/gadolinium/competitor-pricing-monitor/api/mcp, 2026.

Prior knowledge (no URL captured): Marn and Rosiello (1992, HBR); Anderson and Simester (2003, QME); Bijmolt, van Heerde and Pieters (2005, JMR); Lewis, Singh and Fay (2006, Marketing Science); Huber, Payne and Puto (1982); Frederick, Lee and Baskin (2014); Yang and Lynn (2014); Scheibehenne et al. (2010); Chernev et al. (2015); Wadhwa and Zhang (2015, JCR); Directive 98/6/EC; Directive 2019/2161; Regulation 2022/720 (VBER).
