# Measurement: Pixel, Conversions API, Attribution and Incrementality

> Knowledge as of 2026-10. Boundary: this module covers Meta-specific signal setup and how to read Meta numbers. Cross-channel tracking architecture (GA4, GTM, consent mode, server-side containers, MMM, dashboards) is owned by `measurement`. When a fix requires code, tag manager or consent changes, write the spec here and hand it off.

## 1. The Meta signal stack

| Component | What it is | Status check |
|-----------|-----------|--------------|
| Dataset | Container in Events Manager for website, app, offline and messaging events (the Pixel ID is the dataset ID) | One per brand or site; shared to all relevant ad accounts |
| Meta Pixel | Browser JavaScript events | Pixel Helper, Events Manager Test events |
| Conversions API (CAPI) | Server-to-server events | Events Manager, Overview: "Received from" shows Browser and Server |
| Partner integrations | Shopify, WooCommerce, BigCommerce, Wix, Squarespace, Magento and others; GTM server-side; Stape and similar hosts | Confirm "Maximum" data sharing level where offered (Shopify) |
| Conversions API Gateway | Meta-provided gateway you host in your own cloud (AWS or GCP) or via a partner; mirrors Pixel events server-side | Gateway health in Events Manager |
| Signals Gateway | Meta first-party data pipeline (2024) that routes events to Meta and other destinations | Optional; for complex stacks |
| App events | Meta SDK or MMP (AppsFlyer, Adjust, Branch, Singular, Kochava) | Events Manager app dataset; SKAdNetwork configuration |
| Offline / CRM events | Conversions API with action_source physical_store or system_generated; the separate Offline Conversions API was discontinued in May 2025 with the expiry of Graph API v16.0, the last version supporting offline event sets [Official, Graph API changelog v20.0] | Offline events visible in dataset |
| Business messaging events | Conversions API for business messaging (events from Messenger, Instagram, WhatsApp chats) | Needed to optimize chats for leads or purchases |

## 2. Implementation standard (what "done" looks like)

| Requirement | Target | How to verify |
|-------------|--------|---------------|
| Key events on both Pixel and CAPI | PageView, ViewContent, AddToCart, InitiateCheckout, Purchase (ecommerce); Lead, CompleteRegistration, Schedule, custom qualified events (lead gen) | Events Manager event list shows Browser and Server per event |
| Deduplication | Same `event_name` and identical `event_id` on browser and server versions, sent within 48 hours | Events Manager deduplication status; "Event coverage" for server vs browser |
| Event Match Quality (EMQ) | Purchase and Lead 7+ out of 10; 8+ for Scale tier [Practitioner consensus] | Events Manager, event details, EMQ |
| Customer information parameters | em, ph, external_id, fn, ln, ct, st, zp, country (hashed SHA-256), plus fbp, fbc, client_ip_address, client_user_agent (not hashed) | Payload inspection in Test events |
| Value and currency | Every Purchase (and valued Lead) has numeric `value` and ISO `currency` | Events Manager event parameters |
| content_ids match catalog | For catalog ads, content_ids equal catalog item IDs | Commerce Manager, Events data sources, match rate |
| Freshness | Server events sent in real time or within 1 hour | Data freshness indicator |
| Consent | Events sent only under valid consent where required (EU, UK, Turkey KVKK); Limited Data Use for US states where applicable | `measurement` audit |

CAPI payload example (server, Purchase):
```json
{
  "data": [{
    "event_name": "Purchase",
    "event_time": 1791446400,
    "event_id": "order_100234",
    "action_source": "website",
    "event_source_url": "https://example.com/checkout/thank-you",
    "user_data": {
      "em": ["<sha256 of lowercase trimmed email>"],
      "ph": ["<sha256 of E.164 digits>"],
      "external_id": ["<sha256 of customer id>"],
      "client_ip_address": "203.0.113.10",
      "client_user_agent": "Mozilla/5.0 ...",
      "fbp": "fb.1.1791440000000.1234567890",
      "fbc": "fb.1.1791440000000.IwAR..."
    },
    "custom_data": { "currency": "USD", "value": 129.00, "content_ids": ["SKU123"], "content_type": "product", "num_items": 1 }
  }]
}
```
The browser Pixel must fire `fbq('track', 'Purchase', {...}, {eventID: 'order_100234'})` with the same ID.

