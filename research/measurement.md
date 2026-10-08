# Research Dossier: Measurement (tracking, attribution, incrementality, MMM)

> Compiled 2026-10-08 for the Ads Master `measurement` agent. Evidence labels follow docs/AUTHORING_SPEC.md section 7.

## Research method and limitations

- 14 web searches were run (several in extended mode) across Google Analytics, Tag Manager, Google Ads, Meta, TCF, KVKK, EU Digital Omnibus and Privacy Sandbox topics before the session's shared search budget was exhausted. Direct page fetching (WebFetch and curl) was blocked in this environment, so findings rely on search result extracts that quote official pages, plus prior knowledge up to mid 2026.
- Two research notes from sibling builders in the same session (Microsoft Ads and ChatGPT Ads, both built from search extracts) were used for Microsoft UET and ChatGPT Ads measurement details and are cited as such.
- Items that could not be confirmed against a primary source carry [Unverified] or "verify" in the skill. The Freshness Protocol in SKILL.md lists the pages to check before acting.
- Not covered by fresh searches this session (prior knowledge only, labeled in the skill): TikTok, LinkedIn, Pinterest, Snap and Reddit CAPI field details; Microsoft UET Conversions API status; Safari 26 privacy changes; US state law list beyond widely known effective dates; AdAttributionKit iOS 26 additions; Meta incremental attribution; vendor pricing.

## 1. Executive summary

1. Chrome kept third-party cookies. Google confirmed in April 2025 it would not launch a new cookie choice prompt, then announced on 2025-10-17 the retirement of most Privacy Sandbox APIs (Topics, Protected Audience, Attribution Reporting, Private Aggregation, Shared Storage, IP Protection, Related Website Sets and others), with deprecation from Chrome 144 (January 2026) and removal targeted for Chrome 150 (July 2026). Measurement roadmaps built on Attribution Reporting API are dead; consent, first-party data and server-side events are what matter [Official, 2025-10].
2. Meta changed attribution twice in 2026: 7-day view and 28-day view windows were removed from the Ads Insights API on 2026-01-12 (queries return empty data, not errors), and from March 2026 click-through only counts link clicks while likes, shares, saves and comments moved to a new 1-day "engage-through" category. Reported conversions dropped with no change in real performance; dashboards and targets need rebaselining [Official plus secondary, 2026].
3. Google moved offline conversion imports and enhanced conversions for leads uploads from the Google Ads API to the Data Manager API from 2026-06-15; new users of session attributes and IP data in Google Ads API imports were blocked from 2026-02-02. Silent upload failures after June 2026 are a top audit item [Official, 2026].
4. Google is merging enhanced conversions for web and for leads into one setting during 2026 and recommends the Data Manager API for new server-to-server integrations, while keeping the GA4 Measurement Protocol supported [Official, 2025 to 2026].
5. GA4 added an AI Assistant channel to the Default Channel Group on 2026-05-13 (medium ai-assistant), not retroactive and blind to referrer-less app traffic; a custom channel group is still needed for history and full coverage [Official plus secondary, 2026-05].
6. Google Ads Conversion Lift became accessible to far smaller advertisers: $5,000 minimum budget and at least 1,000 observed conversions, with Search and Performance Max now self-serve and feasibility ratings shown before launch [Official help page; announcement date contested between 2025-05 and 2025-11].
7. Google tag gateway for advertisers (renamed from first-party mode in May 2025) serves Google tags from the advertiser's domain via Cloudflare (free, one click) and, since 2026-06-01, Google Cloud load balancers (GA). It does not bypass consent or reliably bypass ad blockers, and can disturb CMP load order [Official, 2025 to 2026].
8. Consent infrastructure tightened: IAB TCF v2.3 became mandatory for TC strings created from 2026-03-01 (disclosedVendors segment), and Google may serve Limited Ads on non-compliant requests. The EU Digital Omnibus cookie reform (browser signal consent, cookies into GDPR) remains a proposal as of 2026-10-08 with the Council split and the browser signal article removed in a June Council text [Official and press, 2026].
9. Turkey's KVKK cross-border regime (Law No. 7499, in force 2024-06-01; consent fallback ended 2024-09-01) requires standard contracts notified within 5 business days, with 2026 fines of roughly TRY 90k to 1.8m for notification failures and no adequacy decisions as of August 2026. Ad pixels and CAPIs that send personal data abroad fall under it [Official and law firm summaries, 2024 to 2026].
10. ChatGPT Ads launched pixel and Conversions API with its self-serve Ads Manager beta around 2026-05-05 (event ID dedup, oppref click parameter, standard events for optimization, 30-day click window recommended), and expanded to 60+ countries by late September 2026: measurement teams must add it to click ID capture, CAPI senders and channel groups [Secondary, 2026].

## 2. State of measurement in 2026 (with numbers)

