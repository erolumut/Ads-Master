# App Growth Audit Checklist (scored)

> Knowledge as of 2026-10. Score each item 0 (missing or broken), 1 (partial) or 2 (done and verified). Multiply by the weight from the severity. Record the evidence (file, screen, report and date) for every score; an item without evidence scores 0. Sections that do not apply (for example networks at Starter tier) are marked N/A and removed from the denominator.

Severity weights: Critical x3, High x2, Medium x1, Low x0.5.

## A. Measurement and attribution (weight of section: 25%)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | Revenue truth defined (RevenueCat, Adapty or backend) and reconciled with store reports within 5% | All targets depend on it | Compare 28 days of proceeds | Critical | Server notifications V2 and RTDN, webhook QA |
| A2 | MMP or equivalent attribution live with cost ingestion for every paid network | Channel comparison | MMP integrations page | Critical | Integrate or remove the channel |
| A3 | AdServices attribution for Apple Ads flows to MMP or RevenueCat | Apple Ads keyword decisions | Keyword level installs visible downstream | High | Enable token collection |
| A4 | SKAN 4 conversion schema live, documented in MEASUREMENT.md, aligned with bid events | iOS optimization | MMP SKAN config, last change date | Critical | Design per measurement module section 5 |
| A5 | AdAttributionKit implemented alongside SKAN | Future proofing, re-engagement | SDK versions, AAK postbacks present | Medium | Update SDKs |
| A6 | Google iOS on-device conversion measurement and ICM (if Google iOS spend) | iOS performance on Google | Google Ads diagnostics | High | Implement ODM and ICM |
| A7 | Subscription lifecycle events (trial, purchase, renewal, refund) sent server side to MMP and networks with value and currency | Deep funnel bidding | Event logs, duplicate check | High | Server to server integration |
| A8 | No fingerprinting or IP matching for ATT denied iOS users; MMP methods documented | Policy and legal risk | Written MMP answer in MEASUREMENT.md | Critical | Disable; document |
| A9 | ATT prompt timing tested; opt-in rate tracked by country; EU alternative prompt copy ready for iOS 27.2 | Signal volume and EU compliance | Analytics and copy doc | Medium | Run the timing test; prepare copy |
| A10 | Weekly data QA table run, with thresholds | Bad data breaks bidding | Journal entries | High | Add to heartbeat |
| A11 | At least one incrementality read (geo holdout, lift or brand pause test) in the last 12 months for the largest channel | Calibrated targets | MEASUREMENT.md incrementality table | Medium (Growth), High (Scale) | Plan with measurement |

## B. Store presence and ASO (weight: 20%)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Name, subtitle and keyword field use all available characters with no duplicated words and no competitor names | Search reach, policy | App Store Connect | High | Keyword map |
| B2 | Google Play title, short and full description optimized without policy violations | Search reach | Play Console | High | Rewrite |
| B3 | Product page conversion rate at or above peer benchmark in App Store Connect | Multiplier on all traffic | Analytics peer benchmarks | High | Creative program, PPO |
| B4 | First 3 screenshots communicate outcome; localized for top 5 revenue markets | Conversion | Visual review | High | Redesign |
| B5 | PPO or store listing experiment run in the last 90 days | Learning velocity | Test history | Medium | Test calendar |
| B6 | Custom product pages and custom store listings mapped to ad groups, campaigns and keyword clusters | Message match | CPP registry | Medium (Starter), High (Growth+) | Build portfolio |
| B7 | App Store Tags reviewed (irrelevant tags deselected) | Discovery accuracy | App Store Connect | Low | Review |
| B8 | New creative assets (header, search result asset) planned or live for iOS 27 | Early mover advantage | Asset Library | Low | Plan with creative |
| B9 | Localization coverage matches revenue and opportunity (50 Apple languages available) | Market reach | Locale list vs revenue by country | Medium | Locale waves |
| B10 | Android vitals below bad behavior thresholds; iOS crash rate stable | Visibility and ratings | Vitals, Organizer | Critical if breached | App team fix |
| B11 | Target API 36 met (or extension) and current Apple SDK minimum met | Ability to ship updates | Play Console, Xcode build settings | Critical | Update build |

## C. Paid user acquisition (weight: 20%)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Targets per channel derived from LTV and payback, written in PROJECT_BRIEF.md | Avoids bidding on aspiration | Unit economics memo | Critical | Build memo |
| C2 | Apple Ads structure: BRAND, CATEGORY, COMPETITOR, DISCOVERY with cross-negatives; Search Match only in DISCOVERY | Clean data and costs | Apple Ads UI | High | Restructure |
| C3 | Apple Ads keywords judged on cost per trial or payer, not CPI | Quality | Joined keyword report | High | Join with RevenueCat or MMP |
| C4 | Maximize Conversions used only where install quality is uniform; CPA caps migration planned | Avoid cheap low quality installs | Campaign settings | Medium | Rebalance |
| C5 | Google App campaigns budgets meet ratios (50x tCPI, 10x tCPA, 15x ACe); bid event volume at least 10 users per day | Learning | Campaign settings vs conversions | High | Adjust event or budget |
| C6 | iOS and Android split in Meta, Google and TikTok where economics differ | Budget allocation | Campaign list | Medium | Split |
| C7 | Meta and TikTok ad sets reach about 50 bid events per week | Exit learning | Delivery status | High | Consolidate or shallower event |
| C8 | Creative throughput meets tier cadence; registry kept | Main performance lever | creative-library/registry.csv | High | Creative system |
| C9 | Networks and DSPs run as test cells with fraud checks and publisher blocklists | Waste and fraud | MMP fraud reports | Medium | Protocol |
| C10 | Change log with timestamps and approvals for every live change | Cause and effect | Journal, actions.jsonl | High | Enforce |
| C11 | Brand incrementality tested on Apple Ads and Google brand search | Cannibalization | Test record | Medium | Run test |

