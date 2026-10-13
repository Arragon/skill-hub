# CTO Technical Review Framework

Use this reference for comprehensive technical decisions. Select only dimensions that can change the recommendation.

## Stage gates

| Stage | Evidence required before the next commitment |
| --- | --- |
| Discovery | Outcome, system boundary, current pain, constraints, stakeholders, and riskiest assumptions are explicit |
| PoC | One uncertain mechanism works under representative conditions; limitations and non-goals are recorded |
| MVP/pilot | Small end-to-end path, real users/data, acceptance metrics, failure handling, instrumentation, and operational owner |
| Production | Security review, capacity evidence, SLOs, observability, runbook, backup/restore, rollout/rollback, support ownership |
| Migration | Compatibility, data reconciliation, dual-run/cutover plan, rollback boundary, downtime and loss budgets |
| Scale | Measured bottleneck, capacity model, cost curve, fault isolation, governance, and team ability to operate added complexity |

Do not apply production overhead to a disposable PoC or treat PoC success as proof of production readiness.

## Technical intake

Capture:

- Decision and desired outcome.
- Current architecture, pain, incidents, and technical debt.
- Users, traffic/workload shape, data volume/growth, geography, and peak behavior.
- Data classification, privacy, security, regulatory, and audit requirements.
- Availability, latency, throughput, consistency, recovery, and support expectations.
- Team skills, ownership, budget, timeline, procurement, and deployment constraints.
- Fixed integrations, platforms, licenses, network boundaries, and legacy compatibility.
- Reversibility: what is cheap to change later and what becomes structural.

Unknowns should become questions, assumptions, or experiments—not silent defaults.

## Quality attributes

| Dimension | Review questions | Warning signs |
| --- | --- | --- |
| Correctness | What invariants and acceptance criteria must always hold? How are errors detected and repaired? | Happy-path-only design; ambiguous source of truth |
| Security/privacy | Assets, actors, trust boundaries, threats, least privilege, secrets, encryption, retention, audit, incident response? | Security postponed; shared credentials; excessive data |
| Reliability | Failure modes, timeouts, retries, idempotency, backpressure, redundancy, recovery objectives, degraded mode? | Retry storms; hidden single points; no restore test |
| Performance | Representative latency/throughput targets? Where are queues, hot paths, and expensive operations? | Benchmarks on toy data; optimizing without a target |
| Scalability | Which dimension grows, to what range, and what measured bottleneck requires change? | “Internet scale” without demand; premature distribution |
| Data | Ownership, schema, lineage, quality, consistency, lifecycle, migration, backup, reconciliation? | Multiple sources of truth; irreversible schema change |
| Integration | Contracts, versioning, compatibility, rate limits, partial failure, vendor changes? | Tight coupling; undocumented implicit contracts |
| Operability | Logs, metrics, traces, alerts, runbooks, support path, deployment and rollback? | Dashboards without decisions; no owner on call |
| Maintainability | Clear boundaries, tests, documentation, upgrade path, dependency health, cognitive load? | Clever abstraction; framework proliferation |
| Cost | Fixed and variable drivers, peak cost, unit cost, support/egress/license cost, budget controls? | Free-tier economics; ignored human operations |
| Portability | Exit plan, data export, proprietary dependency, switching cost, contractual limits? | Accidental lock-in; abstraction with no realistic second provider |
| Delivery/team | Does the architecture match skills, staffing, ownership, schedule, and change capacity? | More services than owners; critical single expert |

## Architecture reasoning

Trace the system rather than naming patterns:

1. Define external actors and system boundary.
2. Identify components and single owners.
3. Trace request, event, and data flows end to end.
4. Mark state, source of truth, consistency needs, trust boundaries, and failure domains.
5. Describe behavior under timeout, duplicate, reordering, partial outage, overload, bad input, dependency failure, and rollback.
6. Define deployment, configuration, secrets, observability, support, and recovery.
7. Show how the design evolves if measured thresholds are crossed.

