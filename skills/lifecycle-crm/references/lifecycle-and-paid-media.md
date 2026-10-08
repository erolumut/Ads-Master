# Lifecycle and Paid Media

How retention data improves acquisition: suppression, customer list audiences, existing customer controls in campaign settings, value based audiences, LTV values for bidding, and the cohort feedback loop into budget allocation. You prepare the audiences, definitions and specs; channel agents (`meta-ads`, `google-ads`, `microsoft-ads`, `tiktok-ads`, `linkedin-ads`, `chatgpt-ads`) configure their platforms; `measurement` owns conversion values and data pipelines. Uploading customer data to an ad platform is a transfer of personal data: G3 with a lawful basis check every time.

## 1. Uses of first-party lists in paid media

| Use | What | Who configures | Refresh |
|-----|------|----------------|---------|
| Exclusion of recent buyers from acquisition | Customers who purchased in the last N days (N about the reorder interval) excluded from new customer campaigns | Channel agents | Daily to weekly |
| Existing customer definition for new customer goals | Customer lists that tell the platform who is "existing" (Google new customer acquisition goal; Meta Advantage+ sales existing customer settings) | Channel agents with measurement | Weekly |
| Suppression of active subscribers from first order discount ads | Prevent margin leakage | Channel agents | Weekly |
| Retargeting lapsed customers | Winback audiences on paid channels when email and SMS fail | Channel agents; lifecycle defines audience | Weekly |
| Value based seed audiences | Top predicted or historic LTV customers as seeds for lookalikes or value based expansion | Channel agents | Monthly |
| Value rules and value adjustments | Bid more for audiences with higher LTV (Meta value rules for audiences fire on customer list and website custom audiences as of 2026-04) [Secondary, 2026] | meta-ads | Monthly |
| Customer list targeting for cross sell | Buyers of A shown B on paid social | Channel agents | Weekly |
| LTV or predicted value as conversion value | First order value plus predicted future value sent to platforms for value based bidding | measurement | Per event |

## 2. Platform rules (October 2026)

### 2.1 Google (Customer Match)

- From 2026-04-01 Customer Match uploads through the Google Ads API fail for developer tokens without recent Customer Match activity; most new integrations must use the Data Manager API (single ingestion request, confidential matching, encryption). Existing eligible integrations may continue for now; a data partner deadline of March 2027 was reported but not confirmed in an official post [Official, Google Ads API docs; Search Engine Land 2026; March 2027 Unverified].
- Ask the ESP, CDP or connector vendor whether their Google sync uses the Data Manager API.
- Customer Match eligibility and policy requirements (account history, policy compliance, consent for EEA users under the EU user consent policy) apply [Official, Google Ads policy].
- New customer acquisition goal in Google Ads uses customer lists and conversion data to identify existing customers; keep the list fresh [Official].

### 2.2 Meta (Customer List Custom Audiences)

- Advertisers certify list compliance (prompted in Ads Manager since January 2025); sharing audiences only within the same Business Portfolio under same domain conditions [Secondary, Jon Loomer 2025].
- From 2025-09-02 Meta proactively restricts custom and lookalike audiences that suggest health conditions or financial status; Meta's customer list terms (reported update 2025-12-03) bar audiences built on health, financial or consumer report information [Secondary, 2025; Unverified exact terms wording].
- Exclusion only custom audiences launched 2026-08-10 (cannot be switched to inclusion after creation) [Secondary, Common Thread 2026-08]. Use them for buyer suppression lists.
- Value rules for audiences apply to customer list and website custom audiences only (as of 2026-04) [Secondary, 2026].
- Uploads: up to 10,000 records per request via API; hashing (SHA-256) of normalized identifiers is required for API uploads [Official, Meta Marketing API docs].

### 2.3 Others

| Platform | Notes |
|----------|------|
| TikTok | Customer file audiences; exclusions for acquisition; TikTok Shop has its own buyer data rules |
| Microsoft Advertising | Customer Match lists (consent and eligibility requirements) [Official] |
| LinkedIn | Contact and company list matched audiences for ABM and exclusions |
| ChatGPT ads and AI assistant surfaces | Audience capabilities limited and evolving; check `chatgpt-ads` freshness notes |

## 3. Data handling rules

1. Only profiles with a lawful basis for this use (consent covering advertising use in EU, UK and Turkey; opt-out rights honored in US states with privacy laws) and who have not objected.
2. Exclude unsubscribed and suppressed profiles if the privacy notice ties advertising use to marketing consent [Practitioner consensus; confirm with compliance].
3. Never upload health related, financial or other sensitive segments.
4. Use the ESP's native integration or the ad platform's official connector rather than CSV files where possible; CSV exports with emails or phones never go into the repository, `ads-master/`, journal or outputs.
5. Document each audience in an audience register: name, definition, source, lawful basis, refresh cadence, platforms, owner, created date.

