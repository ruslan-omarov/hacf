# 03 · Assessment Method

*Layer: Core (gates, evidence logic, flags) + Indicators (thresholds). The reference implementation is [`tools/hacf_score.py`](../tools/hacf_score.py).*

## 1. Inputs

For each person the assessment produces:

| Input | Values |
|---|---|
| Dimension scores | K, A, C, J, R — integers 0–5 |
| Evidence level | E1–E5 (strongest evidence actually obtained) |
| Scope of impact | Self, Team, Organisation, Ecosystem |
| Role (optional) | Used to compare with a target role profile |

## 2. Evidence levels

| Code | Evidence type | What it is | Reliability |
|---|---|---|---|
| **E1** | Self-declaration | Self-assessment questionnaire | Low |
| **E2** | Knowledge check | Scored scenario-based questions | Medium for K, J, R; low for A, C |
| **E3** | Practical task | Timed task with AI, scored by rubric | Good |
| **E4** | Work artefact | Real workflow, solution or decision record, validated by an assessor or manager | High |
| **E5** | Sustained outcome | Measured business outcome over ≥ 3 months, or external recognition | Highest |

**Evidence caps the reportable level:**

| Strongest evidence | Highest level that can be reported |
|---|---|
| E1 | L2 (marked *provisional*) |
| E2 | L2 |
| E3 | L3 |
| E4 or E5 | L5 |

A self-assessment alone can never produce L3+. This is deliberate (Principle P7).

## 3. Gates

<a id="gates"></a>
The level is the **highest level whose gates are all satisfied**. It is *not* an average.

| Level | K | A | C | J | R | Evidence | Scope |
|---|---|---|---|---|---|---|---|
| L1 Aware | ≥1 | – | – | ≥1 | ≥1 | E1 | any |
| L2 User | ≥2 | ≥2 | – | ≥2 | ≥2 | E1 | any |
| L3 Practitioner | ≥2 | ≥3 | ≥2 | ≥3 | ≥3 | E3 | any |
| L4 Builder | ≥3 | ≥3 | ≥4 | ≥3 | ≥3 | E4 | ≥ Team |
| L5 Leader | ≥3 | ≥3 | ≥2 | ≥4 | ≥4 | E4 | ≥ Organisation |

Note that L4 and L5 are deliberately not nested: L4 demands building depth (C≥4), L5 demands judgment, responsibility and organisational scope (J≥4, R≥4). A person may meet L5 without meeting L4. The algorithm checks from L5 downward and returns the first level fully satisfied. Dimension scores for each instrument are computed by the deterministic rules in [assessment/scoring-rules.md](../assessment/scoring-rules.md).

**Why gates instead of averages?** With averages, K2 A5 C4 J1 R1 (a productive but dangerous user) would score as a practitioner. With gates, this person is L1 with two risk flags — which is the truth an organisation needs.

## 4. Flags

Flags are reported alongside the level. They are often more actionable than the level itself.

| Flag | Rule | Meaning |
|---|---|---|
| `RISK-J` | A − J ≥ 2 | Uses AI beyond ability to verify it |
| `RISK-R` | max(A, C) − R ≥ 2 | Uses or builds beyond ability to do it safely |
| `UNTAPPED` | K − A ≥ 2 | Understands AI but does not apply it — quick-win candidate |
| `CEILING` | all gates of next level met except one dimension | One targeted development step away from next level |
| `EVIDENCE-CAP` | a higher level's gates and scope are met, but evidence is too weak | Collect stronger evidence (practical task or artefact) — likely a higher level |
| `PROVISIONAL` | evidence = E1 | Result based on self-report only |

## 5. Assessment instruments

| Instrument | Duration | Measures | Evidence | Where |
|---|---|---|---|---|
| Self-assessment | 10 min | all, roughly | E1 | [assessment/question-bank.md §A](../assessment/question-bank.md) |
| Scenario knowledge check | 20–25 min | K, J, R | E2 | [§B](../assessment/question-bank.md) |
| Practical task | 45–90 min | A, J, R (+C) | E3 | [assessment/practical-tasks.md](../assessment/practical-tasks.md) |
| Artefact review | 30–60 min per person | A, C, J, R | E4 | [practical-tasks.md §Portfolio](../assessment/practical-tasks.md#portfolio-review-e4) |
| Outcome review | periodic | A, scope | E5 | manager + metrics |

**Recommended funnel for organisations:** everyone takes self-assessment + scenario check; people who reach provisional L2 with A≥2 take the practical task; L3 candidates who build for others submit artefacts.

## 6. Scoring each dimension

Each instrument item maps to one or more dimensions. Final dimension score = assessor judgment guided by:

1. The **highest descriptor level** for which the person shows consistent evidence (not a single lucky answer).
2. If instruments disagree, the **stronger evidence wins** (E4 > E3 > E2 > E1).
3. Self-assessment can raise nothing above the score supported by the strongest objective instrument for that dimension, except where no objective instrument covered the dimension — then the self-score stands, and `PROVISIONAL` is set.

## 7. Reliability and fairness requirements

- **Two-assessor rule** for any L4/L5 decision, or calibration on a shared sample of at least 10 cases per assessor.
- **Language and accessibility:** tasks are offered in the participant's working language; time limits are adjusted for documented needs.
- **No tool-brand bias:** participants may use any approved AI tool; scoring ignores which tool was used.
- **Re-assessment:** every 12 months, or after significant role change. Levels decay if not evidenced: a score older than 24 months is reported as `EXPIRED`.

## 8. Data protection

Individual results are personal data. Organisations must define purpose, legal basis, access rights and retention before assessment, inform participants, and report aggregated results to management with groups smaller than **5 people suppressed**.
