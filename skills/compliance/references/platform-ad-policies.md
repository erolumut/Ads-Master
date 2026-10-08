# Platform Ad Policies

> Knowledge as of 2026-10. Working summaries of the ad and store policies that most often decide whether an asset runs. Policy text governs; re-read the live page and changelog before a regulated launch (Freshness protocol in the SKILL). Platform approval is not legal clearance, and legal compliance does not guarantee platform approval. Account level work (appeals, certifications, special ad category settings) is done by the channel agent; this module tells it what is needed.

## 1. Where the rules live

| Platform | Policy center | Changelog | Notes |
|----------|---------------|-----------|-------|
| Meta | transparency.meta.com/policies/ad-standards | Policy pages show "Policy details" dates | Health and Wellness standard dated 2026-07-22 |
| Google Ads | support.google.com/adspolicy | Advertising Policies Help "change log" and update notices per policy | 35 policy updates in 2025 (Ads Safety Report) |
| TikTok | ads.tiktok.com/help (Advertising Policies) | "Key TikTok Ad Policy Updates" change log 2026 | Many 2026 updates in finance, gambling, alcohol, weight |
| Microsoft Advertising | Microsoft Advertising policies site | Monthly policy update posts | Healthcare restructure 2026-07-01 |
| LinkedIn | linkedin.com/legal/ads-policy | No public changelog | Political ads banned since 2019 |
| OpenAI (ChatGPT ads) | openai.com/policies/ad-policies | Versioned changelog on the page | v1.6 dated 2026-09-10; see chatgpt-ads module |
| Apple App Store | developer.apple.com/app-store/review/guidelines | Apple Developer news | Revisions 2026-02-06 and 2026-06-08 |
| Google Play | Play Developer Program Policy and Policy Deadlines page | Policy announcements (2026-04-15, 2026-07-15) | At least 30 days to comply after announcements |

## 2. Meta (Facebook, Instagram, Threads, Messenger, WhatsApp)

| Rule ID | Rule | Source |
|---------|------|--------|
| PLAT-META-01 | Personal attributes: ads must not assert or imply personal attributes, directly or indirectly: race, ethnic origin, religion, beliefs, age, sexual orientation or practices, gender identity, disability, physical or mental health (including medical conditions), vulnerable financial status, trade union membership, criminal record, name. "Are you overweight?", "Struggling with debt?", "Other Christians near you" fail; "For people who want to get fit" passes | Meta Advertising Standards [Official; page cited as updated 2024-06-26] |
| PLAT-META-02 | Health and Wellness (policy date 2026-07-22): weight loss or gain products, cosmetic procedures and dietary or health supplements targeted 18+; no content that disparages appearance; no pinched fat close-ups, no promises of results from wearables only, no sensational timeframes without qualifiers; before and after depictions allowed for general cosmetic products, procedures and surgeries targeting 18+; weight loss before and after is no longer auto rejected according to vendors but the official wording is unclear [Contested]; curative claims for listed diseases prohibited | Meta Transparency Center 2026-07-22 [Official]; vendor reading [Contested] |
| PLAT-META-03 | Special ad categories: housing, employment, financial products and services (expanded from "credit" in 2025-01 for the US: credit, insurance, investments, banking, payments), social issues, elections or politics. Declare the category; targeting is restricted (age typically fixed 18 to 65+, no gender, no ZIP or fine geography, limited detailed targeting, lookalikes restricted) | Meta Help and developer docs [Official]; start date 2025-01-14 or 2025-01-21 [Contested] |
| PLAT-META-04 | Restricted goods with written permission or certification: online pharmacies and prescription drugs (LegitScript), cryptocurrency trading platforms and services (licence via Authorizations and Verifications), real money gambling, dating; alcohol and some categories prohibited where local law bans | Meta restricted goods and services pages [Official] |
| PLAT-META-05 | EU: no political, electoral or social issue ads since 2025-10-06 | Meta newsroom 2025-07 [Official] |
| PLAT-META-06 | Health and wellness data restrictions (since 2025-01): health related advertisers may lose access to lower funnel optimization events and custom conversions; do not rename events to bypass | Meta, see meta-ads module [Official] |
| PLAT-META-07 | AI: "AI info" label for ads made or significantly edited with Meta generative tools (2025) and detected third party AI media via C2PA and similar signals (from 2026-06-01); political and social issue ads must disclose realistic digital alteration | See ai-disclosure-and-synthetic-media.md |
| PLAT-META-08 | Alcohol pages lost algorithmic recommendation eligibility on Facebook in 2026 without a published ad policy change (reported, possibly a bug) | Spirits trade reports 2026 [Unverified] |

