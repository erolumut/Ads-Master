# Sources (annotated)

> Read on 2026-10-08 unless stated. "Primary" means read directly from the publisher's code repository or document. "Via search" means the content was read through search result extracts because the publisher's site was not reachable from the research environment; treat those as needing a recheck. Dates are publication or last update dates where known.

## Google Merchant Center, Merchant API, Google Shopping

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | Merchant API products_common.proto (ProductAttributes) | Google (googleapis) | https://github.com/googleapis/googleapis/blob/master/google/shopping/merchant/products/v1/products_common.proto | Latest commit 2026-09-29 (primary) | Attribute names, limits (GTINs up to 10, Q&A limits), new attributes, DigitalSourceType, loyalty fields, related product types |
| 2 | Commit history of products_common.proto | Google (googleapis) | https://github.com/googleapis/googleapis/commits/master/google/shopping/merchant/products/v1/products_common.proto | 2025-08-05 to 2026-09-29 (primary) | Dates of carrier_shipping (2025-10-06), handling cutoff fields (2026-03-11), video_links (2026-04-20), Q&A and other attributes (2026-07-13), offer-level returns (2026-09-29) |
| 3 | Merchant API products.proto and productinputs.proto | Google (googleapis) | https://github.com/googleapis/googleapis/tree/master/google/shopping/merchant/products/v1 | 2026 (primary) | Product naming, base64url IDs, legacy_local, version_number, 30-day refresh, insert and patch endpoints |
| 4 | Merchant API reports.proto | Google (googleapis) | https://github.com/googleapis/googleapis/blob/master/google/shopping/merchant/reports/v1/reports.proto | 2026 (primary) | Report views: price competitiveness, price insights, best sellers, product view, competitive visibility |
| 5 | Merchant API datasourcetypes.proto | Google (googleapis) | https://github.com/googleapis/googleapis/blob/master/google/shopping/merchant/datasources/v1/datasourcetypes.proto | 2025-08-04, 2025-10-31 (primary) | Data source types, feed label rules, default_rule precedence |
| 6 | Shopping types.proto (destinations, reporting contexts) | Google (googleapis) | https://github.com/googleapis/googleapis/blob/master/google/shopping/type/types.proto | 2026 (primary) | FREE_LISTINGS_UCP_CHECKOUT, YouTube and Demand Gen contexts |
| 7 | Merchant API sub-API directory | Google (googleapis) | https://github.com/googleapis/googleapis/tree/master/google/shopping/merchant | 2026 (primary) | Sub-APIs including productstudio v1alpha, loyaltycustomers, notifications |
| 8 | Introducing Merchant API | Google Merchant Center Help | https://support.google.com/merchants/answer/16493611?hl=en | 2025 (via search) | Content API shutdown on 2026-08-18 |
| 9 | Merchant Center product data specification update 2026 | Google Merchant Center Help | https://support.google.com/merchants/answer/16989427?hl=en | 2026 (via search) | 2026-04-14 changes, video timing, 500 x 500 from 2027-01-31 |
| 10 | Merchant Center announcements change log | Google Merchant Center Help | https://support.google.com/merchants/announcements/6192467?hl=en | Ongoing (via search) | Pickup cost (2026-04-28) and other changes |
| 11 | Google Updates Some Merchant Center Product Specifications For 2026 | Search Engine Roundtable | https://www.seroundtable.com/google-updates-some-merchant-center-product-spec-41171.html | 2026 | Secondary confirmation of spec update |
| 12 | Google Merchant API replacing the Content API for Shopping | Search Engine Roundtable | https://www.seroundtable.com/google-merchant-api-content-api-for-shopping-39958.html | 2025 | Merchant API GA context |
| 13 | Google launches Merchant API, signals transition from Content API | PPC Land | https://ppc.land/google-launches-merchant-api-signals-transition-from-content-api/ | 2024 to 2025 | Migration background |
| 14 | Google is sunsetting the Content API for Shopping | Producthero | https://www.producthero.com/post/google-is-sunsetting-the-content-api-for-shopping-what-you-need-to-know | 2025 to 2026 | Migration impact for advertisers |
| 15 | Google Merchant API migration before the August 2026 deadline | Productsup | https://www.productsup.com/blog/google-merchant-api-migration-what-changes-before-the-august-2026-deadline-and-how-to-prepare/ | 2026 | v1beta retirement (2026-02-28), migration steps |
| 16 | Google Merchant API migration | Feedonomics | https://feedonomics.com/blog/google-merchant-api-migration/ | 2025 to 2026 | Vendor migration approach |
| 17 | Merchant API in Google Ads Scripts: April 22 migration | Digital Applied | https://www.digitalapplied.com/blog/merchant-api-google-ads-scripts-april-22-migration | 2026 | Scripts migration (single source) |
| 18 | Content API for Shopping sunset: extension form | Elsop | https://www.elsop.com/content-api-shopping-sunset/ | 2026 | Extended access request form |
| 19 | GMC multi-channel product ID requirements | Adsroid | https://adsroid.com/google-merchant-center-updates-multi-channel-product-id-requirements/ | 2026-01 | Online and in-store ID guidance (Unverified enforcement) |
| 20 | GMC Product Data Specification 2026 released | PPC News Feed | https://ppcnewsfeed.com/ppc-news/2026-04/gmc-product-data-specification-2026-released/ | 2026-04 | Secondary confirmation |
| 21 | Google for WooCommerce readme and changelog | WooCommerce, Google | https://github.com/woocommerce/google-listings-and-ads | 3.9.5 on 2026-09-29 (primary) | WooCommerce sync behavior |

