# Creative Library

Every creative gets a stable ID before it runs, so performance can be tied back to its angle, hook, format and learning. `registry.csv` is the index; files live wherever your team keeps assets (link them in `asset_url`).

ID format: the ad name grammar owned by the creative-strategy agent (`skills/creative-strategy/references/briefs-and-naming-conventions.md`), for example `20261008_C021_hcause_runner_prob_ugc_H03_cr07_30s_916_v2_wl`. video-studio names files the same way (without the launch date) and validates names before delivery. The same name goes into the ad name and `utm_content`, so platform data, backend data and this registry join on one key.

Columns: creative_id, created_date, launch_date, status (draft, approved, live, paused, retired), angle, concept, hook, format, ratio, duration_s, product_or_offer, creator, ai_generated (yes or no), disclosure_label, claims_review (approved, needs review), asset_url, primary_text, headline, landing_page, channel, spend, impressions, clicks, ctr, cpa, roas_or_value, hook_rate, hold_rate, result_summary, learning, next_action.

Rule: a learning explains what happened, why it might have happened and what to test next. "Winner" or "loser" alone is not a learning.
