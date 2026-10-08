# Account Structure and Campaign Types

> Knowledge as of 2026-10. TikTok renames objectives, toggles and campaign flows several times a year and rolls features out by account, market and objective. Confirm every menu name in the live Ads Manager before writing a launch plan. Evidence labels follow the Ads Master spec.

## 1. The hierarchy and where each setting lives

```
Business Center (BC)
  -> Ad account (currency + time zone fixed at creation)
       -> Campaign (objective, campaign budget / CBO, Smart+ or manual, special flags)
            -> Ad group (placement, targeting, ad group budget, schedule + dayparting,
                         optimization goal, bid strategy, attribution settings, pixel/event)
                 -> Ad (identity, video/image, ad text, CTA, destination URL or Shop/LIVE,
                        tracking URL parameters, interactive add-ons)
  -> Shared assets: Pixels and Events API datasets (Events Manager), catalogs, audiences,
     TikTok accounts (identities), TikTok Shop, payment methods, members and roles
```

| Level | Settings that live here | Common mistake |
|-------|------------------------|----------------|
| Business Center | Ownership of ad accounts, pixels, catalogs, TikTok accounts, Shop link, payment, member roles, 2-step verification | Agency owns the BC; brand loses pixel history and Spark identities when the agency leaves |
| Ad account | Currency, time zone, billing, account-level spending limit | Time zone mismatched with backend reporting day; currency cannot be changed later [Practitioner consensus] |
| Campaign | Objective, Smart+ vs manual flow, Campaign Budget Optimization, campaign spending limit, split test flag | Too many campaigns at Starter and Growth tier fragment signal |
| Ad group | Placements, audience, budget (ABO), schedule, dayparting, optimization event, bid strategy, attribution windows | Optimizing to a shallow event (Add to cart) to exit learning, then never moving to Purchase |
| Ad | Identity (TikTok account for Spark Ads or custom identity), creative, text, CTA, URL, UTMs | No UTMs, so GA4 cannot triangulate TikTok traffic |

## 2. Objective menu (verify names in your account)

| Objective (UI label) | Funnel | Use when | Typical optimization goals | Notes |
|----------------------|--------|----------|---------------------------|-------|
| Reach | Awareness | Brand reach at lowest cost per reach, launches, tentpoles | Reach, frequency caps | Also bought as Reach and Frequency (fixed price, guaranteed) |
| Traffic | Consideration | Content sites, cheap landing page traffic, building retargeting pools | Click, Landing page view | Smart+ Traffic has a separate documented flow [Official, 2026-07] |
| Video views | Consideration | Cheap 2s or 6s views, creative pre-testing, engagement pools | 2-second view, 6-second focused view | Good for building engager audiences, poor proxy for sales |
| Community interaction | Consideration | Follower growth, profile visits, LIVE viewers | Follows, profile visits, LIVE | Use for creator-led brands and LIVE sellers |
| App promotion | Conversion | App installs, in-app events, app retargeting | Install, in-app event (AEO), value (VBO) | Smart+ App supported in the upgraded flow [Official, 2025-10] |
| Lead generation | Conversion | Instant forms, website forms, DMs, messaging apps | Leads, form submit, qualified CRM events | Smart+ Lead Generation exists [Official] |
| Sales | Conversion | Website purchases, catalog sales, app purchases, TikTok Shop | Purchase / Complete Payment, value | TikTok Shop destination routes to GMV Max only [Official, 2025-07] |

Search Ads Campaigns are created from the Traffic or Web Conversion (Sales) objective and then a search option opens a dedicated flow [Official, 2026-08].

## 3. Buying types

| Buying type | What it is | Use when |
|-------------|-----------|----------|
| Auction | Self-serve bidding in Ads Manager | Default for every performance use case |
| Reach and Frequency (R&F) | Fixed CPM, predictable reach, frequency control, booked in advance | Brand campaigns that need guaranteed reach and frequency caps |
| Reservation (TopView, TopReach, Prime Time, Logo Takeover) | Premium first-impression or sequential placements, usually via a TikTok rep | Launches, tentpoles. TopView became bookable in Ads Manager per the Q3 2026 product preview [Official, 2026-07] |

## 4. Smart+ versus manual campaigns