## D. Monetization and paywall (weight: 15%)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Paywall shows billed amount, period, trial terms, restore, terms and privacy links | Policy and trust | Screenshots | Critical | Fix design |
| D2 | At least 2 paywall or pricing tests in the last 6 months, judged on net revenue per install | Monetization learning | Test log | High | Test calendar |
| D3 | Trial length and plan mix chosen from tests, not copied | Category variance | Test log | Medium | Test |
| D4 | Billing grace period and retry enabled (Apple); grace and account hold reviewed (Google) | Involuntary churn | Store settings | High | Enable |
| D5 | Win-back offers and Retention Messaging (fall 2026) configured or planned | Recovered revenue | App Store Connect, Play Console | Medium | Configure with lifecycle-crm |
| D6 | Web to app or link out evaluated with a fee model per market | Margin | Memo with fee table | Medium (High for US heavy subscription apps) | Model and test |
| D7 | Refund rate monitored by plan and channel | Hidden losses | RevenueCat or store reports | Medium | Investigate spikes |

## E. Retention, ratings and engagement (weight: 10%)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Activation event defined and D1 activation tracked | Retention root | Analytics | High | Define |
| E2 | Rating prompt uses system APIs, triggered after success moments, never gated by sentiment | Policy and rating | Code and analytics | High | Fix triggers |
| E3 | 1 to 2 star reviews replied within 72 hours | Ratings and trust | Review tool | Medium | Process |
| E4 | In-app events and promotional content calendar for the next quarter | Discovery and reactivation | Calendar | Medium | Plan |
| E5 | Deep links QA matrix passed in the last release | Campaign and CRM continuity | QA log | High | Fix and retest |
| E6 | Lifecycle flows exist for onboarding, trial end and win-back | Retention | lifecycle-crm handoff | Medium | Handoff |

## F. Compliance and policy (weight: 10%)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | All store and ad claims in brand/CLAIMS.md as approved | Rejections and legal risk | Claims registry | Critical | Compliance review |
| F2 | Age rating answers current, including social media capability question | Submission blocks | App Store Connect | High | Update |
| F3 | Privacy labels, privacy manifest and Data safety section match SDKs | Policy | SDK list vs declarations | High | Update |
| F4 | External purchase links only where allowed, with program enrollment (Google) | Removal risk | Paywall code by storefront | Critical | Gate by storefront |
| F5 | Category requirements (finance, health, medical device, gambling, kids) met | Removal risk | Checklist | Critical when applicable | Fix |
| F6 | No purchased installs, reviews or rank manipulation | Account termination risk | Vendor list | Critical | Stop |

## Scoring rubric

1. Section score = sum(item score x severity weight) / sum(2 x severity weight) for applicable items.
2. Overall score = sum(section score x section weight).
3. Grades:

| Overall | Grade | Meaning |
|---------|-------|---------|
| 90% to 100% | A | Top tier operation; focus on scale and incrementality |
| 75% to 89% | B | Solid; fix the High items in 30 days |
| 60% to 74% | C | Leaking value; fix Critical and High items before adding spend |
| 40% to 59% | D | Measurement or store foundations broken; freeze scaling |
| under 40% | F | Rebuild foundations; paid spend likely unprofitable |

4. Override: any Critical item scored 0 caps the grade at C, and any Critical item in sections A or F scored 0 is reported first in the top 5 fixes.

## Audit report template

```
# App growth audit: <app>, <date>
Data used: <sources, date ranges, attribution sources>; Freshness check: <date>
Tier and maturity: <Starter/Growth/Scale/Enterprise>, <new/running/plateau/scaling>
Score: <overall %>, grade <A to F>; section scores A to F
Top 5 fixes (impact x confidence x ease)
Findings by section (item, score, evidence, fix)
Quick wins (under 1 week)
30, 60, 90 day plan
Change list (approval lines)
Handoffs requested
Data gaps and [Unverified] items
```

## Quick audit (30 minutes, cold start)

When only store access and one export exist, score these 10 items first and state the rest as data gaps:
1. A1 revenue truth, 2. A4 SKAN schema, 3. B3 product page conversion vs peers, 4. B10 vitals and crash rate, 5. C1 targets from unit economics, 6. C2 Apple Ads structure, 7. D1 paywall disclosures, 8. D2 paywall tests, 9. E2 rating prompt rules, 10. F4 external links by storefront.

## Evidence log template

| Item | Score | Evidence (file, screen, report) | Date range | Notes |
|------|-------|----------------------------------|-----------|-------|
| A1 | 1 | RevenueCat overview vs App Store Connect proceeds, 8% gap | 2026-09-01 to 2026-09-28 | Refund events missing |

## Scoring example

Section D with D1 (Critical, score 2), D2 (High, score 0), D4 (High, score 1), D7 (Medium, score 1): earned = 2x3 + 0x2 + 1x2 + 1x1 = 9; possible = 2x3 + 2x2 + 2x2 + 2x1 = 16; section score 56%.
