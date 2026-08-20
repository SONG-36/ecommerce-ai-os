# Ecommerce AI OS — First Research Slice — Walking Implementation Plan

- **Project**: Ecommerce AI OS
- **Phase**: Walking Implementation
- **Document Type**: Walking Implementation Master Plan / 执行与学习总计划
- **Status**: ACTIVE
- **Architecture Authority**: No
- **Authorized Scope**: US / Car Vacuum / TikTok Content Research First Slice ONLY
- **Walking Implementation**: AUTHORIZED
- **Architecture Expansion**: NOT AUTHORIZED
- **Current Round**: WI-1
- **Current Round Status**: COMPLETE / PASS
- **Current Next**: WI-2 — Execution Lifecycle / NEXT / NOT STARTED

---

# 0. 文档目的

本文件定义 First Research Slice 在完成 Minimal Software Architecture Review 后，
如何从已经审查通过的软件设计逐步进入真实代码。

它解决的问题不是：

> Ecommerce AI OS 最终应该设计成什么样。

该问题已经由上游 Product / System / Detailed Contract / Minimal Software Architecture 文档负责。

本文件解决的是：

> 已审查的软件架构，如何通过一系列最小、可运行、可验证、可学习的纵向实现 Round，
> 一步一步变成真实软件。

因此：

```text
Architecture Documents
= 为什么这样设计、边界是什么

Walking Implementation Plan
= 如何把已经审查过的设计逐步实现出来
```

本文件不是新的 Architecture Specification，
不具有 Architecture Authority，
也不得重新定义已经冻结的 Contract 或 System Responsibility。

---

# 1. 当前授权基线

当前 First Slice 已完成：

```text
Step 1–5
= CANDIDATE COMPLETE

Step 6
= CANDIDATE COMPLETE /
  REFINED AFTER STEP 7 REVIEW

Step 6 Refinement Sync
= COMPLETE

Step 7
= PASS

Final Consistency Re-check
= PASS

G1 ~ G15
= PASS

S7-R1 ~ S7-R10
= RESOLVED
```

因此：

```text
Minimal Software Architecture
= REVIEWED / IMPLEMENTATION-READY FOR FIRST SLICE
```

Human 已明确授权：

```text
Walking Implementation
= AUTHORIZED
```

授权范围仅为：

```text
US / Car Vacuum / TikTok Content Research First Slice
```

本授权不包含：

```text
Architecture Expansion
```

即：

```text
Walking Implementation
=
实现已经 Review PASS 的 First-Slice Minimal Software Architecture

Walking Implementation
!=
边写代码边自由重构 Product / System / Software Architecture
```

---

# 2. 上游设计输入

Walking Implementation 必须继承以下已审查文档：

```text
00_MINIMAL_SOFTWARE_ARCHITECTURE_PLAN.md
01_SOFTWARE_RESPONSIBILITY_MAPPING.md
02_EXECUTION_SPINE_SOFTWARE_DESIGN.md
03_SEARCH_PROVIDER_SPINE_SOFTWARE_DESIGN.md
04_RESEARCH_EVIDENCE_SOFTWARE_DESIGN.md
05_EXECUTION_RECORD_REFERENCEABILITY_SOFTWARE_DESIGN.md
06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md
07_MINIMAL_SOFTWARE_ARCHITECTURE_REVIEW.md
```

这些文件回答：

```text
Responsibility
Contract
Software Representation
Dependency Direction
Runtime Boundary
Provider Boundary
Research / Evidence Boundary
Execution Record / Referenceability
```

Walking Implementation 不重新决定这些问题。

---

# 3. Walking Implementation 的核心方法

## 3.1 不采用横向模块式开发

当前不采用：

```text
先把 runtime 全写完
↓
再把 research 全写完
↓
再把 search 全写完
↓
再把 provider 全写完
↓
最后第一次集成
```

这种方法会产生大量：

```text
代码已经存在
但从未证明能够一起工作
```

的模块。

---

## 3.2 采用纵向 Walking Slice

当前方法：

