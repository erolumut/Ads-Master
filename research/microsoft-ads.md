# Research Dossier: Microsoft Advertising

> Compiled 2026-10-08 for the `microsoft-ads` agent. Covers January 2025 to October 2026.
>
> Method and limits: 17 web searches (extended mode for 2025 to 2026 items) returned extracts of Microsoft Advertising blog roundups, Microsoft Learn documentation and trade press. Direct page fetching was blocked by the research environment's egress policy and the shared web search budget ran out before the target of 35 searches, so several items rely on search extracts and are labeled accordingly. GitHub repository search (2026-10-08) was used for tools and MCP servers. Items that need live verification are in the watch list.

## 1. Executive summary

1. Copilot is a placement, not a campaign type. Ads reach Copilot through Search, Shopping, AI Max and PMax campaigns; eligibility depends on formats (logo, images, multimedia, feeds), market and rollout. Copilot specific reporting is inconsistent across sources [Contested].
2. AI Max for Search became generally available in August 2026 (announcement 2026-08-27) after an open pilot from May. It bundles search term matching, text customization and final URL expansion, with brand controls and term exclusions, and imports from Google Ads [Official, 2026-08].
3. Performance Max matured fast: NCA goal GA (2026-02), self-serve negative keywords up to 5,000 per list (2026-03), share of voice (2026-01), landing page report (2026-04), Ad Preview Hub (2026-07), uplift experiments GA (2026-09) [Official].
4. Experiments became generally available for Search, Shopping, Audience and PMax in September 2026, with side by side results and one click apply [Official, 2026-09].
5. Measurement shifted: UET consent mode mandatory for EEA, UK and Swiss users since 2025-05-05; modeled conversions since 2025-08; Advanced Consent Mode guidance 2026-02-19; Conversions API documented 2026-08 but beta and enrolled per account [Official].
6. LinkedIn profile targeting remains Microsoft's unique B2B lever. Company lists grew from 1,000 to 10,000 names (2026-09). LinkedIn profile data excludes EEA, UK and Swiss users [Official, 2026-09].
7. Bidding gained portfolio depth: cross-account portfolios (2026-05), seasonality adjustments for portfolios and shared budgets (2026-05), data-driven attribution for all advertisers (by end of 2026-05) [Official, 2026-05].
8. Migration is easier and riskier: Import Center for Google, Meta and Pinterest (2026-05); PMax with NCA and AI Max settings import from Google. Scheduled imports can overwrite Microsoft specific divergence if not scoped [Official, 2026-04 to 2026-08].
9. Programmatic retreat: Microsoft Invest (Xandr DSP) wound down by early 2026 with Amazon DSP named preferred partner; sell side Monetize and Curate continue with Copilot features [Practitioner consensus, trade press 2025-05 to 2026-01].
10. API: SOAP retires 2027-01-31; the earlier plan for REST only features from 2026-10-01 was relaxed. Any SOAP integration needs a migration plan now [Official, 2026-09].

## 2. State of the channel in 2026

| Dimension | State (October 2026) | Evidence |
|-----------|---------------------|----------|
| Networks | Microsoft Search Network (Bing, Yahoo, AOL, DuckDuckGo and syndicated partners, Edge, Copilot) and Microsoft Advertising Network (MSN, Outlook, Edge, partners) | Platform structure [Practitioner consensus] |
| Campaign types | Search (with AI Max), Shopping, Performance Max, Audience, vertical (hotel, property promotion, tours and activities and others) | [Official, 2026] |
| AI layer | AI Max GA; Copilot in the Microsoft Advertising Platform (GA since 2024-05); Ads Studio with brand kits; Copilot powered image animation (2025-11) | [Official] |
| Commerce | Microsoft Merchant Center with Test feed, supplemental feeds, Product explorer; Universal Commerce Protocol and Copilot Checkout announced 2026-05 | [Official, 2025-04 to 2026-06] |
| Measurement | UET, consent mode, ACM, modeled conversions, enhanced conversions, offline import, CAPI beta, DDA | [Official] |
| Market share | Bing global share in low single digits, higher on US desktop [Unverified]; Copilot and partners extend reach | Check StatCounter |
| Platform claims | Copilot ad relevance about 25% better, CTR roughly 2x (2025-03); PMax about 8% more incremental conversions (2026-05) | Company sourced [Official] [Unverified] for any account |
| Policy and governance | Asset level editorial review (2025-11), bulk edit for disapproved assets (2026-08), Optimization score retired (2025-04), Ads for Social Impact grants ended (2025-12) | [Official] and trade press |

