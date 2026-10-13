---
name: premortem
description: Implementation failure pre-mortem. Use selectively for consequential plans, architectures, migrations, launches, or long-running systems where identifying a small number of plausible failure mechanisms, early signals, and proportionate mitigations could materially improve the outcome.
---

# premortem

Implementation Failure Pre-Mortem.

Use this skill for consequential plans, architectures, migrations, launches, long-running systems, or other commitments where discovering plausible failure mechanisms before execution could materially improve the outcome.

Assume the plan was executed and later failed. Work backward to identify how that failure most plausibly happened.

This is not a generic risk checklist.

## Core principle

> Imagine the plan has already failed. What realistic mechanism most likely caused it, and what early signal could have exposed it sooner?

The goal is to reveal actionable failure paths, not to maximize the number of risks.

## When to use

Use `premortem` when:

- the commitment is expensive, difficult to reverse, or strategically important;
- failure would cause meaningful operational, financial, security, migration, maintenance, or delivery cost;
- the plan contains multiple interacting components or stakeholders;
- long-term behavior matters more than a one-time demo;
- success depends on assumptions that may degrade after deployment;
- ordinary design review tends to focus on how the plan works rather than how it fails.

Do not use it for trivial, cheap, easily reversible decisions unless the user explicitly requests it.

## Workflow

### 1. DEFINE THE FAILURE EVENT

Assume a concrete future state:

> We followed this plan. It is now considered a failure.

Define what "failure" means in this context, such as:

- missed delivery;
- unacceptable maintenance burden;
- user rejection;
- reliability collapse;
- migration rollback;
- runaway cost;
- architectural dead end;
- security or compliance failure.

Avoid vague statements like "something went wrong."

### 2. GENERATE FAILURE MECHANISMS

Work backward from the failed state.

Look for mechanisms such as:

- hidden dependencies;
- incentives that drive undesirable behavior;
- operational load ignored by the design;
- gradual complexity accumulation;
- feedback loops or delayed effects;
- ownership gaps;
- brittle assumptions;
- vendor or ecosystem dependency;
- migration or compatibility traps;
- local optimization that damages the wider system;
- observability gaps that allow problems to grow unnoticed.

A risk without a mechanism is weak.

Bad:

> Maintenance may become difficult.

Better:

> The compatibility adapter starts accumulating business-specific branches as the old and new APIs diverge, eventually becoming a second implementation layer that every feature must modify.

### 3. PRIORITIZE

Keep only failure modes that are plausible and consequential.

Default to 1–5 strong failure modes.

Do not include remote possibilities merely because they can be imagined.

Consider both likelihood and impact qualitatively, but do not invent numerical probabilities.

### 4. FIND EARLY SIGNALS

For each retained failure mode, identify something observable before full failure.

Good early signals are specific enough to monitor, such as:

- exception branches increasing in an abstraction layer;
- deployment rollback frequency rising;
- manual coordination becoming necessary for routine changes;
- queue latency steadily increasing before saturation;
- user workarounds appearing outside the intended flow;
- dependency upgrades repeatedly being postponed.

### 5. PROPOSE CHEAP MITIGATION

For each failure mode, propose the lowest-cost action that materially reduces the risk or improves detectability.

Prefer:

- boundary clarification;
- instrumentation;
- small validation tests;
- rollback plans;
- ownership assignment;
- explicit limits;
- staged rollout;
- removing unnecessary dependencies;
- documented escape hatches.

Do not redesign the entire system unless the failure mechanism truly requires it.

### 6. REASSESS THE PLAN

Finish by deciding whether the pre-mortem:

- leaves the plan unchanged;
- adds lightweight safeguards;
- exposes a condition that must be validated first;
- reveals a failure mechanism serious enough to reconsider the plan.

The purpose is not to make the plan look dangerous. It is to improve the plan proportionally to the risks found.

## Stop condition

Stop once the strongest plausible failure mechanisms, early signals, and proportionate mitigations are identified.

Do not continue generating risks to appear comprehensive.

## Guardrails

Never:

- produce a generic risk register;
- list a risk without explaining its mechanism;
- inflate extremely remote scenarios;
- assume every risk needs preventive engineering;
- use the pre-mortem as an excuse for speculative architecture;
- recommend a mitigation more expensive than the risk justifies;
- confuse "could happen" with "worth designing for now."

## Default output

For each retained failure mode:

```text
Failure mode:
...

Why it could happen:
...

Early signal:
...

Cheap mitigation:
...
```

Finish with:

```text
Plan reassessment:
UNCHANGED / SAFEGUARD / VALIDATE FIRST / RECONSIDER
```

## Success criterion

The skill succeeds when it identifies a small number of realistic failure mechanisms early enough to change monitoring, validation, safeguards, or the plan itself—without turning risk awareness into speculative overengineering.
