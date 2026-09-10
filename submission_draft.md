# Written Submission Draft — Ops COO 009

**Brief version: 2026-07**

> Working draft. Final submission must stay within the 2-page written limit; linked artifacts/diagrams are separate.

## 1. First 48 hours
My first goal is not understanding everything; it is reducing irreversible downside and restoring ownership.

**Hour 0–4:** freeze the failing auto-send path behind Q-08; block Q-11 and Q-16 pending source/legal/data review; open a senior-client incident on Q-15; validate Q-01 and merge Q-09 into it. Preserve logs before changing the systems.

**Hour 4–12:** assign every yellow/red item an owner, SLA and completion-evidence requirement. Reopen Q-13 because “done” without CRM evidence is not done. Validate Q-04, Q-17 and Q-18 before any external action.

**Hour 12–24:** close obviously invalid work (Q-14, Q-09, likely Q-06), complete reversible work already in review (Q-07), and batch low-signal alerts (Q-05/Q-12).

**Hour 24–48:** implement the first deterministic controls: active-client check, dedupe key, company/person validation before external send, source/provenance requirement for client metrics, and completion-evidence field.

My one sponsor session produces only four things: red-line categories, financial/contract authority thresholds, top-client list, and who can act as delegated senior approver. I do not use it for a listening tour.

## 2. Risk system
See `risk_policy.md`. Green auto-executes only when action is reversible, entity state is validated, there is no legal/sensitive-data exposure, confidence clears threshold, dedupe passes, and an owner/audit trail exist. Yellow requires operator review. Red requires a designated senior/executive decision.

A bad auto-approved action triggers containment, recovery, log preservation, root-cause classification, a deterministic guardrail where possible, replay on adjacent cases, and only then re-enable.

## 3. Portfolio audit
I would not keep eight workflows intact. Competitive monitoring is merged into one scored digest. Search/content is gated to active clients and ranked by expected impact. Prospect sourcing remains useful but auto-send is paused until identity and dedupe quality are proven. Customer-risk detection stays because expected value is high, but Q-01/Q-09 show duplicate handling is broken. Full decisions: `automation_portfolio.md`.

## 4. Operating edge
My strongest operating pattern is turning activity into a measurable decision system. [Observed] At NewCo/MyLife, I centered the operating model on new-trial volume and predicted trial LTV; the forecast used cohort demographics, payment method, and early cancellation behavior, and was recalibrated against realized cohorts. [Observed] Revenue increased 235% over six months and the business reached cash-flow break-even. Evidence tier should be stated only at the level I can substantiate with a checkable record.

[Observed] At Propel, I led product, engineering, data science and analytics for a platform processing >5B impressions/day. CTR/CVR predictions were translated into expected impression value and real-time bid decisions; [Observed] advertiser ROAS improved ~37%.

When I am not the domain expert, I do not ask an AI whether another AI is “good.” I define observable decision criteria, provenance and failure costs; calibrate scoring with domain experts on a sample; track false positives/negatives and realized outcomes; and escalate only uncertain/high-cost cases.

An AI-native COO designs the decision architecture: what machines can propose, what they can execute, what evidence is required, what humans own, and how outcomes update the system.
