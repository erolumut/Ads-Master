---
name: chatgpt-ads
description: Run ChatGPT Ads (OpenAI Ads Manager at ads.openai.com, Advertiser API) and plan AI assistant ad surfaces (Google ads in AI Overviews and AI Mode, Microsoft Copilot ads, Amazon Alexa for Shopping sponsored prompts, Perplexity, Meta AI, Sponsored Agents). Use to check eligibility and country availability, set up and verify accounts, build campaigns, ad groups and context hints, choose Views (CPM), Clicks (CPC) or Conversions (oCPC, oCPM) and Maximize results, set budgets and pacing, launch product feed and carousel ads, write chat card copy, install the OpenAI pixel and Conversions API with oppref and dedup, read Insights, audit accounts, design incrementality tests, set kill and scale rules, troubleshoot Not serving, low delivery and policy rejections, and decide which AI ad surface to test next.
---

# ChatGPT Ads and AI Assistant Ad Surfaces

> Knowledge as of 2026-10. ChatGPT Ads launched in February 2026 and changed almost monthly (formats, bidding, countries, policies, measurement). Run the Freshness Protocol before acting on any feature, setting, policy or benchmark.

## Mission and scope
Make ChatGPT Ads an incremental, measured acquisition channel when it fits the business, and decide where other AI assistant ad surfaces belong in the media plan.

In scope:
- OpenAI ChatGPT Ads: eligibility, account setup, structure, context hints, bidding, budgets, creative, product feed ads, Sponsored Agents, visual ads, pixel and Conversions API, reporting, policies, API and MCP tooling, testing and scaling.
- Cross surface AI ad strategy: Google ads in AI Overviews and AI Mode, Microsoft Copilot ads, Amazon Alexa for Shopping (formerly Rufus) sponsored prompts, Perplexity, Meta AI, Gemini, Grok, Claude, AI ad networks.

Out of scope (hand off): building Google and Microsoft campaigns (google-ads, microsoft-ads), organic AI visibility (ai-search-optimization), merchant feeds and agentic checkout (commerce-feeds), tracking implementation (measurement).

Evidence labels used in this skill and its references: `[Official, YYYY-MM]` OpenAI or platform documentation, `[Study, YYYY-MM]` data study with a stated method (usually a vendor panel), `[Practitioner consensus]`, `[Contested]`, `[Unverified]` (single source, trade press or could not confirm). Trade press reports that OpenAI has not confirmed are always `[Unverified]`.

## Intake (minimum facts; where to find them)
| Fact | Why it matters | Where in ads-master/ |
|------|----------------|---------------------|
| Advertiser legal entity country and billing currency | Self-serve access follows the legal entity country; country, currency and timezone are fixed at account creation | PROJECT_BRIEF.md section 1, 7 |
| Target markets (countries, regions) | Ads serve only where ChatGPT Ads is live and where the account may target | PROJECT_BRIEF.md section 1 |
| Category and regulated status | Finance, health, legal are US only and case by case; many categories are prohibited | PROJECT_BRIEF.md section 8 |
| Business model, AOV or deal value, margin, target CPA or ROAS | Budget sizing and kill rules | PROJECT_BRIEF.md sections 3, 4 |
| Monthly test budget available | Decides test design (learning test vs decision test) | PROJECT_BRIEF.md section 5 |
| Conversion definitions and source of truth | Choosing the optimization event and reconciling | MEASUREMENT.md |
| Site stack, tag manager, server runtime, consent platform | Pixel vs CAPI vs both, consent gating | PROJECT_BRIEF.md section 7, MEASUREMENT.md |
| Product catalog and feed source (ecommerce) | Product feed campaigns and carousels | PROJECT_BRIEF.md section 7 |
| Existing ChatGPT Ads account ID, access level, exports | Audit and reporting | PROJECT_BRIEF.md section 6, data/imports/ |
| Google and Microsoft campaign types running | Whether AI Overviews, AI Mode and Copilot inventory is already reachable | PROJECT_BRIEF.md section 6 |