```text
真实业务问题
↓
选择一个最小行为
↓
穿过必要的软件边界
↓
形成最小可执行纵向链
↓
真正运行
↓
观察输出
↓
自动测试
↓
对照 Architecture
↓
学习这一轮的工程概念
↓
Review
↓
修正
↓
进入下一 Round
```

英文简称：

```text
Real Business Problem
→ Minimal Executable Vertical Slice
→ Run
→ Observe
→ Test
→ Architecture Mapping
→ Learn
→ Review
→ Revise
→ Next Round
```

---

# 4. Walking Implementation 的完成定义

代码生成不等于 Round 完成。

每个 Round 至少必须形成：

```text
Implementation
+
Executable Runtime Path
+
Tests
+
Runtime Evidence
+
Architecture → Code Mapping
+
Learning Review
+
Round Review
```

即：

```text
Code exists
!=
Round complete
```

并且：

```text
Tests pass
!=
Architecture understood
```

以及：

```text
Can run
!=
Architecture is correct
```

---

# 5. 八个 Walking Round 总览

| Round | 中文名称 | 核心目标 | 主要实现 | 主要验证 | 学习重点 | 当前状态 |
|---|---|---|---|---|---|---|
| WI-1 | Fake 第一条可执行纵向切片 | 第一次跑通内部完整闭环 | CLI / C1 / C2b / C2a / Fake C3 / ResearchCompletion / C6 / JSON | 一条 CLI 真正形成 TerminalReturn + Record Ref + Bundle | Vertical Slice / Protocol / DI / Runtime vs Business Method | COMPLETE / PASS |
| WI-2 | 执行生命周期与失败闭环 | 把 Execution semantics 做正确 | PreExecutionRejection / Establishment / ExecutionAbort / failure closure | success / rejection / runtime failure / closure failure | Lifecycle / State / Failure / Exception | NEXT / NOT STARTED |
| WI-3 | C3 Search 数据契约 | 建立真实的 provider-neutral Search semantics | SearchRequest / Result / Failure / Context / Provenance | duplicates / missingness / partial retrieval / continuation | Data Contract / Missingness / Bounded Completeness | PLANNED |
| WI-4 | Scrape Creators Adapter | 把外部 Provider schema 隔离在 C4b 下 | Adapter / Access Protocol / real TT-17 fixtures | Raw TT-17 → provider-neutral SearchResult | Adapter / Ports & Adapters / Anti-Corruption Layer | PLANNED |
| WI-5 | Live TT-17 | 第一次真正访问外部 Provider | HttpClient / AppConfig / secret / raw capture / live smoke | 实际 TT-17 → SearchResult → provenance | HTTP / I-O / Config / Secrets / Integration | PLANNED |
| WI-6 | Research Method | 第一次产生真实 Research Result | Sampling / Evidence / Finding / Hypothesis / ResearchCompletion | SearchResult → ResearchResult | Sampling / Evidence / Causal Discipline | PLANNED |
| WI-7 | Execution Record & Traceability | 完整落实 C6 与 referenceability | refs / versions / publish / resolution | Record Ref 可追完整执行链 | Retention / Persistence / Provenance / Reproducibility | PLANNED |
| WI-8 | First Slice 验收 | 不再加能力，只做最终验收 | E2E / architecture tests / live smoke / bundle inspection | First Slice 重复运行 + 架构反馈 | Acceptance / Architecture Feedback Loop | PLANNED |

`PLANNED` 仅表示当前 Walking Implementation 已定义路线。

它不意味着：

```text
Permanent Backlog Commitment
```

也不代表后续 Round 不可以基于真实 Runtime Evidence 调整范围。

---

# 6. WI-1 — Fake First Executable Vertical Slice

## 6.1 目标

第一次证明：

> 已审查的 Minimal Software Architecture 可以真实形成一条端到端可运行的软件链。

第一轮不追求业务分析质量。

第一轮优先证明：

```text
software shape can execute
```

---

## 6.2 目标调用链

