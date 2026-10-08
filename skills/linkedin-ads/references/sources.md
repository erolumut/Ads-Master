# Sources (annotated)

> Research method note (updated 2026-10-08): the first build had no live search. A verification pass on 2026-10-08 ran 57 web searches (extended mode for 2025 to 2026 items) over LinkedIn Help Center pages, the Marketing API changelog on Microsoft Learn, LinkedIn product pages, trade press, dated benchmark studies, B2B Institute and Forrester material, practitioner sources and GitHub. Direct fetching of linkedin.com and learn.microsoft.com was blocked, so official facts were confirmed through search extracts of those pages and dated trade coverage. Numbers in brackets refer to the numbered source list in `research/linkedin-ads.md`. Status column: Verified (confirmed in the 2026-10-08 pass), Known (stable official source, not re-checked for a specific claim), Contested (sources disagree), Verify (still open).

## Official LinkedIn sources

| # | Title | Publisher | URL | Date | Supports | Status |
|---|-------|-----------|-----|------|----------|--------|
| 1 | LinkedIn Marketing Solutions (ads overview, Ads Guide, specs) | LinkedIn | https://business.linkedin.com/marketing-solutions | Rolling | Objectives, formats, specs | Known |
| 2 | LinkedIn Help Center, Marketing Solutions | LinkedIn | https://www.linkedin.com/help/lms | Rolling | Campaign Manager settings | Known |
| 3 | LinkedIn Marketing Blog | LinkedIn | https://www.linkedin.com/business/marketing/blog | Rolling | Product announcements | Known |
| 4 | LinkedIn Marketing API documentation | Microsoft Learn (LinkedIn) | https://learn.microsoft.com/en-us/linkedin/marketing/ | Rolling | API, versioning, adAnalytics, conversions, lead sync | Known |
| 5 | LinkedIn Advertising Policies | LinkedIn | https://www.linkedin.com/legal/ads-policy | Rolling | Prohibited and restricted content, political ads prohibition | Known |
| 6 | LinkedIn Ad Library | LinkedIn | https://www.linkedin.com/ad-library | Rolling | Competitor ad research, transparency | Known |
| 7 | Campaign Manager | LinkedIn | https://www.linkedin.com/campaignmanager | Rolling | UI names, forecast panel, reports | Known |
| 8 | LinkedIn B2B Institute | LinkedIn | https://business.linkedin.com/marketing-solutions/b2b-institute | 2019 to 2025 | 95 to 5 rule, Easy to Find | Known |
| 47 | Recent Marketing API Changes | Microsoft Learn | https://learn.microsoft.com/en-us/linkedin/marketing/integrations/recent-changes?view=li-lms-2026-09 | 2026-09 | MAX_QUALIFIED_LEAD (202602), event ads lead gen (202605), OPTIMIZED creative selection (2026-07), MQL and SQL types (202608), 202609 changes | Verified |
| 48 | Conversions FAQ | Microsoft Learn | https://learn.microsoft.com/en-us/linkedin/marketing/conversions/conversions-faq?view=li-lms-2026-09 | 2026-09 | CAPI identifiers, hashing, 180 and 365 day windows | Verified |
| 49 | Conversions API | Microsoft Learn | https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/conversions-api?view=li-lms-2026-08 | 2026-08 | Click ID mapping kept 365 days, windows | Verified |
| 50 | LMS API Documentation Versioning | Microsoft Learn | https://learn.microsoft.com/en-us/linkedin/marketing/versioning?view=li-lms-2026-05 | 2026-05 | Monthly versions, 202609 | Verified |
| 51 | Campaign Objectives | Microsoft Learn | https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/campaign-objectives?view=li-lms-2026-09 | 2026-09 | Objective list, 202510 sunset 2026-10-15 | Verified |
| 52 | Event Ads API | Microsoft Learn | https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/advertising-targeting/version/event-ads-integrations?view=li-lms-2026-05 | 2026-05 | Event ads lead gen, no Audience Network | Verified |
| 53 | Create and Manage LinkedIn Campaigns | Microsoft Learn | https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaigns?view=li-lms-2025-09 | 2025-09 | MAX_FREQUENCY for BRAND_AWARENESS | Verified |
| 54 | LinkedIn conversion window | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/a426359 | Rolling | 365 day lookback types, 90/90 recommendation, attribution models, 2025-04 event registration windows | Verified |
| 55 | Conversions API best practices | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/a5538676 | Rolling | Identifiers (email hash, click ID, Acxiom, MOAT) | Verified |
| 56 | Conversions API Playbook | LinkedIn (PDF) | https://business.linkedin.com/content/dam/me/business/en-us/marketing-solutions/resources/pdfs/Conversions-API-Playbook.pdf | Undated | Window recommendations by event type | Verified |
| 62 | Set a frequency cap for your ad set | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/a6573757 | Rolling | Frequency cap rules | Verified |
| 63 | Maximize your budget | LinkedIn | https://business.linkedin.com/advertise/ads/best-practices/maximize-your-budget | Rolling | $10 daily, $100 lifetime minimums, lifetime pacing | Verified |
| 64 | Campaign and ad set budgets | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/a422101 | Rolling | Daily overspend example (up to 50%) | Verified |
| 65 | Dynamic Group Budget best practices | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/a1502134 | Rolling | 1 to 50 ad sets, rules, suggested minimums | Verified |
| 75 | BrandLink | LinkedIn | https://business.linkedin.com/advertise/ads/sponsored-content/brandlink | Rolling | Beta status, sales routed | Verified |
| 87 | Thought Leader Ads (Help) | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/a1399568 | Rolling | Eligible posts, objectives by format | Verified |
| 88 | Thought Leader Ads (product page) | LinkedIn | https://business.linkedin.com/advertise/ads/sponsored-content/thought-leader-ads | Rolling | Brand awareness and Engagement | Verified |
| 100 | Lookalike audiences discontinued | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/94287 | 2024-02-29 | Lookalike retirement, replacements | Verified |
| 102 | Sponsored Messaging | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/71201 | Rolling | EEA and Swiss opt in rule | Verified |
| 103 | Conversation ads | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/104116 | Rolling | EU targeting since mid October 2024 | Verified |
| 108 | Revenue Attribution Report Overview | LinkedIn | https://business.linkedin.com/marketing-solutions/revenue-attribution-report | Rolling | CRMs, metrics | Verified |
| 109 | RAR getting started guide v01 | LinkedIn (PDF hosted by PPC Land) | https://ppc.land/content/files/2025/07/linkedin-business-manager-revenue-attribution-report-getting-started-guide-v01.pdf | 2025-07 | Model, 180 day default lookback | Verified; lookback Contested |
| 110 | Lead Gen Form fields | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/79852 | Rolling | 12 fields, 3 custom questions, work email validation | Verified |
| 111 | Lead Gen Form hidden fields | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/a421421/ | Rolling | Hidden field behavior | Verified |
| 112 | Carousel Ads specifications | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/88137 | Rolling | Carousel specs | Verified |
| 113 | Accelerate Getting Started Guide | LinkedIn (PDF) | https://business.linkedin.com/content/dam/lem/business/de/advertise/ads/linkedin-accelerate/Accelerate-Getting-Started-Guide.pdf | Undated | Accelerate limits | Contested |
| 122 | 95-5 Rule | LinkedIn B2B Institute | https://business.linkedin.com/advertise/resources/b2b-institute/b2b-research/trends/95-5-rule | Rolling | 95 to 5 rule | Verified |
| 125 | LinkedIn Audience Network (Help) | LinkedIn Help Center | https://www.linkedin.com/help/lms/answer/a420372 | Rolling | Default on for single image, carousel, document, video | Verified |

