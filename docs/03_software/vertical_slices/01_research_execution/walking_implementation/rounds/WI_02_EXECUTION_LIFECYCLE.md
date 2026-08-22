# WI-02 Round Record — Execution Lifecycle

## 1. Round Identity / Status

**Document Type**

Walking Implementation Round Record

**Project**

Ecommerce AI OS

**Repository**

```text
/Volumes/projects/andy/0813/ecommerce-ai-os
```

**Vertical Slice**

```text
US / Car Vacuum / TikTok Content Research First Slice
```

**Round**

```text
WI-02 — Execution Lifecycle
```

**Current Phase**

```text
Walking Implementation
```

**Document Maturity**

```text
HUMAN REVIEWED ROUND PLAN / P0 PASS / P1 PASS / P2 PASS / P3 PASS / P4 PASS
```

**Repository Materialization**

```text
PERFORMED
```

**Round Status**

```text
P4 COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS
```

**Current Internal Checkpoint**

```text
P4 — COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS
```

**Implementation**

```text
P4 COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS
```

**Python Changes**

```text
P4 ACTUAL / COMMITTED
```

**Test Changes**

```text
P4 ACTUAL / COMMITTED
```

**Architecture Expansion**

```text
NOT AUTHORIZED
```

**Architecture Reopen**

```text
NO
```

**Contract Reopen**

```text
NO
```

**New Contract Required**

```text
NO
```

**New Service Required**

```text
NO
```

**Audit Result**

```text
PASS
```

**Audit Corrections Incorporated**

```text
1. Canonical Human-reviewed design text and live repository materialization
   facts are represented separately.

2. 06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md was treated as the required
   pre-P1 live repository audit input and has now been directly reviewed.

3. P4 C6 finalization/publication failure injection is explicitly treated as a
   Candidate Test Strategy rather than an upstream frozen architecture fact.
```

---

# 2. Repository Entry Facts

本 Round Record 是经过 Human Review 的 canonical Round Plan，并已物化为
repository working tree 中的当前文件。

```text
Canonical Human-reviewed design text
!= live repository fact
```

Repository materialization 不表示该文件此前已经 tracked 或 committed。

Change Set A commit 后核对的 live repository facts：

```text
Branch
= main

Historical WI-02 Entry HEAD
= f32ad7ba7d26063ddb038cd726e1360d56098023

Current Pre-P1 HEAD
= 7ba1e5e49ce98fe6da35bd8e84bf72668da74fd7

Worktree before WI-02 commit
= only untracked
  docs/03_software/vertical_slices/01_research_execution/
  walking_implementation/rounds/WI_02_EXECUTION_LIFECYCLE.md

Historical WI-02 Entry HEAD
!= Current Pre-P1 HEAD
```

当前稳定项目状态来自 Current Handoff、Walking Implementation Plan、Architecture-Code Traceability 与已完成 WI-01 Round Record：

```text
WI-01
= COMPLETE / PASS

P0-P5
= COMPLETE

WI-02
= ROUND PLANNING / P0 COMPLETE
```

Current Handoff 中的 milestone navigation anchor 是 WI-02 的 historical
entry fact：

```text
f32ad7b
docs: close wi-1 baseline state sync
```

本次 live repository audit 已验证：

```text
Branch = main
Current Pre-P1 HEAD = 7ba1e5e49ce98fe6da35bd8e84bf72668da74fd7
Initial WI-02 materialization worktree scope = this Round Record only
```

当前文档不得伪造未从 live repository 获得的 Git 事实。

---

# 3. Inherited WI-01 Baseline

WI-02 不重新设计 WI-01。

WI-01 已经通过真实 Fake executable vertical slice 证明：

```text
CLI
→ BusinessWorkRequest
→ TaskRuntime.execute()
→ ExecutionContext
→ RuntimeResearchExecutionPort
→ Concrete ResearchSkill
→ ResearchExecutionPort.search(...)
→ TaskRuntime-controlled Search invocation
→ Fake SearchCapability
→ SearchResult
→ ResearchCompletion
→ TaskRuntime recognizes Business Completion
→ minimal C6
→ Local JSON Execution Bundle
→ Record Ref
→ TerminalReturn
→ CLI
```

WI-01 已建立以下实现基线：

```text
TaskRuntime
= Execution coordination owner

ResearchSkill
= Business Method owner

Capability access
= Runtime-controlled

Composition
= concrete wiring owner

Retention
= physical retention / publication mechanics

Owner-local serializers
= semantic serialization ownership
```

WI-01 已验证：

```text
Fake CLI E2E
= PASS

Record Ref resolves
= PASS

Architecture Import Guard
= PASS

Sequential Execution isolation
= PASS

TaskRuntime responsibility audit
= GREEN with bounded YELLOW pressure

Architecture Assumption Conflict
= NONE OBSERVED
```

WI-01 PASS 只证明：

```text
reviewed First-Slice minimal software shape
can execute
```

WI-01 PASS 不证明：

```text
full lifecycle semantics

real Provider

TT-17

full Search semantics

full Research Method

full C6 semantics

Agent

MCP

Memory

Async

Queue

Scheduler

Multi-task execution

Generic Task Framework

C++ Runtime

production readiness
```

因此：

```text
WI-02
must extend verification depth

WI-02
must not redesign the WI-01 executable spine
```

---

# 4. WI-02 Goal

WI-02 的核心目标是：

> 将 WI-01 中已经能够真实运行的 Execution Spine，进一步验证为符合已经 reviewed 的 Execution Lifecycle、Failure Closure 与 C6 Closure semantics 的执行模型。

WI-01 回答：

```text
Can the reviewed software shape execute?
```

WI-02 回答：

```text
Does the same software shape behave correctly
across the important lifecycle boundaries?
```

本轮主要验证：

```text
PreExecutionRejection

Execution Establishment

Active Execution

Business Completion

Execution Failure

ExecutionAbort

Execution Terminalization

C6 closure

closure failure
```

本轮不是：

```text
new architecture design round

new Search semantics round

new Research Method round

full C6 round

Provider integration round
```

---

# 5. Scope

## 5.1 In Scope

WI-02 只实现和验证 First Research Slice 当前已经 reviewed 的 lifecycle semantics：

```text
C1 admission / rejection

Execution Establishment Commit boundary

established Execution lifecycle

full First-Slice C1 response distinction
required for rejection and terminal execution outcomes

non-continuable Execution failure

private ExecutionAbort control / unwind mechanism

failure terminalization

minimum failure C6 closure

failure Record Ref / referenceability

Business Completion
→ Execution Terminalization
ordering

C6 finalization / publication failure

at-most-once logical terminal transition

success-path regression against WI-01
```

---

## 5.2 Explicit Non-Scope

WI-02 不实现：

```text
real Scrape Creators Provider

TT-17

ScrapeCreatorsAdapter

ScrapeCreatorsHttpClient

full SearchFailure semantics

full SearchRequest / SearchResult semantics

SearchInvocationProvenance

RawProviderResultRef

full missingness semantics

full pagination semantics

full bounded retrieval semantics

full Research Method

Finding formation

Hypothesis formation

advanced Sampling

full Evidence semantics

full C6 semantics

full version / reproducibility semantics

Agent

MCP Runtime

Memory

Async Architecture

Queue

Scheduler

Multi-task execution

parallel Capability invocation

Generic Task Framework

C++ Runtime

Retry Engine

Checkpoint

Crash Recovery

Durable Execution

Event / Message Architecture

Database

Repository Layer

RecorderService

ReferenceResolverService

UniversalReference model

new Contract

new Service
```

---

# 6. Architecture Inputs

## 6.1 Directly Reviewed During Current WI-02 Planning

当前 Human planning 已直接读取并使用：

