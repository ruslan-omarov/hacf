# 04 · Enterprise Application

*Layer: Indicators. Practical guidance for organisations, consultants and HR/L&D teams.*

## 1. Two questions, two measurements

AI adoption fails in two ways: the organisation is not ready for capable people, or capable people are missing for a ready organisation. HACF measures the **people side** and pairs it with a lightweight **organisational enablement** check.

```
                     ORGANISATIONAL ENABLEMENT (low → high)
                   ┌──────────────────────┬──────────────────────┐
  PEOPLE      high │  FRUSTRATED TALENT   │   SCALING ENGINE     │
  CAPABILITY       │  shadow AI, attrition│   compounding value  │
  (HACF)           ├──────────────────────┼──────────────────────┤
              low  │  STANDING START      │   EXPENSIVE SHELFWARE│
                   │  awareness first     │   licences unused    │
                   └──────────────────────┴──────────────────────┘
```

### Organisational enablement check (6 areas, 1–4 each)

Inspired by perspectives common in cloud-provider AI adoption models (business, people, governance, platform, security, operations); simplified and vendor-neutral.

| Area | 1 — Envision | 2 — Experiment | 3 — Operate | 4 — Scale |
|---|---|---|---|---|
| Strategy & value | Ideas only | Pilots without metrics | Use cases with measured value | Portfolio managed for value |
| People & culture | No programme | Ad-hoc training | Role-based development | Capability is a managed asset |
| Governance | No policy | Draft policy | Policy, risk classification, owners | Automated, audited governance |
| Platform & data | Personal tools | Sanctioned tools | Integrated with corporate data | Shared, reusable platform |
| Security & privacy | Unmanaged | Basic rules | Controls and monitoring | Continuous assurance |
| Operations | None | Manual | Monitored solutions in production | Lifecycle management at scale |

## 2. Organisational metrics

| Metric | Definition | Why it matters |
|---|---|---|
| **HACF Index** (0–100) | mean level of assessed people ÷ 5 × 100 | One trend number for executives |
| **Level distribution** | % of people at L0…L5 | Shape of capability |
| **Role coverage** | % of people meeting their role's target profile | Gap to business need |
| **Risk exposure** | % of people with `RISK-J` or `RISK-R` | Where incidents will come from |
| **Untapped potential** | % with `UNTAPPED` | Cheapest wins |
| **Builder density** | L4+ per 100 employees | Capacity to create solutions internally |
| **Champion ratio** | L3+ per team | Peer support availability |
| **Evidence quality** | % of results at E3+ | How much to trust the picture |

**Reading the distribution.** A typical early organisation has most people at L0–L2, few L3, almost no L4. Healthy targets vary by industry, but a useful rule of thumb is **at least one L3 per team and one L4 per 50–100 employees** before scaling AI solutions broadly. These are working hypotheses for validation, not norms.

## 3. Engagement model (8–12 weeks)

| Phase | Weeks | Activities | Outputs |
|---|---|---|---|
| 0. Mobilise | 1 | Sponsor, scope, data-protection setup, communication | Charter, privacy notice |
| 1. Baseline | 2–4 | Org enablement check; self-assessment + scenario check for all | Provisional profiles, Index |
| 2. Deep-dive | 4–7 | Practical tasks for L2+ candidates; artefact reviews for L3+ | Validated profiles |
| 3. Targets | 6–8 | Define target profiles per role with business owners | Role profile catalogue |
| 4. Analyse | 8–9 | Gap, risk and heat maps; identify Champions and Builders | Capability map |
| 5. Roadmap | 9–12 | Development plan linked to AI use-case pipeline | 6–12-month roadmap |
| 6. Re-measure | +6–12 months | Repeat assessment | Progress, ROI evidence |

## 4. The heat map

Rows: departments. Columns: dimensions and flags. Cells: mean score, with groups under 5 people suppressed.

```
Department    n   K    A    C    J    R   L3+  RISK  Index
Finance      42  2.6  2.9  1.4  2.8  3.1  19%   7%    46
Sales        65  1.9  3.2  1.1  1.7  1.8   6%  38%    31   ← risk hotspot
IT           30  3.4  3.1  3.0  3.0  2.9  43%  10%    58
HR           18  2.0  1.6  0.8  2.2  2.6   0%   0%    27   ← untapped
```

## 5. From gaps to roadmap

| Situation | Intervention | Typical duration |
|---|---|---|
| Many L0–L1 | Mandatory awareness + rules (K1, J1, R1) | 2–4 h per person |
| L2 with `RISK-J`/`RISK-R` | Verification and data-handling training **before** wider tool rollout | 1 day |
| `UNTAPPED` | Role-specific workflow clinics | 2–3 sessions |
| L2 → L3 | Practice programme: redesign 2 real workflows, measured | 6–8 weeks |
| L3 → L4 | Builder track: automation/agent design, testing, permissions | 8–12 weeks + project |
| Few L5 | Executive programme: strategy, portfolio, governance | 3–5 days + coaching |

**Link capability to use cases.** Every planned AI use case should name the levels it needs: e.g. "Contract review agent — needs 1×L4 builder, 3×L3 legal practitioners with J≥3, all users L2 with R≥2". This turns the roadmap into a staffing plan.

## 6. Measuring return

HACF does not claim a fixed ROI. It provides the before/after structure:

1. Baseline: profiles + selected process metrics (time, quality, error rate, cost).
2. Intervention: development activities and use cases.
3. Re-measure: profiles + same process metrics.
4. Attribute carefully: compare trained vs. not-yet-trained groups where possible.

## 7. What not to do

- Do not rank individuals publicly or tie results directly to pay in the first cycle.
- Do not report a single Index without distribution and risk.
- Do not use self-assessment results as validated levels.
- Do not equate tool licences with capability.
