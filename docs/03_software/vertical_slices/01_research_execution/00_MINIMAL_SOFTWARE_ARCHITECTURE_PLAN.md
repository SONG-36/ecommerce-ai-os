# Ecommerce AI OS — First Research Slice — Minimal Software Architecture Plan V0.1

- Phase: Minimal Software Architecture
- Slice: US / Car Vacuum / TikTok Content Research
- Status: Active Planning
- Step 1–6: CANDIDATE COMPLETE
- Step 7: NEXT
- Architecture Authority: No
- Walking Implementation: NOT YET AUTHORIZED
- Upstream:
  - `01_MINIMAL_SOFTWARE_ARCHITECTURE_PHASE_HANDOFF.md`
  - `06_ARCHITECTURE_REVIEW.md`
  - D1–D5 Detailed Contracts
  - TT-17 Endpoint Admission / Selection Closure

---

# 0. Purpose

本文件只负责：

1. 记录 Minimal Software Architecture 的推进顺序；
2. 记录当前正在设计哪一步；
3. 记录每一步的输入、输出与完成状态；
4. 为新聊天 / Codex 提供软件阶段导航。

本文件不是：

- Global Software Architecture Authority；
- System Architecture；
- Contract；
- ADR；
- Implementation Specification。

---

# 1. Governing Principle

Minimal Software Architecture 不是从零设计。

设计输入：

```text
Product Architecture
↓
System Architecture V0.2
↓
First Slice Responsibility Coverage
↓
Minimal Runtime Path
↓
9 Required Contracts / Detailed Semantics
↓
Deferred / Not Yet Proven Guardrails
↓
TT-17 Endpoint Admission / Selection Closure
↓
Minimal Software Architecture
```

核心原则：

```text
Existing semantics first.
Software representation second.
```

先继承已有设计，
只设计尚未决定的软件表现形式。

必须继续保持：

```text
Responsibility ≠ Contract ≠ Software Component
Contract Boundary ≠ Service
Runtime Semantic Flow ≠ Software Call Graph
Current src scaffold ≠ Approved Software Architecture
```

---

# 2. Anchor Runtime / Contract Flow

```text
Business Work Request
→ C1
→ C2b Task Runtime
↔ C2a Research Skill
→ C3 Search
→ C4a Provider Resolution
→ C4b Scrape Creators Adapter
→ Scrape Creators
→ TT-17
→ Raw Provider Result
→ C4b
→ C3 Search Result
→ C2b
→ C2a
→ Sampling / Actual Sample Boundary
→ C5a Evidence
→ C2a Interpretation
→ Finding
→ Testable Hypothesis
→ C5b Research Result
→ C2a Business Completion
→ C2b Execution Terminalization
→ C6 Execution Record
→ C1 Terminal Return
```

该图是：

```text
Contract / Runtime Semantic Anchor
```

不是：

```text
Software Component Diagram
```

---

# 3. Work Plan

## Step 1 — Responsibility → Software Responsibility Mapping

Status: CANDIDATE COMPLETE

Goal:

把已确认的 System Responsibility / Contract Boundary
映射为最小 Software Responsibility。

重点判断：

- runtime component？
- interface / contract boundary？
- data representation？
- static binding？
- formalization logic？
- provider adapter？

不决定 package / class / framework。

Output:

`01_SOFTWARE_RESPONSIBILITY_MAPPING.md`

---

## Step 2 — Execution Spine Software Design

Status: CANDIDATE COMPLETE

Upstream:

`D1 = C1 + C2a + C2b`

Goal:

设计一次 Research Execution 的最小软件协作：

```text
Business Request
→ execution establishment
→ Skill binding
→ capability need
→ capability execution
→ result return
→ business completion
→ terminalization / failure
```

Output:

`02_EXECUTION_SPINE_SOFTWARE_DESIGN.md`

---

## Step 3 — Search / Provider Spine Software Design

Status: CANDIDATE COMPLETE

Upstream:

```text
D2 + D5
C3 + C4a + C4b
TT-17
```

Goal:

设计：