| Area | State | Numbers and source |
|------|-------|--------------------|
| Browser signal loss | Third-party cookies remain in Chrome; Safari and Firefox restrict tracking; ad blockers persist | Topics API was used on about 13% of page loads at retirement (Google intent thread, 2025) [Official, 2025-10]; site-specific loss must be measured against backend |
| Consent | Opt-in regimes (EEA, UK, CH, TR) shape GA4 and Google Ads modeling | GA4 behavioral modeling needs 1,000 denied events per day for 7 days and 1,000 granted daily users for 7 of 28 days [Official, long standing]; Google Ads conversion modeling cited at 700 ad clicks over 7 days per country and domain grouping [Official, verify] |
| Platform attribution | Narrower, more conservative windows at Meta; GA4 adds impression-inclusive and per-conversion attribution | Meta: secondary sources report 15% to 40% lower reported conversions after 2026-01-12 for view-heavy accounts [Secondary, unaudited] |
| Server-side | CAPIs standard on Meta, Google, TikTok, LinkedIn, Pinterest, Snap, Reddit; ChatGPT Ads added in 2026; Microsoft UET Conversions API in pilot or rollout | Google offline uploads moved to Data Manager API 2026-06-15 [Official] |
| Incrementality | Self-serve lift more accessible | Google user-based lift: $5,000 and 1,000 conversions; High feasibility 60% to 90% chance of conclusive results, Low 0% to 30% [Official] |
| MMM | Open-source Bayesian MMM mainstream (Meridian GA January 2025, Robyn, PyMC-Marketing) | Data rule of thumb 2 years weekly [Practitioner consensus] |
| Privacy law | US state patchwork growing; EU reform stalled; KVKK enforcement on transfers | About 19 US states with comprehensive laws in force by January 2026 [Practitioner consensus, verify]; Digital Omnibus 1,750+ committee amendments by 2026-07-15 [Press, 2026] |

### 2a. Server-side and conversion API landscape (October 2026)

| Platform | Server route | Dedup | Key match keys | Status notes | Label |
|----------|-------------|-------|----------------|--------------|-------|
| Meta | Conversions API, CAPI Gateway, Signals Gateway, partner apps | event_id plus event_name, 48 hours | em, ph, external_id, fbc, fbp, IP, UA | EMQ per event; sensitive category restrictions since 2025; attribution changes 2026 | [Official] |
| Google Ads | Enhanced conversions (tag), Data Manager UI and API, legacy Google Ads API for allowlisted tokens | order_id per conversion action | Hashed email, phone, address; gclid, gbraid, wbraid | Uploads moved to Data Manager API from 2026-06-15; web and leads settings combined in 2026 | [Official] |
| GA4 | Measurement Protocol (EU endpoint available), sGTM | transaction_id (prevent at source) | client_id, session_id, user_id | Data Manager recommended for new server-to-server integrations into Google Ads | [Official] |
| TikTok | Events API (v1.3), Events API Gateway, partner apps | event_id | email, phone (E.164 before hashing), external_id, ttclid, ttp | Check version sunset dates | [Official, verify] |
| LinkedIn | Conversions API (versioned headers), CRM integrations | eventId | SHA256 email, li_fat_id, name and company | B2B pipeline loops | [Official, verify] |
| Microsoft | UET with enhanced conversions, offline import by MSCLKID, Conversions API | Varies | Hashed email and phone, msclkid | Conversions API in pilot or rollout as of 2026-10; consent mode required for EEA, UK, CH | [Official via microsoft-ads notes; Unverified details] |
| Pinterest | Conversions API v5 | event_id | em, ph, epik, IP, UA | | [Official, verify] |
| Snap | Conversions API v3 | event_id | em, ph, ScCid, _scid, IP, UA | | [Official, verify] |
| Reddit | Conversions API (Ads API) | conversion_id | rdt_cid, email, IP, UA, _rdt_uuid | v3 API paths introduced | [Official, verify] |
| ChatGPT Ads | Pixel plus CAPI, Shopify app, MMPs | event ID, first event wins | oppref click parameter, hashed form data | Launched with self-serve beta around 2026-05-05 | [Secondary, Unverified details] |

### 2b. Consent and privacy landscape by region (October 2026)

| Region | Regime | Practical default for tags | Open items |
|--------|--------|----------------------------|-----------|
| EEA | GDPR plus ePrivacy national laws; DMA for gatekeepers; Google EU user consent policy | Opt-in: consent mode v2 defaults denied, certified CMP, TCF v2.3 if TCF is used | Digital Omnibus outcome |
| UK | UK GDPR plus PECR; Data (Use and Access) Act 2025 | Opt-in for advertising; analytics exemption once in force and guided by ICO | Commencement and ICO guidance |
| Switzerland | revFADP | Treat as opt-in for Google ad products (EU user consent policy covers CH) | |
| Turkey | KVKK; cookie guideline; Article 9 transfer regime (Law 7499) | Opt-in for non-essential cookies; transfer safeguards for vendors abroad | Adequacy decisions; vendor standard contracts |
| United States | About 19 state comprehensive laws; GPC honoring in many; sector rules (health) and litigation (CIPA, VPPA) | Notice plus opt-out, GPC honored, restricted processing for opted-out users; no pixels on sensitive health pages | New state laws, California browser signal law |
| Rest of world | Varies (Brazil LGPD, India DPDP rules phasing in, others) | Follow CMP region rules; counsel review for large markets | Track per project |

## 3. Timeline of changes, January 2025 to October 2026