## Google AI shopping, UCP, AP2

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 22 | About UCP and UCP-powered checkout on Google | Google Merchant Center Help | https://support.google.com/merchants/answer/16837055?hl=en | 2026 (via search) | Eligibility, select merchants, countries |
| 23 | How to onboard to the UCP integration hub in Merchant Center | Google Merchant Center Help | https://support.google.com/merchants/answer/16992327?hl=en | 2026-10 (via search) | US first, Canada and Australia next year |
| 24 | Under the Hood: Universal Commerce Protocol | Google Developers Blog | https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/ | 2026-01 (via search) | UCP design, AP2 compatibility |
| 25 | New tech and tools for retailers in an agentic shopping era | Google (The Keyword) | https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/ | 2026-01 (via search) | UCP launch, partners, new Merchant Center attributes |
| 26 | Google Marketing Live 2026 shopping updates (title paraphrased) | Google (The Keyword) | https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/ | 2026-05-20 (via search) | UCP expansion to Canada, Australia, later UK |
| 27 | UCP specification repository | Universal Commerce Protocol | https://github.com/Universal-Commerce-Protocol/ucp | Commits to 2026-10-07 (primary) | Capabilities, transports, versions, catalog, ask, lodging |
| 28 | UCP catalog capability | Universal Commerce Protocol | https://github.com/Universal-Commerce-Protocol/ucp/blob/main/docs/specification/shopping/catalog/index.md | 2026 (primary) | Catalog search and lookup IDs and fields |
| 29 | Google rolling out agentic Buy for me | 9to5Google | https://9to5google.com/2025/11/13/google-agentic-shopping/ | 2025-11-13 | Agentic checkout launch and merchants |
| 30 | Google rolls out agentic commerce in Search and Gemini | The Register | https://www.theregister.com/2026/01/12/google_gemini_agentic_ai_shopping_protocol/ | 2026-01-12 | UCP launch coverage |
| 31 | Google Search adds AI try-on, previews agentic checkout | Search Engine Land | https://searchengineland.com/google-search-ai-try-on-agentic-checkout-455716 | 2025-05 | I/O 2025 shopping features |
| 32 | Canada and Australia face 2027 wait for Merchant Center UCP hub | PPC Land | https://ppc.land/canada-and-australia-face-2027-wait-for-googles-merchant-center-ucp-hub/ | 2026-10 | Rollout timing conflict |
| 33 | Google tests buying from Flipkart through Gemini and AI Mode in India | TechCrunch | https://techcrunch.com/2026/09/26/google-tests-buying-from-walmart-owned-flipkart-through-gemini-and-ai-mode-in-india/ | 2026-09-26 | India test |
| 34 | Google donates Agent Payments Protocol to FIDO Alliance | Google (The Keyword) | https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/ | 2026-04 (via search) | AP2 governance |
| 35 | AP2 repository | Google Agentic Commerce | https://github.com/google-agentic-commerce/AP2 | 2026 (primary) | AP2 samples and status |
| 36 | PayPal and Google Cloud agentic commerce solution | Google Cloud Blog | https://cloud.google.com/blog/topics/financial-services/introducing-an-agentic-commerce-solution-for-merchants-from-paypal-and-google-cloud | 2025 (via search) | AP2 deployment |
| 37 | Google UCP merchant guide | commercetools | https://commercetools.com/blog/google-ucp-merchant-guide-to-agentic-commerce | 2026 | Integration options |
| 38 | Google UCP and Merchant Center | ChannelEngine | https://www.channelengine.com/en/blog/google-universal-commerce-protocol-merchant-center-ai-shopping | 2026 | native_commerce attribute claim (Unverified) |
| 39 | Google agentic checkout guide | BigCommerce | https://www.bigcommerce.com/articles/ecommerce/google-agentic-checkout/ | 2026 | Merchant enablement |

