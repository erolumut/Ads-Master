# ChatGPT Shopping and the Agentic Commerce Protocol (ACP)

> The fastest-changing module in this skill. Knowledge as of 2026-10-08. Run the Freshness Protocol (chatgpt.com/merchants, developers.openai.com/commerce, the ACP GitHub changelog) before giving a merchant any instruction from this file.

## 1. Status at a glance (October 2026)

| Capability | Status | Evidence |
|-----------|--------|----------|
| Product discovery in ChatGPT (shopping answers, product carousels) | Live for US users | OpenAI merchants page [Official, 2026] |
| Instant Checkout inside ChatGPT (standalone) | Retired as a standalone feature in March 2026. Purchases complete on merchant-owned websites or apps. OpenAI said merchants could still offer in-chat checkout through apps in ChatGPT "for the time being". | OpenAI merchants page; CNBC 2026-03-24; TechCrunch 2026-03-24 [Official, 2026-03] |
| Shopify and Etsy catalogs | Integrated automatically, no application needed | OpenAI merchants page [Official, 2026] |
| Other merchants, organic feed | Apply at chatgpt.com/merchants (asks whether the feed meets the spec and the SKU count). Reported as waitlisted. A self-serve merchant platform is "later this year" per OpenAI. | [Official, 2026]; waitlist [Unverified] |
| Google-compatible feed path | OpenAI accepts Google-format product feeds; accepted products have search enabled and checkout disabled; per-item search opt-out needs an OpenAI-format feed | developers.openai.com/commerce products spec, via search snippet [Official, undated] |
| Product feed ads (ChatGPT Ads Manager, Feeds) | Beta from June 2026; self-serve in Ads Manager; feed products serve ads only, not organic answers, during the beta | PPC Land, SERoundtable, June 2026 [Official per coverage, 2026-06] |
| Feed share of ChatGPT shopping recommendations | Feed retrieval jumped from 8.26 percent to 61.54 percent of tracked picks on 2026-07-10 and was about 65 percent by 2026-09-03 in Profound's tracked prompts | Profound via SEJ 2026-09-09 [Study, 2026-09] with caveats below |
| ACP | Open spec maintained by OpenAI and Stripe, Apache 2.0, latest stable 2026-04-17 (feed, cart, orders, authentication, MCP binding) | GitHub repo [Official, 2026-04] |

Implication: in late 2026 the feed is the main lever for ChatGPT shopping visibility. Checkout integration is optional and secondary for most merchants.

## 2. Timeline

| Date | Event | Label |
|------|-------|-------|
| 2025-09-29 | Instant Checkout launches in ChatGPT for US users with Etsy sellers, Shopify merchants announced as coming; ACP open-sourced (initial spec version 2025-09-29) | [Official, 2025-09] |
| 2025-10-28 | PayPal joins as an ACP payment provider | [Official per coverage, 2025-10] |
| 2025-12-11 and 12 | Stripe Agentic Commerce Suite; ACP fulfillment enhancements | [Official, 2025-12] |
| 2026-01-16 and 30 | ACP capability negotiation; extensions, discounts and payment handlers | [Official, 2026-01] |
| 2026-02 | Forrester estimate of about 30 Shopify merchants live on Instant Checkout; other reports say about a dozen | [Contested] |
| 2026-03 (reports from 2026-03-06; OpenAI approach published by 2026-03-24) | OpenAI moves away from standalone Instant Checkout; prioritizes discovery and merchant-owned checkout; feed and promotion submissions emphasized. Reported reason includes Walmart data showing in-chat purchases converting at about one third the rate of click-outs | [Official, 2026-03]; Walmart figure [Unverified, reported] |
| 2026-04-17 | ACP release: push-model Feed API, carts, native orders, delegate authentication (3DS2), MCP transport binding, `/.well-known/acp.json` discovery, required Idempotency-Key | [Official, 2026-04] |
| 2026-06 (disclosed 2026-06-02; launch reported 2026-06-11) | Product feed ads in ChatGPT Ads Manager beta (Tools, Feeds, Create Feed) | [Official per coverage, 2026-06] |
| 2026-06-15 | Merchant Feed Terms of Service published (single source) | [Unverified] |
| 2026-07-10 | Feed-sourced recommendations overtake web retrieval in Profound's data | [Study, 2026-09] |
| 2026-08-31 and 09-16 | ChatGPT Ads self-serve beta expands to more countries (Europe, India, MENA, then UAE, Saudi Arabia, Israel, Turkey) | [Official per coverage, 2026-09] |

