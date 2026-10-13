# UI/UX Context

## Goal
Build a reliable picture of the product and incumbent design without redesigning anything.

## Procedure

1. Read explicit user requirements first.
2. Read PRODUCT.md, DESIGN.md, architecture/know-how docs when relevant.
3. Inspect the actual target implementation before making design claims.
4. Identify routes/navigation, direct components, shared components, tokens/theme, data/state semantics, important tests/stories, and representative adjacent screens.
5. If rendered UI is available, inspect representative states rather than inferring appearance from code alone.
6. Distinguish:
   - user-confirmed facts;
   - evidence-confirmed project facts;
   - unknowns/inferences.
7. Record unresolved facts only if they could matter later.

## Output
Return a concise context brief:

- product purpose and primary user/task;
- target surface and current flow;
- incumbent design language;
- relevant technical/component constraints;
- reusable assets/components;
- unknowns that may become material questions.

## Prohibitions

- Do not modify production code.
- Do not invent product requirements.
- Do not normalize inconsistencies by silently redesigning them.
