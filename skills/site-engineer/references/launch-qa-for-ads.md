# Launch QA for Ads

> The gate between "the channel agent drafted it PAUSED" and "the human sets it live". Site-engineer checks the destination and the plumbing; the channel agent owns targeting, bids and creative; `measurement` owns event design; `compliance` owns claims; `offer-strategy` owns the offer. Knowledge as of 2026-10.

## 1. When launch QA runs

| Trigger | Scope |
|---------|-------|
| New campaign, ad set or ad group with new final URLs | Full launch QA (sections 3 to 7) |
| Final URL, URL parameters, tracking template or final URL suffix changed | Sections 3, 4 and 6 |
| Landing page released or changed while ads point at it | Sections 3, 4, 5 and the price check |
| Offer, price or stock change on an advertised product | Section 5 |
| Pixel, CAPI, GTM, consent or checkout change | Section 6 with `measurement` |
| Weekly on live top spend URLs (top 20 by spend) | Sections 3 and 5 (drift check) |

Inputs to request from the channel agent's change request: platform, account, entity IDs and names, status, budget, schedule, final URLs, URL parameters or suffix, tracking template, conversion goal or optimization event, pixel or dataset ID, and the ad copy with the offer and price claimed.

## 2. Verdicts

- PASS: every Critical and High item passes. The channel agent may present the change request for activation.
- PASS WITH NOTES: Medium items open with an owner and date.
- FAIL: any Critical or High item fails. Activation must not be proposed. Write the failure into the change request and the journal.

## 3. Destination checks (every final URL)

| # | Check | Pass rule | Severity | How |
|---|-------|-----------|----------|-----|
| D1 | Resolves | Final status 200 over HTTPS, no interstitial, no password page, no geo block for the targeted countries | Critical | [url_check.py](../scripts/url_check.py), browser with a VPN or proxy in the target country when geo logic exists |
| D2 | Redirects | At most 1 redirect hop; no meta refresh or JS redirect chains | High | `url_check.py` shows hops; Playwright redirect template |
| D3 | Parameters survive | Every `utm_*` and click ID present on the final URL after redirects, locale switches and consent banner interaction | Critical | `url_check.py --add-click-ids`; [UTM redirect test](automated-qa-and-tests.md) |
| D4 | Speed on mobile | Lab LCP under 2.5 s on a mid tier mobile profile; field LCP and INP good if CrUX data exists | High | Lighthouse mobile, PSI API |
| D5 | Right page | Language, currency and market match the targeting; the product or service in the ad is above the fold | Critical | Manual with screenshots per market |
| D6 | Offer and price match | Price, discount, free shipping threshold, bundle contents and dates on the page equal the ad and `brand/PRODUCT_FACTS.md`; terms visible | Critical | Side by side screenshot of ad preview and page |
| D7 | Stock | Advertised product or variants in stock above the stock guard in `GUARDRAILS.md` | Critical | Admin or feed availability; PDP add to cart works |
| D8 | Consent banner | Does not cover the primary CTA or price on a 390 x 844 viewport; dismissible; respects choices | High | Device check and screenshot |
| D9 | Conversion path works | Add to cart and checkout handoff, or form submit in test mode, on mobile | Critical | Smoke tests on the live URL (read only checkout) |
| D10 | Indexing intent | Paid only pages may be `noindex`; the main PDP must not be | Medium | `url_check.py` flags noindex; confirm intent with `seo` |
| D11 | Destination policy basics | No broken pages, no pop ups that block navigation, no auto downloads, working back button, business contact info reachable | High | Manual; platform destination policies |
| D12 | In-app browsers | Section 7 passes for each social channel in the plan | High | Real devices |

## 4. Tracking parameter conventions (agree once, check every launch)

UTM rules: lowercase, no spaces, underscores inside values, `utm_source` = platform (`google`, `meta`, `tiktok`, `microsoft`, `linkedin`, `chatgpt`), `utm_medium` = channel type from `MEASUREMENT.md` (`cpc`, `paid_social`, `display`, `video`), `utm_campaign` = campaign name or ID per the governance doc. Never put emails, names or phone numbers in any parameter.