| Date | Change | Impact on measurement | Label |
|------|--------|----------------------|-------|
| 2025-01 | KVKK publishes cross-border transfer guideline | Clarifies Article 9 mechanisms | [Law firm summary] |
| 2025-01 | Google Meridian generally available | Open-source Bayesian MMM with geo hierarchy and experiment priors | [Official, prior knowledge] |
| 2025-03-19 | GTM first-party mode via Cloudflare (beta) | First-party serving of Google tags | [Official, GTM release notes] |
| 2025-04 | Google says Chrome will not add a new third-party cookie prompt | No cookieless cliff | [Official] |
| 2025-04 | European Commission fines Meta EUR 200m under the DMA (pay or consent) | Consent models for ads under scrutiny | [Official, prior knowledge] |
| 2025-05 | First-party mode renamed Google tag gateway for advertisers; Cloudflare one-click integration (2025-05-08) | Low effort first-party Google tags | [Official] |
| 2025-05 | Google Marketing Live: cross-channel reporting, third-party cost import (Meta, TikTok, Snap, Reddit, Pinterest), impression-inclusive multi-touch attribution previewed; lower incrementality thresholds reported | Cross-channel views in GA4 | [Official; lift threshold date contested] |
| 2025-05 to 2025-06 | GA4 Measurement Protocol EU endpoints, geographic, device and user_agent fields | Better server-side GA4 events | [Official, MP changelog] |
| 2025-06 | UK Data (Use and Access) Act receives Royal Assent | Future analytics cookie exemption, higher PECR fines | [Official, prior knowledge; commencement verify] |
| 2025-06-30 | GTM serves scripts through the web container | Container serving change | [Official] |
| 2025-08-01 | GTM template API readAnalyticsStorage | Templates can read client and session IDs | [Official] |
| 2025-08-28 | Shopify Plus deadline for Thank you and Order status page upgrade | Additional scripts tracking ends for Plus | [Official, verify] |
| 2025-09 | CM360 splits Floodlight into web and app streams for new GA properties | Floodlight users | [Official] |
| 2025-10-17 | Google announces retirement of most Privacy Sandbox APIs | Stop investing in Attribution Reporting API | [Official] |
| 2025-11 | European Commission proposes Digital Omnibus (cookies into GDPR Article 88a, browser signals Article 88b) | Possible future change to banners | [Official] |
| 2025-11-11 | Google lowers lift test minimum to $5,000 (one report; another ties it to May 2025) | Lift tests for mid-size advertisers | [Contested date] |
| 2025-12 | Data Manager API launch reported (2025-12-09) | One endpoint for conversions, leads, audiences | [Secondary] |
| 2025-12-11 | GTM built-in Client ID, Session ID, Session Number variables; MP accepts in_app_purchase for app streams | Easier stitching of server events | [Official] |
| 2026-01-01 | Indiana, Kentucky, Rhode Island privacy laws effective | More US opt-out obligations | [Practitioner consensus, verify] |
| 2026-01-05 | Google tag gateway on Google Cloud load balancer (beta) | Non-Cloudflare option | [Official] |
| 2026-01 | Chrome 144 begins Privacy Sandbox API deprecation | | [Official] |
| 2026-01-12 | Meta removes 7-day and 28-day view windows from Ads Insights API | Empty data in old queries; lower reported conversions | [Secondary, multiple] |
| 2026-01-16 | GA4: cross-channel budgeting announced, attribution settings per conversion, conversion attribution analysis report (beta); OpenAI announces ad testing in ChatGPT | New GA4 planning features; new ad surface | [Official] |
| 2026-02-02 | Google Ads API stops onboarding new session attributes and IP users for imports | Use Data Manager | [Official] |
| 2026-02-09 | ChatGPT ads test begins for US logged-in adult Free and Go users | | [Secondary via chatgpt-ads notes] |
| 2026-02-10 | GA4 cross-channel budgeting (beta) | | [Official] |
| 2026-03-01 | TCF v2.3 mandatory for new TC strings; Google may fall back to Limited Ads | CMP updates required | [Official] |
| 2026-03-03 | Meta: click-through limited to link clicks; engage-through category (1 day) | Reporting break | [Official, Meta business news; details secondary] |
| 2026-04 | Google begins combining enhanced conversions for web and leads into one setting | Settings migration | [Official] |
| 2026-04-29 | GA4 Task Assistant | Built-in configuration recommendations | [Secondary mirror of Google notes] |
| 2026-05-05 | ChatGPT Ads Manager self-serve beta with pixel and CAPI | New CAPI to implement | [Secondary via chatgpt-ads notes] |
| 2026-05-13 | GA4 AI Assistant default channel | AI referral reporting | [Official plus secondary] |
| 2026-05 | Microsoft Ads data-driven attribution rolling out to all accounts | Attribution model change | [Official via microsoft-ads notes] |
| 2026-06-01 | Google tag gateway on Google Cloud generally available | | [Official] |
| 2026-06-05 | ChatGPT conversion-optimized campaigns first wave | Pixel or CAPI needed | [Secondary] |
| 2026-06-15 | Offline conversion imports and enhanced conversions for leads uploads moved to Data Manager API | Legacy uploads blocked unless allowlisted | [Official] |
| 2026-06-18 | Council text reportedly removes Digital Omnibus Article 88b (browser signals) | Banners stay | [Press, noyb] |
| 2026-07 | Chrome 150 removal target for Privacy Sandbox APIs | | [Official; completion verify] |
| 2026-07 | KVKK announcement on standard contract execution formalities | Contract signing and translations | [Law firm summary] |
| 2026-08-26 | Shopify non-Plus deadline for Thank you and Order status page upgrade | Additional scripts tracking ends | [Official, verify] |
| 2026-08 to 2026-09 | ChatGPT Ads serving in 31 European markets (2026-08-24), India and MENA, Turkey and Gulf (2026-09-16), Southeast Asia (late September) | Consent and CAPI in more regions | [Secondary] |
| 2026-09-08 | Microsoft PMax uplift experiments generally available | New lift option | [Official via microsoft-ads notes] |
| 2026-09-09 | GA4 Dashboards | In-product KPI views | [Official] |
| 2026-09-29 | GA4 improved app conversion management for Google Ads customers | App advertisers | [Official] |
| 2026-10-11 | Coreper vote on Digital Omnibus (postponed from 2026-10-07) | Watch outcome | [Press] |

