# Marketing Mix Modeling (MMM)

MMM estimates how each channel (paid, owned, offline) and non-marketing factors (price, promotions, seasonality, distribution) drive a business KPI using aggregated time series. It needs no user-level tracking, so consent and browser loss do not break it, but it needs history, spend variation and calibration. This module covers readiness, data, open-source tools, calibration, validation and using outputs.

## 1. Readiness checklist

Recommend an MMM only when most of these are true:

| # | Criterion | Why |
|---|-----------|-----|
| 1 | At least 2 years of weekly data (absolute minimum about 18 months, 78 weeks) | Seasonality and enough observations per parameter |
| 2 | 3 or more channels with meaningful spend (each at least about 5% of total) | Otherwise a simpler analysis answers the question |
| 3 | Spend varied over time (flights, tests, launches, pauses) | No variation, no identification |
| 4 | Stable KPI definition and reliable backend data for the whole period | Garbage in, garbage out |
| 5 | Known non-marketing drivers documented (price changes, promotions, stock-outs, distribution, competitor events, macro shocks) | Omitted variables bias channel effects |
| 6 | At least one incrementality test to calibrate or validate | Prevents plausible but wrong models |
| 7 | Spend at Scale tier or above (roughly $30k per month plus across channels; more channels need more data) | Cost and value of the exercise |
| 8 | A decision the model will inform (annual plan, quarterly reallocation) | Otherwise it is a report nobody uses |

Not ready? Use: blended MER and aMER trends, geo tests on the top channel, simple regression of weekly KPI on spend with seasonality controls as a sanity check (label as exploratory).

## 2. Data specification

