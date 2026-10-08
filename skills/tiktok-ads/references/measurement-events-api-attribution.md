# Measurement: Pixel, Events API, Attribution and Triangulation

> Knowledge as of 2026-10. The measurement agent owns the tracking stack; this module tells the tiktok-ads agent what TikTok needs, how to verify it, and how to read TikTok numbers inside a triangulated setup. Trust `ads-master/MEASUREMENT.md` over platform numbers.

## 1. Signal stack

| Component | Purpose | Status check |
|-----------|---------|--------------|
| TikTok Pixel (browser) | Page and event tracking, _ttp cookie, ttclid capture | Events Manager shows recent events; TikTok Pixel Helper browser extension shows firing |
| Events API (server) | Server-side events with hashed identifiers; resilient to browser loss | Events Manager shows server events; diagnostics tab clean |
| Deduplication | Prevents counting the same event twice when pixel and server both send it | event_id present on both; dedup rate visible in Events Manager |
| Advanced matching | Hashed email and phone (and external ID) attached to events | Event match quality per event |
| First-party cookie setting | Lets the pixel use first-party cookies | Enabled in pixel settings [Unverified current label] |
| Catalog | Product IDs match content_id in events | Catalog diagnostics, match rate |
| MMP / SDK (apps) | App events, SKAdNetwork on iOS | MMP dashboard vs TikTok SAN |
| CRM events (lead gen) | Qualified stages sent back via Events API | Event counts by stage |
| UTMs | GA4 and BI triangulation | GA4 source/medium = tiktok / paid_social |

Recommended setup: Pixel plus Events API for every web advertiser, with event_id deduplication [Official]. On Shopify, the TikTok sales channel app offers data sharing levels; the highest level sends both pixel and server events [Unverified current level names]. GTM web plus server-side GTM templates for TikTok also exist; hand implementation to measurement.

## 2. Standard events and parameters

| Funnel step | Event (verify names in Events Manager) | Required parameters |
|-------------|----------------------------------------|--------------------|
| Product view | ViewContent | content_id, content_type, value, currency |
| Add to cart | AddToCart | content_id, quantity, value, currency |
| Checkout start | InitiateCheckout | value, currency |
| Payment info | AddPaymentInfo | value, currency |
| Purchase | CompletePayment (shown as Complete Payment; newer setups may label it Purchase) [Unverified naming] | value, currency, content_id list, order ID as event_id |
| Lead | SubmitForm / Contact / CompleteRegistration | value if lead values exist |
| Search | Search | query |
| Subscribe | Subscribe | value, currency |

Value rules: send the value the business optimizes on (revenue net of tax and shipping, or margin if the team agrees). Keep currency consistent. Never send zero or placeholder values on purchase events used for value-based bidding.

## 3. Deduplication rules [Official, help article updated 2025-05]

1. Deduplication is needed only when the same event type reaches TikTok through both pixel and Events API.
2. Use the same `event_id` on the pixel event and the server event (order ID for purchases is the best key).
3. If the server event has no `event_id` but TikTok receives the `_ttp` cookie value, TikTok attempts deduplication based on `_ttp`.
4. Windows: pixel-only duplicates and Events API-only duplicates are collapsed within 48 hours of the first event. For pixel plus Events API overlap, the article describes merging when the copy arrives after 5 minutes and within 48 hours of the first event. Behavior for copies arriving within 5 minutes is not stated; test it.
5. TikTok keeps the first event received for measurement and reporting.

Verification procedure:
1. Place a test order. In Events Manager, use Test Events to see both browser and server events with the same event_id.
2. Compare 7 days of TikTok-reported purchases (all attribution, not just ad-attributed if the view exists) to backend orders from TikTok-attributed sessions. A ratio near 2x indicates duplication.
3. Check the dedup rate or overlap indicator in Events Manager diagnostics.

## 4. Event match quality (EMQ)
- TikTok shows a per-event match quality score (0 to 10) in Events Manager [Practitioner reports; TikTok introduced EMQ around late 2024 per Triple Whale].
- Third-party guidance: above 7 is strong; below 5 means events arrive but cannot be tied to users; a single email identifier scores about 5 to 6 [Unverified, Journify]. Others warn not to chase 10/10 [Triple Whale].
- Improve by sending, hashed (SHA-256, normalized): email, phone (E.164), external_id; plus ttclid (from URL), _ttp cookie, IP and user agent from the server.

Events API payload skeleton (verify against the current Events API reference before use):

```json
{
  "event_source": "web",
  "event_source_id": "<PIXEL_ID>",
  "data": [{
    "event": "CompletePayment",
    "event_time": 1760000000,
    "event_id": "order_100234",
    "user": {
      "email": "<sha256 lowercase trimmed email>",
      "phone": "<sha256 E.164 phone>",
      "external_id": "<sha256 customer id>",
      "ttclid": "<from landing URL>",
      "ttp": "<_ttp cookie>",
      "ip": "<client ip>",
      "user_agent": "<client user agent>"
    },
    "properties": {
      "currency": "USD",
      "value": 89.00,
      "content_type": "product",
      "contents": [{"content_id": "SKU-123", "quantity": 1, "price": 89.00}]
    },
    "page": {"url": "https://example.com/checkout/thank-you"}
  }]
}
```

Endpoint pattern: `POST https://business-api.tiktok.com/open_api/v1.3/event/track/` with an `Access-Token` header [Unverified, confirm in API docs].

## 5. Attribution settings