## 3. Google Ads (Search, PMax, YouTube, Demand Gen, Shopping)

| Rule ID | Rule | Source |
|---------|------|--------|
| PLAT-GOOG-01 | Misrepresentation, including dishonest pricing practices (enforced from 2025-10-28): disclose payment model and full cost; no omitted taxes or fees; no bait and switch; no "free" paid apps; free trials must state length and auto charge; warning at least 7 days before suspension | Google Ads Help [Official] |
| PLAT-GOOG-02 | Unreliable claims and unacceptable business practices: unrealistic promises, misleading health claims, hidden business information, impersonation, fake reviews | Google Ads Help [Official] |
| PLAT-GOOG-03 | Healthcare and medicines: prescription drug terms usable in non promotional contexts since 2025-10-29, keyword targeting of them requires certification; online pharmacies certified (LegitScript or national); India certified online pharmacies may promote prescription drug services (2026-04); Spain certified telemedicine providers from 2026-08 (no drug names in ads or landing pages) | Google Ads policy updates 2025-10, 2026-04, 2026-07 [Official] |
| PLAT-GOOG-04 | Financial services verification: required in many countries; extended to 24 more EEA markets announced 2026-06-23 with rolling enforcement from 2026-07-23 (verification via partner G2, then Google application; agencies running the ads also verify); UK covered by earlier rules; US personal loan restrictions | Google Ads Help 17127726; Google blog 2026-06 [Official] |
| PLAT-GOOG-05 | Crypto: EU exchanges and software wallets need MiCA CASP authorisation plus Google certification (since 2025-04-23); other countries per local list | Google policy update 2025-03 [Official via CoinDesk] |
| PLAT-GOOG-06 | Gambling and games: certification per country; good policy health for new applicants (2026-03-23) and for all gambling categories (2026-09-14); not on free platforms or third party subdomains; landing page needs age warning, addiction resources, terms, licensee name and number, privacy policy naming the controller; revised application forms from 2026-08-26 | Google Ads Help 2026-03 to 2026-08 [Official] |
| PLAT-GOOG-07 | Alcohol: unified global policy from 2026-09-30 with one table of allowed countries (not listed means not allowed); mixers allowed for legal purchase age audiences; home brewing kits and distilling equipment explicitly allowed; 0% alcohol in Egypt, India and Indonesia needs certification (earlier permissions revoked 2026-09-30); THC drinks fall under dangerous products | Google Ads Help 17452318; SER 2026-08 [Official] |
| PLAT-GOOG-08 | Personalized advertising policy: no targeting by sensitive interests (health conditions, financial hardship, sexual orientation, religion and others); updates published 2026-01 and 2026-09 (read the notices before audience builds) | Google Ads Help 16828044, 17598957 [Official; content of 2026 updates not reviewed] |
| PLAT-GOOG-09 | Political content: election ads need verification and "Paid for by" disclosures; altered or synthetic content disclosure for election ads; Google stopped serving EU political ads (2025-10) | Google [Official] |
| PLAT-GOOG-10 | AI labeling (2026-07): advertisers may add text or visual AI labels inside AI generated or modified creatives without breaching overlay rules; Google may auto label some assets from its own AI tools; an AI label setting rolled out across Google Ads, DV360, CM360, Merchant Center and Editor | Google Ads Help 17257106 (via creative-strategy module) [Official] |
| PLAT-GOOG-11 | Destination requirements: landing page must work, match the ad, not be under construction, not cloak; final URL expansion (PMax, AI Max) can send traffic to pages that make unreviewed claims, so sweep all crawlable pages | Google Ads Help [Official] |

Scale reference: Google's 2025 Ads Safety Report (published 2026-04) reports 8.3 billion ads blocked or removed (up about 63% from 5.1 billion), 24.9 million advertiser accounts suspended (39.2 million the year before), 4.8 billion ads restricted, 602 million scam related ads, and an 80% cut in incorrect suspensions claimed by Google [Official, Google 2026-04].

Read disapprovals via the API (Google Ads Query Language):

```sql
SELECT campaign.name, ad_group.name, ad_group_ad.ad.id,
       ad_group_ad.policy_summary.approval_status,
       ad_group_ad.policy_summary.review_status,
       ad_group_ad.policy_summary.policy_topic_entries
FROM ad_group_ad
WHERE ad_group_ad.policy_summary.approval_status IN ('DISAPPROVED', 'APPROVED_LIMITED', 'AREA_OF_INTEREST_ONLY')
```

