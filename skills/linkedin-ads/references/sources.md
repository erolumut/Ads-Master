# Sources (annotated)

> Research method note (2026-10-08): the shared web search budget for this build was exhausted before LinkedIn specific searches could run, and direct page fetching was blocked by the environment's egress policy. LinkedIn platform facts therefore come from the author's knowledge of official LinkedIn documentation up to mid 2026 and are labeled by confidence; GitHub repository facts were verified by GitHub search on 2026-10-08; Microsoft Advertising items that involve LinkedIn data were verified through search extracts of Microsoft's blog. Status column: Verified (checked in this build), Known (official source known to the author, not re-fetched), Verify (specific claim needs checking).

## Official LinkedIn sources

| # | Title | Publisher | URL | Date | Supports | Status |
|---|-------|-----------|-----|------|----------|--------|
| 1 | LinkedIn Marketing Solutions (ads overview, Ads Guide, specs) | LinkedIn | https://business.linkedin.com/marketing-solutions | Rolling | Objectives, formats, specs | Known |
| 2 | LinkedIn Help Center, Marketing Solutions | LinkedIn | https://www.linkedin.com/help/lms | Rolling | Campaign Manager settings, Insight Tag, lead gen forms, minimums | Known |
| 3 | LinkedIn Marketing Blog | LinkedIn | https://www.linkedin.com/business/marketing/blog | Rolling | Product announcements (Accelerate, Thought Leader Ads, BrandLink, CTV) | Known |
| 4 | LinkedIn Marketing API documentation | Microsoft Learn (LinkedIn) | https://learn.microsoft.com/en-us/linkedin/marketing/ | Rolling | API, versioning, adAnalytics, conversions, lead sync | Known |
| 5 | LinkedIn Advertising Policies | LinkedIn | https://www.linkedin.com/legal/ads-policy | Rolling | Prohibited and restricted content, political ads prohibition | Known |
| 6 | LinkedIn Ad Library | LinkedIn | https://www.linkedin.com/ad-library | Rolling | Competitor ad research, transparency | Known |
| 7 | Campaign Manager | LinkedIn | https://www.linkedin.com/campaignmanager | Rolling | UI names, forecast panel, reports | Known |
| 8 | LinkedIn B2B Institute | LinkedIn | https://business.linkedin.com/marketing-solutions/b2b-institute | 2019 to 2024 | 95 to 5 rule, B2B effectiveness research | Known |
| 9 | Accelerate campaigns announcement | LinkedIn | Marketing Blog (see 3) | 2023-10 | AI campaign type | Known; 2026 coverage Verify |
| 10 | Lookalike audiences retirement and predictive audiences | LinkedIn | Help Center (see 2) | 2024-02 | Lookalikes retired; predictive audiences | Known; seed rules Verify |
| 11 | Thought Leader Ads expansion to any member with permission | LinkedIn | Marketing Blog (see 3) | 2024 | Thought Leader scope | Known; 2026 formats Verify |
| 12 | Conversions API launch | LinkedIn | Marketing Blog and API docs (3, 4) | 2023 | CAPI | Known; identifiers Verify |
| 13 | Revenue attribution report | LinkedIn | Help Center (see 2) | 2023 | RAR | Known; CRMs and model Verify |
| 14 | Business Manager | LinkedIn | Help Center (see 2) | 2023 | Account ownership | Known |
| 15 | BrandLink and CTV | LinkedIn | Marketing Blog (see 3) | 2024 to 2025 | Video programs | Verify |
| 16 | EU Group targeting removal | LinkedIn and press coverage | Press coverage of DSA complaint outcome | 2024 | EU targeting limits | Verify |
| 17 | Member data use for AI training and Microsoft ad personalization update | LinkedIn | LinkedIn privacy policy and terms updates | 2025 | Data policy context | Verify |

## Official LinkedIn developer repositories (verified on GitHub, 2026-10-08)

| # | Repository | URL | Created | Supports | Status |
|---|-----------|-----|---------|----------|--------|
| 18 | linkedin-api-python-client | https://github.com/linkedin-developers/linkedin-api-python-client | 2023-01-12 | Official Python client | Verified |
| 19 | linkedin-api-js-client | https://github.com/linkedin-developers/linkedin-api-js-client | 2022-12-28 | JavaScript client | Verified |
| 20 | linkedin-capi-tag-template | https://github.com/linkedin-developers/linkedin-capi-tag-template | 2023-08-30 | Official GTM server template for CAPI | Verified |
| 21 | reactor-extension-linkedin-edge | https://github.com/linkedin-developers/reactor-extension-linkedin-edge | 2026-06-24 | Adobe event forwarding of conversions to LinkedIn | Verified |
| 22 | java-sample-application | https://github.com/linkedin-developers/java-sample-application | 2021-10-08 | API samples | Verified |

## Research and studies