```text
docs/00_project/02_CURRENT_HANDOFF.md

docs/00_project/00_PROJECT_BASELINE_V0.1.md

docs/02_system/00_SYSTEM_ARCHITECTURE.md

docs/03_software/00_SOFTWARE_ARCHITECTURE.md

docs/03_software/vertical_slices/01_research_execution/
02_EXECUTION_SPINE_SOFTWARE_DESIGN.md

docs/03_software/vertical_slices/01_research_execution/
05_EXECUTION_RECORD_REFERENCEABILITY_SOFTWARE_DESIGN.md

docs/03_software/vertical_slices/01_research_execution/
walking_implementation/00_WALKING_IMPLEMENTATION_PLAN.md

docs/03_software/vertical_slices/01_research_execution/
walking_implementation/01_ARCHITECTURE_CODE_TRACEABILITY.md

docs/03_software/vertical_slices/01_research_execution/
walking_implementation/rounds/WI_01_FAKE_VERTICAL_SLICE.md

docs/02_system/vertical_slices/01_research_execution/
contracts/01_EXECUTION_SPINE.md

docs/02_system/vertical_slices/01_research_execution/
contracts/04_EXECUTION_RECORD.md
```

这些输入已经足以确定 WI-02 当前的：

```text
Goal

Scope

Lifecycle semantic distinctions

Required verification scenarios

Checkpoint sequencing

Deferred boundaries
```

---

## 6.2 Required Pre-P1 Live Repository Audit Input

Walking Implementation Plan 对 WI-02 的 Architecture Reading Map 还要求：

```text
docs/03_software/vertical_slices/01_research_execution/
06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md
```

该文档已在本次 pre-P1 live repository audit 中从真实 repository 直接读取。

审核结果：

```text
06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md
= DIRECTLY REVIEWED IN PRE-P1 LIVE REPOSITORY AUDIT

Representation Check
= PASS

Blocking Contradiction
= NONE

Architecture Assumption Conflict
= NONE
```

本次 audit 已核对以下 reviewed representation：

```text
PreExecutionRejection representation

TaskExecutionResponse representation

Execution Establishment representation

ExecutionAbort representation

failure TerminalReturn representation

C6 finalization / publication representation

closure failure representation
```

如果 `06` 与当前 Round Plan 之间出现真正的 blocking contradiction：

```text
do not silently rewrite the Round Plan

→ record contradiction
→ classify
→ explicit Human Review
```

---

# 7. Lifecycle Semantic Model

WI-02 当前使用以下 semantic lifecycle：

```text
BusinessWorkRequest
        │
        ▼
PRE-EXECUTION
        │
        ├── cannot form legal Execution
        │       ↓
        │   PreExecutionRejection
        │
        │   Execution = NOT ESTABLISHED
        │   execution_id = ABSENT
        │   C6 = ABSENT
        │   Record Ref = ABSENT
        │
        └── request can establish Execution
                ↓
          ESTABLISHMENT
                ↓
       EXECUTION ESTABLISHMENT COMMIT
                ↓
              ACTIVE
          ┌──────┴───────────────┐
          │                      │
          │                      │
 Business Method            non-continuable
 progresses legally             failure
          │                      │
          │                      ↓
          │              Execution Failure
          │                      ↓
          │               ExecutionAbort
          │              [private unwind]
          │                      ↓
          │              C2b failure handling
          │                      ↓
          │              failure terminalization
          │                      ↓
          │                   C6 closure
          │                      ↓
          │            failed TerminalReturn
          │
          ▼
 ResearchCompletion
          ↓
 Business Completion
          ↓
 Execution Terminalization
          ↓
       C6 closure
        /      \
   succeeds   fails
      ↓         ↓
 Record Ref   no clean closure
      ↓       no valid Record Ref
 TerminalReturn
```

这些是：

```text
lifecycle semantics
```

它们不是：

```text
approved TaskState enum

database state machine

workflow DAG

event graph

new Contract graph
```

---

# 8. Core Lifecycle Invariants

WI-02 必须保持以下不变量。

## 8.1 Business Work 与 Execution

```text
BusinessWorkRequest
!= Execution
```

BusinessWorkRequest 只是进入 C1 的业务请求。

Execution 只有在 C2b 完成 minimum legal execution establishment 并跨过 establishment commit 后才语义上存在。

---

## 8.2 PreExecutionRejection 与 Execution Failure

```text
PreExecutionRejection
!= Execution Failure
```

PreExecutionRejection 发生于：

```text
Execution Establishment Commit
BEFORE
```

Execution Failure 只能发生于：

```text
Execution Establishment Commit
AFTER
```

---

## 8.3 Establishment Commit

```text
Execution Establishment Commit
= semantic lifecycle boundary
```

它不是：

```text
SQL commit

database transaction

distributed transaction

event commit

CommitService
```

临时 UUID 或临时 Python object 的创建本身不代表 Execution 已经语义建立。

---

## 8.4 Runtime 与 Business Method Authority

```text
C2b TaskRuntime
= Execution lifecycle owner
```

```text
C2a ResearchSkill
= Business Method owner
```

TaskRuntime 不解释 Research 业务含义。

ResearchSkill 不拥有 Execution lifecycle。

---

## 8.5 Execution Failure 与 ExecutionAbort

```text
Execution Failure
!= ExecutionAbort
```

其中：

```text
Execution Failure
= semantic fact that an established Execution
  cannot legally continue
```

而：

```text
ExecutionAbort
= C2b-private control / unwind mechanism
```

ExecutionAbort 不是：

```text
Business Result

public Contract

Application-facing error model

new lifecycle Contract

Capability Contract

Provider error Contract
```

---

## 8.6 Business Completion 与 Execution Completion

```text
Business Completion
precedes
Execution Completion
```

```text
Business Result
!= Execution Outcome
```

不得：

```text
mark Execution SUCCESS
→ later construct Research Result
```

正确顺序是：

```text
valid Research Result
→ ResearchCompletion
→ Business Completion
→ Execution Terminalization
→ C6 closure
```

---

## 8.7 Runtime State / Stable Facts / C6

```text
Runtime State
!= Stable Execution Facts
!= Finalized Execution Record
```

Execution Record 不是 Runtime State、Trace、Logs 或 complete runtime history。

---

## 8.8 Failure Closure 与 Closure Failure

```text
failed Execution
can still have
clean failure closure
```

而：

```text
clean failure closure
!= closure failure
```

例如：

```text
Execution fails
→ failure C6 succeeds
→ failure Record Ref resolves

= clean failure closure
```

而：

```text
Business Completion succeeds
→ C6 finalization/publication fails

= closure failure
```

---

## 8.9 C6 Closure Failure

```text
C6 finalization failure
!= Research Business Failure
```

Business Completion 已经发生时，后续 closure failure 不得倒退成：

```text
Research never completed
```

---

## 8.10 Record Ref

```text
Record Ref
exists only after successful
finalization / publication semantics
```

因此：

```text
no successful publication
→ no fabricated valid Record Ref
```

---

## 8.11 Terminalization

```text
Terminalization
= at-most-once logical lifecycle transition
```

同一 established Execution 不得制造：

```text
second logical terminal outcome

second logical Execution completion

second independent C6 finalization
```

当前不因此引入 distributed idempotency protocol、lock 或 transaction architecture。

---

# 9. Required Verification Scenario A — Normal Success

目标路径：

```text
Valid BusinessWorkRequest
→ C1 admission
→ Execution Establishment
→ Execution Establishment Commit
→ ACTIVE
→ Research Skill progresses
→ ResearchCompletion
→ Business Completion
→ C2b recognizes completion
→ Execution Terminalization
→ C6 finalization
→ required-reference validation
→ publication
→ resolvable Record Ref
→ successful TerminalReturn
```

