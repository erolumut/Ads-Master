# Platform Overview and Timeline

> Knowledge as of 2026-10. Facts read from OpenAI pages are labeled [Official]. Many OpenAI help and developer pages were read through dated mirrors captured 2026-09-22 to 2026-09-24 because openai.com was not directly reachable during research; re-verify live before acting.

## 1. What ChatGPT Ads is

ChatGPT Ads is OpenAI's advertising product inside ChatGPT. Advertisers buy through:
1. **Ads Manager (self-serve beta)** at ads.openai.com, opened from 2026-05-05 [Official, 2026-05].
2. **OpenAI Ads Solutions team** (managed sales for larger advertisers) [Official, 2026-09].
3. **Agency partners** Dentsu, Omnicom, Publicis, WPP and **technology partners** Adobe, Criteo, Kargo, Pacvue, StackAdapt (named 2026-05-05) [Official, 2026-05]. Later partners reported: AdRoll access 2026-08-11 [Unverified], Amazon DSP pilot [Unverified]. OpenAI says over 50 technology and measurement partners by 2026-08-31 [Official, 2026-08].
4. **Integrations**: HubSpot (first CRM partner) and a ChatGPT Ads app in the Shopify App Store, both from 2026-09-16; Shopify app international from 2026-09-23 [Official, 2026-09].
5. **ChatGPT Ads Manager plugin** inside ChatGPT: create, update and analyze campaigns with prompts, turn a website or brief into a campaign [Official, 2026-09].
6. **Advertiser API** (api.ads.openai.com/v1) for programmatic management and reporting [Official, 2026-09].

Scale claims: $1B annualized revenue run rate in under 200 days, tens of thousands of advertisers, over 40 countries via sales and partners, CPC and outcome optimized bidding are the majority of campaigns (OpenAI, 2026-08-31) [Official, 2026-08]. ChatGPT reach: more than 1B weekly users (2026-08) and 1.2B weekly people (2026-10) [Official, 2026-10]. Reported internal targets of $2.5B ad revenue in 2026 and over $100B by 2030 [Unverified] (Digiday relay, 2026-08).

## 2. Who sees ads (consumer side)

| Rule | Detail | Label |
|------|--------|-------|
| Plans | Free and Go see ads. Plus, Pro, Business, Enterprise and Edu do not | [Official, 2026-09] |
| Go plan | $8 per month in the US, expanded everywhere ChatGPT is available on 2026-01-16; launched in 171 countries from August 2025 | [Official, 2026-01] |
| Age | No ads for accounts that state or are predicted to be under 18 (signals: stated age, account age, time of use patterns, usage over time, topics) | [Official, 2026-09] |
| Logged out | Logged out users can see ads suitable for all audiences; mature content ads only for eligible logged-in users | [Official, 2026-09] |
| Exclusions | No ads in Temporary Chats or in the Atlas browser during the test | [Official, 2026-09] |
| Ads-Free option | Free users can switch to an ad free mode with lower message limits and reduced tools; Go users must switch to Free first | [Official, 2026-09] |
| Sensitive topics | No ads near personal health, mental health, political, emotionally reliant or other sensitive conversations | [Official, 2026-09] |
| Controls | Settings > Ad Controls: View History and Topics, Delete ads data, Personalize ads, Past chats and memory. Ad menu: Hide ad, Report ad, About this ad, Ask ChatGPT | [Official, 2026-09] |

Implication: your reachable audience is skewed to free and low price tier users. Paying power users (Plus, Pro) and most workplace users (Business, Enterprise) are not reachable. Confirm your buyers use ChatGPT on ad supported plans before heavy spend [Study, 2026-08] (SE Ranking recommendation).

## 3. Formats