## 4. Best practice consensus

1. Reconcile to backend first; treat platform and GA4 numbers as estimates [Practitioner consensus].
2. Send browser and server events with a shared event_id for dedup on every platform that supports CAPI [Official, Meta and others].
3. Consent defaults before any tag; CMP update on choice and on load; all four consent mode v2 parameters [Official, Google].
4. Capture click IDs on landing and persist them into the CRM; upload qualified stages, not raw leads [Official, Google; Practitioner consensus].
5. Normalize then SHA-256 hash personal data per platform rules; never hash IP, user agent or click IDs [Official].
6. Optimize to the deepest event with enough volume; document proxy events [Practitioner consensus].
7. Use profit or contribution values when margins vary; keep margins server-side [Practitioner consensus].
8. Use blended metrics (MER, aMER, nCAC, CM3) for business health, platform metrics for in-platform optimization [Practitioner consensus].
9. Calibrate attribution with incrementality tests; refresh every 6 to 12 months [Practitioner consensus].
10. MMM only with roughly 2 years of weekly data, spend variation and at least one experiment for calibration [Practitioner consensus].
11. BigQuery export from day one at Growth tier, because GA4 has no backfill and short retention by default [Official].
12. Annotate every tracking and attribution change [Practitioner consensus].

## 5. Contested topics

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Consent mode advanced vs basic | Advanced gives modeling and cookieless pings that recover measurement | Some DPAs and counsel see any pre-consent network request as non-compliant | Counsel decides; default to advanced only with sign off |
| Google tag gateway as ad blocker workaround | First-party path improves collection | Blockers can still match; consent unchanged; CMP load order issues | Use for resilience, not as a blocker bypass claim |
| sGTM value for small sites | Longer cookies, control, fewer scripts | Cost and ops; native integrations already send CAPI | Starter and most Growth: native apps; Scale: sGTM |
| MTA vendors | Consistent cross-platform rules, first-party pixels | Cannot see impressions, click bias, black box incrementality claims | Use as a lens; never sole budget input |
| Meta 28-day click availability after 2026 | Available for reporting via API in some accounts | Removed from standard UI | Verify per account |
| Explicit consent as KVKK transfer basis for ad tech | Many sites still rely on cookie consent | Post 2024-09-01 it is only for occasional transfers; regular transfers need safeguards | Flag to counsel; keep transfer register |
| Lift threshold date (Google $5,000) | Announced at GML May 2025 | Announced 2025-11-11 | Irrelevant to action; check help page |
| Platform lift tests | Randomized and easy | Platform defines conversions and grades itself | Prefer backend KPIs and geo tests for big decisions |

## 6. What top operators do differently

1. They write the conversion contract (definitions, dedup keys, values, consent behavior) before touching tags, and every agent and vendor works from it.
2. They reconcile weekly to the backend and track platform-to-backend ratios as a time series; a ratio change triggers investigation before any budget decision.
3. They send profit or predicted LTV values, not revenue, once margins or retention vary, and translate bid targets on the same day.
4. They run a standing test calendar (one major channel test per quarter, always-on holdouts for retargeting and CRM audiences) and keep incrementality factors in reporting.
5. They treat measurement as software: version control, staging environments, release notes, monitoring, incident reports.
6. They capture every click ID, including new ones (oppref for ChatGPT Ads), and close the loop with daily offline uploads under 24 hours.
7. They separate reporting of click-through, view-through and engage-through, and rebaseline immediately after platform definition changes.
8. They measure their own signal loss (by browser, region, payment method) and invest in server-side only where the measured loss justifies it.
9. They keep legal posture explicit (region-specific consent defaults, transfer registers for KVKK and GDPR, GPC handling) and avoid sensitive data entirely in ad platforms.
10. They use MMM response curves and marginal ROI, not average ROAS, for allocation, and move budgets in capped steps verified by tests.

## 7. Common expensive mistakes