### 2.1 Differences vs Google that matter

| Difference | Microsoft | Google | Implication |
|------------|-----------|--------|-------------|
| Professional targeting | LinkedIn company, industry, job function on Search, Shopping, Audience; PMax signal; company lists up to 10,000 | No LinkedIn data | Microsoft is the only search platform with native B2B firmographic layers (not for EEA, UK, Swiss users) |
| Demographic bid adjustments on Search | Age and gender adjustments available | Demographic controls on Search are limited | More manual control for older or gender skewed audiences |
| Search partner control | Ad distribution choices, publisher level report, website exclusions | Search partners toggle only, limited domain visibility | Domain level partner pruning is possible on Microsoft |
| Audience Network exposure from Search | Possible depending on settings | Display expansion is separate | Check and decide per campaign |
| Device mix | Higher desktop share [Practitioner consensus] | Mobile majority | Device adjustments and landing pages must reflect desktop users |
| Audience profile | Older, higher income on average [Practitioner consensus, Microsoft marketing claims] | Broad | Test premium offers and detail rich copy |
| CPC level | Often lower [Contested] | Higher competition | Measure with parity report |
| ValueTrack | {msclkid}, {QueryString} available | {gclid}; no raw query parameter | Offline import and landing page personalization differ |
| Copilot | Ads in Copilot answers from existing campaigns | Ads in AI Overviews and AI Mode from Google campaigns | Both are placements; neither is a separate buy for most advertisers |
| Experiments | GA across Search, Shopping, Audience, PMax (2026-09) | Mature experiments | Parity reached in 2026 |

### 2.2 Google import: what transfers and what breaks (summary)
- Transfers: Search structure, keywords, negatives, RSAs, most assets, budgets, bid strategies (mapped), locations, schedules, device adjustments, Shopping (with a matching Merchant Center store), PMax (including NCA goals from 2026-04), PMax negatives (2026-03), brand lists (2025-05), AI Max settings (2026-08) [Official].
- Does not transfer: audience lists, customer match data, Google conversion actions (UET goals must be created), Display, Video, Demand Gen, App, Smart and Local Services campaigns, experiments [Practitioner consensus].
- Breaks or drifts: location intent defaults, Audience Network exposure, tracking templates with Google only parameters, bid targets set for a different auction, scheduled imports overwriting Microsoft changes [Practitioner consensus].
- Fix list and scheduling strategy: see `skills/microsoft-ads/references/account-setup-and-google-import.md`.

### 2.3 Copilot ads deep dive
- Model: Copilot is a placement fed by Search, Shopping, AI Max and PMax campaigns [Practitioner consensus, multiple 2026 guides].
- Formats announced 2025-03: Showroom ads (pilot from 2025-04, account team access), dynamic filters (pilot), ad voice, brand agents (planned or pilot) [Official, 2025-03].
- Commerce: Universal Commerce Protocol and Copilot Checkout announced at Activate 2026 to power purchase flows with fresh product data [Official, 2026-06].
- Eligibility signals cited by guides: multimedia ads, product ads, search ads with logo assets, property promotion and tours and activities ads; market and rollout state matter [Unverified].
- Measurement: unresolved; treat Copilot as not separable unless the account shows a segment [Contested].
- Skeptic view: PCWorld (2025-03) argued large conversational ad units could be intrusive; expect user experience changes and format iteration.

### 2.4 Measurement stack in 2026 (summary)
| Layer | Status | Notes |
|-------|--------|-------|
| UET | Core | One tag per site, custom events for conversions |
| Consent mode | Mandatory for EEA, UK, Swiss users since 2025-05-05 | ad_storage granted or denied; default denied before CMP |
| Advanced Consent Mode | Guidance 2026-02-19 | Cookieless pings when denied; modeling [Contested] |
| Modeled conversions | Since 2025-08 for eligible EEA, CH, GB advertisers | Estimates, not observations |
| Enhanced conversions | Opt-in per goal since 2024-02 | Hashed email and phone |
| Offline import | MSCLKID, 90 day click window | CRM stage values for lead gen |
| Conversions API | Beta, per account since 2026-08 | eventId dedupe with UET |
| Data-driven attribution | All advertisers by end of 2026-05 | Coordinate changes with bidding |
| CRM integration | HubSpot integration announced 2026-09 [Contested] on availability | Lifecycle events to bidding |
| Clarity | Session insight; AI Visibility reporting 2026-08 | Official Clarity MCP server |

