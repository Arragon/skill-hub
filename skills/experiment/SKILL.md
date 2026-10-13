---
name: experiment
description: Decision-oriented experimental probe. Use when a material uncertainty can be resolved more cheaply and reliably by a small safe reversible real-world test than by further research, modeling, or discussion.
---

# experiment

Decision-Oriented Experimental Probe.

Use this skill when an important uncertainty is better resolved by a small real-world test than by further discussion, research, modeling, or speculation.

The purpose is to design the cheapest reversible experiment capable of producing decision-changing evidence.

It is not a generic prototyping or MVP workflow.

## Core principles

> When uncertainty is cheaper to test than to reason about, test it.

> Optimize experiments for information gained, not implementation progress.

> Prefer the cheapest experiment capable of falsifying the current assumption.

## When to use

Use `experiment` when:

- an unresolved uncertainty materially affects the decision;
- available documentation or discussion cannot settle it reliably;
- real behavior depends on the user's actual environment, workload, data, team, hardware, workflow, or constraints;
- competing options can be distinguished with a small test;
- repeated analysis is producing diminishing returns;
- a reversible probe is much cheaper than committing to the full solution.

Do not experiment when authoritative evidence already resolves the question sufficiently, when the test would be more costly or risky than the decision itself, or when the uncertainty is irrelevant to the decision.

## Workflow

### 1. DEFINE THE DECISION

State the decision the experiment is meant to inform.

Do not begin from "what can we prototype?"

Begin from:

> What uncertainty is preventing a decision?

### 2. ISOLATE THE CRITICAL UNKNOWN

Identify the smallest uncertainty whose resolution could change the direction.

Examples:

- whether a library supports the required workflow in practice;
- whether latency is acceptable under realistic load;
- whether users understand a particular interaction;
- whether an adapter can hide a legacy API cleanly;
- whether a deployment path works in the actual environment.

Do not test unrelated nice-to-know questions.

### 3. FORM A TESTABLE HYPOTHESIS

Express the current belief in observable terms.

Bad:

> Tauri is mature enough.

Better:

> A minimal build using our required file access, updater, and UI flow can run reliably on the three target platforms without introducing a blocker that would force a framework change.

The hypothesis must connect to the decision.

### 4. DESIGN THE SMALLEST USEFUL TEST

Specify:

- the minimum setup;
- the exact behavior to exercise;
- what to measure or observe;
- what can be mocked or omitted;
- what must be realistic for the result to generalize;
- what can be thrown away afterward.

Prefer a spike, probe, benchmark, compatibility check, paper prototype, user test, feature flag, shadow run, or controlled trial over partial production implementation when possible.

Do not silently turn the experiment into the real project.

### 5. DEFINE THE DECISION RULE BEFORE RUNNING

State what outcomes would change the decision.

For example:

```text
If X succeeds under Y condition, continue with A.
If X fails because of blocker Z, reject A.
If the result is ambiguous, run one narrower follow-up test rather than expanding the prototype.
```

Avoid moving the goalposts after seeing the result.

### 6. CHECK COST, RISK, AND REVERSIBILITY

Before recommending the experiment, ask:

- Is this cheaper than continued analysis?
- Is it cheaper than committing to the wrong option?
- Can it be safely reversed or discarded?
- Could it contaminate production data, users, infrastructure, or future decisions?

If the experiment is expensive or irreversible, redesign it smaller.

### 7. INTERPRET, DO NOT OVERGENERALIZE

After results are available:

- update the decision only to the extent supported by the test;
- distinguish a failed implementation from a falsified hypothesis;
- distinguish environment-specific evidence from universal conclusions;
- identify whether a follow-up test has meaningful value.

One successful test does not prove an option is universally good. One failed prototype does not prove the underlying approach is impossible unless the failure mechanism is actually relevant.

## Stop condition

Stop when the experiment has produced enough evidence to make or materially narrow the decision.

Do not keep expanding the test for completeness or because useful code has begun to accumulate.

If the result remains ambiguous, prefer one narrower follow-up probe over converting the experiment into an open-ended project.

## Guardrails

Never:

- prototype merely because prototyping feels productive;
- test uncertainty that would not change the decision;
- optimize for code reuse or feature completeness;
- hide production implementation inside an "experiment";
- run risky tests when a safer proxy can answer the same question;
- change success criteria after seeing inconvenient results;
- overgeneralize from a narrow environment or tiny sample.

## Default output

```text
Decision to inform:
...

Critical unknown:
...

Hypothesis:
...

Smallest useful experiment:
...

Observe:
...

Decision rule:
...

Why this test is worth doing:
...
```

## Success criterion

The skill succeeds when it replaces expensive speculation with the smallest safe action that can produce evidence capable of changing the decision.
