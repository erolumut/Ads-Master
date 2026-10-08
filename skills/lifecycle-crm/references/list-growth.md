# List Growth with Quality

Strategy, offers, consent, targeting rules and measurement for growing email, SMS and WhatsApp audiences. Boundary: `storefront-ux` owns the on-site capture UI patterns (pop up design, layout, account pages, component code); this module owns what to ask, when, for whom, with which incentive and consent text, and how to judge list quality. `offer-strategy` owns incentive economics; `compliance` owns consent text approval.

## 1. Principles

1. A subscriber is worth what they buy, not that they exist. Judge every capture source on subscriber to customer rate and 90 day value, not volume.
2. Capture consent per channel. Email first, then SMS or WhatsApp as a second step for those who opted into email.
3. Never buy, rent, scrape or co-register lists. They damage deliverability (spam traps, complaints) and break consent law.
4. Ask for zero party data at capture only when you use it in the welcome flow.
5. Incentives are acquisition investment. Count them (METRICS.md): discount cost on first orders from subscribers belongs in first order economics.

## 2. Capture point inventory

| Capture point | Typical quality | Notes |
|---------------|----------------|-------|
| Pop up or flyout (timed, exit intent, scroll) | Medium to high depending on offer | UI by storefront-ux; you set targeting, offer, steps, consent |
| Embedded footer and blog forms | High intent, low volume | |
| Checkout marketing checkbox (unticked in EU, UK, Turkey) | High (buyers) | Soft opt-in in EU and UK still requires an opt-out choice at collection |
| Account creation | High | Separate checkboxes per channel |
| Post purchase page (thank you) and order status | High; buyers | Ask for SMS or WhatsApp with a utility reason (shipping updates) plus marketing opt-in separately |
| Back in stock and price drop requests | Very high intent | Consent for the alert is not consent for marketing; ask separately |
| Quiz and product finder | High; rich zero party data | Results by email as the value exchange |
| Gated content (lead gen and B2B) | Medium | Ask topic interest |
| SMS keyword (text JOIN to short code) and QR codes in packaging, retail, events | High | Keyword confirmation message with full disclosures |
| Click to WhatsApp ads and WhatsApp click to chat links | Medium to high | Free 72 hour window from ads; opt-in for marketing still needed |
| Meta lead ads and other native lead forms | Variable; check quality | Sync to ESP in real time; consent text inside the form; measure subscriber to customer rate separately |
| Retail POS and events | Variable | Capture consent text and staff script; İYS registration in Turkey within 3 business days |
| Giveaways and partnerships | Low unless double opt-in | Double opt-in; only the brand's own consent |

## 3. Offer strategy for capture

| Offer type | When it works | Risks |
|------------|---------------|-------|
| Percent or fixed discount on first order | Mass market ecommerce, high competition | Trains discount behavior; margin leakage; code sharing (use unique codes) |
| Free shipping | High shipping friction, low AOV | Cost per order; check acquisition investment |
| Free gift with first order | Strong brand, sampling logic | Inventory cost |
| Early access, drops, waitlist | Hype products, limited editions | Must deliver on the promise |
| Content (guide, routine, recipe) | Considered purchases, lead gen | Lower capture rate, often higher quality |
| Quiz result | Personalization driven categories (beauty, supplements, pet, apparel fit) | Build effort |
| Sweepstakes | Brand awareness | Low quality; legal rules for prize promotions |
| Loyalty points on signup | Loyalty program in place | Liability accounting |

Rules: test offers with a holdout or A/B on capture rate and 90 day contribution per subscriber; offer-strategy decides the level; never promise an incentive the welcome flow does not deliver immediately.

## 4. Targeting and timing rules (for storefront-ux implementation)

| Rule | Default |
|------|---------|
| Do not show to existing subscribers | Suppress by cookie and identified profile |
| Do not show on checkout and cart | Avoid interrupting purchase |
| Delay on landing | After meaningful engagement (time on site or scroll, or second page view) rather than instantly; test |
| Exit intent on desktop; timed or scroll on mobile | Exit intent is unreliable on mobile |
| Paid traffic landing pages | Coordinate with cro and channel agents so the pop up does not break message match or speed |
| Frequency | Do not re-show for 7 to 30 days after dismiss |
| Two step email then SMS | Step 1 email; step 2 SMS or WhatsApp with its own consent text |
| Country specific consent | Show the correct consent text by detected country (EU, UK, US, Turkey) |
| Accessibility | Focus management, close button, keyboard and screen reader support (storefront-ux implements; EAA applies in the EU) |
| Google intrusive interstitials | Avoid full screen mobile pop ups on landing from search (SEO risk) [Official, Google Search guidance] |

## 5. Consent text by market (approve with compliance)

Email (EU, UK; unticked checkbox or clear action):
```
Yes, send me emails from <Brand> about products, offers and news. I can unsubscribe at any time. See our Privacy Policy <link>.
```