## 4. TikTok

| Rule ID | Rule | Source |
|---------|------|--------|
| PLAT-TT-01 | Prohibited: political ads (including issue ads), and political paid creator content | TikTok Advertising Policies [Official] |
| PLAT-TT-02 | 2026 change log entries (read each before launch): weight management and body image (2026-05), weight loss and muscle gain (2026-07), financial services (2026-06, 2026-07), investment consultation or advice (2026-07), precious metals trading and CFDs (2026-08), crypto mining devices (2026-07), social casinos and rewarded gaming (2026-06), online casinos and prediction markets (2026-07), lotteries (2026-08), online gambling (2026-10), alcohol and market specific requirements (2026-06 to 2026-08), 0% alcohol (2026-07) | TikTok "Key TikTok Ad Policy Updates" 2026 [Official; rule text not reviewed] |
| PLAT-TT-03 | AI generated or significantly edited content needs the AIGC label or a clear disclaimer; ads that use AI voices or likenesses to simulate celebrity or influencer endorsements are prohibited | TikTok ad policy [Official via creative-strategy module]; celebrity rule [Unverified] |
| PLAT-TT-04 | Custom Identity phased out: new campaigns run from a verified TikTok profile (affects disclosure: the brand identity is always shown) | TikTok business blog 2026 [Official] |
| PLAT-TT-05 | Weight management products 18+, no before and after body comparisons, no unrealistic results [verify current text] | TikTok policy [Unverified detail] |

## 5. Microsoft Advertising

| Rule ID | Rule | Source |
|---------|------|--------|
| PLAT-MS-01 | Political and issue ads prohibited (ban expanded 2025-09 for TTPA, covers issue based ads such as climate, immigration, taxation) | Microsoft [Official via secondary] |
| PLAT-MS-02 | 2026-01 updates: definitions for games of skill, chance and social sweepstakes casinos; pre-approval for all gaming advertisers; online pharmacy pre-approval; crypto exchange ads in 29 European countries if eligible; UK less healthy food rules from 2026-01-05 | PPC News Feed 2026-01 [Official via secondary] |
| PLAT-MS-03 | Healthcare policy restructured 2026-07-01 (market specific sections for 130+ markets; consumer targeted sensitive health condition ads not allowed; clinical trial recruitment banned, unlike Google) | PPC News Feed 2026-07 [Official via secondary] |
| PLAT-MS-04 | Government services (2026-08-19): third party providers need documented authorisation and pre-approval; aggregators, affiliates and lead gen barred; must disclose they are not the government and separate their fees | PPC News Feed 2026-08 [Official via secondary] |
| PLAT-MS-05 | Gambling market changes (2026-05: Taiwan social and sweepstakes casinos; Belgium casino, sports betting, fantasy on Search); US prediction markets pilot for CFTC designated contract markets in select states | ALM Corp 2026 [Unverified detail] |

## 6. LinkedIn

| Rule ID | Rule | Source |
|---------|------|--------|
| PLAT-LI-01 | Prohibited: political and issue ads (since 2019), illegal products, tobacco and e-cigarettes, drugs, weapons, adult content, counterfeit, gambling and sweepstakes, misleading health and weight loss claims; LinkedIn may reject any ad at its discretion | LinkedIn Advertising Policies [Official] |
| PLAT-LI-02 | Restricted with prior authorisation and market limits: alcohol, dating, pharmacy and telehealth, medical devices, financial services (UK needs FCA authorisation), crypto | LinkedIn policy; vendor summaries [Official; tier detail Unverified] |
| PLAT-LI-03 | Health: may restrict any health related advertising and audience practices implying sensitive health information; EU DSA bans ads based on special category profiling and profiling based ads to minors | LinkedIn; DSA Art 26 and 28 [Official] |
| PLAT-LI-04 | Job ads: no targeting by protected characteristics; no discriminatory hiring language | LinkedIn Help [Official] |

## 7. OpenAI ChatGPT ads (summary; full module in chatgpt-ads)

- Allowed verticals in all available markets: lifestyle and household goods, local services, travel and experiences, entertainment, digital products and education. Restricted (US only, approved advertisers, manual review): financial services, health services, legal services. Disallowed: adult and dating, alcohol and tobacco, counterfeit, gambling, individual job and housing listings, political content, recreational drugs, scams, sensitive social topics, weapons, wellness products with unsupported health claims. No ads to users identified or predicted under 18, or in sensitive conversations (mental health, personal health). Copy must not imitate ChatGPT or imply OpenAI endorsement. [Official, OpenAI Ad Policies v1.6, 2026-09-10, via chatgpt-ads package]