Prefer a modular monolith or managed service when it satisfies requirements and lowers cognitive/operational load. Choose microservices, event-driven systems, multi-region, Kubernetes, custom infrastructure, or elaborate abstraction only when a concrete constraint justifies their failure modes and operating cost.

## Option comparison

Always include plausible status quo/minimal-change and staged options. Compare with criteria derived from requirements, not generic fashion:

- Requirement coverage and correctness.
- Delivery time and migration risk.
- Security, reliability, performance, and operability.
- Team fit and ownership.
- Total cost and cost variability.
- Reversibility, portability, and lock-in.
- Complexity now versus optionality later.

Use must-have criteria as gates. Do not average away a failed critical requirement.

For build versus buy, include integration, customization, data rights, security review, procurement, SLA, pricing curve, exit/migration cost, vendor viability, and the opportunity cost of owning undifferentiated infrastructure.

## Evidence and estimation

Evidence generally strengthens from intuition/vendor claim → official documentation → minimal experiment → representative benchmark → staging under realistic load/failure → production telemetry over time.

For unstable versions, limits, compatibility, pricing, vulnerabilities, and product behavior, verify current primary sources. Distinguish measured, calculated, quoted, inferred, and assumed values.

Estimate with ranges and expose the model:

> load × work per unit × peak factor × redundancy/headroom × unit cost

Include uncertainty, dominant cost drivers, and sensitivity. Avoid precision unsupported by inputs.

## Risk register

For each material risk record: scenario/cause, likelihood, impact/blast radius, detectability, leading signal, prevention, mitigation, contingency/rollback, owner, and decision deadline.

Prioritize:

- **Blocker:** unsafe or unjustified to proceed.
- **Gate:** resolve before the next irreversible commitment.
- **Mitigate:** proceed with an explicit control and owner.
- **Monitor:** acceptable now with threshold and response.
- **Accept:** cost of mitigation exceeds risk within stated scope.

Use a pre-mortem: “Six months later this failed—what plausible chain caused it?” Prefer credible chains over dramatic edge cases.

## Execution and migration

Turn recommendations into:

1. Scope, non-goals, and architecture decision records.
2. Dependency order and thin end-to-end walking skeleton.
3. Spikes for uncertain mechanisms; production work only after their gates pass.
4. Phases with deliverables, owners, acceptance criteria, and stop conditions.
5. Test strategy: unit, contract, integration, end-to-end, load, security, chaos/recovery as proportionate.
6. Deployment strategy: feature flags, canary, shadow/dual run, incremental migration, or blue-green where justified.
7. Data migration: versioning, backfill, reconciliation, cutover, rollback, and deletion.
8. Operations: SLO/SLI, dashboards, actionable alerts, runbooks, support, backup/restore drills.
9. Technical-debt register with owner, trigger, and repayment window.

Prefer milestones that prove an outcome or retire a risk, not “finish component X.”

## AI and data systems

Also review:

- Baseline without AI and whether AI is necessary.
- Task-specific evaluation set, quality dimensions, acceptance thresholds, and human review.
- Model/provider/version traceability and reproducibility.
- Hallucination, prompt injection, data leakage, tool abuse, poisoning, and unsafe automation.
- Latency/token/cost budgets, routing, caching, rate limits, fallbacks, and graceful degradation.
- Retrieval/source quality, permissions, freshness, citations, deletion, and tenant isolation.
- Drift, regression tests, shadow evaluation, feedback quality, and rollback.

Do not treat model demos or aggregate benchmarks as proof of fitness for the user's workflow.

## Decision records and output controls

An ADR should contain: status/date; context; requirements/constraints; considered options; decision; rationale; positive/negative consequences; validation; rollout/rollback; revisit trigger.

A deep review should lead with the recommendation, then context, requirements, evidence gaps, options, proposed architecture, risk register, delivery/migration plan, verification/operations, and open decisions.

Avoid framework dumping, trend-driven architecture, premature optimization, false certainty, “rewrite everything,” security theater, unowned complexity, vague “best practices,” recommendations without migration paths, and plans with no rollback or success criteria.