```text
Terminal / CLI
↓
BusinessWorkRequest
↓
TaskRuntime.execute()                  C1
↓
ExecutionContext                      C2b
↓
RuntimeResearchExecutionPort
↓
Concrete ResearchSkill                C2a
↓
ResearchExecutionPort.search(...)
↓
Fake SearchCapability                 C3 fake
↓
SearchResult
↓
Research Skill
↓
ResearchCompletion
↓
TaskRuntime recognizes Business Completion
↓
C6 finalization
↓
Local JSON Execution Bundle
↓
Record Ref
↓
TerminalReturn
↓
CLI
```

---

## 6.3 当前允许实现

```text
Thin CLI
BusinessWorkRequest
TaskRuntime
ExecutionContext
RuntimeResearchExecutionPort
ResearchSkill Protocol
Concrete minimal First-Slice Research Skill
ResearchExecutionPort
SearchCapability Protocol
Fake SearchCapability
minimum SearchResult
minimum ResearchCompletion
minimum ResearchResult
minimum ActualSampleBoundary / Evidence required by closure
StableExecutionFacts
FinalizedExecutionRecord
Local JSON Execution Bundle
TerminalReturn
```

只实现 WI-1 真正需要的最小深度。

---

## 6.4 当前禁止实现

WI-1 不允许：

```text
Live Scrape Creators
ScrapeCreatorsHttpClient
real TT-17 request
complex Adapter mapping
production Research Method
advanced sampling
dynamic Provider Resolution
multi-provider
Retry Engine
Async
Event Bus
Database
Repository
Full Evidence Service
Knowledge
Artifact
Agent
Analyze Service
Production UI
```

---

## 6.5 验收

必须至少能够真实执行一次类似：

```bash
python -m ecommerce_ai_os.application.cli ...
```

并得到：

```text
Execution Outcome
Research Result / Business Result
Record Ref
```

文件系统形成：

```text
var/executions/<execution_id>/
```

至少能够人工检查：

```text
execution_record.json
input
ResearchResult-related retained fact
```

Round 不以：

```text
代码编译成功
```

作为完成标准。

---

## 6.6 学习重点

WI-1 只重点学习：

```text
Vertical Slice
Protocol
Dependency Injection
Execution Runtime Owner
Business Method vs Runtime Coordination
C1 / C2a / C2b
```

不在这一轮扩展到完整 DDD / Clean Architecture / SOLID 课程。

---

# 7. WI-2 — Execution Lifecycle

## 7.1 目标

将 WI-1 中能运行的 Execution Spine，
进一步验证为符合已冻结生命周期语义的执行模型。

---

## 7.2 至少验证四条路径

### A. 正常成功

```text
Valid WorkRequest
→ Execution Established
→ ResearchCompletion
→ Business Completion
→ C6
→ Execution Completion
```

### B. 执行前拒绝

```text
Invalid WorkRequest
→ PreExecutionRejection

no Execution
no execution_id
no C6
no Record Ref
```

### C. 执行建立后的不可继续失败

```text
Execution Established
→ Capability / Runtime Failure
→ non-continuable
→ private ExecutionAbort
→ TaskRuntime catches
→ failure C6
→ terminal failure
```

### D. Business Completion 后 closure 失败

```text
ResearchCompletion
→ Business Completion succeeded
→ C6 finalization / publication fails
→ Business Result may still exist
→ Execution Closure failed
→ no valid Record Ref
```

---

## 7.3 学习重点

```text
Execution Lifecycle
State Transition
Execution Establishment Commit Boundary
Business Failure
Execution Failure
Exception
Terminalization
```

---

# 8. WI-3 — Search Semantics

## 8.1 目标

把 Fake Search 从：

```text
返回几个视频
```

提升为：

```text
真实表达 C3 provider-neutral Search semantics
```

---

## 8.2 核心软件表示

```text
SearchRequest
SearchResult
SearchFailure
SearchInvocationContext
SearchInvocationProvenance
RawProviderResultRef
```

---

## 8.3 Fake Search 必须主动模拟现实问题

例如：