### 4.1 What Smart+ is in 2026
- Smart+ is TikTok's AI-driven campaign type (the successor to Smart Performance Campaign). In the upgraded experience announced on 2025-10-07, one buying flow lets advertisers choose full automation, partial automation or fully manual control, module by module (targeting, budget, placement, creative, catalog) [Official, 2025-10].
- The upgraded flow supports Sales, Lead Generation and App Promotion for eligible advertisers; Traffic has a separate Smart+ flow [Official, 2026-07]. Availability depends on objective, account and market, and some features need a TikTok rep to enable [Official, 2026].
- Search Ads Campaign is "powered by Smart+": Smart+ can expand keywords and choose creatives [Official, 2026-08].
- Rollout: the upgraded flow was announced 2025-10-07 and has rolled out in stages; the "Smart+ Upgraded Experience" help article was last updated 2026-09 [Official, 2026-09]. Trade posts cite 2026-01-21 (Auto-select, previews), May 2026 (tiered SMB controls) and 2026-09-07 or 2026-09-30 for a further upgrade (creative material ID reporting, paid plus organic signal integration) [Contested dates]. No source confirms rollout to every advertiser; treat the account UI as the truth.
- Q3 2026 preview: Smart+ capabilities extend to Search Ads; Creator+ was rebuilt as Creative Upgrades for Smart+ Catalog Ads (review assets ranked by predicted performance and exclude any before launch); Symphony generation is being built into the Smart+ workflow [Official, 2026-07].

### 4.2 Module controls (upgraded flow)

| Module | Automated default | Manual or partial option | Override when |
|--------|------------------|--------------------------|---------------|
| Targeting | Automatic targeting finds the audience with minimal input | Audience controls set baseline limits (age, location, language); "Switch to custom targeting" for manual; some settings can be enforced [Official, 2026] | Legal limits (age 18+, 21+ for alcohol), geo restrictions, regulated categories, exclusion of existing customers |
| Placement | Automatic placement is the default for Sales, Lead Generation and App Promotion and may include non-TikTok partner surfaces through TikTok Ad Network (Pangle) depending on region; Smart+ Web lists TikTok, Pangle (where available), Search and Lemon8; Smart+ App on iOS is TikTok and Lemon8 only, on Android includes TikTok Ad Network [Official, Help Center] | The upgraded flow allows choosing specific placements in manual mode; older Smart+ Web help says manual placement is not supported and you must build a non-Smart+ campaign to exclude TikTok Ad Network [Official, pages conflict] | Brand safety, off-platform inventory converting poorly, US campaigns now that TikTok Ad Network is generally available in the US (2026-10-05). If the account has no placement module, use a manual campaign or ask the rep; one blog says opt-out goes through support [Unverified] |
| Budget | Automatic campaign budget | Custom ad group budgets | You must guarantee spend on a market, product line or test cell |
| Creative | Recommended Creatives, Auto-add (adds fresh creative while live), generation from a product URL | Choose assets, exclude recommended or generated assets, creative combination control | Brand compliance, claims review, regulated categories, likeness rights |
| Catalog | Catalog products and Catalog Image and Video Auto-Crawl from public landing pages [Official, 2026-07] | Product sets, manual creative | Pricing or claims on crawled pages are not ad-approved |

### 4.3 Smart+ capacity and creative features (verify per account)
- Structure limits: TikTok's Smart+ business blog gives up to 30 ad groups per campaign, 30 asset groups per ad group and 50 creatives per asset group, with text-to-creative pairing and multiple URLs [Official, TikTok business blog]; the help article on Smart+ ads says up to 30 unique ads (asset groups) per ad group, while the upgraded-flow notes say "up to 50 asset groups" [Official pages conflict, Contested]. Plan on 30 per ad group. Account limits outside Smart+: 5,000 campaigns per ad account, 999 ad groups per campaign, 50 ads per ad group [Official, Help Center "About ad account limits"].
- Creative minimums: TikTok best practice asks for at least 6 creatives at Smart+ Web creation; practitioners use 4 to 6 for Smart+ App and 3 to 4 per ad group at small budgets so each creative gets spend [Official for Web; Practitioner consensus otherwise].
- Auto-select creative: scans existing ads and eligible TikTok One creator content and recommends the strongest; first for Smart+ App (2026-01), extended to Lead Generation (Q3 2026 preview) [Official, 2026-07].
- Creative Upgrades (Smart+ Catalog Ads), Asset Manager, AI-generated campaign summaries, Music Autofix (detects music that cannot be used) were announced at TikTok World on 2026-05-13 and in the Q3 2026 preview [Official, 2026-05].
- Creative-level reporting by individual creative material ID across video, image, catalog and text assets, reported with the 2026-09 upgrade [Unverified, single third-party source].

### 4.4 Decision tree: Smart+ or manual

```
Is the destination TikTok Shop with a Sales objective?
  yes -> GMV Max (only option since July 2025). See tiktok-shop-and-gmv-max.md
  no  -> continue
Does the pixel/Events API record >= 50 primary conversions per week account-wide,
and can you supply >= 6 creatives at launch (TikTok's Smart+ Web guidance)?
  no  -> Manual campaign, 1 ad group, broad targeting, optimize to the deepest event that
         reaches ~25 to 50 per week; plan to graduate to Smart+ when signal allows
  yes -> continue
Do legal, brand safety or claims rules require locking targeting, placements or creative?
  yes -> Smart+ with those modules set to manual (partial automation)
  no  -> Smart+ with full automation for scaling; keep one manual testing campaign
         for controlled creative and audience tests
```