### 2.5 Why B2B advertisers should care
- LinkedIn profile targeting and company lists make Microsoft the only search platform where firmographics and job functions can steer search bids [Official, 2026-09].
- The desktop and workday skew means B2B buyers researching at work are well represented [Practitioner consensus].
- HubSpot integration and offline imports let bidding learn from pipeline stages [Official, 2026-09] [Contested] on availability.
- Limits: LinkedIn data excludes EEA, UK and Swiss users; volumes are small, so pooling (portfolios) and Bid only layers beat narrow targeting.

## 3. Timeline of changes (January 2025 to October 2026)

| Date | Change | Area | Label |
|------|--------|------|-------|
| 2025-02 | LinkedIn profile targeting as PMax audience signal, pilot in 6 markets | PMax, B2B | [Official, 2025-02] |
| 2025-03 | Showroom ads, dynamic filters, ad voice announced for Copilot; brand agents planned; Showroom pilot from 2025-04 | Copilot | [Official, 2025-03] |
| 2025-03-17 | Notice: UET consent mode required for EEA, UK, Swiss users by 2025-05-05 | Measurement | [Official, 2025-03] |
| 2025-04 | Test feed in Merchant Center; primary feed for local inventory ads | Commerce | [Official, 2025-04] |
| 2025-04-08 | Optimization score retirement begins | Platform | [Official, 2025-04] |
| 2025-05-05 | Consent mode deadline | Measurement | [Official, 2025-03] |
| 2025-05 | Ads Studio GA in Editor; PMax scripts and automated rules; asset and audience reporting; LinkedIn audience signal; brand list import and NCA goal announced as coming | Tools, PMax | [Official, 2025-05] |
| 2025-05 | Auction change: PMax and Standard Shopping on the same products compete | Shopping | [Official, 2025-06] |
| 2025-05 | Trade press: Microsoft Invest DSP to wind down by early 2026 | Programmatic | [Practitioner consensus] |
| 2025-06 | Custom report builder | Reporting | [Official, 2025-06] |
| 2025-07 | API: annotation opt-out operations, new reports | API | [Official, 2025-07] |
| 2025-08 | Modeled conversions for UET consent mode (EEA, CH, GB); impression based remarketing from up to 20 campaigns or ad groups | Measurement, audiences | [Official, 2025-08] |
| 2025-09 | Supplemental feeds GA; PMax budget suggestions and estimates for non-feed; asset group reporting; share of voice | Commerce, PMax | [Official, 2025-09] |
| 2025-10-07 | Amazon DSP named preferred partner as Microsoft exits DSP | Programmatic | [Practitioner consensus] |
| 2025-11-18 | Asset level editorial review with per asset appeals; Copilot image animation | Policy, creative | [Official, 2025-11] |
| 2025-11 | Publisher: new Microsoft Prebid adapter replaces AppNexus adapter | Sell side | [Official, 2025-11] |
| 2025-12 | Ads for Social Impact grant program ends | Nonprofits | Trade press [Unverified] |
| 2025-12 | API: GetAudienceBreakdown, TopicCriterion, multi entity impression based remarketing | API | [Official, 2025-12] |
| 2026-01 | PMax NCA open beta; PMax share of voice (search and shopping, data from 2025-11-10); asset group tracking template and custom parameters | PMax | [Official, 2026-01] |
| 2026-01 | Trade press: Xandr DSP shut down; Prebid video caching to stop around 2026-04-30 | Programmatic | [Practitioner consensus] |
| 2026-02 | Ad Preview Hub for Audience ads (MSN, Outlook); NCA GA; PMax negative keywords open beta | Audience, PMax | [Official, 2026-02] |
| 2026-02-19 | Advanced Consent Mode guidance | Measurement | [Official, 2026-02] |
| 2026-03 | Self-serve PMax negative keywords (lists, account level, 5,000 per list, API, Editor, Google import) | PMax | [Official, 2026-03] |
| 2026-04 | Import PMax with NCA goals from Google; PMax landing page report; seasonality for portfolios; 400 character campaign names | PMax, bidding | [Official, 2026-04] |
| 2026-04 | API platform evolution post (REST direction); AI Max open pilot announced for May | API, Search | [Official, 2026-04] |
| 2026-05 | Import Center (Google, Meta, Pinterest); cross-account portfolios; seasonality for portfolios and shared budgets GA; DDA to all advertisers | Import, bidding | [Official, 2026-05] |
| 2026-05-19 | Activate 2026: AI Max, PMax search insights, custom columns with LTV and AOV, Merchant Center self-serve, UCP and Copilot Checkout, Ad Studio brand kits, shareable previews | Multiple | [Official, 2026-06] |
| 2026-06 | Product explorer in Merchant Center (under 100,000 SKUs); ad disclaimers guidance | Commerce | [Official, 2026-06] |
| 2026-06 | BingAds PHP REST SDK repository active (created 2025-06) | API | GitHub |
| 2026-07-27 | Ad Preview Hub extended to PMax (MSN, Bing Search, Outlook) | PMax | [Official, 2026-07] |
| 2026-07 | Copilot in Monetize and Curate open beta (MCP backed, publisher side) | Sell side | [Official, 2026-07] |
| 2026-08-04 | Conversions API documentation published (updated 2026-08-15); beta, per account enrollment | Measurement | [Official, 2026-08] |
| 2026-08-11 | Bulk edit tool for disapproved assets | Policy | [Official, 2026-08] |
| 2026-08-12 | Clarity AI Visibility reporting expanded (Topic Insights, grounding queries, citation share, Share of Authority) | Analytics | [Official, 2026-08] |
| 2026-08 | First monthly product newsletter on LinkedIn | Comms | Trade press |
| 2026-08-27 | AI Max for Search GA | Search | [Official, 2026-08] |
| 2026-09-08 | PMax uplift experiments GA (as announced in August) | PMax | [Official, 2026-08] |
| 2026-09-30 | Experiments GA across Search, Shopping, Audience, PMax; HubSpot integration; LinkedIn company lists 10,000; SOAP retirement 2027-01-31 | Multiple | [Official, 2026-09] |
| 2026 (date unclear) | Reports that Max CPC is unavailable for some new campaigns | Bidding | [Unverified] |
| 2026-08 (headline) | Reports of a 7 day gate on offline conversion uploads | Measurement | [Unverified] |

