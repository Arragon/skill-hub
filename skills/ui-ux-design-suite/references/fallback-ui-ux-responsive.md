# Responsive / Platform Adaptation

## Web responsive
Do not merely scale the desktop UI down. Re-evaluate:

- content priority;
- navigation collapse/placement;
- control reachability and touch targets;
- tables vs lists/cards/overflow strategies;
- wrapping/truncation;
- fixed/sticky elements;
- modal/drawer/sheet behavior;
- dense data presentation;
- keyboard vs touch expectations.

Verify representative narrow and desktop widths, plus tablet/intermediate behavior when it is materially different.

## Cross-platform transpose
When moving desktop↔mobile or web↔native:

1. Identify invariant user intent and product semantics.
2. Identify interaction patterns that must change for the target platform.
3. Adapt navigation, inputs, density, content priority, and platform affordances.
4. Preserve continuity of terminology and core mental model where reasonable.

Do not force desktop conventions onto mobile merely for visual consistency.
