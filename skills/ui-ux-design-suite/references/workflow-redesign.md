# Existing-Product Redesign Workflow

Use when a working product, page, flow, or component family already exists.

## Phase 1 — Preserve the current truth

Before proposing anything:

- inspect the current flow and representative rendered screens;
- identify what users can currently accomplish;
- read PRODUCT.md/DESIGN.md when present;
- inspect tokens, component primitives, route/navigation rules, state/data semantics, and relevant tests/stories.

Do not change code yet.

## Phase 2 — Audit

Audit the actual experience, not an imagined redesign. Rank findings by user impact and evidence.

Separate:

1. structural UX / flow issues;
2. IA/navigation issues;
3. layout/hierarchy/density issues;
4. typography/readability issues;
5. color/state/contrast issues;
6. interaction/feedback issues;
7. accessibility/responsive issues;
8. generic/AI-pattern or personality issues;
9. polish-only issues.

Distinguish defects from preference.

## Phase 3 — Impact/regression map

Map target → direct components → shared primitives → tokens/theme → other consumers → data/behavior contracts → tests/stories.

For each proposed shared change, decide: systemic fix, local variant, or unclear propagation.

## Phase 4 — User alignment

Present the highest-impact issues first. Then ask only material questions that remain, each with a recommended default.

Examples:

- Is the user willing to change the navigation model, or must it remain stable?
- Should a shared component change propagate globally or only on this surface?
- Is the target a conservative refinement or a deliberate visual re-positioning?
- Is mobile parity required in the same task?

Do not ask about details that can be safely decided from established project conventions.

## Phase 5 — Reference research

Find 2–4 mature references for the **specific problems**, not simply visually attractive products. For each reference record:

- the pattern;
- why it works for the target task;
- what should not be copied;
- how it fits the current project's constraints.

## Phase 6 — Resolve structure before style

If the audit found flow/IA defects, fix journey/IA first. Otherwise preserve the current UX model and move directly to wireframe/layout refinement.

## Phase 7 — Preview

Create the cheapest credible preview:

- wireframe for structure;
- HTML/CSS sandbox for layout/visual rhythm;
- design canvas/static mock for visual direction;
- interactive mini-prototype for changed interactions.

Use realistic content and important states.

**Approval gate:** user approves one direction before production UI changes.

## Phase 8 — Implementation

Freeze scope. Reuse existing components/tokens. Apply shared changes only with explicit propagation intent. Avoid unrelated refactoring.

## Phase 9 — Regression + QA

Verify the primary flow, changed alternate states, affected shared consumers, responsive behavior, keyboard/focus basics, accessibility risks, and fidelity to the approved preview.

## Phase 10 — Durable documentation

Update DESIGN.md only for decisions intended to become project-wide conventions. Do not write temporary page-specific styling into the global design system.
