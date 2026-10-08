# Sources

Annotated sources behind the lifecycle-crm package. Seen dates are 2026-10-08 unless noted. Method: web search summaries (direct page fetching was blocked in the build environment), plus primary reads of the Klaviyo OpenAPI specification, the Klaviyo Python SDK changelog and the Iterable MCP server repository cloned from GitHub. Items marked secondary were read through publisher summaries; re-verify before quoting externally.

Evidence key: O = official vendor or regulator; L = law firm or legal publisher; S = study or data report; V = vendor or agency blog (secondary); N = news.

## Deliverability and mailbox providers

| # | Title | Publisher | URL | Date | Supports | Type |
|---|-------|-----------|-----|------|----------|------|
| 1 | Email sender guidelines FAQ | Google | https://support.google.com/a/answer/14229414 | ongoing | Bulk sender rules, spam rate 0.1% and 0.3%, rejection behavior | O |
| 2 | Email sender guidelines | Google | https://support.google.com/a/answer/81126 | ongoing | All sender and bulk sender requirements | O |
| 3 | Why Gmail is rejecting your emails | Valimail | https://www.valimail.com/blog/google-email-compliance-enforcement/ | 2025-11 | Enforcement shift to temporary and permanent rejections | V |
| 4 | Gmail's enforcement ramps up | Red Sift | https://redsift.com/blog/gmails-enforcement-ramps-up-what-bulk-senders-need-to-know | 2025-11 | 4.7.x vs 5.7.x codes; bulk status permanent | V |
| 5 | New Gmail bulk sender compliance updates November 2025 | Suped | https://www.suped.com/blog/new-gmail-bulk-sender-compliance-updates-november-2025 | 2025-11 | November 2025 enforcement | V |
| 6 | Microsoft enforces SPF, DKIM, DMARC for high-volume senders | dmarcian | https://dmarcian.com/microsoft-enforces-spf-dkim-dmarc/ | 2025 | Outlook consumer requirements, 2025-05-05 | V |
| 7 | Outlook error 550 5.7.515 and how to fix it | URIports | https://www.uriports.com/blog/outlook-error-550-5-7-515-and-how-to-fix-it/ | 2025 | Rejection text | V |
| 8 | Microsoft sender requirements: 2026 reference | Mailercloud | https://www.mailercloud.com/blog/microsoft-sender-requirements | 2026 | 2026 status, conflicting claims | V |
| 9 | Postmaster information for iCloud Mail | Apple | https://support.apple.com/en-us/102322 | ongoing | Apple bulk requirements | O |
| 10 | Yahoo Sender Hub Insights and Google Postmaster Tools v2 | Validity | https://www.validity.com/blog/peek-behind-the-curtain-how-email-marketers-should-use-yahoos-new-sender-hub-insights-and-google-postmaster-tools-v2/ | 2025 | Monitoring tools | V |
| 11 | Learn about the deprecation of the old Postmaster Tools interface | Gmail Help | https://support.google.com/mail/answer/16594218 | 2025 to 2026 | Postmaster v2, v1 API retirement, reputation not in v2 | O |
| 12 | BIMI in 2026: verified logos, CMCs | Red Sift | https://redsift.com/guides/bimi-in-2026-verified-logos-cmcs-and-the-fastest-path-to-inbox-display | 2026 | VMC vs CMC; checkmark only with VMC | V |
| 13 | Google CMC BIMI announcement | Valimail | https://www.valimail.com/blog/google-cmc-bimi-announcement/ | 2024 | CMC acceptance | V |
| 14 | Manage email subscriptions from a single location in Gmail | Google Workspace Updates | https://workspaceupdates.googleblog.com/2025/07/manage-email-subscriptions-in-gmail.html | 2025-07 | Manage subscriptions view | O |
| 15 | New purchase tracking view and more relevant promotions in Gmail | Google | https://blog.google/products-and-platforms/products/gmail/one-stop-purchase-tracking-in-gmail/ | 2025-09-11 | Promotions most relevant sorting, Purchases view | O |
| 16 | Relevance comes to the Gmail promo tab | Spam Resource | https://www.spamresource.com/2025/09/relevance-comes-to-gmail-promo-tab.html | 2025-09 | Practitioner analysis | V |
| 17 | Gmail's Gemini AI is changing the inbox | Klaviyo | https://www.klaviyo.com/blog/gmail-gemini-in-the-inbox | 2025 | Gemini summaries guidance | V |
| 18 | Email client market share | Litmus | https://www.litmus.com/email-client-market-share | 2026-07 | Apple and Gmail share of tracked opens | S |
| 19 | RFC 8058 Signaling one-click functionality for list email headers | IETF | https://www.rfc-editor.org/rfc/rfc8058 | 2017-01 | One click unsubscribe headers | O |

