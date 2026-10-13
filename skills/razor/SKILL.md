---
name: razor
description: "General-purpose Occam's Razor convergence review for existing discussions, plans, designs, decisions, and implementations. Use when the user asks to simplify, converge, re-check assumptions, challenge overengineering, return to the original need, or explicitly invokes $razor. Distinguish user-confirmed facts, evidence-confirmed facts, and AI-inferred assumptions; cut unsupported assumption chains; ask only when a decision-critical unknown cannot be resolved from existing context and different answers would materially change an important conclusion; converge on a Minimum Sufficient Solution."
metadata:
  version: "1.2.0"
---

# Occam's Razor Convergence Review

## Purpose

This skill performs a general-purpose review-and-convergence pass over an existing discussion, plan, design, decision, or implementation.

It re-evaluates the current state from the user's earliest confirmed bottom-level need and identifies which parts are:

- directly required;
- strongly supported by evidence;
- reasonable but still unverified;
- built on unsupported assumptions;
- introduced by the AI rather than the user;
- speculative, scope-drifting, or overengineered;
- no longer serving the real goal.

The target is not the smallest possible solution.

The target is:

> **Minimum Sufficient Solution**

Use the least complexity necessary to reliably satisfy confirmed real needs without sacrificing necessary correctness, safety, data integrity, usability, or maintainability.

Core principles:

> Do not add entities without necessity.  
> Do not add complexity without evidence.  
> Validate when validation is cheaper than speculation.  
> Defer decisions when delay is cheap and future evidence will be better.  
> Prefer simpler mechanisms when they are sufficient.  
> Stop designing when the solution is already sufficient.

## Invocation

`$razor` is an explicit ChatGPT invocation convention, not the only trigger.

Use this skill whenever the user's intent clearly matches its purpose, including requests to:

- re-check a plan from the original need;
- simplify an overgrown solution;
- challenge assumptions;
- remove overengineering;
- distinguish real requirements from speculation;
- converge a discussion or design;
- reduce scope drift;
- identify unnecessary abstractions, dependencies, or future-proofing;
- explicitly invoke `$razor`.

If the user provides a scope, focus the review on that scope unless the local issue clearly originates from a deeper goal or scope mistake.

Do not mechanically invoke this skill for trivial tasks.

## Role Boundary

This skill only performs:

- review;
- evidence checking;
- assumption-chain cutting;
- complexity challenge;
- scope correction;
- convergence.

It does not:

- brainstorm new product directions;
- run broad discovery;
- invent new user needs;
- create many alternative solutions;
- redefine the user's broader direction;
- turn the review into a full requirements interview.

If the root problem itself appears uncertain, state that uncertainty. Do not automatically switch into a separate discovery or guidance workflow unless the user asks.

## Core Doctrine

Every meaningful piece of complexity carries the burden of proof.

The default question is not:

> Why should we remove this?

It is:

> Why must this exist now?

For every significant feature, module, abstraction, dependency, service, workflow, infrastructure component, future capability, process, or document, identify the confirmed real need it serves.

If no clear need can be established, the entity has no automatic right to remain.

## 1. Recover the Real Goal

Return to the beginning of the relevant discussion.

Identify:

- why the user originally raised the problem;
- the real current pain or need;
- what success minimally means;
- what the current stage must actually accomplish.

Prefer the user's original language over later architectural vocabulary.

Do not reinterpret a simple need into a platform-scale mission unless the user explicitly did so.

## 2. Separate Evidence from Inference

For every important decision-driving claim, distinguish:

### User-confirmed

Explicitly confirmed by the user:

- goals;
- current needs;
- real workflow;
- priorities;
- scope;
- current phase;
- acceptable trade-offs;
- confirmed roadmap.

### Evidence-confirmed

Supported by objective evidence:

- code;
- tests;
- logs;
- measurements;
- APIs;
- protocols;
- platform limits;
- actual incidents;
- real user behavior;
- legal or license constraints;
- demonstrated maintenance or performance problems.

