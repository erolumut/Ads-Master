# Price Display Law: What to Check and Hand to Compliance

> Offer-strategy designs offers that can be displayed legally; `compliance` decides whether the exact wording and display are legal; `storefront-ux` and `cro` build the display. This module lists the rules that most often break offers, so the design is right before it reaches review. It is not legal advice.

## 1. The rules that break offers most often

| Rule | Where | What it means for the offer | Status Oct 2026 |
|------|-------|-----------------------------|-----------------|
| Prior price rule for announced reductions: the reference price is the lowest price applied in the prior 30 days | EU Price Indication Directive Art. 6a (added by Omnibus Directive 2019/2161), applied from 2022-05-28 | Every "was" price, struck price and percentage refers to the 30 day low; frequent promotions lower the reference | In force [Official, 2019] |
| Percentage reductions must also be calculated from the 30 day prior price | CJEU C-330/23 Aldi Süd, 2024-09-26 | "Minus 20%" computed from a higher interim price is unlawful | In force [Official, 2024-09] |
| Netherlands application | ACM guidance; fines up to EUR 900,000 per violation | Only your own earlier price; recommended retail price cannot suggest a bigger discount; progressive discounts up to 3 months; ACM found misleading claims at 18 of 24 sellers checked before Black Friday 2025 | Active enforcement [Official, 2025] |
| Turkey: discount ads reference the lowest price of the prior 10 days in the same channel | Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği as amended (Official Gazette 2026-07-01, in force 2026-08-01); price tag regulation changed from 30 to 10 days on 2025-10-11 | Website and app tracked separately; loyalty and conditional offers ("2 al 1 öde") in scope; campaign dates and stock limits must be shown | In force [Official, 2026-07, via secondary sources] |
| UK prior price and pricing practices | CMA guidance, DMCC Act unfair practices regime (from 2025-04-06), CMA price transparency guidance CMA209 (2025-11-18) | Reference prices must be genuine; drip pricing is on the blacklist | In force [Official, 2025] |
| Unit pricing | EU Price Indication Directive (selling price and unit price per kg, litre, metre, item), national exemptions; UK Price Marking Order reforms from 2026-04-06 (wider product scope, standard units per kg or litre, ordinary price shown next to loyalty price) | Multipacks and bundles must show unit price where the rules require it | In force [Official, 2026-04] |
| Drip pricing (mandatory fees revealed late) | UK DMCC blacklist since 2025-04-06 (CMA fines: AA and BSM GBP 4.2M, StubHub, Marks Electrical GBP 720,000; new probes opened 2026-08-19); EU inclusive price requirement; US states: California (2024-07-01), Minnesota (2025-01-01), Virginia (2025-07-01), Massachusetts (2025-09-02, total price before collecting personal data), Colorado (2026-01-01), Connecticut (2026-07-01); FTC fees rule covers only live events and short term lodging | Headline price includes all mandatory fees; shipping may be shown separately in most US state laws if it is a real carrier charge | In force [Official and law firm sources, 2025 to 2026] |
| Personalized price disclosure | EU Consumer Rights Directive (Omnibus); New York Algorithmic Pricing Disclosure Act (2025-11-10) | If prices are personalized from personal data, disclose; prefer non-personalized offers | In force; New York One Fair Price Act pending signature [Unverified status] |
| Free claims | EU UCPD Annex I item 20 ("free" when the consumer pays anything beyond the unavoidable cost of responding and delivery); UK equivalent | "Free gift" must be truly free; shipping charges for a "free" item can make the claim unlawful | In force |
| Fake urgency and scarcity | EU UCPD Annex I (false limited time claims); UK DMCC; US FTC Act | Countdown timers and stock counts must be true | In force |
| Former price comparisons (US) | FTC Guides Against Deceptive Pricing (16 CFR Part 233): former price must be a bona fide price offered for a reasonably substantial period; California Business and Professions Code 17501 (former price must be the prevailing market price within the prior 3 months, unless disclosed) | "Compare at" and "was" prices need evidence | In force; class actions common [Official] |
| "Up to X% off" | UK CAP guidance and general misleading practice rules | A meaningful share of the range must carry the maximum reduction [Practitioner consensus] | Ongoing |
| Statutory rights as a selling point | EU UCPD Annex I item 10; UK DMCC | Do not advertise the 14 day withdrawal or 2 year legal guarantee as a special benefit | In force |
| Subscription terms | See [Subscriptions](subscriptions-and-repeat-offers.md) section 6 | Discount duration and renewal price shown at sign-up | Mixed |
| BNPL promotions | UK FCA regime from 2026-07-15; EU CCD2 from 2026-11-20 | Credit promotions need the lender's approved wording | In force or imminent |

