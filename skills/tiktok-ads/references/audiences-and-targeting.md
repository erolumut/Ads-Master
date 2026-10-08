# Audiences and Targeting

> Knowledge as of 2026-10. TikTok's delivery system leans on creative signal more than declared targeting. The default in 2026 is broad or automatic targeting with guardrails, and creative does the targeting. Exact audience size minimums and retention windows below were not re-verified this cycle; check the Audiences page in Ads Manager.

## 1. The 2026 default: broad with guardrails

| Situation | Targeting stance | Why |
|-----------|-----------------|-----|
| Sales or app with 50+ conversions per week | Smart+ automatic targeting or manual broad (country, age floor, language) | The system finds buyers from creative engagement and conversion signal; narrow interests raise CPM and cap scale [Practitioner consensus] |
| New pixel, under 25 conversions per week | Broad, plus one interest or lookalike ad group as a comparison cell | Little signal to learn from; a comparison cell shows whether constraints help |
| Regulated category | Enforced audience controls (age 18+ or 21+, geo) | Legal compliance overrides performance |
| Local services | Location radius or city plus age floor, otherwise broad | Geography is the only constraint that matters |
| B2B SaaS | Broad plus job-related interests as a test cell; let creative call out the role | TikTok has no firmographic targeting; creative must self-select the buyer |
| Retargeting | Only when the pool is large enough (see section 5) | Small pools fatigue in days on TikTok |

In the upgraded Smart+ flow, automatic targeting is the default; "Audience controls" set baseline parameters, and "Switch to custom targeting" moves to manual. Some targeting settings can be enforced so the system cannot expand past them [Official, 2026].

## 2. Manual targeting menu (ad group)

| Section | Options (verify names) | Notes |
|---------|------------------------|-------|
| Demographics | Location (country, region, city; DMA in the US [Unverified]), age groups (18 to 24, 25 to 34, 35 to 44, 45 to 54, 55+; 13 to 17 restricted), gender, languages, household income or spending power in some markets [Unverified] | Age floors are the most common compliance control |
| Audience | Custom audiences and lookalikes, include and exclude | Exclude purchasers on acquisition campaigns when the pool is large |
| Interests and behaviors | Interests (general and purchase intention), video interactions, creator interactions, hashtag interactions, time window (7 or 15 days for behaviors [Unverified]) | Useful for testing and cold starts, not for scaling |
| Devices | OS, OS version, device model, connection type, carrier, device price | Use OS split for apps; device price as a proxy for income in some markets |
| Targeting expansion | Lets the system go beyond chosen interests or lookalikes | Turn on unless a legal reason exists |

Behavior targeting note: "video interactions" (watched to end, liked, commented, shared) on a category and "creator interactions" (followed, viewed profile) can be the best interest-style cells for niche products because they reflect recent behavior on TikTok itself.

## 3. Custom audience types

| Type | Built from | Retention (verify) | Best use |
|------|-----------|--------------------|----------|
| Customer File | Hashed emails, phones, mobile ad IDs | n/a (refresh monthly) | Exclusions, lookalike seeds, win-back |
| Website Traffic | Pixel / Events API events (all visitors, specific pages, events, time spent) | Up to 180 days [Unverified] | Cart and checkout retargeting, purchaser exclusion |
| App Activity | MMP / SDK events | Up to 180 days [Unverified] | Re-engagement, payer exclusion |
| Engagement | Users who viewed, watched 2s or 6s, completed, clicked, liked, commented, shared your ads | Up to 365 days [Unverified] | Warm pools for retargeting with offer or proof creative |
| Lead Generation | Users who opened or submitted Instant Forms | Varies | Retarget openers who did not submit |
| Business Account | Followers and users who interacted with your TikTok account and organic videos | Varies | Retarget organic viewers for Spark Ads |
| Shop Activity | Product views, add to cart, purchase in TikTok Shop | Varies | GMV Max handles most Shop retargeting automatically; use for web campaigns' exclusions |
| LIVE | Users who watched or interacted with your LIVE | Varies | LIVE promotion and replay retargeting |

Minimum sizes: a custom audience generally needs on the order of 1,000 matched users before it can be used for targeting [Unverified, check the audience status column]. Small lists (B2B accounts, high-ticket customers) often fail to match.

## 4. Lookalike audiences
- Seeds: purchasers (best), high-value purchasers (top 20% by value), qualified leads from CRM, app payers, 75% or 100% video viewers (weakest for sales).
- Size: narrow, balanced or broad options. Start balanced. Narrow lookalikes in small countries raise CPM.
- Refresh seeds monthly. Stale seeds are a silent performance drain.
- At Scale tier, lookalikes rarely beat broad on CPA. Keep one lookalike cell only if a split test shows a win.

## 5. Retargeting on TikTok: limits and rules

| Rule | Why |
|------|-----|
| Do not run a separate retargeting campaign until the combined pool (website visitors 30 days + engagers 30 days) is large enough to spend at least the $20 ad group minimum without frequency above 3 per week | Small pools fatigue fast; CPM spikes |
| Broad and Smart+ campaigns already re-reach warm users | Separate retargeting often double-counts the same conversions [Practitioner consensus] |
| Use proof, offer and objection creative in retargeting, not the same hook ads | Warm users have seen the hook |
| Cap retargeting at 10% to 20% of TikTok spend unless incrementality evidence says otherwise | Retargeting looks great in platform ROAS and is the least incremental spend |
| Exclude purchasers from the last 30 to 180 days on acquisition campaigns when the business model is not repeat-heavy | Avoids paying for existing customers; for consumables, keep them in |