| Platform | Click ID | Where parameters are set | Dynamic values | Common failure |
|----------|----------|-------------------------|----------------|----------------|
| Google Ads | `gclid` (auto tagging), `gbraid` and `wbraid` on iOS app to web | Final URL suffix (account, campaign or ad group level) and tracking template with `{lpurl}`; parallel tracking sends users straight to the final URL | ValueTrack `{campaignid}`, `{adgroupid}`, `{creative}`, `{keyword}`, `{matchtype}`, `{device}` | Redirects or plugins that strip `gclid`; tracking template without `{lpurl}`; AI Max or PMax final URL expansion sending traffic to pages that never passed QA (check URL expansion settings with `google-ads`) |
| Microsoft Ads | `msclkid` (auto tagging) | Final URL suffix, tracking template | `{CampaignId}`, `{AdGroupId}`, `{keyword:default}` (Microsoft uses its own macro set; verify) | Imported Google campaigns carry Google ValueTrack syntax that Microsoft does not resolve |
| Meta | `fbclid` appended by Meta | "URL parameters" field at ad level | `{{campaign.id}}`, `{{adset.id}}`, `{{ad.id}}`, `{{placement}}`, `{{site_source_name}}` | Parameters typed into the Website URL field and the URL parameters field (duplicates); in-app browser issues; Pixel and CAPI without matching `event_id` (double counting) |
| TikTok | `ttclid` | URL parameters in the ad | `__CAMPAIGN_ID__`, `__AID__`, `__CID__`, `__PLACEMENT__` | Macros left unresolved in manual URLs; in-app browser cookie isolation |
| LinkedIn | `li_fat_id` (with enhanced conversion tracking enabled) | UTM parameters in the destination URL or campaign level | `{{CAMPAIGN_ID}}`, `{{CREATIVE_ID}}` (verify the current macro list) | Lead gen form campaigns with no site visit to QA; check form field mapping instead |
| ChatGPT ads | `oppref` per `chatgpt-ads` skill | Destination URL | Per the chatgpt-ads skill | New surface: verify the parameter reaches the OpenAI pixel or CAPI as `chatgpt-ads` specifies |

Apple privacy note: Safari Link Tracking Protection removes known click identifiers in Private Browsing, in links opened from Mail and Messages, and in all browsing when the user sets Advanced Tracking and Fingerprinting Protection to "All Browsing"; UTM parameters are not stripped. Vendor claims that iOS 26 strips `gclid` and `fbclid` in all standard browsing are contradicted by testing on the final release [Contested, 2025-09 to 2026-07]. Safari 27 (iOS 27, 2026-09) brought no documented change to where it applies; third party reviews of WebKit source report more parameters added to the list [Unverified]. Engineering response: capture UTMs and click IDs server side or first party on landing, store them with the session or cart attributes, and never rely on a click ID surviving multiple redirects.

## 5. Offer, price and stock parity (the expensive failures)

| Check | Rule |
|-------|------|
| Price shown in the ad | Equals the page price for the targeted market and currency, tax display included |
| Strike through or compare at price | Real and allowed under the market's price rules (EU Omnibus 30 day prior price rule where it applies); confirm with `compliance` |
| Discount code in the ad | Works in a test checkout for the advertised products, at the advertised dates; does not stack unexpectedly |
| Free shipping or threshold claims | Match checkout behavior for the targeted country |
| Bundle or bonus product | Contents and availability on the page match the ad; bonus product in stock |
| Dates | Sale start and end dates match the ad schedule and the page; the sale state flips at the right time in the store timezone |
| Stock | Advertised variant sizes or colors available; sold out variants not featured in creative |

Run the parity check again at sale start and sale end ([Release process](release-process-and-rollback.md) Play 5).

## 6. Entity and plumbing checks (read only, from the platform or the change request)

| # | Check | Pass rule | Severity |
|---|-------|-----------|----------|
| E1 | Status | Every new campaign, ad set or ad group, and ad is PAUSED (or draft) until the human activates | Critical |
| E2 | Budget | Daily and lifetime budgets within `guardrails.json` caps (`daily_budget_per_campaign`, `daily_spend_per_account`); increase within `max_budget_increase_pct` | Critical |
| E3 | Schedule and geo | Start date, end date, time zone, countries and languages as approved | High |
| E4 | Conversion setup | Optimization event or conversion goal equals the primary conversion in `MEASUREMENT.md`; the right pixel or dataset ID; no test events left as primary | Critical |
| E5 | Event firing on the live URL | The optimization event fires once per action, with value and currency, browser and server events deduplicated (`event_id` or `transaction_id`) | Critical |
| E6 | Consent | Events follow consent choices; consent mode signals present where used | High |
| E7 | Links in ads | Sitelinks, callouts with URLs, lead form privacy policy links, app store links resolve | Medium |
| E8 | Creative destination | Every ad in the set points to a QA'd URL (no forgotten old URL in one variant) | High |
| E9 | Read back after any write | The channel agent read the entity back after creating it; IDs and values in the change request match the platform | High |

