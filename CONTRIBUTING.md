# Contributing to HACF

Thank you for helping build an open standard for human capability in the age of AI.

## Ways to contribute

1. **Feedback** — open an issue: unclear wording, missing indicators, examples from your industry.
2. **Translations** — Russian, Kazakh and other languages (`i18n/<lang>/`).
3. **Industry profiles** — target role profiles and practical tasks for banking, energy, telecom, retail, public sector, education, healthcare.
4. **Assessment items** — new scenario items following the blueprint in `assessment/question-bank.md §C`. *Do not submit items from live private banks.*
5. **Pilot data** — share anonymised, aggregated results (distributions, flags, reliability statistics). Never share personal data. Groups under 5 must be suppressed.
6. **Code** — improvements to `tools/` with tests.

## Rules

- State which **layer** your change affects (Core / Indicators / Examples).
- Keep the framework **vendor-neutral**: product names only in clearly marked non-normative examples.
- Cite sources for regulatory or research claims.
- By contributing, you agree your contribution is licensed under CC BY 4.0 (documentation) or MIT (code), and that you have the right to contribute it.
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Pull requests

1. Fork, create a branch, make focused changes.
2. Run `python -m unittest discover tests` if you touched `tools/` or `assessment/hacf-spec.json`.
3. Update `CHANGELOG.md` under "Unreleased".
4. Open a PR describing the change, the layer, and the reasoning.