## Consent, privacy and law

| # | Title | Publisher | URL | Date | Supports | Type |
|---|-------|-----------|-----|------|----------|------|
| 20 | Recommendation on tracking pixels in emails | CNIL | https://www.cnil.fr/sites/default/files/2026-05/recommandation_tracking_pixels_emails.pdf | 2026-04 | Consent for pixels, exemptions | O |
| 21 | CNIL issues FAQs on recommendation for tracking pixels in emails | Hunton | https://www.hunton.com/privacy-and-cybersecurity-law-blog/cnil-issues-faqs-on-recommendation-for-tracking-pixels-in-emails | 2026 | Transition, scope | L |
| 22 | France: email tracking pixels, what the CNIL recommendation changes | Baker McKenzie | https://connectontech.bakermckenzie.com/france-email-tracking-pixels-what-the-cnils-recommendation-changes-in-practice/ | 2026 | Practical implications | L |
| 23 | Statement on the commencement of the DUAA | ICO | https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/statement-on-the-commencement-of-the-data-use-and-access-act-duaa/ | 2026-02 | 2026-02-05 commencement, fines | O |
| 24 | The charitable purposes soft opt-in | Lewis Silkin | https://www.lewissilkin.com/insights/2026/05/08/the-charitable-purposes-soft-opt-in-ico-issues-updated-direct-marketing-guidanc-102ms57 | 2026-05-08 | Charity soft opt-in guidance | L |
| 25 | How do we comply with the PECR electronic mail marketing rules? | ICO | https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/how-do-we-comply-with-the-pecr-electronic-mail-marketing-rules/ | 2026 | Soft opt-in conditions | O |
| 26 | Digital Omnibus reshapes EU cookie rules | Osborne Clarke | https://www.osborneclarke.com/insights/digital-omnibus-reshapes-eu-cookie-rules-leaves-banner-fatigue-largely-intact | 2025 to 2026 | Omnibus proposal status | L |
| 27 | How the Digital Omnibus could reshape cookie compliance | Freshfields | https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/how-the-eu-commissions-digital-omnibus-could-reshape-cookie-compliance-in-europe-102m196 | 2025-11 | Article 88a proposal | L |
| 28 | Eleventh Circuit vacates FCC one-to-one consent rule | Pierce Atwood | https://www.pierceatwood.com/alerts/eleventh-circuit-vacates-fccs-tcpa-one-one-consent-rule-eve-effective-date | 2025-01 | One-to-one vacatur 2025-01-24 | L |
| 29 | FCC issues final rule formally eliminating one-to-one consent | Goodwin | https://www.goodwinlaw.com/en/insights/blogs/2025/09/the-fcc-issues-final-rule-formally-eliminating-the-one-to-one-consent-requirement | 2025-09 | Formal removal | L |
| 30 | FCC delays revoke-all rule until January 31, 2027 | Burr and Forman | https://www.burr.com/telephone-consumer-protection-act/the-fcc-delays-effective-date-of-tcpa-revoke-all-rule-until-january-31-2027 | 2026-01 | Delay order 2026-01-06 | L |
| 31 | FCC adopts final order and further notice on TCPA consent revocation | Inside Global Tech (Covington) | https://www.insideglobaltech.com/2026/10/02/update-fcc-adopts-final-order-and-further-notice-on-tcpa-consent-revocation/ | 2026-10-02 | 2026-09-30 order | L |
| 32 | FCC scraps revoke all and lets businesses pick how consumers opt out | Nixon Peabody | https://nixonpeabody.com/insights/alerts/2026/10/07/fcc-scraps-revoke-all-and-lets-businesses-pick-how-consumers-opt-out | 2026-10-07 | Order content | L |
| 33 | A loud decision on TCPA quiet hours | Nixon Peabody | https://www.nixonpeabody.com/insights/alerts/2026/05/13/a-loud-decision-on-tcpa-quiet-hours | 2026-05-13 | Quiet hours litigation | L |
| 34 | FCC seeks comments on petition to address TCPA quiet hours | Troutman Pepper Locke | https://www.troutman.com/insights/fcc-seeks-comments-on-petition-to-address-tcpa-quiet-hours/ | 2025 | Petition status | L |
| 35 | FCC set to adopt TCPA revocation reforms | Ecommerce Innovation Alliance | https://www.ecomm-alliance.org/blog/fcc-set-to-adopt-tcpa-revocation-reforms/ | 2026-09 | Industry view, quiet hours case counts | V |
| 36 | CAN-SPAM Act: a compliance guide for business | FTC | https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business | ongoing | CAN-SPAM requirements | O |
| 37 | İleti Yönetim Sistemi (İYS) | T.C. Ticaret Bakanlığı | https://ticaret.gov.tr/ic-ticaret/ticari-elektronik-iletiler/ileti-yonetim-sistemi-iys | ongoing | İYS obligations | O |
| 38 | Yönetmelikte değişiklik | İYS | https://iys.org.tr/iys/yonetmelik-degisiklik | ongoing | 3 business day rules, traders | O |
| 39 | KVKK Kurulu 2025/1072 sayılı ilke kararı | KVKK | https://www.kvkk.gov.tr/Icerik/8338/2025-1072 | 2025-06-10 | Separate consents, OTP | O |
| 40 | Elektronik ticaret kanunu idari para cezaları 2026 | Erdem and Erdem | https://www.erdem-erdem.av.tr/bilgi-bankasi/elektronik-ticaret-kanunu-kapsaminda-idari-para-cezalari-2026-yili-icin-guncellendi | 2025-12 | 2026 fine bands | L |
| 41 | Click to cancel just got cancelled | Cooley | https://www.cooley.com/news/insight/2025/2025-07-11-click-to-cancel-just-got-cancelled-eighth-circuit-vacates-entirety-of-ftcs-negative-option-rule | 2025-07-11 | Eighth Circuit vacatur | L |
| 42 | FTC seeks public comment on ANPRM regarding negative option marketing | FTC | https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-seeks-public-comment-response-advance-notice-proposed-rulemaking-regarding-negative-option | 2026-03 | Rulemaking restart | O |
| 43 | California Automatic Renewal Law amendments take effect July 1, 2025 | Cooley | https://www.cooley.com/news/insight/2025/2025-06-04-california-automatic-renewal-law-amendments-take-effect-on-july-1-2025 | 2025-06-04 | ARL rules | L |
| 44 | Final rule banning fake reviews and testimonials | FTC | https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials | 2024-08-14 | Review incentives and suppression | O |