WI-01 已经建立该路径的 executable evidence。

WI-02 不重新实现一套 success path。

WI-02 重新验证：

```text
establishment ordering

Business Completion ordering

terminalization ordering

C6 closure ordering

Record Ref validity

no regression against WI-01
```

必须保持：

```text
Task marked success
→ later construct Research Result
```

为非法顺序。

正确顺序：

```text
valid Research Result
→ Business Completion
→ Execution Terminalization
→ C6 closure
→ TerminalReturn
```

---

# 10. Required Verification Scenario B — PreExecutionRejection

目标路径：

```text
Invalid / non-formable BusinessWorkRequest
→ C1 admission attempt
→ PreExecutionRejection
```

必须观察：

```text
Execution
= NOT ESTABLISHED

execution_id
= ABSENT

ExecutionContext
= ABSENT

C6 Record
= ABSENT

Record Ref
= ABSENT
```

必须保持：

```text
PreExecutionRejection
!= Execution Failure
```

PreExecutionRejection 只发生在：

```text
Execution Establishment Commit
BEFORE
```

一旦已经越过 establishment commit：

```text
failure belongs to the established Execution lifecycle
```

不得再表示为 PreExecutionRejection。

---

# 11. Required Verification Scenario C — Established Non-continuable Execution Failure

目标路径：

```text
Valid BusinessWorkRequest
→ Execution Established
→ ACTIVE
→ controlled Capability / Runtime failure
→ current Execution cannot legally continue
→ Execution Failure
→ private ExecutionAbort
→ control unwinds to C2b
→ C2b failure handling
→ failure terminalization
→ minimum failure C6 finalization
→ publication succeeds
→ resolvable failure Record Ref
→ failed TerminalReturn
```

核心区分：

```text
Execution Failure
= semantic fact

ExecutionAbort
= software control mechanism
```

ExecutionAbort 必须保持：

```text
private to Runtime implementation
```

不得让：

```text
Application

ResearchSkill

Search Capability

Provider
```

把 `ExecutionAbort` 当成稳定公共 Contract。

---

# 12. Failure C6 Semantics Required by WI-02

WI-02 只实现 failure closure 所需的 minimum C6 depth。

失败 Execution 不要求伪造完整成功路径。

合法 failure record 可以包含：

```text
Execution identity

Task / input references

actual Skill reference
where established

actually invoked Capability reference
if invocation occurred

resolved Provider reference
only if resolution actually occurred

actually used Provider reference
only if Provider invocation actually occurred

stable failure-stage facts

terminal failure outcome
```

合法 failure record 可以缺少：

```text
Evidence Ref

Finding

Hypothesis

Research Result Ref

Business Output Ref
```

原则：

```text
Record what actually occurred.
```

不得：

```text
Declared dependency
→ infer actual invocation

Configured Provider binding
→ infer resolved Provider

Resolved Provider
→ infer actually used Provider

bound Skill
→ infer Research Result exists
```

Failure C6 也不得退化成：

```text
stack trace dump

raw Provider error dump

full log history

observability backend
```

---

# 13. Required Verification Scenario D — Business Completion Followed by Closure Failure

目标路径：

```text
Execution Established
→ ACTIVE
→ ResearchCompletion exists
→ Business Completion accepted
→ Business Result exists
→ Execution enters terminalization
→ C6 finalization / publication fails
```

此时必须保持：

```text
Business Completion
= DID OCCUR
```

但：

```text
Clean Execution Closure
= FAILED
```

以及：

```text
Valid Record Ref
= ABSENT
```

这条路径的核心不变量：

```text
C6 finalization failure
!= Research Business Failure
```

不能把已经形成的：

```text
ResearchCompletion

Business Result
```

倒退为：

```text
Research never completed
```

也不能伪造：

```text
successful TerminalReturn
+
fake Record Ref
```

WI-02 当前只要求识别并正确传播 closure failure semantics。

Scenario D 的 C1 response representation 遵循已 reviewed 的 `06`：

Scenario D may therefore return a partial `TerminalReturn` representation
consistent with the reviewed `06` representation.

```text
TaskExecutionResponse
= PreExecutionRejection | TerminalReturn

Already-established Execution closure failure
→ does not create a third public response family

Partial TerminalReturn
→ Business Result = may exist
→ Execution closure = failed
→ Record Ref = absent when finalization / publication
  did not establish a valid record
```

它不因此引入：

```text
Retry Engine

secondary recorder

transactional outbox

Checkpoint

Crash Recovery

Durable Execution subsystem
```

---

# 14. Failed Execution vs Closure Failure

## 14.1 Failed Execution with Clean Failure Closure

```text
Execution Established
→ business/runtime execution cannot continue
→ terminal failure
→ failure C6 succeeds
→ valid failure Record Ref
```

结果：

```text
Business Result
= may be absent

Execution Outcome
= failure

Execution closure
= clean

failure C6
= valid

Record Ref
= valid
```

---

## 14.2 Closure Failure after Business Completion

```text
Execution Established
→ Business Completion succeeds
→ Business Result exists
→ C6 finalization/publication fails
```

结果：

```text
Business Completion
= yes

Business Result
= may exist

clean Execution closure
= no

valid Record Ref
= no
```

因此：

```text
Execution Failure
!= Closure Failure
```

WI-02 不要求现在冻结最终：

```text
CLOSURE_FAILED
```

Runtime enum。

语义必须可区分，但最终 lifecycle/state taxonomy 继续保持开放，除非 live `06` 已 reviewed representation 明确要求具体 software form。

---

# 15. Internal Checkpoint Plan

P0-P5 是 WI-02 内部 Implementation / Learning Checkpoints。

它们不是：

```text
new Walking Rounds

new Contracts

new Architecture Steps
```

推进规则：

```text
P0
→ Human Review

→ P1
→ Code / Test / Review
→ Human Review

→ P2
→ Code / Test / Review
→ Human Review

→ P3
→ Code / Test / Runtime Evidence
→ Human Review

→ P4
→ Closure Failure Verification
→ Human Review

→ P5
→ Full Verification / Learning Review

→ WI-02 Round Review
```

必须保持：

```text
Later checkpoint
must not be implemented
before current checkpoint
has completed Human Review.
```

---

# 16. P0 — Pre-Code Lifecycle Review

## 16.1 Status

```text
COMPLETE / HUMAN REVIEWED / PASS
```

## 16.2 Goal

在写任何生命周期代码前建立统一 mental model。

P0 只回答：

```text
where Execution begins

where rejection ends

where established failure begins

what ExecutionAbort means

where Business Completion occurs

where terminalization occurs

what C6 closure means

what closure failure means
```

## 16.3 Implementation Boundary

```text
DO NOT WRITE PYTHON

DO NOT MODIFY TESTS

DO NOT IMPLEMENT ExecutionAbort
```

## 16.4 Learning Questions

Human 至少需要能够解释：

1. 为什么 `BusinessWorkRequest` 不等于 established Execution？
2. Execution Establishment Commit 的语义边界是什么？
3. 为什么 commit 前失败是 `PreExecutionRejection`？
4. 为什么 commit 后失败不能重新表示成 rejection？
5. `Execution Failure` 与 `ExecutionAbort` 分别是什么？
6. 为什么 `ExecutionAbort` 必须保持 C2b-private？
7. 为什么 Business Completion 必须先于 Execution Completion？
8. failed Execution 如何仍然形成合法 failure C6？
9. 为什么 failure C6 可以没有 Research Result？
10. 为什么 C6 closure failure 不是 Research Business Failure？
11. 为什么 C6 publish 失败后不能返回 fake Record Ref？
12. 为什么 WI-02 不需要 Retry Engine？