| Setting | Current state | Label |
|---------|--------------|-------|
| Default web windows | 7-day click and 1-day view (default since Attribution Manager, 2022) | [Official, 2022-06] |
| Where set | Ad group level: Click-through attribution (CTA), Engaged view-through attribution (EVTA), View-through attribution (VTA) | [Official, 2025-02] |
| Options in the help article | CTA 1 or 7 days; EVTA 1 or 7 days; VTA off or 1 day | [Official, 2025-02] |
| Other options reported | Click 14 or 28 days, view 7 days, EVTA 28 days | [Contested] |
| EVTA definition | Conversion after a user watched at least 6 seconds (or the full ad if shorter than 6 s) without clicking, within the window (max 7 days per TikTok) | [Official] |
| EVTA prerequisite (app) | Advertiser must have transitioned to SAN | [Official] |
| Editable after launch | Sources disagree on whether attribution settings can change after an ad group goes live | [Contested] |
| Attribution Portfolio with assisted conversions | Reported May 2026 launch | [Unverified] |

Agent rules:
1. Record the attribution setting of every ad group in reports. Comparing ad groups with different windows is invalid.
2. Default for performance: 7-day click + 1-day view (or EVTA where available) for optimization; report click-only alongside it.
3. Never set targets from 7-day view numbers. They inflate ROAS [Practitioner consensus].
4. If budget underspends with view-through on, TikTok suggests turning view-through off [Official].
5. For Shop, GMV Max attribution is internal to TikTok and includes in-app paths; treat it as an upper bound until a holdout says otherwise.

## 6. UTM template

```
utm_source=tiktok&utm_medium=paid_social&utm_campaign=__CAMPAIGN_NAME__&utm_content=__CID_NAME__&utm_term=__AID_NAME__&ttc_cid=__CAMPAIGN_ID__&ttc_aid=__AID__&ttc_ad=__CID__
```

TikTok URL macros commonly documented: __CAMPAIGN_ID__, __CAMPAIGN_NAME__, __AID__ (ad group ID), __AID_NAME__ (ad group name), __CID__ (ad ID), __CID_NAME__ (ad name), __PLACEMENT__ [Unverified, confirm in the URL parameter builder]. Keep naming free of spaces and special characters so macros resolve cleanly.

## 7. Reading TikTok in a triangulated setup

TikTok is a demand creation channel with heavy view-driven and delayed effects. Last-click tools under-credit it; platform reporting over-credits it. Use a range.

| Lens | What it says | Bias |
|------|-------------|------|
| TikTok Ads Manager (7d click + 1d view or EVTA) | Platform-attributed conversions | Over-credits (view-through, overlap with other channels) |
| GA4 / last-click analytics | Sessions and conversions with tiktok / paid_social | Under-credits (no view-through, cross-device loss, in-app browser issues) |
| Post-purchase survey ("Where did you hear about us?") | Self-reported discovery | Recall bias, but catches TikTok discovery well |
| MER / blended CAC | Total revenue / total spend over time | Cannot isolate the channel without variation |
| Conversion Lift Study (TikTok) | User-level randomized holdout run by TikTok; needs rep and sufficient budget [Unverified minimums] | Run by the platform; methodology is sound but TikTok grades its own homework |
| Geo holdout / matched market test (independent) | Incrementality by region | Needs scale and 3 to 6 weeks |
| MMM | Long-run contribution incl. halo on Amazon, retail, search | Needs 2+ years of data or Bayesian priors; hand to measurement |

Calibration procedure:
1. Compute the ratio R1 = TikTok platform conversions / GA4 last-click TikTok conversions for the last 28 days.
2. Compute survey share: % of new customers citing TikTok x total new customers = survey-implied TikTok customers.
3. If a lift test exists, compute the incrementality factor: incremental conversions / platform conversions in the test period.
4. Planning credit = platform conversions x incrementality factor (if tested), otherwise use the midpoint between last-click and survey-implied counts, clearly labeled as an estimate.
5. Set in-platform targets from the planning credit (see bidding-and-budgets.md section 9).
6. Re-run when spend changes by more than 50% or creative mix shifts heavily.

Halo effects to watch: branded search volume (Google Search Console, Google Ads brand impressions), Amazon sales, retail sell-through, direct traffic. TikTok's GMV Max Spillover reporting claims to show sales on other channels where available [Unverified]. Treat any platform-reported halo as a hypothesis for a geo test.

## 8. Lift testing on TikTok

| Test | Run by | Use when |
|------|--------|---------|
| Conversion Lift Study | TikTok measurement team via rep | Spend is large enough for statistical power (ask the rep for the current minimum); you need a user-level read |
| Brand Lift Study | TikTok via rep, third-party survey partners | Awareness, consideration, ad recall |
| Split Test (Ads Manager) | Self-serve | Comparing two strategies (Smart+ vs manual, bid strategies, creative strategies) |
| Geo holdout | Measurement agent | Independent read, Shop and website blended effect |

Lift test design checklist: one primary KPI from backend data, pre-registered test and control regions or randomization, minimum detectable effect computed, duration fixed in advance, no other major changes in test regions, result logged in `ads-master/MEASUREMENT.md` Incrementality evidence and `ads-master/EXPERIMENTS.md`.

## 9. Measurement health checks (weekly)

| Check | Pass condition |
|-------|---------------|
| Event volume | No day with zero purchases or leads when spend > 0 |
| Pixel vs server overlap | Most purchase events arrive from both sources with matching event_id |
| Duplicate ratio | TikTok purchases (all) / backend orders from TikTok traffic within expected band, not near 2x |
| Value integrity | Average order value in TikTok within 10% of backend AOV |
| EMQ | Purchase EMQ stable or rising; no drop of 1+ point week over week |
| Catalog match | content_id match rate stable |
| UTMs | TikTok sessions visible in GA4 with correct source/medium |
| Consent (EEA/UK) | Pixel respects consent state; drops in event volume explained |

Any failure: write a journal alert and request a handoff to the measurement agent. Do not change bids while measurement is broken.
