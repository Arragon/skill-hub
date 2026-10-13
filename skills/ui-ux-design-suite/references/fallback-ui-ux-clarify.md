# Material Clarification

## Principle
Ask less, but ask before guessing on decisions that matter.

## Material question test
A question is material only if two plausible answers would lead to meaningfully different implementation or design decisions.

Common material unknowns:

- primary user or core task;
- allowed changes to navigation/IA/flow;
- redesign scope and non-goals;
- whether a shared component change should propagate globally;
- target platform/responsive requirement;
- conservative refinement vs deliberate visual repositioning;
- compatibility/accessibility constraints;
- acceptance condition.

## Procedure

1. First inspect available evidence; do not ask what can be inferred safely.
2. Identify at most the smallest set of blocking material questions.
3. For each question provide:
   - why it matters;
   - recommended default;
   - consequence of choosing the main alternative.
4. For an existing redesign, present the diagnosed high-impact issues before asking the user to choose a direction.
5. Stop before broad/irreversible implementation until blocking questions are resolved.

## Do not ask about

- cosmetic details already governed by DESIGN.md;
- trivial reversible choices;
- facts visible in the code/UI;
- speculative future requirements unrelated to the current success condition.
