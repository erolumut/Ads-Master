# Account Setup and Eligibility

> Knowledge as of 2026-10. Sources: OpenAI Help Center articles "Ads Manager Beta Account Setup" (20001213), "Ads Manager Availability" (20001245), "Billing & Payment" (20001216), "Troubleshooting Common Issues" (20001217), "Create Campaigns" (20001210), developer docs "Account Management". Read via mirrors dated 2026-09-22 to 2026-09-24. Re-verify live.

## 1. Eligibility gate (run before any plan)

| # | Gate | Pass condition | How to verify | If it fails |
|---|------|----------------|---------------|-------------|
| 1 | Legal entity country | The legal entity that will advertise and be billed is based in a country marked Available on Ads Manager Availability | help.openai.com/en/articles/20001245 | Register at ads.openai.com to be notified; use a partner (Criteo, agencies) or the OpenAI Ads Solutions team if available in that market; or no go |
| 2 | Target market served | Users in the target market see ChatGPT ads | OpenAI dated updates on "Testing ads in ChatGPT", regional announcements | Wait; advertiser access can exist before consumer serving is meaningful |
| 3 | Business type | Business advertiser (individuals not supported) | Account setup article | No go |
| 4 | Category | Allowed for the advertiser's country under Ad Policies; restricted categories (finance, health, legal) need US and approval | openai.com/policies/ad-policies/ | Restricted outside US means prohibited; no go |
| 5 | Primary business model | Not primarily in a restricted or prohibited category | Ad Policies, advertiser policies section | A compliant ad can still be refused |
| 6 | Landing page crawlable | Public HTTPS page, 200 status, HTML, no login, no CAPTCHA, not robots blocked for OAI-AdsBot | curl test, robots.txt, WAF logs | Fix crawler access before ad creation |
| 7 | Favicon and brand assets | Favicon JPEG, PNG or WebP, at least 256x256 (older help text said 128x128; use 256) | Account settings | Ads will not serve without brand review approval |
| 8 | Payment | Card in the same country and entity as the account (self-serve) | Billing settings | Card from another country may be rejected |
| 9 | Audience on ad plans | Buyers use ChatGPT on Free or Go | Customer survey, GA4 chatgpt.com referral share, panel data | Lower priority; consider organic visibility instead |
| 10 | Competitive conflict | Not a direct competitor of OpenAI products (v1.6 clause) | Ad Policies v1.6 | Possible refusal; trade press reported image and audio generation tools rejected [Unverified] |

Output of the gate: go, conditional go (list conditions) or no go, with dates of the sources checked.

## 2. Countries (advertiser self-serve)

Ads Manager Availability on 2026-09-22 listed 56 countries, all Available [Official, 2026-09]:
Algeria, Australia, Austria, Bahrain, Belgium, Brazil, Bulgaria, Canada, Croatia, Cyprus, Czech Republic, Denmark, Egypt, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, India, Iraq, Ireland, Israel, Italy, Japan, Jordan, Korea, Kuwait, Latvia, Lebanon, Liechtenstein, Lithuania, Luxembourg, Malta, Mexico, Morocco, Netherlands, New Zealand, Norway, Oman, Poland, Portugal, Qatar, Romania, Saudi Arabia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Tunisia, Turkey, United Arab Emirates, United Kingdom, United States.

Added in late September 2026: Indonesia, Malaysia, Philippines, Singapore, Thailand, Vietnam, Taiwan [Official, 2026-09] (OpenAI post on Southeast Asia and Taiwan; TechNode Global, 2026-09-24), taking the total past 60 countries; exact self-serve status per country [Unverified]. Third-party trackers count 63 countries [Unverified]. No Latin American market beyond Brazil and Mexico and no sub-Saharan African market was announced as of 2026-10-08.

Rules [Official, 2026-09]:
- Access follows the country selected for the advertiser business or ad account, not the ChatGPT login country.
- You can create an account for a country that is not yet available, but cannot use it until access opens.
- In the new European markets, advertisers could start through the OpenAI Ads Solutions team, agency partners or technology partners before and alongside self-serve.
- Larger advertisers with complex needs can request sales support through a form on the availability page.
- New self-serve accounts may be limited to targeting their home country at first; other countries require identity verification and a required amount of home country spend.

