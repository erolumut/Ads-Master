# Geo Market Modules

Country and region rules that change targets, budgets, tracking and creative. Tax, legal and privacy items are operational guidance for planning, not legal or tax advice: flag them for the client's accountant (in Turkey, a mali müşavir) or counsel before acting.

Verification legend for this module: items marked [Official] or [Study] with a date were checked against official or primary reporting; items marked [Unverified] could not be confirmed in the October 2026 research sweep and must be checked in the Freshness Protocol before use.

## 0. How to apply a geo module
1. For every market in PROJECT_BRIEF.md, run the checklist at the end of the relevant module.
2. Put tax and fee effects into the true media cost and into CAC (unit-economics-and-forecasting.md section 5).
3. Hand consent and tracking requirements to the measurement agent.
4. Hand claims, disclosure and restricted category rules to creative-strategy and the channel agents.
5. Log market specific findings in a journal entry and, once confirmed by data, in memory.

---

## 1. Turkey (Türkiye)

### 1.1 Snapshot for planners
| Topic | What matters | Planning effect |
|-------|-------------|-----------------|
| Currency and inflation | High inflation since 2021; annual CPI was 44.38% in December 2024 (TÜİK) and stayed high through 2025 and 2026 [Unverified current figure: read the latest TÜİK release] | Re-base CPA targets, budgets and benchmarks monthly; compare in real terms or hard currency |
| Taxes on ad spend | 15% withholding on payments to non-resident online ad providers; 20% VAT by reverse charge on foreign services; DST on platforms | True media cost is higher than the platform spend line |
| Payments | Credit card installments (taksit) are central to purchase decisions; card penetration is high | Show installment options in ads, feeds and pages; installment commissions reduce contribution margin |
| Marketplaces | Trendyol, Hepsiburada, Amazon.com.tr, n11, Çiçeksepeti, Pazarama and others capture a large share of ecommerce demand [Practitioner consensus] | Marketplace ads and pricing are part of the channel mix; brand search often happens inside marketplaces |
| Search | Google holds the dominant share of search; Yandex is a distant second [Practitioner consensus; check StatCounter] | Google Search and Shopping first for capture; Microsoft Ads is minor |
| Social and messaging | Instagram, YouTube, WhatsApp and TikTok have very high usage; X remains relevant for news [Practitioner consensus; check DataReportal Digital 2026 Turkey] | Meta, YouTube and TikTok for creation; click to WhatsApp for lead gen and service |
| Platform access risk | Access to platforms has been blocked or throttled at times (for example Instagram was blocked from 2 to 10 August 2024) [Practitioner consensus, widely reported] | Keep at least two creation channels live; have a contingency plan for sudden blocks |

### 1.2 Taxes and fees on advertising
| Item | Rule | Source and status |
|------|------|-------------------|
| Withholding (stopaj) on online advertising | 15% on payments for online advertising services to non-resident providers and their intermediaries; 0% when the provider is a Turkish resident company; payer withholds and files on the Muhtasar return | Presidential Decision No. 476 (December 2018), effective for payments from 1 January 2019; guidance in Communiqué No. 17 [Official, 2019; secondary summaries Thomson Reuters, law firm notes] |
| VAT reverse charge (KDV-2) | 20% VAT self assessed by the Turkish buyer on services bought from abroad; declared on KDV-2; deductible on the monthly KDV-1 for VAT registered businesses using the service for taxable activity | Turkish VAT law and rulings; practitioner guides 2025 to 2026 [Practitioner consensus; confirm with mali müşavir] |
| Gross-up | If the foreign provider will not accept a deduction, the base is grossed up: withholding base = invoice / 0.85. Example: TRY 9,600 invoice gives base TRY 11,294.12 and withholding TRY 1,694.12. Some advisors apply 20% KDV-2 on the invoice amount, others on the grossed up base | Practitioner guides disagree [Contested; confirm with mali müşavir] |
| Which entity bills you | Most Turkish Google Ads accounts are billed by Google Ireland; accounts that received an "Affected Products" notice contract with Google Türkiye, which charges Turkish VAT; resident entity invoices do not trigger the 15% withholding | Google Ads Help "Taxes in your country" and Turkish practitioner guides [Official page exists; details Unverified]: read the entity name on each invoice |
| Digital Services Tax (DST) | Rate cut from 7.5% to 5% from 1 January 2026, and to 2.5% from 1 January 2027; applies to large providers' Turkish revenue (thresholds: TRY 20 million Turkish revenue and EUR 750 million worldwide) | Presidential Decision No. 10767, Official Gazette 25 December 2025 [Official, 2025-12] |
| Platform pass through fees | Google has charged a "regulatory operating cost" fee on ads served in some DST countries including Turkey since 2020 | [Unverified current percentage after the 2026 DST cut]: check the Google Ads help page on regulatory operating costs and the invoice lines |