Site-engineer does not change platform entities. It reads them (or reads the change request and the channel agent's read back) and reports.

## 7. In-app browser protocol (Instagram, Facebook, TikTok, and others in the plan)

Why: most paid social clicks open inside the app's own browser (a WebView or system browser view), with its own cookie jar, no saved autofill or logins from the main browser, limited wallet support and app injected scripts. Researcher Felix Krause showed in 2022 that Instagram and Facebook in-app browsers on iOS injected JavaScript into visited pages; Meta said the code respected App Tracking Transparency choices and aggregated events [Study, 2022-08]. Vendor claims of large conversion losses in in-app browsers are unverified [Unverified].

Procedure (real devices: one current iPhone, one Android):
1. Get a real in-app session: open the ad preview link on the phone (Meta Ads Manager "Share a link" preview, TikTok preview QR) or send the final URL with UTMs to yourself in an Instagram or TikTok DM and tap it inside the app.
2. Check the page loads, the consent banner is usable, and the primary CTA is visible above the in-app browser's own toolbar.
3. Add to cart and reach checkout, or submit the form in test mode. Note whether Apple Pay, Google Pay or Shop Pay buttons render; if a wallet is missing in-app, it must not be the only fast path.
4. Confirm UTMs and click IDs on the landing URL (copy link from the in-app menu) and in the network or event debugger where possible (Meta Pixel Helper does not run in-app; use the Events Manager test events tool with the test code).
5. Use the in-app menu "Open in browser" and confirm the session state that matters (cart contents for logged out carts usually do not transfer; design for it, do not promise it).
6. Login, OAuth and payment redirects: test any "Sign in with" or third party payment redirect inside the in-app browser; these flows break most often.
7. Record device, OS version, app version and result in the QA report.

## 8. Launch QA report template

Save to `ads-master/outputs/site-engineer/YYYY-MM-DD_site-engineer_launch-qa-<campaign>.md`.

```markdown
# Launch QA: <campaign or change request ID>
Date: YYYY-MM-DD HH:MM (timezone) | Platform: <name> | Account: <ID> | Requested by: <slug>
Data used: change request <file>, platform read back <date>, url_check run <time>, devices <list>
Verdict: PASS | PASS WITH NOTES | FAIL

## Summary
- <3 bullets: what was checked, what failed, what must happen before activation>

## Destination checks
| URL | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D12 | Notes |
|-----|----|----|----|----|----|----|----|----|----|-----|-------|

## Entity and plumbing checks
| Entity ID | Name | E1 status | E2 budget vs cap | E3 | E4 | E5 | E6 | E8 | Notes |
|-----------|------|-----------|------------------|----|----|----|----|----|-------|

## In-app browser results
| Device and OS | App and version | Load | CTA visible | Cart or form | Wallets | Params kept | Notes |

## Failures and owners
| # | Item | Evidence | Owner (slug) | Fix | Retest by |

## Handoffs requested
- <slug>: <2 to 4 line brief>
```

## 9. Post launch check (within 30 minutes of first delivery, then at 24 hours)

| Check | Rule |
|-------|------|
| Landing page sessions vs clicks | Sessions not far below clicks (a large gap points to slow pages, redirects, consent or in-app issues); compare with the platform's landing page views where available |
| Events in the platform event manager | Optimization event arriving, deduplicated, with values |
| Spend pacing | Within plan (channel agent) |
| Errors | No new JS errors on the landing page in RUM or error tracking |
| Stock | Advertised items still above the stock guard |

If a destination breaks after launch, it is an incident: stop writes, alert, and recommend pausing the affected ads; the channel agent drafts the pause and the human approves (runbook in `ads-master/INCIDENTS.md`).

## 10. Common expensive mistakes

1. Launching with an old URL in one ad variant or sitelink that 404s after a site migration.
2. A redirect (http to https, www, trailing slash, locale) that drops `gclid` or `fbclid`, so conversions attribute to nothing and smart bidding learns from fewer conversions.
3. Ad promises a price or discount the page does not show (or a code that does not work): wasted spend and misrepresentation risk.
4. Consent banner covering the CTA on small phones, raising bounce on the first screen.
5. Pixel and CAPI both firing a purchase without a shared `event_id`, doubling reported conversions.
6. Testing only in desktop Chrome while most paid social clicks open in in-app browsers on phones [Practitioner consensus; measure the share in your own analytics by user agent].
7. Entities created ACTIVE "by accident" through an API or bulk upload default. Status PAUSED is a check, not an assumption.