## SMS, RCS, WhatsApp

| # | Title | Publisher | URL | Date | Supports | Type |
|---|-------|-----------|-----|------|----------|------|
| 45 | Verizon A2P SMS and RCS fees increase October 2026 | Telgorithm | https://www.telgorithm.com/news/verizon-announces-another-a2p-sms-fee-increase-effective-october-1-2026 | 2026 | Verizon fees | V |
| 46 | T-Mobile increases A2P 10DLC pass-through fees for 2026 | Telgorithm | https://www.telgorithm.com/news/t-mobile-announces-new-2026-a2p-sms-pass-through-fees | 2026-01 | T-Mobile fees | V |
| 47 | AT&T A2P SMS and MMS pass-through fee increases (April 2026) | Telgorithm | https://www.telgorithm.com/news/at-t-announces-new-a2p-sms-mms-pass-through-fee-increases-effective-april-1-2026 | 2026 | AT&T fees | V |
| 48 | Toll-free verification is changing in 2026 | Telgorithm | https://www.telgorithm.com/news/toll-free-verification-is-changing-in-2026-heres-what-you-need-to-know | 2025-12 | New fields | V |
| 49 | Toll-free verification | Telnyx | https://developers.telnyx.com/docs/messaging/toll-free-verification | 2026 | Enforcement date 2026-02-17 at Telnyx | O |
| 50 | Carrier fee updates | Tychron | https://www.tychron.com/company/carrier-fee-updates/ | 2026 | November 2026 surcharges | V |
| 51 | iOS 26 Screen Unknown Senders: a measured look | Postscript | https://postscript.io/blog/ios-26-screen-unknown-senders-a-measured-look-at-the-real-impact-on-sms | 2025 to 2026 | Impact contested | V |
| 52 | What iOS 26 means for SMS | Braze | https://www.braze.com/resources/articles/ios-26-sms-mms-rcs | 2025 | Feature mechanics | V |
| 53 | Understand iOS 26 update | Omnisend | https://support.omnisend.com/en/articles/12299862-understand-ios-26-update | 2025 | Default on in Brazil, China, India | V |
| 54 | Pricing on the WhatsApp Business Platform | Meta | https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing | 2026 | Per message pricing | O |
| 55 | Upcoming pricing updates for Meta Business Agent, service and utility messages | Meta | https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages | 2026 | 2026-10-01 changes, 1,000 free service messages | O |
| 56 | WhatsApp marketing: the complete 2026 guide | Braze | https://www.braze.com/resources/articles/whatsapp-marketing | 2026-07 | US marketing pause still in place | V |
| 57 | WhatsApp API message pricing update effective October 1, 2026 | YCloud | https://www.ycloud.com/blog/whatsapp-api-message-pricing-update-effective-october-1-2026 | 2026 | Country rate changes | V |
| 58 | WhatsApp changes its terms to bar general-purpose chatbots | TechCrunch | https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform | 2025-10-18 | AI chatbot policy | N |
| 59 | Brazil orders Meta to suspend policy banning third-party AI chatbots | TechCrunch | https://techcrunch.com/2026/01/13/brazil-orders-meta-to-suspend-policy-banning-third-party-ai-chatbots-from-whatsapp | 2026-01-13 | Brazil carve out | N |
| 60 | Not all chatbots are banned | respond.io | https://respond.io/blog/whatsapp-general-purpose-chatbots-ban | 2026 | Allowed bot types | V |
| 61 | What is WhatsApp frequency capping | Infobip | https://www.infobip.com/blog/what-is-whatsapp-frequency-capping | 2025 | Per user marketing limits | V |
| 62 | RCS Business Messaging | Klaviyo | https://www.klaviyo.com/products/sms-marketing/rcs | 2026 | RCS markets | O |
| 63 | Attentive launches Visibility AI for RCS | Attentive | https://www.attentive.com/press-releases/attentive-launches-visibility-ai-to-improve-deliverability-and-revenue-performance-for-rcs-for-business | 2026-05-20 | RCS features and claimed lifts | O |

