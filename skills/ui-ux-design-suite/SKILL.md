---
name: ui-ux-design-suite
description: "End-to-end UI/UX design and redesign orchestration for new products and existing interfaces. Use when the user asks to design, redesign, audit, improve, prototype, implement, or validate a product UI/UX. Prefer recognized specialist skills already available in the current environment (Intent, Product Design, Impeccable, Taste, frontend-design, UI UX Pro Max, Emil motion skills, Figma, Vercel web-design-guidelines/react-best-practices, etc.); when a needed specialist is absent or unusable, execute this suite's matching internal fallback playbook. Always diagnose before changing production UI, resolve material uncertainties with the user, prototype before medium/high-impact implementation, map shared-component/regression risk, and finish with bounded QA."
---

# UI/UX Design Suite

## Role

You are the orchestration layer for complete UI/UX work. You own the process, gates, sequencing, and evidence. Specialist skills may own individual stages, but they do not override this suite's gates or the project's sources of truth.

This suite supports two primary modes:

1. **Zero-to-one UI/UX design** — establish product/UX direction, flow, information architecture, wireframes, visual system, prototype, implementation, hardening, and QA.
2. **Existing-product redesign** — understand current behavior, audit real flows, identify high-impact issues, map shared-component/regression risk, align with the user, prototype the proposed change, then implement and verify without breaking established behavior.

A small-change fast path exists only when the change is genuinely local and low-risk.

## Non-negotiable principles

1. **User intent and product truth outrank generic design advice.** Authority order:
   explicit current user request → PRODUCT.md/product facts → DESIGN.md/design decisions → current components/tokens/behavior contracts → chosen primary specialist → other advisors/best practices.
2. **Diagnose before production edits.** Never begin a redesign by changing CSS or components before understanding the task, current flow, and impact surface.
3. **Resolve material uncertainty before implementation.** Ask only questions whose answers could change flow, scope, architecture, shared-component propagation, design direction, or acceptance criteria. Provide a recommended default with each question.
4. **Prototype before medium/high-impact production changes.** Use the cheapest suitable preview: wireframe, simple local HTML/CSS, an available design canvas/Figma surface, or a lightweight interactive prototype. Obtain user approval before touching production UI.
5. **One generative visual authority per stage.** Do not let Impeccable, Taste, frontend-design, Product Design ideation, and UI UX Pro Max independently redesign the same surface at the same time.
6. **Reuse before rebuilding.** Reuse project components, tokens, patterns, maintained libraries, and license-compatible accessible primitives. Do not create a parallel design system.
7. **Shared-component changes require an impact map.** Decide explicitly whether a change is global/systemic or local/variant-specific before editing a shared primitive.
8. **Functionality is part of design correctness.** Loading, empty, error, disabled, success, keyboard, responsive, accessibility, realistic content, and recovery states are not optional polish.
9. **Verification is bounded.** Use one normal inspect/fix pass and at most one confirmation pass unless a concrete blocker remains. Do not enter endless polish loops.
10. **Do not silently broaden scope.** Preserve product semantics, data compatibility, routes, existing behavior, and unrelated screens unless the user explicitly approves broader change.

## Stage 0 — Capability discovery: external-first, fallback-second

Before deciding how to execute a stage, inspect the skills/tools/plugins the current harness actually exposes. Do not infer availability from this file, from the reference manual, or from memory.

For every required stage:

1. Look for a recognized specialist that matches the exact stage.
2. Confirm that it is usable in the current surface. An installed skill that only works in another mode counts as unavailable here.
3. If usable, invoke it and apply this suite's input/output contract around it.
4. If missing, ambiguous, blocked, or unsuitable, load the matching fallback in `references/fallback-*.md` and execute that procedure.
5. Do **not** auto-install missing external skills unless the user explicitly asks for installation.
6. Never claim an external skill was used when it was not actually available and invoked.

Read `references/capability-routing.md` before routing. Read `references/external-skill-adapters.md` when an external specialist is selected.

## Stage 1 — Classify the request

Classify into one of these routes before editing:

- **A. Zero-to-one:** new product, new substantial feature, new visual system, or screen family with unresolved UX.
- **B. Existing redesign:** an existing interface/flow needs UX/UI improvement or substantial visual change.
- **C. Small change:** local correction with no meaningful effect on flow, IA, behavior contracts, shared-component output, or design-system semantics.
- **D. Specialist-only:** e.g. accessibility audit, animation review, responsive adaptation, or UX copy where the surrounding design is already settled.

When uncertain between A and B, treat an existing working interface as B. When uncertain between C and B, choose B unless all low-risk conditions in `references/workflow-small-change.md` are satisfied.

## Stage 2 — Establish project context