Cold start (no `ads-master/`): ask only for legal entity country, target countries, category, business model, monthly test budget, target CPA or ROAS, and whether a pixel or server events exist. Or suggest the `ads-setup` skill.

## Platform snapshot (verify with Freshness Protocol)
| Item | Current state | Label |
|------|---------------|-------|
| Who sees ads | Logged-in and logged-out users on Free and Go plans; not Plus, Pro, Business, Enterprise, Edu; not users identified or predicted under 18; not in Temporary Chat or the Atlas browser | [Official, 2026-09] |
| Where ads appear | Below the response, labeled Sponsored; one or more units per response; carousel for product feeds; visual ads during image generation in US test from late October 2026 | [Official, 2026-10] |
| Matching | Current conversation context and intent, ad title, copy and landing page, context hints, geo, platform and custom audience targeting; with personalization on, past chats, memory and ad interactions | [Official, 2026-09] |
| EEA and Switzerland | No ad personalization; do not use custom audiences | [Official, 2026-09] |
| Objectives | Views (CPM), Clicks (CPC), Conversions (oCPC click billing or oCPM impression billing for eligible advertisers) | [Official, 2026-09] |
| Auction | Relevance weighted second price auction | [Official, 2026-09] |
| Bid guidance | Start CPC max bid at $3 to $5 (US); no recommended bid for conversion campaigns | [Official, 2026-09] |
| Budgets | Daily (7-day average, max 2x per day, max 7x per Sunday to Saturday week) or campaign total; minimum daily $25, EUR 15, GBP 15 | [Official, 2026-09] |
| Measurement | OpenAI pixel and Conversions API, oppref click reference, event_id dedup, click windows 7, 14 or 30 days, 1-day view-through for reporting only | [Official, 2026-10] |
| Countries (advertiser self-serve) | 56 listed as Available on 2026-09-22, then Southeast Asia and Taiwan added late September; over 60 reported | [Official, 2026-09] and [Unverified] |
| Scale | $1B annualized run rate and tens of thousands of advertisers (2026-08-31); 1.2B weekly users claimed in October 2026 | [Official, 2026-08] and [Official, 2026-10] |
| Benchmarks | OpenAI says there are no cross advertiser performance benchmarks yet | [Official, 2026-09] |

## Operating protocol
1. **Load state.** Read PROJECT_BRIEF.md, MEASUREMENT.md, STRATEGY.md, PRIORITIES.md, memory/chatgpt-ads.md and the last 10 journal entries.
2. **Freshness check.** For anything that depends on platform behavior, check the sources in the Freshness Protocol and log changes found.
3. **Eligibility gate.** Confirm legal entity country is Available in Ads Manager Availability, category is allowed for that country under the Ad Policies, the landing pages are crawlable by OAI-AdsBot, and target users are on ad supported plans in a served market. Output a go, conditional go or no go with reasons. See [Account setup and eligibility](references/account-setup-and-eligibility.md) and [Policies and brand safety](references/policies-and-brand-safety.md).
4. **Fit assessment.** Score the business on intent fit (do people ask ChatGPT about this category before buying), offer clarity, landing page continuity, measurement readiness and budget sufficiency. Use the adaptation matrix below.
5. **Measurement first.** Specify the data source, standard events, pixel plus CAPI with shared event_id, oppref capture through redirects, consent gating, UTM template and GA4 channel rules. Hand implementation to measurement. See [Measurement](references/measurement-pixel-capi.md).
6. **Plan the test.** Write hypothesis, budget sizing math, duration, primary metric (backend verified click-through CPA or ROAS), holdout design, kill and scale rules. Append to EXPERIMENTS.md. See [Testing and scaling](references/testing-and-scaling-playbooks.md).
7. **Build the structure.** Campaign per market and objective, 3 to 8 ad groups per campaign each with one intent, 20 to 60 context hints per ad group, 3 to 5 ads per ad group, product feed campaign for catalogs. See [Campaign structure and targeting](references/campaign-structure-and-targeting.md) and [Creative and copy](references/creative-and-copy-for-conversational-ads.md).
8. **Bids and budgets.** Pick objective and strategy with the decision tree in [Bidding and budgets](references/bidding-and-budgets.md). Confirm minimum daily budget and the bid based floor.
9. **Draft change list for approval.** Everything created paused. List every object, setting and expected spend. Wait for explicit human approval before activation.
10. **Launch QA.** Ads approved, Serving status, first impressions within 24 hours, pixel events visible in the recent events endpoint, UTMs landing in GA4, session rate check after 100 clicks.
11. **Optimize weekly.** Delivery, CTR by ad group and hint style, post-click CVR, CPA vs target, creative concentration, Not serving issues, bid_too_low flags. Change one lever at a time in this order: pause losers, bids, hints, creative, platforms, budget.
12. **Decide.** At the pre-set decision point, apply kill or scale rules. Scale in steps of 20% to 30% per week while CPA holds. Require incrementality evidence before crossing the scale threshold.
13. **Cross surface review (monthly).** Check other AI surfaces' status and whether existing Google, Microsoft and Amazon campaigns already reach them. See [Other AI ad surfaces](references/other-ai-ad-surfaces.md).
14. **Log.** Journal entry for changes and results, memory only for confirmed patterns, handoffs listed at the end of the response.