| # | Title | Publisher | URL | Date | Supports | Status |
|---|-------|-----------|-----|------|----------|--------|
| 23 | Advertising effectiveness and the 95-5 rule (John Dawes) | Ehrenberg-Bass Institute for the LinkedIn B2B Institute | B2B Institute pages (see 8) | 2021 | 95 to 5 rule | Known |
| 24 | The 5 Principles of Growth in B2B Marketing (Les Binet, Peter Field) | LinkedIn B2B Institute | B2B Institute pages (see 8) | 2019 | Brand and activation balance in B2B | Known |
| 25 | B2B buying group research | Gartner | gartner.com (B2B buying journey research) | Various | 6 to 10 stakeholder buying groups | Known; exact edition Verify |

## Microsoft Advertising sources involving LinkedIn data (verified via search extracts)

| # | Title | URL | Date | Supports |
|---|-------|-----|------|----------|
| 26 | Less busywork, more growth: What's new in Microsoft Advertising this September | https://about.ads.microsoft.com/en/blog/post/september-2026/less-busywork-more-growth-what-new-in-microsoft-advertising-this-september | 2026-09-30 | LinkedIn company lists up to 10,000 in Microsoft Search and Audience campaigns; LinkedIn data excludes EEA, UK, Swiss users |
| 27 | New Performance Max tools and other product updates for February | https://about.ads.microsoft.com/en/blog/post/february-2025/new-performance-max-tools-and-other-product-updates-for-february | 2025-02 | LinkedIn profile targeting as PMax signal pilot |
| 28 | Microsoft Advertising gains LinkedIn company lists of up to 10,000 firms | https://ppc.land/microsoft-advertising-gains-linkedin-company-lists-of-up-to-10-000-firms | 2026 | Coverage of the same change |

## MCP servers and tools (verified on GitHub, 2026-10-08)

| # | Repository | URL | Created | Notes |
|---|-----------|-----|---------|-------|
| 29 | danielpopamd/linkedin-ads-mcp | https://github.com/danielpopamd/linkedin-ads-mcp | 2026-01-20 | Community, write capable |
| 30 | amekala/ads-mcp | https://github.com/amekala/ads-mcp | 2025-10-27 | Multi platform |
| 31 | markifact/markifact-mcp | https://github.com/markifact/markifact-mcp | 2026-05-03 | Multi platform, human in the loop writes |
| 32 | adkit/ads-mcp | https://github.com/adkit/ads-mcp | 2026-05-19 | Multi platform |
| 33 | stan-rym/liam-linkedin-ads-MCP | https://github.com/stan-rym/liam-linkedin-ads-MCP | 2026-06-14 | Campaign creation |
| 34 | Nuraveda/linkedin-ads-mcp | https://github.com/Nuraveda/linkedin-ads-mcp | 2026-05-29 | Python, MIT |
| 35 | DanielSylvester/linkedin-ads-mcp | https://github.com/DanielSylvester/linkedin-ads-mcp | 2026-05-25 | Community |
| 36 | proxy-intell/linkedin-ads-library-mcp | https://github.com/proxy-intell/linkedin-ads-library-mcp | 2026-08-05 | Ad Library research |
| 37 | CDataSoftware/linkedin-ads-mcp-server-by-cdata | https://github.com/CDataSoftware/linkedin-ads-mcp-server-by-cdata | 2025-06-23 | Read only |
| 38 | pipeworx-io/mcp-linkedin_ads | https://github.com/pipeworx-io/mcp-linkedin_ads | 2026-04-15 | Community pack |
| 39 | Synter-Media-AI/mcp-server | https://github.com/Synter-Media-AI/mcp-server | 2026-01-29 | Multi platform |
| 40 | PaidSync/paidsync-mcp | https://github.com/PaidSync/paidsync-mcp | 2026-05-11 | Hosted multi platform |
| 41 | opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms | https://github.com/opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms | 2026-07-10 | Hosted, approval gates |
| 42 | jshorwitz/awesome-agentic-advertising | https://github.com/jshorwitz/awesome-agentic-advertising | 2026-02-07 | Directory |
| 43 | Dataslayer-AI/Marketing-skills | https://github.com/Dataslayer-AI/Marketing-skills | 2026-03-19 | Skills plus connector MCP |

## Sources by module
| Module | Main sources | Most important claims to verify |
|--------|-------------|--------------------------------|
| Account structure | 1, 2, 9, 14 | Objective list 2026, Accelerate coverage |
| Targeting and ABM | 2, 10, 16, 26 | Matched audience limits and windows, EU restrictions |
| Formats and creative | 1, 11, 15 | Specs, Thought Leader format support, BrandLink and CTV status |
| Lead gen and CRM | 2, 4 | Custom question limits, retention window, integration list |
| Bidding and budgets | 2 | Minimums, overspend rule, frequency caps |
| Measurement | 4, 12, 13, 20, 21 | CAPI identifiers and lookback, RAR CRMs and model |
| Strategy | 8, 23, 24, 25 | None (stable research) |
| Tools | 4, 18 to 22, 29 to 43 | API version support window, MCP maintenance |

## Freshness log
| Date | Checked | Change found | Module updated |
|------|---------|--------------|----------------|
| 2026-10-08 | GitHub repositories, Microsoft blog items on LinkedIn data | Initial build; LinkedIn web sources not re-fetched | All |
