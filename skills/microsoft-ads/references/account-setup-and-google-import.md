# Account Setup and Google Import

> Scope: account hierarchy, pre-launch setup, Google Import (one time and scheduled), the post-import fix list and the decision of when to diverge from Google. Evidence labels follow the spec. Import option names drift; confirm in the Import Center before running.

## 1. Account hierarchy and access

| Level | What lives here | Notes |
|-------|----------------|-------|
| Manager account (customer) | Users, billing setup, linked accounts, cross-account portfolios (since 2026-05) | Agencies manage many accounts from one manager account |
| Account | Time zone, currency, billing, UET tags, conversion goals, audiences, Merchant Center store links, shared libraries (negative keyword lists, website exclusion lists, brand lists) | Currency and time zone cannot be changed later; create a new account if wrong |
| Campaign | Type (Search, Shopping, PMax, Audience, vertical types), budget, bid strategy, locations, languages, ad schedule, device settings, AI Max settings | Campaign names up to 400 characters since 2026-04 [Official, 2026-04] |
| Ad group | Keywords or audiences, ads, ad distribution, ad group level targeting and bid adjustments | Microsoft keeps more ad group level targeting than Google; check both levels when auditing |
| Asset group (PMax) | Assets, audience signals, listing groups, asset group URL options (tracking template, custom parameters since 2026-01) | [Official, 2026-01] |

Access checklist:
- [ ] Human owner holds Super Admin; agencies get Standard or campaign manager roles, not ownership.
- [ ] Multi-factor authentication on every user (required for UI and API sign in) [Practitioner consensus].
- [ ] Billing: payment method, invoice eligibility, spending limits checked. Prepay accounts stop serving when funds run out; set a low balance alert.
- [ ] Advertiser identity verification completed if prompted; unverified accounts can be limited [Unverified] for current scope.

## 2. Pre-launch setup (do in this order)

1. **Account settings.** Time zone matching the business day and the Google account (so day parting and pacing compare cleanly). Currency matching backend reporting.
2. **Auto-tagging.** Turn on Microsoft Click ID (MSCLKID) auto-tagging. Decide UTM auto-tagging: if the site relies on hand-built UTMs, choose the option that keeps existing UTMs; never let two systems write conflicting UTMs.
3. **UET tag.** Create one UET tag per website (not per campaign). Install through GTM or the site platform integration. Verify with UET Tag Helper. See [Measurement](measurement-uet-and-conversions.md).
4. **Consent mode.** For any EEA, UK or Swiss visitors, UET consent mode must send a default of denied before the CMP loads and update to granted on consent. Required since 2025-05-05 [Official, 2025-03].
5. **Conversion goals.** Create goals for the primary conversion (purchase, qualified lead) and secondary goals. Set "Include in conversions" only on goals you want bidding to optimize. Set values (static or dynamic revenue).
6. **Microsoft Merchant Center (ecommerce).** Create a store, verify and claim the domain, connect a feed (direct file, scheduled fetch, Shopify integration or Google Merchant Center import). See [PMax and Shopping](performance-max-and-shopping.md).
7. **Microsoft Places (local).** Claim the business listing (formerly Bing Places) for location assets and local signals.
8. **Clarity.** Link a Microsoft Clarity project for session insight on paid traffic and AI referral data.
9. **Shared libraries.** Account negative keyword list (brand protection, irrelevant terms), website exclusion list (known bad publishers), brand list (for PMax brand exclusions).
10. **Billing alert and budget plan.** Approved monthly budget and daily caps per campaign.

## 3. Google Import: methods

| Method | Use when | Notes |
|--------|----------|-------|
| Import Center (Google, Meta, Pinterest) | Default for new accounts and migrations; shows what is being moved and gives suggestions | Updated 2026-05 [Official, 2026-05] |
| Sign in to Google Ads and import selected accounts or campaigns | Standard for Google to Microsoft | Choose campaigns, then import options |
| File import (Google Ads Editor export) | No Google login available, or you want to edit before upload | Gives full control; no scheduling |
| Scheduled import | Google is the master and you want new keywords, ads and negatives copied | Highest risk of overwriting Microsoft changes |
| Microsoft Advertising Editor import | Bulk edit before posting | Lets you review every entity before it goes live |

## 4. What transfers, what breaks

