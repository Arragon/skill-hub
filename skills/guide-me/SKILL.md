---
name: guide-me
description: Guided problem discovery and framing. Use when the user may be describing a symptom, proxy goal, prematurely chosen solution, or imprecise requirement and discovering the real outcome could materially change the recommended direction.
---

# guide-me

Guided Problem Discovery & Framing.

Use this skill when the user's stated request may be a proxy for a deeper goal, a symptom rather than the real problem, an prematurely chosen solution, or an imprecise expression caused by limited domain knowledge.

The purpose is not to make the user's request more detailed. The purpose is to discover what actually needs to be solved and provide a useful direction.

## Core principle

> The user's proposed solution is evidence about their needs, not the definition of their needs.

Do not optimize a proposed implementation until the underlying outcome is sufficiently clear.

## When to use

Use `guide-me` when uncertainty about the real goal could materially change the recommended direction, especially when:

- the user asks which solution/tool/architecture to choose without a clear success condition;
- the user describes symptoms but not the outcome they need;
- the proposed solution appears much more specific than the stated problem;
- requirements conflict or keep changing;
- the user explicitly says they do not know what they really need;
- domain knowledge may prevent the user from knowing the relevant options;
- solving the literal request may leave the underlying problem unchanged.

Do not use it merely because some details are missing. If the task is straightforward and the missing information would not materially change the answer, answer directly.

## Workflow

### 1. DETECT

Identify the current stated request and ask internally:

- What outcome is the user actually trying to obtain?
- Is the request a goal, a constraint, a symptom, or already a candidate solution?
- If I solved the literal request perfectly, could the user's real problem remain unsolved?

Escalate only when problem-definition uncertainty is decision-relevant.

### 2. DISCOVER

Ask only high-information questions needed to uncover the real problem.

Prefer questions about outcomes before implementation preferences.

Useful targets include:

- desired observable outcome;
- current pain or failure;
- minimum acceptable success;
- hard constraints versus assumed constraints;
- what must remain true even if the proposed solution changes;
- what has already been tried and why it failed.

Do not run a generic interview checklist. Ask the smallest number of questions that can change the direction.

When the user cannot reasonably know the answer because it depends on domain knowledge, do not push the decision back to them. Investigate or apply professional judgment instead.

### 3. INVESTIGATE

When external knowledge could materially expand or correct the solution space, investigate it.

Examples:

- existing tools or standards the user may not know exist;
- technical constraints that make the proposed approach unnecessary or unsuitable;
- mature open-source implementations;
- platform capabilities that already solve part of the problem;
- real-world practices that change what is practical.

Do not ask the user to choose among options they cannot reasonably know exist.

Keep investigation proportional to the decision. Do not turn problem discovery into an open-ended research project.

### 4. FRAME

Reconstruct the problem using four objects:

**Root Goal**  
The outcome actually desired.

**Minimum Success Condition**  
The smallest observable result that would count as solved.

**Hard Constraints**  
Constraints that genuinely bound the solution space.

**Problem Statement**  
A concise formulation of how to achieve the Root Goal under the Hard Constraints while satisfying the Minimum Success Condition.

Separate these from candidate solutions, preferences, historical baggage, and speculative future needs.

### 5. REDUCE

Classify accumulated requirements only when useful:

- `ESSENTIAL` — required for the real goal or minimum success;
- `SUPPORTING` — useful but not necessary for initial success;
- `OPTIONAL` — preference or enhancement;
- `DISTRACTION` — does not materially contribute to the real goal.

Do not confuse a detailed requirement list with better understanding.

### 6. GUIDE

Provide a direction, not merely a cleaned-up requirements document.

State:

- what the real problem appears to be;
- what success actually requires;
- what can be ignored or deferred;
- what direction you recommend and why;
- any single unresolved issue that genuinely blocks the direction.

If the current user-proposed approach is still the best option, say so. The goal is not to replace the user's idea; it is to test whether it is solving the right problem.

## Stop condition

Stop when the real problem, minimum success condition, and relevant constraints are sufficiently clear to choose a direction.

Do not keep interviewing merely to increase confidence or detail.

If another distinct problem remains—such as uncertain external facts, unnecessary complexity, or an uncertainty better resolved by testing—identify it without silently expanding this skill into a different workflow.

## Guardrails

Never:

- assume the user's proposed implementation is the true requirement;
- ask questions whose answers would not change the direction;
- force the user to supply domain knowledge the agent can reasonably obtain;
- convert every vague request into a lengthy discovery session;
- optimize requirement volume;
- hide behind "it depends" when a professional recommendation can be made;
- continue discovery after the decision-relevant problem is already clear.

## Default output

Keep the result compact unless the problem is genuinely complex.

Suggested structure:

```text
What I think the real problem is:
...

Minimum success:
...

What matters / what does not:
...

Recommended direction:
...

Remaining critical unknown, if any:
...
```

## Success criterion

The skill succeeds when the user leaves with a better-defined problem and a more useful direction than they would get from solving the literal wording of the original request.