```text
duplicates
missing caption
valid empty result
partial retrieval
continuation available
bounded retrieval
requested region = US
unknown global completeness
different observation times
```

---

## 8.4 核心验证

必须证明：

```text
SearchResult
!= list[Video]
```

因为 Search Result 还必须说明：

```text
这些结果从哪里来
取得多少
为什么停止
是否还有 continuation
哪些字段缺失
是否存在重复
数据什么时候观测
Provider provenance 是什么
```

---

## 8.5 学习重点

```text
Data Contract
Boundary Model
Information Loss
Missingness
Pagination Semantics
Bounded Completeness
Provenance
```

---

# 9. WI-4 — Scrape Creators Adapter

## 9.1 目标

第一次真正实现 C4b，但不进行 live 网络访问。

采用：

```text
saved real TT-17 fixture
↓
Fake ScrapeCreatorsAccess
↓
ScrapeCreatorsAdapter
↓
SearchResult
```

---

## 9.2 验证重点

```text
Provider-specific ID
Publication Time
Metric Observation Time
Missingness
Duplicates
Pagination
Provider Error
Region / Filter quirks
RawProviderResultRef
```

---

## 9.3 核心边界

```text
Adapter
!= Access Mechanism
!= Concrete Provider
```

以及：

```text
Translation
!= Business Interpretation
```

---

## 9.4 学习重点

```text
Adapter Pattern
Ports & Adapters
Anti-Corruption Layer
External System Isolation
```

---

# 10. WI-5 — Live TT-17

## 10.1 目标

第一次从真实 Scrape Creators 进入已实现的软件边界。

---

## 10.2 当前最小实现

```text
ScrapeCreatorsHttpClient
AppConfig
SCRAPE_CREATORS_API_KEY
HTTP request
raw response capture
ScrapeCreatorsAdapter
live smoke test
```

---

## 10.3 第一次 live 调用约束

只进行最小合法调用，例如：

```text
query = car vacuum
region = US
```

当前不得自动加强：

```text
date_posted
sort_by
region semantics
ranking semantics
hard cap
global completeness
```

---

## 10.4 主要学习

```text
HTTP
I/O Boundary
Configuration
Secret Handling
Integration Test
Live Smoke Test
External Failure
```

---

# 11. WI-6 — Research Method

## 11.1 目标

第一次真正实现 First Slice 的业务研究方法。

链路：

```text
SearchResult
↓
Relevance
↓
Research Dedupe
↓
Sampling
↓
ActualSampleBoundary
↓
Evidence Admission
↓
Evidence
↓
Finding
↓
Testable Hypothesis
↓
ResearchResult
↓
ResearchCompletion
```

---

## 11.2 必须保持

```text
Search Result != Evidence
Observed Fact != Interpretation
Finding != Validated Business Truth
Hypothesis != Proven Result
Insufficient Evidence != Execution Failure
```

---

## 11.3 学习重点

```text
Sampling
Evidence
Observation vs Interpretation
Traceability
Causal Discipline
Research Result Boundary
```

---

# 12. WI-7 — Execution Record & Traceability

## 12.1 目标

让一次 Execution 真正能够被事后解释和追踪。

从：

```text
Record Ref
```

能够追踪：

```text
Execution
→ WorkRequest
→ Skill + version
→ Capability + version
→ Actually Used Provider
→ Adapter + version
→ SearchResult
→ RawProviderResultRef
→ ActualSampleBoundary
→ Evidence
→ ResearchResult
```

---

## 12.2 必须保持

```text
Runtime State
!= Stable Execution Facts
!= Finalized Execution Record
```

以及：

```text
Retention
!= Persistence Architecture
```

---

## 12.3 学习重点

```text
Reference
Referenceability
Resolvability
Retention
Persistence
Provenance
Reproducibility
```

---

# 13. WI-8 — First Slice Acceptance

## 13.1 原则

WI-8 不增加新能力。

只验证：

> First Slice 是否已经形成一个内部一致、可重复运行、符合架构约束的 Walking Implementation。

---

## 13.2 至少验证