## Trade coverage of LinkedIn announcements (dated)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 57 | LinkedIn Launches Qualified Leads Optimization | Social Media Today | https://www.socialmediatoday.com/news/linkedin-qualified-leads-optimization-crm-targeting/746055/ | 2025-04 | QLO, 39% claim, 5 per two weeks |
| 58 | LinkedIn Introduces Qualified Leads Optimization | DestinationCRM | https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/LinkedIn-Introduces-Qualified-Leads-Optimization-169110.aspx | 2025-04-22 | Launch date |
| 59 | LinkedIn Renames Ad Campaign Elements | Social Media Today | https://www.socialmediatoday.com/news/linkedin-updates-advertising-campaign-naming-conventions/761534/ | 2025-09 | Campaign and Ad set rename |
| 60 | LinkedIn Campaign Manager Rename: Reporting Impact | Dataslayer | https://www.dataslayer.ai/blog/linkedin-campaign-manager-rename-2026 | 2026 | API unchanged, UTM tokens renamed |
| 61 | LinkedIn launches frequency capping for brand awareness campaigns | PPC Land | https://ppc.land/linkedin-launches-frequency-capping-for-brand-awareness-campaigns/ | 2025-07 | Frequency cap launch |
| 67 | LinkedIn introduces Reserved Ads, ad personalization, new AI tools | Search Engine Land | https://searchengineland.com/linkedin-rolls-out-tools-to-make-b2b-brand-advertising-more-predictable-466019 | About 2025-12 | Reserved Ads, personalization |
| 68 | LinkedIn launches First Impression Ads | AdNews | https://www.adnews.com.au/news/linkedin-launches-first-impression-ads | 2025-06-05 | First Impression and Reserved Ads |
| 69 | LinkedIn advertisers gain 20% higher CTR with 5-plus ad variants | PPC Land | https://ppc.land/linkedin-advertisers-gain-20-higher-ctr-with-5-plus-ad-variants/ | 2026-07-01 | AI creative tools |
| 70 | LinkedIn rolls out new AI-powered promotional tools | Social Media Today | https://www.socialmediatoday.com/news/linkedin-rolls-out-new-ai-powered-promotional-tools/824290/ | 2026-07 | AI creative tools |
| 71 | LinkedIn introduces significant updates to Campaign Manager | PPC Land | https://ppc.land/linkedin-introduces-significant-updates-to-campaign-manager/ | 2025-03-25 | Media Planner |
| 72 | LinkedIn overhauls event ads | PPC Land | https://ppc.land/linkedin-overhauls-event-ads-with-off-platform-targeting-and-lead-gen-forms/ | 2026-04-28 | Off-platform event ads |
| 73 | LinkedIn launches Creator Marketplace and BrandWorks | PPC Land | https://ppc.land/linkedin-launches-creator-marketplace-and-brandworks-for-b2b-brands/ | 2026-06-10 | Creator Marketplace |
| 74 | LinkedIn expands BrandLink Programme and CTV advertising | Social Samosa | https://www.socialsamosa.com/news-2/linkedin-expands-brandlink-programme-ctv-advertising-11248078 | 2026-03 | BrandLink self serve, Trade Desk CTV |
| 76 | LinkedIn expands BrandLink, offers video ads with top creators | eCommerceNews | https://ecommercenews.com.au/story/linkedin-expands-brandlink-offers-video-ads-with-top-creators | 2025-05 | Wire renamed BrandLink |
| 77 | LinkedIn CTV ads at its Marketing Summit | Marketing Brew | https://marketingbrew.com/stories/2024/04/03/linkedin-ctv-ads-marketing-summit | 2024-04-03 | CTV launch |
| 78 | LinkedIn partners with Paramount | StreamTV Insider | https://www.streamtvinsider.com/advertising/linkedin-partners-paramount-levels-emerging-ctv-ad-game | 2025-06-04 | CTV Select |
| 79 | LinkedIn CTV Ads available through Amazon DSP | Amazon Ads | https://advertising.amazon.com/library/news/linkedin-ctv-ads-amazon-dsp | 2026-05 | Amazon DSP route |
| 80 | LinkedIn Profile Targeting Expands to CTV in Microsoft Ads (clarified) | PPC Newsfeed | https://ppcnewsfeed.com/ppc-news/2026-05/linkedin-profile-targeting-expands-ctv-microsoft-ads/ | 2026-05 | Not available in Microsoft CTV |
| 81 | Microsoft Monetize fuses LinkedIn profile data into CTV | PPC Land | https://ppc.land/microsoft-monetize-fuses-linkedin-profile-data-into-ctv-via-three-dsps/ | 2026-05 | Monetize context |
| 82 | DoubleVerify global measurement for LinkedIn Audience Network | GlobeNewswire | https://www.globenewswire.com/news-release/2026/05/21/3299391/0/en/doubleverify-delivers-global-media-quality-measurement-for-linkedin-audience-network-elevating-transparency-for-b2b-advertisers.html | 2026-05-21 | Post-bid verification |
| 83 | LinkedIn Product Updates: September 2026 Recap | Influent | https://influent.co/blog/linkedin-updates-september-2026 | 2026-09 | Booked appointments, brand safety warnings, In-Stream alpha |
| 84 | Book meetings from LinkedIn Lead Gen Forms | Chili Piper Help | https://help.chilipiper.com/hc/en-us/articles/52302755601683-How-do-I-book-meetings-from-LinkedIn-Lead-Gen-Forms | 2026 | Booking setup |
| 85 | LinkedIn offers tips on company targeting | Social Media Today | https://www.socialmediatoday.com/news/linkedin-offers-tips-on-company-targeting-via-campaign-manager/830615/ | 2026-09-16 | Companies view guidance |
| 86 | LinkedIn's new Companies Hub | CMSWire | https://www.cmswire.com/the-wire/measure-engagement-and-reach-buyers-with-insights-from-linkedins-new-companies-hub | 2024 | Companies tab |
| 89 | LinkedIn expands Thought Leader Ads | PPC Land | https://ppc.land/thought-leader-ads | 2024-03 | Any member posts |
| 104 | LinkedIn to limit targeted ads in EU | TechCrunch | https://techcrunch.com/2024/06/07/linkedin-to-limit-targeted-ads-in-eu-after-complaint-over-sensitive-data-use | 2024-06-07 | EU Group targeting |
| 105 | LinkedIn restricts ad targeting after our complaint | Bits of Freedom | https://www.bitsoffreedom.nl/en/2024/06/27/linkedin-restricts-ad-targeting-after-our-complaint/ | 2024-06-27 | Complaint detail |
| 106 | LinkedIn updates terms for AI and ad targeting | HR Dive | https://hrdive.com/news/linkedin-updates-terms-of-service-ai-ad-targeting-microsoft/760614 | 2025-09 | 2025-11-03 terms |
| 107 | LinkedIn to tighten data rules, expand Microsoft ad sharing | Digital Information World | https://www.digitalinformationworld.com/2025/09/linkedin-to-tighten-data-rules-expand.html | 2025-09 | Regions excluded |
| 114 | LinkedIn unveils Live Event Ads and Accelerate | Swipe Insight | https://web.swipeinsight.app/posts/linkedin-unveils-live-event-ads-and-accelerate-campaigns-for-b2b-marketing-11753 | 2024-10-15 | Accelerate all objectives, 42% claim |
| 124 | LinkedIn hits 1.2 billion members | IANS | https://ianslive.in/linkedin-hits-12-billion-members-microsoft-ceo-satya-nadella-highlights-ai-driven-growth-across-platforms--20251022105445 | 2025-10-22 | Member count |
| 133 | Innovid expands integration with LinkedIn CTV | Business Wire | https://secure.businesswire.com/news/home/20250721295367/en/Innovid-Expands-Integration-with-LinkedIn-to-Support-CTV-Ads | 2025-07-21 | CTV activation |
| 134 | LinkedIn now supports Dynamic UTMs | PPC Land | https://ppc.land/linkedin-now-supports-dynamic-utms/ | 2024-03 | Dynamic UTMs |
| 135 | LinkedIn launches Wire program | Lindsey Gamble | https://www.lindseygamble.com/blog/linkedin-launches-wire-program-for-in-stream-video-ads-on-publisher-content | 2024-06 | Wire beta |

