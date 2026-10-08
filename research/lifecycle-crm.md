# Research Dossier: Lifecycle Marketing, CRM and Retention

> Research date: 2026-10-08. Scope: email, SMS, RCS, WhatsApp, push and in-app lifecycle marketing; flows, segmentation, deliverability, consent law, list growth, subscriptions, loyalty, referral, reviews, B2B nurture and lead scoring, cohort and LTV analysis, and the lifecycle to paid media loop.
>
> Method and limits: 33 web searches (extended mode for 2025 to 2026 facts, standard for reference facts). Direct page fetching (WebFetch) failed with DNS errors in the build environment, so most findings rely on search result summaries of the cited pages. Primary documents read directly: the Klaviyo OpenAPI specification (revision 2026-07-15) and the klaviyo-api-python changelog (cloned from github.com/klaviyo), and the Iterable MCP server repository (github.com/Iterable/mcp-server, v1.9.0). Long standing legal texts (TCPA, CAN-SPAM, ePrivacy, CASL) are cited from established knowledge where noted. Every claim carries an evidence label; single source or unconfirmed items are marked [Unverified]. Source numbers in brackets refer to section 12.

## 1. Executive summary

1. Mailbox enforcement got real. Gmail moved non compliant bulk traffic from mostly temporary errors to temporary and permanent rejections in November 2025 [3, 4, 5]; Microsoft has rejected unauthenticated high volume mail to Outlook consumer domains with `550 5.7.515` since 2025-05-05 [6, 7]; Apple publishes requirements and rejects non compliant bulk mail [9]. SPF, DKIM, aligned DMARC, RFC 8058 one click unsubscribe and a spam rate under 0.1% are table stakes [1, 2, 19].
2. Opens are dead as a decision metric. Apple (with Mail Privacy Protection) accounted for about 62% of tracked opens in Litmus's July 2026 sample [18], AI assistants and scanners create machine opens, and France's CNIL now requires consent for individual open tracking used for campaign optimization (recommendation adopted 2026-03-12, transition ended 2026-07-14) [20, 21, 22]. Engagement tiers must be built on clicks, orders and site activity.
3. Inbox UX shifted power to recipients. Gmail's Manage subscriptions view (July 2025) lists senders by volume with one tap unsubscribe [14]; the Promotions tab gained "Most relevant" sorting and a Purchases view (2025-09-11) [15, 16]; Gemini and Apple Intelligence summaries paraphrase emails [17]. High frequency to unengaged subscribers is now directly punished.
4. US SMS got more expensive and legally noisier. Carrier pass-through fees rose through 2026 (Verizon outbound SMS to $0.0050 from 2026-10-01; AT&T and T-Mobile increases earlier) [45, 46, 47]; toll-free verification added business registration fields [48, 49]; quiet hours class actions surged [33, 35]; the FCC one-to-one consent rule was vacated (2025-01-24) [28, 29] and the "revoke all" rule was delayed to 2027-01-31 then narrowed by an order adopted 2026-09-30 [30, 31, 32].
5. WhatsApp became a priced, policed channel. Per message template pricing since 2025-07-01, service and in-window utility messages charged beyond 1,000 free service messages per number per month from 2026-10-01 [54, 55, 57]; marketing templates to US numbers paused since 2025-04-01 [56]; general purpose AI chatbots barred from the Business API from 2026-01-15, with a Brazil carve out [58, 59, 60].
6. Every major ESP shipped agents and MCP access. Klaviyo Composer (2026-03, public beta 2026-06) and a remote MCP server; Braze Decisioning Studio Go (GA 2026-10-14) and Operator Connect via the Braze MCP server; Customer.io MCP v2 (2026-05-04); Iterable Nova (2026-04-22) and a safe by default open source MCP server; HubSpot remote MCP GA (2026-04-13); Omnisend MCP with write actions (2026-07) [64 to 85]. Agent access is easy; gating sends is the governance problem.
7. Flows still carry the program. Klaviyo's 2026 benchmark reports flows at 5.3% of sends but about 41% of email revenue [86, secondary]; Omnisend's 2025 data shows automations at 2% of sends and 30% of email revenue, with cart and welcome driving 76% of automation orders [88]. Both are attributed figures; incrementality needs holdouts.
8. Subscriptions consolidated and regulation shifted to states. Recharge acquired Skio (2026-04-30, reported $105 million) [90, 91]; the FTC click to cancel rule was vacated (2025-07-08) and rulemaking restarted with an ANPRM (2026-03-13) [41, 42]; California's amended Automatic Renewal Law (from 2025-07-01) is the practical US standard [43].
9. Consent law diverged by market. UK PECR fines rose to £17.5 million or 4% of turnover and a charity soft opt-in started (2026-02-05) [23, 24]; the EU Digital Omnibus cookie changes remain unadopted [26, 27]; Turkey raised 2026 fines and the KVKK Board required separate consents (no single OTP for membership, data processing and commercial messages) [39, 40].
10. Lifecycle data now flows into paid media through stricter pipes. Google Customer Match uploads via the Google Ads API were disabled for most tokens from 2026-04-01 in favor of the Data Manager API [95, 96]; Meta restricted health and financial audiences (from 2025-09-02) and launched exclusion only audiences (2026-08-10) [97, 98]. Suppression lists and validated LTV values are the main lifecycle contributions to acquisition efficiency.

## 2. State of the channel in 2026 (with numbers)

### 2.1 Email
- Klaviyo 2026 Omnichannel Benchmark (183K+ brands): flows 5.3% of sends, about 41% of email revenue; flow placed order rate 2.11% vs 0.16% for campaigns; revenue per recipient $1.94 for flows vs $0.11 for campaigns [86, via secondary summaries; Study, vendor].
- Omnisend 2026 report (about 150,000 brands, 27 billion emails, 321 million SMS, 458 million push in 2025): automations 2% of sends, 30% of email revenue, 16x revenue per send, 19x conversion rate; back in stock emails converted at 6.46%; welcome emails 2.11% conversion and $6.16 per email; abandoned cart 1.51% and $2.54 per email; click to conversion across emails rose from 5.9% to 9% year over year [88; Study, vendor].
- Litmus July 2026 sample of 1 billion+ opens: Apple about 62.26%, Gmail about 27.03%, Outlook about 5.83% of tracked opens (figures via secondary) [18].
- Gmail bulk sender rules in force since February 2024; enforcement escalated November 2025 [1 to 5].

