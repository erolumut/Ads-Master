# Policy and Account Health

> Knowledge as of 2026-10. Google Ads policy changes monthly. Check the Advertising Policies Help "policy change log" before launching in any restricted category, and before any appeal. Never advise a user to work around a policy or create new accounts to evade a suspension.

## 1. The account health stack

| Layer | What can go wrong | Impact |
|---|---|---|
| Account | Suspension (egregious violations, circumventing systems, unacceptable business practices, suspicious payment activity, unpaid balance), failed advertiser verification | All ads stop |
| Advertiser verification | Identity or business operations verification not completed within the deadline | Ads paused until completed |
| Limited Ad Serving | New or not yet trusted advertisers get limited impressions in scope of the policy | Low delivery, slow ramp |
| Ad and asset level | Disapproved, eligible (limited), restricted by region | Lower or no delivery |
| Destination | Destination not working, mismatched, malware, insufficient original content | Disapprovals |
| Merchant Center | Misrepresentation, unsupported content, product disapprovals | Shopping and feed PMax stop |
| Payments | Declined payments, unusual activity | Account hold or suspension |
| Access | Compromised users, unauthorized MCC links | Fraudulent spend, suspension risk |

## 2. 2025 to 2026 policy and enforcement changes

| Date | Change | Label |
|---|---|---|
| 2026-04 | Ads Advisor adds policy guidance for complex violations, round-the-clock account security monitoring (announced as coming soon), automated certifications | [Official, 2026-04] |
| 2026-07-21 | In-account appeals no longer available for policy decisions made more than 6 months earlier (suspensions, ad disapprovals, asset restrictions). Support is the only route after that | [Official, 2026-07] |
| 2026-08 | Limited Ad Serving policy expanded to all Google Ads; gradual implementation until 2028; in-account notice and an appeals form for affected advertisers | [Official, 2026-08] |
| 2026-08 | Certification process update: Social Casino Games certification introduced gradually; updates to gambling and games (global), cryptocurrencies, political content, YouTube and Discover feed ad requirements | [Official, 2026-08] |
| 2026-09-07 | Limited Ad Serving applied to Demand Gen and other surfaces | [Practitioner report, 2026-09] |
| 2026-10-30 | Personalized advertising policy update: alcohol ads allowed on YouTube inventory where locally permitted; targeting based on alcohol-related health information stays prohibited | [Official, 2026-09 notice] |
| 2026-10 | Policy updates listed for Gambling and Games (Colombia), Editorial, Financial products and services, Government documents and services | [Official policy change log, 2026-10] |

## 3. Advertiser verification

- Google requires advertisers to verify identity and, in many cases, business operations. Advertisers receive a deadline in the account (typically 30 days) [Official, verify current deadline].
- Use legal entity names and documents that match the payments profile and the business name on ads. The business name asset must match the verified advertiser or an authorized brand relationship.
- Agencies: the advertiser (end client) verifies, or the agency verifies if it pays and is the advertiser of record.
- Failure to verify pauses ads. Check Policy manager, Advertiser verification.

## 4. Suspension types and recovery

| Suspension | Typical triggers | Recovery approach |
|---|---|---|
| Circumventing systems | Cloaking, creating new accounts after a suspension, hiding destination content, tricking reviewers, repeated resubmission of the same violation | Immediate suspension without warning [Official]. Find and remove the cause (redirects, cloaking plugins, linked suspended accounts), document fixes, appeal with evidence. Never open new accounts |
| Unacceptable business practices | Scam patterns, misleading claims, hiding business info, impersonation, fake reviews | Make business identity transparent (address, phone, legal name, policies on site), remove misleading claims, appeal with documentation |
| Misrepresentation (Merchant Center or Ads) | Missing return policy, shipping info, contact info, unrealistic discounts, dishonest pricing | Fix site transparency, request review in Merchant Center; hand off to commerce-feeds for feed issues |
| Suspicious payment activity | Payment method mismatch, card issues, sudden billing changes | Verify payment profile, contact billing support |
| Unpaid balance | Failed payments | Pay, update payment method |
| Promotion of unauthorized pharmacies, dangerous products, sexual content and other egregious policies | Category violations | Usually permanent if confirmed; appeal only with a clear factual error |
| Three strikes system (certain policies) | Repeated violations of specific policies after warning | Warning, then strike 1 (3 days hold), strike 2 (7 days), strike 3 suspension [Official, verify policy list] |

Appeal procedure:
1. Read the exact policy in the notice and the policy help page. Identify every possible trigger, not only the obvious one.
2. Fix the site and account first (landing pages, claims, disclosures, redirects, linked accounts, payment profile).
3. Gather evidence: screenshots, documents, licenses, before and after.
4. Submit one appeal through Policy manager or the suspension notice. Do not mass appeal: practitioners warn that repeated appeals can make things worse [Practitioner consensus].
5. Appeal within 6 months of the decision; older decisions cannot be appealed in-account since 2026-07-21 [Official].
6. Log the case in the journal with dates and evidence. Escalate through the Google rep if one exists.

## 5. Trademarks

