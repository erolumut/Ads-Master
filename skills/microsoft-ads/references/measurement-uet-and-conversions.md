# Measurement: UET, Consent Mode and Conversions

> Scope: UET tag, conversion goals, consent mode (basic and Advanced Consent Mode), enhanced conversions, offline conversions by MSCLKID, Conversions API, attribution, Clarity and CRM integrations. Implementation is owned by the measurement agent; this module defines what Microsoft Ads needs and how to verify it. Code samples are patterns to verify against current Microsoft documentation before deployment.

## 1. Measurement architecture

```
Browser: UET tag (bat.bing.com) --- consent state (ad_storage) --- enhanced conversions (hashed pid)
Server:  Conversions API (beta, per account)  --- shared eventId dedupes with UET
CRM:     MSCLKID stored on lead -> offline conversion import (90 day click window)
         or hashed email or phone -> enhanced conversions for leads (no click ID)
Analysis: Clarity (session behavior, AI referral visibility), backend revenue, data-driven attribution
```

## 2. UET tag

Install:
1. Create one UET tag per website in Tools > UET tag.
2. Deploy on every page via GTM (official Microsoft UET template), the site platform integration (Shopify and others), or the base code in the head.
3. Fire custom events for conversions; avoid destination URL goals on single page apps.
4. Verify with UET Tag Helper (browser extension) and the network tab: requests to bat.bing.com with the tag ID.

Event pattern (verify parameter names in current docs):
```javascript
// Purchase with dynamic revenue
window.uetq = window.uetq || [];
window.uetq.push('event', 'purchase', {
  'revenue_value': 129.90,
  'currency': 'USD'
});

// Lead
window.uetq.push('event', 'submit_lead_form', {});
```

Goal types: destination URL, duration, pages per visit, custom event, app install, offline (imported), and others by market. Prefer custom events for purchases and leads.

### Conversion goal settings checklist
| Setting | Recommended | Why |
|---------|-------------|-----|
| Goal category | Purchase, lead, signup and so on | NCA and some features require the purchase category |
| Include in conversions | On only for goals bidding should optimize | Micro goals in this column distort automated bidding |
| Count | All for purchases, unique for leads | Prevents double counted leads |
| Revenue | Dynamic for ecommerce; static value per lead stage for lead gen | Value bidding needs values |
| Conversion window | Match sales cycle; 30 days default for most, longer for B2B | Short windows undercount long cycles |
| View-through window | Short (1 day) for Audience campaigns unless tested | Reduces credit for passive exposure |
| Attribution model | Last click or data-driven (available to all since 2026-05) | Coordinate changes with measurement [Official, 2026-05] |

## 3. UET consent mode

Requirement: advertisers with users in the EEA, UK and Switzerland must provide consent signals through UET consent mode. Notice sent 2025-03-17; deadline 2025-05-05 [Official, 2025-03]. The requirement follows where users are located, not where the business is registered. Non compliance can disable conversion tracking and remarketing for those users, and accounts have received notices citing the Microsoft Advertising Agreement [Official, 2025-03] [Practitioner consensus].

Signal: a single parameter `ad_storage` with values granted or denied. When denied, UET does not read or write first-party cookies and does not write third-party cookies (third-party cookies may be read for fraud and spam prevention only) [Official, 2025-03].

Pattern (verify against current docs):
```javascript
window.uetq = window.uetq || [];
// Default must be set before the consent banner can update it
window.uetq.push('consent', 'default', { 'ad_storage': 'denied' });

// After the user accepts marketing cookies
window.uetq.push('consent', 'update', { 'ad_storage': 'granted' });
```

Some third party guides mention an `ad_user_data` parameter for Microsoft; Microsoft's announcement and FAQ describe `ad_storage` only [Contested]. Follow the current Microsoft FAQ.

### Advanced Consent Mode (ACM)
Microsoft published ACM guidance on 2026-02-19 [Official, 2026-02]:
- UET must load before the CMP so it can read the default denied state. If the CMP blocks UET entirely before consent, ACM cannot work.
- With GTM: use the official UET template on all pages; the GTM container loads before the CMP.
- Without GTM: place UET above the CMP script and set the default to denied.
- When denied, UET sends cookieless pings; Microsoft describes modeling from aggregate trends to fill measurement gaps.

Modeled conversions for consent mode launched 2025-08 for eligible advertisers in the EEA, Switzerland and Great Britain [Official, 2025-08]. Sources disagree on whether modeling needs ACM, applies by default, or applies at all to denied users [Contested]. Treat modeled conversions as an estimate, and check which goals show modeled data in your account.

### Verification test (run after any CMP or tag change)
1. Open the site in a private window from an EEA IP or with the CMP forced to show.
2. Network tab, filter `bat.bing.com`. Before consent, requests should carry `asc=D` (denied, cookieless).
3. Accept marketing cookies. Subsequent requests should carry `asc=G` (granted).
4. Reject in a new session; requests stay `asc=D` and no `_uetsid` or `_uetvid` cookies are set.
5. Record results in MEASUREMENT.md via the measurement agent.

## 4. Enhanced conversions (online)
- Opt-in per conversion goal; launched as beta 2024-02, recommended by Microsoft [Official, 2024-02].
- Sends hashed email or phone with the conversion to improve matching.
- Pattern (verify in docs):
```javascript
window.uetq = window.uetq || [];
window.uetq.push('set', { 'pid': {
  'em': 'customer@example.com',   // UET can hash; or send a SHA-256 hash
  'ph': '+14255550100'           // E.164 format
}});
```
- Hashing rules from the Conversions API guide: trim whitespace, remove dots from the local part, strip +alias, lowercase, SHA-256, lowercase hex [Official, 2026-08]. Note these are Microsoft specific normalization rules; dot removal differs from some other platforms.
- Only send when consent and privacy policy allow.

