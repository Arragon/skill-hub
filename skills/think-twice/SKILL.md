---
name: think-twice
description: Independent second-pass reasoning review. Use when an important conclusion may be anchored to one reasoning path and a genuinely different perspective could reveal material assumptions, trade-offs, alternative explanations, or decision conditions without manufacturing disagreement.
---

# think-twice

Independent Second-Pass Reasoning Review.

Use this skill to temporarily step outside the reasoning path that produced the current conclusion and examine the problem from a genuinely different, independent perspective.

Its purpose is not to argue, negate the current answer, or force an alternative conclusion.

Its purpose is to discover a small number of questions, assumptions, alternative explanations, or decision factors that are valuable enough to reconsider before committing to the current conclusion.

## Core objective

Do not merely inspect the original reasoning for internal consistency.

Reconstruct the problem from another plausible starting point and ask:

> If I had not seen the existing reasoning path, what might I notice, question, or prioritize differently?

Then compare that independent perspective with the existing conclusion.

The goal is discussion-worthy challenges, not objections for their own sake.

## Principles

### Independent, not oppositional

Do not begin from:

> The current conclusion is wrong.

Begin from:

> Suppose I had to analyze this problem independently. Would I naturally reach the same conclusion, and for the same reasons?

Agreement is a valid result.

### Do not manufacture disagreement

Never invent weak objections merely because the skill was invoked.

If no materially useful challenge is found, say so explicitly.

### Challenge reasoning, not wording

Ignore cosmetic issues, phrasing preferences, and minor implementation details unless they materially affect the outcome.

Prioritize issues that could change:

- the conclusion;
- the recommended option;
- architecture or strategy;
- cost or complexity;
- risk;
- maintainability;
- reversibility;
- expected benefit;
- confidence in the decision.

### Prefer different frames over direct rebuttals

Useful alternative frames may include:

- another stakeholder's perspective;
- short-term versus long-term consequences;
- technical versus product considerations;
- implementation versus operational reality;
- expected case versus failure case;
- optimization versus robustness;
- local optimum versus system-level optimum;
- build versus buy versus defer;
- irreversible versus reversible decisions;
- nominal capability versus actual workflow behavior;
- theoretical correctness versus practical maintainability.

Use only frames relevant to the problem.

### Separate uncertainty from disagreement

Distinguish among:

- **Contradiction** — evidence or reasoning directly challenges the conclusion;
- **Alternative explanation** — another plausible model explains the same facts;
- **Unknown** — insufficient evidence exists to resolve the issue;
- **Trade-off** — the conclusion may still be correct, but an important cost was underweighted.

Missing information is not automatically evidence against the conclusion.

## Workflow

### 1. Identify the actual conclusion

Determine what is currently being claimed, recommended, or decided.

Do not review vague surrounding discussion.

### 2. Detach from the original reasoning path

Temporarily ignore how the current answer was derived.

Reconstruct the problem using confirmed goals, constraints, evidence, and observable facts.

Do not inherit assumptions merely because the previous reasoning used them.

### 3. Generate an independent model

Ask what conclusion you would reach starting fresh.

Look especially for:

- assumptions treated as facts;
- omitted variables;
- hidden dependencies;
- alternative causal explanations;
- asymmetric risks;
- second-order effects;
- constraints that may have been overweighted or underweighted;
- options excluded too early;
- incentives or stakeholder behavior;
- operational realities that theoretical reasoning may miss.

### 4. Compare reasoning paths

Identify only material differences.

For each difference ask:

> If this issue were resolved differently, could it meaningfully change the decision?

If not, discard it.

### 5. Select high-value challenges

Return only the strongest points.

Default target:

- 1–3 substantive questions or challenges;
- up to 5 for unusually complex decisions.

Do not produce a catalogue of hypothetical objections.

### 6. Reassess

Use one of these states when useful:

- `REINFORCED` — the independent review strengthens the original conclusion;
- `UNCHANGED` — no material challenge changes the current conclusion;
- `CONDITIONAL` — the conclusion remains reasonable but depends on an important unresolved condition;
- `RECONSIDER` — a material flaw or alternative justifies reconsideration.

Do not reverse the original conclusion unless the independent analysis actually supports doing so.

## What counts as a useful challenge

A strong challenge usually has this structure:

```text
The current reasoning assumes X.

From another perspective, Y may also be plausible because Z.

If Y is true, it would affect the decision by ...

Therefore the useful question is ...
```

The value lies in whether resolving the issue improves the decision.

## What does not count

Do not use:

- mechanical contrarianism;
- edge-case dumping;
- repetition of caveats already adequately addressed;
- semantic or stylistic objections without decision impact;
- false balance between unequally supported options;
- rhetorical debate techniques.

## Stop condition

Stop after the strongest material challenges have been identified and their decision impact assessed.

If no strong challenge exists, stop and say so.

Do not expand into a full duplicate analysis.

## Default output

```text
Second perspective:
[Brief independent framing.]

1. [High-value challenge/question]
   Why it matters: ...

2. [High-value challenge/question]
   Why it matters: ...

Reassessment:
[REINFORCED / UNCHANGED / CONDITIONAL / RECONSIDER] — ...
```

## Success criterion

The skill succeeds when it either increases confidence that the conclusion survives an independent reasoning path or reveals a small number of concrete issues worth resolving before commitment.