## ESPs, AI and MCP

| # | Title | Publisher | URL | Date | Supports | Type |
|---|-------|-----------|-----|------|----------|------|
| 64 | Klaviyo expands AI agents (Composer) | Klaviyo | https://www.klaviyo.com/newsroom/composer | 2026-03 | Composer launch | O |
| 65 | Klaviyo launches AI agents that work together | Klaviyo / Business Wire | https://www.businesswire.com/news/home/20260630493754/en/Klaviyo-Launches-AI-Agents-that-Work-Together-to-Drive-Revenue-for-Consumer-Brands | 2026-06-30 | Composer beta, Customer Agent, MCP with Claude | O |
| 66 | K:BOS 2026 demonstrates Klaviyo's flywheel | Info-Tech | https://www.infotech.com/software-reviews/vendor-technology-notes/k-bos-2026-demonstrates-klaviyo-s-marketing-service-flywheel-for-autonomous-b2c-crm | 2026-09 | SQL via Composer and MCP, 260+ MCP tools | V |
| 67 | Klaviyo MCP server | Klaviyo Developers | https://developers.klaviyo.com/en/docs/klaviyo_mcp_server | 2026 | Remote MCP endpoint, roles, core tools | O |
| 68 | Klaviyo OpenAPI specification (revision 2026-07-15) | Klaviyo (GitHub) | https://github.com/klaviyo/openapi | 2026-07-15 | Endpoints, rate limits, scopes, report statistics | O |
| 69 | klaviyo-api-python CHANGELOG | Klaviyo (GitHub) | https://github.com/klaviyo/klaviyo-api-python | 2026-07-15 | API revisions 2025 to 2026 | O |
| 70 | Understanding Klaviyo's predictive analytics | Klaviyo Help | https://help.klaviyo.com/hc/en-us/articles/360020919731 | ongoing | CLV requirements | O |
| 71 | Analyze signup form performance | Klaviyo Help | https://help.klaviyo.com/hc/en-us/articles/360015960712 | ongoing | Submit rate definition | O |
| 72 | Introducing Klaviyo WhatsApp | Klaviyo | https://www.klaviyo.com/blog/klaviyo-whatsapp-product-launch | 2025 | WhatsApp launch | O |
| 73 | Klaviyo pricing 2026 | Kanal | https://getkanal.com/blog/klaviyo-pricing | 2026-10 | Plan pricing, credits | V |
| 74 | Braze accelerates AI innovation (Forge 2026) | Braze | https://www.braze.com/press-releases/braze-accelerates-ai-innovation-empowering-marketers-to-treat-every-customer-like-their-only-customer | 2026-09-29 | Decisioning Studio Go, Agentic Standards, MCP | O |
| 75 | Braze completes acquisition of OfferFit | Braze | https://www.braze.com/press-releases/braze-completes-acquisition-of-offerfit | 2025-06 | Decisioning Studio origin | O |
| 76 | Customer.io MCP: why we rebuilt it around one agent | Customer.io | https://customer.io/learn/how-we-work/customer-io-mcp-connector | 2026-05 | MCP v2 | O |
| 77 | Customer.io MCP get started | Customer.io Docs | https://docs.customer.io/ai/mcp/get-started/ | 2026 | MCP scope and permissions | O |
| 78 | Iterable unveils Nova Agent | Iterable / Business Wire | https://www.businesswire.com/news/home/20260422200702/en/Iterable-Unveils-Nova-Agent-and-a-New-Wave-of-AI-Innovations-to-Power-Real-Time-Personalization-and-Predictable-Growth | 2026-04-22 | Nova | O |
| 79 | Iterable MCP server | Iterable (GitHub) | https://github.com/Iterable/mcp-server | 2026 (v1.9.0) | Safe by default modes | O |
| 80 | Intuit Mailchimp launches Analytics AI | Intuit | https://investors.intuit.com/_assets/_6a9ee074199c0a511699c988d19108db/intuit/news/2026-05-28_Intuit_Mailchimp_Launches_Analytics_AI_and_1313.pdf | 2026-05-28 | Analytics AI, Claude integration | O |
| 81 | What's new July 2026 | Omnisend | https://support.omnisend.com/en/articles/15700809-what-s-new-july-2026 | 2026-07 | MCP write actions | O |
| 82 | Attentive unveils agentic AI at Thread 2026 | Business Wire | https://www.businesswire.com/news/home/20260526090213/en/Attentive-Unveils-Next-Generation-of-Agentic-AI-Marketing-Innovation-at-Thread-2026 | 2026-05-26 | Brand Voice 2.0, Reporting Agent | O |
| 83 | Q2 2026 what's new | Postscript | https://help.postscript.io/en/articles/14855933-q2-2026-what-s-new | 2026 | Shopper, Infinity Testing | O |
| 84 | With HubSpot Score retiring | Six and Flow | https://www.sixandflow.com/marketing-blog/with-hubspot-score-retiring-where-is-lead-scoring-in-hubspot | 2025 | Legacy score retirement | V |
| 85 | HubSpot AI in 2026 guide | SwyftRev | https://swyftrev.com/hubspot-ai-in-2026-the-complete-guide/ | 2026 | Remote MCP GA | V |