Privacy and regulatory limits on retargeting:
- Users aged 13 to 17 do not see personalized ads in the EEA (and TikTok has extended similar limits elsewhere) [Unverified for current market list]. Do not plan any youth-targeted campaign without legal review.
- The EU Digital Services Act bans profiling-based ads to minors and ads based on special category data (health, sexual orientation, religion, political views). Do not build audiences from health-condition pages for EEA users.
- Housing, employment and credit advertisers in the US and Canada face restricted targeting options on most major platforms. Check TikTok's current special ad category rules before building HEC campaigns [Unverified].
- Consent: in the EEA and UK the pixel must respect the consent banner; audiences shrink accordingly. Hand consent questions to the measurement agent.

## 6. Exclusions and overlap
- Exclude existing customers (Customer File) from acquisition when new customer CAC is the KPI.
- Exclude recent converters from Lead Generation to avoid duplicate leads.
- In Smart+ with enforced audience controls, add exclusions where the UI allows; otherwise accept overlap and measure blended.
- Overlap across ad groups is normal for broad targeting. Do not split broad into many ad groups to "control overlap". That fragments learning.

## 7. Geo and language
- One market per campaign when currencies, languages, pricing or shipping differ.
- Language targeting is optional; creative language is the real filter. In bilingual markets, use creative in each language and broad targeting.
- TikTok Shop ads (GMV Max) only serve where the Shop operates.
- US TikTok Ad Network (formerly Pangle) opened on 2026-10-05; US campaigns can now reach users outside the TikTok app [Official, 2026-10]. Decide deliberately per campaign.

## 8. Audience testing design

| Test | Cells | Budget per cell | Duration | Read |
|------|-------|----------------|----------|------|
| Broad vs interest | 2 manual ad groups, same creatives, same bid | At least 10x target CPA per day | 14 days | Backend-matched CPA and new customer share |
| Broad vs lookalike | 2 ad groups | Same | 14 days | Same |
| Smart+ automatic vs manual broad | Ads Manager Split Test | Equal | 14 to 21 days, or until significance | Platform CPA plus backend check |
| Retargeting incrementality | Holdout: exclude 50% of the pool by random split where possible, or geo split | n/a | 21 to 28 days | Conversion rate difference between exposed and held-out halves |

Use the Ads Manager Split Test (A/B test) tool where available because it splits users without overlap. Log every test in `ads-master/EXPERIMENTS.md` with hypothesis, primary metric and stop rule.

## 9. Audience diagnostics

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| CPM 50%+ above account average in one ad group | Narrow audience or small geo | Broaden, merge ad groups, add creatives |
| Frequency above 4 per 7 days in a retargeting cell with rising CPA | Pool too small | Merge into acquisition, extend window, rotate creative |
| Lookalike "not ready" | Seed too small or not matched | Use a broader seed (all purchasers 180 days) or engagement seed |
| Customer File match rate very low | Unhashed or badly formatted data, B2B emails | Normalize (lowercase, trim, E.164 phone), add phone and MAIDs |
| Audience size shrinking in EEA | Consent rate falling, cookie changes | Measurement agent to check CMP and Events API identifiers |

## 10. Customer file preparation (before upload)

Normalize, then hash with SHA-256 if you hash yourself (TikTok also accepts files it hashes on upload; check the current upload options). Upload only with the human's approval and only for customers who consented under the project's privacy policy.

```python
import hashlib, re, pandas as pd
def norm_email(e):
    return str(e).strip().lower() if pd.notna(e) else None
def norm_phone(p, default_cc="1"):
    if pd.isna(p): return None
    d = re.sub(r"\D", "", str(p))
    if not d: return None
    return "+" + (d if len(d) > 10 else default_cc + d)  # E.164; adjust per market
def sha(v):
    return hashlib.sha256(v.encode("utf-8")).hexdigest() if v else None
df = pd.read_csv("customers.csv")            # keep outside ads-master/ if it holds raw PII
df["email_sha256"] = df["email"].map(norm_email).map(sha)
df["phone_sha256"] = df["phone"].map(norm_phone).map(sha)
df[["email_sha256", "phone_sha256"]].dropna(how="all").to_csv("tiktok_upload_hashed.csv", index=False)
```

Never write raw customer files into `ads-master/`. Delete local raw copies after upload.

## 11. Seed quality ranking for lookalikes and value signals

| Rank | Seed | Why |
|------|------|-----|
| 1 | Top 20% customers by 12-month value | Teaches the system what valuable buyers look like |
| 2 | All purchasers, last 180 days | Volume plus intent |
| 3 | Qualified leads or SQLs from CRM (lead gen) | Quality over raw form fills |
| 4 | App payers or subscribers | Monetization signal |
| 5 | Add to cart or checkout starters, 30 days | Intent without purchase |
| 6 | 6-second or 100% video viewers | Attention, weak purchase signal |
| 7 | Followers of the brand account | Affinity, weak purchase signal |

## 12. Smart+ audience controls procedure
1. Start from automatic targeting.
2. Open audience controls and set only what is required: locations, minimum age, languages if creative is single-language.
3. Enforce settings that are legal or contractual requirements (age floors for alcohol, gambling, dating, weight management; geo for licensed services).
4. Add exclusions (recent purchasers, existing customers) where the KPI is new customers.
5. Record every enforced control in the launch plan with the reason. Unexplained restrictions get removed at the next audit.

## 13. Audience naming convention

```
CA_{Source}_{Event}_{Window}        CA_WEB_PURCH_180D, CA_ENG_6SVIEW_30D, CA_CRM_SQL_365D
LAL_{Seed}_{Size}_{Market}          LAL_TOP20VALUE_BAL_US
EXCL_{What}                          EXCL_CUSTOMERS_ALL
```