## 3. Aggregated Event Measurement (AEM) status

- AEM was introduced in 2021 for iOS 14.5+ with an 8-event prioritization per domain and domain verification.
- In 2025 Meta removed the requirement to configure and rank events in AEM and the 8-event limit, processing iOS web events automatically [Unverified exact date; verify in Events Manager]. Domain verification remains good practice for brand ownership and link editing permissions.
- Practical stance: do not spend time on AEM event ranking unless Events Manager still shows the configuration for the account. Focus on CAPI quality.

## 4. Attribution settings and 2026 changes

| Date | Change | Impact | Label |
|------|--------|--------|-------|
| 2021 | Default 7-day click and 1-day view; 28-day windows removed from default | Lower reported conversions vs pre-2021 | [Official, 2021] |
| 2025 | Incremental attribution model option launched in Ads Manager | Optimization and reporting toward incremental conversions | [Official, 2025] |
| 2025-10 announcement, 2026-01-12 effective | Ads Insights API stopped returning 7-day view and 28-day view windows; requests return empty data; historical queries with those windows cannot be regenerated | Broken BI pipelines; lower view-through totals in reports | [Official, 2025-10 developer blog via secondary] |
| 2026-03-03 | Click-through attribution counts only link clicks (to website, lead form, app, Messenger). Other interactions (likes, shares, saves, comments, profile taps, expansions, 5s+ video views) moved to engage-through attribution with a 1-day window; engaged-view video threshold lowered from 10s to 5s | Click-through conversions fell (vendors report 15 to 40% in some accounts); totals shift to engage-through | [Official, 2026-03 via trade coverage; impact figures Unverified] |

Reporting standard after March 2026:
1. Default reporting columns: 7-day click, 1-day view, 1-day engage-through, plus "Compare attribution settings" columns for 1-day click and incremental.
2. Compare any conversion drop against 2026-01-12 and 2026-03-03 before concluding performance changed.
3. Note in ads-master/MEASUREMENT.md which setting each campaign optimizes on; optimization and reporting windows can differ.
4. For BI pipelines: request `action_attribution_windows` of `1d_click`, `7d_click`, `1d_view` (and engage-through where the API exposes it). Remove `7d_view` and `28d_view`.

Choosing the optimization attribution setting:
| Situation | Setting |
|-----------|---------|
| Default ecommerce, impulse to medium consideration | 7-day click + 1-day view (+ engage-through default) |
| View-through looks inflated (high existing customer share, retargeting heavy, low incrementality in tests) | 7-day click only, or 1-day click |
| Very short cycle (food delivery, apps with instant conversion) | 1-day click |
| Mature account with stable tracking, want true lift | Incremental attribution (test first) |

## 5. Reading platform ROAS versus incrementality

Three lenses, used together:
| Lens | Question | Source | Cadence |
|------|----------|--------|---------|
| Platform attributed | What did Meta's model credit? | Ads Manager | Daily to weekly |
| Business outcome | Did total revenue, new customers and MER move? | Backend, Shopify, CRM; `measurement` dashboards | Weekly |
| Causal | What would have happened without Meta spend? | Conversion Lift, GeoLift, holdouts, MMM | Quarterly |

Rules:
1. Never compare platform ROAS across channels as if comparable. Each platform over-credits itself differently.
2. Track MER (total revenue / total paid media) and new customer CAC (new customers / total spend) weekly. If Meta ROAS rises while MER and new customers are flat, suspect attribution, not performance.
3. Calibrate: after a lift test, compute incrementality factor = incremental conversions / platform-attributed conversions for the test period. Apply it to targets until the next test. Example: platform ROAS 4.0, factor 0.55, incremental ROAS 2.2; with breakeven ROAS 2.22 the campaign is at breakeven, not "4x".
4. Retargeting and existing customer-heavy campaigns usually have the lowest factors. Independent data: Cassandra reported incremental ROAS 1.90x for cold acquisition and 3.64x for retargeting against platform-reported 8x [Study, vendor, 2025 to 2026]; contexts differ, so test your own.
5. Record every test in ads-master/MEASUREMENT.md (Incrementality evidence table) and ads-master/EXPERIMENTS.md.