### 2.2 SMS and RCS
- Omnisend 2025 data: SMS campaigns 12.39% click through and 0.12% conversion across 246 million sends; automated SMS 20.34% click through, 0.77% conversion, $0.74 revenue per send vs $0.15 for campaigns; monthly campaign click through ranged 3.47% (January) to 23.92% (December) [89; Study, vendor].
- US 10DLC: unregistered A2P traffic blocked since 2025-02-01; TCR brand fee $4.50 since 2025-08-01; Verizon $0.0050 per outbound SMS since 2026-10-01 [45 to 50; secondary].
- RCS: Klaviyo lists RCS in 12 markets (US, UK, France, Germany, Italy, Spain, Sweden, Norway, Denmark, Austria, Poland, Mexico) [62]; Attentive claims 45% higher click through and 37% higher conversion for RCS vs SMS in early data [63; Unverified vendor claim]; Iterable added native RCS in 2026-09 [78].
- iOS 26 "Screen unknown senders" filters texts from unknown numbers when enabled; adoption unknown, impact contested [51, 52, 53].

### 2.3 WhatsApp
- Per message pricing (template categories, by country) since 2025-07-01; from 2026-10-01 free form service replies charged after 1,000 free service messages per business number per month and in-window utility templates become paid; marketing and authentication unchanged by that step [54, 55, 57].
- US marketing templates paused since 2025-04-01, still paused as of 2026-07 [56].
- General purpose AI assistants banned from 2026-01-15; task specific bots allowed; Brazil suspended the policy for +55 numbers [58 to 60].
- Klaviyo WhatsApp (launched about 2025-10) uses SMS credits, non US destinations only [72, 73].

### 2.4 Subscriptions and loyalty
- Recharge self-reports 71% of Shopify subscriptions; acquired Skio 2026-04-30 [90, 91].
- LoyaltyLion AI Campaigns (2026-01) and order count tiers (2026-08) [92, 93]; Smile Loyalty Hub in Shopify customer accounts and Sidekick (2026-06) [94]; Yotpo pricing changes and acquisition rumors reported only by aggregators [Unverified].

### 2.5 B2B
- HubSpot retired the legacy HubSpot Score (no new legacy scores from 2025-05-01; stopped updating 2025-08-31) [84]; remote MCP server GA 2026-04-13 [85].

### 2.6 Repeat purchase and time to second order
- One vendor dataset of 156K DTC customers: 18.8% 12 month repeat rate; 50.3% of second orders within 30 days and 76.4% within 90 days of the first [99; Unverified]. Vendor medians for time to second purchase: apparel 15 to 27 days, supplements 27 to 68 days, durables 30+ days [100; Unverified].

## 3. Timeline of changes, January 2025 to October 2026