| Format | Status (2026-10) | Description | Label |
|--------|------------------|-------------|-------|
| Chat card (standard ad unit) | Live | Below the response, labeled Sponsored, visually separated: advertiser name, favicon or logo, headline, description, image, landing page | [Official, 2026-09] |
| Product feed ads | Beta, live | Ads generated from a product feed using a product ad template: product images, titles, stars, prices, sale prices, brand. OpenAI says feed ads "have been among the strongest-performing ads in our program to date" | [Official, 2026-09] |
| Carousel | Live in some placements | Multiple products from one retailer in one placement; OpenAI decides single product vs carousel. About 23% of US desktop ads were carousels 2026-08-15 to 08-30 per a Sensor Tower relay | [Official, 2026-09] (reporting fields exist) and [Unverified] (share) |
| Sponsored Agents | Test with select US advertisers; not accepting early access requests | User opens a labeled conversation with an AI representative of the business from an ad, asks follow up questions, follows a link to the site | [Official, 2026-09] |
| Visual ads in image generation | US test with initial advertisers announced 2026-10-05, starting later in October | Image based ads (product inspiration, product in use, experiences) shown during image generation, labeled and separate from the generated image; press describes product carousels on the loading screen | [Official, 2026-10] |
| Hotel ads | Limited beta for approved advertisers, not open | Hotel property feed (`hotel_property_v1`) based ads | [Official, 2026-09] |
| AI text customization | Opt-in | Adapts existing headlines and descriptions to conversation context and translates copy to the user's language | [Official, 2026-09] |
| AI suggested creative | Live | AI suggested ad copy and imagery from landing page and objective; "Add new ad" prefill from website metadata | [Official, 2026-09] |
| Lead forms, business agents (API) | Removed from public API spec in 2026-09 | Self-serve returns 404 or 403 | [Unverified] (community API notes) |

## 4. How ads are matched and ranked

Inputs to selection [Official, 2026-09]:
1. Current conversation context and intent.
2. The ad itself: title, copy and landing page.
3. Advertiser context hints (ad group level) and targeting (geo, platform, custom audiences).
4. With ad personalization on (not in EEA or Switzerland): past chats, memory (if memory is on) and past ad interactions.

Ranking weighs relevance and advertiser bids in a relevance weighted second price auction [Official, 2026-09]. Each response can show one or more ad units depending on relevance [Official, 2026-09]; an August 2026 panel saw one sponsored offer per answer in every case [Study, 2026-08].

Observed behavior (independent):
- 66.3% of ChatGPT ads appeared after the second prompt or later in a conversation (Similarweb panel, July 2026) [Study, 2026-07]. Plan for ads that show mid conversation, after the user has refined the need.
- The same prompt can show an ad in one session and none in another [Study, 2026-08].
- Off topic placements: 14.35% of ad impressions were no more related to the query than random pairing; worst in relationships and news niches [Study, 2026-08].
- Ads were delivered as a separate event type in the response stream, with topic based matching observed across travel, sports, fashion and productivity prompts (independent reverse engineering, 2026-04) [Unverified].

What advertisers do not get: prompts, conversations, chat history, memories, names, emails, precise location or IP [Official, 2026-09]. There is no search query or prompt report; optimization is by hint variants and outcomes [Practitioner consensus].

## 5. Privacy model summary

| Topic | Rule | Label |
|-------|------|-------|
| Advertiser data access | Aggregate performance only (views, clicks, conversions) | [Official, 2026-09] |
| Direct messages | Messages a user sends to an advertiser (for example a Sponsored Agent) are visible to that advertiser | [Official, 2026-09] |
| Data sale | "We never sell your data to advertisers" | [Official, 2026-01] |
| EEA and Switzerland | No personalized ads initially; custom audiences not to be used | [Official, 2026-09] |
| Pixel data | OpenAI states it does not currently use pixel data for user level personalization | [Official, 2026-09] |
| Pixel cookies | `__oppref` 30 days (click reference), `__obref` 365 days (browser reference) on the advertiser domain | [Official, 2026-09] |
| Cross site cookie | Independent research reported a `__obi` cookie on `.openai.com` linking browsers across advertisers, classified by OpenAI as analytics; unconfirmed by OpenAI | [Unverified] |
| Automatic advanced matching | Pixel can detect, hash (SHA-256) and attach on page customer info; reportedly enabled on existing pixels on 2026-08-17 as opt-out | [Official, 2026-09] (feature) and [Unverified] (default change) |
| EU regulation | ChatGPT search reported 159.1M average monthly active EU recipients for the six months to 2026-03-31; trade press reports VLOSE designation on 2026-08-31 with DSA obligations from January 2027 (ad repository expected) | [Official, 2026-09] (user number) and [Unverified] (designation date) |

