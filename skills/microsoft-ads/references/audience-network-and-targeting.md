# Audience Network and Targeting

> Scope: Microsoft Advertising Network (Audience ads), audience types, LinkedIn profile targeting, remarketing, customer match, demographics and device, and B2B ABM through Microsoft. Programmatic buying through Microsoft Invest is no longer an option (see section 8).

## 1. Microsoft Audience Network inventory

| Inventory | Typical placements | Notes |
|-----------|--------------------|-------|
| Microsoft owned | MSN, Outlook.com, Microsoft Edge new tab, Microsoft Start, Windows surfaces | Ad Preview Hub shows renders for MSN and Outlook (2026-02) and for PMax on MSN, Bing Search and Outlook (2026-07) [Official, 2026-02] [Official, 2026-07] |
| Partner sites and apps | Third party publishers | Use website exclusions and placement reports |
| Connected TV and online video | Video and CTV inventory | Availability by market and through which buying path changed after Microsoft Invest wound down [Unverified] |

Audience campaign ad types:
- Image based responsive Audience ads (images, headlines, descriptions, logo).
- Feed based Audience ads (product ads from Merchant Center for dynamic remarketing).
- Video ads where available.

## 2. Audience types

| Audience | Built from | Best use | Notes |
|----------|-----------|----------|-------|
| Remarketing lists | UET site visitors with rules | Recover cart and lead abandoners | Membership duration up to the platform maximum; consent affects list growth |
| Dynamic remarketing | UET with product IDs plus feed | Ecommerce retargeting | Needs product IDs in UET events |
| Impression-based remarketing | People who saw your ads | Sequential messaging after Audience or video ads | Up to 20 campaigns or ad groups per list since 2025-08 [Official, 2025-08] |
| Customer match | Hashed emails from CRM | Exclusions, upsell, NCA definitions | Requires accepting customer match terms; availability by market [Unverified] |
| Combined lists | AND, OR, NOT of other lists | Exclude converters, layer intent | Build "visited pricing NOT purchased" |
| In-market audiences | Microsoft intent signals | Cold audience acquisition on Audience ads; bid only on Search | Check category list in UI |
| Custom audiences | Data partner or custom definitions | Specific segments | Availability varies |
| LinkedIn profile targeting | Company, industry, job function from LinkedIn | B2B targeting and bid adjustments | Microsoft unique lever; see section 3 |
| Similar audiences | Modeled from lists | Check availability before planning | [Unverified] current status |

Targeting mode:
- **Bid only (observation):** ads show to everyone eligible; bid adjustment applies to the audience. Default for Search.
- **Target and bid:** ads show only to the audience. Default for Audience campaigns.

## 3. LinkedIn profile targeting

What it is: Microsoft uses LinkedIn profile data (company, industry, job function) for targeting and bid adjustments in Microsoft campaigns. LinkedIn is owned by Microsoft, so no other search platform offers this.

| Dimension | Values | Where available | Practice |
|-----------|--------|-----------------|----------|
| Company | Named companies; company lists up to 10,000 names (raised from 1,000 in 2026-09) | Search and Audience campaigns, supported markets | ABM lists from CRM; add at setup or in the audience library [Official, 2026-09] |
| Industry | LinkedIn industry taxonomy | Search, Shopping, Audience; PMax as signal | Bid only on Search with +/- adjustments |
| Job function | LinkedIn job functions (for example Information Technology, Finance, Engineering) | Search, Shopping, Audience; PMax as signal | Bid up decision makers, bid down students and job seekers |

Data scope: LinkedIn profile data used for these features excludes users in the EEA, UK and Switzerland [Official, 2026-09]. For European campaigns, LinkedIn layers do not apply; use keyword intent and remarketing instead.

LinkedIn profile setup procedure for B2B Search:
1. Pull CRM data: closed won and SQL accounts by industry and company size; contacts by function.
2. Add industry and job function layers to non-brand Search campaigns as Bid only.
3. Wait 30 days. Pull performance by layer (Audiences report).
4. Apply bid adjustments: segments with CPA 25%+ better than average get +15% to +40%; segments with CPA 50%+ worse or zero conversions after 2x target CPA spend get -30% to -90%.
5. Add a company list (target accounts from CRM or ABM platform, up to 10,000) as Bid only on Search and Target and bid on an Audience campaign.
6. Review monthly. Log adjustments in the journal.

ABM via Microsoft (cheap complement to LinkedIn Ads):
| Step | Action |
|------|--------|
| 1 | Export target account list (company names exactly as on LinkedIn where possible) |
| 2 | Upload as company list in the audience library |
| 3 | Search: Bid only +30% to +50% on problem and category terms |
| 4 | Audience campaign: Target and bid on the company list with case study creative |
| 5 | Measure: pipeline from target accounts in CRM (MSCLKID or HubSpot integration) |
| 6 | Hand off company list results to linkedin-ads for cross channel ABM |

## 4. Demographics and device

Microsoft keeps age and gender targeting and bid adjustments on Search, which Google does not offer on Search in the same way [Practitioner consensus].

