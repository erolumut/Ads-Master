# GAQL Audit Queries and Google Ads Scripts

> Knowledge as of 2026-10. Field availability depends on the Google Ads API version. Supported versions on 2026-10-08: v23, v24 and v25 (v25.2 released 2026-09-23). Sunsets in 2026: v20 on 2026-06-10, v21 on 2026-08-05, v22 on 2026-10-07 [Official, Google Ads Developer Blog and client library changelog]. Every field name in this module was checked on 2026-10-08 against the v25 type definitions published in Google's official client library (googleads/google-ads-python, release 33.0.0). Field names are therefore [Official, v25]; where a resource and segment combination could not be confirmed, the query says so.

All queries are read-only. They run in: the official Google Ads MCP server (`search` tool), community MCP servers, the Google Ads API (GoogleAdsService.Search or SearchStream), Google Ads Scripts (`AdsApp.search`), and the Google Ads Query Builder for testing. GAQL does not support comments, so notes sit outside the code blocks.

Conventions:
- Money fields end in `_micros`: divide by 1,000,000.
- Date filters: `segments.date DURING LAST_30_DAYS` or `segments.date BETWEEN '2026-09-01' AND '2026-09-30'`.
- Selecting `segments.date` returns one row per day; filtering on it without selecting it returns totals.
- Replace 1234567890 with real IDs. Replace thresholds with values derived from the target CPA.
- Reporting history: since 2026-06-01, daily, weekly and hourly segments are available for 37 months only; older periods return a date range error (REQUESTED_DATE_GRANULARITY_NOT_SUPPORTED in v24 and later). Query older periods with `segments.month`, `segments.quarter` or `segments.year` (kept 11 years) [Official, Google Ads Developer Blog 2026-05].

## Part A: Audit queries

### Q1. Campaign overview (last 30 days)
```sql
SELECT campaign.id, campaign.name, campaign.status, campaign.advertising_channel_type,
  campaign.advertising_channel_sub_type, campaign.bidding_strategy_type,
  campaign_budget.amount_micros, metrics.impressions, metrics.clicks, metrics.cost_micros,
  metrics.conversions, metrics.conversions_value, metrics.all_conversions
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
```
Use: spend concentration, campaign types, bid strategies. Compute CPA = cost / conversions and ROAS = conversions_value / cost.

### Q2. Search impression share and lost share
```sql
SELECT campaign.name, campaign.advertising_channel_type, metrics.search_impression_share,
  metrics.search_budget_lost_impression_share, metrics.search_rank_lost_impression_share,
  metrics.search_top_impression_share, metrics.search_absolute_top_impression_share,
  metrics.search_exact_match_impression_share, metrics.cost_micros, metrics.conversions,
  metrics.conversions_value
FROM campaign
WHERE campaign.advertising_channel_type = 'SEARCH'
  AND campaign.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
```
Read: lost IS (budget) above 10% on a campaign at or below target CPA means budget is the constraint. Lost IS (rank) above 40% means target, bid or quality is the constraint. Brand campaigns should show search IS above 90%.

### Q3. Search terms (Search campaigns)
```sql
SELECT campaign.name, ad_group.name, search_term_view.search_term, search_term_view.status,
  segments.search_term_match_type, metrics.impressions, metrics.clicks, metrics.cost_micros,
  metrics.conversions, metrics.conversions_value
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.impressions > 0
ORDER BY metrics.cost_micros DESC
LIMIT 10000
```

### Q3b. Search terms with match source, all campaign types including PMax
```sql
SELECT campaign.name, campaign.advertising_channel_type, campaign_search_term_view.search_term,
  segments.search_term_match_source, metrics.impressions, metrics.clicks, metrics.cost_micros,
  metrics.conversions, metrics.conversions_value
FROM campaign_search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.cost_micros > 0
ORDER BY metrics.cost_micros DESC
LIMIT 10000
```
- `campaign_search_term_view` returns one row per search term per campaign with cost metrics, including Performance Max. Adding keyword-related segments (ad group, keyword, match type) removes PMax rows from the result [Official, API reference v21 to v25].
- `segments.search_term_match_source` values in v25: ADVERTISER_PROVIDED_KEYWORD, AI_MAX_KEYWORDLESS, AI_MAX_BROAD_MATCH, DYNAMIC_SEARCH_ADS, PERFORMANCE_MAX, VERTICAL_ADS_DATA_FEED [Official, v25 enum]. Use it to split spend between your keywords, AI Max expansion, DSA and PMax.
- The combination of this segment with this view was not test-run for this edition. If the API rejects it, drop the segment, keep the view for PMax, and use Q3 with `segments.search_term_match_type` (v25 values include AI_MAX and PERFORMANCE_MAX besides BROAD, EXACT, PHRASE, NEAR_EXACT and NEAR_PHRASE).