SMS (US): use the TCPA disclosure in [Consent and law](consent-and-law.md) section 3.1, shown next to the phone field and the submit button.

Turkey (separate from KVKK explicit consent and from membership terms):
```
<Brand> tarafından kampanya, duyuru ve fırsatlar hakkında ticari elektronik ileti (SMS, e-posta, WhatsApp) almak istiyorum. İznimi dilediğim zaman geri alabilirim.
```
Then register in İYS within 3 business days, and send the electronic consent confirmation within 24 hours if collected outside İYS [Official, Regulation; verify text with compliance].

## 6. Benchmarks (use with caution)

| Metric | Value | Source, date | Caveat |
|--------|-------|--------------|--------|
| Klaviyo median pop up and flyout submit rate | 2.3% | Klaviyo in-app benchmarks via a secondary source [Unverified, 2025 to 2026] | Submit rate = submitted form events / viewed form events, not unique visitors |
| Average ecommerce email pop up conversion | About 4.8%; top performers 10% to 15% | Revlifter [Unverified, vendor] | Definitions vary |
| Sleeknote all goal campaigns | 4.13% across 26,270 campaigns | Sleeknote via CrazyEgg [Study, vendor] | Mixed goals |
| OptiMonk email capture pop ups | 5.10% to 7.65% by lead magnet | via CrazyEgg [Study, vendor] | |
| Klaviyo benchmark tiers | Poor below 25th percentile, Fair 25th to 50th, Good 50th to 75th of peer group | Klaviyo Academy [Official] | Use the account's Benchmarks tab |

Compare to the project's own history first. A higher submit rate with a lower subscriber to customer rate is not a win.

## 7. List quality metrics

| Metric | Formula | Healthy signal |
|--------|---------|----------------|
| Capture rate | New subscribers / sessions (by source and device) | Trend vs own baseline |
| Subscriber to customer rate (30 and 90 day) | New subscribers who order in 30 or 90 days / new subscribers | By capture source and offer |
| Discount redemption share | Subscribers redeeming welcome code / subscribers | High share with low repeat = discount seekers |
| 90 day value per subscriber | Contribution from subscribers in 90 days / subscribers | The number that decides offers |
| Early unsubscribe and complaint rate | Within 30 days of signup | Spikes mean mismatch between promise and content |
| Fake or bot share | Signups with no site activity, disposable domains, bursts | Fix with verification and rate limits |
| SMS step 2 take rate | SMS opt-ins / email opt-ins in two step forms | |

## 8. Handoff spec to storefront-ux (capture form brief)

```
## Capture form brief: <name> (for storefront-ux to design and build)
Goal and KPI: <capture rate by device; subscriber to customer rate 90 days>
Audience and targeting: <new visitors, excluding subscribers; pages included and excluded; markets>
Trigger: <time, scroll, page count, exit intent desktop only>; re-show after dismiss: <days>
Steps: 1) email with consent text <id>; 2) SMS or WhatsApp with consent text <id>; 3) zero party question <field>
Offer: <from offer-strategy, code type unique single use, expiry>; delivered by welcome E1 immediately
Consent texts: <versions approved by compliance per market>
Data written: list <id>, properties <source, capture_form_id, zero party fields, consent timestamp>
Exclusions: checkout, cart, account pages, paid landing pages flagged by cro
Measurement: form views, submits, submit rate, downstream orders by capture_form_id
Accessibility and speed requirements: per storefront-ux standards
Test plan: <variant, metric, duration> logged in EXPERIMENTS.md
```

## 9. Paid list growth (native lead forms)

- Meta lead ads, TikTok lead generation and LinkedIn Lead Gen Forms can feed the ESP in real time (native integrations or connectors); include the marketing consent checkbox and privacy link inside the form.
- Tag the source (`source = meta_lead_ad_<campaign>`) and give these subscribers their own welcome branch; they often convert lower than on-site subscribers [Practitioner consensus].
- Judge the campaign on cost per subscriber who buys within 90 days, not on cost per lead. Share that number with the channel agent.
- Turkey: native lead form consents still need İYS registration within 3 business days.

## 10. Experiments backlog (examples)

| Hypothesis | Metric | Notes |
|------------|--------|-------|
| Quiz entry vs discount pop up raises 90 day value per subscriber | 90 day contribution per subscriber | Expect lower capture, higher quality |
| Two step email then SMS vs single step both fields | Total consented contacts and complaints | |
| Delayed trigger (second page) vs immediate | Capture rate and bounce rate | Coordinate with cro |
| Free gift vs 10% off | Contribution per subscriber | offer-strategy |
| Post purchase SMS opt-in with shipping update framing | SMS opt-in rate among buyers | Separate utility and marketing consent |

Log each in EXPERIMENTS.md with the capture source ID.