## 3. Account creation procedure (self-serve)

1. Go to ads.openai.com and sign in with an OpenAI account tied to a work email (or create one) [Official, 2026-09].
2. If your company already has an OpenAI organization (tenant, for example ChatGPT Business or Enterprise), an IT admin may need to grant the **Ads Admin** role: OpenAI admin console > Users > the user's profile > Direct roles > assign Ads Admin [Official, 2026-09].
3. Onboarding: enter business name, website, logo, industry; account country, currency, time zone; answer identity and business verification questions through **Persona** [Official, 2026-09].
4. Application enters review (rolling queue). Review checks whether products or services are eligible under the Ad Policies. Duplicate applications do not speed review; OpenAI cannot expedite account or ad reviews [Official, 2026-09].
5. After the platform access email: Settings > Account info, confirm **Account name** and **Logo** as they should appear in ads. Ads will not serve until this is done [Official, 2026-09].
6. Billing: create a billing profile (business name, invoice delivery email, billing address; country must match the account) and add a credit card [Official, 2026-09].
7. Invite team members: Settings > Users > Invite [Official, 2026-09].
8. Create API keys if needed (Settings > API keys; each key is scoped to one ad account) and Conversions API keys separately in the Conversions area [Official, 2026-09].

Campaigns do not deliver until all required steps are complete [Official, 2026-09].

### Immutable at creation
| Field | Changeable? | Consequence |
|-------|-------------|-------------|
| Country or region | No | New account needed |
| Billing currency | No | New account needed |
| Time zone | No | Reporting and budget weeks follow it; new account needed |
| Legal entity, billing country | Generally not self-editable; contact support with account ID | Plan correctly |

Advice: create one ad account per legal entity, country and currency combination. Use the account time zone that matches your reporting day in GA4 and backend.

### Branding fields (API terms) [Official, 2026-09]
| Field | Meaning |
|-------|---------|
| `legal_name` | Legal business name |
| `account_name` | Internal name in Ads Manager |
| `brand_name` | Public advertiser name shown in ads |
| Favicon | JPEG, PNG or WebP, at least 256x256, uploaded with purpose `account_favicon` |

Changing the legal or public brand name pauses ad delivery until the account passes review again [Official, 2026-09]. A separate account integrity review status may exist; if omitted, do not treat it as approved or rejected.

## 4. Multiple accounts, agencies and roles

| Topic | Rule | Label |
|-------|------|-------|
| One login, many accounts | One OpenAI login can access and switch between multiple ad accounts | [Official, 2026-09] |
| Creating more accounts | Requires an eligible existing self-serve account with credit card billing; limit of 10 total accounts created plus joined (can still be invited beyond) | [Official, 2026-09] |
| Agencies | Cannot create advertiser accounts on a client's behalf in Ads Manager; the client creates and verifies, then invites the agency | [Official, 2026-09] |
| Partners and resellers | Advertising Terms cover advertising intermediaries and a reseller program | [Official, 2026-09] |
| Roles | Admin, member, viewer reported; Ads Admin role at tenant level for creating ad accounts | [Unverified] (role names) and [Official, 2026-09] (Ads Admin) |
| HubSpot | For ChatGPT Business or Enterprise organizations, a global admin must approve HubSpot's Ads access in the OpenAI Admin Console (off by default) | [Official, 2026-09] |

Agency procedure that works [Practitioner consensus]: the client's authorized person creates the account with the company's details and billing, then invites the agency user with their own OpenAI login. The client keeps billing ownership. Record the account ID and owner in PROJECT_BRIEF.md.

## 5. Billing