## 6. Dated timeline (January 2025 to October 2026)

| Date | Event | Label |
|------|-------|-------|
| 2025-05 | Fidji Simo named CEO of Applications at OpenAI (later author of the ads approach post) | [Unverified] |
| 2025-08 | ChatGPT Go launches (India first), reaching 171 countries by January 2026 | [Official, 2026-01] |
| 2025-09-29 | Instant Checkout (Etsy, Shopify coming) and the Agentic Commerce Protocol (ACP) with Stripe; merchants pay a fee on completed purchases | [Official, 2025-09] |
| 2025-10 | ChatGPT Atlas browser launches (later excluded from ads) | [Unverified] (date) |
| 2025-12-01 | Reported internal "code red" memo deprioritizing ads to focus on ChatGPT quality | [Unverified] |
| 2026-01-16 | "Our approach to advertising and expanding access to ChatGPT": test planned for US Free and Go; five principles (mission alignment, answer independence, conversation privacy, choice and control, long-term value); Go at $8 in the US | [Official, 2026-01] |
| 2026-02-09 | Ads test begins in the US for logged-in adults on Free and Go | [Official, 2026-02] |
| 2026-02 | Pilot pricing reported at about $60 CPM with $200k to $250k minimum commitments; early advertisers include Williams-Sonoma, Target, The Knot, Expedia, Best Buy; agency partners WPP, Omnicom, Dentsu | [Unverified] |
| 2026-02-20 | Adthena finds ads on about 0.8% of 500+ prompts | [Study, 2026-02] |
| 2026-03-02 | Criteo becomes the first ad tech partner integrated with the pilot | [Official, 2026-05] (Criteo) |
| 2026-03 | Ad Policies v1.0 published | [Official, 2026-09] |
| 2026-03-04 to 03-24 | Instant Checkout removed for Shopify merchants and other retailers; OpenAI says merchants will use their own checkout and focus shifts to discovery with ACP | [Unverified] (Digital Commerce 360) |
| 2026-03-26 | Pilot enters next phase; OpenAI reports no impact on consumer trust metrics and low dismissal rates; pilots announced for Canada, Australia, New Zealand; reported $100M annualized run rate and 600+ advertisers | [Official, 2026-03] and [Unverified] (revenue) |
| 2026-04 | Ad Policies v1.1: medical, legal and financial advice contexts no longer blocked by default; reported minimum commitment cut to $50k and CPMs down to $25 | [Official, 2026-09] and [Unverified] |
| 2026-05-05 | "New ways to buy ChatGPT ads": self-serve Ads Manager beta, CPC bidding added to CPM, partner list, pixel and Conversions API "recently launched"; $50k minimum removed | [Official, 2026-05] and [Unverified] (minimum) |
| 2026-05-07 | Plan announced to expand to UK, Mexico, Brazil, Japan, South Korea | [Official, 2026-05] |
| 2026-05 | Ad Policies v1.2: review standards and enforcement section | [Official, 2026-09] |
| 2026-06-05 | First wave of conversion optimized campaigns reported for accounts with pixel or CAPI before June 1 | [Unverified] |
| 2026-06-06 | UK pilot reported to start (managed sales) | [Unverified] |
| 2026-06-15 | Merchant Feed Terms of Service published | [Official, 2026-06] |
| 2026-06-22 | Criteo reports over 2,000 brands on ChatGPT Ads through Criteo | [Official, 2026-06] (Criteo) |
| 2026-07 | Ad Policies v1.3: advertiser policies, financial and health categories and markets | [Official, 2026-09] |
| 2026-08-06 | Product carousels reported in ChatGPT ads (one retailer per carousel) | [Unverified] (Digiday) |
| 2026-08-11 | ChatGPT Ads launched in UK, Mexico, Brazil, Japan, South Korea | [Official, 2026-08] |
| 2026-08-17 | Similarweb AI ads data: ads in 26% of ChatGPT responses (June, US desktop) | [Study, 2026-08] |
| 2026-08-18 | Expansion to 31 European markets announced (EU 27 plus Iceland, Liechtenstein, Norway, Switzerland), serving from the following week; managed and partner buying first | [Official, 2026-08] |
| 2026-08 | Ad Policies v1.4 (housing and job listings) and v1.5 (legal services eligible in the US) | [Official, 2026-09] |
| 2026-08-31 | $1B run rate; self-serve Ads Manager opens in India, Europe, Middle East and North Africa; over 40 countries; over 50 partners | [Official, 2026-08] |
| 2026-09-10 | Ad Policies v1.6: OpenAI may decline ads conflicting with its principles, business interests or competitive position; granular web platform targeting reported | [Official, 2026-09] |
| 2026-09-16 | "Reimagining advertising with AI": Sponsored Agents test (US), Ads Manager plugin in ChatGPT, AI suggested copy and imagery, opt-in AI text customization, HubSpot and Shopify integrations; UAE, Saudi Arabia, Israel, Turkey added to self-serve around this date | [Official, 2026-09] and [Unverified] (country date) |
| 2026-09-22 | Ads Manager Availability lists 56 countries as Available | [Official, 2026-09] |
| 2026-09-23 | Shopify ChatGPT Ads app expands internationally | [Official, 2026-09] |
| 2026-09-23 to 09-24 | Expansion to Indonesia, Malaysia, Philippines, Singapore, Thailand, Vietnam and Taiwan; over 60 countries reported | [Official, 2026-09] (post exists) and [Unverified] (exact date, count) |
| 2026-10-05 | "Building advertising for the way people use AI": visual ads during image generation (US test later in October), measurement partner expansion (Hightouch, Tealium, LiveRamp and others), 1-day view-through in reporting, brand safety pilots with DoubleVerify and Integral Ad Science, Negative Phrases for qualifying advertisers | [Official, 2026-10] (read via secondary summaries; verify) |