## Official LinkedIn developer repositories (verified on GitHub, 2026-10-08)

| # | Repository | URL | Created | Supports | Status |
|---|-----------|-----|---------|----------|--------|
| 21 | linkedin-api-python-client | https://github.com/linkedin-developers/linkedin-api-python-client | 2023-01-12 | Official Python client | Verified |
| 22 | linkedin-api-js-client | https://github.com/linkedin-developers/linkedin-api-js-client | 2022-12-28 | JavaScript client | Verified |
| 23 | linkedin-capi-tag-template | https://github.com/linkedin-developers/linkedin-capi-tag-template | 2023-08-30 | Official GTM server template for CAPI | Verified |
| 24 | reactor-extension-linkedin-edge | https://github.com/linkedin-developers/reactor-extension-linkedin-edge | 2026-06-24 | Adobe event forwarding of conversions to LinkedIn | Verified |
| 25 | java-sample-application | https://github.com/linkedin-developers/java-sample-application | 2021-10-08 | API samples | Verified |

## Research, studies and benchmarks

| # | Title | Publisher | URL | Date | Supports | Status |
|---|-------|-----------|-----|------|----------|--------|
| 9 | Advertising effectiveness and the 95-5 rule (John Dawes) | Ehrenberg-Bass for the B2B Institute | Via 8 and 122 | 2021 | 95 to 5 rule | Verified |
| 10 | The 5 Principles of Growth in B2B Marketing (Binet, Field) | LinkedIn B2B Institute | https://business.linkedin.com/advertise/resources/b2b-institute/marketing-as-growth | 2019 | Brand and activation balance | Verified |
| 121 | Easy to Find: owned prominence (B2B Institute) | PPC Land coverage | https://ppc.land/why-linkedin-says-building-owned-prominence-beats-rented-ads-in-b2b-marketing/ | 2025-12 | Presence, prominence, portfolio | Verified |
| 123 | State of Business Buying 2024 release | Forrester via Stock Titan | https://www.stocktitan.net/news/FORR/forrester-to-master-b2b-buying-mayhem-providers-must-prioritize-biyipkl01ko0.html | 2024-12 | 13 people per buying decision | Verified |
| 95 | LinkedIn Ads 2026 Benchmarks Report | Dreamdata | https://dreamdata.io/blog/announcing-linkedin-ads-benchmarks-report-2026 | 2026 (data 2024-08 to 2025-07) | CTR, CPC, CPM, ROAS, journey length | Verified |
| 96 | LinkedIn Ads Benchmarks Report 2025 highlights | Dreamdata | https://dreamdata.io/blog/dreamdata-2025-linkedin-ads-benchmarks-report-highlights | 2025 | Prior year comparisons | Verified |
| 90 | Thought Leader Ads Benchmarks 2026 | Kiin | https://kiin.co/research/linkedin-thought-leader-ads-benchmarks | 2026-09 | TLA CPM and landing page CTR | Verified |
| 91 | LinkedIn Ads Benchmarks 2026 | Kiin | https://kiin.co/linkedin-ads-benchmarks | 2026-09 | Format and region benchmarks | Verified |
| 92 | Lead Gen Forms Benchmarks 2026 | Kiin | https://kiin.co/research/linkedin-lead-gen-forms-benchmarks | 2026 | Form open, completion, CPL | Verified |
| 93 | CTV Ads benchmarks (31 accounts) | Kiin | https://kiin.co/research/linkedin-ctv-ads-benchmarks | 2026 | CTV CPM | Verified |
| 94 | Benchmarks for HR audiences (113 accounts) | Kiin | https://kiin.co/research/linkedin-ads-benchmarks/hr-audience | 2026 | Document ads lead gen | Verified |
| 97 | 2025 LinkedIn Ads Benchmark Report | HockeyStack | https://www.hockeystack.com/lab-blog-posts/linkedin-ads-benchmarks | 2025 | SaaS CTR, CPC | Verified |
| 98 | LinkedIn Ads Benchmarks 2026 | The Smarketers | https://thesmarketers.com/blogs/linkedin-ads-benchmarks-2026/ | 2026 | Regional CPM ranges | Verified |
| 99 | LinkedIn Ad Benchmarks | Metadata.io | https://metadata.io/resources/blog/linkedin-ad-benchmarks/ | 2021 data | Older CPL and CPM | Verified (old) |
| 101 | Predictive Audiences guide | Carnegie Higher Ed | https://www.carnegiehighered.com/linkedin-predictive-audiences-for-higher-ed/ | Undated | Seed rules, 30 audience cap | Verified (agency) |
| 137 | Predictive Audiences Getting Started Guide | LinkedIn (PDF) | https://business.linkedin.com/content/dam/me/business/en-us/marketing-solutions/resources/pdfs/predictive-audiences-getting-started-guide.pdf | Undated (2024) | 300 member source floor | Verified |
| 138 | LinkedIn DMP segment cap 1,000 | Digital Applied | https://www.digitalapplied.com/blog/linkedin-dmp-segment-cap-1000-audience-cleanup | 2026-08-18 | Segment cap per account (API 202608) | Verify |