## 16.5 P0 PASS Gate

P0 只有 Human Review 明确通过后，才能进入 P1。

此外：

```text
P0 Human Review PASS
does not by itself authorize P1 code
until the required pre-P1 live repository audit
including 06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md
has completed without blocking contradiction.
```

---

# 17. P1 — Admission + Execution Establishment Boundary

## 17.1 Goal

第一次实现并验证：

```text
before Execution establishment
!=
after Execution establishment
```

## 17.2 Target Path A — Rejection

```text
invalid BusinessWorkRequest
→ PreExecutionRejection

Execution
= absent

execution_id
= absent

C6
= absent

Record Ref
= absent
```

## 17.3 Target Path B — Establishment

```text
valid BusinessWorkRequest
→ establishment preparation
→ Execution Establishment Commit
→ ExecutionContext exists
→ execution_id exists
→ existing WI-01 success path remains valid
```

## 17.4 Main Traceability Coverage

```text
A02 — BusinessWorkRequest

A03 — C1 response family
       rejection side / lifecycle distinction

A05 — ExecutionContext + Execution Establishment
```

## 17.5 Explicit P1 Non-Scope

```text
ExecutionAbort

failure C6

closure failure

full SearchFailure

full C6
```

P1 完成后必须暂停进行 Human Review。

## 17.6 P1 Actual Evidence

### Status

```text
P1
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P1 Human PASS
= PASS

P1 Runtime Evidence
= ESTABLISHED

P2
= NEXT / NOT AUTHORIZED
```

### Actual Files and Symbols

```text
src/ecommerce_ai_os/runtime/execution.py
→ PreExecutionRejection
→ TaskExecutionResponse = PreExecutionRejection | TerminalReturn

src/ecommerce_ai_os/runtime/task_runtime.py
→ TaskRuntime.execute
→ TaskRuntime._pre_execution_rejection

src/ecommerce_ai_os/application/cli.py
→ main rejection presentation

tests/unit/runtime/test_execution.py
→ BusinessWorkRequestTests.test_c1_response_family_distinguishes_rejection_from_terminal_return

tests/integration/test_fake_first_slice.py
→ FakeFirstSliceIntegrationTests.test_successful_fake_execution_publishes_resolvable_bundle
→ FakeFirstSliceIntegrationTests.test_incomplete_request_is_rejected_before_execution_establishment
```

### Actual Rejection Path

```text
BusinessWorkRequest with incomplete required First-Slice context
→ TaskRuntime._pre_execution_rejection
→ PreExecutionRejection

Execution identity = absent
ExecutionContext = absent
ResearchSkill execution = absent
Search capability invocation = absent
C6 = absent
Execution bundle = absent
Record Ref = absent
```

The admission check uses only the already-required First-Slice request context fields. It does not add a new business policy.

### Actual Establishment Path

```text
valid BusinessWorkRequest
→ admission passes
→ execution_id allocated
→ ExecutionContext constructed
→ Execution is established
→ existing WI-01 success path
→ TerminalReturn
```

For P1, successful `ExecutionContext` construction is the exact Execution Establishment Commit. A valid runtime run established one `execution_id` and propagated it through the existing published WI-01 bundle and terminal return.

### Test and Runtime Evidence

```text
PYTHONPATH=src python -m unittest tests.unit.runtime.test_execution -v
→ 3 tests / PASS

PYTHONPATH=src python -m unittest tests.integration.test_fake_first_slice -v
→ 3 tests / PASS

PYTHONPATH=src python -m unittest discover -s tests/unit -v
→ 19 tests / PASS

PYTHONPATH=src python -m unittest discover -s tests/integration -v
→ 3 tests / PASS

PYTHONPATH=src python -m unittest tests.unit.architecture.test_import_directions -v
→ 1 test / PASS

python -m compileall -q src tests
→ PASS

git diff --check
→ PASS
```

Valid-path runtime evidence:

```text
CLI exit = 0
Execution outcome = SUCCEEDED
execution_id = b609cb2c-5c7e-45e3-9b74-d417fc725214
Record Ref = execution://b609cb2c-5c7e-45e3-9b74-d417fc725214/execution_record.json
required references = 5
resolved references = 5
staging bundle after publication = absent
```

Rejection-path runtime evidence:

```text
CLI output = Request Rejected: required First-Slice request context is incomplete
CLI exit = 1
Execution root = absent
```

### Traceability and Review Result

```text
A02 — BusinessWorkRequest admission evidence established
A03 — C1 rejection / terminal response distinction established
A05 — rejection-before-establishment and exact establishment commit established

Architecture Deviation = NONE
Architecture Assumption Conflict = NONE
```

### Final Focused Audit — Actual Skill Binding

```text
self._research_skill
= actual statically bound ResearchSkill

composition
→ creates one concrete ResearchSkill
→ constructor-injects it before TaskRuntime.execute()

TaskRuntime.execute()
→ uses the same stored Skill instance

reviewed synchronous First-Slice execution
→ no dynamic Skill change or selection

TaskRuntime._run_research_skill declaration equality check
= post-establishment defensive consistency invariant
!= Skill binding operation

BusinessWorkRequest.skill_id
= NOT REQUIRED

dynamic Skill selection
= NOT REQUIRED

Classification
= NO ISSUE
```

---

# 18. P2 — Established Execution Failure + ExecutionAbort

## 18.1 Goal

证明：

```text
failure after establishment
cannot become
PreExecutionRejection
```

## 18.2 Target Path

```text
Execution Established
→ ACTIVE
→ controlled non-continuable failure
→ Execution Failure
→ ExecutionAbort
→ unwind to TaskRuntime lifecycle owner
```

## 18.3 Required Proof

```text
ExecutionAbort
= private Runtime control signal

ExecutionAbort
!= C1 response

ExecutionAbort
!= Business Result

ExecutionAbort
!= new Contract

Execution identity remains available

facts established before failure
are not silently lost
```

## 18.4 Main Traceability Coverage

```text
A04 — TaskRuntime

A05 — Execution Establishment

A09 — ExecutionAbort
```

P2 不完成 failure C6 publication。

P2 完成后必须暂停进行 Human Review。

## 18.5 P2 Actual Evidence

### Status

```text
P2
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P2 Human PASS
= PASS

P2 Final Verdict
= PASS

P3
= NEXT / NOT AUTHORIZED
```

### Existing Failure Surface Before P2

```text
ResearchSkill.run
→ could propagate exceptions from business method or execution port

RuntimeResearchExecutionPort.search
→ propagated TaskRuntime._invoke_search and observer exceptions

TaskRuntime._invoke_search
→ rejected undeclared Search with RuntimeError
→ otherwise cast the SearchCapability outcome to SearchResult

SearchCapability.search
→ WI-01 Fake returned SearchResult only
→ no implemented SearchFailure representation
```

### Actual Files and Symbols

```text
src/ecommerce_ai_os/runtime/task_runtime.py
→ private _ExecutionAbort
→ TaskRuntime.execute private-abort catch boundary
→ TaskRuntime._invoke_search controlled non-result recognition
→ TaskRuntime._abort_execution

tests/unit/runtime/test_task_runtime.py
→ ControlledFailureSearchCapability
→ TaskRuntimeCoordinationTests.test_non_result_search_outcome_triggers_private_execution_abort

tests/integration/test_fake_first_slice.py
→ ControlledFailureSearchCapability
→ FakeFirstSliceIntegrationTests.test_established_failure_unwinds_privately_to_task_runtime_owner
```

### Actual Control Path