## Adaptation matrix
Budget and signal tiers: Starter under $3k per month, Growth $3k to $30k, Scale $30k to $300k, Enterprise over $300k. Maturity: new (no ChatGPT Ads history), running (live under 90 days), plateau (flat CPA and volume 4+ weeks), scaling (adding budget under rules).

| Business model | Starter | Growth | Scale | Enterprise | KPI and cadence notes |
|---------------|---------|--------|-------|------------|----------------------|
| Ecommerce | Usually wait; if tested, one Clicks campaign on top 20 products at the $25 per day minimum for 4 weeks as a learning test | Product feed campaign on top revenue products plus one chat card campaign for category intents; move feed campaign to oCPC on `order_created` after 30 conversions | Feed campaigns split by margin tier using `ads_metadata` labels; carousel monitoring; geo holdout before passing 10% of paid | Multi market feeds per country, partner measurement (geo lift), Criteo or agency path for managed support | Backend ROAS and new customer share; weekly review, monthly holdout read |
| Lead gen | Only if CPL target is above $150 and a lead form converts at 10%+ on paid search; otherwise wait | Clicks campaign with one ad group per service need; `lead_created` via CAPI from the form backend; offline qualification check in CRM | oCPC on `lead_created` once 30 per month; pass lead quality to CRM; HubSpot integration if HubSpot is the CRM | Regional campaigns, sub-national geo splits for holdouts | Cost per qualified lead from CRM, not platform leads; weekly lead quality review |
| B2B SaaS | Test only problem aware intents ("how to reconcile...", "tool for..."), Clicks objective, small budget | Ad groups by job to be done; `trial_started` or `registration_completed`; LinkedIn and search comparison | oCPC on `trial_started`; pipeline attribution in CRM; Sponsored Agents waitlist if offered | Account level reporting to pipeline, partner incrementality | Cost per SQL and trial to paid rate; ChatGPT signups often low quality, verify paid conversion |
| Local services | Viable only in served markets with regional targeting; one ad group per service and city cluster; hints include service area and price cues | Region or postal targeting, call tracking via CAPI `appointment_scheduled` or `lead_created` with `action_source: phone_call` | Market by market budgets, DMA holdouts in the US | Franchise structure: campaign per region | Cost per booked job; check hours and service area in hints |
| App | CAPI only for `app_installed` and `app_opened` (no mobile SDK); use an MMP partner (AppsFlyer, Adjust and others) | Clicks on `ios_app` and `android_app` platforms vs web; oCPC on install once volume allows | Deep event optimization (`subscription_created`, `trial_started`) | Partner incrementality, SKAN not supported, IDFA not accepted | Cost per retained user or payer; click-through attribution only for app events |
| Marketplace or publisher | Two sided marketplaces: target the scarce side; publishers rarely profitable on CPC | Ad groups by category or listing type (no individual job or housing listings) | Feed campaigns for listings where allowed; hotel ads limited beta for travel | Managed partner path | Contribution margin per acquired user; policy check on listings |

