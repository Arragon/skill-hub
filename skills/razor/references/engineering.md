# Engineering Razor

Use this reference only when the reviewed task is materially about software engineering, architecture, implementation, infrastructure, dependencies, technical planning, or codebase structure.

These are domain heuristics, not universal laws.

## YAGNI

Do not fully implement unconfirmed future capabilities.

Distinguish avoiding an obvious irreversible dead end from prematurely building the future system.

Reasonable low-cost slack can include:

- avoiding hard-coded values that are obviously expected to vary;
- isolating volatile external APIs;
- preserving data migration paths;
- choosing a format that avoids obvious lock-in.

Do not convert that into:

- plugin frameworks;
- generic DSLs;
- generalized provider systems;
- distributed architectures;
- extension marketplaces;
- workflow engines;
- multi-backend systems

without real evidence.

## Premature Abstraction

Challenge abstractions when:

- only one implementation exists;
- two implementations are generalized before their real variation is known;
- wrappers only forward calls;
- Manager / Engine / Core / Provider / Service layers multiply without clear value;
- a small amount of duplication is replaced by a large conceptual framework;
- boundaries are based on imagined future variation.

Useful heuristic:

- first occurrence → implement directly;
- second occurrence → tolerate small duplication;
- third stable recurrence → seriously consider abstraction.

This is a heuristic, not a law.

> Duplication is often cheaper than the wrong abstraction.

## Architecture Size

Compare architecture complexity with real product complexity.

Challenge a small system that already contains many:

- core modules;
- providers;
- repositories;
- lifecycle systems;
- event types;
- extension points;
- runtime services;
- abstraction layers.

Ask whether the architecture is starting to reproduce itself.

## Count Concepts, Not Only Lines

Complexity also includes:

- abstraction count;
- runtime component count;
- configuration surface;
- state sources;
- data-flow branches;
- extension points;
- failure modes;
- dependencies.

Saving a few lines is not a win if it creates many new concepts.

## Dependency Razor

Treat every dependency as an entity.

Evaluate:

- actual capability needed;
- maintenance activity;
- API stability;
- transitive dependencies;
- supply-chain risk;
- security;
- runtime or bundle cost;
- platform compatibility;
- upgrade burden;
- replaceability;
- cognitive overhead;
- license and commercial compatibility.

Prefer mature, active, license-compatible existing implementations when they genuinely save work.

But:

> Open-source first does not mean dependency first.

If the required behavior is tiny and stable, a small local implementation may be lower cost than adopting a large framework.

## License Razor

Do not treat licenses as equivalent.

Permissive licenses such as MIT, BSD, and Apache-2.0 are generally easier to reuse, subject to their terms.

GPL, AGPL, LGPL, and MPL require analysis of the concrete linking, distribution, SaaS, and modification model.

SSPL, BUSL, Commons Clause, and commercial dual licenses require extra caution where commercial or redistribution restrictions matter.

When direct reuse creates meaningful risk, prefer learning from:

- architecture;
- interfaces;
- algorithms;
- testing strategy;
- failure-handling patterns

rather than blindly forking or copying implementation.

## Best Practice Is Not a Requirement

Invalid logic:

"Large systems often use X → therefore this project should use X."

Required logic:

"Real problem Y exists → X demonstrably addresses Y → its cost is proportionate → use X."

## Reversibility

Raise the evidence bar for decisions with high migration cost:

- public APIs;
- persistence and data formats;
- synchronization protocols;
- plugin protocols;
- cloud or local architecture;
- multi-tenant models;
- core technology stacks;
- restrictive-license dependencies.

Prefer reversible decisions where uncertainty remains.

## Security Proportionality

First establish the threat model:

- what data exists;
- who could attack;
- trust boundaries;
- deployment environment;
- real failure consequence.

Then choose proportionate controls.

Do not introduce enterprise-grade security infrastructure to solve an abstract risk that does not exist.

Do not use this rule to dismiss confirmed security requirements.

## Documentation Inflation

Documentation is also an entity.

Ask:

> Who will use this document, and when?

Delete or merge documents with no real consumer.

Do not generate layers of ADRs, policies, roadmaps, and duplicate specifications merely because AI can generate them cheaply.

## MVP Is Not a Demo

A converged engineering solution should still:

- complete the real workflow;
- preserve required data;
- handle critical errors;
- be stable enough for real use;
- provide sufficient UX where applicable;
- satisfy confirmed platform and security constraints.

Do not confuse convergence with removing basic product quality.

## Decision Hierarchy

When several approaches could solve the problem, generally prefer:

1. do not solve a nonexistent problem;
2. simple convention;
3. small local implementation;
4. reuse mature existing capability;
5. lightweight abstraction;
6. new dependency;
7. generalized subsystem;
8. heavy infrastructure.

The lower the choice, the stronger the evidence required.