## Practitioner and vendor sources

| # | Title | URL | Date | Supports |
|---|-------|-----|------|----------|
| 66 | How budgets work on LinkedIn Ads (B2Linked) | https://b2linked.com/blog-page/how-budgets-work-on-linkedin-ads | 2025-08 | 50% overspend, UTC reset |
| 126 | 5 pitfalls killing your LinkedIn ads performance (B2Linked) | https://b2linked.com/blog-page/5-pitfalls-that-are-killing-your-linkedin-ads-performance | 2026-05-20 | Audience expansion default |
| 130 | LinkedIn Ads Strategy for 2026: Q and A with AJ Wilcox | https://www.marketingprofs.com/articles/2026/55621/linkedIn-ads-tips-aj-wilcox | 2026-08 | AI imagery view |
| 116 | LinkedIn marketing strategy 2026 (Hootsuite) | https://blog.hootsuite.com/linkedin-marketing-strategy/ | 2026 | Accelerate objective history |
| 117 | LinkedIn Accelerate review (Optimize LinkedIn Ads) | https://www.optimizelinkedinads.com/blogs/linkedin-accelerate-review | 2026 | Accelerate quality concerns |
| 127 | Campaign Manager Tutorial 2026 (Kiin) | https://kiin.co/blog/linkedin-campaign-manager | 2026 | Companies tab, Accelerate fit |
| 129 | LinkedIn Insight Tag in GTM (Piotr Litwa) | https://piotrlitwa.com/articles/en/linkedin-insight-tag-gtm.html | 2026 | Consent gating |
| 131 | Advertising on LinkedIn in 2026 (Funnel) | https://funnel.io/blog/linkedin-advertising-2026 | 2026 | Video warmed members 1.6x |
| 132 | LinkedIn Ad Specs and Sizes 2026 (Kiin) | https://kiin.co/blog/linkedin-ad-specs | 2026 | Spec cross check |
| 128 | Releasebot LinkedIn release notes | https://releasebot.io/updates/linkedin | 2026-09 | Changelog alerts |