Audience register row template:
```
| AUD-012 | Recent buyers 60d (exclusion) | Placed Order in last 60 days | Klaviyo segment <id> via native Meta sync | Privacy notice section 4, legitimate interest assessment LIA-03 | daily | Meta, Google (Data Manager), TikTok | lifecycle-crm | 2026-10-08 |
```

## 4. LTV values for bidding (handoff to measurement)

Lifecycle provides the evidence; measurement implements.

| Approach | When | What lifecycle provides |
|----------|------|------------------------|
| Static uplift: send first order value x LTV multiplier by segment | Scale tier, stable cohorts | 12 month contribution LTV by first product, acquisition channel and discount use ([Cohort and LTV analysis](cohort-and-ltv-analysis.md)) |
| Predicted value at first purchase | Enterprise, data science capacity | Model features, validation on past cohorts (predicted vs realized) |
| New customer value bonus | Platforms with new customer bidding | The incremental value of a new customer vs a returning one (contribution LTV minus first order contribution) |
| Lead gen: value by lead stage | B2B | Stage conversion rates and deal values for value rules |

Rules: use contribution, not revenue; cap predicted values to avoid runaway bids; refresh multipliers quarterly; never send predicted LTV without a validation table (decile of predicted vs actual 12 month value).

## 5. Cohort feedback into budget allocation

Every month, share with `growth-orchestrator` and channel agents:

| Acquisition source (first order) | New customers | First order AOV | Discount share | 90 day repeat rate | 12 month contribution LTV (mature cohorts) | Acquisition investment per new customer | LTV to CAC | Payback months |
|-------------------------------|---------------|----------------|----------------|--------------------|-------------------------------------------|---------------------------------------|-----------|----------------|

Sources: backend orders joined to first touch or platform attribution and post purchase survey answers ("Where did you hear about us?") from measurement. Flag channels whose customers repeat far less (common for deep discount and some marketplace or affiliate sources) and channels whose customers repeat more (often brand search, referral, organic).

## 6. Coordinated plays

| Play | Lifecycle side | Paid side |
|------|---------------|-----------|
| Launch or drop | Waitlist capture, early access email and SMS | Retarget waitlist non openers; exclude buyers after launch |
| Winback | Email and SMS winback first | Paid winback to non responders after 21 days, then stop |
| Second order push | Post purchase and replenishment | Exclude recent buyers from acquisition; cross sell ads only for high value cohorts |
| Peak season | Segment by engagement; early access for VIP | Suppress VIP from discount acquisition ads; new customer goals on |
| Subscription | Upcoming charge and save flows | Exclude active subscribers from subscription acquisition offers |

## 7. Identifier preparation and match rates

Native ESP to ad platform syncs handle normalization and hashing. When a custom pipeline is unavoidable (built by `measurement` or `site-engineer`), follow platform specs:

| Identifier | Normalize before hashing |
|-----------|--------------------------|
| Email | Trim spaces, lowercase; Google also removes dots before the @ for gmail.com and googlemail.com addresses in its guidance [Official, Google Ads docs; verify] |
| Phone | E.164 format with country code (for example +905321234567), digits only after the plus |
| First and last name | Lowercase, no punctuation (where used) |
| Country, postal code | ISO 3166 alpha-2 country; postal code per platform spec |

```python
import hashlib
def norm_hash_email(email: str) -> str:
    return hashlib.sha256(email.strip().lower().encode("utf-8")).hexdigest()
```

Run hashing inside the pipeline, never in a notebook that writes raw identifiers to disk. Match rates commonly land between 30% and 70% depending on identifier coverage and platform [Practitioner consensus]; adding phone numbers usually raises them. Report match rate per upload in the audience register.

## 8. Worked example: suppression value

Illustrative: an acquisition campaign spends 40,000 EUR per month; backend shows 9% of attributed purchases came from customers who had bought in the prior 60 days. Excluding the 60 day buyer list (about 18,000 profiles) moves that spend toward new customers. If new customer CPA holds, the shift is worth about 0.09 x 40,000 = 3,600 EUR per month of spend that previously reached existing buyers, who are reached at near zero cost by email and SMS. Validate with the channel agent: some platforms reallocate delivery and CPA can rise; read nCAC and aMER (METRICS.md) before and after for 4 weeks.

## 9. Post purchase survey as a shared input

The "Where did you hear about us?" question in the post purchase flow or thank you page is a lifecycle asset that feeds `measurement` (self reported attribution, podcast, creator and AI assistant mentions that click attribution misses). Rules: one required question with randomized options plus "Other", capture only for first orders, store as a profile and order property, report aggregates monthly.

## 10. Checklist

- [ ] Buyer exclusion lists live on every acquisition campaign that targets new customers
- [ ] Existing customer lists refreshed at least weekly where platforms use them for new customer goals
- [ ] Google sync path uses the Data Manager API or a vendor confirmed compliant
- [ ] No sensitive data segments uploaded; audience register maintained
- [ ] LTV by acquisition source shared monthly with growth-orchestrator
- [ ] Value signals validated before being sent to bidding