Watch list: the EU Digital Fairness Act (proposal expected Q4 2026; consultation asked about an outright ban on drip pricing, unfair personalization and subscription traps); Illinois junk fee bill (2027 if signed); FTC negative option rulemaking (ANPRM 2026-03-13).

## 2. Prior price procedure (EU, UK, Turkey)

1. Store daily price history per SKU and per channel (website and app separately for Turkey). Shopify and many platforms do not compute the 30 day low natively; use an app, the ERP, or a nightly export [Practitioner consensus, verify per platform].
2. Before the promo: compute the lowest price in the lookback window (30 days EU and UK, 10 days for Turkish ads) for each SKU.
3. The struck price and the percentage must use that low. If the product was already reduced in the window, the new reduction is calculated from the reduced price.
4. Exceptions exist (perishable goods, new products on the market for less than 30 days, progressive reductions in some member states); `compliance` decides whether one applies.
5. Keep the evidence file (price history export, date of the check) attached to the change request.
6. After the promo, the promo price becomes part of the next 30 day window. Plan the calendar so the next event does not start from a depressed reference.

## 3. Display requirements the offer must allow (pass to `storefront-ux`)

| Element | Requirement to pass on |
|---------|------------------------|
| Price shown | Total price including VAT and mandatory fees (consumer markets) |
| Reference price | Lowest prior price in the window, labeled clearly (for example "Lowest price in the last 30 days: EUR 59.99") |
| Percentage | Calculated from the reference price |
| Unit price | Per kg, litre, metre or item where required, near the selling price |
| Loyalty or member price | UK: ordinary price shown next to the member price, with conditions nearby |
| Offer conditions | Minimum spend, exclusions, end date and time zone, stock limits (Turkey: campaign dates and stock information) |
| Shipping cost | Shown before checkout; free shipping threshold explained |
| Subscription terms | Price per delivery, cadence, discount duration, how to cancel |
| Gift | What the gift is, limits ("while stocks last" only if true, with quantities where required) |

## 4. Handoff package to `compliance`

```
Offer ID:
Markets and channels:
Exact customer facing wording (ads, PDP, cart, email, feed promotion text):
Price evidence: price history export for each SKU, lookback window used, computed reference price
Offer mechanics: eligibility, exclusions, stacking, dates and time zone
Free claims: what is free and what the customer pays
Urgency claims: deadline source, stock numbers source
Personalization: none | segment based (which segments) | algorithmic (inputs)
Subscription or trial terms (if any)
BNPL or installment messaging (if any)
Deadline for review:
```

## 5. Red flags that stop an offer until compliance clears it
- Any reference price higher than the lowest price in the window.
- "Compare at" prices taken from MSRP or competitors.
- Price increased in the 30 days (EU, UK) or 10 days (Turkey) before a planned discount.
- Free shipping or gift claims where the customer pays a fee to receive the free item.
- Timers that reset, or "only 3 left" counts not tied to inventory.
- Different prices for the same offer by country of residence inside the EU without separate storefronts and legal review (Geo-blocking Regulation 2018/302).
- Price tests that show different list prices for identical items at the same time.
- Subscription preselected by default without clear terms.