### Q4. Wasted spend: search terms with cost and no conversions
```sql
SELECT campaign.name, ad_group.name, search_term_view.search_term, segments.search_term_match_type,
  metrics.clicks, metrics.cost_micros, metrics.conversions
FROM search_term_view
WHERE segments.date DURING LAST_90_DAYS
  AND metrics.conversions = 0
  AND metrics.cost_micros > 50000000
ORDER BY metrics.cost_micros DESC
LIMIT 5000
```
Set the cost threshold to 1x target CPA (here 50 in account currency). Sum cost of all rows = visible zero-conversion search term spend. Report it as a share of total Search spend. Typical finding in unmanaged accounts: 10% to 30% [Practitioner consensus, varies widely].

### Q5. Keywords with Quality Score components
```sql
SELECT campaign.name, ad_group.name, ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type, ad_group_criterion.status,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.search_predicted_ctr,
  ad_group_criterion.quality_info.creative_quality_score,
  ad_group_criterion.quality_info.post_click_quality_score, metrics.impressions, metrics.clicks,
  metrics.cost_micros, metrics.conversions
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
LIMIT 5000
```
Compute cost-weighted Quality Score. Flag keywords with QS 1 to 4 and cost above 1x target CPA.

### Q6. Conversion actions setup
```sql
SELECT conversion_action.id, conversion_action.name, conversion_action.status,
  conversion_action.type, conversion_action.category, conversion_action.origin,
  conversion_action.primary_for_goal, conversion_action.include_in_conversions_metric,
  conversion_action.counting_type, conversion_action.click_through_lookback_window_days,
  conversion_action.view_through_lookback_window_days,
  conversion_action.attribution_model_settings.attribution_model,
  conversion_action.value_settings.default_value,
  conversion_action.value_settings.always_use_default_value
FROM conversion_action
WHERE conversion_action.status = 'ENABLED'
```
Flag: micro conversions (page view, add to cart, begin checkout, engagement) with primary_for_goal = TRUE; leads with counting_type MANY_PER_CLICK; purchases with always_use_default_value = TRUE; duplicate purchase actions from GA4 and the Google tag both primary.

### Q7. Conversions by action per day (tracking health)
```sql
SELECT segments.date, segments.conversion_action_name, segments.conversion_action_category,
  metrics.conversions, metrics.conversions_value, metrics.all_conversions
FROM customer
WHERE segments.date DURING LAST_90_DAYS
ORDER BY segments.date
```
Plot per action. Flag days with zero conversions where the trailing 28-day average is above 3, and days above 2x the trailing average.

### Q8. Campaign settings audit
```sql
SELECT campaign.id, campaign.name, campaign.advertising_channel_type,
  campaign.network_settings.target_google_search, campaign.network_settings.target_search_network,
  campaign.network_settings.target_content_network,
  campaign.geo_target_type_setting.positive_geo_target_type,
  campaign.geo_target_type_setting.negative_geo_target_type, campaign.bidding_strategy_type,
  campaign.bidding_strategy, campaign.maximize_conversions.target_cpa_micros,
  campaign.maximize_conversion_value.target_roas, campaign.target_cpa.target_cpa_micros,
  campaign.target_roas.target_roas, campaign_budget.amount_micros,
  campaign_budget.explicitly_shared, campaign.optimization_score
FROM campaign
WHERE campaign.status = 'ENABLED'
```
Flag: Search campaigns with target_content_network = TRUE (Display expansion), positive_geo_target_type = PRESENCE_OR_INTEREST for local or shipping-limited businesses, shared budgets mixing different targets.

