# Capability Routing Matrix

Use this file after capability discovery. Availability means the skill/tool is both installed/exposed **and usable in the current surface**.

| Stage | Preferred external capability when available | Fallback |
|---|---|---|
| Product context / incumbent design documentation | Impeccable `init` / `document` where appropriate | `ui-ux-context` |
| Product/problem research | Product Design `research`; Intent `investigate` | `ui-ux-research` |
| Strategy / root UX direction | Intent `strategize` | `ui-ux-strategy` |
| Existing UX evaluation | Product Design `audit`; Intent `evaluate`; Impeccable `critique` for UI-oriented diagnosis | `ui-ux-audit` |
| Journey / task flow | Intent `journey` | `ui-ux-journey` |
| IA / navigation / taxonomy | Intent `organize` | `ui-ux-ia` |
| Wireframe / screen structure | Intent `wireframe`; Product Design ideation only when visual exploration is actually needed | `ui-ux-wireframe` |
| Visual direction for product UI | Impeccable by default; Product Design `ideate` when image-based variants help; `frontend-design` may be selected as sole visual authority | `ui-ux-visual-direction` |
| Strong visual personality / landing surface | Taste `design-taste-frontend` / `high-end-visual-design` when suitable | `ui-ux-visual-direction` |
| Existing product bounded visual upgrade | Impeccable `critique` + optionally Taste `redesign-existing-projects` as consultant | `ui-ux-visual-direction` |
| New design-system direction | UI UX Pro Max; Figma design-system capabilities if already available | `ui-ux-design-system` |
| Prototype / variants | Product Design prototype/ideation; Impeccable `live`; Emil `prototype`; Figma if available | `ui-ux-prototype` |
| Implementation | Impeccable; `frontend-design`; Product Design image/url-to-code for a selected target where supported | `ui-ux-implementation` |
| Edge cases / resilience | Intent `fortify`; Impeccable `harden` | `ui-ux-harden` |
| UX copy / terminology | Intent `articulate`; Impeccable `clarify` | `ui-ux-copy` |
| Onboarding / first run | Intent `journey` + `articulate` + `include`; Impeccable `onboard` | `ui-ux-onboarding` |
| Accessibility design | Intent `include`; Impeccable `audit`; Vercel web-design-guidelines | `ui-ux-accessibility` + `ui-ux-qa` |
| Responsive / platform adaptation | Impeccable `adapt`; Intent `transpose` | `ui-ux-responsive` |
| Localization | Intent `localize` | `ui-ux-harden` |
| UI performance | Impeccable `optimize`; React `react-best-practices` | `ui-ux-performance` |
| UX measurement | Intent `measure`; product analytics specialist when actually connected | `ui-ux-measure` |
| Motion | Emil `find-animation-opportunities` / `animate` / `review-animations`; Impeccable `animate` for ordinary refinement | `ui-ux-motion` |
| Frontend QA | Impeccable `audit`/`polish`; Product Design `design-qa`; Vercel `web-design-guidelines`; React `react-best-practices` | `ui-ux-qa` |
| Engineering handoff | Intent `specify` | `ui-ux-handoff` |

## Selection rules

1. Use the narrowest expert that exactly matches the stage.
2. Do not use a specialist merely because it is available.
3. Do not ask two generative visual specialists to independently redesign the same surface in the same stage.
4. An audit specialist may critique a chosen direction after generation; it must not silently create a second competing design.
5. External skill output is advisory when it conflicts with explicit user requirements, PRODUCT.md, DESIGN.md, existing behavior contracts, or the approved implementation contract.
6. If an external skill is unavailable in the current mode (for example, it requires Work mode or another product), treat it as unavailable and use fallback.
7. Missing specialists are not blockers: use fallback. Do not auto-install unless requested.

## Optional reference/data tools

Reference/data tools such as Mobbin, public web search, product analytics, or design repositories may improve evidence. They are inputs, not design authorities. Do not require paid access. Prefer accessible public references and the project's own design evidence when sufficient.