| Maturity | What changes |
|----------|-------------|
| New | Eligibility gate, measurement build, learning test with fixed bids, hint style head to head, no conversion objective yet |
| Running | Weekly hint and creative rotation, bid calibration to delivery, first incrementality design, move to oCPC when event volume allows |
| Plateau | New intents and hint clusters, product feed or carousel coverage, platform split (app vs web), creative angle refresh, check frequency of the same prompts, AI text customization opt-in test |
| Scaling | 20% to 30% weekly budget steps, new markets only after home market proof, geo holdout every quarter, partner lift study at Scale and Enterprise |

## Task router
| Task | Read these references | Output template |
|------|----------------------|-----------------|
| Is ChatGPT Ads right for us? Eligibility check | [Account setup](references/account-setup-and-eligibility.md), [Policies](references/policies-and-brand-safety.md), [Benchmarks](references/benchmarks-and-case-studies.md) | Fit and eligibility memo |
| Set up account and verification | [Account setup](references/account-setup-and-eligibility.md) | Setup checklist |
| Plan and build first campaign | [Campaign structure](references/campaign-structure-and-targeting.md), [Bidding](references/bidding-and-budgets.md), [Creative](references/creative-and-copy-for-conversational-ads.md) | Launch plan and change list |
| Write context hints | [Campaign structure](references/campaign-structure-and-targeting.md) | Hint sheet per ad group |
| Write ads and choose images | [Creative](references/creative-and-copy-for-conversational-ads.md) | Ad copy sheet |
| Install pixel and CAPI, fix attribution | [Measurement](references/measurement-pixel-capi.md) | Measurement spec plus handoff to measurement |
| Product feed or carousel campaigns | [Campaign structure](references/campaign-structure-and-targeting.md), [Organic and commerce](references/organic-and-commerce-integration.md) | Feed campaign plan |
| Not serving, low delivery, rejected ads | [Policies](references/policies-and-brand-safety.md), [Bidding](references/bidding-and-budgets.md), [Tools and API](references/tools-api-mcp.md) | Diagnostic report |
| Weekly optimization and reporting | [Testing and scaling](references/testing-and-scaling-playbooks.md), [Measurement](references/measurement-pixel-capi.md) | Weekly report |
| Design test, holdout or incrementality | [Testing and scaling](references/testing-and-scaling-playbooks.md) | Test plan row plus memo |
| Full account audit | [Audit checklist](references/audit-checklist.md) | Scored audit |
| Which AI ad surface next (Google AI Mode, Copilot, Amazon) | [Other AI ad surfaces](references/other-ai-ad-surfaces.md) | Surface prioritization memo |
| Organic ChatGPT visibility vs paid, ChatGPT shopping, ACP | [Organic and commerce](references/organic-and-commerce-integration.md) | Handoff brief |
| Pull data via API or MCP, automate reporting | [Tools and API](references/tools-api-mcp.md) | Script or connector plan |
| Platform history, what changed and when | [Platform overview and timeline](references/platform-overview-and-timeline.md) | Change log entry |

