# UI/UX Quality Bar

Use this as a final reasoning checklist, not as a mandate to optimize every dimension on every task.

## UX

- Primary task is obvious and efficient.
- Information grouping matches the user's mental model.
- Navigation and labels are predictable.
- Destructive/irreversible actions are safe.
- Feedback explains what happened and what to do next.
- Recovery paths exist where failure is realistic.

## Visual hierarchy

- Primary, secondary, and tertiary information are distinguishable.
- Spacing and alignment encode structure.
- Density fits the product and frequency of use.
- Typography hierarchy is consistent and readable.
- Color communicates priority/state rather than decoration.

## Interaction

- Interactive elements have clear affordances and states.
- Keyboard/focus behavior is coherent.
- Motion is purposeful, interruptible where needed, and supports reduced motion.
- Loading does not cause unnecessary layout instability.

## System coherence

- Existing tokens/components are reused where appropriate.
- New variants are justified by repeated or durable needs.
- No parallel design system is introduced.
- Shared changes have known consumers and explicit propagation intent.

## Accessibility and resilience

- Semantics, labels, focus, contrast, target size, color-independent state communication, and reduced-motion concerns are addressed where relevant.
- Empty, partial, error, slow, permission-denied, disabled, success, long-content, narrow viewport, and localization expansion states are considered based on actual product behavior.

## Anti-slop / anti-generic rules

Avoid defaults without product justification: excessive card grids, gratuitous purple gradients, giant rounded containers, indiscriminate glassmorphism, decorative charts, too many pills, weak gray-on-gray hierarchy, huge whitespace in high-density tools, and motion added only to look sophisticated.