### Q8b. AI Max status and auto-upgrade dates per campaign
```sql
SELECT campaign.id, campaign.name, campaign.status, campaign.ai_max_setting.enable_ai_max,
  campaign.ai_max_setting.bundling_required, campaign.aca_migration_date_time,
  campaign.broad_match_migration_date_time
FROM campaign
WHERE campaign.advertising_channel_type = 'SEARCH'
  AND campaign.status = 'ENABLED'
```
- `enable_ai_max` FALSE or empty means no AI Max feature serves, whatever the individual feature settings say. Search term matching is on by default when AI Max is on and can be turned off per ad group [Official, v25 field docs].
- `bundling_required` = REQUIRED means AI Max must stay enabled for the campaign to keep serving text asset automation and brand list targeting [Official, v25 field docs].
- `aca_migration_date_time` and `broad_match_migration_date_time` (added in v25.1, 2026-08-19) are output-only timestamps in account time ("yyyy-MM-dd HH:mm:ss") recording when the campaign was migrated to AI Max from automatically created assets or campaign-level broad match. Empty means not migrated by that route [Official, v25 field docs]. Use them to date the trend break in reports.

### Q9. PMax channel split
```sql
SELECT campaign.name, segments.ad_network_type, metrics.impressions, metrics.clicks,
  metrics.cost_micros, metrics.conversions, metrics.conversions_value
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND segments.date DURING LAST_30_DAYS
```
The v25 `AdNetworkType` enum includes SEARCH, SEARCH_PARTNERS, CONTENT, YOUTUBE, GOOGLE_TV, GMAIL, DISCOVER, MAPS, GOOGLE_OWNED_CHANNELS and MIXED [Official, v25 enum]. Versions before the 2026 channel segmentation updates (v24.2 added ad network segmentation for PMax placement reporting) return MIXED for PMax. If the result still shows only MIXED, use the Channel performance report in the UI (Insights and reports) or its export, and the placement view below. Flag when Display plus YouTube exceed 30% of cost and deliver under 10% of conversion value.

### Q10. PMax placements (Display, YouTube, apps)
```sql
SELECT campaign.name, performance_max_placement_view.display_name,
  performance_max_placement_view.placement, performance_max_placement_view.placement_type,
  performance_max_placement_view.target_url, metrics.impressions
FROM performance_max_placement_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC
LIMIT 1000
```
Placement view returns impressions only. Use it to build the account-level placement exclusion list (mobile app categories, low quality sites, kids content).

### Q11. PMax search term insights (category level)
```sql
SELECT campaign_search_term_insight.category_label, campaign_search_term_insight.id,
  metrics.impressions, metrics.clicks, metrics.conversions, metrics.conversions_value
FROM campaign_search_term_insight
WHERE campaign_search_term_insight.campaign_id = '1234567890'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.conversions DESC
```
Requires a single campaign ID filter. For query-level PMax search terms with cost, use Q3b (`campaign_search_term_view`). If your connector runs an older version without it, export the PMax search terms report from the UI to `ads-master/data/imports/`.

### Q12. PMax asset group performance
```sql
SELECT campaign.name, asset_group.id, asset_group.name, asset_group.status,
  asset_group.primary_status, asset_group.ad_strength, metrics.impressions, metrics.clicks,
  metrics.cost_micros, metrics.conversions, metrics.conversions_value
FROM asset_group
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

### Q13. PMax asset performance (asset level reporting)
```sql
SELECT campaign.name, asset_group.name, asset_group_asset.field_type,
  asset_group_asset.status, asset_group_asset.primary_status, asset_group_asset.source,
  asset.id, asset.type, asset.name, asset.text_asset.text, asset.youtube_video_asset.youtube_video_id,
  metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions,
  metrics.conversions_value
FROM asset_group_asset
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```
`asset_group_asset.performance_label` is gone: Google deprecated PMax performance labels in favor of full metrics in 2025, and the field is absent from the v23 to v25 type definitions [Official, client library; Practitioner report, 2025-05]. Judge assets on conversions and value per impression instead. `source` separates advertiser assets from automatically created ones. If metrics are rejected for this resource in your version, use the asset group level report (Q12) and the UI asset report.

### Q14. RSA asset performance
```sql
SELECT campaign.name, ad_group.name, ad_group_ad_asset_view.field_type,
  ad_group_ad_asset_view.performance_label, ad_group_ad_asset_view.pinned_field,
  asset.text_asset.text, metrics.impressions, metrics.clicks, metrics.conversions
