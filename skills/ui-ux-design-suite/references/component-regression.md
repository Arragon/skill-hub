# Shared Component and Regression Analysis

## Build the impact graph

For each target, trace:

```text
surface / route
  → direct components
  → shared composites
  → primitives
  → tokens / theme / CSS variables
  → other consumers
  → behavior/data contracts
  → tests / stories / snapshots
```

Do not stop at the file being edited.

## Classify every shared change

### Systemic defect

Evidence indicates the shared component/token is wrong for its intended role across consumers.

Action: fix the shared primitive, then verify representative consumers and variants.

### Local requirement

The target surface legitimately needs different layout, emphasis, density, or interaction.

Action: use composition, an existing variant, or a carefully scoped new variant. Do not change unrelated consumers.

### Unclear propagation

There is not enough evidence to decide whether the behavior is globally wrong or locally different.

Action: ask the user before implementation. Present the likely consequences of each choice.

## Functional regression checklist

Check relevant areas:

- click/keyboard behavior and focus order;
- forms and validation;
- loading/error/empty/success states;
- route transitions/back/cancel;
- permissions and destructive actions;
- responsive layout and overflow;
- theme/light/dark behavior;
- long labels/localization expansion;
- component variants in other consumers;
- data density and truncation;
- automation selectors/test assumptions if DOM structure changes.

## Scope rule

A UI task is not permission to refactor shared architecture for cleanliness. Refactor only when necessary for the approved result or when existing architecture makes the change unsafe; explain the reason.
