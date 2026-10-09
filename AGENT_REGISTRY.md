# Agent Registry

Master list of every agent and utility skill in Ads Master. Knowledge as of 2026-10. Each agent has a subagent file (`agents/<slug>.md`), a playbook (`skills/<slug>/SKILL.md` plus `references/`) and a research dossier (`research/<slug>.md`).

## Agents

23 agents in seven groups. Each group answers one question about the business.

### Strategy and control: where do we grow, and what is true?
| Agent | Mission | Headline KPIs | Default cadence | Activate when |
|-------|---------|---------------|-----------------|---------------|
| `growth-orchestrator` | Turn the business goal into a channel mix, budget, forecast and ranked priorities, and keep the system honest with unit economics | Contribution margin after marketing, MER and aMER, nCAC, LTV to CAC, payback | Daily report, weekly review, monthly reallocation, quarterly strategy | Always |
| `measurement` | Give every agent conversion data it can trust: complete, deduplicated, consented, valued in profit terms, reconciled and calibrated | Backend capture rate, duplicate rate, CAPI coverage and match quality, consent rate, calibration coverage | Weekly health check, monthly reconciliation, quarterly test plan | Always |
| `compliance` | Every customer facing word, image, number and offer true, provable, lawful per market, policy compliant and disclosed, with a reusable claims registry | Pre-publish coverage, live blocked claims, expired evidence in live copy, policy disapproval rate | On every publish, monthly registry review | Always in practice |
| `market-intel` | An accurate, current picture of competitors, customers and demand, turned into angles, offers, keywords and prompts | Competitor coverage, intel freshness, insight adoption, AI share of voice benchmark | Monthly, quarterly landscape | Any paid channel active, or on request |

### Paid acquisition: buy the right customers at the right price
| Agent | Mission | Headline KPIs | Default cadence | Activate when |
|-------|---------|---------------|-----------------|---------------|
| `meta-ads` | Profitable, incremental revenue or pipeline from Meta via signal, structure, creative throughput and bidding | CPA or ROAS vs target, new customer share, creative throughput, signal health | Daily alerts, weekly optimization | Meta active or planned |
| `google-ads` | Maximum verifiable profit or qualified pipeline from Google Ads within targets and policies | Non-brand CPA or ROAS, POAS, zero-conversion search term spend, budget limited profitable spend | Daily alerts, weekly optimization | Google active or planned |
| `microsoft-ads` | Profitable, incremental demand capture from Microsoft Advertising with no wasted network spend | CPA or ROAS vs target, non-brand impression share, CPC ratio vs Google, network spend share | Daily alerts, weekly optimization | Search spend present, B2B or desktop heavy audience |
| `chatgpt-ads` | Make AI assistant ads an incremental, measurable channel, or prove fast and cheaply that they are not | Backend verified CPA or ROAS, incremental CPA, post-click CVR, delivery rate | Daily during tests, weekly | Test planned in STRATEGY.md, eligible market |
| `tiktok-ads` | Profitable, incremental TikTok growth through a high throughput creative and creator engine | Calibrated CPA or ROAS, GMV Max ROI vs breakeven, creative velocity and hit rate | Daily alerts, weekly optimization | TikTok active or planned, under 45 audience or TikTok Shop |
| `linkedin-ads` | Measurable qualified pipeline and target account demand at an affordable cost per opportunity | Cost per SQL, pipeline per dollar, target account reach, buying committee coverage | Weekly | B2B, deal size above about $5k |
| `mobile-app-growth` | Grow retained, paying app users within the payback target: store conversion, trustworthy measurement, efficient app campaigns, tested monetization | Net revenue per install (D7, D30), payback days, cost per payer, product page CVR, D1, D7, D30 retention | Daily alerts, weekly | iOS or Android app |

### Organic visibility: be found and be recommended
| Agent | Mission | Headline KPIs | Default cadence | Activate when |
|-------|---------|---------------|-----------------|---------------|
| `seo` | Grow qualified organic traffic and its revenue from Google and Bing while staying inside spam policies | Non-branded organic clicks, organic conversions, index coverage, Core Web Vitals pass rate | Weekly, monthly report | Website exists |
| `ai-search-optimization` | Raise accurate mention, recommendation and citation share across AI engines, proven with sound prompt tracking | Mention rate, recommendation rate, citation share, AI referral sessions and conversions | Monthly report, weekly when a program runs | Website exists |

### Conversion and storefront: turn visits into orders
| Agent | Mission | Headline KPIs | Default cadence | Activate when |
|-------|---------|---------------|-----------------|---------------|
| `storefront-ux` | Raise revenue per visitor and order completion across every storefront template with proven patterns shipped as reviewed code, routing uncertain ideas to tests | Conformance score, PLP to PDP rate, PDP add to cart rate, cart to checkout rate, search health, accessibility defects | Monthly audit, on storefront changes | Ecommerce storefront |
| `cro` | Raise conversion value per visitor through research, better pages and offers, and valid experiments | Value per visitor, CVR by step and source, lead quality, Core Web Vitals on top landing pages | Weekly | Website with paid or organic traffic |
| `site-engineer` | Release every site change and ad destination with evidence it works on desktop, phones and in-app browsers, tracks correctly and can be rolled back | Change failure rate, time to restore, launch QA coverage, destination health, money path test pass rate | On every release and launch | Site in a repo or a theme the team changes |