| Dimension | Values | Bid adjustment range | Practice |
|-----------|--------|----------------------|----------|
| Age | 18 to 24, 25 to 34, 35 to 49, 50 to 64, 65+, unknown | Typically -100% to +900% [Unverified] for exact range by type | Apply only after 30+ days and 2x target CPA spend per segment |
| Gender | Male, female, unknown | Same | Respect policy limits in housing, employment and credit categories |
| Device | Desktop, mobile, tablet | -100% to +900% | Microsoft traffic skews to desktop; check CVR by device |
| Location | Countries, regions, cities, postal codes, radius | -90% to +900% [Unverified] | Use for local and regional economics |
| Ad schedule | Day and hour | -90% to +900% [Unverified] | B2B: weekdays office hours often convert better; verify with data |

Audience profile context: Microsoft has long described its search audience as older and higher income than average, with a large desktop share [Practitioner consensus]. Treat this as a hypothesis to test in each account, not a rule.

Restrictions: in regulated categories (housing, employment, credit) and some markets, age, gender and other demographic targeting are limited by policy. Check category rules before applying demographic exclusions [Unverified] for current market list.

## 5. Audience campaign build (cold audience acquisition and remarketing)

| Campaign | Audience | Bidding | Creative |
|----------|----------|---------|----------|
| Remarketing | Site visitors 30 days excluding converters | tCPA or Maximize conversions | Offer, proof, urgency |
| Dynamic remarketing (ecommerce) | Product viewers, cart abandoners | Maximize conversion value | Feed based ads |
| B2B ABM | Company list plus job function | Manual CPC or Maximize clicks at low volume, then tCPA | Case studies by industry |
| In-market acquisition | In-market segments relevant to product | tCPA with a test budget | Brand plus offer |

Rules:
- Exclude converters via combined lists.
- Set website exclusions for known low quality placements; review placement reports every 2 weeks.
- Use the Ad Preview Hub to check rendering before launch.
- Audience ads are judged on view and click based conversions separately; view-through windows inflate results, so compare against a holdout where possible.

## 6. Search campaigns and the Audience Network
Search campaigns can be eligible to serve on the Audience Network depending on settings [Practitioner consensus]. Check each Search campaign's settings and the Ad distribution segment. If audience placements appear in a Search campaign, either opt out or set a bid adjustment that reflects their value. Do not let display style traffic dilute search CPA unnoticed.

## 7. Consent and audience growth
- EEA, UK and Swiss visitors: remarketing lists only grow with consent; consent rates directly cap list size.
- Advanced Consent Mode guidance (2026-02) addresses conversion measurement; do not expect it to restore remarketing for non consenting users [Practitioner consensus].
- Track list size weekly; a sudden drop usually means a tag or CMP change.

## 8. Programmatic changes: Microsoft Invest and Curate
- Microsoft announced in 2025 that Microsoft Invest (the former Xandr DSP) would wind down by early 2026, with Amazon DSP named a preferred partner for advertisers (trade press, 2025-05 and 2025-10) [Practitioner consensus].
- Trade press in 2026-01 reported the DSP shutdown and related Prebid changes on the publisher side [Practitioner consensus].
- Sell side products (Microsoft Monetize, Microsoft Curate) continue, with Copilot features in open beta for publishers since 2026-07 [Official, 2026-07].
- Implication: programmatic CTV and open web buying that used Microsoft Invest must move to another DSP; Audience ads in the Microsoft Advertising platform are separate and continue. Hand off DSP planning to growth-orchestrator.

## 9. Audience ads creative standard

| Asset | Practice |
|-------|----------|
| Images | Supply landscape and square crops; product or person in context; minimal text overlay so automatic cropping does not cut words |
| Short headline | Brand or category plus benefit |
| Long headline | Benefit plus proof (rating, years, customers) |
| Description | Offer and next step |
| Logo | Square and landscape, approved |
| Business name | Exact brand |
| Variants | 3 to 5 image sets per ad group; refresh every 6 to 8 weeks at Growth tier |

Pre-launch checks:
- [ ] Ad Preview Hub renders reviewed on MSN and Outlook (and Bing Search for PMax) [Official, 2026-07].
- [ ] Shareable preview links sent to the human for approval instead of screenshots [Official, 2026-06].
- [ ] Landing page matches the ad promise; Clarity linked to watch sessions.
- [ ] Frequency and placement reports scheduled for the first 2 weeks.

## 10. Brand safety and placement hygiene
1. Apply an account level website exclusion list from day one (known low quality apps and sites from prior accounts).
2. Review placement or publisher reports after the first 1,000 clicks, then every 2 weeks.
3. Exclude placements with CTR over 5x the campaign average and no conversions (possible accidental clicks or invalid traffic).
4. For sensitive brands, restrict Audience campaigns to Microsoft owned placements where the setting allows [Unverified] for current options.
5. Record exclusions in the journal so other channel agents can reuse them.

## 11. Targeting matrix template
| Campaign | Keywords or audience | LinkedIn layer | Age or gender | Device | Mode | Adjustment | Review date |
|----------|---------------------|----------------|---------------|--------|------|-----------|-------------|
| | | | | | Bid only or Target and bid | | |