## 7. Country rollout (consumer serving vs advertiser access)

Advertiser access (self-serve) follows the legal entity country. Consumer serving follows where users are. They do not always move together.

| Wave | Consumer ads live | Self-serve for local advertisers | Label |
|------|-------------------|----------------------------------|-------|
| US | 2026-02-09 | 2026-05-05 | [Official] |
| Canada, Australia, New Zealand | Pilots from 2026-03-26 announcement (live by mid April reported) | Listed Available by mid 2026 | [Official] and [Unverified] (dates) |
| UK | Pilot reported 2026-06-06; launched by 2026-08-11 | Listed Available by July 2026 | [Official] and [Unverified] |
| Japan, South Korea, Mexico, Brazil | Launched by 2026-08-11 | Japan and Korea first listed Coming Soon, Available by 2026-09-22 | [Official] |
| 31 European markets | From the week after 2026-08-18 | 2026-08-31 | [Official] |
| India, MENA (Algeria, Bahrain, Egypt, Iraq, Jordan, Kuwait, Lebanon, Morocco, Oman, Qatar, Tunisia) | Around late August to early September | 2026-08-31 | [Official] and [Unverified] |
| UAE, Saudi Arabia, Israel, Turkey | September | Mid September | [Unverified] (dates) |
| Southeast Asia and Taiwan | Late September announcement | Late September | [Official] and [Unverified] |

New self-serve accounts may initially target only their home country; targeting other countries requires identity verification and a required amount of home country spend [Official, 2026-09].

## 8. Product principles that constrain tactics
- Ads never change answers ("Ads do not influence the answers ChatGPT gives you") [Official, 2026-01]. You cannot buy inclusion in the response.
- OpenAI does not optimize for time spent and says it prioritizes trust over revenue [Official, 2026-01]. Expect conservative placement around sensitive topics and continued tightening when trust metrics move.
- A paid ad free tier will always be available [Official, 2026-01].
- OpenAI may decline advertisers for competitive reasons (v1.6) [Official, 2026-09]; trade press reported rejections of standalone image and audio generation tools [Unverified].

## 9. Open questions to watch
- Whether CPA billing (pay per conversion) arrives; as of 2026-10 conversion campaigns bill per click or impression [Official, 2026-09].
- Query or topic level reporting (none today).
- Multi advertiser carousels (built for, not confirmed live) [Unverified].
- Sponsored Agents general availability, pricing and lead handling.
- EU DSA ad repository launch (expected around January 2027) [Unverified].
- Expansion of personalization to EEA.
- Visual ads performance and whether they reach markets outside the US.
