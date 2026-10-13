# UI Performance

## Diagnose first
Do not optimize architecture based on intuition alone. Identify the user-visible issue and available evidence.

Prioritize meaningful causes such as:

- unnecessary rendering/re-renders;
- excessive client-side work;
- waterfalls/blocking work;
- oversized assets/fonts/images;
- expensive layout/paint/animation;
- list/table rendering cost;
- avoidable bundle/dependency cost;
- unstable loading/layout behavior.

## Procedure

1. Preserve the approved visual output and product behavior unless the bottleneck makes a change necessary.
2. Fix high-impact causes before micro-optimizations.
3. Prefer framework-native/existing solutions before new infrastructure.
4. Re-measure or at least reproduce the affected path after the change.
5. Avoid unrelated performance rewrites.

For React/Next.js, prefer an available `react-best-practices` specialist before this fallback.
