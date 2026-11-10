# HACF White Paper
## Measuring Human Capability in the Age of Artificial Intelligence

**Ruslan Omarov** · Version 0.1.0 (Public Draft) · November 2026 · CC BY 4.0

---

### Abstract

Organisations are buying AI faster than they are building the human capability to use it. Existing instruments either measure general digital competence of citizens, knowledge of a specific vendor's services, or the technical readiness of the organisation. None directly answers the operational question a business faces: *what can our people actually achieve with AI, how safely, and what should we develop next?* The Human–AI Capability Framework (HACF) proposes a vendor-neutral model with six levels defined by the person's relationship to AI (observe, ask, collaborate, delegate and orchestrate, govern), five independently scored dimensions (Knowledge, Application, Creation, Judgment, Responsibility), gate-based level assignment in which judgment and responsibility are mandatory, evidence-weighted scoring, and a three-layer versioning model intended to keep the core valid across technology generations. This paper sets out the rationale, design decisions, enterprise use, limitations and research agenda.

---

### 1. The problem

Three gaps motivate HACF.

**The licence fallacy.** Counting licences, logins or prompts measures access and activity, not capability. Two employees with identical usage can differ tenfold in value created — and in risk.

**The averaging fallacy.** Composite scores hide dangerous profiles. A highly productive user who never verifies output and pastes client data into unapproved tools can average out as "advanced".

**The obsolescence trap.** Frameworks written around today's techniques (specific prompting methods, specific products) age within one or two technology cycles. Organisations then rebuild competency models every few years and lose comparability over time.

### 2. Design choices

| Choice | Alternative rejected | Reason |
|---|---|---|
| Levels defined by **interaction mode** | Levels defined by tools or techniques | Modes persist as AI evolves from assistants to agents to autonomous systems |
| **Five dimensions** reported separately | Single score | Profiles drive decisions; single scores hide risk |
| **Gates** with J and R mandatory | Averages | Capability without control is risk |
| **Evidence caps** levels | Self-assessment as result | Self-report is weak evidence, especially at higher levels |
| **Scope of impact** for L4–L5 | Pure skill tests | Building and leading are defined by effect on others |
| **Three layers** with different change rates | Single document revised at once | Longevity and comparability over decades |
| **Open licence** (CC BY 4.0) | Proprietary | Adoption, scrutiny and improvement by a community |

### 3. The model

Summarised in the [README](README.md); normative descriptions in [docs/01-levels.md](docs/01-levels.md), [docs/02-dimensions.md](docs/02-dimensions.md) and [docs/03-assessment-method.md](docs/03-assessment-method.md).

A key conceptual claim: **as AI capability grows, the centre of human capability moves from doing to directing and verifying.** The dimensions J (Judgment) and R (Responsibility) therefore become more important over time, not less. HACF encodes this by gating every level on them.

### 4. Relation to existing work

HACF builds on and interoperates with the European Digital Competence Framework (DigComp 3.0), which integrates AI competence across its 21 competences and four proficiency levels; with professional skills frameworks such as SFIA; with workplace AI-literacy frameworks that differentiate baseline, operational and oversight duties; with regional literacy frameworks such as ASEAN's; and with organisational AI maturity models. See [docs/07-crosswalk.md](docs/07-crosswalk.md). HACF's distinct contribution is the combination of workplace value creation, building, gated judgment and responsibility, evidence weighting, and an explicit longevity design.

### 5. Enterprise use

HACF is paired with a six-area organisational enablement check, producing a two-axis view (people capability × organisational enablement) and metrics such as the HACF Index, role coverage, risk exposure and builder density. It links capability to the AI use-case pipeline, turning a roadmap into a staffing and development plan. See [docs/04-enterprise.md](docs/04-enterprise.md).

It also supports documentation of AI-literacy measures expected under the EU AI Act (Article 4, as amended in 2026), Kazakhstan's Law "On Artificial Intelligence", and the competence clause of ISO/IEC 42001 — without claiming to guarantee compliance. See [docs/06-regulatory-mapping.md](docs/06-regulatory-mapping.md).

### 6. Limitations

- **Thresholds are hypotheses.** Gate values and descriptor boundaries in v0.1 are expert-designed and not yet empirically validated.
- **Assessor dependence.** E3–E5 evidence requires trained assessors; reliability must be demonstrated.
- **Context dependence.** The same score may mean different things across industries and cultures; industry profiles are planned.
- **Measurement effects.** Once a level matters for careers, people optimise for it. Rotated private item banks and artefact-based evidence mitigate but do not eliminate this.
- **Ethical risk.** Capability data can be misused for surveillance or unfair decisions. Principle P9 and the data-protection rules in the method are binding parts of the framework.

### 7. Research agenda

1. **Construct validity:** do the five dimensions separate empirically (factor analysis on pilot data)?
2. **Predictive validity:** do levels and flags predict outcomes — productivity gains, quality, AI-related incidents?
3. **Reliability:** inter-rater agreement for E3/E4 scoring (target: weighted κ ≥ 0.7).
4. **Threshold calibration:** are gates set at points that discriminate meaningfully?
5. **Fairness:** do results differ by language, age, gender or region beyond true capability differences?
6. **Longitudinal stability:** does the core remain discriminative as AI systems become more autonomous?

Organisations and researchers are invited to run pilots and contribute anonymised, aggregated findings ([CONTRIBUTING.md](CONTRIBUTING.md)).

### 8. Conclusion

Access to AI is converging; capability to use it well is diverging. Measuring that capability honestly — with judgment and responsibility at the centre and evidence behind every claim — is a precondition for investing in people as wisely as in technology. HACF is offered as an open starting point for that work.

---

*Cite as:* Omarov, R. (2026). *HACF — Human–AI Capability Framework* (Version 0.1.0). Zenodo. https://doi.org/10.5281/zenodo.24108829