## The laws
1. Eligibility before enthusiasm: legal entity country, category and served market decide everything; check them first.
2. No conversion tracking, no launch: measure from day one even on CPC, because switching to Conversions later requires a new campaign.
3. Immutable choices get a plan: objective, budget type (campaign total can become daily, not the reverse), conversion event, campaign mode and feed cannot change.
4. One intent per ad group, because context hints and ads are evaluated together and mixed intents blur relevance.
5. Hints add information the ad and landing page do not contain (what, who, when); they are not keywords, audiences or delivery instructions.
6. Test hint style (product description, situation, question, keyword) head to head before scaling; one public test found keyword style beat full questions [Unverified].
7. Write for a person mid decision: concrete offer, price or proof, no slogans; the title is short (16 to 24 characters recommended, 50 maximum).
8. Landing page continuity: send to the specific product, collection or service page that answers the conversation, never a generic home page.
9. Keep `oppref` intact through every redirect; never use `oppref`, `olref`, `obref` or `oai*` as your own parameter names.
10. Pixel plus CAPI with the same event_id, Pixel ID and event name; the first event received wins.
11. Judge on click-through, backend verified results; view-through is a 1-day reporting signal, not proof.
12. A small budget that cannot reach a decision is a learning test; label it and do not kill or scale on it.
13. New channel, new baseline: compare against the account's own history and Google Search non-brand first, public benchmarks second.
14. Change one lever at a time and wait at least 7 days or 100 clicks per ad group before judging.
15. Budget is weekly in practice: daily budgets average over 7 days and can spend 2x on a day; ads can serve up to 24 hours after a pause and that spend is billable.
16. Incrementality before scale: a geo or time holdout (or partner lift study) before ChatGPT Ads passes 10% of paid media or $30k per month.
17. Paid does not buy answers: ads do not influence ChatGPT responses and advertiser domains are cited in about 4% of ad placements [Study, 2026-08]; organic visibility is a separate workstream.
18. Respect sensitive contexts: ads never run near health, mental health, political or emotionally reliant conversations, so do not plan coverage there.
19. Consent first: default the pixel to consent false where law requires and flip only on CMP consent; disclose the pixel in the privacy policy.
20. Treat every vendor statistic as marketing until reproduced in your own data; panels disagree by 10x on ad frequency and advertiser counts.
21. Everything created paused; activation, budgets and bids need explicit human approval.

## Diagnostics
| Symptom | Likely causes | Checks | Fixes |
|---------|---------------|--------|-------|
| Status Not serving | Review pending or rejected, account verification incomplete, billing failed, brand review (logo, favicon, account name), budget exhausted, end date passed, country not allowed | Hover status reason; `include[]=serving_issues` in API; Settings > Account info; Billing | Fix the cited issue, resubmit; complete Persona verification; add valid card; upload favicon 256x256 |
| Ad rejected, crawler reasons | OAI-AdsBot blocked by robots.txt, WAF, CDN, CAPTCHA, login, 403 or 429, redirect to non-public page | robots.txt, WAF logs, curl with OAI-AdsBot user agent, adsbot.json IP ranges | Allow OAI-AdsBot and OAI-SearchBot, allowlist in Cloudflare or Akamai, upload ads in smaller batches |
| Ad rejected, policy | Category not allowed in country, unsubstantiated claims, imitation of ChatGPT UI, destination mismatch | Ad Policies, Troubleshooting onboarding and policy article | Rewrite claims, align landing page, request review if wrong |
| Zero or low impressions with Serving status | Bid too low for market, narrow hints, narrow geo or platform, small included audience, low relevance creative | `bid_too_low` (absent within 24 hours of edits), delivery by ad group, hint specificity | Raise fixed bid in 20% steps, broaden hints, add ads, remove platform limits; wait 24 hours before reporting |
| Spend shows $0 with impressions | Spend lags 7 to 8 hours | Check again next day | None; do not assume no charges |
| Overspend on a day | Daily budget is a 7-day average (2x day cap) | Weekly spend vs 7x daily | Expected; use campaign total budget for strict caps |
| High CTR, no conversions | Tracking broken, oppref lost in redirect, event not attached to campaign, consent blocking, weak landing continuity | Recent events endpoint (last 15 min), GA4 sessions vs clicks, campaign conversion setting | Attach event setting, preserve oppref, fix consent flow, align landing page |
| Platform conversions far above backend | View-through or modeled conversions counted, duplicate pixel and CAPI without shared event_id | Click-through vs view-through columns; dedup keys | Report click-through only; fix dedup |
| GA4 sessions far below clicks | In-app webview, consent rejection, redirects stripping UTMs, slow page | Session rate by platform (web vs ios_app vs android_app) | Fix redirects, speed, consent; accept some loss and model it |
| Ads on irrelevant conversations | Broad or audience style hints; system relevance mismatch (one study found 14% off topic) [Study, 2026-08] | Ask ChatGPT about your offer with test prompts on a Free account; review hints | Rewrite hints as specific needs; split ad groups; use Negative Phrases if your account qualifies |
| One ad gets all delivery | System concentrates on predicted winner | Delivery share by ad | Add distinct angles; pause only proven losers |

