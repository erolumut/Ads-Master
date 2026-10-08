# Search, AI Max and Copilot Placements

> Scope: Search campaign build, keywords, ads and assets, AI Max for Search, Dynamic Search Ads status, Copilot ad formats and eligibility, and search partner controls.

## 1. Where Microsoft search ads serve

| Surface | How you reach it | Control |
|---------|------------------|---------|
| Bing (web, Edge, Windows search) | Search campaigns, Shopping, PMax | Owned and operated, always on in Search |
| Yahoo and AOL search | Part of Microsoft owned and operated plus partner inventory | Not separable as a single toggle; review in publisher report [Practitioner consensus] |
| DuckDuckGo, Ecosia and other syndicated search partners | Syndicated search partners | Ad distribution setting and website exclusions |
| Microsoft Copilot (copilot.microsoft.com, Copilot in Edge, Windows, Bing) | Placement fed by Search, Shopping, AI Max and PMax | No separate campaign type; eligibility by format [Unverified] for opt-out options |
| Microsoft Audience Network (MSN, Outlook, Edge new tab, partners) | Audience campaigns, PMax, and Search campaigns if not opted out | See [Audience network](audience-network-and-targeting.md) |

## 2. Search campaign structure

| Campaign | Purpose | Match types | Bidding default | Notes |
|----------|---------|-------------|-----------------|-------|
| Brand | Defend and capture brand demand cheaply | Exact and phrase | Target impression share (top of page) or Manual CPC | Separate budget; exclude brand from all other campaigns and PMax |
| Non-brand core | Highest intent category and product terms | Exact and phrase, broad only with conversion bidding | Maximize conversions or value with target after 30 conversions | Split by margin or service line, not by match type |
| Non-brand discovery | Find new queries | Broad or AI Max | Conversion bidding with a target | Run only when core is profitable |
| Competitor | Comparison demand | Exact and phrase | Manual or tCPA with lower target | Check trademark policy per market |
| Problem or category (B2B) | Earlier stage demand | Phrase and broad | tCPA on qualified lead goal | Layer LinkedIn profile Bid only |

Rules:
- Ad groups: tight themes, 5 to 20 keywords; one landing page theme per ad group.
- Keep brand and non-brand in separate campaigns so budgets and bid strategies do not blend.
- Negative keywords: Microsoft negatives are exact or phrase match; build shared lists for brand protection, irrelevant terms and job seekers [Practitioner consensus].

## 3. Ads and assets

### Responsive search ads
| Field | Limit | Practice |
|-------|-------|----------|
| Headlines | 3 to 15, 30 characters | Fill 15. At least 3 with keywords, 3 with benefits, 2 with proof, 2 with offer or CTA |
| Descriptions | 2 to 4, 90 characters | Fill 4. One proof, one offer, one objection handler |
| Paths | 2 x 15 characters | Category and intent words |
| Pinning | Optional | Pin only legal or brand lines; heavy pinning lowers combinations |

Write for the Microsoft audience: older, more desktop, more research oriented [Practitioner consensus]. Specifics and proof (years in business, certifications, warranty, price from) tend to outperform hype.

### Assets checklist (fill all that apply)
- [ ] Sitelinks (4 to 8, with descriptions)
- [ ] Callouts (6 or more)
- [ ] Structured snippets
- [ ] Call asset (verified number) and call reporting
- [ ] Location asset via Microsoft Places
- [ ] Image assets (multiple aspect ratios)
- [ ] Logo and business name (needed for logo display, and logo presence is cited as a Copilot eligibility factor) [Unverified]
- [ ] Price and promotion assets where relevant
- [ ] Filter link and action assets (Microsoft specific formats) [Practitioner consensus] for availability by market
- [ ] Video assets where available

### Multimedia ads
Image led search ads that can show on the right rail, in Copilot and on partner surfaces. Build at least one per core ad group with 3 or more images, headlines and descriptions. Eligibility for Copilot answers is reported for multimedia ads by third party guides [Unverified].

### Asset level editorial review
Since 2025-11 Microsoft reviews each headline, description and image independently; ads keep serving while enough assets remain approved, and disapproved assets can be appealed, edited or removed in the platform [Official, 2025-11]. A bulk edit tool for disapproved assets launched 2026-08 [Official, 2026-08]. Weekly: filter assets by status, fix or appeal.

## 4. AI Max for Search

Status: generally available since 2026-08 (main announcement 2026-08-27) after an open pilot from 2026-05 [Official, 2026-08].

| Component | What it does | Control |
|-----------|-------------|---------|
| Search term matching | Expands beyond keywords to relevant queries | Term exclusions, negative keywords, brand inclusions and exclusions |
| Text customization | Generates and personalizes ad text from your assets and landing pages | Review generated text in reporting; remove off-brand variants |
| Final URL expansion | Sends users to the most relevant page on your site | URL exclusions, URL rules; disable for single landing page funnels |

When to turn it on:
1. Core Search is profitable and has 30+ conversions in 30 days.
2. Conversion goals are trustworthy (qualified stages for lead gen).
3. The site has many relevant landing pages (ecommerce, marketplaces, multi service firms) for URL expansion, or you disable URL expansion.
4. You can review search terms weekly.

How to test: run AI Max as an Experiment (50/50 split) on the top 1 to 3 campaigns for 4 weeks or until each arm has 50 or more conversions. Primary metric: CPA or ROAS on backend data. Guardrail: brand query share and landing page mix. Log in EXPERIMENTS.md.

Google parity: Google Import carries AI Max settings; scheduled imports keep applying them to matched campaigns [Official, 2026-08]. If Microsoft performance differs, stop syncing and set AI Max per platform.

