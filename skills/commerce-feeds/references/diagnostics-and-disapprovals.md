# Diagnostics and Disapprovals

> Triage order, issue-by-issue fixes, account suspension recovery, and decision trees for sudden drops. Knowledge as of 2026-10. Issue names below follow Merchant Center wording as commonly displayed; exact strings vary by language and change over time.

## 1. Triage order
1. Account-level issues (suspension, warnings, misrepresentation, website claim lost). Everything else waits.
2. Data source failures (fetch failed, sync stopped, item count dropped).
3. Disapprovals on top revenue SKUs (sort by last 30 days revenue or click potential HIGH).
4. Price and availability mismatches (they escalate to account warnings).
5. Limited performance warnings (missing identifiers, image quality, missing recommended attributes).
6. Cosmetic warnings.

Always quantify: disapproved SKUs, their share of last 30 days revenue or clicks, and the destinations affected (Shopping ads, free listings, local, UCP checkout).

## 2. Item-level issues: cause and fix

| Issue (as shown) | Likely cause | Check | Fix |
|------------------|-------------|-------|-----|
| Mismatched value (page crawl) [price] | Feed price differs from page or checkout; geo currency; sale timing; cached page | Run parity script; view page from target country without cookies | Fix source of truth; refresh frequency; sale dates; disable geo redirect for crawlers |
| Mismatched value (page crawl) [availability] | Stock moved since last feed; variant not preselected | Parity script; variant URL | Hourly or API stock updates; variant URLs |
| Invalid value [gtin] / Incorrect identifier | Wrong check digit, restricted prefix, GTIN of another product | `feed_qa.py` GTIN check; GS1 lookup | Correct GTIN from supplier or GS1; remove invented GTINs |
| Missing value [gtin] / Limited performance due to missing identifiers | Branded product without GTIN | Brand and category | Add GTIN; if none exists, MPN plus brand; `identifier_exists=no` only when truly none |
| Image too small / low quality | Below minimum or blurry | Image dimensions | Replace; plan for 500 x 500 minimum from 2027-01-31 |
| Promotional overlay on image | Text, badges, watermarks | Visual check | Clean image; automatic image improvements as a temporary net |
| Generic image / placeholder | "Image coming soon" | Image URL pattern | Real product image or exclude item |
| Image could not be crawled | Bot protection, robots.txt, CDN rules, 403 | Fetch image URL as Googlebot | Allow Googlebot-Image and Storebot-Google; stable public URLs |
| Landing page not working / Unavailable desktop or mobile landing page | 404, redirect, soft 404, geo block, consent wall | Fetch as crawler, mobile and desktop | Fix URL, remove redirects, allow crawler |
| Unclaimed website / Invalid value [link] | Domain not verified or claimed, link to other domain | Business info, website | Verify and claim; links on claimed domain |
| Missing shipping information | No account shipping for the country | Shipping settings | Add shipping service for the country |
| Invalid or missing [availability_date] | Preorder or backorder without date | Feed | Add ISO 8601 date |
| Item group issues (variants) | Variants missing shared `item_group_id` or missing distinguishing attributes | Feed | Shared group ID; color, size, material, pattern per variant |
| Too many products in item group | Very large variant sets | Group size | Split by a meaningful dimension |
| Restricted or unsupported content (healthcare, weapons, adult, alcohol, gambling) | Category policy | Policy center | Remove, certify, or exclude destination or country |
| Counterfeit goods / trademark | Brand claims | Policy notice | Provide authorization or remove |
| Missing or invalid apparel attributes [color] [size] [gender] [age_group] | Apparel in required countries | Feed | Add from product data |
| Value too long [title] / [description] | Over 150 or 5,000 | `feed_qa.py` | Trim with templates |
| Processing failed / Pending initial review | New items or account | Time and volume | Wait 3 to 5 business days typical; do not resubmit repeatedly [Practitioner consensus] |
| Video rejected [video_link] (from 2026-06-30) | Policy or quality | Needs attention tab | Fix or remove video; listing stays live |
| Pickup cost missing (UK, CH, EEA, from 2026-04-28) | Pickup offers without `pickup_cost` | Local feed | Add pickup cost and minimum order value |

## 3. Account-level problems

### 3.1 Misrepresentation suspension: recovery runbook
1. Do not request review immediately. Repeated failed reviews can trigger cooldown periods before you can request again [Practitioner consensus, verify current rule in the notice].
2. Read the notice and Account issues page; note the policy and date.
3. Audit the site like a reviewer (checklist below). Fix everything, not just the likely trigger.
4. Make business identity consistent: legal name, address, phone, email the same on site, Merchant Center business info, Google Business Profile, payment descriptor and invoices.
5. Remove or substantiate claims: "best", "number one", "clinically proven", "free" with conditions, fake countdown timers, fake scarcity, reviews you cannot prove, trust badges you are not entitled to.
6. Pricing: no reference prices that were never charged; discounts real and documented.
7. Request review once, with a short factual description of changes if a field is offered.
8. Log every step and date in the journal; tell growth-orchestrator the revenue at risk.
9. If rejected again, look for less obvious triggers: payment page domain, checkout on a different domain, subscription terms, shipping times promised versus actual, AI-generated product images that misrepresent the product, copied content from other stores.