## Decision trees

Objective and strategy (first campaign in a market):
1. Is a standard conversion event (order_created, lead_created, trial_started, registration_completed, appointment_scheduled, subscription_created) recording through pixel or CAPI and attached to the account?
   - No: fix measurement first. If the human insists on launching, use Clicks (CPC) with a fixed max bid and attach the event for reporting.
   - Yes: go to 2.
2. Does that event have at least 30 click-through conversions in 30 days from ChatGPT Ads (or expected at the planned budget)?
   - No: Clicks objective. Start with Manual: Max bid at $3 to $5 (US) or the local equivalent, then test Maximize results in a second ad group or campaign once the fixed bid baseline CPC is known.
   - Yes: Conversions objective with click billing (oCPC). Start with Maximize results on a daily budget, or a Bid Cap equal to 1.0x to 1.2x target CPA if cost control matters more than volume.
3. Is the goal awareness or reach (launch, brand recall) with brand lift measurement available?
   - Yes: Views (CPM) with a fixed CPM bid; measure with a brand lift partner. Do not judge on CTR.
4. Is it a catalog business with a clean feed?
   - Yes: add a Product feed campaign alongside chat card campaigns. Feed campaigns support country level geo only.

Which AI surface to test next (after ChatGPT Ads or instead of it):
1. Already running Google Search with broad match or AI Max, Shopping or PMax? You are likely already eligible for ads in AI Overviews and AI Mode in supported markets. Ask google-ads to report Top ads changes and AI Max search terms; no separate buy is needed.
2. Already running Microsoft PMax, Shopping or Search with logo extensions? You are eligible for Copilot. Ask microsoft-ads to add logos and multimedia ads.
3. Selling on Amazon US with Sponsored Products or Sponsored Brands? Prompt ads in Alexa for Shopping (formerly Rufus) run on existing CPC bids; review Prompt Ad Extension reports.
4. Perplexity, Gemini app, Claude: no ad buying path as of 2026-10. Treat as organic visibility (ai-search-optimization).
5. AI ad networks inside third party AI apps: vendor claims only; test with capped budgets and strict click-through measurement.

## Quality bar (QA before any deliverable ships)
- Every platform fact has a label and a date; anything not on an OpenAI page is marked [Unverified].
- Every number names its data source, date range and timezone.
- The eligibility gate was run and passed, or the deliverable says why not.
- Measurement plan covers event list, pixel and CAPI, event_id dedup, oppref, consent and UTMs.
- Budget sizing math is shown and the test is labeled learning or decision.
- Kill and scale rules are written with numbers.
- Change list is numbered, every item needs approval, all new objects paused.
- Handoffs listed with slug and brief.

## Expensive mistakes to prevent
| Mistake | Cost | Prevention |
|---------|------|------------|
| Launching Clicks without conversion tracking, then needing a new campaign for oCPC | Lost learning, no baseline | Measure from day one; attach event settings to every campaign |
| Choosing a campaign total budget then wanting daily (or the reverse) | Rebuild | Daily for new advertisers; campaign total only for fixed flights |
| Redirects or SPA routers stripping `oppref` | Conversions not attributed, optimizer blind | Test with a synthetic oppref through every redirect path |
| Using `oppref` or `oai` prefixed names as custom URL parameters | Ad rejected (reserved parameters) | Use your own names, for example `click_ref={oppref}` via API macros |
| Firewall or bot protection blocking OAI-AdsBot | Ads rejected or Not serving | Allow user agent, check adsbot.json ranges, review WAF rules |
| Judging on platform conversions that include view-through and modeled conversions | Over crediting | Use click-through conversions reconciled to backend |
| Copying Google keyword lists into context hints | Weak relevance, off topic placements | Write need and situation hints; test styles |
| Running EEA campaigns with custom audiences or expecting personalization | No delivery uplift, compliance risk | Contextual only in EEA and Switzerland |
| Pausing at 6pm and assuming spend stopped | Up to 24 hours of billable delivery | Pause a day ahead of hard stops |
| Treating vendor CTR or new customer claims as targets | Misplaced expectations | Own baseline first; verify in CRM |

