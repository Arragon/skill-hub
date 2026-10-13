# Small-Change Fast Path

Use only when **all** of these are true:

- The requested change is local and reversible.
- It does not change user flow, IA, navigation, data semantics, permissions, or behavior contracts.
- It does not require changing the output of a shared primitive across unrelated consumers.
- It does not introduce a new design-system rule.
- The intended result is unambiguous from the request and current project conventions.
- The change can be validated with a targeted rendered check and relevant tests/smoke path.

Examples: fixing a misaligned icon, correcting an obvious spacing inconsistency, using an existing semantic token instead of a hard-coded equivalent, repairing a broken focus ring using the existing pattern.

## Procedure

1. Inspect the affected implementation and nearest visual context.
2. Confirm whether the target component/token is shared.
3. Make the smallest change that satisfies the request.
4. Render/check the affected state.
5. Run targeted verification.
6. Stop. Do not use the request as permission for wider redesign.

## Promote to full redesign when

- the local fix exposes a structural issue;
- the target is shared and propagation is unclear;
- the user request is aesthetic but under-specified;
- multiple screens must change coherently;
- the fix requires new tokens/components or changed interaction semantics.
