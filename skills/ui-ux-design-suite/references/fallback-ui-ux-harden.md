# Harden the Experience

Consider only states the product can realistically represent.

## State inventory
Where relevant verify/design:

- initial/loading/slow loading;
- no data / partial data;
- invalid input / validation failure;
- permission denied/auth boundary;
- backend/network failure;
- stale/concurrent state;
- retry and repeated action;
- destructive action confirmation/recovery;
- disabled/submitting/success;
- long text / large numbers / truncation;
- narrow/wide viewport;
- localization expansion / RTL if applicable;
- keyboard-only path;
- focus order/restoration;
- screen-reader semantics/announcements where applicable;
- color-independent state communication;
- target size / motor accessibility;
- reduced motion.

## Responsive principle
Do not simply shrink desktop. Re-evaluate content priority, navigation collapse, controls, tables/lists, wrapping, sticky/fixed elements, and modal/drawer behavior.

## Accessibility claim limit
Do not claim full WCAG compliance unless the required testing actually occurred.