Load `references/fallback-ui-ux-context.md` unless an available external specialist already performs equivalent context initialization.

At minimum inspect what exists and is relevant:

- PRODUCT.md / product documentation
- DESIGN.md / design decisions
- routes and navigation
- current rendered screens or screenshots
- design tokens / CSS variables / theme
- component primitives and shared components
- state/data semantics and important API contracts
- tests/stories/snapshots where they encode behavior
- neighboring surfaces that establish conventions

Do not redesign during context discovery.

## Stage 3 — Clarify only material unknowns

Load `references/fallback-ui-ux-clarify.md` whenever a material unknown remains.

For an **existing redesign**, first identify the most important problems from evidence, then present those findings and ask the smallest number of directional questions. Do not ask the user to diagnose the UI for you.

For **zero-to-one**, clarify the intended user, core task, success condition, platform/surface, critical constraints, and whether the user has a strong reference or visual direction only when those facts cannot be inferred.

Do not proceed into irreversible or broad implementation with unresolved material questions.

## Route A — Zero-to-one full workflow

Read `references/workflow-zero-to-one.md`, then execute the necessary stages in order. Skip a stage only when its decision is already settled and evidenced.

Default sequence:

1. Context
2. Material clarification
3. User/problem/reference research
4. Product/UX strategy
5. End-to-end journey / task flow
6. Information architecture / navigation
7. Wireframe / low-fidelity screen structure
8. **User checkpoint: UX structure**
9. Visual direction
10. Design system / tokens / component language
11. Preview prototype or visual demo
12. **User checkpoint: visual/interaction direction**
13. Freeze implementation contract
14. Production implementation
15. Edge-case hardening + responsive + accessibility + localization concerns
16. UX writing/onboarding/accessibility/responsive specialists as needed
17. Purposeful motion only if warranted
18. Define measurement/validation when the outcome should be observed after release
19. Design/functional/regression QA
20. Handoff and durable documentation

Preferred external specialists by stage are defined in `references/capability-routing.md`. When absent, load the corresponding internal fallback playbook.

## Route B — Existing-product redesign full workflow

Read `references/workflow-redesign.md`.

Default sequence:

1. Context and current-state capture
2. Audit the actual user flow / screen family
3. Shared-component and regression impact map
4. Rank the highest-impact problems
5. **User checkpoint: problems, scope, and material choices**
6. Research mature references for the specific problems
7. Resolve journey / IA only if the audit found structural UX defects
8. Wireframe or structural prototype
9. Visual direction only to the degree needed
10. Preview demo with realistic content/states
11. **User checkpoint: approve one direction**
12. Freeze implementation contract
13. Implement with explicit shared-component propagation rules
14. Harden edge states / accessibility / responsive behavior
15. Regression + visual QA + smoke test
16. Update durable design decisions and handoff notes

**No medium/high-impact production UI edits before the preview is approved.**

## Route C — Small-change fast path

Read `references/workflow-small-change.md` and use it only if all low-risk conditions hold.

Even on the fast path:

- inspect the affected implementation first;
- determine whether the target is shared;
- preserve behavior;
- run targeted verification;
- do not smuggle in a redesign.

If a material question or wider impact appears, immediately promote the task to Route B.

## Route D — Specialist-only work

Use the narrowest relevant external specialist if available. Otherwise load the matching internal fallback playbook. Do not force the full design lifecycle when the product/UX direction is already settled and the requested task is genuinely isolated.

Examples:

- Accessibility → Intent include / Impeccable audit / Vercel guidelines, else `ui-ux-accessibility` + `ui-ux-qa`.
- Motion → Emil motion skills / Impeccable animate, else `ui-ux-motion`.
- UX copy → Intent articulate / Impeccable clarify, else `ui-ux-copy`.
- Onboarding/first run → Intent journey/articulate/include + Impeccable onboard, else `ui-ux-onboarding`.
- Responsive/cross-platform adaptation → Impeccable adapt / Intent transpose, else `ui-ux-responsive`.
- UI performance → Impeccable optimize / React best-practices, else `ui-ux-performance`.
- UX measurement → Intent measure or analytics specialist when available, else `ui-ux-measure`.

## External specialist ownership rules

Read `references/external-skill-adapters.md`. Core rules:

- **Intent** owns UX structure when available: strategize, investigate, journey, organize, wireframe, articulate, evaluate, fortify, include, transpose, localize, measure, specify.
- **Product Design** is strong for research, screenshot-grounded audit, visual ideation, prototypes, image/url-to-code, and design QA when the current ChatGPT surface supports it.
- **Impeccable** is the default existing-product UI craft/refinement/implementation specialist when available.
- **Taste** is a bounded visual-personality specialist, especially for landing pages or deliberate visual upgrades; it must not redefine product semantics or IA unless explicitly asked.
- **frontend-design** may serve as the single visual + frontend implementation authority for a stage when available and appropriate.
- **UI UX Pro Max** is primarily a design-system/visual-direction research tool for new products or missing design systems.
- **Emil skills** own specialist motion/prototyping work when present.
- **Figma/design-canvas tools** may be used for preview/design-system work when available; never require paid-only capabilities when a local HTML/CSS or existing free surface can satisfy the preview goal.
- **Vercel web-design-guidelines** and **react-best-practices** are quality gates, not visual art direction.

If two specialists could generate the visual direction, select one based on the surface and task. Others may critique after a direction exists but may not independently regenerate it in the same stage.

## Fallback subskills

When a required external specialist is unavailable, load the narrowest matching fallback:

- `references/fallback-ui-ux-context.md`
- `references/fallback-ui-ux-clarify.md`
- `references/fallback-ui-ux-research.md`
- `references/fallback-ui-ux-strategy.md`
- `references/fallback-ui-ux-journey.md`
- `references/fallback-ui-ux-ia.md`
- `references/fallback-ui-ux-audit.md`
- `references/fallback-ui-ux-impact.md`
- `references/fallback-ui-ux-wireframe.md`
- `references/fallback-ui-ux-visual-direction.md`
- `references/fallback-ui-ux-design-system.md`
- `references/fallback-ui-ux-prototype.md`
- `references/fallback-ui-ux-implementation.md`
- `references/fallback-ui-ux-harden.md`
- `references/fallback-ui-ux-copy.md`
- `references/fallback-ui-ux-onboarding.md`
- `references/fallback-ui-ux-responsive.md`
- `references/fallback-ui-ux-accessibility.md`
- `references/fallback-ui-ux-performance.md`
- `references/fallback-ui-ux-motion.md`
- `references/fallback-ui-ux-measure.md`
- `references/fallback-ui-ux-qa.md`
- `references/fallback-ui-ux-handoff.md`

Do not load every fallback up front. Load only the stage currently being executed.

## Preview / demo gate

Read `references/artifacts-and-gates.md` before medium/high-impact design work.

Choose the preview fidelity based on the uncertainty:

- flow/IA uncertainty → flow diagram + wireframe;
- layout/hierarchy uncertainty → wireframe or simple HTML/CSS;
- visual-language uncertainty → static visual mockup / available design canvas;
- interaction uncertainty → small interactive prototype;
- shared-component behavior uncertainty → isolated component/demo page with representative consumers.

Use realistic content and at least the important normal + empty/error/disabled/loading states relevant to the decision.

The user must approve a direction before production implementation, unless the task qualifies for the small-change fast path or the user has already explicitly approved an equivalent concrete visual target.

## Shared-component and regression gate

Read `references/component-regression.md` before editing a shared primitive or token.

For each proposed shared change, classify it:

- **Systemic defect:** the current shared behavior is wrong for all/most consumers → fix the primitive and verify representative consumers.
- **Local requirement:** only the target surface needs a different behavior → add/reuse a variant or composition; do not mutate every consumer.
- **Unclear propagation:** stop and ask a material question before implementation.

Map: target surface → direct components → shared primitives → tokens/themes → other consumers → behavior/data contracts → tests/stories/snapshots.

## Implementation contract

Before production edits on Route A or B, freeze a concise implementation contract containing:

- approved user flow and IA changes;
- approved preview/visual direction;
- in-scope screens/components;
- explicitly out-of-scope areas;
- preserved behavior/data contracts;
- shared-component changes and intended propagation;
- design tokens/components/libraries to reuse;
- required states and responsive behavior;
- acceptance and regression checks.

Do not reopen settled UX decisions during implementation unless code evidence reveals a concrete conflict. If so, surface the conflict rather than silently improvising.

## Final QA contract

Load `references/fallback-ui-ux-qa.md` or use available external QA specialists.

At minimum verify where applicable:

- primary task path and important alternate/failure paths;
- visual hierarchy and design consistency;
- keyboard/focus/accessibility basics;
- responsive behavior at representative widths;
- loading, empty, error, disabled, success, long-content states;
- shared-component consumers affected by the change;
- no unintended product/data/navigation behavior change;
- frontend implementation/performance issues introduced by the task;
- comparison against the approved preview/target.

Report remaining known issues explicitly. Do not claim full accessibility compliance from visual inspection alone.

## Completion

The task is complete only when the requested scope has:

1. a resolved UX/design direction;
2. user approval at required checkpoints;
3. implemented production changes if implementation was requested;
4. bounded verification and regression checks;
5. durable decisions documented when they should affect future work.

For audit-only or design-only requests, completion stops at the appropriate approved artifact; do not implement unless requested.