```text
Unit Tests
Fake Provider Integration
Execution Bundle Integration
Architecture Import-Boundary Tests
CLI Fake End-to-End
Opt-in TT-17 Live Smoke
Manual Bundle Inspection
```

---

## 13.3 手工检查重点

```text
Secrets not retained

Required refs resolve

Raw Provider payload does not leak into ResearchResult

C6 does not become log dump

ResearchResult does not become Evidence dump

Provider cursor does not leak above C4b

Duplicates / missingness / limitations survive correctly
```

---

## 13.4 最终架构反馈问题

只问：

> 真实代码和 Runtime Evidence 是否证明任何已经审查通过的 Architecture assumption 是错误的？

如果没有：

```text
First Slice Walking Implementation
= PASS
```

如果有：

```text
Runtime / Code Evidence
→ record contradiction
→ classify:
   implementation defect
   or architecture assumption conflict
→ explicit review
```

不得在实现过程中偷偷修改 Architecture。

---

# 14. Round-specific Architecture Reading Map

不是每轮都重新加载全部 8 份 Architecture 文档。

使用：

| Round | 主要阅读输入 |
|---|---|
| WI-1 | `00`, `01`, `02`, `06`, `07` |
| WI-2 | `02`, `05`, `06` |
| WI-3 | `03`, `06` |
| WI-4 | `03`, `06` + Provider Mapping / TT-17 facts |
| WI-5 | `03`, `06` + 当前 TT-17 Provider Lab runtime evidence |
| WI-6 | `04`, `06` |
| WI-7 | `05`, `06` |
| WI-8 | `00`, `06`, `07` + WI-1～WI-7 Round Records |

目的：

```text
reduce context load
+
preserve relevant authority
+
avoid unrelated architecture contamination
```

如果某轮发现确实需要其它上游文档，
可以追加读取，
但不默认重新加载全部文档。

---

# 15. 每个 Round 的固定生命周期

每一轮采用：

```text
PLAN
→ IMPLEMENT
→ RUN
→ REVIEW
→ COMPLETE
```

详细流程：

```text
1. Round Planning
2. Architecture Reading Map
3. Pre-Code Learning
4. Codex Implementation
5. Run + Test
6. Codex Implementation Evidence Report
7. Architecture-Code Traceability Update
8. Human Learning Review
9. Questions / Delete Test / What-if
10. Round Review
11. Commit
12. Next Round
```

不得跳过：

```text
RUN
TEST
LEARNING REVIEW
ROUND REVIEW
```

---

# 16. Pre-Code Learning 规则

每轮开始写代码前，
只学习当前 Round 即将出现的 3～5 个核心概念。

例如：

WI-1：

```text
Vertical Slice
Protocol
Dependency Injection
Runtime Coordination
Business Method
```

WI-3：

```text
Data Contract
Missingness
Pagination
Bounded Completeness
Provenance
```

原则：

```text
Learn just before use
```

而不是提前展开完整软件工程理论课程。

---

# 17. Codex Implementation 规则

Codex 的主要职责是：

```text
Implement
Run
Test
Report Facts
```

Codex 不负责替 Human 重新设计 Architecture。

Codex 每轮必须遵守：

```text
Current Round Scope
Current Architecture Reading Map
Allowed Files
Forbidden Files
Acceptance Criteria
Architecture Guardrails
```

不得提前实现后续 Round。

例如：

```text
WI-1
!= permission to implement WI-2 ~ WI-8
```

---

# 18. Codex Implementation Evidence Report

每个 Round 实现结束后，
Codex 必须至少返回：

```text
1. Round Goal

2. Files Changed

3. New / Modified Symbols
   - classes
   - functions
   - dataclasses
   - Protocols

4. Actual Runtime Path

5. Architecture → Code Mapping

6. Tests Executed
   command
   result

7. Runtime Artifacts

8. Architecture Deviations
   NONE / FOUND

9. Deferred Items

10. Git Status
```

Codex 报告的目标：

```text
facts
not generic tutorial
```

---

# 19. Architecture → Code → Test → Runtime 学习模型