FROM ad_group_ad_asset_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_ad_asset_view.field_type IN ('HEADLINE', 'DESCRIPTION')
ORDER BY metrics.impressions DESC
```
Replace assets labeled LOW with at least 5,000 impressions. Count pinned assets per ad.

### Q15. RSA ad strength and approval
```sql
SELECT campaign.name, ad_group.name, ad_group_ad.ad.id, ad_group_ad.ad_strength,
  ad_group_ad.policy_summary.approval_status, ad_group_ad.ad.final_urls, metrics.impressions,
  metrics.clicks, metrics.conversions
FROM ad_group_ad
WHERE ad_group_ad.ad.type = 'RESPONSIVE_SEARCH_AD'
  AND ad_group_ad.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
```

### Q16. Disapproved and limited ads
```sql
SELECT campaign.name, ad_group.name, ad_group_ad.ad.id, ad_group_ad.policy_summary.approval_status,
  ad_group_ad.policy_summary.review_status, ad_group_ad.policy_summary.policy_topic_entries
FROM ad_group_ad
WHERE ad_group_ad.status = 'ENABLED'
  AND ad_group_ad.policy_summary.approval_status IN ('DISAPPROVED', 'APPROVED_LIMITED', 'AREA_OF_INTEREST_ONLY')
```
Remember the 2026-07-21 change: in-account appeals are not available for policy decisions older than 6 months [Official, 2026-07].

### Q17. Negative keywords (campaign level) and shared lists
```sql
SELECT campaign.name, campaign_criterion.keyword.text, campaign_criterion.keyword.match_type
FROM campaign_criterion
WHERE campaign_criterion.negative = TRUE
  AND campaign_criterion.type = 'KEYWORD'
```
```sql
SELECT shared_set.id, shared_set.name, shared_set.type, shared_set.member_count, shared_set.status
FROM shared_set
WHERE shared_set.type = 'NEGATIVE_KEYWORDS'
```
```sql
SELECT campaign.name, shared_set.name, campaign_shared_set.status
FROM campaign_shared_set
WHERE shared_set.type = 'NEGATIVE_KEYWORDS'
```

### Q18. Brand list exclusions on PMax and AI Max
```sql
SELECT campaign.name, campaign.advertising_channel_type, campaign_criterion.type,
  campaign_criterion.negative, campaign_criterion.brand_list.shared_set
FROM campaign_criterion
WHERE campaign_criterion.type = 'BRAND_LIST'
```
Any non-brand PMax or AI Max campaign without a negative BRAND_LIST criterion is a brand leakage risk. Field names, the BRAND_LIST criterion type and the BRANDS shared set type are confirmed in v25 [Official, v25]. To list the brand lists themselves: `SELECT shared_set.id, shared_set.name, shared_set.member_count FROM shared_set WHERE shared_set.type = 'BRANDS'`.

### Q19. Landing pages (including expanded URLs)
```sql
SELECT landing_page_view.unexpanded_final_url, metrics.clicks, metrics.cost_micros,
  metrics.conversions, metrics.conversions_value, metrics.mobile_friendly_clicks_percentage,
  metrics.speed_score
FROM landing_page_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 500
```
```sql
SELECT expanded_landing_page_view.expanded_final_url, metrics.clicks, metrics.cost_micros,
  metrics.conversions
FROM expanded_landing_page_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 500
```
Flag expanded URLs on blog, careers, login, support or out of stock pages.

### Q20. Geography: where users actually were
```sql
SELECT campaign.name, user_location_view.country_criterion_id,
  user_location_view.targeting_location, metrics.clicks, metrics.cost_micros, metrics.conversions
FROM user_location_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```
Rows with targeting_location = FALSE are clicks from outside targeted locations (Presence or interest leakage).

### Q21. Device split
```sql
SELECT campaign.name, segments.device, metrics.clicks, metrics.cost_micros, metrics.conversions,
  metrics.conversions_value
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
```

### Q22. Shopping and PMax product performance
```sql
SELECT campaign.name, segments.product_item_id, segments.product_title, segments.product_brand,
  segments.product_type_l1, segments.product_custom_attribute0, metrics.impressions,
  metrics.clicks, metrics.cost_micros, metrics.conversions, metrics.conversions_value
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 10000
```
Classify heroes, sidekicks, villains and zombies (see shopping module). Zombies are products in the feed with no rows here; compare against the feed export.

### Q23. Budgets and pacing (month to date)
```sql
SELECT campaign.name, campaign_budget.amount_micros, campaign_budget.explicitly_shared,
  campaign_budget.has_recommended_budget, campaign_budget.recommended_budget_amount_micros,
  metrics.cost_micros, metrics.conversions