```text
valid BusinessWorkRequest
→ admission succeeds
→ statically bound ResearchSkill available
→ execution_id allocated
→ ExecutionContext constructed
→ Execution Establishment Commit
→ active ResearchSkill.run
→ RuntimeResearchExecutionPort.search
→ controlled test-only non-result Search outcome
→ established Execution cannot legally continue
→ TaskRuntime._abort_execution
→ private _ExecutionAbort
→ current Skill call unwinds
→ TaskRuntime.execute catches _ExecutionAbort
→ P2 stops at TaskRuntime lifecycle-owner boundary
```

P2 intentionally does not create a failed `TerminalReturn`, failure C6, failure Record Ref, or CLI failure response. The private signal is not a member of `TaskExecutionResponse` and does not escape as the public exception type.

### Test Strategy and Evidence

The deterministic failure is supplied by a constructor-injected test double at the existing provider-neutral `SearchCapability` seam. It returns a test-only non-result marker after receiving the execution-scoped `SearchInvocationContext`. No production failure flag, Provider behavior, TT-17 semantics, or full `SearchFailure` representation is introduced.

The focused integration evidence established:

```text
Execution established = YES
execution_id exists = YES
ExecutionContext exists = YES
active Research execution entered = YES
Search invocation entered = YES
controlled non-continuable failure occurred = YES
PreExecutionRejection used = NO
private _ExecutionAbort occurred = YES
control returned to TaskRuntime owner = YES

staging bundle exists = YES
input fact retained before failure = YES
failure C6 exists = NO
final bundle exists = NO
TerminalReturn returned = NO
```

### Tests Executed

```text
PYTHONPATH=src python -m unittest tests.unit.runtime.test_task_runtime -v
→ 5 tests / PASS

PYTHONPATH=src python -m unittest tests.integration.test_fake_first_slice.FakeFirstSliceIntegrationTests.test_established_failure_unwinds_privately_to_task_runtime_owner -v
→ 1 test / PASS

PYTHONPATH=src python -m unittest discover -s tests/unit -v
→ 20 tests / PASS

PYTHONPATH=src python -m unittest discover -s tests/integration -v
→ 4 tests / PASS

PYTHONPATH=src python -m unittest tests.unit.architecture.test_import_directions -v
→ 1 test / PASS

python -m compileall -q src tests
→ PASS

git diff --check
→ PASS
```

### Architecture Mapping and Review Result

```text
A04 — TaskRuntime recognizes and catches established failure control
A05 — execution identity/context and pre-failure input fact remain available
A09 — private _ExecutionAbort unwind mechanism established

Architecture Deviation = NONE
Architecture Assumption Conflict = NONE

P2-YELLOW-1
= P3 must verify that the bounded stable failure facts required for failure C6
  remain available after private ExecutionAbort unwind.

Blocking
= NO
```

---

# 19. P3 — Failure Terminalization + Minimum Failure C6

## 19.1 Goal

将 P2 的：

```text
Execution failed
```

闭合成：

```text
valid failed Execution
with clean failure closure
```

## 19.2 Target Path

```text
ExecutionAbort caught by Runtime
→ failure terminal outcome
→ minimum path-actual Stable Execution Facts
→ failure C6 finalization
→ publication
→ resolvable failure Record Ref
→ failed TerminalReturn
```

## 19.3 Required Proof

```text
failed Execution
does not require Business Result

failure C6
contains path-actual facts only

failure Record Ref
exists only after successful publication

failure Record Ref
resolves

failure C6
is not a log / trace dump
```

## 19.4 Main Traceability Coverage

```text
A03 — full C1 terminal response behavior

A09 — ExecutionAbort

D01 — failure Execution Record

D02 — failure Record Ref / referenceability
```

P3 不升级为 full WI-07 C6 implementation。

## 19.5 P3 Actual Evidence

### Status

```text
P3
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P3 Human PASS
= PASS

P3 Final Verdict
= PASS

P4
= NEXT / NOT AUTHORIZED
```

### Existing P2 Failure Path Before P3

```text
established Execution
→ controlled non-result Search outcome
→ private _ExecutionAbort(execution_id)
→ TaskRuntime owner catches the unwind
→ temporary RuntimeError
→ no failure C6
→ no Record Ref
→ no TerminalReturn
```

### Actual Files and Symbols

```text
src/ecommerce_ai_os/runtime/execution.py
→ TerminalReturn.business_result permits absence on failed Execution closure

src/ecommerce_ai_os/runtime/task_runtime.py
→ _ExecutionAbort bounded stable failure fields
→ TaskRuntime.execute failure catch / finalization / publication / return
→ TaskRuntime._abort_execution

src/ecommerce_ai_os/runtime/execution_record.py
→ StableExecutionFacts.record_execution_failure
→ StableExecutionFacts.finalize_failure
→ FinalizedExecutionRecord path-sensitive optional facts
→ serialize_finalized_execution_record path-sensitive output

tests/unit/runtime/test_execution.py
→ BusinessWorkRequestTests.test_terminal_return_allows_failure_without_a_business_result

tests/unit/runtime/test_task_runtime.py
→ TaskRuntimeCoordinationTests.test_non_result_search_outcome_triggers_private_execution_abort

tests/integration/test_fake_first_slice.py
→ FakeFirstSliceIntegrationTests.test_established_failure_closes_with_path_sensitive_record
```

`LocalJsonRetention` and `StagingExecutionBundle.publish` were reused without modification. No second writer, store, service, or response family was introduced.

### Exact Actual Failure Closure Path

```text
valid BusinessWorkRequest
→ admission succeeds
→ execution_id allocated
→ ExecutionContext constructed
→ Execution Establishment Commit
→ staging bundle created
→ work request retained
→ bound ResearchSkill enters Search
→ controlled test-only non-result Search outcome
→ TaskRuntime identifies non-continuable established failure
→ _ExecutionAbort carries bounded stable failure facts
→ Skill call unwinds
→ TaskRuntime catches _ExecutionAbort
→ StableExecutionFacts records actual Search participation + failure facts
→ minimum path-sensitive FAILED C6 finalized
→ required input reference validated
→ failure bundle atomically published
→ Record Ref exposed and resolves
→ TerminalReturn(execution_outcome="FAILED", business_result=None, record_ref=...)
```

The private `_ExecutionAbort` remains an internal control mechanism. It is neither `TaskExecutionResponse` nor a public failure Contract and does not escape `TaskRuntime.execute`.

### P2-YELLOW-1 Closure and Bounded Failure Facts

```text
P2-YELLOW-1
= VERIFIED / CLOSED

Facts carried across private _ExecutionAbort unwind
= execution_id
= actual_capability = Search
= failure_code = SEARCH_OUTCOME_NOT_RESULT
= failure_reason = Search invocation did not produce a contract-valid SearchResult

Retained raw exception object = NO
Retained stack trace = NO
Retained logs = NO
Retained raw Provider error = NO
Retained observability payload = NO
```

After the unwind, `TaskRuntime` transferred these bounded facts into `StableExecutionFacts` before C6 finalization. The focused unit and integration tests verify that the same code and reason survive into the finalized failure record.

### Failure C6 Contents and Path Sensitivity

The actual failure C6 contains only facts established on the controlled path:

```text
record identity = present
execution identity = present
work request reference = present / required / resolvable
actual Skill id/version = present
actual Capability participation = Search
bounded failure code/reason = present
terminal outcome = FAILED

SearchResult reference = absent
ActualSampleBoundary reference = absent
Evidence references = absent
ResearchResult reference = absent
Business Result = absent
Provider fact = absent
provider_raw = absent
```

The failure record's `required_references` contains only the retained work-request reference. It does not use empty or null success-only fields to imply facts that never formed.

### Tests Executed