## 3. Paths to be present in ChatGPT shopping

```
Are you on Shopify or Etsy?
  yes -> catalog already integrated. Verify in Shopify admin (AI channels / Agentic Storefronts, Catalog)
         that products are shared and data is complete. Fix data in Shopify, not in ChatGPT.
  no  -> Do you have a clean Google Merchant Center feed?
           yes -> apply at chatgpt.com/merchants; submit the Google-compatible feed (search on, checkout off)
                  or, better, an OpenAI-format feed for per-item control.
           no  -> fix the master feed first (this skill), then apply.
Do you want paid placement in ChatGPT?
  yes -> hand off to chatgpt-ads: Ads Manager Feeds (beta). commerce-feeds prepares the feed.
Do you want in-chat checkout?
  Usually no in 2026. Consider only if OpenAI or a partner invites you, or you build an app in ChatGPT.
```

## 4. OpenAI product feed (file upload) essentials

Confirmed from the official spec page via search snippets [Official, undated, verify]:
- `item_id` is the unique product ID (per variant). Aliases accepted: `id` or `sku`. If several are sent, `item_id` wins.
- `is_eligible_search` and `is_eligible_checkout` are booleans. Aliases `enable_search` and `enable_checkout` are still accepted; when both naming styles are sent, the `enable_` fields win.
- Set `is_eligible_search` to false to remove a product from search. OpenAI keeps its last processed record for up to 14 days.
- Google-compatible products are accepted with search enabled and checkout disabled; uploading `is_eligible_search=false` does not opt a product out on that path.

Reported by multiple third-party guides [Unverified, verify in the live spec before building]:
| Topic | Reported requirement |
|-------|----------------------|
| Delivery | File upload to an SFTP location provided by OpenAI after acceptance |
| Formats | Parquet preferred; `jsonl.gz`, `csv.gz`, `tsv.gz` accepted; UTF-8; no XML |
| File naming | Stable file name, overwritten each run |
| Size | Up to 500,000 items per shard, files under about 500 MB |
| Refresh | Full snapshot at least daily; more often for price and stock |
| Required core | `item_id`, `title`, `description` (plain text), `url`/`link`, image, `price`, `availability`, `brand`, GTIN or MPN, `is_eligible_search` |
| Checkout eligibility | `is_eligible_checkout=true` requires `is_eligible_search=true` plus seller privacy policy and terms of service URLs (`seller_privacy_policy`, `seller_tos`) |
| Variants | One row per variant; group with an item group ID |
| Extras that help ranking | Reviews (count and average), product highlights, Q&A, related products, rich attributes [Practitioner consensus] |

Fees: OpenAI's merchants page says there are no fees on purchases that start in ChatGPT for discovery; a 4 percent fee was reported for the original Instant Checkout [Contested].

### Mapping from a Google feed to OpenAI format (template)