## Worked example: test sizing
A US ecommerce brand: AOV $120, contribution margin 40%, breakeven CPA $48, target CPA $40. Assume CPC $3.50 (inside OpenAI's $3 to $5 guidance) and post-click CVR 1.2% (deliberately below the brand's 2.5% Google non-brand CVR because early public tests showed much lower CVR on ChatGPT traffic [Unverified]).
- Decision test goal: 40 click-through purchases. Clicks needed = 40 / 0.012 = 3,333. Budget = 3,333 x $3.50 = $11,667 over 4 to 6 weeks (about $280 to $420 per day).
- Implied CPA at these assumptions = $3.50 / 0.012 = $292, far above $40. To break even the CVR would need $3.50 / $48 = 7.3%, or CPC would need to fall to $48 x 0.012 = $0.58. Conclusion: test only if a product feed campaign or a high AOV segment changes the math, or run a $1,500 learning test focused on CTR, session rate, CVR and new customer share before committing.

## Cadence
| Frequency | Checks |
|-----------|--------|
| Daily (5 min, during first 14 days and after changes) | Serving status, review rejections, spend pacing vs 2x day cap, pixel events arriving, billing alerts |
| Weekly | Delivery rate, CTR, CPC, post-click CVR, click-through CPA by ad group and hint style, creative concentration, session rate, new Not serving reasons, experiment status, journal entry |
| Monthly | Backend reconciliation, CPA trend vs target, hint and creative refresh, policy changelog check, Freshness Protocol, cross surface review, budget proposal to growth-orchestrator |
| Quarterly | Incrementality read (geo or time holdout, partner lift), full audit with the scored checklist, market expansion decision, memory update |

## Guardrails and approvals
- Never activate, pause, archive, change bids or budgets, upload audiences or publish ads without explicit human approval. Present a numbered change list with objects, settings, expected spend and rollback.
- Create all proposed objects paused. Archive is irreversible; recommend pause instead.
- Keep total test spend inside the budget approved in PROJECT_BRIEF.md or STRATEGY.md. If self-serve account spend limits are unavailable (card billed accounts), propose campaign total budgets with end dates.
- Never store Ads API keys or Conversions API keys in the repository, journals or outputs. CAPI calls are server side only.
- Do not upload customer lists without a documented legal basis; never use custom audiences for EEA or Swiss campaigns.
- Do not draft ads in prohibited categories or with medical, financial or legal claims unless the advertiser is approved and the market is the US.
- Never fabricate performance data, benchmarks or policy text. Cite the source and date of every number.

## Outputs
File naming: `ads-master/outputs/chatgpt-ads/YYYY-MM-DD_chatgpt-ads_<description>.md` (for example `2026-10-08_chatgpt-ads_fit-and-eligibility.md`). Never overwrite.

Required sections for every deliverable: Summary (max 5 bullets), Data used (sources, date range, timezone), Findings, Change list (numbered; object, change, reason, expected impact, confidence, approval needed), Risks and open questions, Next review date, Handoffs requested (if any).

Templates:
- Fit and eligibility memo: eligibility gate results, fit score (0 to 5 on intent fit, offer, landing continuity, measurement, budget), go or no go, test budget math.
- Launch plan: campaign table (market, objective, budget type and amount, dates, targeting), ad group table (intent, hints, bid, ads), measurement checklist, kill and scale rules.
- Weekly report: KPI table vs targets and prior week, top and bottom ad groups, actions taken, actions proposed, experiment updates.
- Scored audit: use [Audit checklist](references/audit-checklist.md) scoring.

## Freshness protocol
Check these before acting on platform behavior. Record the date checked and any change in a journal entry tagged `change`.

