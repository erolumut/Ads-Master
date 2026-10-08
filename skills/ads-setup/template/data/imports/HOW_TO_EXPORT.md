# How to export data for the agents

Drop files here with a date prefix: `YYYY-MM-DD_<source>_<what>.csv`. If a connector or MCP server is available, agents pull data directly and you can skip this.

| Agent | Export | Where | Range |
|-------|--------|-------|-------|
| meta-ads | Ads Manager: campaign, ad set, ad level with spend, results, CPA/ROAS, CPM, CTR (link), frequency; breakdowns by placement and age/gender | Ads Manager > Reports > Export | Last 30 and 90 days, daily |
| google-ads | Campaigns, ad groups, keywords, search terms, assets, PMax channel report, auction insights | Google Ads > Reports or Report editor | Last 30 and 90 days |
| microsoft-ads | Campaign, keyword, search term reports | Reports | Last 30 days |
| chatgpt-ads | Campaign and ad report from Ads Manager | ads.openai.com | Last 30 days |
| tiktok-ads | Campaign, ad group, ad with video metrics (2s, 6s views, average watch time) | Ads Manager > Reporting | Last 30 days |
| linkedin-ads | Campaign and creative performance, demographics | Campaign Manager | Last 90 days |
| seo | Search Console performance (queries, pages), Coverage/Pages report, crawl export (Screaming Frog), backlinks | GSC, crawler, Ahrefs/Semrush | Last 16 months |
| ai-search-optimization | Prompt tracking exports, GA4 AI referral traffic, Bing Webmaster AI Performance | Tracking tool, GA4, Bing WMT | Last 90 days |
| measurement | GA4 traffic acquisition and key events, backend orders, CRM pipeline | GA4, Shopify, CRM | Last 90 days |
| commerce-feeds | Merchant Center diagnostics, feed file | Merchant Center | Current |
| cro | GA4 funnel exploration, Clarity/Hotjar insights, test results | GA4, testing tool | Last 90 days |
| lifecycle-crm | Flow and campaign performance, list growth, deliverability, cohort repeat rates | Klaviyo, Braze, Customer.io, Shopify | Last 90 days |
| offer-strategy | Orders with bundle or SKU group, discount codes, shipping charged, competitor and retail prices | Shopify or backend, price checks | Last 90 days |
| mobile-app-growth | App Store Connect and Play Console analytics, MMP cohorts (installs, D1, D7, D30, revenue), Apple Ads keywords | App Store Connect, Play Console, MMP | Last 90 days |
| video-studio | Creative performance by creative ID (hook rate, hold rate, CTR, CPA) | Channel exports | Last 30 days |
| daily report (measurement) | Platform spend CSV (date, channel, spend, impressions, clicks, conversions, conversion_value) and backend orders CSV | Platforms, backend | Last 30 days |
