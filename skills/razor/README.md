# Razor v1.2

A general-purpose Occam's Razor convergence-review skill.

`$razor` is an explicit ChatGPT invocation convention, not the only trigger. The skill should also activate when the user's intent clearly calls for convergence, assumption checking, scope reduction, overengineering review, or a return to the original need.

Package structure:

- `SKILL.md` — universal core
- `references/engineering.md` — optional engineering-specific review rules
- `references/product.md` — optional product-specific review rules

Design goals:

- general-purpose rather than engineering-first;
- efficient core prompt;
- ask only necessary questions;
- domain rules loaded only when relevant;
- review and convergence only;
- converge to a Minimum Sufficient Solution;
- English-only content for consistency.
