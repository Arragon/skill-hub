# Artifacts and Decision Gates

The suite is process-driven, not document-driven. Create only artifacts that reduce uncertainty or preserve durable decisions.

## Suggested artifacts

- **Product/design brief** — short statement of user, task, success, constraints, and non-goals.
- **Audit report** — evidence-backed problems ranked by impact.
- **Impact map** — shared components, tokens, consumers, behavior contracts, tests.
- **UX spec** — approved journey, IA, screen/state requirements.
- **Wireframe/prototype** — preview used for user review.
- **DESIGN.md update** — only durable visual/system decisions.
- **Implementation contract** — frozen scope and acceptance checks before production edits.
- **QA report** — what was tested, what passed, remaining risks.

## Gate 1 — Material questions

Do not ask a generic discovery questionnaire. Ask only when an answer could materially change:

- primary user/task;
- flow or IA;
- scope;
- shared-component propagation;
- platform/responsive expectations;
- visual positioning;
- compatibility constraints;
- acceptance criteria.

Each question should include the recommended default and why.

## Gate 2 — UX structure approval

Required for zero-to-one work when journey/IA/wireframe is newly defined or materially changed.

## Gate 3 — Preview approval

Required before medium/high-impact production UI changes unless the user already supplied and approved an equivalent concrete target.

Do not treat vague praise such as “looks okay” from a different earlier concept as approval for a new variant. Approval must clearly refer to the direction being implemented.

## Gate 4 — Shared propagation decision

Required before changing a shared primitive/token when it is unclear whether all consumers should change.

## Gate 5 — Ship/closeout

Require bounded QA results and remaining known issues. Do not equate “code compiles” with UI/UX completion.