```text
PYTHONPATH=src python -m unittest \
  tests.unit.runtime.test_task_runtime \
  tests.unit.runtime.test_execution \
  tests.integration.test_fake_first_slice.FakeFirstSliceIntegrationTests.test_established_failure_closes_with_path_sensitive_record -v
→ 10 tests / PASS

PYTHONPATH=src python -m unittest discover -s tests/unit -v
→ 21 tests / PASS

PYTHONPATH=src python -m unittest discover -s tests/integration -v
→ 4 tests / PASS

PYTHONPATH=src python -m unittest \
  tests.unit.architecture.test_import_directions -v
→ 1 test / PASS

python -m compileall -q src tests
→ PASS

git diff --check
→ PASS
```

### Actual Runtime Evidence

```text
Runtime evidence root
= /tmp/ecommerce-ai-os-WI2-P3-runtime.aSqVYc/executions

execution_id
= b81bcde3-d32b-4245-9e93-236b1581336d

TerminalReturn type
= TerminalReturn

Execution outcome
= FAILED

Business Result
= None

Record Ref
= execution://b81bcde3-d32b-4245-9e93-236b1581336d/execution_record.json

Record Ref resolves
= YES

required references resolve
= YES

staging bundle after publication
= absent

success-only C6 keys
= absent

Provider facts
= absent
```

The `/tmp` path is inspectable review evidence only and is not a repository artifact or a durability guarantee.

### Architecture Mapping and Review Result

```text
A03 — established failure returns the existing TerminalReturn family
A09 — private ExecutionAbort carries bounded facts and does not escape Runtime
D01 — minimum path-sensitive failure Execution Record finalized and published
D02 — failure Record Ref exists only after publication and resolves

Architecture Deviation = NONE
Architecture Assumption Conflict = NONE

P4 closure failure = NOT IMPLEMENTED AT P3 CHECKPOINT
P4 = NEXT / NOT AUTHORIZED AT P3 CHECKPOINT
```

---

# 20. P4 — Business Completion + Closure Failure

## 20.1 Goal

验证：

```text
Business Completion
can succeed

while

clean Execution closure
can fail
```

## 20.2 Candidate Failure-Injection Strategy

当前推荐的最小 test strategy 是：

```text
inject a controlled failure
at the existing
C6 finalization / publication seam
```

原因：

```text
it isolates closure failure semantics

it does not require real Provider behavior

it does not require TT-17

it does not require full SearchFailure semantics

it does not require full Research Method
```

但必须保持：

```text
P4 failure injection at C6 finalization/publication
= Candidate Test Strategy

P4 failure injection at C6 finalization/publication
!= upstream frozen Architecture fact
```

该 strategy 只有在 pre-P1 / pre-P4 live repository audit 证明现有 `06` 与 retention representation 没有 contradiction 时才能采用。

如果现有 reviewed representation 已提供更直接且不扩大 architecture 的 deterministic failure seam，应优先遵循 reviewed representation。

## 20.3 Target Path

```text
ResearchCompletion
→ Business Completion
→ Business Result exists
→ C6 finalization / publication fails
→ no successful final publication
→ no valid Record Ref
→ clean Execution closure fails
```

## 20.4 Required Proof

```text
Business Result is not silently erased

closure failure
!= Research Business Failure

no fake Record Ref

no automatic hidden retry

no second recorder

no Retry Engine

no transactional outbox
```

## 20.5 Deferred Recovery Questions

WI-02 不提前决定：

```text
whether failed staging is deleted

whether failed staging is retained

whether failed staging is quarantined

cleanup duration

restart recovery policy
```

这些属于未来 retention / recovery policy 问题。

本轮只要求：

```text
not successfully published
→ no valid Record Ref
→ no fake clean closure
```

## 20.6 P4 Actual Evidence

### Status

```text
P4
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P4 Human PASS
= PASS

P4 Runtime Evidence
= ESTABLISHED

P4 Final Verdict
= PASS

P5
= NEXT / NOT AUTHORIZED
```

### Reviewed Closure-Failure Representation Used

```text
TaskExecutionResponse
= PreExecutionRejection | TerminalReturn

TerminalReturn
= execution_id
= execution_outcome
= business_result = ResearchResult | None
= record_ref = ExecutionRecordRef | None

P4 partial TerminalReturn
= execution_outcome = FAILED
= business_result = present
= record_ref = absent
```

P4 does not add a third response family or a new lifecycle enum. The existing `FAILED` outcome plus the independent presence of Business Result and absence of Record Ref distinguishes closure failure from P3's failed business execution with clean closure.

### Selected Failure-Injection Strategy

The deterministic P4 test patches the existing `StagingExecutionBundle.publish()` method to raise one controlled `RuntimeError`. The patch is test-only and is installed after composition without adding a production flag, Protocol, service, repository, or fault-injection API.

The selected seam is after Business Completion because `TaskRuntime.execute` has already:

```text
received ResearchCompletion
→ retained ActualSampleBoundary
→ retained Evidence
→ retained ResearchResult
→ recorded Research completion facts
→ finalized the in-memory success C6 candidate
→ entered StagingExecutionBundle.publish()
```

The failure is not injected in Search, Research Method, Provider, TT-17, or `_ExecutionAbort`.

### Actual Files and Symbols

```text
src/ecommerce_ai_os/runtime/execution.py
→ TerminalReturn.record_ref permits absence on failed closure

src/ecommerce_ai_os/runtime/task_runtime.py
→ TaskRuntime.execute bounded success-closure failure handling

tests/integration/test_fake_first_slice.py
→ FakeFirstSliceIntegrationTests.test_business_completion_survives_controlled_closure_failure
```

`LocalJsonRetention` and `StagingExecutionBundle` production behavior were reused without modification.

### Exact Actual P4 Control Path

```text
valid BusinessWorkRequest
→ Execution established
→ ResearchSkill runs successfully
→ SearchResult returned and retained
→ ResearchCompletion returned
→ Business Completion reached
→ Business Result retained and remains available
→ StableExecutionFacts records Research completion
→ successful C6 candidate finalized in memory
→ StagingExecutionBundle.publish() entered
→ controlled test-only RuntimeError
→ TaskRuntime recognizes clean closure did not complete
→ partial TerminalReturn(
     execution_outcome="FAILED",
     business_result=<existing ResearchResult>,
     record_ref=None
   )
```

### Required Semantic Proof

```text
Execution established = YES
ResearchSkill completed = YES
ResearchCompletion exists = YES
Business Completion reached = YES
Business Result exists = YES
closure attempt entered = YES
controlled closure failure occurred = YES
clean closure = NO
successful publication = NO
valid Record Ref = NO
Business Result erased = NO
PreExecutionRejection used = NO
P3 ExecutionAbort path used = NO
publication attempts = 1
automatic retry = NO
```

The attempted in-memory C6 candidate had `terminal_outcome = SUCCEEDED` and a real `research_result_ref`, proving business completion facts existed before publication failed. No finalized C6 record was published and no Record Ref was exposed.

### Observed Staging Behavior

```text
staging bundle = present
staged input = present
staged SearchResult = present
staged ActualSampleBoundary = present
staged Evidence = present
staged ResearchResult = present
staging execution_record.json = absent
final bundle = absent
```

This is an observed fact only. P4 does not establish deletion, retention, quarantine, cleanup, restart, or recovery policy for failed staging material.

### Tests Executed