## 6. Incrementality tools on Meta

| Tool | Design | Requirements | Notes |
|------|--------|-------------|-------|
| Conversion Lift (Meta) | Randomized user-level holdout run by Meta | Eligibility varies; self-serve lift tests are available in Experiments for some accounts, others need a Meta rep; enough conversions for power | Gold standard for Meta-only lift; measures conversions captured by Meta's signal |
| Brand Lift | Polls exposed vs holdout | Reach thresholds | Awareness campaigns |
| GeoLift (open source, Meta) | Synthetic control on matched geographies with spend on/off or up/down | 20+ geo units preferred, stable sales data by geo, 3 to 6 weeks test | Measures business outcome (backend sales), works across channels; R package |
| Robyn (open source, Meta) | Marketing mix model with ridge regression, adstock and saturation, calibrated with lift tests | 2+ years of weekly data recommended, or 1 year daily | Strategic allocation; hand off build to `measurement` |
| A/B test (Experiments) | Split audiences between strategies | Budget per cell | Compares strategies, not absolute incrementality |
| Holdout by exclusion | Exclude a random customer list share from retargeting | CRM lists | Cheap retention incrementality check |

GeoLift quick design (spec for `measurement`):
1. Define KPI (backend orders or revenue by region per day), 1 to 2 years of history.
2. Run power analysis to choose treatment geos and test length (minimum detectable effect 5 to 10%).
3. Choose design: holdout (turn Meta off in treatment geos) or scale (raise spend 50 to 100%).
4. Lock other channels' changes during the test where possible.
5. Read lift, compute iROAS = incremental revenue / incremental spend, update incrementality factor.

## 7. Health, finance and other data restrictions

Accounts classified as health and wellness (from 2025) or in other restricted data categories may have lower funnel events, custom parameters and URL paths blocked [Official, 2025]. Effects: cannot optimize to Purchase or Lead in fully restricted cases, custom conversions on restricted URLs fail. See [policy module](policy-and-account-health.md) for the classification check, appeal and adaptation plan. Never rename restricted events to evade restrictions (policy violation risk).

## 8. Diagnostics: measurement issues that look like performance issues

| Symptom | Check | Likely cause |
|---------|-------|-------------|
| Conversions drop to near zero overnight | Events Manager last received, site deploy log, consent banner change | Pixel or CAPI broken, consent misconfig, domain change |
| Conversions doubled overnight | Deduplication status, event_id consistency | Dedup broken (browser and server counted twice) |
| ROAS down 20 to 40% from a specific date with stable backend revenue | Date vs 2026-01-12 or 2026-03-03, attribution columns | Attribution reporting change |
| Purchase value mismatch vs backend | Currency, tax and shipping inclusion, refunds | Value definition inconsistent |
| Catalog ads not delivering to retargeting | content_ids match rate | ID mismatch between events and feed |
| EMQ dropped | Payload parameters, hashing errors | Missing email or phone after checkout change |
| Health classification notice | Events Manager data source category | Restricted data category |

## 9. Insights API query for reconciliation (read only)

```bash
curl -G "https://graph.facebook.com/v{VERSION}/act_{AD_ACCOUNT_ID}/insights" \
  --data-urlencode "level=campaign" \
  --data-urlencode "time_increment=1" \
  --data-urlencode "date_preset=last_30d" \
  --data-urlencode "fields=campaign_id,campaign_name,spend,impressions,reach,frequency,actions,action_values,purchase_roas" \
  --data-urlencode 'action_attribution_windows=["1d_click","7d_click","1d_view"]' \
  --data-urlencode "access_token={TOKEN}"
```
Use the current Marketing API version from the changelog. Join daily results with backend orders by date to compute platform-to-backend ratios per week.
