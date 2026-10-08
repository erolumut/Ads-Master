# Tag Management and Server-Side

How to choose and run the collection architecture: GTM web, server-side GTM (sGTM), Google tag gateway for advertisers, direct server-to-server events and CDPs, plus what browsers and ad blockers do to client-side data in 2026.

## 1. Architecture options

| Option | What it is | Pros | Cons | Fits |
|--------|-----------|------|------|------|
| A. Native integrations | Shopify Google and YouTube app, Meta Facebook and Instagram app (with CAPI), TikTok app, platform plugins for WooCommerce | Fast, maintained by vendors, CAPI included | Limited control, black box dedup, values fixed | Starter, Shopify Growth |
| B. gtag in code | Google tag snippet and gtag() calls | Simple, no container | Every change is a code deploy | Small custom sites, Next.js with dev team |
| C. GTM web | Container in the page, data layer driven | Marketer control, versioning, consent checks | Client-side loss (blockers, ITP, consent) | Most sites |
| D. GTM web plus Google tag gateway | Google tags served from your own domain path via CDN (Cloudflare, Google Cloud load balancer) | First-party serving for Google tags, low effort | Google tags only; not a blocker bypass; consent still required | Growth and above using Google heavily |
| E. GTM web plus sGTM | Browser sends one stream to your server container (first-party subdomain or path), which fans out to GA4, Google Ads, Meta CAPI, TikTok, others | Control over data sent, enrichment, longer-lived server cookies, fewer third-party scripts | Hosting cost, ops skill, still needs consent | Growth (selective), Scale, Enterprise |
| F. Direct server-to-server | Backend sends events (order webhooks, CRM changes) to CAPIs, Measurement Protocol, Data Manager API | Highest completeness for purchases and offline events | No browser context unless you capture it (fbp, fbc, client_id, user agent, IP) | Purchases, subscriptions, offline stages |
| G. CDP or event pipeline | Segment, RudderStack, Snowplow, mParticle, Hightouch events | One tracking plan, many destinations, warehouse native | Cost, vendor lock in, destination quirks | Scale, Enterprise, product-led SaaS |

Default stack by tier:
- Starter: A or C, plus one CAPI via native integration.
- Growth: C plus D, CAPI via native app or a managed sGTM (Stape or similar), purchases also sent server-side.
- Scale: C plus E (sGTM on first-party path), F for purchases and offline, BigQuery.
- Enterprise: E or G with data contracts, F everywhere, monitoring SLAs.

## 2. GTM web container standards

1. Naming: `<Type> | <Platform> | <Event> | <Detail>`, for example `Tag | GA4 | purchase`, `Trigger | CE | purchase`, `Var | DLV | ecommerce.transaction_id`.
2. Folders by platform. Workspaces per change. Version name and notes on every publish: what, why, ticket, tester.
3. Environments: use GTM environments (Live, Staging) so staging uses a separate container snippet.
4. Consent: enable "Consent Overview" in container settings. Set consent defaults with a CMP template on the Consent Initialization (All Pages) trigger. Google tags have built-in consent checks; for non-Google tags set "Require additional consent for tag to fire" (ad_storage for ad pixels, analytics_storage for analytics).
5. Triggers fire on data layer custom events (`purchase`, `generate_lead`), not on clicks or page URL patterns, wherever the site can push events.
6. Clear the ecommerce object before each ecommerce push: `dataLayer.push({ ecommerce: null });`.
7. Use one Google tag (configuration) and Google Analytics event tags; set shared parameters (user_id, page type) in the Google tag configuration settings.
8. Preview with Tag Assistant on staging and production before every publish. Test with consent granted and denied.
9. Access: Publish permission limited to 1 to 2 people; agents never publish without approval.
10. Quarterly cleanup: remove paused tags, unused variables, old vendors (each extra script costs speed and data leakage risk).

## 3. Server-side GTM (sGTM)

### How it works

Browser (GTM web or gtag) sends events to `https://example.com/metrics` (same-origin path) or `https://sgtm.example.com` (subdomain). The server container's Clients parse requests (GA4 client, Data client for custom streams, Measurement Protocol client), create event data, and Tags send to destinations (GA4, Google Ads conversion tracking and remarketing, Floodlight, Meta CAPI, TikTok Events API, LinkedIn CAPI, Pinterest, Snap, Reddit, Microsoft, webhooks, BigQuery).

### Hosting options