True media cost multiplier (planning default until the accountant confirms):
```
True cost of foreign billed media ~ platform spend x (1.15 to 1.1765) + non deductible VAT (if any) + regulatory fee (if billed)
Example: TRY 100,000 Meta spend, withholding grossed up: 100,000 / 0.85 = 117,647 -> true cost ~ TRY 117,647 (+17.6%), VAT deductible for a VAT registered company.
```
Use the true cost in CAC, MER and breakeven calculations. Platform ROAS overstates real return by the same factor.

### 1.3 Privacy and marketing consent
| Rule | What it requires | Effect on ads and tracking |
|------|------------------|----------------------------|
| KVKK (Law No. 6698) | Lawful basis, transparency notice (aydınlatma metni), data controller registration in VERBIS above thresholds | Privacy notice must cover ad pixels, CAPI and CRM uploads |
| KVKK amendment (Law No. 7499, Official Gazette 12 March 2024, in force 1 June 2024) | Cross border transfers move to an EU style regime: adequacy, appropriate safeguards such as standard contracts and binding corporate rules, limited incidental transfer exceptions; standard contracts must be notified to the Authority within 5 business days of signing | Sending personal data to Meta, Google, TikTok or OpenAI servers abroad (pixels, Conversions API, customer list uploads) needs a valid transfer mechanism. Work with counsel on standard contracts [Official, 2024; implementation details: confirm with counsel] |
| KVKK cookie guidance (2022) | Non essential cookies (analytics, advertising) need explicit consent; no pre ticked boxes; rejecting must be as easy as accepting | Run a CMP and wire Google Consent Mode and platform consent signals for Turkish traffic even though Google's EEA consent requirement does not cover Turkey [Official guidance, 2022; verify any update] |
| Commercial electronic messages (Law No. 6563 and its regulation) | Prior consent for marketing SMS, email and calls to consumers; consents must be registered in İYS (İleti Yönetim Sistemi); traders and craftsmen can be messaged on opt out basis | Email, SMS and WhatsApp marketing lists must be İYS synced; non registered consent means messages are blocked or fined [Official] |
| Advertising law (Consumer Protection Law No. 6502, Regulation on Commercial Advertising and Unfair Commercial Practices) | Truthful, substantiated claims; the Advertising Board (Reklam Kurulu) of the Ministry of Trade fines violations | Claims list in BRAND.md must hold up to Reklam Kurulu standards |
| Discount announcements | The pre discount price shown must be the lowest price applied in the last 30 days [Practitioner consensus; verify current regulation text] | Promo ads and feeds must use compliant reference prices |
| Influencer disclosure | Reklam Kurulu influencer guide (2021): commercial content must be clearly labeled (for example #reklam or #işbirliği) at the start | Creator contracts must require disclosure |
| Restricted categories | Alcohol and tobacco advertising banned; gambling only via state licensed operators; health claims and medicines restricted; crypto asset service ads require licensing under the 2024 capital markets amendment | Check before any campaign in these categories [Practitioner consensus; verify specifics] |
| Social media law (Law No. 7253, 2020) | Large foreign platforms must appoint local representatives; non compliance can trigger advertising bans for Turkish taxpayers and bandwidth throttling | Past ad bans affected some platforms in 2021 before they complied [Practitioner consensus]: check platform status before planning a new channel |
| Large marketplace rules (e-commerce law amendment Law No. 7416, 2022) | Large e-commerce intermediaries face licensing and limits, including on advertising budgets tied to transaction volume | Relevant if the client is a large marketplace [Unverified details: confirm with counsel] |

### 1.4 Payments and pricing
- Installments: advertise "peşin fiyatına taksit" (installments at cash price) or the maximum installment count when offered. Banking regulator BDDK limits installment counts by category and price [Unverified current limits: check BDDK rules before promising installments].
- Payment commissions: installment sales carry higher merchant commissions; include them in CM2.
- Cash on delivery (kapıda ödeme) still exists in some categories; it raises return and refusal rates; include refusal cost in contribution margin.
- Price display: TRY prices with VAT included for consumers; frequent price changes in inflation need daily feed updates (commerce-feeds) to avoid price mismatch disapprovals.

### 1.5 Marketplaces and retail media
| Marketplace | Notes for planning |
|-------------|--------------------|
| Trendyol | Largest Turkish marketplace by most accounts; Alibaba is the majority owner; offers on platform advertising and "Efsane" sale events [Practitioner consensus] |
| Hepsiburada | Major marketplace; Kaspi.kz acquired a controlling stake (announced 2024, completed 2025) [Practitioner consensus; verify]; on platform ads |
| Amazon.com.tr | Operating since 2018; Sponsored Products and Brands available |
| n11, Çiçeksepeti, Pazarama, PttAVM | Secondary; category specific relevance |
Rules: treat each marketplace as its own P&L (fees, ads, returns); protect brand terms inside marketplaces; watch price parity across marketplaces and your own site because shoppers compare in one search. Ecommerce volume figures are published yearly by the Ministry of Trade (eticaret.gov.tr); 2024 volume was reported around TRY 3 trillion [Unverified exact: check the latest report].

### 1.6 Search and language behavior
- Turkish characters (ı, ğ, ş, ç, ö, ü) are often typed without diacritics ("ayakkabi" for "ayakkabı"). Cover both in keywords, negatives and SEO titles.
- Turkish is agglutinative: one stem appears with many suffixes ("ayakkabı", "ayakkabılar", "ayakkabıları", "ayakkabısı"). Exact match lists explode; rely on phrase and broad match with good negatives and AI Max controls (google-ads agent).
- High intent modifiers: "fiyat", "fiyatları", "en ucuz", "indirim", "kampanya", "taksit", "yorum", "şikayet", "orijinal", "garanti". "Şikayet" queries surface Şikayetvar, a major complaint site that shapes trust (market-intel monitors it).
- Navigational marketplace queries ("trendyol <product>") are common: marketplace presence captures them.

### 1.7 Seasonality
| Period | Notes |
|--------|-------|
| Ramazan and Ramazan Bayramı, Kurban Bayramı | Dates move about 11 days earlier each year; gifting, travel and food peaks; consumption patterns shift to evenings during Ramazan |
| 11.11 and November "Efsane" or Black Friday events | Marketplace driven discount peaks; CPMs rise |
| Back to school (September), New Year gifts (December), Valentine's Day, Mother's Day (May) | Category peaks |
| Minimum wage updates (January, sometimes mid year) | Short term spending lift in mass categories [Practitioner consensus] |

### 1.8 Inflation playbook for bidding and budgets
1. Store targets in real terms: target CPA (real) x current CPI index / base index = this month's nominal target.
2. Prefer ROAS, POAS or MER targets (ratios) over CPA for ecommerce; they self adjust as AOV inflates.
3. Increase daily budgets monthly by the inflation rate just to stand still in real terms; label this "inflation maintenance", not "scaling".
4. Compare CPC and CPM year over year in USD or real TRY; nominal comparisons mislead.
5. If the ad account currency differs from the store currency, make sure conversion values are converted at current rates (measurement).

### 1.9 Turkey checklist
- [ ] True media cost multiplier agreed with the accountant and used in CAC.
- [ ] Invoice entity checked per platform (resident or non resident).
- [ ] KVKK notice covers pixels, CAPI, customer list uploads; transfer mechanism documented.
- [ ] CMP live with explicit consent for advertising cookies; consent signals passed to platforms.
- [ ] İYS registration and consent sync for SMS, email, WhatsApp marketing.
- [ ] Discount reference prices compliant; installment claims verified.
- [ ] Turkish keyword variants (with and without diacritics, suffixes) covered.
- [ ] Marketplace P&L and ads included in the channel mix.
- [ ] Monthly inflation re-basing scheduled in the monthly review.
- [ ] Contingency plan for platform access disruption.

---

## 2. European Union and United Kingdom

### 2.1 Rules that shape paid media
| Rule | Status (as of 2026-10) | Effect |
|------|------------------------|--------|
| GDPR and ePrivacy (cookie consent) | In force | Consent required for advertising cookies and most tracking; signal loss proportional to opt out rates |
| Google EU user consent policy and Consent Mode v2 | Required for EEA and UK traffic since March 2024 for personalization and remarketing [Official, 2024] | Without consent signals, audiences and conversion modeling degrade |
| Digital Markets Act (DMA) | Gatekeepers include Alphabet, Amazon, Apple, ByteDance, Meta, Microsoft and Booking | Cross service data combination needs consent |
| Meta less personalized ads (LPA) | European Commission fined Meta EUR 200 million in April 2025 over "pay or consent"; Meta committed in December 2025 to a choice between full and less personalized ads; revised choice flows rolled out to EU users from January 2026; the Commission is monitoring uptake [Official, 2025-12; Meta SEC filings 2026] | Part of the EU Meta audience receives less personalized ads; expect weaker targeting and attribution for that share; lean on creative and first-party data |
| Digital Services Act (DSA) | Applies to all platforms since 17 February 2024; very large platforms since August 2023 | Ad transparency per ad, no ads based on profiling with special category data, no profiling based ads to minors, public ad repositories (used by market-intel) |
| Political advertising regulation (TTPA, Regulation (EU) 2024/900) | Applied from 10 October 2025. Meta stopped political, electoral and social issue ads in the EU from 6 October 2025; Google stopped serving political ads in the EU [Official announcements 2024-11 and 2025-07] | Advocacy, NGO and issue adjacent ads can be blocked on Meta and Google in the EU; plan other channels |
| EU AI Act transparency obligations (Article 50) | Scheduled to apply from 2 August 2026; simplification proposals in late 2025 may change timing [Unverified: check status] | Disclose AI generated or manipulated content (deepfakes) in ads where required |
| European Accessibility Act | Applies since 28 June 2025 to many consumer ecommerce sites and apps (micro enterprises exempt for services) | cro must check accessibility of landing pages and checkout |
| Omnibus Directive price reduction rule | Prior price in a discount claim = lowest price in the previous 30 days | Promo ads and feeds |
| VAT on B2B ad purchases | Reverse charge for cross border B2B services within the EU | Billing profile must hold a valid VAT ID |
| Digital services taxes | Several countries tax large platforms (for example France, Italy, Spain, Austria, UK); Google charges regulatory operating cost fees in some of them [Unverified current rates] | Check invoice lines; include fees in true media cost |

### 2.2 United Kingdom specifics
| Rule | Status | Effect |
|------|--------|--------|
| UK GDPR and PECR | In force | Cookie consent model similar to the EU |
| Data (Use and Access) Act 2025 | Royal Assent June 2025; provisions commence in stages; includes exemptions from consent for some low risk cookies such as certain analytics, and raises PECR fines toward UK GDPR levels [Unverified commencement dates] | Analytics consent may relax; advertising cookies still need consent |
| DMCC Act 2024 | CMA direct consumer enforcement from April 2025 with fines up to 10% of global turnover; fake reviews and drip pricing rules [Official, 2025] | Reviews and price claims in ads and on pages must be clean |
| Less healthy food (HFSS) paid online advertising restrictions | Scheduled for January 2026 after delays [Unverified final status] | Food and drink advertisers check product scoring before UK campaigns |

### 2.3 EU and UK checklist
- [ ] CMP with Consent Mode v2 (advanced mode where appropriate) and platform consent signals.
- [ ] Server-side events with consent state for Meta CAPI, Google enhanced conversions, TikTok Events API.
- [ ] Expect modeled conversions: compare consented vs total traffic trends.
- [ ] No issue, political or advocacy ads on Meta or Google in the EU; route alternatives.
- [ ] No targeting on special category data, no profiling based ads to minors.
- [ ] Discount reference prices compliant (30 day lowest).
- [ ] Accessibility check on key pages (cro).
- [ ] AI generated content disclosure policy in BRAND.md.

---

## 3. United States

### 3.1 Privacy patchwork
| Item | Status (as of 2026-10) | Effect |
|------|------------------------|--------|
| Comprehensive state privacy laws | About 20 states, including California (CCPA as amended by CPRA), Virginia, Colorado, Connecticut, Utah, Texas, Oregon, Montana, Iowa, Delaware, Nebraska, New Hampshire, New Jersey, Tennessee, Minnesota, Maryland, Indiana, Kentucky and Rhode Island; the last three took effect 1 January 2026 [Practitioner consensus; check the IAPP tracker] | Opt out rights for targeted advertising and "sale" or "sharing" of data |
| Universal opt out signals (Global Privacy Control) | Must be honored in a growing number of states [Practitioner consensus] | Tag managers and CMPs must read GPC and suppress advertising tags or flag events |
| Maryland Online Data Privacy Act | Effective October 2025; strict data minimization; bans sale of sensitive data; limits targeted ads to minors [Practitioner consensus] | Extra care in health, finance and youth categories |
| Washington My Health My Data Act | In force since 2024; broad "consumer health data"; private right of action | Health related advertisers: avoid pixels on health pages without valid consent |
| California regulations on automated decision making and risk assessments | Finalized 2025 with phased obligations from 2026 [Unverified exact dates] | Risk assessments for targeted advertising processing |
| Pixel litigation (wiretap and video privacy claims) | Ongoing class action wave against pixels, session replay and chat widgets [Practitioner consensus] | Review tags on sensitive and video pages with counsel; server-side with consent where possible |
| FTC rules | Fake reviews and testimonials rule in effect since October 2024; Health Breach Notification Rule covers health apps; the "click to cancel" negative option rule was vacated by a federal appeals court in July 2025 [Practitioner consensus] | No fake reviews in ads; health apps must not leak data to ad platforms |

### 3.2 Market facts for planning
- The US is the first market for most new ad products (ChatGPT ads self serve beta May 2026; ads in Google AI Mode formats announced May 2026; OpenAI visual ads alongside image generation announced October 2026 for the US first) [Study and news reports 2026; see sources].
- IAB revised its 2026 US ad spend growth forecast to 12.3% in September 2026, with social at 16.5%, CTV 15.6%, commerce media 13.6% and paid search 8.1% [Study, 2026-09].
- Sales tax does not apply to most ad purchases; Maryland taxes large platforms' digital ad revenue (platforms may pass through costs) [Unverified pass through status].

### 3.3 US checklist
- [ ] GPC honored; opt out of targeted advertising wired to tags and CAPI.
- [ ] Sensitive pages (health, finance, children) audited for pixels.
- [ ] State specific consent for sensitive data where required.
- [ ] Reviews and testimonials in ads verifiable and compliant.

---

## 4. MENA and GCC

### 4.1 Snapshot
| Topic | What matters |
|-------|-------------|
| Platforms | Snapchat and TikTok are especially strong in Saudi Arabia and the Gulf; Instagram, YouTube and WhatsApp are near universal; X stays relevant in Saudi Arabia [Practitioner consensus; verify with platform reach tools] |
| Search | Google dominant |
| Language | Arabic (Gulf dialect often beats Modern Standard Arabic in social creative) plus English (UAE expat majority); right to left layouts; Hijri dates |
| Currency | SAR and AED are pegged to USD (stable budgets); Egypt's pound has been volatile, so re-base targets as in Turkey |
| Payments | Cards and Apple Pay high in the Gulf; mada debit network in Saudi Arabia; BNPL (Tabby, Tamara) widely used; cash on delivery persists in some categories and markets |
| Weekends | Saudi Arabia Friday to Saturday; UAE Saturday to Sunday (since 2022), which shifts dayparting |
| AI assistant ads | ChatGPT ads self serve opened to MENA markets on 31 August 2026 per reports [Unverified secondary] (chatgpt-ads agent verifies eligibility) |

### 4.2 Regulation
| Market | Rule | Effect |
|--------|------|--------|
| Saudi Arabia | Personal Data Protection Law (PDPL), in force September 2023 with enforcement from September 2024; regulator SDAIA; transfer rules | Consent and notices for tracking and marketing; cross border transfer review [Practitioner consensus] |
| Saudi Arabia | Influencer advertising requires a media license (commonly called Mawthooq) [Practitioner consensus; verify current regulator] | Creator campaigns need licensed creators |
| UAE | Federal PDPL (Decree-Law No. 45 of 2021); DIFC and ADGM have separate regimes | Consent and notices; check free zone status |
| UAE | Media law updates require permits for advertising content creators [Unverified dates and scope] | Creator campaigns need permitted creators |
| Qatar, Bahrain, Oman, Kuwait, Egypt | National data protection laws with consent requirements [Practitioner consensus] | Local notices and consent |
| Region wide | Alcohol (banned or restricted), gambling (banned), dating and some health products restricted; cultural and religious sensitivities in imagery | Creative and category review before launch |

### 4.3 Seasonality
| Period | Notes |
|--------|-------|
| Ramadan | Biggest season; media consumption and shopping shift to evenings and late night; CPMs rise; plan creative and budgets 6 to 8 weeks ahead |
| Eid al-Fitr, Eid al-Adha | Gifting, fashion, travel peaks |
| White Friday (November), 11.11 | Major ecommerce sales (Noon, Amazon) |
| Saudi National Day (23 September), Founding Day (22 February), UAE National Day (2 December) | Patriotic campaigns and promotions |
| Summer | Travel out of the region; demand dips for local services |

### 4.4 MENA checklist
- [ ] Arabic and English creative per segment; RTL landing pages tested.
- [ ] BNPL and local payment methods shown in ads and checkout.
- [ ] Ramadan plan (seasonal workflow) 8 weeks ahead.
- [ ] Creator licensing verified for Saudi Arabia and UAE.
- [ ] Consent and notices per national data protection law.

---

## 5. Other markets: quick facts to verify
| Market | Notable facts |
|--------|---------------|
| Brazil | LGPD privacy law; WhatsApp central; Pix instant payments; installments (parcelamento); Mercado Livre retail media |
| India | Digital Personal Data Protection Act 2023 with rules phasing in [Unverified dates]; UPI payments; very price sensitive CPMs; ChatGPT ads self serve opened to India in August 2026 per reports [Unverified] |
| Japan | APPI privacy law; LINE Yahoo ecosystem; Rakuten and Amazon marketplaces |
| South Korea | PIPA; Naver and Kakao ecosystems; Coupang retail media |
| China | Separate ecosystem (Baidu, WeChat, Douyin, Tmall); out of scope for this system |