```text
PYTHONPATH=src python -m unittest \
  tests.integration.test_fake_first_slice.FakeFirstSliceIntegrationTests.test_business_completion_survives_controlled_closure_failure \
  tests.integration.test_fake_first_slice.FakeFirstSliceIntegrationTests.test_established_failure_closes_with_path_sensitive_record \
  tests.integration.test_fake_first_slice.FakeFirstSliceIntegrationTests.test_incomplete_request_is_rejected_before_execution_establishment \
  tests.integration.test_fake_first_slice.FakeFirstSliceIntegrationTests.test_successful_fake_execution_publishes_resolvable_bundle -v
→ 4 tests / PASS

PYTHONPATH=src python -m unittest discover -s tests/unit -v
→ 21 tests / PASS

PYTHONPATH=src python -m unittest discover -s tests/integration -v
→ 5 tests / PASS

PYTHONPATH=src python -m unittest \
  tests.unit.architecture.test_import_directions -v
→ 1 test / PASS

python -m compileall -q src tests
→ PASS

git diff --check
→ PASS
```

### Actual Runtime / Test Evidence

```text
Runtime evidence root
= /tmp/ecommerce-ai-os-WI2-P4-runtime.ziIk6j/executions

execution_id
= dea75b2e-6a07-461b-ae76-632e34d9bd56

lifecycle event order
= business_completion
→ closure_failure

response type
= TerminalReturn

Execution outcome
= FAILED

Business Result exists / preserved
= YES / YES

Record Ref
= None

publication attempts
= 1

P3 ExecutionAbort calls
= 0

staging bundle
= present

final bundle
= absent

hypothetical Record Ref resolves
= NO
```

The `/tmp` path is inspectable review evidence only and is not a repository artifact, cleanup-policy decision, or durability guarantee.

### Architecture Mapping and Review Result

```text
A03 — existing TerminalReturn carries partial closure-failure result
A10 — ResearchCompletion / Business Completion occurred before closure failure
D02 — failed publication exposed no Record Ref and a hypothetical ref did not resolve
D04 — publish was attempted once, did not complete, final bundle stayed absent

Observed Contradictions = NONE
Architecture Deviation = NONE
Architecture Assumption Conflict = NONE

P5 = NEXT / NOT AUTHORIZED
```

---

# 21. P5 — Full Lifecycle Verification + Human Learning Review

P5 不新增业务能力。

P5 只验证整个 WI-02 lifecycle matrix：

```text
A. Normal Success

B. PreExecutionRejection

C. Established Execution Failure
   with clean failure C6 closure

D. Business Completion
   followed by closure failure
```

同时重新执行 WI-01 regression：

```text
Fake CLI success path

Architecture import guard

sequential Execution isolation

Record Ref resolution

bundle inspection

unit tests

integration tests

compile checks

git diff checks
```

P5 还必须证明：

```text
terminalization remains at-most-once

no second logical terminal outcome

no second independent C6 finalization

no execution-scoped state leakage

no real Provider

no TT-17

no WI-03 full Search semantics

no WI-06 Research Method expansion

no WI-07 full C6 expansion
```

P5 完成后进行：

```text
Architecture → Code → Test → Runtime Review

Delete Test / What-if Review

Human Learning Review

WI-02 Round Review
```

---

# 22. Traceability Coverage

WI-02 的主要 Traceability coverage：

```text
A03
C1 response family

A05
ExecutionContext + Execution Establishment

A09
ExecutionAbort

D01
C6 Execution Record — failure path depth

D02
Record Ref + post-terminal referenceability — failure path depth
```

辅助覆盖：

```text
A01
TaskRuntime.execute()

A04
TaskRuntime lifecycle ownership

A10
ResearchCompletion ordering

D03
Local JSON Execution Bundle regression

D04
STAGING → FINALIZED/PUBLISHED lifecycle regression
```

必须保持：

```text
Round coverage
!= implementation proof
```

只有实际：

```text
Code
+
Executed Test
+
Runtime Evidence
```

才能升级 Traceability status。

---

# 23. Candidate Implementation Surface After Human Authorization

以下只是基于现有 reviewed ownership 与 WI-01 actual code evidence 的候选 implementation surface。

它不是已批准的本轮文件 diff。

进入对应 checkpoint 前仍应以 live repository audit 和 `06` representation 为准。

可能涉及：

```text
src/ecommerce_ai_os/runtime/execution.py

src/ecommerce_ai_os/runtime/task_runtime.py

src/ecommerce_ai_os/runtime/execution_record.py

src/ecommerce_ai_os/runtime/retention.py
```

必要时：

```text
src/ecommerce_ai_os/application/cli.py
```

只能用于呈现已经 reviewed 的 C1 response semantics。

Application 不得吸收：

```text
lifecycle ownership

Business Method

failure classification ownership

C6 finalization
```

测试可能涉及：

```text
tests/unit/runtime/

tests/integration/

tests/unit/architecture/
```

不得因为实现方便扩大到 WI-03 / WI-06 / WI-07。

---

# 24. Explicitly Forbidden Architecture Drift

WI-02 implementation 不得静默引入：

```text
GenericTaskRuntime

ITask framework

Workflow DAG

State Machine framework

Agent Runtime

Agent Layer

Tool Layer

Standalone Orchestration Layer

Retry Engine

RetryService

ExecutionService

RecorderService

PersistenceService

Repository Layer

Event Bus

Message Architecture

Database

GlobalContext

UniversalTask

UniversalExecution

UniversalReference

ReferenceResolverService

SearchService

ResearchService

EvidenceService
```

不得把：

```text
private implementation mechanism
```

升级为：

```text
new architectural responsibility
```

除非真实 Runtime / Code Evidence 证明当前 reviewed representation 存在 blocking Architecture Assumption Conflict。

---

# 25. Acceptance Criteria

WI-02 只有同时满足以下条件，才能进入最终 Round PASS Review。

## AC-01 — Rejection Semantics

```text
Invalid WorkRequest
→ PreExecutionRejection
```

并证明：

```text
no Execution

no execution_id

no C6

no Record Ref
```

---

## AC-02 — Establishment Boundary

Valid WorkRequest 明确跨越一次：

```text
Execution Establishment Commit
```

commit 前后 lifecycle semantics 可区分。

---

## AC-03 — Post-establishment Failure

commit 后发生的 non-continuable failure：

```text
must not
be reported as PreExecutionRejection
```

---

## AC-04 — ExecutionAbort Boundary

```text
ExecutionAbort
= C2b-private control / unwind mechanism
```

并且没有泄漏为 public Contract。

---

## AC-05 — Failure Terminalization

established non-continuable failure 可以形成：

```text
terminal failure outcome
```

---

## AC-06 — Failure C6

failed Execution 可以形成合法 minimum failure C6。

---

## AC-07 — Failure Referenceability

failure C6 成功 publication 后：

```text
failure Record Ref
= resolvable
```

---

## AC-08 — Path-sensitive Facts

failure C6 只记录实际已经形成的 facts。

不得伪造：

```text
Evidence

Research Result

Provider use

Capability invocation
```

---

## AC-09 — Business Completion Ordering

```text
Business Completion
precedes
Execution clean closure
```

---

## AC-10 — Closure Failure

Business Completion 后 C6 finalization/publication failure：

```text
does not erase Business Completion
```

---

## AC-11 — No Fake Record Ref

closure failure 时：

```text
valid Record Ref
= absent
```

---

## AC-12 — At-most-once Terminalization

单一 Execution 不产生：

```text
second logical terminal outcome

second independent C6 finalization
```

---

## AC-13 — WI-01 Regression

WI-01 established success path remains PASS.

---

## AC-14 — Architecture Boundaries

Architecture import / responsibility constraints remain intact.

---

## AC-15 — Scope Discipline

未提前实现：

```text
WI-03

WI-04

WI-05

WI-06

WI-07

or deferred architecture
```

---

## AC-16 — No Hidden Architecture Conflict

```text
Architecture Assumption Conflict
= NONE
```

或者：

```text
FOUND
→ explicit review required
→ WI-02 cannot silently PASS
```

---

# 26. Delete Test / What-if Review

