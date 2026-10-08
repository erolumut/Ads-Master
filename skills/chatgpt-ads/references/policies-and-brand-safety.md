# Policies, Brand Safety and Privacy

> Knowledge as of 2026-10. Primary source: OpenAI Ad Policies (openai.com/policies/ad-policies/), last updated 2026-09-10, version v1.6, read via a mirror captured 2026-09-22. Also: Help Center (Ads in ChatGPT 20001047, Troubleshooting onboarding and policy 20001534, crawler guidance 20001243), Commerce and Prohibited Products policies, October 2026 brand safety announcement. Policy text governs; this module is a working summary. Re-check the changelog before every launch.

## 1. Policy changelog [Official, 2026-09]

| Version | Date | Change |
|---------|------|--------|
| v1.0 | 2026-03 | Initial publication |
| v1.1 | 2026-04 | Medical, legal and financial advice contexts no longer blocked by default; sensitive and other prohibited contexts remain ineligible |
| v1.2 | 2026-05 | Review standards, implementation and enforcement section |
| v1.3 | 2026-07 | Advertiser policies section; eligible financial and health categories and markets clarified |
| v1.4 | 2026-08 | Housing and job listing policy clarified |
| v1.5 | 2026-08 | Legal services permitted in the US |
| v1.6 | 2026-09 (page updated 2026-09-10) | OpenAI may decline, restrict or remove advertisers and ads for any reason, including conflicts with its advertising principles, business interests or competitive position |

Freshness rule: if the live version is newer than v1.6, read the new changelog entries before drafting any creative or category assessment, and log the change.

## 2. Where ads never appear (placement exclusions) [Official, 2026-09]

| Context type | Examples |
|--------------|----------|
| Sensitive user contexts | Emotionally reliant conversations, mental health, personal health, sensitive user journeys and life situations |
| Inappropriate topics | Child safety, cyber abuse, dangerous activities, fraud, hate, illicit content, misinformation, political content, self-harm, terrorism, weapons |
| Brand unsafe contexts | Anything violating OpenAI usage policies or widely recognized brand safety frameworks |
| Audiences | Users identified or predicted under 18; Plus, Pro, Business, Enterprise, Edu; Temporary Chat; Atlas browser |

Context hints and negative phrases influence relevance but never override these blocks [Official, 2026-09]. Do not plan reach in these contexts. Note one panel found ads on 28.69% of "healthcare" niche prompts [Study, 2026-08]; that niche includes non-sensitive shopping prompts (devices, insurance comparisons), not personal health conversations.

## 3. Category tiers

### Allowed (consumer verticals, all available markets) [Official, 2026-09]
- Lifestyle and household goods (retail, apparel, home, electronics, beauty)
- Local services
- Travel and experiences, entertainment
- Digital products and education (software, apps, courses)
OpenAI says these may expand over time. B2B software is commonly treated as digital products [Unverified].

### Restricted: US only, approved advertisers, case by case manual review [Official, 2026-09]
| Category | Examples allowed for approved US advertisers | Never allowed |
|----------|---------------------------------------------|---------------|
| Financial services | Cards, loans, insurance, investing, mortgages, payments (proof of licensure may be required) | Credit repair, debt settlement, alternative investments such as bullion |
| Health services | Dental, vision, diagnostics, devices, supplements, health insurance (select approved), hospitals, minimally invasive cosmetic procedures | Prescription medicines, OTC medicines, telehealth, online pharmacies, pregnancy tests [Official, 2026-09] (help center health table) |
| Legal services | Licensed in the jurisdiction where the ad runs (since v1.5) | Unlicensed services |
Outside the US, financial, health and legal services are generally prohibited [Official, 2026-09]. Disease awareness content is allowed in the US only [Official, 2026-09].

### Disallowed [Official, 2026-09]
- Adult content, dating and sexual content (retail lingerie and swimwear allowed in a standard retail context)
- Alcohol (above 0.5% ABV reported) and tobacco or vaping
- Counterfeit goods
- Gambling (casino hotels may advertise lodging or entertainment where gambling is not the focus; games without real money prizes reported allowed)
- Graphic sexual or violent content
- Individual job listings and individual housing rentals or sales (platforms allowed if they do not promote a specific listing)
- Political content, including elections, policy and contested social issues
- Recreational drugs including THC (non-intoxicating hemp products carve-out)
- Scams, fraud, impersonation
- Sensitive social topics and tragedies
- Weapons
- Wellness products with unsupported health claims (diet pills, detox, health coaching)
Details marked "reported" come from a community preflight summary of v1.5 [Unverified].