| Item | Rule | Label |
|------|------|-------|
| Model | Postpay. Card accounts are charged when unpaid spend reaches the payment threshold, plus a month end charge for any remainder | [Official, 2026-09] |
| Threshold | Assigned by OpenAI, starts low, can rise automatically with good payment history; cannot be changed on request; it is not a budget or spend cap | [Official, 2026-09] |
| Invoice terms | Eligible sales managed advertisers can have postpaid invoice terms | [Official, 2026-09] |
| Authorization hold | Adding a card can create a temporary hold, released after verification (up to about 8 days visible) | [Official, 2026-09] |
| Tax IDs | VAT and tax IDs under Billing > Settings, apply to future invoices only. Japanese Consumption Tax not currently charged on ChatGPT Ads invoices for Japan billed advertisers | [Official, 2026-09] |
| Failed payment | Ads may stop delivering; campaigns show Not serving; email notice; fix payment method | [Official, 2026-09] |
| Late fees | Overdue undisputed fees may carry a 1.5% monthly finance charge (Advertising Terms) | [Official, 2026-09] |
| Account daily spending limit | Only for eligible postpaid invoice accounts; card accounts cannot use it | [Official, 2026-09] |
| After pause | Ads may serve up to 24 hours after a pause; that spend is billable | [Official, 2026-09] |
| Support | ads-support@openai.com with the ad account ID; include invoice or charge ID, dates, amounts, campaign IDs for billing disputes | [Official, 2026-09] |

Spend control without account limits: set campaign total budgets with end dates for fixed flights, or daily budgets knowing a single day can reach 2x and a week 7x the daily amount.

## 6. Managed and partner paths (when self-serve is not the right door)

| Path | When to use | Notes | Label |
|------|------------|-------|-------|
| OpenAI Ads Solutions (sales) | Large budgets, complex needs, markets before self-serve opens, invoice terms | Contact through the availability page form | [Official, 2026-09] |
| Criteo (Criteo GO for SMB, API integration for brands) | Retail media buyers already on Criteo, wanting managed activation and retail data | Minimums fell from $50k to $100k (March pitch deck) to $10k per month with a dollar-for-dollar media match (Adweek, 2026-06) | [Official, 2026-06] (availability) and trade reports (minimums; Criteo declined comment) |
| Amazon Ads (Amazon DSP, managed service) | Amazon advertisers wanting ChatGPT inventory with Amazon's managed team | Select US advertisers from 2026-09-10; CPC or CPM; aggregate reporting (impressions, clicks, CPM, CPC); no commission or affiliate reporting | Trade reports (Digiday, Marketing Dive, PPC Land, 2026-09) |
| StackAdapt, Kargo, Pacvue, Adobe | Programmatic or commerce teams already on these platforms | Partner controls budgets, bids and creative; OpenAI controls delivery | [Official, 2026-05] |
| Holding company agencies (Dentsu, Omnicom, Publicis, WPP) | Enterprise brands with agency of record | Early pilot access was mainly via these | [Official, 2026-05] |
| Shopify app | Shopify merchants wanting catalog sync and simple campaigns | US from 2026-09-16, international from 2026-09-23 | [Official, 2026-09] |
| HubSpot | HubSpot Marketing Hub users wanting lead follow up in CRM | Settings > Tools > Marketing > Ads > Connect account > ChatGPT Ads; create "ChatGPT Chat Card" campaigns | [Official, 2026-09] |

## 7. Setup checklist (copy into the launch plan)
- [ ] Gate 1 to 10 passed and dated.
- [ ] Ad account created under the correct legal entity, country, currency, time zone.
- [ ] Persona verification complete; platform access email received.
- [ ] Account name and logo confirmed in Settings > Account info; favicon 256x256 uploaded; brand review approved.
- [ ] Billing profile and card added; payment threshold noted.
- [ ] Users invited with least privilege; agency invited by client; owner recorded.
- [ ] OAI-AdsBot and OAI-SearchBot allowed in robots.txt and WAF; landing pages return 200.
- [ ] Pixel data source created; Conversions API key created and stored in the server secret manager; events verified (see measurement reference).
- [ ] Event settings attached to each campaign before traffic starts.
- [ ] UTM convention agreed and documented in MEASUREMENT.md.
- [ ] PROJECT_BRIEF.md channel table updated with account ID and status.

## 8. Common onboarding blockers
| Blocker | Fix |
|---------|-----|
| "No permission to create an ad account" | Tenant admin assigns Ads Admin role |
| Verification abandoned midway | Retry, do not submit inconsistent information |
| Card rejected | Use a card issued in the account country under the same entity |
| Account approved but Not serving | Account info name and logo not confirmed, brand review pending, billing incomplete |
| Agency cannot create account | Client creates and invites agency |
| Wrong currency or time zone | New account; cannot be edited |
| Country not available | Register interest; use partner or sales path; check again monthly |