## 4. Best practice consensus

1. Import from Google for speed, then fix settings that imports carry poorly: location intent, ad distribution, Audience Network exposure, bids and budgets, tracking templates [Practitioner consensus].
2. Build Microsoft goals in UET before switching on conversion based bidding; imported Google conversion actions do not exist in Microsoft [Practitioner consensus].
3. Separate brand and non-brand; exclude brand from PMax with brand lists [Practitioner consensus].
4. Review syndicated partners by publisher and exclude failing domains [Practitioner consensus].
5. Use Microsoft only levers: LinkedIn profile targeting and bid adjustments for age, gender, device and audience [Practitioner consensus].
6. Fill every asset slot; logos, images and multimedia ads increase eligibility on right rail and Copilot [Practitioner consensus] [Unverified] for Copilot weighting.
7. Feed quality caps Shopping and PMax performance [Practitioner consensus].
8. Comply with consent mode in Europe and test the asc parameter after CMP changes [Official, 2025-03].
9. Feed qualified pipeline back via offline conversions (MSCLKID) for lead gen [Practitioner consensus].
10. Test big changes as Experiments now that they are GA across campaign types [Official, 2026-09].

## 5. Contested topics

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Copilot reporting | Some guides: a Copilot segment exists in network or distribution reports | Others: Copilot is mixed with Microsoft sites or no Copilot metrics exist | Check the account; report "not separable" when absent |
| Copilot opt-out | Guides say eligible campaigns are opted in and cannot opt out | No official confirmation found | Treat as unconfirmed; ask the account team |
| Brand agents status | Adweek (2025-03) called branded agents unveiled | Microsoft and 2026 roundups call them planned or pilot | Pilot via account team only |
| Modeled conversions under consent mode | Microsoft (2025-08, 2026-02) describes modeling to fill gaps | Usercentrics says no modeling for denied users; MB Adv says ACM opt-in needed | Treat modeled data as estimates; verify which goals show modeling |
| ad_user_data parameter | One guide says both ad_storage and ad_user_data are needed | Microsoft docs describe ad_storage only | Follow Microsoft FAQ |
| CPC advantage vs Google | Many practitioners report 20% to 40% lower CPCs | Competitive verticals sometimes show parity | Measure with the parity report |
| HubSpot integration status | Microsoft roundup (2026-09) describes it as available | HubSpot docs (2026-09-07) describe an opt-in beta | Check in HubSpot and Microsoft before planning |
| PMax incrementality | Microsoft claims about 8% more incremental conversions | No independent method published | Run PMax uplift experiments |

## 6. What top operators do differently

