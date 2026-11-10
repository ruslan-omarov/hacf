# 05 · Target Role Profiles

*Layer: Examples (non-normative starting points). Each organisation should adapt targets to its strategy, risk appetite and the autonomy of the AI systems in use.*

A target profile states the **minimum** dimension scores a role needs. It is a business decision, reviewed yearly. Coverage is always measured against the **profile**, not against the level.

The *Target level* column is not chosen freely: it is what the [gates](03-assessment-method.md#gates) produce for that profile at the stated scope. An automated test (`tests/test_scoring.py`) keeps the table and the gates consistent.

Machine-readable version: [`tools/sample/role_profiles.json`](../tools/sample/role_profiles.json).

| Role family | K | A | C | J | R | Scope | Target level | Rationale |
|---|---|---|---|---|---|---|---|---|
| All employees (baseline) | 1 | – | – | 1 | 1 | Self | L1 | Safe awareness for everyone exposed to AI features |
| Knowledge worker (general) | 2 | 2 | – | 2 | 2 | Self | L2 | Daily productivity with verification |
| Customer-facing staff | 2 | 2 | – | 3 | 3 | Self | L2 | Errors reach clients; confidentiality critical |
| Analyst / specialist | 2 | 3 | 2 | 3 | 3 | Self | L3 | Complex work, repeatable workflows |
| Legal, compliance, audit | 3 | 3 | 2 | 4 | 4 | Self | L3 | Verification and accountability dominate |
| HR professional | 2 | 3 | 2 | 3 | 4 | Self | L3 | Personal data, fairness in people decisions |
| People manager | 2 | 3 | 2 | 3 | 3 | Team | L3 | Redesigns team work, oversees AI use |
| Software engineer | 3 | 3 | 4 | 3 | 3 | Team | L4 | Builds AI-enabled software |
| Automation / AI builder | 3 | 3 | 4 | 3 | 3 | Team | L4 | Creates solutions others depend on |
| Operator of high-risk / autonomous AI | 3 | 3 | 1 | 4 | 4 | Self | L2 + oversight profile | See note |
| IT / security lead | 4 | 3 | 4 | 4 | 4 | Team | L4 | Platform, access, threats |
| Executive (C-level) | 3 | 3 | 2 | 4 | 4 | Organisation | L5 | Strategy, governance, accountability |
| Chief AI / Digital Officer | 4 | 3 | 3 | 4 | 4 | Organisation | L5 | Accountable for AI portfolio |

**Note on oversight roles.** An operator who supervises a high-risk or autonomous system does not need to build anything, so the gates place the profile at L2. The profile itself is demanding (J4, R4) — it is the profile, not the level, that the role must meet. This is intentional: HACF levels describe *breadth of relationship with AI*, while profiles describe *what a role requires*.

## Proportionality modifiers

Raise J and R targets by one point (max 5) when the role:

- works with AI systems classified as **high-risk** under applicable law;
- supervises AI that acts **autonomously** (sends, pays, decides, changes records);
- handles **special categories** of personal data, minors' data, or state secrets;
- produces **synthetic content** published under the organisation's name.
