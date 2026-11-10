# 11 · Validation Protocol

*Layer: Core (method of evidence). How HACF moves from v0.1 (expert-designed hypotheses) to v1.0 (validated thresholds).*

HACF v0.1 is an expert-designed framework. Its thresholds are **hypotheses**. This protocol states in advance what evidence will confirm, change or reject them, so that later changes are traceable rather than arbitrary.

## Pilot requirements

- At least **3 organisations**, from at least **2 industries**, **≥ 150 participants** in total.
- Each pilot uses self-assessment, scenario check, and at least one practical task for ≥ 30% of participants.
- 20% of practical tasks double-scored.
- Outcome data collected 3–6 months later for a subsample: AI-related incidents, measured time or quality gains on AI-supported work, manager rating of AI effectiveness.
- Only anonymised, aggregated data leaves the organisation unless participants give explicit consent.

## Questions and decision rules (pre-registered)

| # | Question | Method | Decision rule |
|---|---|---|---|
| V1 | Are the five dimensions distinct? | Correlations, confirmatory factor analysis | If two dimensions correlate > 0.85 across pilots, merge or redefine them |
| V2 | Is scoring reliable? | Weighted κ / ICC on double-scored tasks | Target ≥ 0.70; below 0.60 → rewrite rubric anchors |
| V3 | Do flags predict risk? | Compare incident rates for `RISK-J`/`RISK-R` vs. others | If no difference after two pilots, revise flag rules |
| V4 | Do levels predict outcomes? | Ordinal association between level and outcome measures | Monotonic trend expected; if absent, review gates |
| V5 | Are gates placed well? | Distribution of scores at each gate; ROC against outcomes | Move a threshold by at most one point per version, with evidence |
| V6 | Is the self-assessment biased? | Self vs. objective scores by group | Report bias; adjust self-assessment mapping |
| V7 | Is it fair? | Differential item functioning by language, gender, age group | Remove or rewrite items with substantial DIF |

## Publication

Results are published as aggregated reports in `research/` and summarised in the CHANGELOG. Negative results are published too.