- provider-neutral Search invocation；
- static Search → Scrape Creators binding；
- Adapter boundary；
- Provider access；
- TT-17 mapping；
- pagination / duplicates / missingness / identity / limitation preservation。

### Step 3 Closure Summary

```text
C2b depends on the provider-neutral C3 Search seam.

C4a = static / single-provider binding responsibility;
it does not require an independent runtime Router.

C4b = current Scrape Creators translation responsibility
and may provide the concrete implementation behind the C3 seam.

C4b Adapter ≠ Concrete Access Mechanism.

TT-17 endpoint mapping is an internal C4b responsibility
for this Slice.

Search Result ≠ Raw Provider Result ≠ Evidence.

C3 → C4a → C4b
is a responsibility / dependency view,
not a mandatory three-service runtime call chain.
```

Output:

`03_SEARCH_PROVIDER_SPINE_SOFTWARE_DESIGN.md`

---

## Step 4 — Research / Evidence Software Design

Status: CANDIDATE COMPLETE

Upstream:

`D3 = C5a + C5b`

Goal:

设计：

```text
C3 Result
→ sampling
→ Actual Sample Boundary
→ Evidence formalization
→ Research interpretation
→ Finding
→ Hypothesis
→ Research Result
```

必须避免提前建设：

```text
EvidenceService
AnalyzeCapability
ResearchService
```

### Step 4 Closure Summary

```text
C2a owns sampling,
Evidence admission / evidence-worthiness,
Evidence interpretation,
Finding / Hypothesis formation,
and Research Result formation.

C5a = Evidence representation + bounded formalization.

C5b = Research Result representation + bounded validity/formalization.

Actual Sample Boundary = Stable Research Execution Fact.

Evidence / Finding / Hypothesis / Result
require software presence
but not independent runtime services.

Insufficient Evidence = valid Research Result outcome,
not Execution Failure.

Step 4 defines Evidence / Result reference relationships.
Step 5 owns post-terminal resolvability / retention representation.
```

Output:

`04_RESEARCH_EVIDENCE_SOFTWARE_DESIGN.md`

---

## Step 5 — Execution Record / Referenceability

Status: CANDIDATE COMPLETE

Upstream:

`D4 = C6`

Goal:

回答：

- stable execution facts 谁持有；
- C6 何时 finalize；
- success / failure record；
- post-terminal referenceability；
- minimal retention；
- 是否出现真实 minimal persistence need。

不得从这里直接推出：

```text
Dedicated Persistence Service
Specific Database Technology
```

Output:

`05_EXECUTION_RECORD_REFERENCEABILITY_SOFTWARE_DESIGN.md`

### Step 5 Closure Summary

```text
C2b Task Runtime
→ remains Execution lifecycle owner
→ stable execution facts / references progressively become known

C6
→ stable Execution Record representation
→ terminal finalization responsibility

Runtime State ≠ Stable Execution Facts ≠ Finalized Execution Record
Declared Dependency ≠ Actual Invocation Fact
Configured Provider Binding ≠ Actually Used Provider

C6 supports partial terminal facts.
Success / Failure may have different valid reference sets.
Research Result ≠ Execution Record

Application
→ receives Business Result + Execution Outcome / Record Reference
→ not full C6 payload by default

Post-terminal Resolvability = REQUIRED SEMANTIC OBLIGATION
Minimum Retention Capability = REQUIRED
Concrete Retention Representation = deferred to Step 6

RecorderService = NOT REQUIRED
Repository Layer = NOT REQUIRED
ReferenceResolverService = NOT REQUIRED
Database = NOT REQUIRED
Referenceability / Retention ≠ Persistence Architecture
Finalized C6 Record → logically immutable
```

Step 5 freezes retention / referenceability requirements. Step 6 chooses the minimum concrete representation that satisfies those requirements.

---

## Step 6 — Minimal Software Architecture Assembly + Representation Closure

Status: CANDIDATE COMPLETE

Inputs:

Step 1–5 Reviewed Results

Goal:

Step 6 must resolve, only where required by the First Slice:

- package boundaries；
- module boundaries；
- executable owner placement；
- stable callable / interface boundaries；
- dependency direction；
- dependency wiring / minimum DI shape；
- sync / async decision；
- application entry / transport representation；
- configuration ownership；
- Scrape Creators access implementation placement；
- minimum persistence representation inherited from Step 5；
- test seam / invariant placement needed by Walking Implementation。

```text
Step 6
≠ Final Ecommerce AI OS Software Architecture

Step 6
= minimum implementation-ready software shape
for the First Slice only
```

Step 6 is based on Step 5 retention requirements and does not reopen retention semantics. The selected First-Slice representation is the minimum implementation-ready shape recorded in the Step 6 assembly document.

The empty current `src` scaffold is not Architecture Authority and does not constrain the selected target shape.

### Step 6 Closure Summary

```text
Package Boundaries = CLOSED FOR FIRST SLICE
Module Boundaries = CLOSED FOR FIRST SLICE
Callable / Interface Representation = CLOSED
Dependency Direction = CLOSED
Dependency Injection = CLOSED → manual constructor injection
Sync / Async = CLOSED → SYNC
Application Transport = CLOSED → THIN CLI
Provider Access = CLOSED → SYNC STDLIB HTTP
Stable Model Strategy = CLOSED → DATACLASS
Retention Representation = CLOSED → LOCAL JSON EXECUTION BUNDLE

Database = NOT REQUIRED
Framework = NOT REQUIRED
Repository / Recorder / Resolver = NOT REQUIRED
Event Bus / Async Architecture = NOT REQUIRED
New Contract = NO
System Architecture Reopen = NO
Current empty src scaffold ≠ Architecture Authority
Walking Implementation = STILL NOT YET AUTHORIZED
```

Step 6 is complete as a Minimal Software Architecture Candidate. It does not perform the Step 7 Review Gate and does not authorize Walking Implementation.

Output:

`06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md`

---

## Step 7 — Minimal Software Architecture Review Gate

Status: NEXT

Goal:

验证：

- First Slice 是否可执行；
- 9 Required Contracts 是否都有软件承载；
- Provider details 是否泄漏；
- Evidence Contract 是否被错误升级成 Service；
- 是否引入未证明的 Agent / Analyze / Retry / Event / DB；
- C6 referenceability 是否闭环；
- 每个 component 是否有上游依据；
- Walking Implementation 是否可以授权。

### Implementation Readiness

Review Gate must confirm:

- all required software responsibilities have an explicit software owner/form；
- dependency direction is executable without violating Contract boundaries；
- no Contract was mechanically converted into a Service；
- no representation question remains unresolved if it blocks Walking Implementation；
- all remaining unresolved questions are explicitly mapped to `DEFERRED` / `NOT YET PROVEN` / `NOT REQUIRED`；
- the minimum runtime path can be traced end-to-end：

```text
Application
→ C1
→ C2b / C2a
→ C3
→ C4a / C4b
→ Scrape Creators / TT-17
→ C3 Result
→ C5a / C5b
→ C2a Business Completion
→ C2b Terminalization
→ C6
→ C1
```

Output: Not Yet Created

Possible Verdict:

```text
PASS
PASS_WITH_REFINEMENTS
FAIL
```

Only PASS / accepted refinements may authorize:

```text
Walking Implementation
```

Step 7 remains a Human Review Gate for the assembled Steps 1–6 candidate. It is not executed in this plan update, and its document is not created until Step 7 begins.

---

# 4. Documentation Progress Rule

Step documents are created incrementally under the
“讨论到哪，文件建到哪” principle.

Current created set:

```text
01_SOFTWARE_RESPONSIBILITY_MAPPING.md
02_EXECUTION_SPINE_SOFTWARE_DESIGN.md
03_SEARCH_PROVIDER_SPINE_SOFTWARE_DESIGN.md
04_RESEARCH_EVIDENCE_SOFTWARE_DESIGN.md
05_EXECUTION_RECORD_REFERENCEABILITY_SOFTWARE_DESIGN.md
06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md
```