FROM campaign
WHERE segments.date DURING THIS_MONTH
  AND campaign.status = 'ENABLED'
```

### Q24. Change history (last 14 days)
```sql
SELECT change_event.change_date_time, change_event.change_resource_type,
  change_event.change_resource_name, change_event.client_type, change_event.user_email,
  change_event.resource_change_operation, change_event.changed_fields
FROM change_event
WHERE change_event.change_date_time >= '2026-09-24'
  AND change_event.change_date_time <= '2026-10-08'
ORDER BY change_event.change_date_time DESC
LIMIT 1000
```
change_event covers only the last 30 days in the API and requires a LIMIT. Use it to link performance shifts to edits, auto-applied recommendations (client_type shows the source) and Google-initiated changes.

### Q25. Recommendations and optimization score
```sql
SELECT recommendation.type, recommendation.campaign,
  recommendation.impact.base_metrics.conversions,
  recommendation.impact.potential_metrics.conversions,
  recommendation.impact.base_metrics.cost_micros,
  recommendation.impact.potential_metrics.cost_micros
FROM recommendation
```
```sql
SELECT customer.id, customer.descriptive_name, customer.optimization_score,
  customer.optimization_score_weight, customer.auto_tagging_enabled
FROM customer
```
```sql
SELECT recommendation_subscription.type, recommendation_subscription.status
FROM recommendation_subscription
```
The last query lists auto-apply subscriptions (resource confirmed in v25 [Official]). Flag auto-apply for keyword additions, broad match upgrades, budget increases or target changes.

### Q26. Audience performance and Customer Match sizes
```sql
SELECT campaign.name, ad_group.name, ad_group_criterion.criterion_id, ad_group_criterion.type,
  ad_group_criterion.bid_modifier, metrics.impressions, metrics.cost_micros, metrics.conversions
FROM ad_group_audience_view
WHERE segments.date DURING LAST_30_DAYS
```
```sql
SELECT user_list.id, user_list.name, user_list.type, user_list.membership_status,
  user_list.size_for_search, user_list.size_for_display, user_list.match_rate_percentage
FROM user_list
WHERE user_list.type = 'CRM_BASED'
```

### Q27. Brand vs non-brand split by naming convention
```sql
SELECT campaign.name, metrics.cost_micros, metrics.conversions, metrics.conversions_value
FROM campaign
WHERE campaign.name LIKE '%_BR_%'
  AND segments.date DURING LAST_30_DAYS
```
Run again with `NOT LIKE '%_BR_%'` for non-brand. Depends on the naming convention in the account structure module.

### Q28. AI Max search term, headline and landing page combinations
```sql
SELECT campaign.name, ad_group.name, ai_max_search_term_ad_combination_view.search_term,
  ai_max_search_term_ad_combination_view.headline,
  ai_max_search_term_ad_combination_view.landing_page, metrics.impressions, metrics.clicks,
  metrics.cost_micros, metrics.conversions
FROM ai_max_search_term_ad_combination_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 1000
```
The view was added in API v21 (2025-08); attribute names `search_term`, `headline` (up to three headline assets joined by " | ") and `landing_page` (the dynamically generated destination URL) are confirmed in v25 [Official, v25 field docs]. Related: `final_url_expansion_asset_view` (campaign, ad_group, asset_group, asset, field_type, status, final_url) shows which assets served with expanded URLs [Official, v25].

### Q29. Hour of day and day of week
```sql
SELECT campaign.name, segments.day_of_week, segments.hour, metrics.clicks, metrics.cost_micros,
  metrics.conversions
FROM campaign
WHERE segments.date DURING LAST_90_DAYS
  AND campaign.status = 'ENABLED'
```
Smart Bidding handles time of day. Use this only for staffed call hours or Manual CPC campaigns.

### Q30. Ad group level performance for consolidation decisions
```sql
SELECT campaign.name, ad_group.id, ad_group.name, ad_group.status, metrics.impressions,
  metrics.cost_micros, metrics.conversions
FROM ad_group
WHERE segments.date DURING LAST_90_DAYS
  AND ad_group.status = 'ENABLED'