### Advertiser level eligibility
- A business whose primary model is in a restricted or prohibited category may be ineligible even with a compliant ad [Official, 2026-09].
- Competitive position clause (v1.6): competitors of OpenAI products may be refused. Trade press reported OpenAI stopped approving standalone image and audio generation products [Unverified] (The Information relay).

## 4. Creative and landing page standards [Official, 2026-09]

| Standard | Requirement | Example violation |
|----------|-------------|-------------------|
| Truthful, substantiated | No unfounded claims about capabilities, pricing, outcomes, affiliations or comparisons; no exaggerated results, false endorsements, absolute promises | "Guaranteed to rank #1" |
| Professional language | No obscenity, vulgarity, shock content, including in product or event names | Profane product name in title |
| No discrimination or harassment | Protected groups | Exclusionary language |
| Distinguishable from ChatGPT | Must not imitate ChatGPT or OpenAI interface or imply endorsement | Chat bubble styled image, "ChatGPT recommends" |
| End to end consistency | Copy, image or video, and landing page reviewed together | Food delivery ad that lands on alcohol delivery |
| Identity | Accurate business identity, ownership and affiliations; only owned or licensed trademarks | Using a retailer's logo without license |
| Landing page | Clearly related to advertiser and offer; no phishing, typosquatting, deceptive redirects, unverified messaging channels | Redirect chain to a different domain |
| Law | Comply with laws in every targeted region; keep required licenses; do not misstate location or service area | Service area claim outside license |
| No circumvention | Do not evade review or enforcement | Cloaking landing pages |

## 5. Review and enforcement [Official, 2026-09]

- Review levels: advertiser, creative and landing page, placement.
- Automated review by LLMs and classifiers, human escalation for higher risk or restricted cases. Reviews typically take minutes [Unverified] (practitioner reports 3 to 10 minutes).
- Ads that cannot be evaluated (for example landing page not crawlable) are not eligible.
- Monitoring continues after approval; delivery can be limited or ads removed later.
- Enforcement: reject, remove, limit delivery, suspend or terminate accounts for severe or repeated violations.
- Users can report ads in product; confirmed higher severity issues may pause an ad during investigation.
- Any creative edit triggers a new review; name or status changes do not [Official, 2026-09]. Changing legal or public brand name triggers brand review and pauses delivery [Official, 2026-09].
- If you believe a rejection is wrong, edit and resubmit or request another review; there is no API endpoint to file appeals (Ads Manager only) [Unverified].

Rejection reasons visible in the API (crawler and landing related): `crawl_failed`, `crawler_bot_blocked`, `crawler_captcha`, `crawler_login_required`, `robots_txt`, `unsupported_content_type`, `landing_page_image_processing_failed`, `landing_page_unusable`, `missing_favicon` [Unverified] (community notes from the API spec). Serving issue codes include `ad_account_brand_review_missing_favicon`, `campaign_budget_exhausted`, `landing_page_crawl_issue`, `policy_country_targeting_blocked`, `reserved_query_params_present`, `ad_over_18_only` [Unverified].

## 6. Crawler access (most common technical rejection) [Official, 2026-09]

- OAI-AdsBot is required for landing page validation and review. OAI-SearchBot is recommended.
- robots.txt:
```
User-agent: OAI-AdsBot
Allow: /

User-agent: OAI-SearchBot
Allow: /
```
- IP allowlisting: use https://openai.com/adsbot.json and https://openai.com/searchbot.json; do not rely on IPs seen in logs.
- Cloudflare verifies and allowlists OAI-AdsBot; Akamai and other WAFs may return 403; review bot mitigation rules.
- CAPTCHAs, JavaScript challenges, behavioral analysis and session validation can block crawlers; exempt by user agent.
- Large batch uploads can trigger rate limiting (429); upload in smaller batches over time.
- After fixing, re-upload or resubmit affected ads; support will not manually bypass.
- Page must return HTML with 200, require no login, not be robots blocked [Official, 2026-09].

Quick test:
```bash
curl -s -o /dev/null -w "%{http_code} %{redirect_url}\n" -A "OAI-AdsBot" "https://www.example.com/landing?oppref=test123"
```
This simulates the user agent only; it does not prove OpenAI's real crawler can reach the page (network reputation and bot verification differ) [Practitioner consensus].

## 7. Brand safety controls for advertisers