| Date | Change | Impact on lifecycle | Evidence |
|------|--------|---------------------|----------|
| 2025-01 | Meta prompts advertisers to certify customer list compliance | Audience uploads need policy check | [97] Secondary |
| 2025-01-15 | Klaviyo API revision: Reviews APIs, create Flows API, push in Campaigns API | Programmatic reviews, flows, push | [69] Official |
| 2025-01-24 | Eleventh Circuit vacates FCC one-to-one consent rule | Lead gen SMS consent stays seller specific but not one-to-one | [28] Legal |
| 2025-02 | HubSpot announces retirement of legacy HubSpot Score | Scoring rebuilds | [84] Secondary |
| 2025-02-01 | US carriers block unregistered 10DLC traffic | Registration mandatory | [50] Secondary |
| 2025-04-01 | WhatsApp pauses marketing templates to US numbers | No US WhatsApp marketing | [56] Secondary |
| 2025-04-02 | Microsoft announces high volume sender requirements for Outlook consumer domains | Authentication required | [6] Secondary of official |
| 2025-04-06 | UK DMCC Act consumer enforcement starts (fake reviews, drip pricing) | Review practices | [Prior knowledge; Official UK] |
| 2025-04-07 | FCC delays "revoke all" provision to 2026-04-11 | Opt-out scope | [30] Legal |
| 2025-04-11 | FCC revocation rules take effect (any reasonable means, max 10 business days) | SMS opt-out handling | [30, 31] Legal |
| 2025-04-15 | Klaviyo API: web feeds, universal content, custom metrics, push tokens, AMP | Richer content and reporting | [69] Official |
| 2025-05-05 | Microsoft begins rejecting non compliant mail (550 5.7.515) | Outlook bounces | [6, 7] Secondary |
| 2025-06 | Braze completes OfferFit acquisition (now Decisioning Studio) | AI decisioning | [75] Official |
| 2025-06-10 | KVKK Board principle decision 2025/1072 (Official Gazette 2025-06-26): separate consents, no single OTP | Turkey consent flows | [39] Official |
| 2025-06 (late) | US Supreme Court McLaughlin v. McKesson: courts not bound by FCC TCPA interpretations | TCPA uncertainty | [Prior knowledge; Official ruling] |
| 2025-07 | Gmail Manage subscriptions view | Easier unsubscribes | [14] Official |
| 2025-07-01 | WhatsApp per message pricing replaces conversation pricing | Cost model change | [54] Official |
| 2025-07-01 | California ARL amendments (AB 2863) apply | Subscription consent, cancellation, notices | [43] Legal |
| 2025-07-08 | Eighth Circuit vacates FTC click to cancel rule | No federal rule | [41] Legal |
| 2025-07-15 | Klaviyo API: mapped metrics, custom objects ingestion | Data model | [69] Official |
| 2025-08-01 | TCR brand registration fee to $4.50 | SMS cost | [50] Secondary |
| 2025-08-31 | HubSpot legacy scores stop updating | Broken workflows if not migrated | [84] Secondary |
| 2025-09 | FCC formally removes one-to-one consent rule | Settled | [29] Legal |
| 2025-09-02 | Meta restricts audiences suggesting health or financial status | Lifecycle uploads to Meta | [97] Secondary |
| 2025-09-11 | Gmail Promotions "Most relevant" sorting and Purchases view announced | Engagement weighted promotions | [15] Official |
| 2025-09 | iOS 26 ships with Screen unknown senders | SMS visibility risk | [51, 52] Secondary |
| 2025-10 (about) | Klaviyo WhatsApp launch | WhatsApp in Klaviyo for non US | [72] Official |
| 2025-10-06 | ePrivacy Regulation withdrawal published | Directive stays | [26] Legal |
| 2025-10-15 | WhatsApp terms bar general purpose chatbots for new accounts; Klaviyo Flow Actions and Forms APIs | AI bot policy; flow automation | [58, 69] |
| 2025-11 | Gmail escalates to temporary and permanent rejections for non compliant bulk mail | Compliance or bounce | [3, 4, 5] Secondary |
| 2025-11-19 | EU Digital Omnibus proposal (cookie consent into GDPR Article 88a) | Watch item | [26, 27] Legal |
| 2025-12-03 | Meta customer list terms reportedly bar health, financial, consumer report data | Upload hygiene | [97] Unverified |
| 2025-12-25 | Turkey 2026 administrative fines published (Official Gazette 33118) | Higher İYS exposure | [40] Legal |
| 2026-01 | LoyaltyLion AI Campaigns | Loyalty automation | [92] Official |
| 2026-01-01 to 2026-02-17 | Toll-free verification requires business registration number, country, entity type (provider dates differ) | SMS onboarding | [48, 49] |
| 2026-01-06 | FCC delays "revoke all" to 2027-01-31 | Opt-out scope | [30] Legal |
| 2026-01-15 | WhatsApp general purpose chatbot ban applies to existing accounts; Klaviyo API removes anonymous_id from profiles | AI bots; integrations | [58, 69] |
| 2026-01-19 | T-Mobile updated A2P fees | SMS cost | [46] Secondary |
| 2026-02-05 | UK DUAA PECR changes commence: fines to £17.5m or 4%; charity soft opt-in | UK enforcement risk | [23] Official |
| 2026-02-19 | HubSpot Developer MCP server GA | Developer access | [85] Secondary |
| 2026-03-12 | CNIL adopts tracking pixel recommendation (published 2026-04-14) | French open tracking consent | [20, 21] Official |
| 2026-03-13 | FTC negative option ANPRM published | Rulemaking restart | [42] Official |
| 2026-03-24 | Klaviyo Composer announced | AI built campaigns and flows | [64] Official |
| 2026-04-01 | Google disables Customer Match uploads via Google Ads API for most tokens (Data Manager API); AT&T SMS fees rise | Audience pipelines; SMS cost | [95, 96, 47] |
| 2026-04-13 | HubSpot remote MCP server GA | B2B agent access | [85] Secondary |
| 2026-04-15 | Klaviyo Conversations API (SMS, WhatsApp) and drag and drop templates API | Messaging via API | [69] Official |
| 2026-04-22 | Iterable Nova Agent | AI agents | [78] Official |
| 2026-04-28 | ICO guidance on charitable purposes soft opt-in | UK charities | [24] Legal |
| 2026-04-30 | Recharge acquires Skio | Subscription vendor consolidation | [90, 91] Official |
| 2026-05-01 | Verizon 10DLC surcharge step ($0.0045) | SMS cost | [45] Secondary |
| 2026-05-04 | Customer.io MCP v2 | Agent access | [76] Official |
| 2026-05 | Omnisend MCP integration; SMS from $0.007 per message | SMB agent access, SMS cost | [81] Official |
| 2026-05-20 | Attentive Visibility AI for RCS | RCS routing | [63] Official |
| 2026-05-21 | DMARCbis reportedly published as RFC 9989 to 9991 | No bulk sender change reported | Unverified |
| 2026-05-26 | Attentive Thread 2026: Brand Voice 2.0, Reporting Agent | AI tooling | [82] Official |
| 2026-05-28 | Mailchimp Analytics AI and Claude integration | SMB agent access | [80] Official |
| 2026-06-22 | Council compromise reportedly deletes Omnibus Article 88a | Cookie rules unchanged for now | [26] Contested |
| 2026-06-30 | Klaviyo K:LDN: Composer public beta, Customer Agent upgrades, MCP across Claude products | AI in ESP | [65] Official |
| 2026-07-14 | CNIL pixel transition ends | Enforcement phase | [20 to 22] Official |
| 2026-07-15 | Klaviyo API: custom objects CRUD, event backfill flag, plural Conversations endpoints | Data model | [68, 69] Official |
| 2026-08-01 | WhatsApp Meta Business Agent billed by tokens | AI agent cost | [55] Official |
| 2026-08-10 | Meta exclusion only custom audiences | Cleaner suppression | [98] Secondary |
| 2026-09-09 to 10 | Klaviyo K:BOS: SQL over account data via Composer and MCP (preview) | Agent analytics | [66] Secondary |
| 2026-09-24 | Iterable Fall release: RCS, WhatsApp, Nova Intelligence Agents | Channels | [78] Official |
| 2026-09-29 | Braze Forge 2026: Decisioning Studio Go (GA 2026-10-14), Agentic Standards, Operator Connect, Conversational Agents beta | AI decisioning and QA | [74] Official |
| 2026-09-30 | FCC adopts narrowed revocation order; effective 30 days after Federal Register publication | Opt-out handling | [31, 32] Legal |
| 2026-10-01 | WhatsApp service and in-window utility billing change; Verizon $0.0050 per SMS | Messaging cost | [55, 45] |

## 4. Best practice consensus