Validate with a split test before moving most of the budget: TikTok's own Smart+ Web guidance says to use split testing to validate the lift [Official, Smart+ Web best practices].

## 5. Reference architectures by business model and tier

Use the smallest structure that gives each ad group enough conversions. Rule of thumb: every conversion-optimized ad group needs a daily budget of at least 10x target CPA (TikTok VBO and Cost Cap guidance) and should be able to reach about 50 conversions in 7 days [Practitioner consensus, see bidding-and-budgets.md].

### 5.1 Ecommerce (own website)

| Tier | Structure |
|------|-----------|
| Starter (under $3k per month) | 1 manual Sales campaign, 1 ad group, broad targeting, Maximum Delivery, optimize to Purchase if 25+ per week possible, else Initiate Checkout for 2 to 4 weeks. 3 to 5 creatives. No Pangle / TikTok Ad Network. |
| Growth ($3k to $30k) | 1 Smart+ Sales (Web or Catalog) scaling campaign + 1 manual testing campaign (ABO, 1 ad group per concept batch). Optional retargeting only if audiences exceed size limits. |
| Scale ($30k to $300k) | Smart+ Sales by product line or margin band, Smart+ Catalog Ads, manual creative testing, Search Ads Campaign for brand and category terms, Spark Ads program with creators, Cost Cap or Minimum ROAS guardrails. |
| Enterprise (over $300k) | Per market Smart+ campaigns, brand layer (TopView / TopReach, R&F), Search Hubs, lift-test calendar, separate accounts per market or brand, API or MCP reporting. |

### 5.2 TikTok Shop sellers
- Product GMV Max for the catalog (all products or curated product groups), LIVE GMV Max for live sessions, affiliates feeding content, Smart+ Web or manual campaigns only for the off-Shop website. Details in tiktok-shop-and-gmv-max.md.

### 5.3 App
| Tier | Structure |
|------|-----------|
| Starter / Growth | 1 Smart+ App (or manual App promotion) per OS, optimize to install until 50+ in-app events per week, then to the in-app event (AEO) |
| Scale / Enterprise | Separate Android and iOS campaigns, AEO and VBO (Day 0 or Day 7 ROAS where offered), app retargeting with deep links, TikTok Ad Network as a tested placement, MMP cohort reporting |

### 5.4 Lead generation, B2B SaaS, local services
- 1 Lead Generation campaign (Instant Form or website form), Smart+ Lead Generation once lead volume is stable, CRM stage feedback through Events API. See lead-gen.md.
- Local services: radius or city targeting, dayparting aligned with call center hours, Instant Form with qualifying questions.

### 5.5 Marketplace or publisher
- Traffic or Sales with value-based optimization when GMV or revenue per session is passed back; two-sided marketplaces run supply and demand in separate campaigns with separate events.

### 5.6 Brand
- Reach or R&F, TopReach (TopView + TopFeed; TikTok cites 59% incremental reach at 3x lower cost per reach than TopView alone [Official, 2026-03]), Pulse for contextual adjacency, Brand Lift Study, Search Hubs and Branded Buzz (Brand Discovery Bundle, 2026-05-13 [Official, 2026-05]).

## 6. Search on TikTok

| Option | Control | When |
|--------|---------|------|
| Search Ads Campaign | Keywords per ad group, keyword suggestion tool, negative keywords; Smart+ keyword expansion; one campaign can hold multiple ad groups and ads in the upgraded workflow; budget 20x the bid recommended [Official, 2026-08] | Brand defense, category terms with commercial intent, product names, competitor research terms where allowed |
| Automatic Search Placement (formerly "Search Ads Toggle") | No keyword control; system generates and matches keywords [Official, 2026-06] | Default on for most conversion campaigns; check search placement performance in breakdowns |
| Precedence | If a query matches a keyword in your Search Ads Campaign, that campaign takes priority over Automatic Search Placement [Official, 2026-06] | Run both; isolate brand terms in the dedicated campaign |
| Search Hubs | Brand-owned destination at the top of TikTok Search results [Official, 2026-05] | Brands with search volume on TikTok; reservation or rep-led |
| Keyword Amplifier | Connects Search Ads with creator content via clickable comments and search recommendations that lead to the Search Hub [Official, 2026-05] | Branded Buzz and creator programs |

Use Creative Center Keyword Insights to find terms and phrasing that appear in high-performing TikTok ads before building keyword lists.

## 7. Brand and premium formats (2026 menu)