| OpenAI field | From Google attribute | Transform |
|-------------|----------------------|-----------|
| `item_id` | `id` | Same value: keep IDs identical across channels |
| `title` | `title` | As is (already optimized) |
| `description` | `description` | Strip HTML, plain text |
| `url` or `link` | `link` | Add `utm_source=chatgpt.com&utm_medium=referral` only if the site does not already receive it [Practitioner consensus: ChatGPT appends utm_source=chatgpt.com to many outbound links] |
| image field | `image_link`, `additional_image_link` | As is |
| `price` | `price` (+ `sale_price`) | Same currency formatting rules as spec |
| `availability` | `availability` | Map values to the spec enumeration |
| `brand`, `gtin`, `mpn` | same | As is |
| item group | `item_group_id` | As is |
| `is_eligible_search` | none | `true` for sellable, policy-safe items |
| `is_eligible_checkout` | none | `false` unless approved for checkout |
| seller policy URLs | site footer pages | Absolute URLs |

## 5. ACP Feed API (2026-04-17): the push model

From `spec/2026-04-17/openapi/openapi.feed.yaml` [Official, 2026-04]:
- Merchants push catalog data to agent-hosted feed services; agents do not pull from merchant endpoints.
- Endpoints: `POST /feeds` (create, with `target_country`), `GET /feeds/{id}`, `GET /feeds/{id}/products`, `PATCH /feeds/{id}/products` (partial upsert by `Product.id`; omitted products unchanged).
- Offline ingestion: `metadata.json` (FeedMetadata) plus `products.jsonl` (one Product per line) fully replaces the product set.
- Product: `id` (required), `title`, `description` (`plain`, `html`, `markdown`), `url`, `media[]`, `variants[]` (required).
- Variant: `id` and `title` required; `description`, `url`, `barcodes[]` (`type` such as GTIN, UPC, EAN, and `value`), `price` and `list_price` (integer minor units plus ISO 4217 currency, for example `{"amount": 1999, "currency": "USD"}`), `unit_price`, `availability` (`available` boolean plus `status`: `in_stock`, `limited_stock`, `backorder`, `preorder`, `out_of_stock`, `discontinued`), `categories[]` (`value` plus `taxonomy` such as `google_product_category`, `shopify`, `merchant`), `condition[]`, `variant_options[]` (name and value), `media[]` (first item is the primary listing asset; `type`, `url`, `alt_text`, `width`, `height`), `seller` (name and `links[]` typed `privacy_policy`, `terms_of_service`, `refund_policy`, `shipping_policy`, `faq`), `marketplace`.
- Promotions in the feed were deferred to a later release.

Example `products.jsonl` line:
```json
{"id":"prod_merino_crew","title":"Acme Merino Crew Neck Sweater","description":{"plain":"Midweight 100 percent merino crew neck. Machine washable at 30 C."},"url":"https://www.example.com/products/merino-crew","media":[{"type":"image","url":"https://cdn.example.com/merino-crew-navy.jpg","alt_text":"Navy merino crew neck sweater, front"}],"variants":[{"id":"SKU-MC-NAVY-M","title":"Acme Merino Crew Neck Sweater, Navy, M","barcodes":[{"type":"GTIN","value":"00012345600012"}],"price":{"amount":8900,"currency":"USD"},"availability":{"available":true,"status":"in_stock"},"categories":[{"value":"Apparel & Accessories > Clothing > Shirts & Tops","taxonomy":"google_product_category"}],"condition":["new"],"variant_options":[{"name":"Color","value":"Navy"},{"name":"Size","value":"M"}],"seller":{"name":"Acme","links":[{"type":"refund_policy","url":"https://www.example.com/policies/refunds"},{"type":"shipping_policy","url":"https://www.example.com/policies/shipping"},{"type":"privacy_policy","url":"https://www.example.com/policies/privacy"},{"type":"terms_of_service","url":"https://www.example.com/policies/terms"}]}}]}
```

Note the difference between the ACP Feed API object model (nested products and variants, prices in minor units) and OpenAI's flat file-upload spec (one row per variant). Implement whichever OpenAI asks for at onboarding; keep a single internal model that can emit both.

