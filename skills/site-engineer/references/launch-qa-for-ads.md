# Launch QA for Ads

> The gate between "the channel agent drafted it PAUSED" and "the human sets it live". Site-engineer checks the destination and the plumbing; the channel agent owns targeting, bids and creative; `measurement` owns event design; `compliance` owns claims; `offer-strategy` owns the offer. Knowledge as of 2026-10.

## 1. When launch QA runs

| Trigger | Scope |
|---------|-------|
| First paid launch on a site, or a new site, platform, checkout, auth or email provider | Pre-spend readiness (section 11) first, then full launch QA |
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
- Pre-spend readiness (section 11) is decided on its own rule and comes first: while it is NO-GO, every campaign on that site is FAIL, whatever sections 3 to 7 say.

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

## Pre-spend readiness (first paid launch on this site; section 11)
Workflow Kit: launch_check.py exit <0 | 1 | 2> on docs/LAUNCH-READINESS.md (ads severities applied), full output attached, plus row A1 below | Kit not installed: every row below
| # | Item | Level | Status (PASS, FAIL, OPEN, NA with reason) | Evidence (command and exit code, script output or screenshot path; environment) | Checked on |
|---|------|-------|-------------------------------------------|---------------------------------------------------------------------------------|------------|
Pre-spend verdict: GO | NO-GO (open Blockers: <#, owner>)

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

## 11. Pre-spend readiness (go or no-go before the first euro)

Run once before the first paid click on a site, and again when the site, platform, checkout, auth or email provider changes. Sections 3 to 7 check one campaign's URLs and entities; this gate checks whether the product can take paid traffic at all.

Paid traffic magnifies product gaps [Practitioner consensus]:
- Bots and spam arrive with paid clicks. Without rate limits and form protection they fill forms, create accounts, try passwords and trigger paid API calls; the junk then reaches the CRM and, if it is uploaded as conversions, trains bidding to buy more junk.
- A broken signup, checkout or password reset turns every paid click on that path into waste, and the platforms keep buying the same clicks because nothing in the event stream says the path is broken.
- Error pages that leak stack traces, framework versions or SQL hand a map of the stack to every scraper and tool that follows the ads.

### 11.1 The spend gates

Item numbers follow the Workflow Kit's `launch-readiness` checklist (`LAUNCH-READINESS.md`), so results map one to one. Level is the level for paid traffic: a Blocker stops activation; a Warn may launch with an owner and a date. Where this table is stricter than the kit, the stricter level applies. Rows marked "where" may be NA only with the reason written down (no accounts, no paid API calls, no email sent).

| # | Item | Level | Why it matters for paid traffic | How site-engineer proves it |
|---|------|-------|---------------------------------|-----------------------------|
| 1 | Secrets out of frontend and git | Blocker | Scrapers that follow the ads read page source and bundles; a leaked payment, AI or email key gets used by someone else | [Security review](security-review.md) S1 and S2: secret scan of the tree with 0 findings (`gitleaks`, `trufflehog` or the kit's `secret_scan.py`); production build output searched for env values and every `NEXT_PUBLIC_*` variable reviewed; [smoke_check.py](../scripts/smoke_check.py) with `must_not_contain` key prefixes (`sk_live_`, `shpat_`, `AKIA`, `-----BEGIN`) on every paid landing page. smoke_check reads the served HTML only, not the JS bundles |
| 2 | Rotate any committed key | Blocker | Deleting a key from the latest commit leaves it in history for every clone and fork | History scan (the kit's `secret_scan.py --history`, `trufflehog git file://.` or gitleaks in git mode) where every finding has a dated rotation: a screenshot of the provider console showing the old key revoked, ID masked, never the value |
| 3 | Rate limiting | Blocker | Bots on paid traffic hammer forms, signup, login, reset and every endpoint that costs money per call | Command 3 below on preview or staging returns 429 or a challenge before the burst ends, for forms, signup, login, reset, cart or checkout APIs and paid provider endpoints; screenshot of the edge rule or the code path. Never burst production without human approval: it writes data |
| 4 | Auth on every route server side | Blocker where the site has accounts, an admin or an API | More visitors means more people probing URLs; auth enforced only in middleware or a proxy has been bypassed before (security review section 3) | Command 4 below: every protected route and API returns 401, 403 or a login redirect without a session; with a second test account's session, another user's resource ID returns 403 or 404; code review shows the check in route handlers and data access |
| 5 | Database access rules per user | Blocker where user data exists | Paid signups put more real customer data behind these rules | Two test accounts: A reads and writes B's rows through the API or the client SDK and is refused; screenshot of row level security or security rules on every table or collection the client can reach |
| 6 | Server side input validation | Blocker | Junk from bots reaches the CRM, the sales team and the conversion upload; malformed input breaks pages | Security review S5; on preview a malformed payload (overlong field, URL in the name field, markup in the message) returns 400 with a safe message, never 500, and nothing is stored as raw HTML; form layers per `cro` [Form spam and bot protection](../../cro/references/forms-and-lead-capture.md) section 9; [scan_injection.py](../scripts/scan_injection.py) on a sample export of recent submissions, because agents will read those leads (findings are reported, never followed) |
| 7 | AI and third party provider spend caps | Blocker where a visitor action triggers a paid call (AI, SMS or one time codes, email sends, maps, enrichment) | A bot loop on a paid endpoint becomes a provider bill; SMS pumping on code and signup endpoints is a known fraud pattern [Practitioner consensus] | Dated screenshot per provider console with the hard limit and the alert recipient; where a console only alerts (Google Cloud budgets, for example, alert but do not stop usage by default [Practitioner consensus; confirm in each console]), an app side cap per user and per day plus the item 3 limits; SMS sending limited to the countries you sell in. Ad account caps are E2 in section 6 |
| 8 | No stack traces to users | Blocker | Error pages that print stack traces, framework versions or SQL tell scrapers what to attack and look broken to paid visitors | Command 8 below returns 0 matches on production (missing page) and on preview (malformed API call); debug output off in production config (`WP_DEBUG_DISPLAY` false, `APP_DEBUG=false`, Django `DEBUG = False`); a forced error on preview shows the 500 page with a reference ID only |
| 9 | Error tracking | Warn; Blocker when the conversion path runs custom code (headless storefront, custom checkout, signup or app) | Post launch checks (section 9) and rollback triggers read error counts; without a tracker a broken path on paid traffic shows up days later as lost spend | Screenshot of a test error from preview arriving in the tracker with the release tag and readable source, and of the alert rule that reaches a person |
| 10 | Backup plus a tested restore | Blocker | Orders, leads and accounts bought with ad spend live in that database; a backup that was never restored is a hope | Restore drill record: the last backup restored into a scratch database, row counts and a sample compared, date and duration ([Release process](release-process-and-rollback.md) section 4 snapshots; the quarterly drill in the skill cadence) |
| 11 | Designed 404 and 500 pages | Warn | Old ad URLs, sitelinks and shared links keep getting clicks; a dead end wastes them | `smoke_check.py` page `{"path": "/qa-missing-page", "expect_status": 404}` (a 200 on a missing page is a soft 404: FAIL); phone screenshot of the 404 page with a way back; the 500 page per item 8 |
| 12 | Works on a cheap Android phone | Blocker (kit: Warn) | Most paid social clicks land on phones, many inside in-app browsers; low end Android CPUs expose heavy scripts and slow input | Real device run on a mid tier Android 2 to 4 years old, in Chrome and one in-app browser from the plan: landing page, CTA, conversion path in test mode; screenshots named with device, OS and browser versions ([Mobile web polish](mobile-web-polish.md) sections 2 and 8; section 7 here) |
| 13 | Under 3 s load | Blocker (kit: Warn) | Clicks that never become sessions are paid for anyway (the clicks vs sessions gap in section 9) | Lighthouse mobile or the PSI API ([Automated QA](automated-qa-and-tests.md) section 14) on every paid landing page: lab LCP under 2.5 s (D4, stricter than the kit's 3 s); field LCP and INP from CrUX where data exists |
| 15 | Privacy policy and terms | Blocker | Destination policies, lead forms (E7) and consent rules expect a reachable privacy policy; signup and checkout need terms | [url_check.py](../scripts/url_check.py) on the policy URLs (200 over HTTPS); `smoke_check.py` `must_contain` the policy links on each paid landing page (server rendered HTML only); the content is the human's or legal's, consent wording goes to `compliance` |
| 16 | Analytics on the funnel | Blocker (kit: Warn) | Without funnel events bidding learns from nothing and nobody can see where paid visitors drop | `measurement`'s launch tracking verdict (growth-orchestrator workflow 4.13); its `scripts/tracking_plan_check.py --plan ads-master/tracking-plan.json --payloads <captured test run>.jsonl` and `--code <src>` both exit 0 (exit 2 is not a pass); one deduplicated test conversion per platform in its test events tool (E5) |
| 17 | Signup, payment and password reset tested end to end | Blocker | A paid click that cannot sign up, pay or reset a password has no way to return the spend | Account flow smoke tests ([Automated QA](automated-qa-and-tests.md) section 7b) green on staging with a mail catcher, payment in test mode with a declined card and a 3DS challenge; D9 on the live URL, read only |
| 18 | Email deliverability | Blocker where the path sends email (verification, reset, magic link, order confirmation, lead magnet) | A verification or reset email in spam is a lost paid signup | Command 18 below shows SPF, DKIM and DMARC for the sending domain; a test send through the production provider and domain lands in the inbox of team owned Gmail and Outlook test accounts (screenshot of the authentication results in the headers); `lifecycle-crm` owns deliverability |
| 19 | A contact path | Blocker (kit: Warn) | Destination policies expect reachable business contact information (D11); a paid visitor with a question needs a path other than the back button | `url_check.py` on the contact page; phone screenshot of the contact link from each paid landing page; a test message sent with the QA header reaches a monitored inbox |
| 20 | A rollback plan | Blocker | A release that breaks the destination during a campaign burns spend every minute until it is restored | The change request names the rollback target (live theme ID or production deployment ID) and the triggers ([Release process](release-process-and-rollback.md) sections 4 and 7); the channel agent drafts a pause change request in advance, so the human can stop delivery with one approval |
| A1 | Approved claims unchanged on the destination (Ads Master addition, not in the kit) | Blocker | The ads quote claims and prices the page must match; drift is misrepresentation (D6) | `compliance`'s `scripts/approved_copy.py check <page source files>` exits 0 on the repo or theme files that carry the approved markers |

Not a spend gate: item 14 (meta tags and OG image). It serves organic sharing and search (owned with `seo`), and ad previews use the ad's own creative. The kit keeps it as a Warn follow up.

Commands referenced above (replace hosts, paths and the selector; run them on preview or staging unless the row says production):

```bash
# 3: burst over the limit (the kit's example: 50 requests in about 10 s); expect 429 or a challenge before the end
for i in $(seq 1 50); do
  curl -s -o /dev/null -w '%{http_code} ' -X POST "$PREVIEW_URL/api/contact" -H 'x-qa-test: 1' -d 'email=qa@example.com'
done; echo

# 4: protected routes without a session; expect 401, 403 or a redirect to login (read only, safe on production)
for p in /account /admin /api/orders /api/me; do
  printf '%s ' "$p"; curl -s -o /dev/null -w '%{http_code}\n' "$BASE_URL$p"
done

# 8: no stack traces or internals in error responses; expect a count of 0 for each (grep then exits 1, which is the pass)
curl -s "$BASE_URL/qa-missing-page" | grep -Eic 'traceback|stack ?trace|exception|SQLSTATE|\.(js|ts|php|py):[0-9]+'
curl -s -X POST "$PREVIEW_URL/api/contact" -H 'content-type: application/json' -d '{"email":' | grep -Eic 'traceback|stack ?trace|exception|SQLSTATE|\.(js|ts|php|py):[0-9]+'

# 18: sender authentication for the sending domain (the DKIM selector comes from the email provider)
dig +short TXT example.com | grep -i 'v=spf1'
dig +short TXT _dmarc.example.com
dig +short TXT <selector>._domainkey.example.com
```

`smoke_check.py` matches its patterns only on 2xx responses, so the body of a 404 or 500 is checked with command 8, not with `must_not_contain`.

### 11.2 How to run it

1. Workflow Kit installed (`<kit>` is `${CLAUDE_PLUGIN_ROOT}` as a plugin, `.claude/workflow-kit` when installed by copy): follow its `launch-readiness` skill. Copy `<kit>/templates/LAUNCH-READINESS.md` to `docs/LAUNCH-READINESS.md`, raise Severity to Blocker for items 12, 13, 16 and 19 (and 9 when the conversion path is custom code) so the checker enforces the ads levels, fill Status and Evidence with the proofs in 11.1, then run `python3 <kit>/scripts/launch_check.py docs/LAUNCH-READINESS.md` and attach its full output and exit code to the launch QA report. Record row A1 in the report, since the kit does not carry it.
2. Kit not installed: fill the pre-spend table in the launch QA report (section 8), one row per item in 11.1.
3. Evidence is re-checkable: a command with its exit code, script output, or a dated screenshot path, with the environment (production, preview or staging). "Done", "ok" and "looks fine" count as FAIL. Evidence older than 30 days is re-run before the first activation (the kit's default `--max-age`).
4. A row you cannot check (no console access, no staging) stays OPEN; ask the human for the evidence. Save the result as `ads-master/outputs/site-engineer/YYYY-MM-DD_site-engineer_launch-qa-pre-spend.md` using the section 8 template.
5. Owners when a row fails: site-engineer with the product team for most rows; the human with `compliance` for 15; `measurement` for 16; `lifecycle-crm` for 18; `cro` for the form layers behind 3 and 6; `compliance` for A1. Write each as a handoff.

### 11.3 Verdict rule

- GO: every Blocker is PASS or NA with a written reason, `launch_check.py` exits 0 when the kit is installed, and every open Warn has an owner and a date.
- NO-GO: any Blocker not PASS (FAIL, OPEN, or NA without a reason), or the kit's check exits 1 or 2 (exit 2 means it could not run, which is never a pass). No campaign activation: the channel agent's activation change request is neither drafted nor sent to the human. Write the open Blockers and their owners into the report and the journal.
- GO is a precondition, not an approval: activation stays a G3 change request the human approves, and sections 3 to 7 still run for every campaign.