| Mistake | Cost | Prevention |
|---------|------|-----------|
| Double counting (two GA4 configs, pixel plus CAPI without event_id, GA4 and Ads tag both primary) | Bidding overpays; false ROAS | Dedup keys, single primary |
| Silent upload failures (Google Ads API path blocked from 2026-06-15) | Lead gen bidding loses quality signal for weeks | Upload monitoring, Data Manager migration |
| Late consent default or missing ad_user_data and ad_personalization | EEA remarketing and measurement loss, compliance risk | Consent Initialization trigger, QA matrix |
| Dashboards still querying removed Meta windows | Empty columns read as zero performance | Update connectors after 2026-01-12 |
| Payment gateway self-referrals | Purchases credited to PayPal or Stripe | Unwanted referrals |
| Optimizing lead gen to raw form fills | Spam and low quality leads scale | Offline qualified stages |
| Switching to profit values without lowering tROAS | Spend collapses | Target translation |
| Shopify migration without pixel rebuild | Missing purchases after Thank you page upgrade | Customer events plan before deadlines |
| Underpowered lift tests read as "no effect" | Cutting incremental channels | Power analysis, MDE reporting |
| PII in URLs and GA4 | Policy violations, data deletion requests | Redaction, POST forms |

## 8. Benchmarks

Benchmarks vary by vertical, geo, season and setup. Compare the project to its own history first.

| Benchmark | Value | Source and date | Sample and caveat |
|-----------|-------|-----------------|-------------------|
| Meta reported conversion change after view window removal | 15% to 40% lower for affected accounts | Agency and vendor blogs, 2026-01 to 2026-03 | Unaudited, view-heavy accounts; not a performance change |
| Meta reported change after March 2026 click redefinition | One source cites 40% to 60% lower click-through conversions | Vendor blog, 2026-03 | Single source outlier [Unverified] |
| Google Conversion Lift feasibility | High: 60% to 90% chance of conclusive result; Low: 0% to 30% | Google Ads Help via PPC Land, 2025 | Google's own rating system |
| Google Conversion Lift minimums | $5,000 budget, 1,000 observed conversions | Google Ads Help, 2025 to 2026 | Availability varies by account |
| Topics API usage at retirement | About 13% of page loads | Google Chromium intent thread, 2025 | Shows low adoption |
| GA4 behavioral modeling thresholds | 1,000 denied events per day for 7 days; 1,000 granted daily users for 7 of 28 days | Google Analytics Help | Eligibility, not accuracy |
| Meta learning phase | About 50 optimization events per ad set per 7 days | Meta Business Help | Guideline |
| KVKK fine for missing standard contract notification (2026) | About TRY 90,308 to 1.8 million | Law firm summaries, 2026 | Upper figure differs by source |
| Small business lift detectability | Effects under 10% to 20% often not detectable even with multi-week tests | Secondary analysis, 2025 to 2026 | Depends on volume and noise |
| Digital Omnibus committee amendments | More than 1,750 by 2026-07-15 (another source: 1,840) | Praxikon, EU Perspectives, 2026 | Process indicator |

## 9. Tools, APIs and MCP servers

| Tool | Type | Use | Label |
|------|------|-----|-------|
| Google Analytics MCP server | Official, read-only | GA4 reports and admin reads from Claude | [Official, 2025] |
| Google Ads MCP server | Official, read-only | GAQL queries on conversion actions and stats | [Official, 2025; verify] |
| MCP Toolbox for Databases | Official open source | BigQuery queries | [Official] |
| Shopify Dev MCP | Official | Web Pixels and webhook docs and schemas | [Official] |
| GA4 Data API and Admin API | Official APIs | Reports, settings audits | [Official] |
| Measurement Protocol | Official API | Server events into GA4 | [Official] |
| Data Manager API | Official API | Offline conversions, leads, audiences | [Official, 2025 to 2026] |
| Tag Manager API v2 | Official API | Container exports and diffs | [Official] |
| Meta Marketing API and CAPI, CAPI Gateway, Signals Gateway | Official | Insights and server events | [Official] |
| TikTok Events API and Gateway | Official | Server events | [Official] |
| LinkedIn Conversions API | Official | B2B server events | [Official] |
| Pinterest, Snap, Reddit CAPIs | Official | Server events | [Official] |
| OpenAI ChatGPT Ads pixel and CAPI | Official | Server events for ChatGPT Ads | [Secondary, 2026] |
| Stape and other sGTM hosts | Commercial | Managed server-side tagging | [Practitioner consensus] |
| GeoLift, CausalImpact, Trimmed Match | Open source | Geo experiments | [Official open source] |
| Meridian, Robyn, PyMC-Marketing | Open source | MMM | [Official open source] |
| Haus, Measured, Recast, Lifesight | Commercial | Incrementality and MMM | [Vendor claims] |
| Community GTM, Meta, TikTok MCP servers | Community | Read and write via APIs | [Unverified; review code] |

## 10. Official sources to monitor