1. Authenticate a branded sending domain (SPF, DKIM 2048, DMARC aligned, moving to enforcement), add RFC 8058 one click unsubscribe, and keep Gmail spam rate under 0.1% [1, 2, 19] [Official].
2. Build core flows before campaign frequency: welcome, checkout and cart abandonment, browse abandonment, post purchase split by first time vs repeat buyer, winback, sunset [86, 88] [Practitioner consensus].
3. Tier campaign audiences by engagement measured with clicks, orders and site activity; sunset 120 to 180 day unengaged profiles [Practitioner consensus; 18, 20].
4. Time replenishment to consumption using SKU reorder intervals [Practitioner consensus].
5. Keep discounts out of the first abandonment touch; use unique, expiring codes; test with holdouts [Practitioner consensus].
6. Capture consent per channel with proof; double opt-in in Germany and for risky sources; separate SMS consent with TCPA language in the US; İYS registration in Turkey [Official law; 37 to 39].
7. Respect SMS quiet hours in recipient time zones (federal 8:00 to 21:00, stricter states 8:00 to 20:00) [Official statutes; 33].
8. Use holdouts to measure incrementality of flows and programs [Practitioner consensus].
9. Feed suppression and existing customer lists to paid media; keep them fresh [95 to 98] [Practitioner consensus].
10. Keep transactional messages transactional and separate from marketing streams [15, 17] [Practitioner consensus].

## 5. Contested topics (both sides)

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Discounts in welcome and abandonment flows | Discounts lift conversion and list growth | Discounts train customers, cut margin, and holdouts often show timing shifts not new orders | Test with holdouts on contribution; late, unique, expiring |
| How much revenue lifecycle "drives" | Attributed figures (often 20% to 40% of DTC revenue) show huge value | Holdouts show much lower incremental shares for abandonment and post purchase upsell | Report both, decide on incremental |
| Aggregate open tracking under CNIL | Anonymous campaign level pixels need no consent | Exemption narrow; anonymization alone not an exemption | For French recipients, avoid individual open data without consent; ask counsel [20 to 22] |
| iOS 26 unknown senders impact | Vendors warn of engagement drops | Postscript sees no meaningful impact at scale; adoption unknown | Measure replied vs non replied subscribers [51, 52] |
| Quiet hours and consented texts | Plaintiffs: quiet hours apply regardless of consent | Some courts: consent is invitation; texts may not be "calls" | Send 10:00 to 20:00 local; watch FCC petition [33 to 35] |
| Microsoft 2026 tightening | Vendors claim stricter PTR and p=none scrutiny | No Microsoft document confirms | Meet baseline; monitor SNDS [6, 8] |
| Gmail Promotions default sort | Some outlets: "most relevant" is default | Google frames it as user choice | Engagement matters either way [15, 16] |
| WhatsApp frequency cap number | About 2 marketing templates per user per day | Meta does not publish a number | Plan for caps; monitor error 131049 [61] |
| Loyalty program ROI | Vendor stats show members spend more | Self selection; little causal evidence | Holdout or matched cohort |
| Dedicated IP | Gives control at scale | Shared pools are fine below high volume; warmup risk | Only at consistent high volume |

## 6. What top operators do differently

- Treat the second order as the north star for DTC and build the post purchase and replenishment engine from their own SKU data.
- Run flow holdouts and a global control group; report incremental contribution, not attributed revenue, to finance and the growth lead.
- Monitor deliverability per mailbox provider weekly (Postmaster v2 compliance status, Yahoo Sender Hub, bounce codes) and sunset relentlessly.
- Version campaigns by lifecycle stage and category affinity; rarely blast the full list.
- Keep consent records audit ready across jurisdictions (TCPA language and logs, İYS sync, CNIL tracking consent, soft opt-in proof).
- Read SMS and WhatsApp on fully loaded cost per message; move low intent sends back to email when carrier fees rise.
- Use AI agents (Composer, Decisioning Studio, Nova) inside guardrails: drafts and bounded decisioning, with holdouts and human approval for sends.
- Share LTV by acquisition source monthly with the paid media team and suppress buyers from acquisition campaigns.
- In B2B, measure speed to lead in minutes and rebuild scoring from closed won data (and migrated off the retired HubSpot legacy score in 2025).

## 7. Common expensive mistakes

- Full list sends after imports or long pauses, causing complaint spikes and Gmail or Yahoo blocks.
- Missing one click unsubscribe headers or DMARC alignment after an ESP migration (Gmail rejections since November 2025; Outlook 5.7.515 since May 2025).
- Optimizing to open rates inflated by Apple MPP; open based sunset rules that never suppress anyone.
- Discount in the first cart email; generic reusable codes leaked to coupon sites.
- SMS sent at 21:15 recipient time; TCPA consent language missing "not a condition of purchase"; STOP not honored across tools.
- WhatsApp marketing templates sent to US numbers or miscategorized as utility; general purpose AI assistants deployed on WhatsApp after 2026-01-15.
- Subscription portals that hide cancel or force a call (California ARL, ROSCA exposure).
- Uploading health related or financial segments to Meta; broken Google Customer Match syncs after 2026-04-01.
- Turkey: consents not registered in İYS within 3 business days; consent collected through a single OTP with membership terms.
- B2B: workflows still keyed to the frozen HubSpot legacy score.

## 8. Benchmarks (source, date, caveat)