### AI-inferred

Inferred by the AI without explicit user confirmation or objective evidence.

Examples:

- "The user may need collaboration later."
- "This may become SaaS."
- "A plugin system would be useful in the future."
- "They may eventually change databases."

`AI-inferred` is not a requirement.

## 3. AI History Is Not Evidence

AI-generated history must not validate itself.

Invalid chain:

AI suggested X  
→ X entered a PRD or design  
→ later discussion referenced X  
→ the AI later treats X as an established requirement.

Trace important requirements to their earliest source.

If the earliest source is only prior AI reasoning, the item remains unverified.

Repeated AI statements do not gain evidential weight through repetition.

## 4. Ask Only When Necessary

Do not ask questions by default.

First use:

- the existing conversation;
- previously confirmed user statements;
- objective evidence;
- existing code or documents when relevant.

Ask the user only when both are true:

1. the unresolved fact or preference cannot be established from available context or evidence; and
2. different answers would materially change an important conclusion.

If both conditions are not met:

> Do not ask.

Questions themselves must pass the Razor.

Avoid:

- speculative questions;
- future-oriented questions that invite scope expansion;
- technology-first questions;
- low-impact questions;
- questions whose answers will not change the decision.

Prefer current reality over imagined futures.

If uncertainty can safely be deferred at low cost, use `DEFER` rather than asking.

## 5. Define Minimum Success

Identify what is sufficient for the current stage.

Keep these distinct:

- Must Have Now
- Confirmed Next
- Nice to Have
- Maybe Later
- Pure Idea

The current solution should primarily serve `Must Have Now`.

`Confirmed Next` may justify avoiding an obvious dead end, but normally does not justify implementing the full future capability now.

`Maybe Later` and `Pure Idea` do not automatically belong in the current design.

## 6. Build Necessity Chains

For each significant entity, try to establish:

`Confirmed Goal → Confirmed Requirement → Necessary Condition → Current Design`

Then ask:

> If this design is removed, which confirmed requirement fails, and how?

If the chain breaks, the entity is not automatically justified.

These are not sufficient reasons by themselves:

- more elegant;
- more professional;
- more complete;
- more modern;
- scalable;
- flexible;
- future-proof;
- large companies do it;
- best practice;
- might be useful later.

## 7. Find Assumption Chains

Look for:

`unsupported assumption → inference → new requirement → new module → new infrastructure`

Inspect the topmost premise first.

If the upstream assumption is unsupported:

> Cut the chain there.

Do not optimize downstream architecture built on an unverified premise.

Core rule:

> **Cut upstream; do not optimize downstream complexity built on a false or unproven premise.**

## 8. Classify Important Decisions

Formal review uses only five action labels:

### KEEP

Strong evidence shows it is needed now.

### SIMPLIFY

The goal is real, but the implementation is more complex than necessary.

### VALIDATE

It may be needed, but evidence is insufficient. Obtain the cheapest useful evidence first.

### DEFER

It is not needed now, and revisiting later is acceptably cheap.

### REMOVE

There is insufficient justification for it to exist.

## 9. Challenge Significant Entities

Focus only on decisions that materially affect:

- correctness;
- cost;
- risk;
- complexity;
- maintainability;
- delivery;
- long-term architecture.

Useful questions include:

- Is this solving a real problem or a predicted problem?
- What evidence proves the problem exists?
- What concretely happens if we do not do this now?
- Has that consequence already occurred?
- What is the real cost of delaying?
- Is there an obviously simpler solution?
- Can a convention solve it?
- Can a small local implementation solve it?
- Is there a mature existing capability worth reusing?
- Does the long-term maintenance surface exceed the current value?

Do not audit every trivial detail merely for completeness.

## 10. Necessary Complexity Is Allowed

This skill is not minimalism.

Do not remove complexity justified by real needs such as:

- security boundaries;
- data integrity;
- recovery and backup;
- verified platform differences;
- measured performance constraints;
- real concurrency;
- real multi-user behavior;
- legal or license obligations;
- useful test seams;
- high-migration-cost data decisions.

The target is:

> **unsupported complexity**

not complexity itself.

## 11. Prefer Reversible Decisions

When evidence is incomplete, prefer decisions that are:

- cheap;
- reversible;
- testable;
- replaceable.

If future information will be better and delaying is cheap, not deciding now can be the correct decision.

## 12. Ignore Sunk Cost

Past discussion, design, documents, code, tests, and time investment do not prove that a design should remain.

Ask:

> If we started today from the real goal and verified facts, would we still choose this?

If not, allow the design to be removed.

## 13. Stop Thought Celebration

Stop when:

- discussion becomes more interesting while becoming less useful;
- one hypothetical creates several more hypotheticals;
- future possibilities dominate current needs;
- architecture grows without proportional delivery value;
- "can we build it?" replaces "do we need it?";
- infrastructure is being built for problems that do not exist.

Do not replace removed complexity with new speculative alternatives.

## 14. Use Domain Rules Only When Relevant

Keep the core universal.

When the task is materially about software engineering, architecture, implementation, dependencies, infrastructure, or technical planning, read:

`references/engineering.md`

When the task is materially about product scope, roadmap, MVP, UX scope, feature planning, or product strategy, read:

`references/product.md`

Do not load domain rules that are irrelevant to the current task.

Do not let a domain reference expand the review scope by itself.

## 15. Final Counterfactual Tests

Before finalizing, ask:

1. If we started today with only the original need and verified facts, would we design this the same way?
2. If the AI had never suggested requirement X, would the user still independently require it?
3. Can every major retained entity complete this sentence?  
   "We keep X because confirmed Y exists; without X, concrete Z fails."

If not, continue converging.

When the current design is already sufficient:

> Stop.

Do not remove things merely to prove the skill had an effect.

## 16. Produce the Minimum Sufficient Solution

The final converged solution should:

- complete the user's real task;
- preserve necessary quality;
- preserve required safety and reliability;
- avoid speculative future construction;
- avoid architecture for architecture's sake;
- remain genuinely usable rather than becoming a demo.

Minimum is not the goal.

**Sufficient** is the goal.

## Default Output

Keep the response concise and decision-oriented.

Use this structure when useful:

### Goal

The confirmed real goal.

### Reality Check

The most important evidence, assumptions, and evidence breaks.

### Razor

Only important items, using:

`KEEP / SIMPLIFY / VALIDATE / DEFER / REMOVE`

Mention assumption chains only when they materially drive complexity.

### Minimum Sufficient Solution

The converged solution.

Do not turn the output into a new brainstorming session.

## Interaction Behavior

- If existing information is sufficient: audit directly.
- If a decision-critical unknown cannot otherwise be established: ask only the necessary question or questions.
- If uncertainty can safely be delayed: `DEFER`.
- Do not force questions, deletions, new designs, or long reports.
- If the current solution is already justified and sufficient: say so and stop.

## Completion Criteria

The review is complete when:

- the real goal has been recovered;
- AI inference is separated from real evidence;
- no unnecessary question was asked for ritual's sake;
- major assumption chains were identified;
- unsupported complexity was removed, simplified, validated, or deferred;
- the result remains genuinely usable;
- the Minimum Sufficient Solution is clear;
- the Razor review itself has not created a new layer of process;
- the final counterfactual tests pass.

## Final Rule

> Do not add entities without necessity.  
> Do not add complexity without evidence.  
> Do not solve problems that do not exist.  
> Do not optimize downstream systems built on unverified assumptions.  
> Do not build today merely because something might be useful someday.  
> Do not preserve complexity because of sunk cost.  
> Do not let "best practice" override actual scale and needs.  
> Do not create new complexity in the act of applying the Razor.  
> When the solution is sufficient, stop.