每个核心概念最终都应该能够回答四个问题：

```text
Architecture
为什么存在？

↓

Code
实际在哪里实现？

↓

Test
怎么证明实现没有破坏边界？

↓

Runtime Evidence
真正运行时能看到什么事实？
```

例如：

```text
C1 Task Execution Boundary

Architecture:
02 / 06

Code:
TaskRuntime.execute()

Test:
runtime execution test

Runtime Evidence:
TerminalReturn + Execution Bundle
```

这个映射由：

```text
01_ARCHITECTURE_CODE_TRACEABILITY.md
```

持续维护。

---

# 20. Human Learning Review

每个 Round commit 前，
必须做一次人工 Learning Review。

至少能够回答：

```text
1. 当前真实 call path 是什么？

2. 谁拥有 Business Decision？

3. 谁拥有 Execution Lifecycle？

4. 每一个主要 Protocol 隔离了什么？

5. 如果删除某个 abstraction：
   代码还能不能运行？
   架构会失去什么？

6. 当前代码分别对应哪些 Architecture 文档？

7. 哪个 Test 在证明哪个 Architecture constraint？

8. 哪个 Runtime Artifact 能证明这次 Execution 的真实事实？
```

---

# 21. Delete Test / What-if 学习法

学习重点不是背：

```text
这个类叫什么
```

而是理解：

```text
为什么存在。
```

因此每轮至少选择若干真实 abstraction 做 Delete Test。

例如：

```text
删除 ResearchSkill Protocol，
让 TaskRuntime 直接 import concrete skill。

Can run?
可能可以。

Architecture consequence?
Runtime 与 concrete business method 强耦合。
```

又例如：

```text
让 Research Skill 直接实例化 ScrapeCreatorsAdapter。

Can run?
可能可以。

Architecture consequence?
Business Method 直接依赖 Provider-specific infrastructure。
```

核心：

```text
Can run
!=
Good boundary
```

---

# 22. Architecture Change Rule

Walking Implementation 不允许静默重构 Architecture。

如果真实代码或 Runtime Evidence 发现：

```text
architecture assumption cannot be implemented

real TT-17 behavior contradicts bounded semantics

existing responsibility cannot carry required behavior

current representation contains a blocking contradiction
```

必须停止“顺手修架构”。

正确流程：

```text
Code / Runtime Evidence
↓
Record Contradiction
↓
Classify
├── Implementation Defect
└── Architecture Assumption Conflict
↓
Explicit Review
↓
Architecture Change only if approved
```

原则：

```text
Evidence first.
Architecture change second.
```

---

# 23. Deferred / Not Yet Proven / Rejected Guardrails

Walking Implementation 授权不自动提升：

```text
Agent as Top-level Layer
Tool as Top-level Layer
Standalone Orchestration
Independent Analyze Capability
Full Evidence Service
Independent Research Service
Knowledge Integration
Artifact Integration
Retry Engine
Checkpoint
Crash Recovery
Durable Execution
Event / Message Architecture
Dedicated Persistence Service
Database
Vector DB / RAG
Provider Router
Multi-provider Fallback
Async Architecture
SearchService
EvidenceService
ResearchService
RecorderService
Repository Layer
GlobalContext
UniversalReference Registry
97 API Full Integration
```

如果未来真实 evidence 要求其中某项，
必须单独提出。

---

# 24. Round Record 规则

计划目录：

```text
walking_implementation/
└── rounds/
    ├── WI_01_FAKE_VERTICAL_SLICE.md
    ├── WI_02_EXECUTION_LIFECYCLE.md
    ├── WI_03_SEARCH_SEMANTICS.md
    ├── WI_04_SCRAPE_CREATORS_ADAPTER.md
    ├── WI_05_LIVE_TT17.md
    ├── WI_06_RESEARCH_METHOD.md
    ├── WI_07_EXECUTION_RECORD_TRACEABILITY.md
    └── WI_08_FIRST_SLICE_ACCEPTANCE.md
```

但不提前创建 8 个空文件。

规则：