## Microsoft Advertising sources involving LinkedIn data

| # | Title | URL | Date | Supports |
|---|-------|-----|------|----------|
| 26 | Less busywork, more growth: What's new in Microsoft Advertising this September | https://about.ads.microsoft.com/en/blog/post/september-2026/less-busywork-more-growth-what-new-in-microsoft-advertising-this-september | 2026-09-30 | LinkedIn company lists up to 10,000; excludes EEA, UK, Swiss users |
| 27 | New Performance Max tools and other product updates for February | https://about.ads.microsoft.com/en/blog/post/february-2025/new-performance-max-tools-and-other-product-updates-for-february | 2025-02 | LinkedIn profile targeting as PMax signal pilot |
| 29 | Microsoft Advertising gains LinkedIn company lists of up to 10,000 firms | https://ppc.land/microsoft-advertising-gains-linkedin-company-lists-of-up-to-10-000-firms | 2026-09 | Coverage of the same change |

## MCP servers, AI connectors and tools (verified 2026-10-08)

| # | Item | URL | Created or date | Notes |
|---|------|-----|-----------------|-------|
| 118 | LinkedIn Ads app for ChatGPT (official, beta) | https://openai.com/business/plugins/linkedin-ads/ | 2026 | Read only ad set and ad performance |
| 119 | LinkedIn Ads MCP: No Official Server Yet | https://theadspend.com/blog/linkedin-ads-mcp | 2026-07 | Status check |
| 120 | PaidSync LinkedIn Ads MCP (status check 2026-09-27) | https://paidsync.ai/linkedin-ads-mcp | 2026-09 | Status check, vendor |
| 31 | danielpopamd/linkedin-ads-mcp | https://github.com/danielpopamd/linkedin-ads-mcp | 2026-01-20 | Community, write capable |
| 32 | amekala/ads-mcp | https://github.com/amekala/ads-mcp | 2025-10-27 | Multi platform |
| 33 | markifact/markifact-mcp | https://github.com/markifact/markifact-mcp | 2026-05-03 | Multi platform, approval gated writes |
| 34 | adkit/ads-mcp | https://github.com/adkit/ads-mcp | 2026-05-19 | Multi platform |
| 35 | stan-rym/liam-linkedin-ads-MCP | https://github.com/stan-rym/liam-linkedin-ads-MCP | 2026-06-14 | Campaign creation |
| 36 | Nuraveda/linkedin-ads-mcp | https://github.com/Nuraveda/linkedin-ads-mcp | 2026-05-29 | Python, MIT |
| 37 | DanielSylvester/linkedin-ads-mcp | https://github.com/DanielSylvester/linkedin-ads-mcp | 2026-05-25 | Community |
| 38 | proxy-intell/linkedin-ads-library-mcp | https://github.com/proxy-intell/linkedin-ads-library-mcp | 2026-08-05 | Ad Library research |
| 39 | CDataSoftware/linkedin-ads-mcp-server-by-cdata | https://github.com/CDataSoftware/linkedin-ads-mcp-server-by-cdata | 2025-06-23 | Read only |
| 40 | pipeworx-io/mcp-linkedin_ads | https://github.com/pipeworx-io/mcp-linkedin_ads | 2026-04-15 | Community pack |
| 41 | Synter-Media-AI/mcp-server | https://github.com/Synter-Media-AI/mcp-server | 2026-01-29 | Multi platform |
| 42 | PaidSync/paidsync-mcp | https://github.com/PaidSync/paidsync-mcp | 2026-05-11 | Hosted multi platform |
| 43 | opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms | https://github.com/opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms | 2026-07-10 | Hosted, approval gates |
| 44 | jshorwitz/awesome-agentic-advertising | https://github.com/jshorwitz/awesome-agentic-advertising | 2026-02-07 | Directory |
| 45 | Dataslayer-AI/Marketing-skills | https://github.com/Dataslayer-AI/Marketing-skills | 2026-03-19 | Skills plus connector MCP |

