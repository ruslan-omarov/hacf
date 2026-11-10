# 09 · Quick Start — a two-week pilot

*Layer: Examples. For an HR/L&D lead, consultant or manager running HACF for the first time with one team (10–40 people).*

## What you need

- A sponsor (head of the team or HR) and one or two assessors.
- This repository: question bank, practical task T1, `tools/`.
- A completed [privacy notice](../templates/privacy-notice.md).
- Python 3.11+ on one laptop (no other software).

## Day-by-day

| Day | Step | Output |
|---|---|---|
| 1 | Agree purpose with the sponsor: **development, not evaluation of performance**. Pick role profiles from [05](05-role-profiles.md) and adjust. | One-page charter |
| 2 | Send the privacy notice and invitation. Explain why: the goal is to target training and reduce AI risk. | Informed participants |
| 3–5 | Everyone completes self-assessment §A and scenario check §B (35 min, any survey tool). Export answers. | Raw answers |
| 6 | Prepare task T1 materials from your own domain, with the planted defects described in [practical-tasks.md](../assessment/practical-tasks.md). | Task pack |
| 7–9 | Participants with provisional A≥2 take T1 (60 min). Score with the rubric; double-score 20% for calibration ([assessor guide](10-assessor-guide.md)). | Rubric scores |
| 10 | Put raw results into the JSON format of `tools/sample/raw_results.json`. Run: `python tools/hacf_assess.py raw.json --out people.csv` then `python tools/hacf_score.py people.csv --roles tools/sample/role_profiles.json --out report.md --results results.csv` | Profiles and team report |
| 11 | Write individual reports with [the template](../templates/individual-report.md); share each one privately. | Personal development plans |
| 12 | Present the team report (aggregates only, groups ≥ 5) to the sponsor. Decide 2–3 interventions. | Decisions |
| 13–14 | Collect feedback from participants and the sponsor. Optional: submit an anonymised [pilot report](../.github/ISSUE_TEMPLATE/pilot-report.md). | Lessons learned |

## Typical first findings

- A cluster of `RISK-J`/`RISK-R` in customer-facing or sales roles → verification and data-handling training **before** extending tool access.
- `UNTAPPED` specialists → workflow clinics, fastest return.
- `CEILING` and `EVIDENCE-CAP` people → candidates for AI Champions; collect artefacts to confirm L3/L4.

## Success criteria for the pilot

Participants find their individual report fair (target ≥ 70% agreement), the sponsor takes at least one decision based on the report, and double-scored tasks agree within one point on ≥ 80% of dimensions.