## 5. Offline conversions (lead gen and B2B)

Click ID route:
1. Auto-tagging on (MSCLKID appended to landing URLs).
2. Site captures `msclkid` from the URL, stores it in a first-party cookie (90 days), and writes it to a hidden form field.
3. CRM stores MSCLKID on the lead and keeps it when the lead converts to opportunity and customer.
4. Create an Offline conversion goal for each stage (for example SQL, Opportunity, Closed won) with values.
5. Wait about 2 hours after creating the goal before the first upload [Official, API docs].
6. Upload daily or at least weekly (UI file, scheduled upload, API `ApplyOfflineConversions`).
7. Only clicks from the last 90 days can be matched [Practitioner consensus from vendor docs]. Data can take several hours to appear. Duplicate uploads: the first instance is kept.

Upload file pattern (verify the template in the UI before use):
```
Parameters:TimeZone=+0000
Microsoft Click ID,Conversion Name,Conversion Time,Conversion Value,Conversion Currency
abcd1234efgh5678ijkl9012mnop3456,SQL,2026-10-01 14:05:00,500,USD
```

Silent failure causes: goal name mismatch, MSCLKID never reaches the CRM (redirects strip it, forms do not capture it), upload before the 2 hour wait, clicks older than 90 days, wrong time zone.

Enhanced conversions for leads (no click ID): upload hashed email or phone against the conversion when a click ID is unavailable (phone or email sales from web leads) [Practitioner consensus from vendor docs]. Use when MSCLKID capture rates are below 70%.

A 2026-08 trade headline mentioned a 7 day gate on offline conversion uploads, but a 2026-10-08 check found no such rule in Microsoft documentation [Unverified headline]. Documented rules: conversion time within the last 90 days and after the click (earlier timestamps are ignored), wait 2 hours after creating a new offline goal, duplicates with the same click ID, conversion name and time are imported once, reporting can lag up to 6 hours, and Microsoft recommends daily uploads because less frequent uploads can hurt automated bidding [Official, Microsoft Learn]. Upload daily regardless.

### Value mapping for lead gen
| Stage | Value logic |
|-------|-------------|
| MQL or lead | Lead to customer rate x average deal value x gross margin |
| SQL | SQL to customer rate x average deal value x gross margin |
| Opportunity | Opportunity win rate x deal value x margin |
| Closed won | Actual first year gross profit |

Bid to the deepest stage that has 30+ conversions in 30 days; use earlier stages until then.

## 6. Conversions API (CAPI)

Status: documentation published 2026-08 (Microsoft Learn), product in beta, enrolled per account by Microsoft through the account manager or support; no GA date announced [Official, 2026-08].

Key mechanics as documented:
| Item | Detail |
|------|--------|
| Endpoint | Server-side POST to a tag specific endpoint on capi.uet.microsoft.com |
| Auth | Bearer token tied to the UET tag that owns the conversion goals; token appears under the UET tag once enrolled |
| Dedupe | Same eventId on UET and CAPI events |
| Batch | Up to 1,000 events per request |
| Timing | eventTime required, within the last 7 days |
| Identifiers | At least one per event; email SHA-256 after Microsoft normalization; phone E.164 |
| Gotchas | Goals must exist first (events for tags without matching goals can return 200 and record nothing); revenue cannot be attached to a page load event |

Run CAPI alongside UET, never instead of it while in beta. Keep offline import as the fallback for CRM stages.

## 7. CRM integrations
- HubSpot: Microsoft's 2026-09-30 roundup calls the integration live (CRM audiences, automated lead follow-up, pipeline and revenue reporting), while HubSpot's knowledge base (updated 2026-09-01) still labels it a public beta for all hubs and tiers that a Super Admin opts into [Contested on status]. Setup facts from HubSpot docs: connect each Microsoft customer account separately (manager accounts cannot connect); the connecting user needs Publish access to HubSpot ads and Super Admin on the Microsoft account; HubSpot sets an account-level Final URL suffix and turns on MSCLKID auto-tagging; lifecycle stage changes become conversion events synced to a selected Microsoft UET tag; no ad creation yet [Official, HubSpot Knowledge Base 2026-09]. Check the account-level suffix against existing tracking templates before connecting.
- Salesforce and others: use offline conversion import (MSCLKID) or a connector.
- Always keep MSCLKID as a dedicated CRM field even with an integration.

## 8. Clarity
- Link a Clarity project to see session recordings and heatmaps for paid traffic; use for CRO handoffs.
- Clarity added AI Visibility reporting (Topic Insights, grounding queries, citation share, Share of Authority) on 2026-08-12 [Official, 2026-08]; this belongs to ai-search-optimization but helps explain Copilot driven demand.
- Official Clarity MCP server exists (github.com/microsoft/clarity-mcp-server) for pulling Clarity data into Claude.

## 9. Measurement health KPIs
| Check | Healthy | Frequency |
|-------|---------|-----------|
| Primary goal recording | Conversions in last 7 days | Daily |
| MSCLKID capture rate | Leads with MSCLKID / leads from Microsoft paid sessions over 85% | Monthly |
| Offline upload success | Matched rows / uploaded rows over 90% | Each upload |
| Consent test | asc=D before, asc=G after acceptance | After each CMP or tag change, monthly otherwise |
| Platform vs backend | Microsoft conversions within 10% to 25% of backend attributed | Monthly |
| Duplicate rate | Duplicate orders under 2% | Monthly |