| Metric | Value | Source and date | Sample | Caveat |
|--------|-------|-----------------|--------|--------|
| Flow share of sends and email revenue | 5.3% of sends, about 41% of revenue | Klaviyo 2026 benchmark [86] | 183K+ brands | Secondary reproduction; attributed |
| Flow vs campaign placed order rate | 2.11% vs 0.16% | Klaviyo 2026 [86] | Same | Attributed |
| Flow vs campaign RPR | $1.94 vs $0.11 | Klaviyo 2026 [86] | Same | Attributed |
| Flow RPR by type | Back in stock $9.14; cart $3.65 (top 10% $28.89); welcome $2.65 (top 10% $21.18); browse $1.07 (top 10% $7.21); winback $0.84 | Klaviyo data via agencies [Unverified] | Unknown | AOV dependent |
| Flow placed order rate by industry | 1.94% (automotive) to 2.46% (food and beverage) | Klaviyo UK benchmarks [87] | Klaviyo accounts | Definitions differ from US page |
| Automation share | 2% of sends, 30% of email revenue | Omnisend 2026 report [88] | 150K brands, 2025 data | Vendor |
| Cart plus welcome share of automation orders | 76% | Omnisend [88] | Same | Vendor |
| Back in stock conversion | 6.46% | Omnisend [88] | Same | Another Omnisend page says 5.34% |
| SMS campaign vs automated | 12.39% CTR, 0.12% CVR vs 20.34% CTR, 0.77% CVR | Omnisend [89] | 246M+ campaign sends | Seasonal |
| Apple share of tracked opens | About 62% | Litmus July 2026 [18] | 1B+ opens | Inflated by MPP; secondary figure |
| Pop up submit rate | About 2.3% median | Klaviyo in-app benchmark via secondary [Unverified] | Unknown | Submits / views |
| Pop up conversion | About 4.8% average | Revlifter [Unverified] | Unknown | Definitions vary |
| Repeat purchase 12 months | 18.8% | Vendor dataset [99] | 156K customers | Reused by vendors |
| Second orders within 90 days | 76.4% of all second orders | Vendor dataset [99] | Same | Same |
| Loyalty redeemer repeat | 50% vs 10.7% | Vendor compilation [Unverified] | Unknown | Correlation, self selection |
| RCS vs SMS lift | +45% CTR, +37% CVR, +36% revenue per send | Attentive [63] | Early adopters | Vendor claim |
| BIMI record errors | 53.6% have at least one error | URIports 2025 via [12] | Published BIMI records | Vendor analysis |

## 9. Tools, APIs and MCP servers

| Tool | Access for Claude | Notes |
|------|-------------------|------|
| Klaviyo | Remote MCP `https://mcp.klaviyo.com/mcp` (OAuth; Owner, Admin, Manager roles; `core-tools-only=true` for about 40 tools); REST API revision 2026-07-15 | Reporting endpoints: burst 1/s, steady 2/m, daily 225/d; Conversations API for SMS and WhatsApp [67, 68, 69] |
| Braze | Braze MCP server (Operator Connect; OAuth; inherits user permissions) | 2025 MCP version deprecated [74] |
| Customer.io | MCP v2 (Journeys UI API, Data Pipelines API), CLI | Admin toggles for AI and MCP [76, 77] |
| Iterable | `@iterable/mcp` (open source, 118 tools); safe default: no PII, no writes, no sends | Creating a blast campaign schedules it [79] |
| HubSpot | Remote MCP `mcp.hubspot.com` (OAuth 2.1 PKCE), Developer MCP | Read and write CRM objects [85] |
| Omnisend | MCP integration with write actions since 2026-07 | [81] |
| Mailchimp | Claude integration (2026-05-28) | [80] |
| Google Postmaster Tools API v2 | Compliance status, spam rate | Reputation not in v2 [11] |
| Google Data Manager API | Customer Match ingestion | Required for most new integrations from 2026-04-01 [96] |
| İYS API | Consent and refusal sync (Turkey) | Via brand account or authorized integrator [37, 38] |

## 10. Official sources to monitor

- Google: sender guidelines and FAQ, Postmaster Tools help, Google Workspace Updates blog, Gmail blog.
- Yahoo Sender Hub; Microsoft Defender for Office 365 blog and Outlook postmaster pages; Apple Support 102322.
- Klaviyo developer changelog and API revisions, help center, What's new, newsroom; Braze press releases and docs; Customer.io release notes; Iterable newsroom; Omnisend What's new; Mailchimp release notes; Attentive and Postscript release notes; HubSpot product updates.
- FCC TCPA proceedings (CG Docket 02-278) and the Federal Register; CTIA messaging principles; provider notices on TCR and carrier fees.
- Meta WhatsApp Business Platform pricing and policy pages.
- CNIL, EDPB, ICO, European Commission Digital Omnibus file.
- iys.org.tr, Ticaret Bakanlığı, KVKK decisions, Resmi Gazete.
- FTC negative option docket P064202; California Attorney General ARL guidance.
- Google Ads API and Data Manager API release notes; Meta Marketing API changelog and customer list terms.

## 11. Open questions and watch list

1. Federal Register publication date and effective date of the FCC 2026-09-30 revocation order; outcome of the further notice (shorter honoring time, two way texting).
2. Any FCC ruling on the quiet hours petition for consented texts.
3. Whether WhatsApp lifts the US marketing template pause; official frequency cap documentation; the 2026-10-01 billing rollout in practice.
4. Final Digital Omnibus text (cookie consent location, aggregated measurement exemption) and whether it touches email pixels.
5. Italy Garante pixel deadlines (reported 2026-07-14 and 2026-10-29) [Unverified].
6. Gmail Postmaster v1 API shutdown date and v2 API scope; Microsoft SNDS migration date.
7. Klaviyo SQL via Composer and MCP general availability; Composer GA; Braze Decisioning Studio Go GA on 2026-10-14.
8. Recharge and Skio product roadmap after integration; Yotpo pricing and ownership [Unverified rumors].
9. UK DMCC subscription contract rules commencement date [Unverified].
10. Google Customer Match deadline for existing Google Ads API integrations (reported March 2027) [Unverified].
11. iOS adoption of Screen unknown senders and measured SMS impact.
12. Turkey: commencement status of the integrator authorization rule; any 2026 İYS regulation changes.

## 12. Sources

