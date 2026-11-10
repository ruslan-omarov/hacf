# 01 · Levels L0–L5

*Layer: Core (level definitions and interaction modes) + Indicators (behavioural indicators). Examples are non-normative.*

## The progression logic

Each level is defined by three things:

1. **Interaction mode** — the person's relationship to AI.
2. **Scope of impact** — whose work changes: *Self → Team → Organisation → Ecosystem*.
3. **Accountability** — what the person is answerable for.

| Level | Name | Interaction mode | Typical scope | Accountable for |
|---|---|---|---|---|
| L0 | Unaware | — | — | — |
| L1 | Aware | **Observe** — recognises AI and its risks | Self | Following AI rules |
| L2 | User | **Ask** — gives tasks, receives and checks output | Self | Correctness of own AI-assisted output |
| L3 | Practitioner | **Collaborate** — iterates with AI inside repeatable workflows | Self / Team | Quality of AI-integrated professional work |
| L4 | Builder | **Delegate & Orchestrate** — designs systems where AI acts, with human control points | Team / Organisation | Reliability and safety of solutions used by others |
| L5 | Leader | **Govern** — decides where AI acts, where humans act, and how it is controlled | Organisation / Ecosystem | AI strategy, portfolio, risk and capability of people |

The modes are cumulative: an L4 Builder still asks, collaborates and observes.

---

## L0 — Unaware

**Definition.** Does not use AI deliberately in work, or cannot describe what generative AI does.

**Behavioural indicators**
- Cannot name a work task where AI could help.
- Unaware of organisational rules on AI use (or that there are none).
- May already be exposed to AI unknowingly (e.g. pasting data into tools with AI features).

**Risk note.** L0 is not neutral: unaware people are the most likely to leak data via AI features embedded in everyday software.

**Development goal →** L1 in weeks, through short awareness training.

---

## L1 — Aware

**Definition.** Understands what AI is, what it is good and bad at, and the rules for using it at work.

**Behavioural indicators**
- Explains in plain words that AI generates plausible output that can be wrong.
- Names at least three suitable and three unsuitable tasks for AI in own role.
- Knows which data must never be entered into which AI tools.
- Knows whom to ask and where the AI policy is.

**Minimum gates:** K≥1, J≥1, R≥1.

---

## L2 — User

**Definition.** Uses AI regularly for own tasks and checks results before relying on them. AI is part of personal productivity.

**Behavioural indicators**
- Gives AI clear tasks with context, constraints and expected format.
- Uses AI for drafting, summarising, analysing documents and data, searching and structuring information.
- Iterates when the first answer is weak instead of accepting or abandoning it.
- Verifies facts, numbers and citations before using output; can show how.
- Chooses an appropriate tool for the data sensitivity of the task.

**Minimum gates:** K≥2, A≥2, J≥2, R≥2.

*Example (non-normative, 2026):* uses a corporate chat assistant to draft a client letter from meeting notes and checks every commitment against the notes.

---

## L3 — Practitioner

**Definition.** Has redesigned own professional work around AI. Uses AI repeatably for complex tasks, measures the effect, and shares methods with colleagues.

**Behavioural indicators**
- Maintains reusable instructions, templates or workflows for recurring tasks.
- Combines several AI capabilities or tools in one piece of work (e.g. research → analysis → document).
- Works with organisational knowledge and data within access rules.
- Can quantify time saved or quality gained for at least one workflow.
- Knows the failure patterns of AI in own domain and designs checks against them.
- Explicitly decides when not to use AI.
- Helps colleagues adopt proven workflows.

**Minimum gates:** K≥2, A≥3, C≥2, J≥3, R≥3. **Evidence ≥ E3.**

*Example (non-normative, 2026):* a financial analyst who runs monthly variance analysis through a documented AI workflow with built-in reconciliation checks, saving two days per month.

---

## L4 — Builder

**Definition.** Creates AI solutions that other people or processes rely on: automations, agents, integrations, internal tools. Not necessarily a software engineer.

**Behavioural indicators**
- Designs a solution from a business problem: inputs, steps, AI role, human control points, outputs.
- Builds with whatever means fit — no-code, low-code or code.
- Connects AI to data and systems with appropriate permissions (least privilege).
- Tests solutions on realistic cases, including adversarial and edge cases, before release.
- Monitors behaviour in use, handles failures, maintains documentation.
- Designs human-in-the-loop or human-on-the-loop controls proportional to risk.

**Minimum gates:** K≥3, A≥3, C≥4, J≥3, R≥3. **Evidence ≥ E4. Scope ≥ Team.**

*Example (non-normative, 2026):* an operations manager who built an agent that triages incoming supplier emails, drafts responses, updates the ERP after human approval, and logs every action.

---

## L5 — Leader

**Definition.** Determines how AI changes the work of a team, organisation or sector, and is accountable for value, risk and people.

**Behavioural indicators**
- Sets AI direction tied to business strategy and measurable outcomes.
- Decides human–AI division of labour for processes and roles.
- Manages a portfolio of AI initiatives: prioritises, funds, stops.
- Establishes governance: policies, risk classification, accountability, oversight.
- Builds people capability: target profiles, development programmes, AI Champions.
- Can read and challenge technical proposals without being a builder.

**Minimum gates:** K≥3, A≥3, C≥3, J≥4, R≥4. **Evidence ≥ E4. Scope ≥ Organisation.**

*Note.* L5 does not require C≥4. A leader must understand building well enough to judge it, not necessarily do it.

---

## Domain qualifiers (optional)

A person's capability can differ by domain. Organisations may record domain-specific levels:

```
HACF L3 [K3·A4·C2·J3·R3] · Domains: Analytics L4, Content L2, Automation L3
```

The headline level is always computed from the five-dimension profile, not from the best domain.