## 6. ACP checkout (only if invited or building an app)
- Specs in the repo: Agentic Checkout API (`openapi.agentic_checkout.yaml`) with webhooks, Delegate Payment (`openapi.delegate_payment.yaml`), Cart (`openapi.cart.yaml`), Delegate Authentication (3DS2), Feed.
- Checkout session lifecycle over REST or MCP tools: `create_checkout_session`, `get_checkout_session`, `update_checkout_session`, `complete_checkout_session`, `cancel_checkout_session`.
- Requirements (2026-04-17): `Idempotency-Key` header on every POST (max 255 chars); webhook signing header `t=<unix_seconds>,v1=<hex>` with a 300-second replay window; discovery document at `/.well-known/acp.json`; order statuses `created`, `confirmed`, `manual_review`, `processing`, `shipped`, `delivered`, `canceled`; markdown fields follow CommonMark 0.31.2 with raw HTML disabled.
- Payment: Stripe Shared Payment Token or other PSP handlers; merchant stays merchant of record.
- Who should build it in 2026: platforms, very large retailers with an OpenAI relationship, or teams building a ChatGPT app. Everyone else: invest in the feed and the PDP.

## 7. Ranking and visibility levers in ChatGPT shopping [Practitioner consensus unless labeled]
1. Be in the feed index: Shopify Catalog sharing on, or an accepted direct feed. Profound's data shows visibility shifting to feed-integrated merchants after July 2026 and concentrating (top 10 stores' share of references rose from 22.5 to 41.8 percent; unique merchants referenced fell from 13,524 to 10,607) [Study, 2026-09, Profound tracked prompts only].
2. Data completeness: identifiers, variant attributes, clear descriptions, policies, shipping and returns.
3. Price competitiveness and availability accuracy.
4. Reviews: ratings and review counts in the feed and on the PDP.
5. Web presence still matters: earlier analysis found most ChatGPT carousel products matched Google Shopping data (about 83 percent in a 43,000-product sample) [Study, 2025, via secondary coverage], and organic citations come from the web. Hand off web visibility to ai-search-optimization.
6. Crawl access: allow OpenAI's search crawler (OAI-SearchBot) in robots.txt and at the CDN or bot manager, or ChatGPT cannot verify your pages. Blocking GPTBot (training) is a separate decision.

## 8. Measurement
- ChatGPT referral traffic appears in analytics as `chatgpt.com` referrals (often with `utm_source=chatgpt.com`).
- Shopify reports orders by AI channel when sold through Agentic Storefronts.
- Without in-chat checkout, conversion happens on site: standard attribution works, but expect undercounting when users copy product names into search instead of clicking.
- Hand off to measurement: create a channel grouping for AI assistants (chatgpt.com, perplexity.ai, copilot.microsoft.com, gemini.google.com).

## 9. Readiness checklist (score 0 to 2 each)
| # | Check |
|---|-------|
| 1 | Product feed passes this skill's QA (no invalid GTINs, accurate price and stock) |
| 2 | IDs identical across Google, Meta and the OpenAI feed |
| 3 | Shopify: Catalog sharing and AI channels reviewed and decided by the human; or non-Shopify: application submitted |
| 4 | PDPs server-render price, availability and Product JSON-LD |
| 5 | robots.txt and bot manager allow OAI-SearchBot |
| 6 | Policy pages (shipping, returns, privacy, terms, contact) linked in the footer with absolute URLs |
| 7 | Reviews present on PDP and in the feed where accepted |
| 8 | Analytics channel grouping for AI assistants exists |
| 9 | Product feed ads decision made with chatgpt-ads (yes, no, later) |
| 10 | Owner and refresh schedule for the OpenAI feed documented |

## 10. Risks and open questions
- Spec instability: field names changed once already (aliases). Pin the version you build against and recheck monthly.
- Waitlists and eligibility change without notice.
- Profound's data covers its tracked prompts only and does not prove causation [Study caveat].
- Ads feeds and organic feeds are separate programs today; keep both pipelines generated from the same master.
