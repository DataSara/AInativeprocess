# Reprocess redesign patterns

Use these after classifying the current steps (Phase 3). Classification asks "how do we do today's step better?" These patterns ask "should this step exist in this shape at all?" Apply the ones that fit, and say why for each. **Every guardrail still applies**: Principle 5's human-accountability list, gates, "numbers come from rules or models, never LLM text", and the risk checklist.

Mode M = a statistical or machine-learning model (forecast, estimate, score), not an LLM. It needs: a baseline it must beat (the current method and a simple naive method), back-testing on past data, accuracy and bias monitoring, a named owner, and a documented fallback. Full governance list: risk checklist §M.

**Hard limit:** M never decides anything on Principle 5's list (money, commitments, prices shown to customers, decisions about individuals, safety, regulated sign-off), and "exceptions, not every item" never applies there. A model may inform; a human decides each item. **Exceptions reduce what a person reviews, never what the accountable approver signs.**
- **What counts as a commitment:** an order, contract, release, allowance or payment to an outside party (supplier, customer, carrier), or an authorization to spend. Internal planning proposals, and system-generated orders within parameters a human has approved, aren't new commitments; the parameters (limits, rules, order caps) are, and a human approves them and any change to them. Orders outside the parameters go to a person.
- **Keep and measure what exists first:** if a model or planning engine already does the step, measure it (accuracy, bias, against a naive method) before proposing a new or second model.
- **Data each designed AI step will read:** check its class and contents (e.g. supplier PDFs carry prices and bank details; emails carry personal data) against the risk checklist before proposing it. **Never design M to score, rank, filter or predict about individual candidates, workers or customers.** If the organization already uses such a tool, treat it as a decision about people: per-item human review, a bias audit where required, never C.
- **When not to use M:** no comparable history to back-test, or one-off judgements: then it's D (or B with evidence). At small volume, start with a simple rule (A), such as a moving average or a reorder point in a spreadsheet, and only move to M when there's enough history to show it beats the rule.
- **Figures:** an LLM never produces a figure. It may extract one (B) only with a check against structured data or the source.