The Step 7 document is not created until Step 7 begins.

---

# 5. Current Progress

Current Step:

Step 7 — Minimal Software Architecture Review Gate

Status:

NEXT

Completed candidate steps:

```text
Step 1 — CANDIDATE COMPLETE
Step 2 — CANDIDATE COMPLETE
Step 3 — CANDIDATE COMPLETE
Step 4 — CANDIDATE COMPLETE
Step 5 — CANDIDATE COMPLETE
Step 6 — CANDIDATE COMPLETE
```

Next Action:

Begin Step 7 only after the assembled Step 1–6 candidate remains aligned
with the existing Contract and scope guardrails.

---

# 6. Scope Guardrails

继续继承：

```text
Absence Does Not Imply Gap

Deferred Does Not Imply Backlog

Not Yet Proven Must Earn Promotion

Primary Status Controls Default Action

Responsibility ≠ Contract ≠ Software Component

Contract Boundary ≠ Service

Runtime Semantic Flow ≠ Software Call Graph

Current src scaffold ≠ Approved Software Architecture
```

本计划更新不改变：

```text
Product Architecture
System Architecture
D1–D5
TT-17 semantics
```

本计划同步不独立引入：

```text
new Contracts
new Services
implementation code
```

Step 6 的 package/module、callable、dependency、sync/async、transport、provider-access、model、retention representation decisions 以 `06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md` 为准；本计划只同步其状态与导航。

当前状态仍为：

```text
Architecture Authority = No
Walking Implementation = NOT YET AUTHORIZED
```

---

# 7. Seven-step Internal Work Plan

| Step | Work package | Status | Output |
|---|---|---|---|
| 1 | Responsibility → Software Responsibility Mapping | **CANDIDATE COMPLETE** | `01_SOFTWARE_RESPONSIBILITY_MAPPING.md` |
| 2 | Execution Spine Software Design | **CANDIDATE COMPLETE** | `02_EXECUTION_SPINE_SOFTWARE_DESIGN.md` |
| 3 | Search / Provider Spine Software Design | **CANDIDATE COMPLETE** | `03_SEARCH_PROVIDER_SPINE_SOFTWARE_DESIGN.md` |
| 4 | Research / Evidence Software Design | **CANDIDATE COMPLETE** | `04_RESEARCH_EVIDENCE_SOFTWARE_DESIGN.md` |
| 5 | Execution Record / Referenceability | **CANDIDATE COMPLETE** | `05_EXECUTION_RECORD_REFERENCEABILITY_SOFTWARE_DESIGN.md` |
| 6 | Minimal Software Architecture Assembly + Representation Closure | **CANDIDATE COMPLETE** | `06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md` |
| 7 | Minimal Software Architecture Review Gate | **NEXT** | Not Yet Created |

---

# 8. Current Status Summary

```text
Minimal Software Architecture
= ACTIVE DESIGN / REVIEW PHASE

Step 1
= CANDIDATE COMPLETE
Output
= 01_SOFTWARE_RESPONSIBILITY_MAPPING.md

Step 2
= CANDIDATE COMPLETE
Output
= 02_EXECUTION_SPINE_SOFTWARE_DESIGN.md

Step 3
= CANDIDATE COMPLETE
Output
= 03_SEARCH_PROVIDER_SPINE_SOFTWARE_DESIGN.md

Step 4
= CANDIDATE COMPLETE
Output
= 04_RESEARCH_EVIDENCE_SOFTWARE_DESIGN.md

Step 5
= CANDIDATE COMPLETE
Output
= 05_EXECUTION_RECORD_REFERENCEABILITY_SOFTWARE_DESIGN.md

Step 6
= CANDIDATE COMPLETE
Output
= 06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md

Step 7
= NEXT

Architecture Authority
= No

Walking Implementation
= NOT YET AUTHORIZED
```

---

# 9. Completion Boundary

本阶段完成条件：

```text
Step 1–6
→ Reviewed

Step 1–6
→ Minimal Software Architecture Candidate

Step 7
→ Review PASS
```

之后才允许：

```text
Walking Implementation
```