- Keywords: Google does not restrict the use of trademarks as keywords in most regions; it does not investigate trademark use in keywords [Official].
- Ad text: trademark owners can file a complaint; Google may then restrict the term in ad text in the specified regions unless the advertiser is authorized (reseller and informational site exceptions exist with conditions) [Official].
- Authorization: to allow a partner or reseller to use your trademark, submit the authorization form for their account IDs.
- Competitor ads using your brand in ad text: file a trademark complaint. Competitors bidding on your brand as a keyword: usually allowed; respond with a strong brand campaign.
- AI generated text (AI Max text customization, PMax) can produce competitor names when the competitor appears in queries or site content. Use text guidelines and brand exclusions, and check generated assets.

## 6. Restricted and sensitive categories (check before launch)

| Category | Notes |
|---|---|
| Healthcare and medicines | Certifications for online pharmacies, addiction services, some treatments; restricted in many countries; no ads in AI Overviews for sensitive verticals [Practitioner report] |
| Financial services | Country-specific verification for financial services advertisers in many markets; crypto exchanges and wallets need certification; disclosure requirements; October 2026 update to Financial products and services policy |
| Gambling and games | Certification per country; social casino games certification from 2026-08 |
| Alcohol | Country restrictions; YouTube personalized advertising change from 2026-10-30 |
| Political and election ads | Verification and country rules; political content policy update 2026-08 |
| Personalized advertising (sensitive interests) | Housing, employment and credit in the US and Canada have targeting restrictions; no targeting on health conditions, sexual orientation, etc. |
| Government documents and services | Must disclose not affiliated; October 2026 update |
| Legal services | Some subcategories (bail bonds, debt services) restricted |
| Adult content | Restricted and not allowed in many formats |

Customer Match and remarketing lists must not be built from sensitive categories (health conditions, financial hardship, etc.).

## 7. Editorial and destination basics that cause most disapprovals

| Policy | Common trigger | Fix |
|---|---|---|
| Editorial | Excessive capitalization, gimmicky punctuation, unclear business name, phone numbers in text | Rewrite; use call assets for numbers |
| Destination not working | 404, redirects, geo-blocked pages, bot protection blocking Google crawler | Whitelist Google crawlers, fix URLs, check from target countries |
| Destination mismatch | Display URL domain differs from final URL domain | Match domains |
| Insufficient original content | Thin pages, arbitrage pages | Add original content or stop advertising the page |
| Unreliable claims | "Guaranteed", "cure", "best" without proof | Substantiate or remove; text guidelines for generated copy |
| Trademark | Restricted term in ad text | Remove or get authorization |

## 8. Account security

- 2-step verification for every user. Remove ex-employees and old agencies quarterly.
- Admin access only for owners. Use read-only or standard access for connectors and analysts.
- Review linked accounts (MCC links, GA4, Merchant Center, YouTube) quarterly.
- Watch for unauthorized changes: change history by user, sudden new campaigns, new payment methods. Ads Advisor security recommendations were announced in 2026 [Official, 2026-04].
- If compromised: remove unknown users, pause rogue campaigns (with owner approval), contact Google Ads support, change Google account passwords, review payment charges.

## 9. Account health monitoring cadence

| Cadence | Check |
|---|---|
| Daily | Disapprovals on active ads (script S5), suspensions or warnings in notifications, payment issues |
| Weekly | Policy manager, limited assets, Merchant Center diagnostics |
| Monthly | Advertiser verification status, certifications expiring, policy change log for the business category |
| Quarterly | User access review, linked accounts review, trademark authorizations |

## 10. Recovery playbook: account suspended

1. Stop: do not create new accounts, do not change payment methods impulsively, do not submit multiple appeals.
2. Read: the suspension email and notice, the exact policy name.
3. Diagnose: site audit (claims, transparency pages, redirects, cloaking plugins, third-party scripts), account audit (linked accounts, payment profile, past violations, change history), Merchant Center status.
4. Fix: implement every fix and document it with dates.
5. Appeal: one well-documented appeal through the notice or Policy manager within the 6-month window.
6. Wait: appeals can take days to weeks. Plan budget shifts to other channels with growth-orchestrator during the outage.
7. After reinstatement: ramp spend gradually (Limited Ad Serving and trust signals), keep compliance checks in the weekly cadence, record learnings in memory if the cause is confirmed.

## 11. Pre-launch compliance checklist

1. Category check: is the product or service in a restricted category for each target country? Certification needed?
2. Claims: every claim in ads and landing pages substantiated and listed as approved in BRAND.md.
3. Site transparency: legal business name, address, contact, refund and return policy, privacy policy, terms, shipping info.
4. Destination: no redirects that change domain, no interstitials that block content, crawlable by Google.
5. Business name and logo assets match the verified advertiser.
6. Generated assets (AI Max text customization, PMax, Asset Studio) reviewed against text guidelines.
7. Audience data: no sensitive categories; Customer Match data collected with consent.
8. Advertiser verification and payment profile complete before launch.
9. Trademark: authorization for any third-party trademark in ad text.
10. Regional rules: EEA consent mode, political ad rules, alcohol and gambling local laws.
