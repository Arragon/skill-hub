# Zero-to-One UI/UX Workflow

Use for new products, substantial new features, or a screen family whose UX and visual system are not yet settled.

## Phase 1 — Understand the product

1. Inspect available product facts and technical constraints.
2. Determine primary user, job-to-be-done, frequency, platform, content/data shape, and success condition.
3. Ask only material questions that cannot be inferred.
4. Define explicit non-goals to prevent scope drift.

Output: concise product/design brief.

## Phase 2 — Research and strategy

1. Research current user pain and mature analogous products when evidence would change the design.
2. Separate transferable interaction patterns from superficial aesthetics.
3. Define primary task, secondary tasks, success metric/observable outcome, and critical constraints.

Output: problem framing + reference rationale.

## Phase 3 — UX structure

1. Journey/task flow: entry, happy path, decisions, cancel/back, recovery, failure, completion.
2. IA/navigation: grouping, labels, hierarchy, findability, scalable placement.
3. Edge-state inventory: no data, partial data, slow/failure, permission, long text, retry, destructive actions, interruptions.
4. Wireframe: low-fidelity screen structures showing hierarchy, controls, states, and continuity.

**Checkpoint 1:** show the structure to the user. Ask only directional questions and obtain approval before visual polish.

## Phase 4 — Visual system

1. Determine whether a durable design system already exists.
2. If not, explore a small number of genuinely distinct product-appropriate directions.
3. Select one visual authority and one direction.
4. Define typography roles, semantic colors, spacing, radius/border/shadow language, component and navigation language, density, motion level, and accessibility expectations.
5. Record durable rules in DESIGN.md when the project uses durable design docs.

## Phase 5 — Preview

Choose the minimum preview fidelity that resolves remaining uncertainty:

- wireframe for structure;
- simple HTML/CSS for layout/density/visual rhythm;
- design canvas/static mock for visual language;
- lightweight interactive prototype for interaction.

Use realistic content and relevant states.

**Checkpoint 2:** user approves one direction. Do not implement production UI before this checkpoint unless an already-approved concrete target exists.

## Phase 6 — Implementation contract

Freeze:

- approved flows and screen set;
- visual direction/design system;
- component ownership and reuse plan;
- required states;
- responsive behavior;
- a11y requirements;
- out-of-scope work;
- acceptance and regression checks.

## Phase 7 — Production implementation

1. Inspect existing implementation boundaries.
2. Reuse current stack and design primitives where possible.
3. Prefer maintained accessible primitives over hand-rolling complex interaction widgets.
4. Avoid speculative abstraction and unrelated refactors.
5. Implement all required states, not only the happy path.

## Phase 8 — Hardening and QA

Validate behavior, responsive layout, accessibility basics, realistic content, edge states, shared component consumers, and fidelity to the approved preview. Run framework-specific QA when available.

## Phase 9 — Handoff

Update durable product/design documentation only with decisions intended to survive the task. Report what changed, what was verified, remaining issues, and whether the scope is ready to ship.