| Source | What to watch |
|--------|---------------|
| Google Analytics What's new and Announcements | Channels, attribution, consent, API changes |
| Measurement Protocol changelog | Fields and endpoints |
| Tag Manager release notes | Gateway, consent, template APIs |
| Google Ads Help: enhanced conversions, offline imports, Conversion Lift | Settings migration, thresholds |
| Google Ads API and Data Manager API release notes | Upload paths, deprecations |
| Meta business news and Conversions API changelog | Attribution, parameters, restrictions |
| TikTok Business API changelog | Events API versions |
| LinkedIn Marketing API versioning page | Version sunsets |
| Microsoft Advertising blog and UET docs | Consent, Conversions API, attribution |
| OpenAI Ads help center and ad policies | Pixel, CAPI, regions |
| IAB Europe TCF pages | Version requirements |
| EDPB, ICO, CNIL, CPPA, state AGs | Enforcement and guidance |
| kvkk.gov.tr | Transfer rules, adequacy, fines |
| EU legislative trackers for Digital Omnibus | Council and Parliament positions |
| Chrome release notes and Privacy Sandbox status | API removals |
| WebKit blog | ITP and link tracking protection |
| Shopify changelog and shopify.dev | Pixels, checkout deadlines |
| Apple developer news | AdAttributionKit and SKAdNetwork |
| GitHub releases: Meridian, Robyn, PyMC-Marketing, GeoLift, google-analytics-mcp, google-ads-mcp | API changes |

## 11. Open questions and watch list

1. Digital Omnibus: Coreper vote on 2026-10-11 and Parliament committee vote; whether cookie rules move into GDPR and whether any browser signal mechanism survives.
2. Chrome 150 removal: confirm whether all retired Privacy Sandbox APIs are gone and whether anything replaces Attribution Reporting for cross-site measurement.
3. Google Data Manager API: allowlist status for legacy Google Ads API uploads after 2026-06-15; next API versions; consent field requirements.
4. GA4 AI Assistant channel: the official list of recognized assistants (Perplexity status), whether tagged paid AI clicks (ChatGPT Ads) are overwritten into AI Assistant, and whether it reaches user acquisition reports.
5. Meta: future attribution changes (incremental attribution adoption, 28-day click status) and parameter restrictions for sensitive categories.
6. Microsoft UET Conversions API general availability and consent enforcement details.
7. ChatGPT Ads measurement: official CAPI endpoint documentation, attribution window defaults, MMP and partner integrations, EEA consent handling.
8. UK DUAA commencement for the analytics cookie exemption and ICO final guidance.
9. KVKK: first adequacy decisions; vendor availability of KVKK standard contracts for ad platforms.
10. US: new state laws effective 2027 and California browser opt-out signal requirement.
11. Safari and iOS 26 privacy changes affecting click IDs and fingerprinting protection in normal browsing.
12. Google impression-inclusive multi-touch attribution in GA4: global rollout and how it changes GA4 versus platform comparisons.

## 12. Sources