## 8. App stores

| Rule ID | Rule | Source |
|---------|------|--------|
| PLAT-APPLE-01 | Guideline 2.3 accurate metadata: description, screenshots, previews and privacy information match the app; 2.3.7 names up to 30 characters, no prices, no irrelevant keywords or competitor names in metadata; 2.3.8 metadata suitable for a 4+ audience; "For Kids" phrasing reserved for the Kids category | Apple App Review Guidelines [Official] |
| PLAT-APPLE-02 | 2026-06-08 revision: clarified 4.3(a) and 4.3(b) spam and lookalike apps (low effort apps in saturated categories can be removed), a new 1.2 paragraph on responsibility for user generated content, 4.5.3 note on Live Activities; 2026-02-06 revision put random or anonymous chat apps under 1.2 | Apple Developer news; MacRumors 2026-06-09 [Official] |
| PLAT-APPLE-03 | Medical and health apps (1.4.1) must disclose methods and data; gambling and lotteries (5.3) need licences, geo restriction and must be free on the store; subscriptions (3.1.2) need clear terms | Apple guidelines [Official, canonical] |
| PLAT-PLAY-01 | Metadata policy: no performance or ranking claims ("#1", "best", "top"), prices, promotions or "free" in the app title, icon or developer name; no misleading or irrelevant keywords; no fake testimonials | Google Play Developer Program Policy [Official, canonical] |
| PLAT-PLAY-02 | Health apps: health data rules expanded for Android 16 and Health Connect data types (announcement 2026-04-15, at least 30 days to comply); health record data access needs justification; organisation account registration for finance and health apps reported with a 2026-09-30 deadline | Play Console Help 2026-04-15 [Official]; registration deadline [Unverified] |
| PLAT-PLAY-03 | Financial services: personal loan policy (APR and repayment disclosures, minimum repayment period, US APR limit); earned wage access and personal loan clarifications in the 2026-07-15 announcement (enforcement unchanged per Google); third party AI integrations must meet User Data consent and disclosure rules | Play Console Help 2026-07-15 [Official] |

## 9. Most common rejection reasons and fixes

| Rejection | Platforms | Typical trigger | Fix |
|-----------|-----------|-----------------|-----|
| Personal attributes | Meta | "Are you...", "your debt", "your acne" | Talk about the product or the situation |
| Unrealistic or misleading claims | All | Guaranteed results, miracle wording, unqualified numbers | Approved claim with source |
| Before and after | Meta, TikTok, Google | Body comparison, implied timeline | Product in use; check 2026 Meta rules for cosmetic procedures |
| Unapproved substances or health products | Google, Meta | Supplements with banned ingredients, peptides, SARMs | Remove product |
| Financial services not verified | Google | Missing G2 verification in the target country | Channel agent completes verification before launch |
| Dishonest pricing | Google | Missing fees, unclear trial terms | Full price and trial terms in ad and landing page |
| Destination mismatch | All | Landing page claims or prices differ from the ad | Align page; compliance reviews both |
| Special ad category not declared | Meta | Credit, insurance, housing, jobs ads without the category | Declare; accept targeting limits |
| Gambling or alcohol country not allowed | Google, Meta, TikTok | Targeting outside the allowed list | Geo exclusion per policy table |
| Political or social issue | Meta, Google (EU), all on TikTok, LinkedIn, Microsoft | Brand ad mentions a law, election or contested issue | Remove issue framing or do not run in the EU |
| AI or synthetic media undisclosed | TikTok, Meta (political), Google (election) | Realistic AI people or events | Label and disclose |
| Trademark | Google, Microsoft | Competitor or licensed brand terms in ad text | Remove or obtain authorisation |
| Circumventing systems | All | Cloaking, rotating domains, masked content | Never; account level risk |

## 10. Appeals and policy health

1. Read the exact policy cited in the disapproval; compare with the live text.
2. If the ad violates: fix the ad and landing page, resubmit; do not appeal a true violation (repeat violations hurt account health and can lead to suspension).
3. If wrongly flagged: appeal with the specific reason and evidence (certificate, licence, landing page screenshot).
4. Log every rejection with policy name and date in the review log; three rejections for the same policy in 30 days triggers a registry update (new Blocked or Needs review row).
5. Account level suspensions are a stop condition: the channel agent pauses related launches and the human decides on appeals.