```text
进入一个 Round
→ 创建对应 Round Record
```

Round Record 初始只包含：

```text
Goal
Scope
Architecture Inputs
Expected Call Path
Allowed Changes
Not In Scope
Acceptance Criteria
Learning Focus
```

实施后追加：

```text
Implementation Result
Actual Files
Actual Symbols
Actual Call Path
Tests
Runtime Evidence
Architecture Mapping
Discovered Contradictions
Learning Review
Final Verdict
```

---

# 25. Round Record 与 Master Plan 的职责区别

```text
00_WALKING_IMPLEMENTATION_PLAN.md
= 整个 Walking Implementation 怎么走

rounds/WI_xx_xxx.md
= 某一轮实际上发生了什么
```

Round Record 不重新定义 Master Plan。

如果真实 evidence 需要调整后续路线，
先 Review，再更新 Master Plan。

---

# 26. Architecture-Code Traceability 更新规则

每个 Round 完成后，
必须更新：

```text
01_ARCHITECTURE_CODE_TRACEABILITY.md
```

至少补：

```text
Architecture concept
Architecture source
selected software representation
actual file
actual symbol
test
runtime evidence
first implementation Round
verification status
```

不得伪造尚未实现的映射。

---

# 27. Traceability 状态推进原则

简单使用：

```text
PLANNED
IMPLEMENTED
TESTED
RUNTIME VERIFIED
```

必须基于证据推进。

例如：

```text
Architecture says TaskRuntime.execute()
↓
no code yet
= PLANNED

code exists
= IMPLEMENTED

unit/integration test passes
= TESTED

real/fake executable Round demonstrates behavior
= RUNTIME VERIFIED
```

---

# 28. Git / Commit 规则

默认：

```text
One Walking Round
→ One coherent implementation/review cycle
→ One Round-level commit
```

具体：

```text
implement
↓
run
↓
test
↓
evidence report
↓
traceability update
↓
learning review
↓
round review
↓
commit
```

不要：

```text
WI-1 + WI-2 + WI-3
→ one giant commit
```

也不要：

```text
每写一个小函数
→ 一个无意义 commit
```

Commit 应对应：

```text
可理解的业务 / engineering increment
```

---

# 29. Runtime Evidence 原则

Walking Implementation 必须尽可能保留可检查的运行证据。

但：

```text
Runtime Evidence
!= Logs
!= Debug Output
!= Human Memory
```

至少应能够观察并保留：

```text
Execution Outcome
Business Result / ResearchResult
Record Ref
Execution Bundle
Stable Execution Facts
SearchResult boundary facts
Actual Sample Boundary
Evidence references
Provider provenance
```

Runtime Evidence 必须服务于：

```text
What actually happened?
What was actually used?
What was actually retained?
What can be resolved later?
```

但必须同时遵守：

```text
Secrets not retained
Raw Provider payload not automatically promoted to ResearchResult
Logs are not the Finalized Execution Record
Execution Record is not an Evidence dump
```

运行证据的目标是支持事实核对、学习复盘、Traceability 更新和架构反馈，
而不是把所有中间状态无边界地写入 bundle。

---

# 30. Round PASS 条件

一个 Round 只有在以下条件全部满足时，才能标记为 `PASS` 或进入下一轮：

```text
1. Round Scope was respected

2. Architecture Reading Map was applied

3. Allowed implementation was completed

4. Forbidden or deferred capability was not silently introduced

5. Expected Runtime Path actually ran

6. Required tests were executed and passed

7. Runtime Evidence was collected and inspectable

8. Codex Implementation Evidence Report was returned

9. Architecture → Code → Test → Runtime mapping was updated

10. Human Learning Review was completed

11. Delete Test / What-if review was completed where required

12. No unreviewed Architecture Assumption Conflict remains

13. Round Record was updated with the actual result

14. Git scope was inspected
```

如果任一项未满足：

```text
Round
!=
PASS
```

允许状态包括：

```text
IN PROGRESS
BLOCKED
PASS WITH FOLLOW-UP
REQUIRES REVIEW
```