ORDER BY metrics.impressions ASC
```
Ad groups with under 100 impressions in 90 days are consolidation candidates.

## Part B: Google Ads Scripts (read-only by default)

Scripts run inside Google Ads (Tools, Bulk actions, Scripts), use JavaScript and `AdsApp.search` with GAQL. Limits: about 30 minutes per run; MCC scripts can process accounts in parallel (executeInParallel, up to 50 accounts per run) [Official, verify]. Every script below only reads data and writes to a spreadsheet or email. Writing scripts that change bids, budgets or keywords require explicit human approval, a preview run, and a rollback plan.

### S1. Wasted search terms to a spreadsheet
```javascript
var SHEET_URL = 'PASTE_SPREADSHEET_URL';
var MIN_COST = 50; // account currency, set to 1x target CPA
var RANGE = 'LAST_30_DAYS';

function main() {
  var query = 'SELECT campaign.name, ad_group.name, search_term_view.search_term, ' +
    'metrics.clicks, metrics.cost_micros, metrics.conversions ' +
    'FROM search_term_view WHERE segments.date DURING ' + RANGE + ' ' +
    'AND metrics.conversions = 0 AND metrics.cost_micros > ' + (MIN_COST * 1000000) + ' ' +
    'ORDER BY metrics.cost_micros DESC';
  var rows = AdsApp.search(query);
  var out = [['Campaign', 'Ad group', 'Search term', 'Clicks', 'Cost', 'Conversions']];
  while (rows.hasNext()) {
    var r = rows.next();
    out.push([r.campaign.name, r.adGroup.name, r.searchTermView.searchTerm,
      Number(r.metrics.clicks), Number(r.metrics.costMicros) / 1000000,
      Number(r.metrics.conversions)]);
  }
  var sheet = SpreadsheetApp.openByUrl(SHEET_URL).getSheets()[0];
  sheet.clear();
  sheet.getRange(1, 1, out.length, out[0].length).setValues(out);
  Logger.log('Rows written: ' + (out.length-1));
}
```

### S2. N-gram analysis of search terms
```javascript
var SHEET_URL = 'PASTE_SPREADSHEET_URL';
var RANGE = 'LAST_90_DAYS';
var N_VALUES = [1, 2];

function main() {
  var query = 'SELECT search_term_view.search_term, metrics.clicks, metrics.cost_micros, ' +
    'metrics.conversions, metrics.conversions_value FROM search_term_view ' +
    'WHERE segments.date DURING ' + RANGE + ' AND metrics.impressions > 0';
  var rows = AdsApp.search(query);
  var grams = {};
  while (rows.hasNext()) {
    var r = rows.next();
    var words = r.searchTermView.searchTerm.toLowerCase().split(/\s+/);
    var cost = Number(r.metrics.costMicros) / 1000000;
    var conv = Number(r.metrics.conversions);
    var value = Number(r.metrics.conversionsValue);
    var clicks = Number(r.metrics.clicks);
    N_VALUES.forEach(function(n) {
      var seen = {};
      for (var i = 0; i + n <= words.length; i++) {
        var g = words.slice(i, i + n).join(' ');
        if (seen[g]) { continue; }
        seen[g] = true;
        if (!grams[g]) { grams[g] = {n: n, clicks: 0, cost: 0, conv: 0, value: 0, terms: 0}; }
        grams[g].clicks += clicks;
        grams[g].cost += cost;
        grams[g].conv += conv;
        grams[g].value += value;
        grams[g].terms += 1;
      }
    });
  }
  var out = [['N-gram', 'N', 'Terms', 'Clicks', 'Cost', 'Conversions', 'Value', 'CPA', 'ROAS']];
  Object.keys(grams).forEach(function(g) {
    var x = grams[g];
    var cpa = x.conv > 0 ? x.cost / x.conv : '';
    var roas = x.cost > 0 ? x.value / x.cost : '';
    out.push([g, x.n, x.terms, x.clicks, x.cost, x.conv, x.value, cpa, roas]);
  });
  var header = out.shift();
  out.sort(function(a, b) { return b[4] > a[4] ? 1 : (b[4] < a[4] ? -1 : 0); });
  out.unshift(header);
  var sheet = SpreadsheetApp.openByUrl(SHEET_URL).getSheets()[0];
  sheet.clear();
  sheet.getRange(1, 1, out.length, header.length).setValues(out);
}
```
Read: n-grams with cost above 2x target CPA and zero conversions are negative phrase candidates. Check that no converting term contains the n-gram before adding it.

### S3. Conversion tracking anomaly alert
```javascript
var EMAIL = 'PASTE_EMAIL';
var LOW_RATIO = 0.5;   // alert if yesterday is below 50% of the trailing median
var HIGH_RATIO = 2.0;  // alert if yesterday is above 200%

