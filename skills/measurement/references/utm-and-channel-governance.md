# UTM and Channel Governance

Bad UTMs create Unassigned traffic, split channels, and mislead every cross-channel report. This module sets the taxonomy, the dynamic parameters per platform, the GA4 channel rules, and a custom channel group with AI assistants and paid AI surfaces.

## 1. Taxonomy rules

1. Lowercase everything. GA4 is case sensitive ("Facebook" and "facebook" are two sources).
2. No spaces; use underscores inside values and hyphens only inside compound words.
3. Controlled vocabulary for utm_source and utm_medium (tables below). Free text only in utm_campaign, utm_content and utm_term.
4. Never put UTMs on internal links. Use internal promotion events (view_promotion, select_promotion) instead.
5. Platforms with auto-tagging (Google gclid, Microsoft msclkid) still get UTMs only where needed for non-Google tools; GA4 uses gclid data for Google Ads traffic when auto-tagging and the link are on.
6. Campaign naming carries the structure so UTMs can inherit it: `<country>_<objective>_<audience>_<offer>_<yyyymm>` (example `tr_conv_cold_spring-sale_202610`). Agree the pattern with channel agents.
7. utm_id carries the platform campaign ID when you want cost data import joins.
8. Every new link goes through the UTM builder sheet (validation formulas) or a link governance tool.

## 2. Source and medium vocabulary

| Channel | utm_source | utm_medium | Notes |
|---------|-----------|-----------|-------|
| Meta paid | facebook, instagram (or {{site_source_name}} mapped) | paid_social or cpc | Both match GA4 Paid Social when source is in the social list |
| TikTok paid | tiktok | paid_social | |
| LinkedIn paid | linkedin | paid_social | |
| Pinterest paid | pinterest | paid_social | |
| Snap paid | snapchat | paid_social | |
| Reddit paid | reddit | paid_social | |
| X paid | x or twitter | paid_social | Check source list membership |
| Google Ads | google (auto-tagging) | cpc | Let auto-tagging handle it; add UTMs only via final URL suffix if needed |
| Microsoft Ads | bing | cpc | Microsoft can auto-append UTMs (account setting) |
| ChatGPT Ads | chatgpt (or openai) | cpc | Lands in Paid Other by default; use the custom channel group below; verify after launch how GA4's AI Assistant channel treats tagged paid clicks [Unverified] |
| Perplexity or other AI ad surfaces | perplexity, copilot | cpc | Same treatment as ChatGPT Ads |
| Affiliates | partner name | affiliate | |
| Email | esp name or newsletter | email | |
| SMS | sms | sms | |
| Push | app or web push vendor | push | Mobile Push Notifications channel |
| Influencer organic | creator handle | social | Organic Social; use a dedicated campaign name |
| Influencer paid (whitelisting) | platform | paid_social | utm_content carries creator handle |
| QR codes and print | print, ooh, packaging | qr | Falls into Unassigned by default: add a custom channel |
| Podcast and audio ads | podcast name | audio | Audio channel |

Pitfall: GA4 paid detection uses the medium regex `^(.*cp.*|ppc|retargeting|paid.*)$`. "paid_social" and "cpc" match; "social_paid" does not and lands in Organic Social.

## 3. Dynamic URL parameters per platform

| Platform | Template | Notes |
|----------|----------|-------|
| Meta (URL parameters field) | `utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&utm_id={{campaign.id}}` | site_source_name returns fb, ig, msg, an; map in a custom channel or use fixed "facebook" |
| Google Ads (final URL suffix, only if needed) | `utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={creative}&utm_term={keyword}` | Auto-tagging gclid wins in GA4; ValueTrack also has {adgroupid}, {matchtype}, {network}, {device}, {targetid}, {loc_physical_ms} |
| Microsoft Ads | `utm_source=bing&utm_medium=cpc&utm_campaign={CampaignId}&utm_content={AdId}&utm_term={keyword:default}` | Or enable automatic UTM tagging in account settings; keep msclkid auto-tagging on |
| TikTok | `utm_source=tiktok&utm_medium=paid_social&utm_campaign=__CAMPAIGN_NAME__&utm_content=__CID_NAME__&utm_term=__AID_NAME__&utm_id=__CAMPAIGN_ID__` | Macros: __CAMPAIGN_ID__, __CAMPAIGN_NAME__, __AID__ (ad group), __AID_NAME__, __CID__ (ad), __CID_NAME__, __PLACEMENT__ [verify current list] |
| LinkedIn | `utm_source=linkedin&utm_medium=paid_social&utm_campaign={{CAMPAIGN_NAME}}&utm_content={{CREATIVE_ID}}&utm_id={{CAMPAIGN_ID}}` | LinkedIn dynamic UTM macros exist for account, campaign group, campaign and creative [verify exact macro names] |
| Pinterest, Snap, Reddit | Use each platform's dynamic macro list | [verify current macros in each platform's help center] |
| ChatGPT Ads | Query string template supports placeholders such as {campaign_id}, {ad_id}, {oppref} per community API notes [Unverified] | Make sure oppref is preserved for the pixel |

## 4. GA4 Default Channel Group rules (summary)

Rules are evaluated in order; the first match wins. Summary of Google's definitions [Official; confirm on the "Default channel group" help page because lists and order change]:

| Channel | Rule (simplified) |
|---------|-------------------|
| Direct | Source is (direct) and medium is (none) or (not set) |
| Cross-network | Campaign name contains "cross-network" (for example Performance Max) |
| Paid Shopping | (Source in shopping sites list or campaign name matches shopping regex) and medium matches paid regex |
| Paid Search | Source in search sites list and medium matches paid regex |
| Paid Social | Source in social sites list and medium matches paid regex |
| Paid Video | Source in video sites list and medium matches paid regex |
| Display | Medium is display, banner, expandable, interstitial or cpm |
| Paid Other | Medium matches paid regex and nothing above matched |
| Organic Shopping | Source in shopping list or campaign name matches shopping regex |
| Organic Social | Source in social list or medium is social, social-network, social-media, sm, social network, social media |
| Organic Video | Source in video list or medium matches video |
| Organic Search | Source in search list or medium is organic |
| Referral | Medium is referral, app or link |
| Email | Source or medium is email, e-mail, e_mail, e mail |
| Affiliates | Medium is affiliate |
| Audio | Medium is audio |
| SMS | Source or medium is sms |
| Mobile Push Notifications | Medium ends with push or contains mobile or notification, or source is firebase |
| AI Assistant (since 2026-05-13) | GA4 sets medium ai-assistant, campaign (ai-assistant) when the referrer matches Google's list of AI assistants (named examples ChatGPT, Gemini, Claude; full list not published; Perplexity status reported inconsistently) [Official plus secondary, 2026-05] |
| Unassigned | Nothing matched |

AI Assistant channel caveats [Secondary, 2026]: not retroactive (data before 2026-05-13 keeps old classification); visits from native apps that strip the referrer stay in Direct; reported as session-scoped (user acquisition may not show it).

## 5. Custom channel group (recommended)

Create one custom channel group (Admin > Data display > Channel groups > Create new channel group) by copying the default and adding channels above the generic ones. Custom channel groups apply retroactively to historical data, which the default AI Assistant channel does not [Official behavior for custom groups].

| Order | Channel | Conditions |
|-------|---------|-----------|
| 1 | Paid AI Assistants | Source matches regex `(chatgpt|openai|perplexity|copilot)` and medium matches regex `^(.*cp.*|ppc|retargeting|paid.*)$` |
| 2 | AI Assistants | Source matches regex `(chatgpt\.com|chat\.openai\.com|openai|perplexity|gemini\.google|bard\.google|copilot\.microsoft|copilot\.cloud\.microsoft|claude\.ai|deepseek|chat\.mistral|mistral\.ai|meta\.ai|grok|you\.com|poe\.com|phind|kagi)` or medium exactly matches ai-assistant |
| 3 | Paid Social (split) | Optional per platform channels: Paid Meta, Paid TikTok, Paid LinkedIn (source regex per platform and paid medium regex) |
| 4 | QR and Print | Medium exactly matches qr or print |
| 5 | Remaining default channels | Default rules in default order |

Review the regex quarterly: add new assistants, and check sources that land in Referral with AI-like domains (BigQuery query below). Note that ChatGPT appends utm_source=chatgpt.com to many outbound links [Practitioner consensus], which helps attribution even without a referrer.

Hand off the channel definition and go-live date to ai-search-optimization so AI visibility reports use the same definition.

## 6. Detection queries

```sql
-- Referral and unassigned sources that look like AI assistants (last 30 days)
SELECT
  collected_traffic_source.manual_source AS src,
  collected_traffic_source.manual_medium AS med,
  COUNT(*) AS events
FROM `project.analytics_123456.events_*`
WHERE _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
                        AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
  AND event_name = 'session_start'
  AND REGEXP_CONTAINS(LOWER(IFNULL(collected_traffic_source.manual_source, '')),
      r'(gpt|openai|perplexity|gemini|copilot|claude|deepseek|mistral|grok|meta\.ai|poe|phind|kagi)')
GROUP BY 1, 2
ORDER BY events DESC;
```

```sql
-- UTM hygiene: mixed case, spaces and non-standard mediums (last 30 days)
SELECT
  collected_traffic_source.manual_source AS src,
  collected_traffic_source.manual_medium AS med,
  COUNT(*) AS sessions
FROM `project.analytics_123456.events_*`
WHERE _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
  AND event_name = 'session_start'
  AND collected_traffic_source.manual_medium IS NOT NULL
  AND (
    REGEXP_CONTAINS(collected_traffic_source.manual_source, r'[A-Z ]')
    OR REGEXP_CONTAINS(collected_traffic_source.manual_medium, r'[A-Z ]')
    OR NOT REGEXP_CONTAINS(collected_traffic_source.manual_medium,
      r'^(cpc|ppc|paid_social|paid.*|display|cpm|email|sms|push|affiliate|referral|social|organic|audio|qr|print|video)$')
  )
GROUP BY 1, 2
ORDER BY sessions DESC;
```

## 7. Redirects, link shorteners and parameter loss

| Cause | Symptom | Fix |
|-------|---------|-----|
| Server redirect drops query string (http to https, www, trailing slash, locale redirects) | Paid traffic shows as Direct, low click ID fill rate | Preserve query string in redirect rules; test every ad final URL |
| Shorteners and QR services that strip parameters | Unassigned or Direct | Use shorteners that keep parameters or encode UTMs in the destination |
| Single page apps rewriting URL before tags read it | Lost UTMs and click IDs | Capture parameters on first load before router replaces URL |
| Consent banner reload or redirect | Lost parameters | Do not redirect on consent |
| Checkout on another domain | Session breaks | Cross-domain linker |
| Safari Link Tracking Protection | gclid, fbclid and similar removed in Private Browsing and from Mail and Messages links | Rely on enhanced conversions and CAPI user data; UTMs are not stripped by that feature |

## 8. Governance workflow

1. UTM builder sheet with dropdowns for source and medium, regex validation, auto lowercase, generated final URL.
2. Channel agents request new values through the journal; measurement approves and adds to the vocabulary.
3. Weekly hygiene query (section 6); fix at source and log.
4. Quarterly review of channel group rules and AI assistant regex.
5. Document the taxonomy in MEASUREMENT.md (UTM governance row) with "Last verified" date.