| Format | What it does | Buy | Source |
|--------|-------------|-----|--------|
| TopView | First full-screen ad on app open | Reservation; bookable in Ads Manager per Q3 2026 preview; region exclusion up to 40% reported | [Official, 2026-07], [Unverified] for the 40% figure |
| TopFeed | Premium first in-feed position | Reservation | [Official] |
| TopReach | TopView + TopFeed in one buy; Creative Sequencing (2026-05); Max Reach variant (Q3 2026) | Reservation | [Official, 2026-03 to 2026-07] |
| Pulse / Pulse Premiere | Contextual placement next to top creator or publisher content | Rep-led | [Official] |
| Prime Time | Sequential series of ads around tentpoles or live events | Rep-led, announced NewFronts 2026-03 | [Official, 2026-03] |
| Logo Takeover | Co-branded placement with the TikTok logo at app open | Rep-led, announced 2026-03 | [Official, 2026-03] |
| Branded Buzz | Creator submission program feeding brand content, paired with Search Hubs | Rep-led, 2026-05 | [Official, 2026-05] |
| Branded Mission | Crowdsourced creator content for a brand brief | Rep-led | [Official] |
| Streaming Ads | Smart+ optimization with title-focused interactive formats for streaming brands | Q3 2026 preview | [Official, 2026-07] |

## 8. App promotion specifics

| Topic | Guidance |
|-------|----------|
| Attribution | TikTok moved app measurement to a Self-Attributing Network (SAN) model; CTA, EVTA and VTA windows are set per ad group [Official, 2025-02]. iOS uses SKAdNetwork through the MMP. |
| MMP | Use the MMP (AppsFlyer, Adjust, Singular, Branch, Kochava) for cohort ROAS and fraud; reconcile MMP vs TikTok SAN numbers weekly |
| Optimization path | Install -> in-app event (AEO) -> value (VBO). Move one step deeper when the deeper event reaches ~50 per week per ad group |
| Creative | App store screenshots perform poorly. Use gameplay or real-use screen recordings with a creator voiceover; Symphony Product Avatars can hold an app screen image [Official, 2026-05] |
| Auto-select | Smart+ App was the first campaign type with Auto-select creative (2026-01), extended to Lead Generation in the Q3 2026 preview [Official, 2026-07; January date via trade press] |
| Off-platform | TikTok Ad Network (formerly Pangle) has playable and rewarded inventory; strong for gaming installs, weaker for subscription quality. Judge on Day 7 retention and ROAS, not CPI |

## 9. Placements

| Placement | Notes | Default stance |
|-----------|-------|----------------|
| TikTok (feed, search, LIVE, Shop surfaces) | Core inventory | Always on |
| Automatic Search Placement | On by default in most conversion flows | On; review breakdown |
| Global App Bundle (ByteDance apps such as CapCut) | Availability varies by market [Unverified] | Test, do not assume |
| Lemon8 | Included by automatic placement where available [Official, 2026] | Test where available |
| TikTok Ad Network (formerly Pangle) | Nearly 400,000 apps (TikTok said "more than" 400,000 in August); generally available for US campaigns from 2026-10-05 as the 48th market after limited US tests; advertisers see the new name, publishers still see Pangle; DoubleVerify and IAS post-bid brand safety measurement [Official, 2026-10, via Adweek, Marketing Dive, PPC Land] | Off for web sales and lead gen until a split test proves it; on for gaming and app installs as a tested cell |

## 10. Naming convention (copy and adapt)

```
Campaign:  {Market}_{Objective}_{Type}_{Product/Line}_{Goal}_{YYMM}
           US_SALES_SMARTPLUS_CORE_PURCH_2610
           US_SALES_MANUAL_TEST_CREATIVE_2610
           US_SHOP_GMVMAX_PRODUCT_ALL_2610
Ad group:  {Audience}_{Placement}_{OptEvent}_{Bid}_{Attribution}
           BROAD_TTONLY_PURCH_MAXDEL_7C1V
Ad:        {ConceptID}_{Hook}_{Format}_{Creator}_{Length}_{Version}
           C014_PAINQ_UGC_jdoe_22s_v3
```

Keep a creative register (concept ID, hook, angle, creator, date launched, status) in the project outputs so every report can join performance to concept, not to file names.

## 11. Account hygiene checklist
1. Brand owns the Business Center; agencies get partner access, never ownership.
2. Two or more admins with 2-step verification; remove departed users monthly.
3. Ad account time zone matches the backend reporting day; currency matches billing.
4. Pixel and Events API dataset owned by the brand BC and shared to each ad account that needs it.
5. TikTok Shop, catalog and TikTok accounts (identities) linked in the BC with documented owners.
6. Payment method backed up (second card or invoicing) to avoid delivery stops; never reuse a payment method or BC tied to a suspended account (see policy-and-account-health.md).
7. One owner of record for the TikTok rep relationship; log every rep-enabled feature (allowlists, betas) in `ads-master/memory/tiktok-ads.md`.