- They maintain an explicit divergence register: which fields differ from Google and why, and they scope scheduled imports to never overwrite those fields.
- They run a monthly Microsoft vs Google parity report on matched keywords and move budget to Microsoft where CPC ratios are low and CVR parity holds.
- They use LinkedIn profile layers as Bid only on Search and company lists on Audience campaigns, turning Microsoft into a cheap ABM complement to LinkedIn Ads.
- They prune syndicated partners by domain every 2 weeks rather than switching partners off wholesale.
- They treat Copilot as an eligibility problem (assets, feeds, broad or AI Max on profitable campaigns) and tell stakeholders the truth about measurement.
- They bid lead gen to SQL or opportunity via offline imports, pooling campaigns in portfolios to reach volume.
- They use Experiments and PMax uplift tests before scaling, not platform reported ROAS.
- They automate alerts (scripts, rules) for zero conversion days, budget caps and import changes.

## 7. Common expensive mistakes

| Mistake | Typical cost | Prevention |
|---------|--------------|------------|
| Import and forget (Google budgets, bids, targets copied) | Overpaying on low volume campaigns or starving profitable ones | Post-import fix list, reset from Microsoft data |
| Scheduled import overwriting Microsoft changes | Divergence undone silently | Scope imports, check import history |
| Location intent left at presence or interest | Spend outside target markets | "People in" |
| Search campaigns serving on Audience Network unnoticed | Display style clicks at search CPCs | Opt out or adjust |
| No partner review | Low quality syndication spend | Publisher report every 2 weeks |
| No UET goals before tCPA or tROAS | Bidding blind | Measurement gate |
| Consent mode missing or CMP blocking UET in Europe | Lost tracking and remarketing, policy notices | Default denied before CMP, asc test |
| PMax without brand exclusions or negatives | Brand cannibalization | Brand lists, negative lists |
| PMax and Shopping overlapping by accident | Internal competition | Product splits |
| Bid adjustments on strategies that ignore them | False sense of control | Verify per strategy |
| SOAP integrations ignored | Breakage at 2027-01-31 | Migration plan |

## 8. Benchmarks

| Metric | Value | Source | Date | Sample and caveat |
|--------|-------|--------|------|-------------------|
| Copilot ad relevance vs traditional search | About 25% better | Microsoft via Adweek and Microsoft blog | 2025-03 | Company research, method not disclosed |
| Copilot CTR vs traditional search ads | Roughly 2x | Microsoft via Adweek | 2025-03 | Company claim |
| PMax incremental conversions | About +8% | Microsoft at Activate 2026 | 2026-05 | Company claim, method not public |
| Microsoft volume vs Google | 5% to 20% of Google clicks on the same keywords | Practitioner rule of thumb | Ongoing | [Unverified]; replace with Keyword Planner and account data |
| Microsoft CPC vs Google | 0.6x to 0.9x | Practitioner reports | Ongoing | [Contested]; varies by vertical |
| CVR parity | 0.8x to 1.2x | Practitioner reports | Ongoing | [Practitioner consensus] |

No independent, method disclosed, cross account Microsoft Advertising benchmark study from 2025 to 2026 was confirmed in this research. The agent must rely on account history and Google parity first.

## 9. Tools, APIs and MCP servers

| Tool | Type | Status | Notes |
|------|------|--------|-------|
| Microsoft Advertising Editor | Official desktop | Active | Ads Studio inside since 2025-05; PMax negatives since 2026-03 |
| Scripts and automated rules | Official | Active | PMax support since 2025-05 |
| Microsoft Advertising API (SOAP v13) | Official | Retiring 2027-01-31 | Features continue until retirement |
| Microsoft Advertising REST API | Official | Active, migration target | SDKs include PHP REST (repo created 2025-06) |
| Conversions API | Official | Beta, per account | capi.uet.microsoft.com |
| Clarity MCP server | Official (Clarity) | Active | github.com/microsoft/clarity-mcp-server |
| Microsoft Ads MCP servers | Community and commercial | Active, varied quality | shinypebble, wvuhskr, bit-of-a-shambles, james-julius, Insightful-Pipe, Synter, PaidSync, adkit, opusgrowth |
| Official Microsoft Advertising MCP server | Not found | n/a | GitHub search 2026-10-08 found none; Microsoft shipped an MCP backed Copilot for publishers (Monetize, Curate) |

## 10. Official sources to monitor