Weekly (or daily aggregated to weekly) rows. National or by geo (geo-level models such as Meridian's hierarchical geo model use more information and usually give tighter estimates).

| Column | Description |
|--------|-------------|
| date (week start) | Consistent week definition |
| geo (optional) | Region code with population |
| kpi | Orders, new customers, revenue, qualified leads (from backend) |
| revenue_per_kpi (if kpi is not revenue) | To convert to ROI |
| <channel>_spend | Spend per channel (split large channels by role: Meta cold acquisition vs retargeting, Google brand vs non-brand vs PMax) |
| <channel>_impressions or reach and frequency | Media exposure (Meridian supports reach and frequency inputs) |
| organic and owned | Email sends, organic sessions (treat carefully, can be mediators), PR events |
| controls | Price index, discount depth, promotions flag, stock availability, holidays, competitor activity, search demand for the category (Meridian commonly uses Google Query Volume for brand or category queries) |
| macro | Inflation, FX (for Turkey and other high inflation markets use real terms or include price index) |

Data rules: consistent currency (and real vs nominal in high inflation markets), no gaps, spend dated when it ran (not when billed), channels defined the same way across history, outliers explained (COVID, site outage) with dummies.

## 3. Open-source tools

| Tool | Owner | Method | Strengths | Watch outs |
|------|-------|--------|-----------|-----------|
| Meridian | Google (open source; generally available January 2025) | Bayesian, hierarchical geo-level, adstock and Hill saturation, reach and frequency, ROI priors, experiment calibration, budget optimizer | Geo hierarchy, priors on ROI calibrated by experiments, Google support ecosystem and partners | Python and compute (GPU helps); priors drive results when data are weak |
| Robyn | Meta (open source) | Ridge regression with adstock and saturation, multi-objective hyperparameter search (fit, decomposition distance, lift calibration error), budget allocator | Many candidate models, calibration with lift tests, mature community | R first (Python port available); choosing among Pareto models needs judgment |
| PyMC-Marketing | PyMC Labs (open source) | Bayesian MMM with adstock and saturation, time-varying parameters, lift test calibration, plus CLV models | Flexible, full Bayesian workflow in Python, customer lifetime value module | Requires modeling skill; API evolves quickly |

Commercial options (Recast, Lifesight, Measured, Haus and others) add managed data pipelines, calibration workflows and planning interfaces. Evaluate method transparency and how they incorporate experiments.

## 4. Meridian workflow (skeleton)

Illustrative; check the Meridian documentation for current module paths and arguments before running.

```python
from meridian.data import load
from meridian.model import model, spec, prior_distribution
from meridian.analysis import analyzer, optimizer

coord = load.CoordToColumns(
    time="week", geo="geo", kpi="orders", revenue_per_kpi="aov",
    population="population",
    controls=["price_index", "promo_flag", "gqv_brand"],
    media=["meta_impr", "google_nonbrand_impr", "tiktok_impr", "youtube_impr"],
    media_spend=["meta_spend", "google_nonbrand_spend", "tiktok_spend", "youtube_spend"],
)
loader = load.CsvDataLoader(
    csv_path="mmm_weekly_geo.csv", kpi_type="non_revenue", coord_to_columns=coord,
    media_to_channel={"meta_impr": "meta", "google_nonbrand_impr": "google_nb",
                      "tiktok_impr": "tiktok", "youtube_impr": "youtube"},
    media_spend_to_channel={"meta_spend": "meta", "google_nonbrand_spend": "google_nb",
                            "tiktok_spend": "tiktok", "youtube_spend": "youtube"},
)
data = loader.load()

# ROI priors: center channels with experiment evidence on the measured iROAS
prior = prior_distribution.PriorDistribution()  # set roi_m per channel from tests
mmm = model.Meridian(input_data=data, model_spec=spec.ModelSpec(prior=prior))
mmm.sample_prior(500)
mmm.sample_posterior(n_chains=4, n_adapt=500, n_burnin=500, n_keep=1000)

summary = analyzer.Analyzer(mmm)          # ROI, mROI, contributions, diagnostics
budget = optimizer.BudgetOptimizer(mmm).optimize()  # constrained reallocation
```

## 5. Robyn workflow (outline)

1. `robyn_inputs()`: data, dependent variable, paid media spends and exposures, context variables, organic variables, adstock type (geometric or Weibull), hyperparameter ranges, `calibration_input` with lift test results (channel, start date, end date, lift absolute, metric).
2. `robyn_run()`: iterations and trials (for example 2,000 iterations x 5 trials).
3. `robyn_outputs()`: Pareto-optimal models; pick by fit (NRMSE), business plausibility (DECOMP.RSSD) and calibration error (MAPE.LIFT).
4. `robyn_allocator()`: budget scenarios with channel constraints.
5. Refresh with `robyn_refresh()` as new weeks arrive.

## 6. PyMC-Marketing workflow (outline)

```python
# Illustrative; class names and import paths change between versions
from pymc_marketing.mmm import MMM, GeometricAdstock, LogisticSaturation

mmm = MMM(
    date_column="week",
    channel_columns=["meta_spend", "google_nb_spend", "tiktok_spend", "youtube_spend"],
    control_columns=["price_index", "promo_flag"],
    adstock=GeometricAdstock(l_max=8),
    saturation=LogisticSaturation(),
    yearly_seasonality=2,
)
mmm.fit(X, y)                       # X: dataframe with date, channels, controls; y: KPI
# mmm.add_lift_test_measurements(lift_df)  # calibrate with experiment results, then refit
```

## 7. Calibration with experiments

1. Run a geo or lift test on the channel (see [Incrementality](incrementality-testing.md)).
2. Express the result in the model's terms (incremental KPI over the test period at the tested spend level, or ROI).
3. Feed it in: Meridian ROI priors centered on the measured value with an uncertainty that reflects the test interval; Robyn `calibration_input`; PyMC-Marketing lift test measurements.
4. Check that the calibrated model still fits the holdout period and that other channels' estimates did not swing implausibly.
5. Plan the next test where the model's uncertainty is widest and spend is largest.

## 8. Validation

| Check | Pass condition |
|-------|----------------|
| Out-of-sample fit | Holdout of last 8 to 13 weeks: MAPE acceptable for the business (often under 10% to 15% weekly for stable KPIs) [Practitioner consensus] |
| Posterior predictive checks (Bayesian) | Simulated KPI resembles actual distribution |
| Convergence | R-hat near 1.0, enough effective samples, no divergences |
| Decomposition plausibility | Baseline share sensible (most businesses have a large base); no channel with impossible ROI |
| Stability | Refit on a shifted window: channel ROI ranks and magnitudes do not swing wildly |
| Agreement with experiments | Calibrated channels within test intervals; uncalibrated channels flagged |
| Sensitivity to priors | Results reported with prior sensitivity notes |

## 9. Using outputs

| Output | Use | Guardrail |
|--------|-----|-----------|
| ROI and contribution by channel | Explain past performance | Show intervals, not points |
| Marginal ROI (mROI) and response curves | Where the next dollar goes | Act on mROI, not average ROI |
| Adstock and lag | Expected delay of effects | Inform test cooldowns and pacing |
| Budget optimizer scenarios | Quarterly allocation | Move at most about 20% to 30% of a channel's budget per quarter, verify with a test where the move is large |
| Saturation points | Cap channels near saturation | Recheck after creative or market changes |

Turn outputs into: an allocation proposal for growth-orchestrator, updated incrementality factors or target CPAs per channel for channel agents, and a test plan for the most uncertain high-spend channels.

## 10. Cadence and ownership

- Build: 4 to 8 weeks for a first model including data work.
- Refresh: monthly or quarterly with new data; full re-specification annually.
- Document every model version: data range, variables, priors, calibration inputs, diagnostics, results, decisions taken. Save summaries to `ads-master/outputs/measurement/`.

## 11. Pitfalls

| Pitfall | Result | Prevention |
|---------|--------|-----------|
| Collinear channels (all scaled together) | Unidentifiable effects | Plan spend variation and geo tests |
| Including mediators as controls (branded search, organic traffic) | Steals credit from upstream media | Model them carefully or exclude; document choice |
| Revenue in nominal terms in high inflation markets | Spurious trends | Deflate or include price index |
| Treating priors as neutral | Prior dominates weak data | Report prior vs posterior; calibrate with tests |
| Reallocating on average ROI | Overinvesting in saturated channels | Use marginal ROI |
| One model, never refreshed | Stale decisions | Scheduled refresh |