## 6. Market notes

| Market | Notes |
|--------|-------|
| Germany | Strict courts and competitor lawsuits (Abmahnung); PAngV implements the prior price rule; unit pricing per kg or litre |
| Netherlands | ACM active every Black Friday season; consumer may annul a purchase made under a misleading discount (consumer law route, verify) |
| France | Prior price rule applies; DGCCRF enforcement; also rules on sales periods (soldes) dates |
| Italy | AGCM consumer enforcement also active on misleading discounts |
| UK | DMCC direct fines by the CMA up to 10% of global turnover |
| Turkey | Reklam Kurulu fines; for 2026 reported ranges are about TRY 1.08M to 10.84M for internet ads and about TRY 0.51M to 5.06M for SMS ads (revalued yearly; verify) [Unverified] |
| US | State laws differ; California 17501 and class actions over "compare at" prices are common; Massachusetts total price before personal data collection |

## 7. Worked example: computing the reference price (EU, 30 day rule)

Price history for SKU A (illustrative): EUR 59.99 from 1 to 20 October, EUR 49.99 from 21 to 25 October (a short promo), EUR 59.99 from 26 October. Black Friday promo planned from 27 November.
- Lookback window: 28 October to 26 November (the 30 days before the reduction).
- Lowest price in the window: EUR 59.99 (the 49.99 promo ended before the window). Reference price EUR 59.99; a promo at EUR 44.99 can be shown as 25% off.
- If the October promo had run to 30 October, the lowest price in the window would be EUR 49.99, and EUR 44.99 could only be shown as 10% off EUR 49.99.
- For Turkish discount ads, run the same logic with a 10 day window per channel (website and app separately).

## 8. Wording examples (for `compliance` to confirm)

| Risky | Safer |
|-------|-------|
| "Was EUR 79.99, now EUR 49.99" where 79.99 was the recommended retail price | "EUR 49.99. Lowest price in the last 30 days: EUR 59.99" |
| "Up to 70% off everything" when 2 items carry 70% | "20% to 70% off selected items" with a real spread |
| "Free gift" when shipping is charged only on gift orders | "Free gift with orders over EUR 50" with normal shipping rules |
| "Only today" banner that runs for a week | Real end date and time zone, banner removed at the end |
| "14 day money back guarantee" (EU, UK) | "60 day returns, return shipping on us" (goes beyond the law) |
| "Lowest price guaranteed" | Remove, or define the price match terms precisely |

## 9. US former price checklist
- [ ] The former price was offered openly and in good faith for a reasonably substantial period (FTC 16 CFR 233.1).
- [ ] Sales actually occurred at the former price (document it); a price nobody paid is weak evidence.
- [ ] California: the former price was the prevailing market price within the 3 months before the ad, or the date it applied is stated (Business and Professions Code 17501).
- [ ] "Compare at" or "value" claims based on comparable goods are supported by real market prices.
- [ ] All-in price rules: mandatory fees included in the advertised price in California, Minnesota, Virginia, Massachusetts, Colorado, Connecticut; Massachusetts total price shown before personal data is collected.

## 10. Turkey checklist
- [ ] Reference price is the lowest price in the 10 days before the discount start, in the same sales channel (website and app tracked separately).
- [ ] Campaign start and end dates and stock limits shown where required.
- [ ] Conditional offers ("2 al 1 öde") and loyalty discounts follow the same reference rules.
- [ ] Price tag and unit price rules met online.
- [ ] Commercial electronic messages promoting the offer sent only to IYS registered consent (`lifecycle-crm` and `compliance`).

## 11. When to escalate to a lawyer, not only `compliance`
- Visitor level list price tests in any market.
- Any personalized or segment based pricing beyond simple new versus returning customer offers.
- Communications with retail partners or resellers about their prices.
- Subscription terms changes for existing subscribers (price increases, new renewal terms).
- Cross-border offers that differ by country inside the EU.