| Hosting | Notes | Cost logic |
|---------|-------|-----------|
| Google Cloud Run (Google's recommended path for new setups) | Automatic provisioning from GTM or manual deploy of the tagging server image; set minimum instances so there is no cold start loss; separate preview server | Pay per vCPU and memory time; a production setup typically runs 2 or more instances [verify current guidance in Google's sGTM Cloud Run docs] |
| App Engine | Legacy automatic provisioning | Prefer Cloud Run for new builds |
| Stape | Managed sGTM hosting with add-ons (custom loader, cookie keeper, own CDN, logs, Meta CAPI Gateway hosting, Google tag gateway integration) | Request-based plans with a free tier [check stape.io pricing] |
| Other managed hosts | Addingwell, TAGGRS and similar | Compare request pricing, EU hosting, logs, support |
| Self-hosted Docker or Kubernetes | Full control | Ops burden |

Choose EU or local region hosting when data residency matters (GDPR, KVKK). Document the processor in the CMP vendor list and DPA register.

### Domain choice and Safari

- Same-origin path (example.com/metrics routed by your CDN or load balancer to the tagging server) is the strongest option: cookies are first-party and share the site's IP space.
- Subdomain (sgtm.example.com) with an A or CNAME record pointing to a different IP range: Safari ITP caps cookies set by servers whose IP address differs significantly from the main site (third-party IP protection, 2020 to 2022 WebKit changes) to 7 days, which defeats the purpose of server-set cookies [Official WebKit behavior; verify current rules on webkit.org].
- Managed hosts offer "same origin" or "own CDN" features to address this. Check the response headers and cookie expiry in Safari before claiming the benefit.

### Server-side cookies

- GA4 client "Server managed" cookie mode (FPID) sets an HttpOnly first-party cookie from the server. If you switch from JavaScript managed _ga to FPID, plan the migration so existing users are not counted as new (GA4 client migration option).
- Meta: set fbp and fbc server-side or keep the pixel's first-party cookies; pass them on CAPI events.
- Never use server cookies to circumvent a user's consent choice. The consent state must travel with the event (Google consent mode parameters in the GA4 request; your own consent flag for other vendors).

### sGTM build steps

1. Create the server container in GTM; choose automatic Cloud Run provisioning or a managed host.
2. Map the custom domain (path or subdomain) and TLS.
3. In the web container Google tag, set `server_container_url` to the tagging server URL (or the gateway path).
4. Add Clients: GA4 (default), plus any vendor client templates you need.
5. Add Tags: GA4, Google Ads conversion (server), Google Ads remarketing, Conversion Linker (server) where needed, Meta CAPI (official Meta template or community template), TikTok Events API, others from the Community Template Gallery. Prefer templates published by the platform or widely used, and read the template code: templates run with permissions you grant.
6. Enrichment: Firestore or Google Sheets lookups (margin by SKU, customer status), hashing of user data, IP and user agent forwarding.
7. Consent: read consent from the incoming event (gcs and gcd parameters for Google) or a custom field; block non-Google tags when ad consent is denied.
8. Preview with the server container debug view, then platform test tools (Meta Test Events code, TikTok test event code).
9. Monitor: Cloud Logging error rate, request counts per client, outgoing HTTP status codes per tag, latency, instance count.

## 4. Google tag gateway for advertisers

Facts (from Google and Cloudflare documentation and release notes, via search extracts):
- First-party mode was renamed Google tag gateway for advertisers in May 2025 and made available broadly, supporting client-side and server-side tags [Official, 2025-05].
- Cloudflare one-click integration announced 2025-05-08; free to use and does not count toward other Cloudflare product billing [Official, 2025-05].
- Google Cloud route using a Global external Application Load Balancer: beta 2026-01-05, generally available 2026-06-01 per Tag Manager release notes [Official, 2026-06; via search extract].
- Setup from GTM, Google Ads or GA4: Google detects the CDN, you grant permissions (Cloudflare roles Super Administrator, Administrator or Zaraz Admin, or Domain Administrator on domain scoped roles), pick domains and a measurement path (default is a random four character path).
- Statuses include "First-party" (active) and "Pending" (enabled, no diagnostics yet).
- Manual legacy setup on Cloudflare (CNAME plus Origin and Transform rules) requires Enterprise; the in-UI setup does not [Contested across sources; check your plan].

What it does and does not do:

| It does | It does not |
|---------|-------------|
| Serve Google tag scripts and measurement requests from your own domain path | Bypass consent; consent mode still governs behavior |
| Improve resilience against some third-party script restrictions | Guarantee bypass of ad blockers (some lists still match) |
| Work alongside sGTM (the gateway can front the server container) | Proxy Meta, TikTok or other vendors' tags |