| Source | URL | Cadence | What to look for |
|--------|-----|---------|------------------|
| Microsoft Advertising blog | https://about.ads.microsoft.com/en/blog | Monthly roundup | Feature launches, GA vs pilot |
| Product newsletter on LinkedIn | Microsoft Advertising LinkedIn page | Monthly since 2026-08 | Summaries and links |
| API release notes | https://learn.microsoft.com/en-us/advertising/guides/release-notes?view=bingads-13 | Monthly | API, REST and SOAP changes |
| UET consent FAQ | https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_uet_consentfaq | On change | Consent rules |
| Conversions API guide | https://learn.microsoft.com/en-us/advertising/guides/uet-conversion-api-integration?view=bingads-13 | On change | GA status, limits |
| Help center | https://help.ads.microsoft.com | As needed | Feature details, policies |
| Microsoft Advertising policies | Policy pages in the help center | Quarterly | Category rules, trademark, consent |
| Clarity blog | Clarity site | Monthly | Clarity and AI visibility features |

## 11. Open questions and watch list

1. Copilot placement reporting: is there an official Copilot segment, and can advertisers exclude Copilot?
2. Showroom ads, dynamic filters and brand agents: pilot or GA in 2026, and in which markets?
3. Dynamic Search Ads: status relative to AI Max final URL expansion.
4. Conversions API: GA date, self-serve enrollment, integrations (GTM server template, CDPs).
5. HubSpot integration: GA or beta; which lifecycle stages feed bidding.
6. Modeled conversions: does modeling require ACM, and which goals receive it?
7. Max CPC availability for new campaigns (reports in 2026 unverified).
8. Offline conversion upload timing gate (reported 2026-08, unverified).
9. LinkedIn profile targeting market list and PMax signal GA status beyond the 2025 pilot markets.
10. Universal Commerce Protocol and Copilot Checkout: merchant enrollment steps and eligible markets.
11. Video and CTV buying inside Microsoft Advertising after the Microsoft Invest wind down.
12. Bid adjustment behavior under each automated strategy (which adjustments apply).

## 12. Sources