### Offer and commerce: what exactly do we sell, and where?
| Agent | Mission | Headline KPIs | Default cadence | Activate when |
|-------|---------|---------------|-----------------|---------------|
| `offer-strategy` | Offers that raise contribution after marketing and win customers worth keeping, without breaking pricing law or channel relationships | Contribution per order by offer, acquisition investment per new customer, discount rate, promo dependency | Monthly, before promos | Ecommerce, subscriptions or a meaningful offer decision |
| `pricing-strategy` | Prices that maximize contribution at a defensible position: level, architecture, basket and delivery policy, corridors per channel, with a cost model that is never computed on missing inputs | Contribution per order and per basket band, price index vs competitors, price realization, free delivery threshold economics | Monthly price watch, quarterly price review, before any price change | Any decision on what to charge, new product or market, cost shock |
| `marketplaces` | Profitable marketplace growth with listings, retail media and the Featured Offer, without breaking price parity or account health | Contribution per marketplace after fees and ads, TACoS, Featured Offer share, account health, stock cover | Weekly | Selling or planning to sell on any marketplace |
| `commerce-feeds` | Every sellable product approved, accurate, findable and profit segmented on every shopping surface, agentic commerce ready | Approval rate, disapproved revenue share, feed to site parity, identifier coverage | Weekly diagnostics | Product catalog |

### Creative: what we show
| Agent | Mission | Headline KPIs | Default cadence | Activate when |
|-------|---------|---------------|-----------------|---------------|
| `creative-strategy` | A steady flow of genuinely different, research backed concepts and data driven scale, iterate or kill calls | Concept hit rate, distinct concepts live, refresh velocity, CPA or ROAS by concept | Weekly | Any paid social or video channel active |
| `video-studio` | Finished, honest, platform native video ad files and variants that every channel accepts, so creative output never limits growth | Brief to delivery time, first pass QA rate, platform rejection rate, iteration win rate, generation spend vs cap | Weekly production batch | Video placements active or planned |

### Retention: keep the customers we paid for
| Agent | Mission | Headline KPIs | Default cadence | Activate when |
|-------|---------|---------------|-----------------|---------------|
| `lifecycle-crm` | Raise repeat purchase and 12 month contribution LTV through consented, deliverable, measured lifecycle messaging, and feed retention truth back to acquisition | Repeat rate at 30, 45, 60, 90 days, incremental lifecycle contribution, deliverability, net list growth | Weekly | Customers or subscribers with consent |

## Utility skills

| Skill | What it does | Invoke |
|-------|--------------|--------|
| `ads-setup` | Creates `ads-master/` from the template, scans the codebase, interviews the human, activates agents, links CLAUDE.md | `/ads-setup` (plugin: `/ads-master:ads-setup`) |
| `ads-review` | Runs the heartbeat: daily report with the alert queue, weekly learning loop, monthly reallocation, quarterly reset | `/ads-review weekly` (plugin: `/ads-master:ads-review weekly`) |
| `ads-verify` | Turns Unverified and Contested claims into project facts via the evidence ladder and `VERIFIED.md` | `/ads-verify <claim or package>` |

## Most common handoffs

| From | To | Typical reason |
|------|----|----------------|
| Any channel agent | measurement | Conversions missing, duplicated or not matching the backend; lift test design |
| meta-ads, tiktok-ads, google-ads (video), linkedin-ads, chatgpt-ads | creative-strategy | Fatigue, low concept diversity, new briefs needed |
| Any channel agent | cro | Clicks are fine, conversion rate is not |
| google-ads, meta-ads, microsoft-ads, tiktok-ads, chatgpt-ads | commerce-feeds | Disapprovals, catalog errors, custom labels for profit bidding |
| seo | ai-search-optimization | AI Overviews and assistant visibility work |
| chatgpt-ads | ai-search-optimization, commerce-feeds | Organic AI visibility, ChatGPT shopping feeds |
| Any agent producing customer facing copy | compliance | Claims, pricing display, disclosure before publishing |
| creative-strategy, channel agents | video-studio | Briefs to produce, resizes, cut downs, re-deliveries after rejections |
| cro, seo, measurement, storefront-ux | site-engineer | Preview, QA, release and rollback of site and tracking changes |
| cro, commerce-feeds | storefront-ux | Table stakes storefront fixes and component builds |
| Channel agents, cro, commerce-feeds | offer-strategy | Offer, bundle, promo and price decisions with full economics |
| measurement, meta-ads, linkedin-ads | lifecycle-crm | Consent, suppression, customer audiences, LTV values |
| google-ads, meta-ads, tiktok-ads, measurement | mobile-app-growth | App campaigns, MMP, SKAN and AdAttributionKit |
| offer-strategy, growth-orchestrator, market-intel | pricing-strategy | Price level, price architecture, basket and delivery thresholds, price changes |
| pricing-strategy | offer-strategy | Incentive mechanics and promo calendar on top of the base price |
| Channel agents, commerce-feeds, pricing-strategy | marketplaces | Marketplace listings, retail media, fees and price parity |
| Any agent | market-intel | Competitor offers, ads, rankings, pricing |
| Any agent | growth-orchestrator | Budget across channels, priorities, forecasts |

## Status

| Version | Date | Notes |
|---------|------|-------|
| 1.2.0 | 2026-10-09 | pricing-strategy and marketplaces agents, ads-verify skill and evidence ladder, living HOW_TO_USE guide with packs, model routing, Workflow Kit plugin (routing agents, parallel sessions, prompts, handover, decision log, guardians, git hooks, gate scripts), tracking plan as code, metric additivity, alert queue, nested subagents disabled by design. |
| 1.1.0 | 2026-10-09 | Seven new agents (compliance, video-studio, site-engineer, storefront-ux, offer-strategy, lifecycle-crm, mobile-app-growth), deterministic guardrail hooks with automation stages, daily report, SEO preflight, unified metrics, claims registry, decision log and incident runbook. |
| 1.0.0 | 2026-10-08 | First release. 14 agents, 16 skills. Research sweep plus a second live verification pass on every package (about 470 live searches in total). |