## OpenAI, ChatGPT, ACP

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 40 | Agentic Commerce Protocol repository | OpenAI and Stripe | https://github.com/agentic-commerce-protocol/agentic-commerce-protocol | Latest stable 2026-04-17 (primary) | Versions, maintainers, license |
| 41 | ACP changelog 2026-04-17 | OpenAI and Stripe | https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/main/changelog/2026-04-17.md | 2026-04-17 (primary) | Feed API, carts, orders, MCP, idempotency, acp.json |
| 42 | ACP Feed API OpenAPI spec | OpenAI and Stripe | https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/main/spec/2026-04-17/openapi/openapi.feed.yaml | 2026-04-17 (primary) | Product and variant schema |
| 43 | Power product discovery in ChatGPT | OpenAI | https://chatgpt.com/merchants/ | 2026 (via search) | Shopify and Etsy automatic, application, checkout moved to merchant sites, self-serve later this year |
| 44 | Commerce products spec (file upload) | OpenAI Developers | https://developers.openai.com/commerce/specs/file-upload/products | Undated (via search) | item_id, is_eligible_search, aliases, Google-compatible path, 14-day retention |
| 45 | Commerce file upload overview | OpenAI Developers | https://developers.openai.com/commerce/specs/file-upload/overview | Undated (via search) | Delivery model |
| 46 | OpenAI revamps shopping experience in ChatGPT after Instant Checkout | CNBC | https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html | 2026-03-24 | Checkout pivot |
| 47 | OpenAI's first crack at online shopping stumbled | CNBC | https://www.cnbc.com/2026/03/20/open-ai-agentic-shopping-etsy-shopify-walmart-amazon.html | 2026-03-20 | Adoption context |
| 48 | OpenAI's plans to make ChatGPT more like Amazon | TechCrunch | https://techcrunch.com/2026/03/24/openais-plans-to-make-chatgpt-more-like-amazon-arent-going-so-well | 2026-03-24 | Apps in ChatGPT checkout statement |
| 49 | ChatGPT lets shoppers buy products within the platform | Retail Dive | https://www.retaildive.com/news/openai-chatgpt-instant-checkout-agentic-commerce-etsy-shopify/761442/ | 2025-09-29 | Instant Checkout launch |
| 50 | OpenAI expands agentic commerce push | Digital Commerce 360 | https://www.digitalcommerce360.com/2026/02/16/openai-expands-agentic-commerce-push/ | 2026-02-16 | Pre-pivot status |
| 51 | ChatGPT Ads Manager now supports product feeds | PPC Land | https://ppc.land/chatgpt-ads-manager-now-supports-product-feeds-after-checkout-is-killed/ | 2026-06 | Feed ads beta, SFTP, limits (Contested) |
| 52 | ChatGPT Ads gains upload product feeds | Search Engine Roundtable | https://www.seroundtable.com/chatgpt-ads-product-feeds-41488.html | 2026-06 | Feed ads beta |
| 53 | ChatGPT Shopping results lean hard on product feeds | Search Engine Journal | https://www.searchenginejournal.com/chatgpt-shopping-results-lean-hard-on-product-feeds/589000/ | 2026-09-09 | Profound data |
| 54 | Profound launches shopping analysis | PR Newswire (Profound) | https://www.prnewswire.com/news-releases/profound-launches-shopping-analysis-as-ai-assistants-become-the-new-front-door-to-retail-302614397.html | 2026 | Study source |
| 55 | OpenAI launches self-serve Ads Manager for ChatGPT | Search Engine Journal | https://www.searchenginejournal.com/openai-launches-self-serve-ads-manager-for-chatgpt/573971/ | 2026 | Ads Manager context |
| 56 | How retail executives will evaluate ChatGPT checkout | Modern Retail | https://www.modernretail.co/technology/how-retail-executives-will-be-evaluating-chatgpt-checkout-this-holiday-season/ | 2025-11 | Merchant sentiment |
| 57 | Your Google Shopping feed is already powering ChatGPT | Athos Commerce | https://athoscommerce.com/blog/your-google-shopping-feed-is-already-powering-chatgpt/ | 2026 | Overlap with Google Shopping data |
| 58 | Product feeds for AI | Patrick Stox | https://patrickstox.com/ecommerce-seo/ai-commerce/product-feeds-for-ai/ | 2026 | Practitioner view of AI feeds |