Known issue: one-click CDN injection can change load order between gtm.js and the CMP stub, causing late consent signals. Verify that the consent default still fires first after enabling [Practitioner reports, 2025 to 2026].

Verify: Network tab shows requests to your domain path; Application tab shows first-party cookies; the Google tag gateway status in GTM reads First-party.

## 5. First-party data collection

| Asset | How to collect | Use |
|-------|---------------|-----|
| Email and phone | Checkout, lead forms, login, newsletter | Enhanced conversions, CAPI match keys, Customer Match (with consent) |
| user_id | Logged-in users; hashed or internal ID | GA4 user_id, external_id on Meta and TikTok |
| Click IDs | Landing URL parameters, stored first-party | Offline uploads, match keys |
| client_id and session_id | _ga cookie and GA4 session cookie | Measurement Protocol stitching |
| fbp and fbc | Meta pixel cookies or server-set | Meta CAPI match keys |
| Consent state | CMP | Must travel with every event |
| Zero-party data | Quizzes, surveys | Segmentation, LTV signals |

Store identifiers in the backend order or CRM record at the moment of conversion. Without that, server events cannot be matched later.

## 6. Browsers, ad blockers and cookies in 2026

| Factor | Current state | Effect on measurement |
|--------|---------------|----------------------|
| Chrome third-party cookies | Google decided in April 2025 not to launch a new user choice prompt and to keep third-party cookies under existing settings; Privacy Sandbox APIs (Topics, Protected Audience, Attribution Reporting, Private Aggregation, Shared Storage, IP Protection, Related Website Sets and others) announced for retirement in October 2025, with deprecation from Chrome 144 (January 2026) and removal targeted for Chrome 150 (July 2026). CHIPS, FedCM and Private State Tokens remain [Official, 2025-10; removal status: check Chrome release notes] | No cookieless cliff in Chrome; do not build on Attribution Reporting API; Incognito still blocks third-party cookies by default |
| Safari ITP | Script-written first-party cookies capped at 7 days, and 24 hours when the landing URL carries tracking parameters from a known tracker domain; CNAME and IP mismatch protections cap server cookies from differing IPs | Returning user and long-lag conversions under counted on iOS and macOS Safari; same-origin collection helps |
| Safari Link Tracking Protection | Strips known click IDs (for example gclid, fbclid, msclkid) in Private Browsing and in links opened from Mail and Messages since Safari 17 (2023) | Lost click IDs; enhanced conversions and CAPI user data compensate; Safari 26 (2025) extended fingerprinting protection [Unverified scope] |
| Firefox | Total Cookie Protection by default; query parameter stripping in strict mode | Smaller share, similar effects |
| Brave and blockers | uBlock Origin, AdGuard, Brave Shields block GA4, Meta, TikTok scripts on many lists; Chrome's Manifest V3 limited some extensions (uBlock Origin Lite) | Client-side loss concentrated in tech-savvy and desktop audiences; server-side purchase events recover it |
| Consent | Opt-in regimes in EEA, UK, Switzerland, Turkey; opt-out regimes in US states | See [Consent and privacy](consent-and-privacy.md) |

Quantify your own loss: compare backend orders to browser purchase events by browser family and device. That number, not a generic benchmark, justifies sGTM or CAPI investment.

## 7. Choosing between Google tag gateway, managed sGTM and full sGTM

```
Is Google (GA4, Google Ads) your main spend and measurement?
  yes -> Enable Google tag gateway (low effort). Continue.
Do you run Meta, TikTok or other platforms at Growth tier or above?
  yes -> Need server events for them:
    Shopify? -> Native apps with CAPI (Meta Facebook and Instagram app "Maximum" data sharing, TikTok app) first; add sGTM only for gaps or control.
    Custom or WooCommerce? -> Managed sGTM (Stape or similar) with Meta and TikTok templates, or backend direct sender (recipe in implementation-recipes.md).
Do you need enrichment (profit values, customer status), central consent enforcement, or to reduce third-party scripts?
  yes -> Full sGTM on same-origin path with Firestore lookups.
Spend over $300k per month or strict data residency?
  yes -> sGTM in your own cloud project, EU or local region, with SLAs and logging.
```

## 8. Change management and rollback

- Every GTM publish: version name `YYYY-MM-DD <change>`, notes with ticket and tester, screenshot of preview results.
- Keep the previous version number in the change list as rollback target.
- After publishing: watch real-time reports, platform test events and sGTM logs for 60 minutes; run the 24-hour and 7-day reconciliation.
- Freeze periods: no tracking changes during peak sales days (Black Friday week, key launches) unless fixing a break.
- Log every publish in the journal with tag "change" so channel agents can explain movement.