1. Email sender guidelines FAQ. Google. https://support.google.com/a/answer/14229414 (ongoing, seen 2026-10-08)
2. Email sender guidelines. Google. https://support.google.com/a/answer/81126 (ongoing)
3. Why Gmail is rejecting your emails. Valimail. https://www.valimail.com/blog/google-email-compliance-enforcement/ (2025-11)
4. Gmail's enforcement ramps up: what bulk senders need to know. Red Sift. https://redsift.com/blog/gmails-enforcement-ramps-up-what-bulk-senders-need-to-know (2025-11)
5. New Gmail bulk sender compliance updates, November 2025. Suped. https://www.suped.com/blog/new-gmail-bulk-sender-compliance-updates-november-2025 (2025-11)
6. Microsoft enforces SPF, DKIM, DMARC for high-volume senders. dmarcian. https://dmarcian.com/microsoft-enforces-spf-dkim-dmarc/ (2025)
7. Outlook error 550 5.7.515 and how to fix it. URIports. https://www.uriports.com/blog/outlook-error-550-5-7-515-and-how-to-fix-it/ (2025)
8. Microsoft sender requirements: the complete 2026 reference. Mailercloud. https://www.mailercloud.com/blog/microsoft-sender-requirements (2026)
9. Postmaster information for iCloud Mail. Apple Support. https://support.apple.com/en-us/102322 (ongoing)
10. Yahoo Sender Hub Insights and Google Postmaster Tools v2. Validity. https://www.validity.com/blog/peek-behind-the-curtain-how-email-marketers-should-use-yahoos-new-sender-hub-insights-and-google-postmaster-tools-v2/ (2025)
11. Learn about the deprecation of the old Postmaster Tools interface. Gmail Help. https://support.google.com/mail/answer/16594218 (2025 to 2026)
12. BIMI in 2026: verified logos, CMCs and the fastest path to inbox display. Red Sift. https://redsift.com/guides/bimi-in-2026-verified-logos-cmcs-and-the-fastest-path-to-inbox-display (2026)
13. Google's latest BIMI changes (CMC). Valimail. https://www.valimail.com/blog/google-cmc-bimi-announcement/ (2024)
14. Manage email subscriptions from a single location in Gmail. Google Workspace Updates. https://workspaceupdates.googleblog.com/2025/07/manage-email-subscriptions-in-gmail.html (2025-07)
15. Introducing a new purchase tracking view and more relevant promotions in Gmail. Google. https://blog.google/products-and-platforms/products/gmail/one-stop-purchase-tracking-in-gmail/ (2025-09-11)
16. Relevance comes to the Gmail promo tab. Spam Resource. https://www.spamresource.com/2025/09/relevance-comes-to-gmail-promo-tab.html (2025-09)
17. Gmail's Gemini AI is changing the inbox. Klaviyo. https://www.klaviyo.com/blog/gmail-gemini-in-the-inbox (2025)
18. Email client market share. Litmus. https://www.litmus.com/email-client-market-share (2026-07)
19. RFC 8058: Signaling one-click functionality for list email headers. IETF. https://www.rfc-editor.org/rfc/rfc8058 (2017-01)
20. Recommendation on tracking pixels in emails. CNIL. https://www.cnil.fr/sites/default/files/2026-05/recommandation_tracking_pixels_emails.pdf (2026-04)
21. CNIL issues FAQs on recommendation for tracking pixels in emails. Hunton Andrews Kurth. https://www.hunton.com/privacy-and-cybersecurity-law-blog/cnil-issues-faqs-on-recommendation-for-tracking-pixels-in-emails (2026)
22. France: email tracking pixels, what the CNIL's recommendation changes in practice. Baker McKenzie. https://connectontech.bakermckenzie.com/france-email-tracking-pixels-what-the-cnils-recommendation-changes-in-practice/ (2026)
23. Statement on the commencement of the Data (Use and Access) Act. ICO. https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/statement-on-the-commencement-of-the-data-use-and-access-act-duaa/ (2026-02)
24. The charitable purposes soft opt-in. Lewis Silkin. https://www.lewissilkin.com/insights/2026/05/08/the-charitable-purposes-soft-opt-in-ico-issues-updated-direct-marketing-guidanc-102ms57 (2026-05-08)
25. How do we comply with the PECR electronic mail marketing rules? ICO. https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/how-do-we-comply-with-the-pecr-electronic-mail-marketing-rules/ (2026)
26. Digital Omnibus reshapes EU cookie rules but leaves banner fatigue largely intact. Osborne Clarke. https://www.osborneclarke.com/insights/digital-omnibus-reshapes-eu-cookie-rules-leaves-banner-fatigue-largely-intact (2025 to 2026)
27. How the EU Commission's Digital Omnibus could reshape cookie compliance in Europe. Freshfields. https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/how-the-eu-commissions-digital-omnibus-could-reshape-cookie-compliance-in-europe-102m196 (2025-11)
28. Eleventh Circuit vacates FCC's TCPA one-to-one consent rule. Pierce Atwood. https://www.pierceatwood.com/alerts/eleventh-circuit-vacates-fccs-tcpa-one-one-consent-rule-eve-effective-date (2025-01)
29. The FCC issues final rule formally eliminating the one-to-one consent requirement. Goodwin. https://www.goodwinlaw.com/en/insights/blogs/2025/09/the-fcc-issues-final-rule-formally-eliminating-the-one-to-one-consent-requirement (2025-09)
30. FCC delays effective date of TCPA revoke-all rule until January 31, 2027. Burr and Forman. https://www.burr.com/telephone-consumer-protection-act/the-fcc-delays-effective-date-of-tcpa-revoke-all-rule-until-january-31-2027 (2026-01)
31. Update: FCC adopts final order and further notice on TCPA consent revocation. Inside Global Tech (Covington). https://www.insideglobaltech.com/2026/10/02/update-fcc-adopts-final-order-and-further-notice-on-tcpa-consent-revocation/ (2026-10-02)
32. FCC scraps revoke all and lets businesses pick how consumers opt out. Nixon Peabody. https://nixonpeabody.com/insights/alerts/2026/10/07/fcc-scraps-revoke-all-and-lets-businesses-pick-how-consumers-opt-out (2026-10-07)
33. A loud decision on TCPA quiet hours. Nixon Peabody. https://www.nixonpeabody.com/insights/alerts/2026/05/13/a-loud-decision-on-tcpa-quiet-hours (2026-05-13)
34. FCC seeks comments on petition to address TCPA quiet hours. Troutman Pepper Locke. https://www.troutman.com/insights/fcc-seeks-comments-on-petition-to-address-tcpa-quiet-hours/ (2025)
35. FCC set to adopt TCPA revocation reforms. Ecommerce Innovation Alliance. https://www.ecomm-alliance.org/blog/fcc-set-to-adopt-tcpa-revocation-reforms/ (2026-09)
36. CAN-SPAM Act: a compliance guide for business. FTC. https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business (ongoing)
37. İleti Yönetim Sistemi (İYS). T.C. Ticaret Bakanlığı. https://ticaret.gov.tr/ic-ticaret/ticari-elektronik-iletiler/ileti-yonetim-sistemi-iys (ongoing)
38. Yönetmelikte değişiklik. İYS. https://iys.org.tr/iys/yonetmelik-degisiklik (ongoing)
39. Kişisel Verileri Koruma Kurulu 2025/1072 sayılı ilke kararı. KVKK. https://www.kvkk.gov.tr/Icerik/8338/2025-1072 (2025-06-10)
40. Elektronik ticaret kanunu kapsamında idari para cezaları 2026 yılı için güncellendi. Erdem and Erdem. https://www.erdem-erdem.av.tr/bilgi-bankasi/elektronik-ticaret-kanunu-kapsaminda-idari-para-cezalari-2026-yili-icin-guncellendi (2025-12)
41. Click to cancel just got cancelled. Cooley. https://www.cooley.com/news/insight/2025/2025-07-11-click-to-cancel-just-got-cancelled-eighth-circuit-vacates-entirety-of-ftcs-negative-option-rule (2025-07-11)
42. FTC seeks public comment in response to ANPRM regarding negative option marketing practices. FTC. https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-seeks-public-comment-response-advance-notice-proposed-rulemaking-regarding-negative-option (2026-03)
43. California Automatic Renewal Law amendments take effect on July 1, 2025. Cooley. https://www.cooley.com/news/insight/2025/2025-06-04-california-automatic-renewal-law-amendments-take-effect-on-july-1-2025 (2025-06-04)
44. FTC announces final rule banning fake reviews and testimonials. FTC. https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials (2024-08-14)
45. Verizon A2P SMS and RCS fees increase October 2026. Telgorithm. https://www.telgorithm.com/news/verizon-announces-another-a2p-sms-fee-increase-effective-october-1-2026 (2026)
46. T-Mobile increases A2P 10DLC pass-through fees for 2026. Telgorithm. https://www.telgorithm.com/news/t-mobile-announces-new-2026-a2p-sms-pass-through-fees (2026-01)
47. AT&T A2P SMS and MMS pass-through fee increases effective April 2026. Telgorithm. https://www.telgorithm.com/news/at-t-announces-new-a2p-sms-mms-pass-through-fee-increases-effective-april-1-2026 (2026)
48. Toll-free verification is changing in 2026. Telgorithm. https://www.telgorithm.com/news/toll-free-verification-is-changing-in-2026-heres-what-you-need-to-know (2025-12)
49. Toll-free verification. Telnyx Developers. https://developers.telnyx.com/docs/messaging/toll-free-verification (2026)
50. Carrier fee updates. Tychron. https://www.tychron.com/company/carrier-fee-updates/ (2026)
51. iOS 26 Screen Unknown Senders: a measured look at the real impact on SMS. Postscript. https://postscript.io/blog/ios-26-screen-unknown-senders-a-measured-look-at-the-real-impact-on-sms (2025 to 2026)
52. What iOS 26 means for SMS, MMS and RCS. Braze. https://www.braze.com/resources/articles/ios-26-sms-mms-rcs (2025)
53. Understand iOS 26 update. Omnisend. https://support.omnisend.com/en/articles/12299862-understand-ios-26-update (2025)
54. Pricing on the WhatsApp Business Platform. Meta for Developers. https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing (2026)
55. Upcoming pricing updates for Meta Business Agent, service and utility messages. Meta for Developers. https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages (2026)
56. WhatsApp marketing: the complete 2026 guide. Braze. https://www.braze.com/resources/articles/whatsapp-marketing (2026-07)
57. WhatsApp API message pricing update effective October 1, 2026. YCloud. https://www.ycloud.com/blog/whatsapp-api-message-pricing-update-effective-october-1-2026 (2026)
58. WhatsApp changes its terms to bar general-purpose chatbots from its platform. TechCrunch. https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform (2025-10-18)
59. Brazil orders Meta to suspend policy banning third-party AI chatbots from WhatsApp. TechCrunch. https://techcrunch.com/2026/01/13/brazil-orders-meta-to-suspend-policy-banning-third-party-ai-chatbots-from-whatsapp (2026-01-13)
60. Not all chatbots are banned: WhatsApp's 2026 AI policy explained. respond.io. https://respond.io/blog/whatsapp-general-purpose-chatbots-ban (2026)
61. What is WhatsApp frequency capping. Infobip. https://www.infobip.com/blog/what-is-whatsapp-frequency-capping (2025)
62. RCS Business Messaging. Klaviyo. https://www.klaviyo.com/products/sms-marketing/rcs (2026)
63. Attentive launches Visibility AI to improve deliverability and revenue performance for RCS for Business. Attentive. https://www.attentive.com/press-releases/attentive-launches-visibility-ai-to-improve-deliverability-and-revenue-performance-for-rcs-for-business (2026-05-20)
64. Klaviyo expands AI agents to power the autonomous B2C CRM. Klaviyo. https://www.klaviyo.com/newsroom/composer (2026-03)
65. Klaviyo launches AI agents that work together to drive revenue for consumer brands. Business Wire. https://www.businesswire.com/news/home/20260630493754/en/Klaviyo-Launches-AI-Agents-that-Work-Together-to-Drive-Revenue-for-Consumer-Brands (2026-06-30)
66. K:BOS 2026 demonstrates Klaviyo's marketing-service flywheel for autonomous B2C CRM. Info-Tech Research Group. https://www.infotech.com/software-reviews/vendor-technology-notes/k-bos-2026-demonstrates-klaviyo-s-marketing-service-flywheel-for-autonomous-b2c-crm (2026-09)
67. Klaviyo MCP server. Klaviyo Developers. https://developers.klaviyo.com/en/docs/klaviyo_mcp_server (2026)
68. Klaviyo OpenAPI specification, revision 2026-07-15. Klaviyo on GitHub. https://github.com/klaviyo/openapi (2026-07-15, read directly)
69. klaviyo-api-python CHANGELOG (SDK 24.0.0). Klaviyo on GitHub. https://github.com/klaviyo/klaviyo-api-python (2026-07-15, read directly)
70. Understanding Klaviyo's predictive analytics. Klaviyo Help Center. https://help.klaviyo.com/hc/en-us/articles/360020919731 (ongoing)
71. Analyze signup form performance. Klaviyo Help Center. https://help.klaviyo.com/hc/en-us/articles/360015960712 (ongoing)
72. Introducing Klaviyo WhatsApp. Klaviyo. https://www.klaviyo.com/blog/klaviyo-whatsapp-product-launch (2025)
73. Klaviyo pricing in 2026. Kanal. https://getkanal.com/blog/klaviyo-pricing (2026-10)
74. Braze accelerates AI innovation, empowering marketers to treat every customer like their only customer. Braze. https://www.braze.com/press-releases/braze-accelerates-ai-innovation-empowering-marketers-to-treat-every-customer-like-their-only-customer (2026-09-29)
75. Braze completes acquisition of OfferFit. Braze. https://www.braze.com/press-releases/braze-completes-acquisition-of-offerfit (2025-06)
76. Customer.io MCP: why we rebuilt it around one agent. Customer.io. https://customer.io/learn/how-we-work/customer-io-mcp-connector (2026-05)
77. Customer.io MCP: get started. Customer.io Docs. https://docs.customer.io/ai/mcp/get-started/ (2026)
78. Iterable unveils Nova Agent and a new wave of AI innovations. Business Wire. https://www.businesswire.com/news/home/20260422200702/en/Iterable-Unveils-Nova-Agent-and-a-New-Wave-of-AI-Innovations-to-Power-Real-Time-Personalization-and-Predictable-Growth (2026-04-22)
79. Iterable MCP server (v1.9.0). Iterable on GitHub. https://github.com/Iterable/mcp-server (2026, read directly)
80. Intuit Mailchimp launches Analytics AI. Intuit. https://investors.intuit.com/_assets/_6a9ee074199c0a511699c988d19108db/intuit/news/2026-05-28_Intuit_Mailchimp_Launches_Analytics_AI_and_1313.pdf (2026-05-28)
81. What's new July 2026. Omnisend Help Center. https://support.omnisend.com/en/articles/15700809-what-s-new-july-2026 (2026-07)
82. Attentive unveils next generation of agentic AI marketing innovation at Thread 2026. Business Wire. https://www.businesswire.com/news/home/20260526090213/en/Attentive-Unveils-Next-Generation-of-Agentic-AI-Marketing-Innovation-at-Thread-2026 (2026-05-26)
83. Q2 2026: what's new. Postscript Help Center. https://help.postscript.io/en/articles/14855933-q2-2026-what-s-new (2026)
84. With HubSpot Score retiring, how to set up lead scoring in HubSpot. Six and Flow. https://www.sixandflow.com/marketing-blog/with-hubspot-score-retiring-where-is-lead-scoring-in-hubspot (2025)
85. HubSpot AI in 2026: the complete guide. SwyftRev. https://swyftrev.com/hubspot-ai-in-2026-the-complete-guide/ (2026)
86. 2026 email marketing benchmarks by industry. Klaviyo. https://www.klaviyo.com/products/email-marketing/benchmarks (2026)
87. Email marketing benchmarks 2026. Klaviyo UK. https://www.klaviyo.com/uk/blog/email-marketing-benchmarks-open-click-and-conversion-rates (2026)
88. Omnisend's 2026 ecommerce marketing report. Omnisend. https://www.omnisend.com/resources/reports/2026-ecommerce-marketing-report/ (2026)
89. SMS marketing benchmarks 2026: campaigns vs automations. Omnisend. https://www.omnisend.com/blog/sms-marketing-benchmarks/ (2026)
90. Recharge welcomes Skio to build the future of subscription commerce. Recharge. https://getrecharge.com/blog/recharge-welcomes-skio-to-build-the-future-of-subscription-commerce/ (2026-04-30)
91. The best teams in subscriptions, together. Skio. https://skio.com/blog/skio-is-now-part-of-recharge (2026-04)
92. LoyaltyLion launches AI Campaigns. LoyaltyLion via Yahoo Finance UK. https://uk.finance.yahoo.com/news/loyaltylion-launches-ai-campaigns-help-120000661.html (2026-01)
93. Product updates. LoyaltyLion. https://loyaltylion.com/platform/product-updates (2026)
94. Smile News Center. Smile.io. https://news.smile.io/ (2026)
95. Google to disable Customer Match uploads in Ads API. Search Engine Land. https://searchengineland.com/google-to-disable-customer-match-uploads-in-ads-api-470796 (2026)
96. Manage customer lists. Google Ads API documentation. https://developers.google.com/google-ads/api/docs/remarketing/audience-segments/customer-match/manage (2026)
97. Restrictions on customer list custom audiences. Jon Loomer Digital. https://www.jonloomer.com/restrictions-on-customer-list-custom-audiences/ (2025)
98. Meta's new exclusion-only audiences. Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/meta-exclusion-only-audiences-ecommerce-2026 (2026-08)
99. Repeat purchase rate benchmarks: 18.8% across 156K customers. BS and Co. https://bsandco.us/blog-post/repeat-purchase-rate-benchmarks (2026)
100. Average ecommerce time to second purchase by vertical (2026). eightx. https://eightx.co/blog/average-ecommerce-time-to-second-purchase-by-vertical-2026 (2026)
101. PyMC-Marketing customer lifetime value models. PyMC Labs. https://www.pymc-marketing.io/ (ongoing)
