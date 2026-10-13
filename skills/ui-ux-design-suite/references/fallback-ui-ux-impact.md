# UI Change Impact Map

Read `../../references/component-regression.md`.

## Procedure

1. Identify the target route/surface.
2. Trace direct components and shared composites/primitives.
3. Trace tokens/theme/CSS variables touched by the proposal.
4. Find representative other consumers.
5. Identify behavior/data/test contracts coupled to the markup/component.
6. Classify each shared change as:
   - systemic defect;
   - local requirement;
   - unclear propagation.
7. For unclear propagation, trigger the material-question gate.

## Output
Produce a compact table/map:

- proposed change;
- shared/local target;
- expected consumers;
- propagation intent;
- regression checks;
- uncertainty/blocker.