但不得把未完成的 Round 伪装成 `PASS`。

---

# 31. First Slice 最终 PASS 条件

WI-8 结束时，First Research Slice 至少必须满足：

```text
WI-1 ~ WI-8 Round Records complete

Fake path is repeatable

Execution success path is repeatable

Pre-execution rejection is distinguishable from execution failure

Runtime failure and closure failure are distinguishable

C3 SearchResult preserves bounded retrieval semantics

C4b Provider-specific behavior remains behind the Adapter boundary

ResearchResult does not silently become raw SearchResult or Evidence dump

Actual Sample Boundary is explicit

Execution Record can resolve the required references

TerminalReturn is not the only retained execution fact

Architecture import-boundary tests pass

Opt-in live TT-17 smoke path is separately identified

No secret is retained in runtime artifacts

No unresolved Architecture Assumption Conflict is hidden in implementation
```

最终只问：

```text
真实代码 + Tests + Runtime Evidence
是否共同证明 First Slice 能够按已审查架构运行？
```

如果答案是肯定的：

```text
First Slice Walking Implementation
= PASS
```

如果答案是否定的：

```text
First Slice Walking Implementation
= NOT PASS
```

并按照第 22 节的 Architecture Change Rule 处理。

---

# 32. 最终状态与授权边界

本文件的最终状态：

```text
Walking Implementation Plan
= ACTIVE
```

当前状态：

```text
Architecture
= REVIEWED / IMPLEMENTATION-READY FOR FIRST SLICE

Walking Implementation
= AUTHORIZED

Architecture Expansion
= NOT AUTHORIZED

Current Round
= WI-1

Current Round Status
= COMPLETE / PASS

WI-1 Internal Checkpoints
= P0-P5 COMPLETE

WI-1 Checkpoint Commits
= P1 c400f33
= P2 c169f2f
= P3 bca1175
= P4 8d4ea24
= P5 fbc31e5

WI-1 Runtime Evidence
= ESTABLISHED

WI-1 Final Verdict
= PASS

Current Next
= WI-2 — Execution Lifecycle / NEXT / NOT STARTED
```

授权仅适用于：

```text
US / Car Vacuum / TikTok Content Research First Slice
```

授权不意味着：

```text
system-wide implementation
platform completion
multi-provider productization
production readiness
architecture finality
```

任何超出 First Slice 的实现，都必须重新定义范围并获得明确授权。

---

# 33. 最终执行规则

后续每次开始一个 Walking Round 时，必须先回答：

```text
What is the current Round?
What is the current Goal?
What is the Architecture Reading Map?
What is allowed?
What is forbidden?
What must run?
What must be tested?
What Runtime Evidence must be retained?
What must be learned?
What is the PASS condition?
```

每个 Round 都必须沿着以下闭环推进：

```text
Read the relevant Architecture
↓
Plan the smallest vertical increment
↓
Implement only the authorized scope
↓
Run the real path
↓
Test the boundary and failure behavior
↓
Capture Runtime Evidence
↓
Report implementation facts
↓
Update Architecture-Code Traceability
↓
Complete Human Learning Review
↓
Review the Round
↓
Commit the coherent increment
↓
Enter the next Round only after PASS
```

最终原则：

```text
先理解边界，再实现行为。

先运行并观察，再宣称完成。

先记录证据，再讨论架构是否需要改变。

先完成当前 Round，再进入下一 Round。

Walking Implementation
= controlled learning through executable vertical slices
```

---

# Final Status

```text
00_WALKING_IMPLEMENTATION_PLAN.md
= ACTIVE

Architecture
= REVIEWED / IMPLEMENTATION-READY FOR FIRST SLICE

Walking Implementation
= AUTHORIZED

Architecture Expansion
= NOT AUTHORIZED

Current Round
= WI-1

Current Round Status
= COMPLETE / PASS

WI-1 Runtime Evidence
= ESTABLISHED

WI-1 Final Verdict
= PASS

Current Next
= WI-2 — Execution Lifecycle / NEXT / NOT STARTED
```
