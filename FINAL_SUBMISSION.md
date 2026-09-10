# Ops COO 009 — Final Written Submission

**Brief version: 2026-07**

## 1. First 48 hours: stabilize downside, restore ownership

I would not begin with a listening tour. I would first stop irreversible damage, then restore ownership and only then optimize the system.

**Immediate containment:** pause the auto-send path behind **Q-08**; block **Q-11** pending contract/legal verification; block **Q-16** pending provenance/client-data review; open a senior-client incident for **Q-15**; validate **Q-01** and collapse duplicate **Q-09** into it. Preserve logs before changing automation behavior.

**Same-day ownership:** every open yellow/red item gets one accountable owner, an action deadline, and completion evidence. Reopen **Q-13** because “done” without CRM evidence is not done. Validate **Q-04**, **Q-17**, and **Q-18** before any external action. Close invalid/stale work such as **Q-14**; likely close **Q-06** as a service failure to learn from rather than a useful current task. Complete reversible work already in review such as **Q-07**. Batch low-signal monitoring **Q-05/Q-12** rather than interrupting operators repeatedly.

**By the end of the second day:** add deterministic controls for active-client state, deduplication, person/company validation before external sends, provenance for client performance numbers, and completion evidence. Full ordering and ownership are in [`triage_board.csv`](triage_board.csv).

My single sponsor session should produce only four decisions: red-line categories, contract/financial authority thresholds, the small set of strategically critical clients, and delegated senior approvers. The sponsor should not become a permanent queue processor.

## 2. Risk tiering: autonomy should be earned

The system is operationalized in [`risk_policy.md`](risk_policy.md) and [`decision_tree.md`](decision_tree.md).

**GREEN — auto-execute / batch review:** reversible, low-downside work with validated entity state, no legal/sensitive-data exposure, no duplicate, adequate confidence, a named owner, and an audit trail.

**YELLOW — operator review:** external communication, ambiguous context, moderate commercial/reputational downside, missing/conflicting state, low confidence, or potential duplication.

**RED — senior/executive review:** legal/contractual exposure, sensitive/client-data disclosure, high-value customer risk, costly/irreversible action, or a confirmed automation failure with external impact.

If a green item should not have passed, I would contain the affected workflow, recover externally if needed, preserve the evidence trail, classify the failure (bad data, stale state, model error, policy error, integration error), add a deterministic guardrail where possible, replay the failure plus adjacent cases, and only then restore autonomy. One bad workflow should not shut down unrelated automations.

## 3. Automation portfolio: fewer workflows, stronger closed loops

I would not keep all eight workflows intact. The audit is in [`automation_portfolio.md`](automation_portfolio.md).

- **KEEP + FIX customer-risk detection:** high potential value, but dedupe and closed-loop ownership are mandatory; Q-01/Q-09 expose duplicate-generation while Q-15 demonstrates the value of a genuine high-risk signal.
- **IMPROVE prospect sourcing; pause auto-send:** Q-08 and Q-17 show identity-quality and dedupe failures. Sourcing can continue, but sending earns autonomy only after measured reliability improves.
- **MERGE competitive monitoring:** Q-05/Q-12 show alert inflation. Convert to one ranked digest and escalate only when there is a concrete client, revenue, or strategic implication.
- **IMPROVE content repurposing:** retain drafting leverage, but require provenance for client metrics and explicit approval ownership; Q-16 is a red-line failure.
- **IMPROVE deal revival:** every recommendation needs owner, next action, and completion evidence; Q-13 proves status alone is not evidence.
- **IMPROVE search/content scan:** gate to active clients and rank by expected impact; Q-14 shows stale customer state can invalidate the whole recommendation.
- **SHRINK editorial planning:** keep only work tied to explicit client/company priorities.
- **IMPROVE candidate/partner follow-up:** validate current relationship/employer context before sending; Q-18 shows why.

My kill rule is simple: pause or retire workflows when attributable outcome value is persistently low, signal quality is poor, or review/cleanup cost exceeds the value created.

## 4. Operating edge

### AI fluency

[Observed] At **NewCo/MyLife**, I centered the operating model on new-trial volume and predicted trial LTV. The forecast used cohort demographic attributes, payment-method attributes, and early cancellation behavior; we measured forecast-versus-realized accuracy and recalibrated the model. [Observed] Revenue increased **235%** over six months and the business reached cash-flow break-even. I will claim only the evidence tier I can support with a checkable record.

[Observed] At **Propel Media**, I led product, engineering, data science, and analytics for an advertising marketplace processing **>5B impressions/day**. CTR/CVR predictions were translated into expected impression value and real-time bid decisions. [Observed] Advertiser ROAS improved approximately **37%**.

My current work extends the same operating pattern into agentic systems. At **[davidwolfe.app](https://davidwolfe.app/)** I have built working prototypes including **Agent-Managed Acquisition**, **Retention Risk Command Center**, and **Pricing Experimentation Control Tower**. Across them, the recurring architecture is: **signal → scoring/prioritization → bounded agent action → operator control → measured economic outcome**. The point is not “AI automation” by itself; it is a decision system with explicit policies, auditability, and economic feedback.

When I am not the domain expert, I do not rely on an AI judging another AI in the abstract. I define observable decision criteria, provenance requirements, and failure costs; calibrate the grader with domain experts on a sample; measure false positives/negatives and realized outcomes; and reserve human review for uncertain or high-downside cases.

An AI-native COO owns the decision architecture: what machines may propose, what they may execute, what evidence is required, what humans retain, and how outcomes update the policy/model.

### Operating rhythm and follow-through

I have repeatedly inherited fragmented operating environments. My pattern is: one metric tree, one operating review, explicit owners, short-cycle decisions, and forecast-versus-actual learning. At NewCo/MyLife, product, marketing, payments, staffing, and investment decisions were tied to the same forward economic model rather than separate functional narratives.

Processes are followed when the system makes the desired behavior easier than bypassing it. I use required fields, deterministic gates, clear ownership, visible aging/SLA exceptions, and completion evidence—not policy documents as the primary control. The weekly cadence in [`operating_cadence.md`](operating_cadence.md) escalates only exceptions and cross-functional tradeoffs.

### Working style

Under ambiguity I am strongest at **starting, prioritizing, and turning fuzzy situations into measurable operating systems**. I am comfortable making provisional decisions with incomplete information when downside is bounded, then updating quickly as evidence improves.

My guardrail: I can move too quickly into architecture/model-building when a simpler operational fix would work. I compensate by forcing an early question: *what is the cheapest reversible intervention that will tell us whether this matters?* I also value complementary partners who are stronger at sustained administrative follow-through once the operating design is stable.

A recurring adjustment from feedback over my career has been to separate **decision quality from analytical completeness**: build enough model to make the next decision, act, measure, then deepen the model only when the result justifies it.

---

**Artifact index:** [`triage_board.csv`](triage_board.csv) · [`risk_policy.md`](risk_policy.md) · [`decision_tree.md`](decision_tree.md) · [`automation_portfolio.md`](automation_portfolio.md) · [`operating_cadence.md`](operating_cadence.md) · [`evidence_log.md`](evidence_log.md) · [`ai_usage.md`](ai_usage.md)