## Benchmarks, subscriptions, loyalty, paid media

| # | Title | Publisher | URL | Date | Supports | Type |
|---|-------|-----------|-----|------|----------|------|
| 86 | 2026 email marketing benchmarks by industry | Klaviyo | https://www.klaviyo.com/products/email-marketing/benchmarks | 2026 | Industry benchmarks | S |
| 87 | Email marketing benchmarks 2026 (UK) | Klaviyo | https://www.klaviyo.com/uk/blog/email-marketing-benchmarks-open-click-and-conversion-rates | 2026 | Placed order rates by industry | S |
| 88 | Omnisend 2026 ecommerce marketing report | Omnisend | https://www.omnisend.com/resources/reports/2026-ecommerce-marketing-report/ | 2026 | Automation share, flow conversion, SMS | S |
| 89 | SMS marketing benchmarks 2026 | Omnisend | https://www.omnisend.com/blog/sms-marketing-benchmarks/ | 2026 | SMS campaign vs automation | S |
| 90 | Recharge welcomes Skio | Recharge | https://getrecharge.com/blog/recharge-welcomes-skio-to-build-the-future-of-subscription-commerce/ | 2026-04-30 | Acquisition | O |
| 91 | Skio is now part of Recharge | Skio | https://skio.com/blog/skio-is-now-part-of-recharge | 2026-04 | Acquisition, 71% share claim | O |
| 92 | LoyaltyLion launches AI Campaigns | LoyaltyLion via Yahoo Finance | https://uk.finance.yahoo.com/news/loyaltylion-launches-ai-campaigns-help-120000661.html | 2026-01 | AI Campaigns | O |
| 93 | Product updates | LoyaltyLion | https://loyaltylion.com/platform/product-updates | 2026 | Order count tiers | O |
| 94 | Smile News Center | Smile.io | https://news.smile.io/ | 2026 | Sidekick, Loyalty Hub | O |
| 95 | Google to disable Customer Match uploads in Ads API | Search Engine Land | https://searchengineland.com/google-to-disable-customer-match-uploads-in-ads-api-470796 | 2026 | 2026-04-01 change | N |
| 96 | Manage customer lists | Google Ads API docs | https://developers.google.com/google-ads/api/docs/remarketing/audience-segments/customer-match/manage | 2026 | Data Manager API requirement scope | O |
| 97 | Restrictions on customer list custom audiences | Jon Loomer Digital | https://www.jonloomer.com/restrictions-on-customer-list-custom-audiences/ | 2025 | Meta restrictions | V |
| 98 | Meta exclusion-only audiences | Common Thread Collective | https://commonthreadco.com/blogs/coachs-corner/meta-exclusion-only-audiences-ecommerce-2026 | 2026-08 | Exclusion only audiences 2026-08-10 | V |
| 99 | Repeat purchase rate benchmarks: 18.8% across 156K customers | BS and Co | https://bsandco.us/blog-post/repeat-purchase-rate-benchmarks | 2026 | Repeat and time to second order | V |
| 100 | Average time to second purchase by vertical 2026 | eightx | https://eightx.co/blog/average-ecommerce-time-to-second-purchase-by-vertical-2026 | 2026 | Vertical medians | V |
| 101 | PyMC-Marketing CLV models | PyMC Labs | https://www.pymc-marketing.io/ | ongoing | BG/NBD and Gamma-Gamma | O |

## Reliability notes

- Strongest: regulator and official vendor documentation (1, 2, 9, 11, 14, 15, 19, 20, 23, 25, 36 to 39, 42, 44, 54, 55, 67 to 71, 74, 79).
- Benchmarks from vendors (86 to 89, 99, 100) describe their own customer bases; use for direction only.
- Items reported only by aggregator blogs (Yotpo pricing and acquisition rumors, Italy pixel deadlines, toll-free URL rule from 2026-09-15, DMARCbis RFC numbers) are marked [Unverified] in the references.