1. Less busywork, more growth: What's new in Microsoft Advertising this September. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/september-2026/less-busywork-more-growth-what-new-in-microsoft-advertising-this-september. 2026-09-30.
2. AI Max for Search and other product news for August 2026. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/august-2026/ai-max-for-search-and-other-product-news-for-august-2026. 2026-08.
3. Reimagining search campaigns for the AI era with AI Max. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/august-2026/reimagining-search-campaigns-for-the-ai-era-with-ai-max. 2026-08-27.
4. Publisher Release Roundup: Copilot Enhancements. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/july-2026/publisher-release-roundup-copilot-enhancements. 2026-07.
5. Product explorer in Merchant Center and other product news for June 2026. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/june-2026/product-explorer-in-merchant-center-and-other-product-news-for-June-2026. 2026-06.
6. Microsoft Advertising Activate 2026: Key Takeaways from the Event. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/june-2026/microsoft-advertising-activate-2026-key-takeaways-from-the-event. 2026-06-19.
7. Building a new AI economy that creates value for everyone. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/june-2026/building-a-new-ai-economy-that-creates-value-for-everyone. 2026-06.
8. New import center and other product news for May 2026. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/may-2026/new-import-center-and-other-product-news-for-may-2026. 2026-05.
9. Performance Max updates and other product news for April 2026. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/april-2026/performance-max-updates-and-other-product-news-for-april-2026. 2026-04.
10. Win across all three eras of the web. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/april-2026/win-across-all-three-eras-of-the-web. 2026-04.
11. Evolving the Microsoft Advertising API Platform. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/april-2026/evolving-the-microsoft-advertising-api-platform. 2026-04.
12. Publisher release roundup: Q1 2026 edition. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/april-2026/publisher-release-roundup-q1-2026-edition. 2026-04.
13. Negative keywords for PMax and other product news for March 2026. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/march-2026/negative-keywords-for-pmax-and-other-product-news-for-march-2026. 2026-03.
14. Ad preview hub and other product news for February 2026. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/february-2026/ad-preview-hub-and-other-product-news-for-february-2026. 2026-02.
15. Advanced Consent Mode: Preserving accurate measurement while respecting user privacy. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/february-2026/advanced-consent-mode-preserving-accurate-measurement-while-respecting-user-privacy. 2026-02-19.
16. Performance Max updates and other product news for January 2026. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/january-2026/performance-max-updates-and-other-product-news-for-january-2026. 2026-01.
17. Asset-level editorial review and other updates for November. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/november-2025/asset-level-editorial-review-and-other-updates-for-november. 2025-11-18.
18. Publisher Release Roundup: Q4 2025 Edition. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/november-2025/publisher-release-roundup-q4-2025-edition. 2025-11-19.
19. Supplemental feeds and other product news for September. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/september-2025/supplemental-feeds-and-other-product-news-for-september. 2025-09.
20. Impression-based remarketing updates and other product news for August. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/august-2025/impression-based-remarketing-updates-and-other-product-news-for-august. 2025-08.
21. New custom report builder and other product updates for June. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/june-2025/new-custom-report-builder-and-other-product-updates-for-june. 2025-06.
22. Ads Studio in Editor and other product updates for May. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/may-2025/ads-studio-in-editor-and-other-product-updates-for-may. 2025-05.
23. Feed updates for Shopping campaigns and other product updates for April. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/april-2025/feed-updates-for-shopping-campaigns-and-other-product-updates-for-april. 2025-04.
24. Providing user consent signals on your Microsoft campaigns by May 5, 2025. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/march-2025/providing-user-consent-signals-on-your-microsoft-campaigns-by-may-5-2025. 2025-03.
25. Transforming the future of audience engagement. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/march-2025/transforming-the-future-of-audience-engagement. 2025-03.
26. New Performance Max tools and other product updates for February. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/february-2025/new-performance-max-tools-and-other-product-updates-for-february. 2025-02.
27. How PMax is working for advertisers and new updates. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/july-2024/how-pmax-is-working-for-advertisers-and-new-updates. 2024-07.
28. Bing Ads API Release Notes. Microsoft Learn. https://learn.microsoft.com/en-us/advertising/guides/release-notes?view=bingads-13. Rolling, entries 2025-07 and 2025-12 cited.
29. FAQ: UET and user consent. Microsoft Learn. https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_uet_consentfaq. Rolling.
30. Enhanced conversions. Microsoft Learn. https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_uet_enhancedconversions. Rolling.
31. Conversions API (CAPI). Microsoft Learn. https://learn.microsoft.com/en-us/advertising/guides/uet-conversion-api-integration?view=bingads-13. 2026-08-04, updated 2026-08-15.
32. ApplyOfflineConversions service operation. Microsoft Learn. https://learn.microsoft.com/en-us/advertising/campaign-management-service/applyofflineconversions?view=bingads-13. Rolling.
33. ConversionGoal data object. Microsoft Learn. https://learn.microsoft.com/en-us/advertising/campaign-management-service/conversiongoal?view=bingads-13. Rolling.
34. Microsoft's Copilot adds Showroom ads and Dynamic filters. Search Engine Land. https://searchengineland.com/microsoft-copilot-showroom-ads-dynamic-filters-453019. 2025-03.
35. Microsoft Lures Brands to Advertise in Chatbot Copilot with New Formats and AI Agents. Adweek. https://www.adweek.com/media/microsoft-copilot-ai-ads-branded-ai-agents/. 2025-03.
36. Microsoft Brand Agent Rolls Out In April, Powered By Copilot. MediaPost. https://www.mediapost.com/publications/article/403904/microsoft-brand-agent-rolls-out-in-april-powered.html. 2025-03.
37. Giant, AI ads are coming to Windows Copilot. PCWorld. https://www.pcworld.com/article/2633816/giant-ai-ads-are-coming-to-windows-copilot-thanks-microsoft.html. 2025-03.
38. Microsoft launches AI Max and new ad tools for the agentic web era. Search Engine Land. https://searchengineland.com/microsoft-launches-ai-max-and-new-ad-tools-for-the-agentic-web-era-474939. 2026.
39. Microsoft Advertising publishes Conversions API documentation. Search Engine Land. https://searchengineland.com/microsoft-advertising-publishes-conversions-api-documentation-485356. 2026-08-18.
40. Microsoft gates its new Conversions API behind per-account pilot approval. PPC Land. https://ppc.land/microsoft-gates-its-new-conversions-api-behind-per-account-pilot-approval/. 2026-08.
41. Microsoft Advertising gains LinkedIn company lists of up to 10,000 firms. PPC Land. https://ppc.land/microsoft-advertising-gains-linkedin-company-lists-of-up-to-10-000-firms. 2026.
42. Microsoft Ads experiments GA, plus HubSpot and REST news. Relevant Audience. https://www.relevantaudience.com/digital-marketing-en/microsoft-advertising-optimization-experiments-september-2026/. 2026-09.
43. Microsoft Launches Modeled Conversions for UET Consent Mode. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2025-08/microsoft-launches-modeled-conversions-for-uet-consent-mode/. 2025-08-07.
44. Microsoft Advertising Publishes First Product Newsletter. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-08/microsoft-advertising-first-product-newsletter/. 2026-08.
45. Microsoft Activate 2026 Recap. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-05/microsoft-activate-2026-recap/. 2026-05.
46. Microsoft Advertising Activate 2026 Recap. ALM Corp. https://almcorp.com/blog/microsoft-advertising-activate-2026-recap/. 2026-05.
47. Everything Microsoft Advertising Announced at Activate 2026. ALM Corp. https://almcorp.com/news/microsoft-advertising-activate-2026-announcements-ai-max/. 2026-05.
48. Microsoft Ads August Update: PMax Previews, AI Visibility. Digital Applied. https://www.digitalapplied.com/blog/microsoft-ads-august-2026-pmax-preview-ai-visibility. 2026-08.
49. Microsoft Ads in 2026: Copilot Integration, Publisher Marketplace, and What's New. CapConvert. https://www.capconvert.com/learn/blog/microsoft-ads-in-2026-copilot-integration-publisher-marketplace-and-what-s-new. 2026.
50. Ads in Microsoft Copilot 2026: showroom ads and what SMBs need to know. Gruenberg Digital. https://www.gruenberg-digital.de/en/ki-blog/advertising-in-microsoft-copilot-2026-showroom-ads-offer-highlights.html. 2026.
51. How to Advertise on Microsoft Copilot in 2026. Thrad. https://www.thrad.ai/content/how-to-advertise-on-microsoft-copilot. 2026.
52. How to Advertise in Microsoft Copilot: A 2026 Guide to Copilot Ads. Branded Agency. https://www.brandedagency.com/blog/advertise-microsoft-copilot-guide. 2026.
53. Microsoft UET Is Not Optional, Here's How To Fix Campaigns. Usercentrics. https://usercentrics.com/knowledge-hub/microsoft-uet-consent-mode/. 2025 to 2026.
54. Microsoft Ads Conversion Tracking and UET: 2026 Guide. MB Adv. https://www.mbadv.agency/microsoft-ads/microsoft-ads-conversion-tracking-uet. 2026.
55. How to Fix Microsoft Consent Signals in 2026. Seers. https://seers.ai/blogs/how-to-fix-microsoft-consent-signals/. 2026.
56. Microsoft UET Consent Mode is now mandatory. Cookie Information. https://cookieinformation.com/blog/implement-microsoft-uet-consent-mode/. 2025.
57. Implement Microsoft Advertising enhanced conversions for offline conversions. Adobe Experience League. https://experienceleague.adobe.com/en/docs/advertising/search-social-commerce/campaign-management/management/special-workflows/microsoft-enhanced-conversions. Rolling.
58. Microsoft Ads offline conversions. MoEngage partner docs. https://www.moengage.com/docs/partner-guide/retargeting-and-audience-sync/ad-conversions/microsoft-ads-offline-conversions. Rolling.
59. Microsoft Advertising tag archive. AdExchanger. https://www.adexchanger.com/tag/microsoft-advertising/. 2025 to 2026.
60. Microsoft Advertising Updates For Shopping Campaigns, Audience Ads, Performance Max and More. Search Engine Roundtable. https://www.seroundtable.com/microsoft-advertising-updates-39160.html. 2025.
61. Microsoft Ads Drops Max CPC on New Campaigns. Ecommerce Paradise. https://ecommerceparadise.com/microsoft-ads-drops-max-cpc/. 2026. Headline only, unverified.
62. Offline conversion uploads: 7-day upload gate. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-08/offline-conversion-uploads-7-day-upload-gate/. 2026-08. Headline only, unverified.
63. 8 Microsoft Advertising Changes in 2026, and What to Do About Each. Michael Bennett. https://michaelbennett.co/blog/microsoft-ads-2026-changes. 2026. Headline only.
64. microsoft/clarity-mcp-server. GitHub. https://github.com/microsoft/clarity-mcp-server. Created 2025-04-15.
65. BingAds SDK repositories (Python, .NET, Java, PHP, PHP REST). GitHub. https://github.com/BingAds. Checked 2026-10-08.
66. shinypebble/microsoft-ads-mcp. GitHub. https://github.com/shinypebble/microsoft-ads-mcp. Created 2026-06-17.
67. wvuhskr/mcp-microsoft-ads. GitHub. https://github.com/wvuhskr/mcp-microsoft-ads. Created 2026-08-24.
68. bit-of-a-shambles/microsoft-ads-mcp-server. GitHub. https://github.com/bit-of-a-shambles/microsoft-ads-mcp-server. Created 2026-01-26.
69. Synter-Media-AI/mcp-server. GitHub. https://github.com/Synter-Media-AI/mcp-server. Created 2026-01-29.
70. itallstartedwithaidea/advertising-hub. GitHub. https://github.com/itallstartedwithaidea/advertising-hub. Created 2026-03-10.