| Element | Transfers | What to check or fix after import |
|---------|-----------|-----------------------------------|
| Search campaigns, ad groups, keywords, match types | Yes | Remove Google only experiments and drafts first; check keyword status for editorial disapprovals |
| Negative keywords and lists | Yes | Rebuild account level negatives as Microsoft shared lists |
| Responsive search ads | Yes | Pinning carries; check ad strength; ad customizers may not map [Unverified] |
| Assets (sitelinks, callouts, structured snippets, call, price, promotion, image) | Mostly | Location assets need Microsoft Places; call assets may need phone verification; image assets may need new crops |
| Bid strategies | Mapped where an equivalent exists | Re-set targets from Microsoft data after 14 to 30 days; if Microsoft has no conversion history, start on a non-target strategy |
| Budgets | Yes (currency converted if needed) | Re-size to Microsoft volume, not Google's |
| Locations, languages, ad schedule | Yes | Fix location intent, check time zone, check language settings |
| Bid adjustments (device, location, schedule) | Yes where supported | Add Microsoft only adjustments later from data (age, gender, LinkedIn profile) |
| Audiences | Not the lists themselves | Recreate remarketing from UET, re-upload customer match where allowed; map observation to "Bid only" and targeting to "Target and bid" |
| Conversion actions | No (Google tags are not Microsoft goals) | Create UET goals before any conversion based bidding |
| Tracking templates and final URL suffix | Yes | Replace {gclid} with {msclkid} where hard coded; check {network} values; see ValueTrack table |
| Performance Max | Yes, including new customer acquisition goals since 2026-04 | Check asset groups, listing groups, brand exclusions, negatives, URL expansion |
| PMax negative keywords | Yes since 2026-03 | Confirm list links |
| Brand lists | Yes since 2025-05 | Confirm brand exclusions attached |
| AI Max settings | Yes since 2026-08; scheduled imports keep inheriting for matched campaigns | Decide whether Microsoft should mirror Google AI Max or diverge [Official, 2026-08] |
| Shopping campaigns | Yes, needs a Microsoft Merchant Center store with matching products | Product IDs must match the Microsoft feed |
| Display, Video, Demand Gen, App, Smart, Local Services | No or limited | Build Microsoft Audience campaigns separately |
| Experiments, drafts, labels | Labels yes; experiments and drafts no | Re-create experiments in Microsoft |

## 5. ValueTrack and tracking differences

| Purpose | Google | Microsoft | Action |
|---------|--------|-----------|--------|
| Click ID | {gclid} (auto) | {msclkid} (auto when auto-tagging is on) | CRM must store MSCLKID in its own field for offline import |
| Network | {network}: g, s, ytv, d, x | {Network}: o (owned and operated), s (syndicated search partners), a (audience network) [Practitioner consensus] | Update reporting logic and URL rules |
| Match type | {matchtype}: e, p, b | {MatchType}: e, p, b | Same letters; confirm in your data |
| Search query | Not available | {QueryString} returns the search query [Practitioner consensus] | Useful for landing page personalization and analytics; respect privacy policy |
| Device | {device}: m, t, c | {Device}: m, t, c | Same |
| Campaign and ad group IDs | {campaignid}, {adgroupid} | {CampaignId}, {AdGroupId} | IDs differ between platforms; never join on ID across platforms |

## 6. Settings to fix after every import (the post-import fix list)

| # | Setting (UI name) | Fix | Why |
|---|------------------|-----|-----|
| 1 | Locations: "Target" options | Set "People in your targeted locations" unless serving travelers or relocation | Presence or interest leaks spend outside the market |
| 2 | Ad distribution (Search) | Choose owned and operated plus syndicated partners deliberately; review partners after 2 weeks | Partner quality varies by publisher |
| 3 | Audience Network on Search campaigns | Opt out unless the campaign is meant to run display style ads | Prevents unplanned audience placements [Practitioner consensus] |
| 4 | Bid strategy and targets | Start on Enhanced CPC, or Maximize Clicks with a cap inside a portfolio (new non-portfolio campaigns cannot set Max CPC from 2026-10-01), if UET has no history; move to conversion strategies after 30 conversions in 30 days | Imported targets reflect a different auction |
| 5 | Budgets | Re-size to forecast (see [Bidding and budgets](bidding-and-budgets.md)) | Google budgets usually overstate Microsoft volume |
| 6 | Tracking template, final URL suffix | Replace Google only parameters; confirm MSCLKID passes through redirects | Broken click IDs break offline import |
| 7 | Conversion goals | Create UET goals, set primary goal, values, windows | Imported bid strategies need Microsoft goals |
| 8 | Ad schedule | Confirm time zone | Day parting shifts when time zones differ |
| 9 | Device bid adjustments | Reset to 0 and let data decide, or apply known Microsoft splits | Microsoft desktop share is higher than Google's [Practitioner consensus] |
| 10 | Assets | Add logo, business name, images, multimedia ads | Asset richness affects Copilot and right rail eligibility |
| 11 | Audiences | Rebuild remarketing, in-market, LinkedIn layers as Bid only | Lists do not transfer |
| 12 | PMax brand exclusions and negatives | Attach brand lists and negative keyword lists | Brand cannibalization control |
| 13 | AI Max | Decide on or off per campaign; set URL exclusions and term exclusions | Imported setting may not fit Microsoft |
| 14 | Editorial disapprovals | Fix trademark, superlative and policy issues | Microsoft editorial rules differ from Google's |
| 15 | Language | Confirm ad language matches target market | Wrong language reduces eligibility |