1. Google is retiring Privacy Sandbox, BetaNews, https://betanews.com/2025/10/20/google-is-retiring-privacy-sandbox/, 2025-10-20
2. Google's Privacy Sandbox Is Officially Dead, Adweek, https://www.adweek.com/media/googles-privacy-sandbox-is-officially-dead/, 2025-10
3. Google's Privacy Sandbox elimination ends the quest for a cookieless Chrome, eMarketer, https://www.emarketer.com/content/google-s-privacy-sandbox-elimination-ends-quest-cookieless-chrome, 2025-10
4. Google Privacy Sandbox officially shuts down, Usercentrics, https://usercentrics.com/knowledge-hub/what-is-google-privacy-sandbox/, 2025 to 2026
5. Google Retires Privacy Sandbox APIs, Keeps Third-Party Cookies in Chrome, Windows Report, https://windowsreport.com/google-is-scrapping-privacy-sandbox-apis-as-chrome-keeps-third-party-cookies-after-all/, 2025-10
6. Privacy Sandbox, Wikipedia, https://en.wikipedia.org/wiki/Privacy_Sandbox, accessed 2026-10
7. Simplifying Ad Measurement for a Social-First World, Meta for Business, https://www.facebook.com/business/news/click-attribution, 2026-03
8. Meta Ads Attribution Window Removed (2026 Fix), Dataslayer, https://www.dataslayer.ai/blog/meta-ads-attribution-window-removed-january-2026, 2026
9. Meta Killed Its 28-Day View Attribution Window on January 12, 2026, Seresa, https://seresa.io/blog/attribution-measurement/meta-killed-its-28-day-view-attribution-window-on-january-12-2026, 2026
10. Meta Attribution 2026: 1-Day vs 7-Day (Jan 12 Update), JetFuel, https://jetfuel.agency/meta-ads-attribution-settings-2026/, 2026
11. What Meta's March 2026 attribution update means, Leafsignal, https://www.leafsignal.com/blog/meta-march-2026-attribution-update, 2026-03
12. Drive Social Media update on 2026 Meta attribution window changes, Business Wire, https://www.businesswire.com/news/home/20260610201735/en/Drive-Social-Media-Offers-an-Update-to-Clients-Regarding-the-2026-Meta-Ads-Attribution-Window-Changes, 2026-06-10
13. Meta Attribution Update: Click-Through vs Engage-Through Explained, ALM Corp, https://almcorp.com/blog/meta-click-through-engage-through-attribution-update/, 2026
14. Set up Conversion Lift based on users, Google Ads Help, https://support.google.com/google-ads/answer/12005564, accessed 2026-10
15. Google cuts incrementality testing budget requirements to $5,000 minimum, PPC Land, https://ppc.land/google-cuts-incrementality-testing-budget-requirements-to-5-000-minimum/, 2025-11
16. Google lowers incrementality testing threshold to $5,000, PPC Land, https://ppc.land/google-lowers-incrementality-testing-threshold-to-5-000-for-advertisers/, 2025
17. Google opens Conversion Lift to Search and Performance Max, Search Engine Land, https://searchengineland.com/google-opens-conversion-lift-to-search-and-performance-max-494195, 2026
18. Google Ads Conversion Lift Measurement Now Self-Service, Search Engine Roundtable, https://www.seroundtable.com/google-ads-conversion-lift-measurement-self-service-42250.html, n.d.
19. Google Moves Lift Studies to the Experiments Section in Google Ads, ALM Corp, https://almcorp.com/blog/google-moves-lift-studies-to-experiments-google-ads/, 2026
20. What's new in Google Analytics, Analytics Help, https://support.google.com/analytics/answer/9164320, accessed 2026-10
21. Announcements, Analytics Help, https://support.google.com/analytics/announcements/10707884, accessed 2026-10
22. Measurement Protocol changelog, Google for Developers, https://developers.google.com/analytics/devguides/collection/protocol/ga4/changelog, accessed 2026-10
23. Tag Manager release notes, Tag Manager Help, https://support.google.com/tagmanager/answer/4620708, accessed 2026-10
24. Google Analytics Adds AI Assistant As Default Channel Group, Search Engine Journal, https://www.searchenginejournal.com/google-analytics-adds-ai-assistant-as-default-channel-group/574974/, 2026-05
25. Cross-channel conversion reporting in Analytics, Analytics Help, https://support.google.com/analytics/answer/16638051, accessed 2026-10
26. About cross-channel budgeting, Analytics Help, https://support.google.com/analytics/answer/14896117, accessed 2026-10
27. Google Marketing Live 2025: roundup of announcements, Google Ads Help, https://support.google.com/google-ads/answer/16290177, 2025-05
28. Google Ads Highlights of 2025, Google Ads Help, https://support.google.com/google-ads/answer/16756291, 2025-12
29. Set up Google tag gateway for advertisers with Cloudflare, Google Ads Help, https://support.google.com/google-ads/answer/16061406, accessed 2026-10
30. Set up Google tag gateway for advertisers in GTM with Cloudflare, Tag Manager Help, https://support.google.com/tagmanager/answer/16061641, accessed 2026-10
31. Set up Google tag gateway for advertisers, Google for Developers, https://developers.google.com/tag-platform/tag-manager/gateway/setup-guide, accessed 2026-10
32. Google tag gateway legacy setups, Google for Developers, https://developers.google.com/tag-platform/tag-manager/gateway/legacy-setups, accessed 2026-10
33. Google tag gateway, Cloudflare Docs, https://developers.cloudflare.com/google-tag-gateway, accessed 2026-10
34. What Is Google Tag Gateway?, Stape, https://stape.io/blog/what-is-google-tag-gateway, 2025 to 2026
35. How to Set Up Google Tag Gateway with Cloudflare, Loves Data, https://www.lovesdata.com/blog/google-tag-gateway/, 2025
36. About offline conversion imports, Google Ads Help, https://support.google.com/google-ads/answer/2998031, accessed 2026-10
37. About enhanced conversions for leads, Google Ads Help, https://support.google.com/google-ads/answer/15713840, accessed 2026-10
38. Data Manager API events overview, Google for Developers, https://developers.google.com/data-manager/api/devguides/events/send-events, accessed 2026-10
39. About session_attributes, Google Ads Help, https://support.google.com/google-ads/answer/16194756, accessed 2026-10
40. Google blocks new offline conversion imports via Ads API from June 15, PPC Land, https://ppc.land/google-blocks-new-offline-conversion-imports-via-ads-api-from-june-15/, 2026
41. Google shuts down session tracking for new advertisers in Ads API, PPC Land, https://ppc.land/google-shuts-down-session-tracking-for-new-advertisers-in-ads-api/, 2026
42. Google Ads API tightens conversion data rules, Search Engine Land, https://searchengineland.com/google-ads-api-tightens-conversion-data-rules-467263, 2026
43. Updates to your enhanced conversions settings, Google Ads Help, https://support.google.com/google-ads/answer/16884284, 2026
44. Manage offline conversions, Google Ads API docs, https://developers.google.com/google-ads/api/docs/conversions/upload-offline, accessed 2026-10
45. Track Google Ads Conversions: Data Manager API Guide, Stape, https://stape.io/blog/google-ads-conversions-tracking-with-data-manager-api, 2026
46. Google's Data Manager API wants to kill your three-pipeline headache, PPC Land, https://ppc.land/googles-data-manager-api-wants-to-kill-your-three-pipeline-headache/, 2025 to 2026
47. All You Need to Know About the Transition to TCF v2.3, IAB Europe, https://iabeurope.eu/all-you-need-to-know-about-the-transition-to-tcf-v2-3/, 2025
48. Publisher integration with the IAB Europe TCF, Google Ad Manager Help, https://support.google.com/admanager/answer/9805023, accessed 2026-10
49. Google mandates TCF v2.3 migration by February 2026, PPC Land, https://ppc.land/google-mandates-tcf-v2-3-migration-by-february-2026/, 2025
50. Standard Contract for the Transfer of Personal Data Abroad (Processor to Processor), KVKK, https://www.kvkk.gov.tr/Icerik/7994/Standard-Contract-for-the-Transfer-of-Personal-Data-Abroad-3-Processor-to-Processor-, 2024
51. What does the guideline on transfer of personal data abroad regulate, Erdem and Erdem, https://www.erdem-erdem.av.tr/en/insights/what-does-the-guideline-on-transfer-of-personal-data-abroad-regulate, 2025
52. KVKK grants first approval for cross-border transfer based on a non-international agreement, DT Law, https://dtlaw.com.tr/en/kvkk-grants-first-approval-for-cross-border-data-transfer-based-on-a-non-international-agreement/, 2025-11
53. 2026 KVKK Administrative Fines, Esenyel Partners, https://www.esenyelpartners.com/2026-kvkk-administrative-fines-current-amounts-and-warnings/, 2026
54. Standard Contract Notification Obligation and Penalties, Cottgroup, https://www.cottgroup.com/en/blog/kvkk-gdpr/item/standard-contract-notification-obligation-and-penalties, 2024 to 2025
55. The long awaited amendments in Turkish data protection law, Gün + Partners, https://gun.av.tr/insights/updates/the-long-awaited-amendments-in-turkish-data-protection-law, 2024
56. EU Member States (and Google) suddenly want to keep cookie banners, noyb, https://noyb.eu/en/eu-member-states-and-google-suddenly-want-keep-cookie-banners, 2026
57. Digital Omnibus reshapes EU cookie rules but leaves banner fatigue largely intact, Osborne Clarke, https://www.osborneclarke.com/insights/digital-omnibus-reshapes-eu-cookie-rules-leaves-banner-fatigue-largely-intact, 2025 to 2026
58. How the Digital Omnibus could reshape cookie compliance, Freshfields, https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/how-the-eu-commissions-digital-omnibus-could-reshape-cookie-compliance-in-europe-102m196, 2025
59. Vote on Digital Omnibus postponed until 11 October, Agence Europe, https://agenceurope.eu/en/bulletin/article/13954/5/vote-on-digital-omnibus-postponed-until-11-october-under-pressure-from-paris-and-berlin, 2026-10
60. Digital Omnibus and the GDPR: what the proposal would change, Praxikon, https://www.praxikon.com/en/avg/digital-omnibus, 2026
61. Digital Omnibus GDPR and cookie reforms stall without a Council mandate, Acompli, https://acompli.ie/news/digital-omnibus-gdpr-cookies-status-september-2026/, 2026-09
62. The Digital Omnibus: cookies, consent and digital advertising, Taylor Wessing, https://www.taylorwessing.com/en/global-data-hub/2026/the-digital-omnibus-proposal/gdh---the-digital-omnibus---cookies, 2026
63. EU drops browser-based cookie consent proposal from Digital Omnibus, Digital Watch, https://dig.watch/updates/eu-cookie-banners-digital-omnibus, 2026
64. Industry coalition calls for meaningful simplification in the digital omnibus, FEDMA, https://www.fedma.org/2026/06/24/ahead-of-the-coreper-meeting-industry-coalition-calls-for-meaningful-simplification-in-the-digital-omnibus/, 2026-06-24
65. Testing ads in ChatGPT, OpenAI, https://openai.com/index/testing-ads-in-chatgpt/, 2026-01-16 (via chatgpt-ads builder notes)
66. New import center and other product news for May 2026, Microsoft Advertising blog, https://about.ads.microsoft.com/en/blog/post/may-2026/new-import-center-and-other-product-news-for-may-2026, 2026-05 (via microsoft-ads builder notes)
67. Performance Max updates and other product news for January 2026, Microsoft Advertising blog, https://about.ads.microsoft.com/en/blog/post/january-2026/performance-max-updates-and-other-product-news-for-january-2026, 2026-01 (via microsoft-ads builder notes)
68. google-analytics-mcp repository, Google, https://github.com/googleanalytics/google-analytics-mcp, 2025
69. google-ads-mcp repository, Google, https://github.com/googleads/google-ads-mcp, 2025
70. Meridian repository, Google, https://github.com/google/meridian, 2025
71. Robyn repository, Meta, https://github.com/facebookexperimental/Robyn, ongoing
72. PyMC-Marketing repository, PyMC Labs, https://github.com/pymc-labs/pymc-marketing, ongoing
73. GeoLift repository, Meta, https://github.com/facebookincubator/GeoLift, ongoing
74. MCP Toolbox for Databases, Google, https://github.com/googleapis/genai-toolbox, ongoing
75. Web Pixels API, Shopify, https://shopify.dev/docs/api/web-pixels-api, accessed 2026-10
76. Conversions API, Meta for Developers, https://developers.facebook.com/docs/marketing-api/conversions-api, accessed 2026-10
77. AdAttributionKit, Apple Developer, https://developer.apple.com/documentation/adattributionkit, accessed 2026-10
