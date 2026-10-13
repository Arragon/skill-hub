# Preview / Prototype

Read `../../references/artifacts-and-gates.md`.

## Select fidelity by uncertainty

- Flow/IA unclear → flow diagram + wireframe.
- Layout/hierarchy unclear → wireframe or simple HTML/CSS.
- Visual language unclear → static mock / available design canvas.
- Interaction unclear → lightweight interactive prototype.
- Shared component behavior unclear → isolated component demo with representative variants/consumers.

## Requirements

1. Keep preview code/artifacts separate from production unless the environment explicitly supports safe prototype branches.
2. Use realistic content, not lorem ipsum when content shape matters.
3. Include the states required to judge the design decision.
4. Make alternatives genuinely different only when a decision tradeoff exists.
5. Explain what the user is being asked to approve.

## Approval gate
Do not promote the preview to production implementation until the user approves one concrete direction, except on the documented small-change path.
