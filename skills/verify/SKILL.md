---
name: verify
description: Decision-relevant verification. Use when a conclusion depends on important uncertain, external, volatile, disputed, version-dependent, regional, or time-sensitive facts or assumptions that should be checked efficiently with appropriate evidence and a clear stopping rule.
---

# verify

Decision-Relevant Verification.

Use this skill to determine what actually needs verification, gather the right evidence efficiently, judge its strength, and stop once additional research is unlikely to change the decision.

This is not a mandate to verify every uncertain statement.

## Core principles

> Verify the weakest important link, not every weak link.

> Do not verify claims merely because they are uncertain. Verify them when resolving the uncertainty has meaningful value for the current decision.

> If this claim is wrong, does the conclusion materially change?

If not, deprioritize it.

## When to use

Use `verify` when a conclusion materially depends on one or more claims that are:

- time-sensitive or volatile;
- external and readily checkable;
- uncertain, disputed, or based on memory;
- consequential to a technical, product, financial, operational, or strategic decision;
- likely to be affected by version, region, policy, pricing, maintenance state, compatibility, or recent events;
- supported only by weak, secondary, or non-independent evidence.

Do not spend verification effort on stable common knowledge or low-impact uncertainty unless the context makes it decision-critical.

## Workflow

### 1. TRIAGE

Extract only the claims or assumptions that could materially change the conclusion.

For each candidate claim, ask:

1. **Impact** — If wrong, would the conclusion, recommendation, architecture, risk, or next action materially change?
2. **Uncertainty** — Is there a real reason to doubt it?
3. **Volatility** — Could it have changed recently or vary by version, region, plan, or context?
4. **Verification value** — Is the expected decision benefit worth the attention and search cost?

Use qualitative judgment. Do not invent numeric scores.

Skip claims that are uncertain but decision-irrelevant.

### 2. SEARCH

Choose evidence based on the claim type.

For specifications, APIs, policies, pricing, compatibility, licenses, plans, limits, and official support:

- prefer current primary or authoritative sources;
- verify version, date, region, and scope;
- use secondary sources mainly to detect exceptions or practical discrepancies.

For reliability, hidden issues, workflow friction, maintenance quality, operational behavior, and real-world experience:

- use actual user reports, issue trackers, engineering communities, independent reviews, and operational evidence;
- distinguish recurring patterns from isolated anecdotes.

For best practices or complex judgments:

- combine authoritative guidance with credible engineering practice and real-world experience;
- seek disagreement and failure reports, not only sources supporting the current view.

For highly time-sensitive claims:

- prioritize freshness;
- do not let an older authoritative source override newer direct evidence about current state without checking whether the older source still applies.

Do not treat multiple pages repeating the same underlying source as independent corroboration.

Diversify searches only when the decision requires it. Do not maximize source count.

### 3. JUDGE

Classify only material claims:

- `VERIFIED` — current, direct, reliable evidence supports the claim;
- `SUPPORTED` — multiple credible or independent signals support it, but direct proof is unavailable or incomplete;
- `UNRESOLVED` — evidence is insufficient, conflicting, stale, or conditional in a way that matters;
- `CONTRADICTED` — reliable evidence conflicts with the claim.

Do not invent precise confidence percentages without a defensible quantitative basis.

When evidence changes, update the conclusion. Do not use evidence merely to decorate an existing belief.

For important hypotheses, consider what evidence would change your mind or disconfirm the current view.

### 4. STOP

Stop when additional verification is unlikely to change:

- the decision;
- the recommended option;
- the required mitigation;
- the evidence-status classification of a material claim.

Continue when:

- a material claim remains unresolved and the decision depends on it;
- reliable sources conflict in a decision-relevant way;
- the available evidence is clearly stale for a volatile claim;
- a cheap additional check could resolve an important ambiguity.

Do not continue searching for completeness, rhetorical confidence, or source-count targets.

## Dependency rule

When reasoning contains many claims, do not verify them uniformly.

Ask:

> If this claim fails, does the conclusion still stand through independent support?

If yes, its verification priority drops.

If a single claim is a critical dependency for the conclusion, verify it before spending effort on peripheral weaknesses.

## Guardrails

Never:

- search every factual sentence by default;
- equate uncertainty with importance;
- use community rumor where direct authoritative evidence is available;
- use vendor marketing as proof of real-world reliability;
- treat repeated secondary reporting as independent confirmation;
- use stale evidence for current-state claims without checking applicability;
- manufacture numeric confidence scores;
- keep researching after new evidence is unlikely to affect the decision.

## Default output

Keep output proportional to the task.

For simple cases:

```text
Key claim: ...
Status: VERIFIED / SUPPORTED / UNRESOLVED / CONTRADICTED
Why it matters: ...
Evidence judgment: ...
Effect on conclusion: ...
```

For complex cases, use a compact set of only the material claims.

End with the decision impact, not with a bibliography dump.

## Success criterion

The skill succeeds when it spends verification effort on the few uncertainties that matter, uses evidence appropriate to each claim, updates the conclusion when needed, and stops once the evidence is sufficient for the decision.
