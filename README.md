# HACF — Human–AI Capability Framework

**An open, vendor-neutral framework for measuring and developing what people can actually do with artificial intelligence — built for business use and designed to stay valid for decades.**

[![Version](https://img.shields.io/badge/version-0.1.0--public--draft-blue)](CHANGELOG.md)
[![License: CC BY 4.0](https://img.shields.io/badge/framework-CC%20BY%204.0-lightgrey)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/tools-MIT-green)](LICENSE-CODE)

> Access to AI is becoming a commodity. The ability to use, direct, build and govern it is not.
> **Human capability × AI capability = professional advantage.**

🇷🇺 [Русская версия](README.ru.md)

---

## Why HACF exists

Most organisations now pay for AI tools. Very few can answer simple questions:

- How many of our people can use AI *well* — and how many use it *riskily*?
- Who can redesign a process with AI, and who only generates text?
- Who can build and safely operate an AI agent?
- Which teams are ready for the next AI project, and what training gives the highest return?

Existing frameworks (DigComp 3.0, SFIA, vendor certifications, organisational maturity models) are valuable but answer different questions: citizen digital competence, professional skills in general, knowledge of one vendor's products, or an organisation's technical readiness. **HACF measures the individual's capability to create value with AI, safely, in a work context — and aggregates it into a decision-ready picture for the organisation.**

## The model in one page

### Six levels — defined by the human's relationship to AI, not by tools

| Level | Name | The person… | Typical interaction mode |
|---|---|---|---|
| **L0** | Unaware | does not use AI deliberately | — |
| **L1** | Aware | understands what AI can and cannot do, and the rules | Observe |
| **L2** | User | uses AI regularly for own tasks and checks the output | Ask |
| **L3** | Practitioner | redesigns own professional work around AI, repeatably | Collaborate |
| **L4** | Builder | creates AI solutions — workflows, agents, integrations — for others | Delegate & Orchestrate |
| **L5** | Leader | decides how AI changes the work of a team, organisation or sector | Govern |

### Five dimensions — scored 0–5 each

| Code | Dimension | Question it answers |
|---|---|---|
| **K** | Knowledge | Does the person understand how AI works, where it fails, and why? |
| **A** | Application | Does the person get real work outcomes with AI? |
| **C** | Creation | Can the person build reusable AI solutions? |
| **J** | Judgment | Does the person verify, detect errors, and know when *not* to use AI? |
| **R** | Responsibility | Does the person handle data, security, law, ethics and accountability correctly? |

### The profile notation

Every assessed person receives a level **and** a profile:

```
HACF L3 [K3 · A4 · C2 · J3 · R3]  evidence: E3  scope: Team
```

### Three rules that make HACF different

1. **Judgment and Responsibility are gates.** Nobody reaches L3+ by usage alone. High application with low judgment is flagged as *risk*, not as *skill* ([details](docs/03-assessment-method.md#gates)).
2. **Level ≠ job title.** An analyst can be L4; a CIO can be L2. Levels describe capability, not hierarchy.
3. **Built to outlive tools.** The framework has three layers with different change rates: a **Core** that is stable for decades, **Indicators** reviewed yearly, and **Examples** that change as fast as the technology ([details](docs/08-versioning-and-longevity.md)).

## For businesses: what you get

| Deliverable | Description |
|---|---|
| Individual profiles | Level + five-dimension profile + evidence quality for every participant |
| Organisational HACF Index | Distribution of levels by department, role and location |
| Capability gap map | Actual profiles vs. **target role profiles** |
| Risk map | Where AI usage outruns judgment and responsibility |
| Compliance evidence | Documented AI-literacy measures (EU AI Act Art. 4, Kazakhstan AI Law, ISO/IEC 42001 competence) |
| Development roadmap | Who to train, in what, in which order; candidates for AI Champions and Builders |

See [Enterprise application](docs/04-enterprise.md) and the [scoring tool](tools/).

## Repository map

| Path | Content |
|---|---|
| [WHITEPAPER.md](WHITEPAPER.md) | Rationale, design choices and research agenda |
| [docs/00-principles.md](docs/00-principles.md) | Ten design principles |
| [docs/01-levels.md](docs/01-levels.md) | Normative description of L0–L5 |
| [docs/02-dimensions.md](docs/02-dimensions.md) | K, A, C, J, R with 0–5 descriptors |
| [docs/03-assessment-method.md](docs/03-assessment-method.md) | Evidence, gates, scoring, flags |
| [docs/04-enterprise.md](docs/04-enterprise.md) | Organisation-wide assessment and roadmap |
| [docs/05-role-profiles.md](docs/05-role-profiles.md) | Target profiles for typical roles |
| [docs/06-regulatory-mapping.md](docs/06-regulatory-mapping.md) | EU AI Act, Kazakhstan, ISO/IEC 42001 |
| [docs/07-crosswalk.md](docs/07-crosswalk.md) | Mapping to DigComp, SFIA, AWS and others |
| [docs/08-versioning-and-longevity.md](docs/08-versioning-and-longevity.md) | How HACF stays valid for decades |
| [docs/glossary.md](docs/glossary.md) | Terms |
| [assessment/](assessment/) | Question bank, practical tasks, machine-readable spec |
| [tools/](tools/) | Open-source scoring script with sample data |
| [templates/](templates/) | Individual and enterprise report templates |

## Status

**v0.1.0 — Public Draft.** The structure is complete; indicators and thresholds are hypotheses awaiting empirical validation. Organisations piloting HACF are invited to share anonymised results — see [CONTRIBUTING.md](CONTRIBUTING.md) and the [research agenda](WHITEPAPER.md#7-research-agenda).

HACF is **not** a certification and **not** a legal compliance guarantee. It is an open methodology.

## How to cite

See [CITATION.cff](CITATION.cff). Suggested form:

> Omarov, R. (2026). *HACF — Human–AI Capability Framework* (Version 0.1.0) [Framework]. https://github.com/ruslan-omarov/hacf

## License

- Framework text, levels, descriptors and templates: **[CC BY 4.0](LICENSE)** — free to use, adapt and use commercially **with attribution**.
- Code in `tools/`: **[MIT](LICENSE-CODE)**.
- The name "HACF" and "Human–AI Capability Framework" identify this project; derivative works must not imply endorsement — see [GOVERNANCE.md](GOVERNANCE.md#name-and-marks).

## Author

**Ruslan Omarov** — author and maintainer. Contributions are welcome under the [governance model](GOVERNANCE.md).
