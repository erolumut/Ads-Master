# Market Intelligence Playbooks

End to end plays. Each lists the trigger, steps, sources, outputs and handoffs. Time boxes assume one analyst session per step unless noted.

## Play 1: New client competitive baseline (week 1)
Trigger: ads-setup completed, or the growth-orchestrator diagnosis requests it.
1. Confirm the competitor set with the four lists (direct, search, AI, alternatives). Propose COMPETITORS.md edits.
2. Ad libraries: 30 minute teardown per top 3 competitor (Meta, Google Transparency Center, TikTok, LinkedIn for B2B).
3. Search: Auction Insights (if accounts exist), organic competitors report, 50 money keyword SERP sample with AI Overview presence.
4. AI visibility quick check: 10 to 20 prompts, 3 runs, 3 to 4 engines.
5. Offers and prices: offer matrix for top 5 competitors; price index for hero SKUs or plans.
6. VoC: 200+ reviews across our product and 3 competitors, coded; language bank.
7. Demand: Google Trends 5 years for the category and share of search for the brand set.
8. Synthesis: competitive baseline template with gaps we can own and top 10 recommendations by owner.
Outputs: `_competitive-baseline.md`, proposed edits to COMPETITORS.md and AUDIENCE.md.
Handoffs: creative-strategy (angles, language bank), google-ads (auction and brand bidding), seo (gaps), ai-search-optimization (AI gaps and cited sources), growth-orchestrator (price corridor, market notes).

## Play 2: Pre-launch intelligence for a new channel
Trigger: growth-orchestrator plans a channel test (TikTok, LinkedIn, ChatGPT ads, Reddit, Pinterest, Amazon).
1. Check if competitors use the channel: ad libraries (TikTok Ad Library or Creative Center, LinkedIn Ad Library), manual observation (ChatGPT ads as a normal user in an eligible market; Reddit promoted posts in relevant communities; Amazon sponsored placements).
2. Category creative norms on the channel: Top Ads (TikTok), top posts in communities (Reddit), top pins (Pinterest).
3. Audience presence: platform audience estimates for the ICP and market.
4. Demand signals on the channel: TikTok keyword insights, Pinterest Trends, marketplace search suggestions.
5. Output: channel intel brief with competitor presence, creative norms, audience size, risks.
Handoffs: growth-orchestrator (go or no go input), creative-strategy (native creative norms), channel agent if one exists.

## Play 3: Competitor launches a big promotion
Trigger: alert (discount 20%+ or new free shipping, guarantee or bundle), especially in peak season.
1. Verify: landing page, ad library ads, email if subscribed; capture date and URL.
2. Scope: which products, markets, channels, end date.
3. Estimate impact: check our daily CVR and CPA trend since the promo started (from channel agents or measurement).
4. Options for the human (through growth-orchestrator): hold and emphasize non price value; match selectively on overlapping hero SKUs; counter with a different mechanic (bundle, gift, guarantee); shift budget to segments less exposed to the promo.
5. Margin check for each option with growth-orchestrator's unit economics.
Outputs: journal alert, short options memo. Handoffs: growth-orchestrator (decision), creative-strategy (counter messaging), cro (page messaging), commerce-feeds (sale price and promotions in feeds).

## Play 4: New competitor enters our auctions or bids on our brand
Trigger: Auction Insights shows a new domain with 10%+ overlap, or brand bidding detected.
1. Identify the advertiser in the Transparency Center (domain search), capture copy and landing pages.
2. Check their social ad activity and offer.
3. For brand bidding: capture SERP evidence by location and device; check whether ad text uses our trademark.
4. Options: brand defense budget, trademark complaint where policy allows, affiliate terms enforcement, counter copy on shared terms, ignore if overlap is small and stable.
Outputs: journal alert, search competition update. Handoffs: google-ads, microsoft-ads, human (legal for trademark).

## Play 5: AI assistants recommend competitors instead of us
Trigger: AI visibility benchmark shows a competitor with a mention or recommendation lead of 20+ points on priority prompts, or sales hears "ChatGPT recommended X".
1. Expand the prompt set around the losing prompts; 5 runs per engine.
2. Citation source analysis: which domains are cited when the competitor is recommended.
3. Compare presence on those domains: reviews (count, rating, recency), Reddit threads, comparison articles, Wikipedia or knowledge panels, YouTube.
4. Check accuracy of statements about us.
5. Output: AI visibility benchmark with "sources to win" list and wrong facts list.
Handoffs: ai-search-optimization (program), seo (content and links), growth-orchestrator (review program, digital PR budget), chatgpt-ads (paid presence on lost prompts if eligible).

## Play 6: Pricing pressure or a pricing decision
Trigger: win and loss or reviews mention price more often; leadership considers a price change.
1. Price corridor: effective prices, offer components, financing norms by market.
2. VoC: share of price related objections in our and competitor reviews, and what customers say they get for the price.
3. Win and loss: price as stated vs real reason.
4. Positioning check: is price the axis buyers use, or value, speed, specialization?
5. Output: offer and pricing matrix plus recommendation options (value framing, packaging, guarantee, price test design for cro and growth-orchestrator).
Handoffs: growth-orchestrator (economics), cro (price test design), creative-strategy (value framing).

## Play 7: Win and loss program setup (B2B, lead gen)
1. Agree with the human: sample size per quarter (10 to 20 interviews), interviewer, incentives, consent wording.
2. Pull closed deals from the CRM (last 30 to 90 days), balanced won and lost, by segment.
3. Run interviews with the guide in offer-pricing-and-positioning.md; record with consent.
4. Code and quantify reasons; compare with CRM loss reasons.
5. Deliver quarterly; update battlecards and COMPETITORS.md.
Handoffs: linkedin-ads and google-ads (messaging), cro (objection handling), human (product and sales process).

## Play 8: Quarterly landscape refresh
1. Re-run the competitor set review; add new entrants from auctions, ad libraries, AI answers and reviews.
2. Update competitor profile cards.
3. Refresh positioning map and offer matrix.
4. Full AI visibility benchmark (same prompt set plus a new cohort).
5. VoC refresh: last quarter's reviews and tickets.
6. Market size update if inputs changed.
7. Output: `_competitive-landscape-<YYYY-QN>.md` for the quarterly strategy reset.
Handoffs: growth-orchestrator (strategy draft inputs), all consumers.

## Play 9: Market entry research
Trigger: growth-orchestrator New market launch workflow.
1. Market snapshot: size, online share, growth, payment norms, language (market-sizing.md, demand-and-trend-research.md).
2. Local competitors vs international players: ad libraries per country, local marketplaces, local search results in the local language.
3. Channel landscape: search engine shares, social platforms, marketplaces, AI assistant ads availability in that market.
4. Price levels and offer norms (installments in Turkey, BNPL and cash on delivery in the Gulf, VAT inclusive pricing in the EU).
5. VoC in the local language (local review sites and complaint platforms, for example Şikayetvar in Turkey).
6. Output: `_market-entry-<geo>.md`.
Handoffs: growth-orchestrator (launch plan), measurement (consent rules), seo (international), creative-strategy (localization).

## Play 10: Peak season intelligence (BFCM, Ramadan, 11.11)
1. Eight weeks before: last season's competitor promo calendar and depths; expected dates.
2. Four weeks before: switch monitoring to peak mode (daily prices, twice weekly ad libraries, daily Auction Insights).
3. During: daily alert digest to the daily check.
4. After: post peak report of competitor tactics and our relative performance; update the promo calendar and memory if patterns repeat.
Handoffs: growth-orchestrator (peak budget), creative-strategy, channel agents, commerce-feeds.
