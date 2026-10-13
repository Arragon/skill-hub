# Motion

## Decide whether motion is needed
Good reasons:

- feedback;
- spatial continuity;
- state transition communication;
- orientation in a changing interface.

Bad reasons:

- making a static design feel expensive;
- slowing a high-frequency action;
- hiding weak hierarchy;
- adding novelty without task value.

## Implementation rules

- Prefer existing motion utilities/tokens.
- Avoid a new dependency for trivial effects.
- Animate performant properties when practical.
- Handle interruption, enter/exit, and repeated actions.
- Respect reduced-motion preferences.
- Gate hover effects for appropriate pointer devices.
- Keep durations/easing consistent with product frequency and urgency.

## Review
Check whether the motion makes the task clearer/faster. Remove it if not.