## Microsoft, Perplexity, Shopify, Meta, Pinterest, schema.org

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 59 | Conversations that convert: Copilot Checkout and Brand Agents | Microsoft Advertising Blog | https://about.ads.microsoft.com/en/blog/post/january-2026/conversations-that-convert-copilot-checkout-and-brand-agents | 2026-01 (via search) | Copilot Checkout terms |
| 60 | Microsoft launches Copilot Checkout and Brand Agents | Search Engine Land | https://searchengineland.com/microsoft-launches-copilot-checkout-and-brand-agents-467175 | 2026-01 | Launch coverage |
| 61 | Copilot in-app checkout and merchant data from 500,000 sellers | Windows Central | https://www.windowscentral.com/microsoft/windows-11/copilots-shopping-upgrade-brings-checkout-to-the-mobile-app-with-deeper-data-from-half-a-million-merchants | 2026-04 | Mobile checkout, catalog size |
| 62 | Microsoft and PayPal launch Copilot Checkout | gHacks | https://www.ghacks.net/2026/01/09/microsoft-and-paypal-launch-copilot-checkout-for-in-chat-purchases/ | 2026-01-09 | Partners |
| 63 | Perplexity Shopping guide | Shopify Blog | https://www.shopify.com/blog/perplexity-shopping | 2025 to 2026 | Instant Buy orders and admin |
| 64 | Perplexity launches free shopping agent | TechBuzz | https://www.techbuzz.ai/articles/perplexity-ai-launches-free-shopping-agent-to-challenge-openai | 2025-11 | Instant Buy expansion |
| 65 | Spring '26 Edition | Shopify | https://www.shopify.com/news/spring-26-edition-merchant | 2026 (via search) | Catalog, agentic commerce |
| 66 | Shopify launches Agentic Storefronts | The Keyword (news site) | https://www.thekeyword.co/news/shopify-launches-agentic-storefronts | 2026 | Launch coverage |
| 67 | Meta Business SDK ProductItem and ProductCatalog | Meta | https://github.com/facebook/facebook-python-business-sdk | API v26.0, SDK v26.0.2 (primary) | Catalog fields, batch endpoints |
| 68 | Pinterest API description (OpenAPI) | Pinterest | https://github.com/pinterest/api-description | v5.28.0 (primary) | Catalog attributes, ai_disclosures, checkout_enabled deprecated |
| 69 | schema.org release history | schema.org | https://schema.org/docs/releases.html (read from the schemaorg GitHub repository) | v28.0 2024-09-17; v29.0 2025-03-24; v30.1 2026-09-16 (primary) | MemberProgram, ShippingService, retail feed vocabulary, DPP |
| 70 | How to get ChatGPT to recommend your product | Bazaarvoice | https://www.bazaarvoice.com/blog/how-to-get-featured-on-chatgpt-ai-recommendations/ | 2026 | Conflicting PDP versus feed figures |