P5 至少检查以下 What-if。

## What-if 1 — Application catches deep Runtime exception directly

```text
Application
→ catches deep Runtime exception
→ prints failed
```

程序可能仍能运行。

但会绕过：

```text
C2b failure ownership

terminalization

C6 closure

C1 terminal semantics
```

Architecture：

```text
NOT PRESERVED
```

---

## What-if 2 — ExecutionAbort becomes public C1 response

可能减少内部转换代码。

但：

```text
implementation control signal
leaks into public semantic boundary
```

Architecture：

```text
NOT PRESERVED
```

---

## What-if 3 — PreExecutionRejection creates execution_id / C6

看起来可以“统一所有请求”。

但会破坏：

```text
BusinessWorkRequest
!= Execution

PreExecutionRejection
!= Execution Failure
```

Architecture：

```text
NOT PRESERVED
```

---

## What-if 4 — Every failure collapses into one FAILED status

例如不再区分：

```text
failed Execution with clean closure

vs

Business Completion followed by closure failure
```

代码可能更短。

但会丢失：

```text
Business Completion may have succeeded
while
Execution closure failed
```

Lifecycle semantics：

```text
NOT PRESERVED
```

---

## What-if 5 — Return Record Ref before successful publish

```text
C6 publication fails
→ return precomputed Record Ref anyway
```

Record Ref 可能无法解析。

会破坏：

```text
post-terminal referenceability

publication-before-reference semantics
```

Architecture：

```text
NOT PRESERVED
```

---

## What-if 6 — Automatically retry C6 publication

可能提高一次运行的成功率。

但：

```text
Retry Engine
= NOT REQUIRED / NOT PROVEN
```

这属于 Architecture Expansion。

当前：

```text
FORBIDDEN
```

---

# 27. Runtime Evidence Required for WI-02

P5 至少应能够观察：

## Scenario A — Success

```text
successful TerminalReturn

successful Record Ref

Record Ref resolves
```

## Scenario B — PreExecutionRejection

```text
PreExecutionRejection

no Execution

no execution_id

no C6

no Record Ref
```

## Scenario C — Established Execution Failure

```text
failed TerminalReturn

failure C6 exists

failure Record Ref exists

failure Record Ref resolves
```

## Scenario D — Closure Failure

```text
Business Completion reached

Business Result may exist

C6 publication/finalization failed

no valid Record Ref

clean closure not claimed
```

Runtime Evidence 必须服务于：

```text
What actually happened?

Was an Execution established?

What facts actually existed?

How did the Execution end?

Was closure clean?

Can the returned Record Ref resolve?
```

Runtime Evidence 不是：

```text
logs

stack dump

human memory
```

---

# 28. Architecture Change Rule

WI-02 不允许因为实现麻烦而静默修改 Architecture。

如果真实代码或 Runtime Evidence 发现：

```text
reviewed lifecycle assumption cannot be implemented

existing C2b responsibility cannot carry required behavior

reviewed C1 response representation blocks required semantics

C6 publication model cannot represent required closure distinction

current representation contains a blocking contradiction
```

必须：

```text
Code / Runtime Evidence
↓
Record Contradiction
↓
Classify

Implementation Defect
or
Architecture Assumption Conflict
↓
Explicit Human Review
↓
Architecture Change only if approved
```

原则：

```text
Evidence first.
Architecture change second.
```

---

# 29. Repository Materialization Rule

Human Review 通过后，本文件才进入 repository materialization。

Materialization 必须遵循：

```text
Canonical Human-reviewed text
→ Codex writes exact approved Markdown
→ Codex does not independently redesign or rewrite
→ live repository facts replace explicit placeholders
→ git diff review
```

Codex 在 materialization 阶段可以：

```text
verify live HEAD

verify branch

verify worktree

write approved document

run git diff --check

show git diff
```

Codex 不可以：

```text
independently redesign lifecycle

add new architectural conclusions

invent new Contract

invent new Service

restructure approved semantics

silently promote Candidate wording
```

因此：

```text
Design text
= Human / architecture discussion ownership

Repository facts
= Codex / live repository evidence

Materialization
= mechanical repository operation
```

---

# 30. P0 Human Review Gate

当前：

```text
WI-02
= P4 Complete / Implemented / Tested / Human Reviewed / Pass

P0
= COMPLETE / HUMAN REVIEWED / PASS

Audit
= PASS

06 Representation Check
= PASS

Blocking Contradiction
= NONE

Architecture Assumption Conflict
= NONE

Python
= P4 ACTUAL / COMMITTED

Tests
= P4 ACTUAL / COMMITTED

P1
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS
```

P0 Human Review 只批准：

> WI-02 的 Goal、Scope、四条 lifecycle verification scenarios、关键 semantic distinctions、P0-P5 checkpoint sequencing、Acceptance Criteria 与 deferred boundaries 足以指导后续 Walking Implementation。

批准 P0 不代表：

```text
P1 code already exists

ExecutionAbort implemented

failure C6 implemented

closure failure representation finalized

full Runtime State taxonomy approved

full C6 semantics approved

WI-02 PASS
```

并且：

```text
P0 Human Review PASS
!= immediate P1 code authorization
```

P1 pre-implementation audit prerequisites 已完成：

```text
live repository audit = PASS

+
06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md review = PASS

+
blocking contradiction = NONE
```

这些 audit prerequisites 已在 P1 implementation 前完成；P1 actual evidence 已通过 Human Review。

---

# 31. Current Next

当前已确认：

```text
P0 Human Review
= PASS

Required Pre-P1 Live Repository Audit
= PASS

06 Representation Check
= PASS

Blocking Contradiction
= NONE
```

因此当前导航为：

```text
Current Next
= P5 — NEXT / NOT AUTHORIZED
```

但必须保持：

```text
P2
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P2 Human PASS
= PASS

P3
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P3 Human PASS
= PASS

P4
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P4 Human PASS
= PASS

P5
= NEXT / NOT AUTHORIZED
```

P1 已实现范围：

```text
PreExecutionRejection boundary

Execution Establishment boundary

minimum C1 response distinction required
for those paths

WI-01 success-path regression
```

P1 不允许提前实现：

```text
ExecutionAbort

failure C6

closure failure

full SearchFailure

full Search semantics

full Research Method

full C6 semantics
```

---

# 32. Final Current Status

```text
WI-02 — Execution Lifecycle

Canonical Round Plan
= HUMAN REVIEWED

Repository Materialization
= PERFORMED

Audit
= PASS

Audit Changes
= INCORPORATED

Inherited WI-01 Baseline
= COMPLETE / PASS

P0
= COMPLETE / HUMAN REVIEWED / PASS

P1
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

Current Next
= P5 — NEXT / NOT AUTHORIZED

P1 Implementation
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P1 Human PASS
= PASS

P1 Runtime Evidence
= ESTABLISHED

P2
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P2 Human PASS
= PASS

P2 Final Verdict
= PASS

P3
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P3 Human PASS
= PASS

P3 Final Verdict
= PASS

P4
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P4 Human PASS
= PASS

P4 Runtime Evidence
= ESTABLISHED

P4 Final Verdict
= PASS

P5
= NEXT / NOT AUTHORIZED

Python Changes
= P4 ACTUAL / COMMITTED

Test Changes
= P4 ACTUAL / COMMITTED

Architecture Reopen
= NO

Contract Reopen
= NO

New Contract
= NO

New Service
= NO

Live Provider
= NO

TT-17
= NO

Architecture Expansion
= NOT AUTHORIZED

Pre-P1 Live Repository Audit
= PASS

06 Representation Check
= PASS

Blocking Contradiction
= NONE

Architecture Deviation
= NONE

Architecture Assumption Conflict
= NONE
```
