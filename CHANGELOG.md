# Changelog

All notable changes to HACF are documented here. Versioning follows the [three-layer model](docs/08-versioning-and-longevity.md): MAJOR = Core, MINOR = Indicators, PATCH = Examples.

## [0.1.0] — 2026-11-10 — Public Draft

### Added
- Core: ten design principles; six levels (L0–L5) with interaction modes and scope of impact; five dimensions (K, A, C, J, R); gate-based level assignment; evidence levels E1–E5 with level caps; flags (RISK-J, RISK-R, UNTAPPED, CEILING, EVIDENCE-CAP, PROVISIONAL).
- Indicators: 0–5 descriptors for each dimension; reference question bank; four practical tasks and portfolio review; enterprise metrics and engagement model.
- Examples: target role profiles; regulatory mapping (EU AI Act Art. 4, Kazakhstan AI Law, ISO/IEC 42001); crosswalk to DigComp 3.0, SFIA and others.
- Tools: reference scoring script (`tools/hacf_score.py`), machine-readable spec, synthetic sample data, unit tests.
- White paper, report templates, governance and contribution rules.
- Deterministic scoring rules (`assessment/scoring-rules.md`) and tool `tools/hacf_assess.py` converting raw instrument results into dimension scores; scenario answer key.
- Quick start (two-week pilot), assessor guide with calibration, pre-registered validation protocol, worked example, privacy-notice template, references.
- Continuous integration: unit tests, end-to-end sample run, and a consistency test that every example role profile produces its stated target level.

- Online self-check `app/index.html` (EN/RU), published via GitHub Pages: self-assessment and scenario check, provisional level capped at L2, risk flags, result download compatible with `tools/hacf_assess.py`. Scoring cross-checked against the Python reference on 302 random answer sets.

### Changed (before first release, after internal review)
- L5 gate for Creation lowered from C≥3 to C≥2: leaders must have built and documented their own AI workflows, not build for others. Resolves an inconsistency where the executive role profile could not reach its target level.
- Role profiles corrected so that the stated target level always follows from the gates (Legal C2, People manager C2, IT/security lead C4, Executive C2; oversight operator explicitly L2 + oversight profile).

### Known limitations
- Gate thresholds and descriptors are not yet empirically validated.
