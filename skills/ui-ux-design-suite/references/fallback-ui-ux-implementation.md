# Production Implementation

## Preconditions
For medium/high-impact work require an approved preview/target and an implementation contract.

## Procedure

1. Re-read affected implementation if file state may be stale.
2. Reuse project tokens, components, utilities, and conventions.
3. Use mature maintained accessible primitives already in the stack for dialogs, menus, comboboxes, toasts, etc. Do not hand-roll complex primitives without need.
4. If a new dependency is truly necessary, evaluate maintenance, license, dependency cost, integration risk, and replaceability.
5. Implement required normal and edge states.
6. Preserve data semantics, routes, API contracts, and existing behavior outside approved scope.
7. Apply shared-component changes according to the impact map; otherwise use local composition/variant.
8. Avoid unrelated cleanup/refactors.
9. Keep markup and state logic testable and semantically appropriate.

## Stop condition
If implementation reveals a concrete conflict with the approved UX/design contract, surface it. Do not silently improvise a new product decision.