function main() {
  var query = 'SELECT segments.date, metrics.conversions, metrics.clicks, metrics.cost_micros ' +
    'FROM customer WHERE segments.date DURING LAST_30_DAYS ORDER BY segments.date';
  var rows = AdsApp.search(query);
  var days = [];
  while (rows.hasNext()) {
    var r = rows.next();
    days.push({date: r.segments.date, conv: Number(r.metrics.conversions),
      clicks: Number(r.metrics.clicks)});
  }
  if (days.length < 10) { return; }
  var y = days[days.length-1];
  var history = days.slice(0, days.length-1).map(function(d) { return d.conv; }).sort(function(a, b) { return a-b; });
  var median = history[Math.floor(history.length / 2)];
  if (median < 3) { return; } // too little volume for a daily alert
  var ratio = y.conv / median;
  if (ratio < LOW_RATIO || ratio > HIGH_RATIO) {
    MailApp.sendEmail(EMAIL, 'Google Ads conversion anomaly ' + AdsApp.currentAccount().getName(),
      'Date: ' + y.date + '\nConversions: ' + y.conv + '\nTrailing median: ' + median +
      '\nClicks: ' + y.clicks + '\nCheck tracking before changing bids. Consider a data exclusion if tracking broke.');
  }
}
```
Schedule daily. Note that yesterday's conversions keep arriving for days (conversion lag); set thresholds with that in mind or compare clicks too.

### S4. Monthly budget pacing alert
```javascript
var EMAIL = 'PASTE_EMAIL';
var MONTHLY_PLAN = 20000; // account currency, from STRATEGY.md

function main() {
  var tz = AdsApp.currentAccount().getTimeZone();
  var now = new Date();
  var day = Number(Utilities.formatDate(now, tz, 'd'));
  var year = Number(Utilities.formatDate(now, tz, 'yyyy'));
  var month = Number(Utilities.formatDate(now, tz, 'M'));
  var daysInMonth = new Date(year, month, 0).getDate();
  var rows = AdsApp.search('SELECT metrics.cost_micros FROM customer WHERE segments.date DURING THIS_MONTH');
  var spend = 0;
  while (rows.hasNext()) { spend += Number(rows.next().metrics.costMicros) / 1000000; }
  var elapsed = Math.max(day-1, 1); // today is partial
  var projected = spend / elapsed * daysInMonth;
  var ratio = projected / MONTHLY_PLAN;
  if (ratio > 1.1 || ratio < 0.9) {
    MailApp.sendEmail(EMAIL, 'Google Ads pacing ' + Math.round(ratio * 100) + '% of plan',
      'Month to date spend: ' + spend.toFixed(0) + '\nProjected: ' + projected.toFixed(0) +
      '\nPlan: ' + MONTHLY_PLAN + '\nDraft a budget change list for approval.');
  }
}
```

### S5. Disapproved ads and policy alert
```javascript
var EMAIL = 'PASTE_EMAIL';

function main() {
  var query = 'SELECT campaign.name, ad_group.name, ad_group_ad.ad.id, ' +
    'ad_group_ad.policy_summary.approval_status FROM ad_group_ad ' +
    "WHERE ad_group_ad.status = 'ENABLED' AND campaign.status = 'ENABLED' " +
    "AND ad_group_ad.policy_summary.approval_status = 'DISAPPROVED'";
  var rows = AdsApp.search(query);
  var lines = [];
  while (rows.hasNext()) {
    var r = rows.next();
    lines.push(r.campaign.name + ' | ' + r.adGroup.name + ' | ad ' + r.adGroupAd.ad.id);
  }
  if (lines.length > 0) {
    MailApp.sendEmail(EMAIL, 'Google Ads: ' + lines.length + ' disapproved ads',
      lines.join('\n') + '\n\nAppeal within 6 months of the decision (in-account appeals close after that).');
  }
}
```

## Part C: Practitioner script libraries

- Google Ads Scripts documentation and solutions gallery (developers.google.com/google-ads/scripts).
- Community and vendor scripts (for example PMax insight scripts and n-gram scripts shared by practitioners and tool vendors) are useful, but read every line before running, run in preview first, and never paste a script that writes changes without approval.