## 5. Dynamic Search Ads (status check required)

Dynamic Search Ads generate headlines from site content and target by page feeds, categories or URL rules. As of 2026-10 their long term status relative to AI Max final URL expansion is not confirmed [Unverified]. Google has been moving DSA functionality into AI Max [Practitioner consensus]. Procedure:
1. Check the help center and UI for DSA creation availability before proposing new DSA builds.
2. For existing DSA, compare against an AI Max experiment on the same domain section.
3. Keep page feeds and URL exclusions current either way; they map to AI Max URL controls.

## 6. Copilot ad formats and status

| Format or program | What it is | Status as known | Label |
|-------------------|-----------|-----------------|-------|
| Ads in Copilot answers | Search and product ads shown inside or next to Copilot responses | Live; served from eligible Search, Shopping, AI Max and PMax campaigns | [Official, 2025-03] [Practitioner consensus] |
| Showroom ads | Split screen immersive brand experience next to Copilot; offered when a user shows purchase intent | Pilot since 2025-04 with select US clients (Mercedes-Benz USA cited); access via account team | [Official, 2025-03] [Unverified] for 2026 status |
| Dynamic filters | Ads that let users narrow product choices in conversation | Pilot announced 2025-03 for English markets | [Official, 2025-03] [Unverified] for current status |
| Ad voice | Copilot explains why an ad is shown | Announced 2025-03 | [Official, 2025-03] |
| Brand agents | Brand trained agent inside Showroom ads or on brand sites | Announced for later rollout; reported pilots | [Contested] Adweek called them unveiled, Microsoft called them planned |
| Copilot Checkout and Universal Commerce Protocol | Purchase inside Copilot using merchant product data | Announced at Activate 2026 (2026-05-19); readiness depends on feed and protocol support | [Official, 2026-06] |

Performance claims from Microsoft: ad relevance in Copilot about 25% better than traditional search and CTR roughly doubling (reported 2025-03, company sourced, not independently audited) [Official, 2025-03] [Unverified] for any specific account.

### Copilot eligibility (what to build)
Third party guides list these as eligible for Copilot placement: multimedia ads, product ads (Shopping and PMax), search ads with a logo asset or business logo, property promotion ads and tours and activities ads [Unverified]. The same guides state eligible campaigns are opted in automatically and cannot opt out [Unverified].

Copilot readiness checklist:
- [ ] RSAs with 15 headlines and 4 descriptions, ad strength good or better
- [ ] Logo and business name assets approved
- [ ] Multimedia ads in core ad groups
- [ ] Image assets approved
- [ ] Shopping or PMax with a healthy Microsoft Merchant Center feed (ecommerce)
- [ ] Landing pages that answer comparison and detail questions (Copilot users ask longer, conversational queries)
- [ ] Broad match or AI Max on profitable campaigns to match longer queries
- [ ] Vertical feeds (hotel, property, tours) where the business fits

### Copilot reporting
Sources conflict: some guides describe a Copilot segment in network or ad distribution reports, others say Copilot data sits with Microsoft sites or audience placements, others say no Copilot specific metrics exist [Contested]. Procedure:
1. In Reports, add the "Ad distribution" or network segment and look for a Copilot label.
2. Check the PMax search insights and landing page reports for conversational query patterns.
3. If no Copilot breakdown exists in the account, report Copilot as "not separable" and do not estimate it.
4. Log what you found in the journal; it informs every other project.

Stakeholder message template:
> Copilot ads are a placement inside our existing Search, Shopping and PMax campaigns, not a separate buy. We improve eligibility with complete assets, images, logos and feeds. As of <date>, the account <does / does not> report Copilot separately, so we measure the total campaign result.

## 7. Search partner controls

| Control | Where | Use |
|---------|-------|-----|
| Ad distribution | Campaign or ad group settings | Choose owned and operated only, partners only, or both. Start with both on non-brand if budget allows learning; brand on owned and operated plus partners usually fine |
| Website exclusions | Campaign, ad group, or account level lists | Block publishers that fail the CPA bar |
| Website URL (publisher) report | Reports | Spend, clicks, conversions by publisher domain |
| Bid adjustment by network | Not available as a direct partner bid adjustment in all cases [Unverified] | If unavailable, split partners into a separate campaign with partners only distribution |

Partner hygiene procedure (every 2 weeks):
1. Export the publisher report for the last 30 days, all Search campaigns.
2. Flag publishers with spend over 2x target CPA and zero conversions, or CPA over 2x target with 3+ conversions.
3. Flag publishers with CTR above 10x the campaign average (possible invalid traffic).
4. Exclude flagged domains via a shared website exclusion list; record in the journal.
5. If partners overall run above 1.5x the owned and operated CPA for 60 days, test partners off as an Experiment.

## 8. Quality score and ad rank levers
- Quality score is 1 to 10 at keyword level; components: expected CTR, ad relevance, landing page experience.
- Fix ad relevance first (keyword in headlines), then landing page (speed, match), then expected CTR (offers, assets).
- Ad Rank uses bid, quality and asset impact; assets raise CTR and rank, so assets are a cost lever.

## 9. Editorial and policy notes for Search
- Trademarks: Microsoft enforces trademark complaints in ad text per market; check before using competitor names in text.
- Superlatives and unverified claims trigger disapprovals; keep proof on the landing page.
- Regulated categories (healthcare, pharmacy, financial services, gambling, alcohol, political) need certifications or are restricted by market. Political ads are not allowed [Practitioner consensus].
- Sensitive industries: autogenerated assets handling was updated in 2026-01 and 2026-04 roundups [Official, 2026-04]; review generated assets manually in regulated verticals.