## Verification pass (2026-10-08, via search)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 71 | Native commerce [native_commerce] | Google Merchant Center Help | https://support.google.com/merchants/answer/17251586 | Checked 2026-10 | Attribute structure, optional, Buy button |
| 72 | How to onboard to the UCP integration hub in Merchant Center | Google Merchant Center Help | https://support.google.com/merchants/answer/16992327 | 2026-10 | Selection, sandbox, US early access |
| 73 | Google rolls out Merchant Center UCP integration hub in the U.S. | Search Engine Land | https://searchengineland.com/google-rolls-out-merchant-center-ucp-integration-hub-in-the-u-s-493889 | 2026-10-06 | Canada and Australia moved to 2027 |
| 74 | Merchant API is coming to Google Ads scripts starting April 22, 2026 | Google Ads Developer Blog | https://ads-developers.googleblog.com/2026/04/merchant-api-is-coming-to-google-ads.html | 2026-04 | Scripts migration date |
| 75 | Content API for Shopping release notes | Google for Developers | https://developers.google.com/shopping-content/guides/rel-notes | Checked 2026-10 | Sunset 2026-08-18, progressive errors from 2026-09-01 |
| 76 | Google Content API for Shopping Extended Access Form | Search Engine Roundtable | https://www.seroundtable.com/google-content-api-extension-41710.html | 2026 | Extension dates 2026-10-15 or 2026-12-31 |
| 77 | Updates to Meta Shops checkout for BigCommerce | BigCommerce | https://www.bigcommerce.com/blog/updates-to-meta-shops-checkout-for-bigcommerce/ | 2025 | Shops move to website checkout |
| 78 | Meta turns to AI to make shopping easier on Instagram and Facebook | TechCrunch | https://techcrunch.com/2026/03/25/meta-turns-to-ai-to-make-shopping-easier-on-instagram-and-facebook/ | 2026-03-25 | One-tap checkout in Facebook ads |
| 79 | TikTok Shop Makes GMV Max Ads Mandatory From Sept 1 | CedCommerce | https://cedcommerce.com/blog/tiktok-shop-mandates-gmv-max-use-for-ads-what-this-means-for-your-strategy/ | 2025 | GMV Max mandatory date |
| 80 | Import from Google Merchant Center | Microsoft Advertising Help | https://help.ads.microsoft.com/apex/index/3/en/56870 | Checked 2026-10 | Import tool, schedules, approved offers only |
| 81 | Feed: How to submit my GoDataFeed feed to ChatGPT Ads? | GoDataFeed Help | https://help.godatafeed.com/hc/en-us/articles/51837706971675-Feed-How-to-submit-my-GoDataFeed-feed-to-ChatGPT-Ads | 2026 | 1,000 minimum and 2 million maximum claim |
| 82 | OpenAI makes it easier to run shopping ads in ChatGPT | Digiday | https://digiday.com/marketing/openai-makes-it-easier-to-run-shopping-ads-in-chatgpt/ | 2026-06 | 100-product sample and 1 million SKU claim |
| 83 | Amazon.com Services, LLC v. Perplexity AI, Inc. (No. 26-1444) | US Court of Appeals for the Ninth Circuit | https://cdn.ca9.uscourts.gov/datastore/opinions/2026/08/04/26-1444.pdf | 2026-08-04 | Comet injunction vacated |
| 84 | Catalog Product Parameters | TikTok Ads Help | https://ads.tiktok.com/help/article/catalog-product-parameters | Updated 2025-02 | Nine required catalog fields |
| 85 | How to create a Catalog | TikTok Ads Help | https://ads.tiktok.com/help/article/create-manage-catalogs | Updated 2026-01 | Feed formats and sync options |

## Recheck list (sources read only via search)
Items 8, 9, 10, 22, 23, 24, 25, 26, 34, 36, 43, 44, 45, 59, 65 and 71 to 85: open the live page before quoting in a client deliverable.

## Monitoring list (what to check, how often)

| Source | URL | Check for | Cadence |
|--------|-----|-----------|---------|
| Merchant Center announcements | https://support.google.com/merchants/announcements/6192467 | Spec changes, policy updates, deadlines | Monthly and before any audit |
| Product data specification | https://support.google.com/merchants/answer/7052112 | Attribute requirements by country | Before bulk feed changes |
| Merchant API release notes and protos | https://github.com/googleapis/googleapis/tree/master/google/shopping/merchant | New fields (often weeks before UI docs) | Monthly |
| UCP help and integration hub | https://support.google.com/merchants/answer/16837055 | Countries, eligibility, attributes | Monthly |
| UCP repository | https://github.com/Universal-Commerce-Protocol/ucp | New protocol versions and capabilities | Monthly |
| OpenAI merchants page | https://chatgpt.com/merchants/ | Application status, self-serve platform, checkout policy | Monthly |
| OpenAI commerce specs | https://developers.openai.com/commerce | Feed field names, formats, aliases | Before building or changing the OpenAI feed |
| ACP repository changelog | https://github.com/agentic-commerce-protocol/agentic-commerce-protocol | New releases (dated versions) | Monthly |
| Microsoft Advertising blog | https://about.ads.microsoft.com/en/blog | Copilot Checkout, Merchant Center changes | Monthly |
| Meta Marketing API changelog and Commerce Manager notices | https://developers.facebook.com/docs/graph-api/changelog | Catalog field and Shops changes | Quarterly, and on each API version |
| Pinterest API description | https://github.com/pinterest/api-description | Catalog attribute changes | Quarterly |
| schema.org releases | https://schema.org/docs/releases.html | Product and Offer vocabulary | Quarterly |
| Shopify changelog and Editions | https://changelog.shopify.com and https://www.shopify.com/editions | Catalog, AI channels, Google app changes | Monthly |
| Google for WooCommerce changelog | https://github.com/woocommerce/google-listings-and-ads | Sync behavior | Quarterly |

## Evidence handling rules
1. Prefer the code repository (protos, OpenAPI files) for field names and dates: they are versioned and dated.
2. Prefer help center pages for requirements and policies; quote the date you read them.
3. Treat vendor blogs as leads, not facts, unless they cite a primary source you can open.
4. When two sources conflict, write both with dates and label the claim [Contested] until a primary source settles it.
5. Never copy a number from a vendor case study into a forecast without the [Unverified] label.