## Core patterns
| Pattern | Today | AI-native | Guardrails |
|---|---|---|---|
| **Model-first, human challenge** | People type estimates (lift, effort, risk) that become the number | A model (M) proposes the number with a range; the human accepts or overrides with a reason. Both numbers are kept | Overrides are allowed and recorded; the model never has the final say on Principle 5 decisions; measure whether overrides help **by stage or role, not per person** (per-person tracking is performance monitoring: HR, privacy and works council first). No model-first scores about individuals (candidates, employees, customers) without HR or legal review and a bias audit |
| **Exceptions, not every item** | Every item is reviewed or discussed | Rules or M handle routine items; people review only items above a materiality or uncertainty threshold | **Never for Principle 5 items, key controls or safety:** by default (Reprocess's rule, not a legal requirement) exceptions change only the preparer's work and each approval stays item by item. Risk-based review of a key control is possible only with control-owner and auditor agreement. Thresholds set from the cost of an error; a random sample of routine items is still checked and kept; thresholds re-tightened when errors rise. If the review is a finance control (e.g. SOX), moving to exceptions is a control redesign: control owner and auditor sign-off first |
| **One versioned source of truth** | Spreadsheets emailed, copied and merged | One shared, versioned record (event register, plan version, case record) that every function reads | Locked snapshots for each approved version; who changed what, when; no side copies |
| **Fewer hand-offs** | A → B → C in sequence, each re-keying | Parallel contributions into the shared record; hand-offs replaced by status and alerts | Each contribution keeps an owner; the record owner is notified of changes; the approver is still separate |
| **Closed learning loop** | Nobody checks whether past estimates were right | Every prediction or estimate is compared with the actual outcome; results feed back into the model and into people's next estimates. Exception queues get the same loop: review the causes of recurring exceptions and fix them at the source | Never park this step. Compare snapshots taken before the outcome (no hindsight). Track bias by source (model, each human adjustment) |
| **Decision brief instead of a meeting to reconcile numbers** | A meeting spends its time agreeing the numbers | Numbers are reconciled before the meeting; an AI-drafted brief (B) lists the decisions, evidence and options; the meeting decides | The brief cites its sources; figures come from systems, not from the AI; the decision and its owner are recorded. Not for meetings on people, legal advice or inside information unless the AI tool is approved for that data |
| **Separate measures** | One number means several things | Keep distinct: what we expect (forecast), what we want (target), what we can do (constrained plan), what we commit to (approved plan or order) | Never adjust the forecast to hit a target; show the gap and let the owner decide what to do about it |
| **Scenarios, not a single number** | One point estimate is passed downstream | Base, upside and downside ranges, with what would trigger each, shaped for each consumer (e.g. Finance revenue band, Procurement requirement range, Supply capacity exposure) | Downstream commitments still go through their own approvals |

## Planning and forecasting (demand, sales, capacity, budget)
- **Statistical baseline (M).** Keep it, and measure it against a naive forecast. Don't rebuild it until its accuracy and bias are measured.
- **Event and promotion uplift (M with human challenge).** People submit the event's facts (dates, mechanics, scope) and their expected effect; a model estimates the effect from comparable past events, with a range. Large gaps between the two go to review with the evidence. This is often the direct fix when estimates are systematically low or high because of incentives.
- **Effects people forget:** pull-forward and post-event dips, cannibalization of related products, overlapping events, stock-outs hiding true demand. Check that an effect already in the baseline history isn't added again.
- **New products (M with human challenge).** Use analogous past launches and adoption curves; Product owns the assumptions and the target; show the gap between expected demand and the target.
- **Reconciliation (A + M).** Align levels and time buckets automatically; detect conflicts and double counts; produce exceptions and a decision brief (B).
- **Measure the value of every adjustment** (forecast value added): accuracy and bias before and after each stage (model, sales, product, consensus), reported by stage or team, not by named person. Stop adjustments that make the forecast worse.
- **Hidden commitments:** ask whether publishing the plan automatically triggers requisitions, purchase orders, production orders or budgets. If so, that release is a commitment (Principle 5) and needs its own approval.
- **Close-out:** after each promotion or event, record actuals against the plan, settle the related allowances or funding, and release leftover accruals (a human approves the release).
- **Vendor or embedded models:** back-test them like your own; ask the vendor for accuracy on your data, not their averages.
- **Rollout for monthly processes:** back-test on past cycles and events first, then shadow the current process for several cycles before switching; a 2–4 week pilot is too short.
- **Primary metrics:** forecast accuracy (e.g. weighted absolute percentage error), bias, forecast value added, uplift calibration; effort comes second.

## People processes (hiring, onboarding, scheduling, performance, HR queries)
- Intake and logistics can be A: structured forms, candidate or employee self-scheduling, status updates.
- A decision brief may be drafted (B) only from people's own written input (interviewers' feedback, the employee's request), reviewed by someone other than the decision-maker's preparer.
- No M or C on decisions about people, and no exceptions-only review of them. Each decision is made and recorded by a person.
- Tell people before AI is used in a process that affects them (notice rules vary; see risk checklist §2).
- Health, accommodation and leave information stays out of AI tools and in the restricted case system.

## Intake and requests (tickets, applications, orders, enquiries)
- Structured intake form (A) instead of free-text email; AI extracts from the unavoidable free text (B) with validation against master data.
- Triage by rules first (A), AI suggestion only where rules can't decide (B); people handle exceptions and anything in Principle 5.
- Status visible to the requester automatically (A), so "where is my request?" messages disappear.

## Approvals and reviews (invoices, expenses, documents, changes)
- Validate completeness and policy rules before a human sees the item (A); the human reviews only what the rules can't settle.
- Show the evidence next to the item; record the decision and reason; keep segregation of duties.
- Measure rework and approval time; don't speed approvals by removing the human for anything on Principle 5's list.

## Reporting and reviews (weekly or monthly business reviews, status reports)
- Numbers flow from systems into the report (A); anomaly detection (M or rules) highlights what changed.
- AI drafts the narrative (B) only from figures and causes the metric owners supplied; it never invents a cause.
- The meeting focuses on decisions and owners, not on reading the numbers.

## Customer and partner communication
- Fixed approved templates for routine messages (A); AI drafts for non-routine ones (B), always sent by a person.
- Commitments, prices and claims stay human (Principle 5).

## How to show the redesign in the report
- Section 1 opens with a "Today → AI-native" table of 5–7 rows (dimension | today | AI-native). A row may say "unchanged" where today's way is already right.
- Size pilots to the metric: slow metrics (monthly accuracy, quarterly bias) need several cycles, not 2–4 weeks.
- Mark M steps in diagrams and tables as **M Model**.
- One worked example with hypothetical numbers is allowed when it makes the design clearer. Put it in a `<p class="note">` box headed **"Illustration: hypothetical numbers"**, use round numbers, keep it out of sections 1 and 2, and never use it as an estimate or a saving.