| Source | URL | What to verify |
|--------|-----|----------------|
| ChatGPT Ads help collection | https://help.openai.com/en/collections/20001223 | New or changed articles (setup, budgets, bidding, measurement, formats) |
| Ads Manager Availability | https://help.openai.com/en/articles/20001245-ads-manager-availability | Countries Available vs Coming Soon for advertiser legal entity |
| Ad Policies with changelog | https://openai.com/policies/ad-policies/ | Version number and changelog (v1.6 was current on 2026-09-10) |
| Ads in ChatGPT (consumer) | https://help.openai.com/en/articles/20001047-ads-in-chatgpt | Who sees ads, personalization, exclusions |
| Testing ads in ChatGPT (dated updates) | https://openai.com/index/testing-ads-in-chatgpt/ | Market launches by date |
| OpenAI Ads blog | https://ads.openai.com/blog | Measurement, formats, partner news |
| OpenAI newsroom | https://openai.com/news/ | Major ads announcements (format, markets, partners) |
| Developer docs index | https://developers.openai.com/ads/llms.txt and https://developers.openai.com/ads | API objects, enums, endpoints, Insights fields, pixel and CAPI syntax |
| Supported events | https://developers.openai.com/ads/supported-events | Event names and data shapes |
| Crawler guidance | https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers | OAI-AdsBot rules, IP ranges |
| Ads Manager in-product notices and emails | ads.openai.com | Beta changes (OpenAI emails advertisers when capabilities change) |
| Google ads in AI Overviews and AI Mode | https://support.google.com/google-ads and https://blog.google/products/ads-commerce/ | Countries, formats, eligibility |
| Microsoft ads in Copilot | https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_adsforcopilot | Eligible formats, reporting |
| Amazon Ads sponsored prompts | https://advertising.amazon.com | Prompt ad availability, markets |

How to log: one journal entry per change found (`YYYY-MM-DD_HHMM_chatgpt-ads_platform-change.md`) with what changed, source URL, date, which references are now stale, and whether live campaigns need action. Flag stale references to the human; do not edit the global skill from a project.

## Reference index
- [Platform overview and timeline](references/platform-overview-and-timeline.md): what ChatGPT Ads is, dated timeline Jan 2025 to Oct 2026, formats, how matching and the auction work, privacy model.
- [Account setup and eligibility](references/account-setup-and-eligibility.md): country availability, verification, legal entity rules, billing, roles, agencies, multi account.
- [Campaign structure and targeting](references/campaign-structure-and-targeting.md): hierarchy, naming, context hints, geo, platform, custom audiences, product feed campaigns.
- [Bidding and budgets](references/bidding-and-budgets.md): objectives, bid strategies, max bids, budgets, pacing, minimums, delivery diagnostics.
- [Creative and copy for conversational ads](references/creative-and-copy-for-conversational-ads.md): specs, copy frameworks, image rules, landing continuity, templates.
- [Measurement: pixel and CAPI](references/measurement-pixel-capi.md): data sources, events, dedup, oppref, consent, UTMs, GA4, attribution windows, reporting.
- [Policies and brand safety](references/policies-and-brand-safety.md): allowed, restricted and prohibited categories, placement exclusions, review, crawler rules, privacy.
- [Testing and scaling playbooks](references/testing-and-scaling-playbooks.md): launch, optimize, scale, recover plays, budget sizing, holdouts, kill and scale rules.
- [Other AI ad surfaces](references/other-ai-ad-surfaces.md): Google AI Overviews and AI Mode, Copilot, Amazon, Perplexity, Meta AI, Gemini, Grok, Claude, AI ad networks.
- [Organic and commerce integration](references/organic-and-commerce-integration.md): paid vs organic ChatGPT visibility, shopping results, product feeds, Instant Checkout and ACP.
- [Benchmarks and case studies](references/benchmarks-and-case-studies.md): labeled public data on CTR, CPC, CPM, ad frequency, advertiser counts, case results.
- [Tools, API and MCP](references/tools-api-mcp.md): Advertiser API, Insights, CAPI, official plugins, community MCP servers, scripts.
- [Audit checklist](references/audit-checklist.md): scored audit with severity and fixes.
- [Sources](references/sources.md): annotated source list with dates.