## Sources by module
| Module | Main sources | Claims still open |
|--------|-------------|-------------------|
| Account structure | 47, 51, 57, 59, 65, 71, 113, 114 | Accelerate limits, Talent leads status |
| Targeting and ABM | 85, 86, 100, 101, 102, 103, 104, 106, 125, 126, 137 | Predictive audience cap, DMP segment cap, website retargeting max lookback |
| Formats and creative | 67, 68, 69, 73, 74, 75, 76, 77, 78, 79, 87, 88, 89, 90, 112 | Thought Leader lead gen, single image, video and document specs, In-Stream Ads |
| Lead gen and CRM | 47, 57, 83, 84, 92, 110, 111 | Higher intent option, 90 day retention |
| Bidding and budgets | 61, 62, 63, 64, 65, 66 | Bid floors, Accelerate floors |
| Measurement | 47, 48, 49, 54, 55, 56, 82, 108, 109 | RAR lookback, MOAT ID support |
| Strategy | 8, 9, 10, 121, 122, 123 | 2026 Forrester figure (13 plus 9) not traced |
| Benchmarks | 90 to 99 | None (dated studies with caveats) |
| Tools | 4, 21 to 25, 31 to 45, 47, 50, 118 to 120 | Official MCP release |

## Verification plan (open after the 2026-10-08 pass)
| Priority | Claim to verify | Where | Suggested query or path |
|----------|----------------|-------|-------------------------|
| 1 | LinkedIn launches after 2026-10-08 | Recent Marketing API Changes, Marketing Blog, Social Media Today | Monthly check of source 47 |
| 2 | Accelerate limits (14 days, $700 and $3,000 floors, single image) | Campaign Manager setup screen, Help Center | "Accelerate ad set requirements" |
| 3 | Thought Leader Ads with Lead generation and lead gen forms | Objective menu, Help Center a1399568 | Create a draft ad set with a member post |
| 4 | RAR default lookback | Business Manager report settings | Read the setting in the report |
| 5 | Predictive audiences cap (30) and the 1,000 DMP segment cap | Help Center, API changelog | "predictive audiences requirements", source 47 |
| 6 | Website retargeting max lookback; lead download retention | Matched audience creation screen; Help Center | Lookback dropdown; "download leads" |
| 7 | Higher intent lead gen form option | Lead gen form builder | Form creation screen |
| 8 | In-Stream Ads, Creator Marketplace expansion, CTV markets | Marketing Blog, account team | "LinkedIn In-Stream Ads", "Creator Marketplace availability" |
| 9 | Single image, video, document, message and conversation specs | Ads Guide | business.linkedin.com ad specs |
| 10 | Restricted categories by region | Advertising policies | Source 5 |
After each check, update the label in the module and add a row to the freshness log.