## 7. Scheduled import strategy

| Situation | Schedule | Import these | Never import |
|-----------|----------|--------------|--------------|
| Starter, Google is master, no divergence yet | Weekly | New campaigns, ad groups, keywords, ads, negatives, URL changes | Budgets (keep Microsoft budgets) |
| Growth, partial divergence | Weekly or monthly | New keywords, new ads, negatives | Bids, bid strategies, budgets, targeting, ad distribution, bid adjustments |
| Scale, fully diverged | Off; use manual imports or Editor for new builds | Selected new campaigns only | Anything to existing campaigns |
| Enterprise with automation | Off; sync via API with your own diff logic | Defined entities only | Unreviewed changes |

Procedure for setting up a scheduled import:
1. Document which fields Microsoft has diverged on (journal entry).
2. In the import options, set "Do not update" (or the equivalent) for bids, budgets, targets, ad distribution, bid adjustments and URL options you changed.
3. Choose the import frequency and a time after the Google team's typical edit window.
4. After the first scheduled run, read the import history and change history; confirm nothing diverged was overwritten.
5. Log the schedule in `ads-master/journal/` and tell google-ads via a handoff so the Google team knows edits flow to Microsoft.

## 8. When to diverge from Google (decision tree)

```
Is Microsoft spend under $1k per month and CPA within 20% of target?
  yes -> stay mirrored, weekly import of new entities only
  no  -> continue
Does Microsoft have 30+ conversions in 30 days in the campaign?
  no  -> keep structure mirrored; diverge only bids, budgets, location intent, distribution
  yes -> continue
Is the Microsoft CPA or ROAS on matched keywords more than 20% different from Google for 2 consecutive months?
  yes -> diverge bids and targets, stop syncing bids and targets
Is the project B2B with job title or company sensitivity?
  yes -> diverge with LinkedIn profile layers and company lists (no Google equivalent)
Does Microsoft show a different device, age or gender profile that changes CPA by 25%+?
  yes -> diverge bid adjustments
Is the product mix or margin structure different on Microsoft (for example older buyers prefer premium SKUs)?
  yes -> diverge PMax or Shopping product splits
```

## 9. Worked example

A B2B software firm with Google Search at $40k per month imports 6 Search campaigns into Microsoft.
- Day 0: Import Center, all campaigns, budgets scaled to 15% of Google, bid strategies set to Enhanced CPC because UET has no history.
- Day 1: Location intent fixed to "People in", Audience Network off, auto-tagging on, UET goals created for demo request and SQL (offline).
- Day 14: Microsoft CPC is 35% below Google on matched keywords; CVR is equal. Manual bids reset from Microsoft data.
- Day 30: 42 demo requests. Move to Maximize conversions with tCPA set at the 30 day Microsoft CPA plus 10%.
- Day 45: LinkedIn job function "Information Technology" and company size 1,000+ added as Bid only with +25%.
- Day 60: Scheduled weekly import set to new keywords, ads and negatives only.
All figures above are illustrative, not benchmarks.

## 10. Import QA checklist
- [ ] Import summary reviewed: counts of campaigns, ad groups, keywords, ads, assets match expectations.
- [ ] Errors and warnings exported and resolved.
- [ ] No campaign launched before the post-import fix list is complete (import paused campaigns, then enable after QA).
- [ ] Tracking verified with a test click (MSCLKID in landing URL, UET fires, goal records).
- [ ] Journal entry written with what was imported and what was changed after.
