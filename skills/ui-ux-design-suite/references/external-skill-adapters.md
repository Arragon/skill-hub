# External Skill Adapters

These adapters describe how to use external specialists **inside** the suite without surrendering process control.

## Intent

Use Intent for UX structure when available. Relevant capabilities from the source manual include `strategize`, `investigate`, `journey`, `organize`, `wireframe`, `articulate`, `evaluate`, `fortify`, `include`, `transpose`, `localize`, `measure`, and `specify`.

Adapter contract:

- Provide product facts and already-approved constraints.
- Tell it not to implement code during UX-definition stages.
- Require explicit happy path, decision points, back/cancel/recovery, failure paths, completion states, and relevant edge cases.
- Treat its output as the UX contract for subsequent visual work once approved.

## Product Design

Use when the current surface supports it and the task benefits from screenshot-grounded audit, current UX research, visual ideation, prototype creation, or design QA.

Adapter contract:

- For audit, insist on evidence from the actual current flow/screens.
- For ideation, provide the brief, constraints, project design context, and any current screenshots/reference material.
- Do not let ideation bypass the suite's user approval gate.
- For image/url-to-code, use only after a concrete visual target has been selected.
- For design QA, compare against the approved target rather than a newly invented target.

## Impeccable

Default product-UI craft/refinement specialist when available. Use narrowly: `shape`, `critique`, `layout`, `typeset`, `colorize`, `distill`, `bolder`, `quieter`, `clarify`, `adapt`, `harden`, `audit`, `polish`, etc.

Adapter contract:

- Read PRODUCT.md and DESIGN.md first when present.
- Reuse incumbent tokens/components.
- Do not create a parallel design system.
- Route structural UX defects back to journey/IA/wireframe instead of trying to fix them with styling.
- `polish` may refine the approved direction but may not redesign it.

## Taste

Use as a bounded visual-personality consultant or primary visual authority for clearly visual landing/portfolio work.

Adapter contract:

- Preserve product semantics, navigation, user flow, data structure, and reusable component contracts unless explicit change is approved.
- For existing product UI, prefer `redesign-existing-projects` as a consultant after diagnosis.
- Do not mix multiple Taste modes or combine Taste with another independent visual generator on the same stage.

## frontend-design

If the environment exposes a `frontend-design` skill and its description matches the task, it may act as the single visual + implementation authority for the selected stage.

Adapter contract:

- Feed it the approved UX structure, preview direction, DESIGN.md, and implementation contract.
- It must not reopen settled UX decisions without evidence of a concrete implementation conflict.
- Other visual skills become reviewers only for that stage.

## UI UX Pro Max

Use primarily for zero-to-one design-system exploration or when a coherent visual system does not exist.

Adapter contract:

- Ask for genuinely distinct directions, not minor palette variations.
- Require rationale, density, typography roles, semantic color strategy, spacing, radius/border/shadow language, component/navigation language, motion level, accessibility, and anti-patterns.
- Select one direction; never average several directions into a generic compromise.
- Convert the selected durable decisions into DESIGN.md before implementation.

## Emil motion/prototype skills

Use for specialist motion or prototype work.

Adapter contract:

- Motion must serve feedback, spatial continuity, or state communication.
- Reject motion on high-frequency interactions where immediacy is better.
- Include reduced-motion behavior and interruption/exit handling.
- Prototype variants should differ in interaction/composition strategy, not just color/radius.

## Figma / design-canvas tools

Use when already available and helpful, especially for shareable review or design-system work.

Adapter contract:

- Do not make Figma a hard dependency.
- Prefer existing free/available capabilities; fall back to local HTML/CSS or static wireframe when paid-only features would be required.
- Keep the preview disposable until the user approves it; production code remains separate.

## Vercel web-design-guidelines / react-best-practices

Use as implementation QA gates.

Adapter contract:

- Fix concrete violations introduced or exposed by the task.
- Do not change the approved visual direction.
- Do not perform unrelated architecture rewrites.
- React best-practices is relevant only to React/Next.js code.