## Source quality rules for this package
| Source type | Can support | Cannot support alone |
|------------|-------------|---------------------|
| LinkedIn Help Center and API docs | Settings, limits, mechanics | Performance expectations |
| LinkedIn Marketing Blog and product pages | Launch dates, feature intent | Availability in a given account or market; product pages can be stale |
| Trade press (Social Media Today, PPC Land, Search Engine Land) | Launch dates and details reported from LinkedIn | Final limits (confirm in Help Center) |
| B2B Institute and academic studies | Strategy (95 to 5, brand vs activation, availability) | Tactical targets |
| Vendor benchmark reports (Dreamdata, Kiin, HockeyStack) | Ranges with disclosed samples | Targets for a specific account |
| LinkedIn platform claims (percent lifts) | Direction of a feature's intent | Any forecast or target |
| Practitioner posts and communities | Edge cases, defaults in practice, sentiment | Platform facts |
| GitHub repositories | Tool existence, dates, maintainers | Tool quality or security |

## How to verify a claim quickly
1. Search the LinkedIn Help Center for the exact feature name.
2. Open Campaign Manager and look for the setting in the relevant step (objective, audience, budget and schedule, placements, ads).
3. If the UI and help page disagree, trust the UI for this account and note the discrepancy in the journal.
4. For API claims, check the Recent Marketing API Changes page for the version the project pins.

## Freshness log
| Date | Checked | Change found | Module updated |
|------|---------|--------------|----------------|
| 2026-10-08 | GitHub repositories, Microsoft blog items on LinkedIn data | Initial build; LinkedIn web sources not re-fetched | All |
| 2026-10-08 | 57 live searches: Help Center, API changelog, trade press, benchmarks, B2B Institute, MCP status | Hierarchy rename; Qualified leads optimization and MQL/SQL types; frequency caps; budget rules; Reserved and First Impression Ads; BrandLink and CTV routes; Companies tab; CAPI identifiers and windows; EU messaging opt in; 2025-11 data terms; dated benchmarks; ChatGPT app; no official MCP | All modules, SKILL.md, agent, dossier |
