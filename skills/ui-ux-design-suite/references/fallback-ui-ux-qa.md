# Final UI/UX QA

Read `../../references/quality-bar.md` and `../../references/component-regression.md`.

## Verify

1. Primary user task works end to end.
2. Relevant alternate/failure/empty/loading/disabled/success states work.
3. Rendered UI matches the approved target/preview in structure and intent.
4. Visual hierarchy, spacing, typography, color/state communication, and density are coherent.
5. Keyboard/focus basics and semantic/accessibility concerns are checked.
6. Representative desktop/mobile widths behave correctly where applicable.
7. Affected shared-component consumers are checked.
8. No unintended navigation/data/product behavior changed.
9. Framework-specific tests/lint/typecheck/build are run when appropriate and discoverable.
10. Frontend performance issues introduced by the change are addressed if meaningful.

## Bounded loop

- Pass 1: inspect, test, fix concrete issues.
- Pass 2: confirmation only.
- Continue only for a concrete unresolved blocker.

## Output
Report:

- what was verified;
- what was fixed;
- remaining known issues/limits;
- ship/readiness status for the requested scope.

Do not use QA as permission for a late redesign.