Site checklist for misrepresentation:
| Item | Pass condition |
|------|---------------|
| Contact page | Physical address (if business has one), phone or email, form, hours |
| About page | Who runs the business, history, real people or company details |
| Returns and refunds | Window, condition, who pays shipping, how to start a return, refund timing |
| Shipping | Countries, costs, times, handling time |
| Terms and privacy | Present, linked in footer, match the business name |
| Checkout | Secure, clear total before payment, no surprise fees |
| Product pages | Real images, accurate specs, stock and price visible |
| Claims | Substantiated or removed |
| Reviews | Genuine, attributed, not copied |
| Business info in Merchant Center | Complete and matching |

### 3.2 Policy warnings with a deadline
- Warnings typically give a fixed window (often 28 days) before enforcement [Official per notices, verify each time]. Treat the deadline as a project with an owner and daily progress.
- Price accuracy warnings: fix the data pipeline, not the individual items.

### 3.3 Website claim lost
- Cause: verification tag removed in a redesign, domain change, or another account claimed the site.
- Fix: re-verify; if claimed elsewhere, the site owner can reclaim (removes the other claim). Coordinate with anyone else running a Merchant Center for the domain (agencies, CSS).

## 4. Sudden drop decision tree (impressions or clicks fell)

```
Did the number of approved items drop?
  yes -> Data source failure or mass disapproval.
         Check data source fetch log, product count trend, new item issues by type.
  no  -> Did prices change versus benchmark (price competitiveness)?
           yes -> Price lost competitiveness; check competitor prices; hand to google-ads for bid context.
           no  -> Did titles, IDs or product types change recently (journal, feed tool log)?
                    yes -> Revert or test; ID changes reset history.
                    no  -> Campaign side (budget, target, listing group, PMax asset group changes)?
                             yes -> hand to google-ads.
                             no  -> Seasonality, demand (best sellers report relative demand), or
                                    a Google change (check Merchant Center announcements, Ads Liaison posts).
```

## 5. Meta, TikTok, Microsoft, Pinterest, OpenAI quick table

| Platform | Where to see errors | Most common issues | Fix |
|----------|--------------------|-------------------|-----|
| Meta | Commerce Manager, Catalog, Issues | Image download failure, policy rejection, missing required fields, pixel match | See [Meta and TikTok module](meta-and-tiktok-catalogs.md) |
| TikTok ads catalog | Catalog Manager, item status | Image and landing page issues, policy | Fix data, resync |
| TikTok Shop | Seller Center, product status | Category attributes, compliance documents, prohibited claims | Edit listing, appeal |
| Microsoft | Microsoft Merchant Center catalog | Policy differences, crawl issues | Fix per item; check domain verification |
| Pinterest | Catalogs, data source status | Ingestion errors (format, image), policy | Fix and re-ingest |
| OpenAI | Onboarding feedback, Ads Manager feed status | Format (CSV vs required format), missing required fields, expired items (ads feed items expire after about two weeks if not refreshed) | Automate delivery (URL or SFTP), validate before upload |

## 6. Diagnostic queries

Merchant API (disapproved and limited items with click potential):
```sql
SELECT offer_id, title, aggregated_reporting_context_status, click_potential, click_potential_rank, item_issues
FROM product_view
WHERE aggregated_reporting_context_status IN ('NOT_ELIGIBLE_OR_DISAPPROVED', 'ELIGIBLE_LIMITED')
```

Google Ads (products with clicks and no sales, last 30 days, for villain review):
```sql
SELECT segments.product_item_id, segments.product_title,
       metrics.clicks, metrics.cost_micros, metrics.conversions, metrics.conversions_value
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS AND metrics.clicks > 30 AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
```

## 7. Escalation and support
- Merchant Center support: contact from the Help menu in the account; for suspensions use the review flow, not support chat.
- Google Ads reps can sometimes route Merchant Center escalations for larger accounts [Practitioner consensus].
- Record ticket IDs and outcomes in the journal.

## 8. What not to do
- Do not create a new Merchant Center account to escape a suspension: this is circumvention and can lead to permanent suspension of related accounts.
- Do not set `identifier_exists=no` to clear GTIN warnings on branded goods.
- Do not delete and re-add products to "reset" them: history and approvals are lost.
- Do not change product IDs to fix an issue.
- Do not hide shipping costs to look cheaper; price and shipping mismatches are policy issues.
- Do not request review before fixing everything you can find.

## Handoffs
| Situation | Hand off to | Pass |
|-----------|------------|------|
| Suspension affects campaigns | google-ads, growth-orchestrator | Status, revenue at risk, expected timeline |
| Landing page or checkout issues | cro | URLs, issue, evidence |
| Robots, crawl, rendering | seo | Blocked URLs and agents |
| Claims and copy changes on site | creative-strategy (copy), human (legal) | Claims list, policy reference |