| Control | Status (2026-10) | Label |
|---------|------------------|-------|
| Platform placement guardrails (sensitive and unsafe contexts excluded) | Always on | [Official, 2026-09] |
| Negative Phrases | For qualifying advertisers with narrow, brand policy driven placement needs (announced 2026-10-05); OpenAI published no eligibility criteria. Adthena saw the field in a live UK account before the announcement: up to 100 phrases of up to 100 characters each; an ad is blocked when the user's message contains a phrase (hard exclusion, unlike context hints) | [Official, 2026-10] (availability) and [Unverified] (limits, single source) |
| Negative keywords in the API | Removed from the public API spec in 2026-09 | [Unverified] |
| Third-party verification | DoubleVerify and Integral Ad Science brand suitability pilots in a controlled test environment; OpenAI states they do not access private conversations | [Official, 2026-10] |
| Placement or query reports | Not available; advertisers cannot see the conversations or prompts | [Official, 2026-09] |
| Off topic risk | One panel found 14.35% of ad impressions unrelated to the query [Study, 2026-08] | |

Brand safety practice: sample your own placements by asking ChatGPT (on a Free account in the target market) the conversations your hints target and screenshot what appears; keep hints specific; use Negative Phrases if eligible; never rely on context hints to exclude.

## 8. Privacy and compliance for advertisers

- Advertisers receive aggregate data only; no prompts or personal data [Official, 2026-09].
- Pixel and CAPI: share conversion data only where permitted; disclose the OpenAI pixel in your privacy notice; obtain consent where required; hashed identifiers are still personal data under GDPR [Official, 2026-09] (OpenAI guidance) and [Practitioner consensus].
- EEA and Switzerland: no ad personalization; do not use custom audiences [Official, 2026-09].
- Custom audience uploads need a legal basis and, for EEA data, are not to be used [Official, 2026-09].
- Independent research raised questions about a cross site `__obi` cookie and AAM defaults [Unverified]; consult counsel for EU and UK deployments and configure consent false by default.
- EU DSA: ChatGPT search reported 159.1M EU monthly recipients; the European Commission designated ChatGPT a Very Large Online Search Engine on 2026-08-31 [Official, 2026-08]. Obligations apply four months after notification (around end of 2026 to January 2027): ad repository, systemic risk assessments, audits, no ads based on profiling of minors or on sensitive data (religion, political opinions, health and other special categories). Expect your ads (creative, advertiser name, targeting parameters) to become publicly visible in an EU ad repository. The UK lists only ChatGPT Search in Ofcom's Category 2A under the Online Safety Act [Unverified] (legal commentary).
- FTC (US): ads must be clearly labeled (OpenAI labels them); your claims remain your responsibility under truth in advertising rules [Practitioner consensus].

## 9. Pre-launch policy checklist
- [ ] Category allowed for the advertiser's country (not just the target market).
- [ ] Primary business model not restricted or prohibited.
- [ ] US only and approved if finance, health or legal.
- [ ] No mention of ChatGPT or OpenAI; no chat UI imitation in images.
- [ ] Claims substantiated with a source recorded in the ad copy sheet.
- [ ] Landing page matches offer, no disallowed content anywhere in the immediate path.
- [ ] Trademarks owned or licensed.
- [ ] Landing page crawlable by OAI-AdsBot (200, HTML, no login, no CAPTCHA, robots allowed).
- [ ] No reserved query parameters (`oppref`, `olref`, `obref`, `oai*`) used as your own parameter names.
- [ ] Favicon 256x256 uploaded; brand review approved.
- [ ] Consent and privacy disclosures in place for the pixel.

## 10. Policy decision quick table
| Advertiser | US | UK, EU, other markets |
|-----------|----|-----------------------|
| Fashion retailer | Allowed | Allowed |
| Online casino | Disallowed | Disallowed |
| Casino resort (rooms, shows) | Allowed if gambling not the focus | Same |
| Craft brewery | Disallowed (alcohol) | Disallowed |
| Non-alcoholic beer (0.0%) | Likely allowed (threshold 0.5% ABV reported) [Unverified] | Same |
| Personal injury law firm | Restricted, allowed if licensed in the jurisdiction (v1.5) | Prohibited |
| Credit card issuer | Restricted, approved advertisers | Prohibited |
| Telehealth clinic | Not allowed | Not allowed |
| Supplement brand | Restricted, approved advertisers, no unsupported claims | Not allowed |
| Dating app | Disallowed | Disallowed |
| Job board (no specific listing promoted) | Allowed as platform | Allowed as platform |
| Real estate listing ad for one home | Disallowed | Disallowed |
| AI image generator app | Possible refusal under v1.6 competitive clause | Same |
| B2B SaaS | Allowed (digital products) | Allowed |
| CBD topical (non-intoxicating) | Possible under hemp carve-out | Check local law |
