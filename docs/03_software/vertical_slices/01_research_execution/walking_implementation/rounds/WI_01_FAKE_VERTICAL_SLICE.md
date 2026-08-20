# WI-1 Round Record - Fake First Executable Vertical Slice

## 1. Round 身份 / 状态（Round Identity / Status）

Document Type:
Walking Implementation Round Record（Walking Implementation 的 Round 实施记录）

Round:
WI-1 - Fake First Executable Vertical Slice

Current Phase:
Walking Implementation

Round Status:
IN PROGRESS

Implementation:
IN PROGRESS

Current Internal Checkpoint:
P4 - COMPLETE / HUMAN APPROVED

P4:
COMPLETE FOR CHECKPOINT / IMPLEMENTED / TESTED / REAL FAKE RUNTIME OBSERVED / HUMAN REVIEWED / HUMAN APPROVED / PASS

Actual Code Evidence:
ESTABLISHED THROUGH P4

Test Evidence:
ESTABLISHED THROUGH P4

Runtime Evidence:
FAKE CLI EXECUTABLE PATH + PUBLISHED BUNDLE ESTABLISHED THROUGH P4

Architecture Deviation:
NONE OBSERVED

本文档不是 Architecture Authority、不是新的 Architecture Specification、不是新的
Contract、不是 code inventory，也不是
Walking Implementation Master Plan 或 Architecture-Code Traceability index 的替代品。

## 2. 已验证的仓库进入事实（Verified Repository Entry Facts）

本 Round Plan 的仓库进入状态如下：

- Branch: `main`
- HEAD: `9e00e75`
- Latest commit message: `docs: align walking handoff maturity wording`
- Working tree before this Round Record creation: clean
- Walking Implementation: `AUTHORIZED`
- Current Round: `WI-1`
- WI-1 status before this Round Record: `NEXT / NOT STARTED`
- Architecture Expansion: `NOT AUTHORIZED`
- Minimal Software Architecture: `REVIEWED / IMPLEMENTATION-READY FOR FIRST SLICE`
- Step 7 Review: `PASS`
- G1 through G15: `PASS`
- S7-R1 through S7-R10: `RESOLVED`
- 当前已跟踪 scaffold 是最小 scaffold，不定义已批准的 Software Architecture。
- `var/executions/` 当前未被 source-control 排除。

当前 Walking Implementation 已跟踪的规划输入为：

- `00_WALKING_IMPLEMENTATION_PLAN.md`
- `01_ARCHITECTURE_CODE_TRACEABILITY.md`

在本 Round Record 建立时，还不存在 WI-1 implementation code、test evidence、runtime evidence，
或 Traceability status upgrade。当前状态已由后续 P1 evidence sync 更新。

## 3. 目标（Goal）

第一次证明：已审查的 First-Slice Minimal Software Architecture 可以形成真实可执行的内部
Vertical Slice（纵向切片）路径。

Primary proof:

```text
software shape can execute
```

即：证明当前已审查的软件形态能够真实运行。

WI-1 不尝试证明：

- 真实 TikTok research quality；
- Scrape Creators behavior；
- TT-17 behavior；
- Car Vacuum 市场结论的经验真实性；
- production readiness。

## 4. 范围（Scope）

Authorized business scope:

```text
US / Car Vacuum / TikTok Content Research First Slice ONLY
```

WI-1 仅限于一条 fake internal executable path：通过 provider-neutral C3 Search seam，
由一个 fake concrete implementation 满足该 seam。

Fake Search 数据：

```text
Fake Search data
    != real TikTok evidence
    != empirical market fact
    != validated business truth
```

WI-1 不得使用 synthetic data 制造真实市场 Findings 或 Hypotheses。

Finding formation:
NOT IMPLEMENTED IN WI-1

Hypothesis formation:
NOT IMPLEMENTED IN WI-1

最小 ResearchResult 可以明确说明：本次 execution 使用的是 synthetic Fake Search data，
因此不建立任何经验性的 TikTok 结论。

这必须继续兼容：

```text
Insufficient Evidence
    != Execution Failure
```

## 5. 架构输入（Architecture Inputs）

WI-1 planning 只读取当前相关输入：

- `docs/00_project/02_CURRENT_HANDOFF.md`
- `docs/03_software/vertical_slices/01_research_execution/walking_implementation/00_WALKING_IMPLEMENTATION_PLAN.md`
- `docs/03_software/vertical_slices/01_research_execution/walking_implementation/01_ARCHITECTURE_CODE_TRACEABILITY.md`
- `docs/03_software/vertical_slices/01_research_execution/00_MINIMAL_SOFTWARE_ARCHITECTURE_PLAN.md`
- `docs/03_software/vertical_slices/01_research_execution/01_SOFTWARE_RESPONSIBILITY_MAPPING.md`
- `docs/03_software/vertical_slices/01_research_execution/02_EXECUTION_SPINE_SOFTWARE_DESIGN.md`
- `docs/03_software/vertical_slices/01_research_execution/06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md`
- `docs/03_software/vertical_slices/01_research_execution/07_MINIMAL_SOFTWARE_ARCHITECTURE_REVIEW.md`

必须保持的 First-Slice representation facts：

- C1 -> `TaskRuntime.execute(...)`
- C2a -> `ResearchSkill` Protocol
- C2a <-> C2b -> `ResearchExecutionPort`
- C3 -> `SearchCapability` Protocol
- C4a -> composition-time static binding
- C4b -> `ScrapeCreatorsAdapter`，位于 WI-1 fake implementation 之外
- Provider Access -> `ScrapeCreatorsAccess` with synchronous stdlib HTTP，位于 WI-1 fake implementation 之外
- Stable model strategy -> stdlib dataclass
- Dependency Injection -> manual constructor injection
- Application -> thin CLI / `argparse`
- Retention -> Local JSON Execution Bundle
- Lifecycle -> `STAGING -> FINALIZED/PUBLISHED`
- Database -> NOT REQUIRED
- Framework -> NOT REQUIRED

Protocol（协议 / 类型边界）：

```text
Protocol
    != runtime hop
```

## 6. 预期调用路径（Expected Call Path）

WI-1 目标是证明以下 semantic / call-path：

```text
Thin CLI
-> BusinessWorkRequest
-> TaskRuntime.execute()                         C1
-> ExecutionContext                             C2b
-> RuntimeResearchExecutionPort
-> Concrete First-Slice ResearchSkill           C2a
-> ResearchExecutionPort.search(...)
-> TaskRuntime-controlled capability invocation C2b
-> dependency typed as SearchCapability         C3
-> Fake SearchCapability
-> minimal SearchResult
-> same ResearchSkill
-> minimal ActualSampleBoundary
-> minimal admitted Evidence
-> minimal ResearchResult
-> ResearchCompletion
-> TaskRuntime recognizes Business Completion
-> C6 finalization
-> Local JSON Execution Bundle
-> required-reference validation
-> atomic publish
-> Record Ref
-> TerminalReturn
-> CLI
```

必须遵守的 coordination rules：

- `ResearchSkill` 不得直接调用 concrete Fake Search implementation。
- `ResearchExecutionPort` 是 C2a <-> C2b seam。
- `TaskRuntime` 拥有 capability invocation coordination。
- Fake Search 只是 provider-neutral C3 seam 后面的 concrete test implementation。
- Protocol 不创建额外的 runtime hop。

## 7. 后续 WI-1 implementation 允许的修改（Allowed Changes for the Later WI-1 Implementation）

在人类批准本 Round Plan 之后，WI-1 implementation 可以只修改本 Round 所需的最小
First-Slice implementation surface，包括：

- `.gitignore`
- `src/ecommerce_ai_os/application/`
- `src/ecommerce_ai_os/runtime/`
- `src/ecommerce_ai_os/research/`
- `src/ecommerce_ai_os/search/`
- `src/ecommerce_ai_os/composition.py`
- `src/ecommerce_ai_os/__init__.py`
- `tests/unit/`
- `tests/integration/`
- `tests/architecture/`
- 当前 WI-1 Round Record，以及 Walking process 要求的 Traceability update

如果以下已跟踪的空 legacy scaffold packages 在 implementation 开始时仍为空，后续
implementation 可以移除或替换它们：

- `src/ecommerce_ai_os/applications/`
- `src/ecommerce_ai_os/capabilities/`
- `src/ecommerce_ai_os/kernel/`
- `src/ecommerce_ai_os/services/`
- `src/ecommerce_ai_os/skills/`

现有 `src/ecommerce_ai_os/providers/` package 不得在 WI-1 中扩展成真实 Provider integration。

旧 scaffold 不是 Architecture Authority。

## 8. 明确禁止 / 不在本轮范围内（Explicitly Forbidden / Not In Scope）

WI-1 excludes:

- Live Scrape Creators
- `ScrapeCreatorsAdapter`
- `ScrapeCreatorsAccess`
- `ScrapeCreatorsHttpClient`
- real TT-17
- live TT-17
- provider raw capture
- real Provider provenance
- dynamic Provider Resolution
- Provider Router
- multi-provider
- fallback
- pagination semantics implementation
- full `SearchInvocationContext`
- full `SearchInvocationProvenance`
- `RawProviderResultRef`
- production Research Method
- real Finding formation
- real Hypothesis formation
- advanced sampling
- `ExecutionAbort`
- full failure lifecycle
- Retry Engine
- Async
- Event Bus
- Database
- Repository Layer
- `SearchService`
- `EvidenceService`
- `ResearchService`
- `RecorderService`
- Knowledge
- Artifact
- Agent
- Analyze Capability
- 97 API integration
- new Contracts
- new Services

本 Round Record 目前不授权 WI-1 implementation。

## 9. 验收标准（Acceptance Criteria）

WI-1 不会仅因为代码能够 import 或 compile 就判定为 PASS。

后续 implementation 完成后，WI-1 至少必须证明：

- thin CLI 真实执行了一次 fake First-Slice run；
- 产生了 TerminalReturn；
- 存在 Execution Outcome；
- 存在最小 ResearchResult / Business Result；
- Record Ref 只在 bundle 成功 publish 后存在；
- Record Ref 可以解析到最终 execution bundle；
- bundle 包含 required retained input / Search / Research / C6 facts；
- `execution_record.json` 作为 terminal C6 record，在 required referents 之后写入；
- required references 在 publish 前可以解析；
- 没有错误记录真实 Provider use；
- 没有伪造 TT-17 / Scrape Creators fact；
- `var/executions/` 被 Git 排除；
- Runtime 拥有 capability invocation coordination；
- Research 不依赖 Runtime / Provider internals；
- Runtime 不依赖 concrete provider 或 concrete skill implementation；
- architecture import-boundary test 通过；
- stdlib unittest tests 真实执行并通过；
- 观察到真实的 fake CLI runtime path；
- Runtime Evidence 可检查；
- Human Learning Review 完成；
- required Delete Test / What-if review 完成；
- 不存在未审查的 Architecture Assumption Conflict。

未来 implementation 在生成 runtime artifacts 前，必须使用实际命令验证 runtime root 已被
source-control 排除，例如：

```bash
git check-ignore -v var/executions/probe.json
```

本 Round Plan 不定义未来的具体 test function names。

## 10. 学习重点（Learning Focus）

WI-1 learning 仅限于：

- Vertical Slice（纵向切片）
- Protocol（协议 / 类型边界）
- Dependency Injection（依赖注入）
- Execution Runtime Owner
- Business Method vs Runtime Coordination
- C1 / C2a / C2b

本 Round Record 不是通用的 DDD、Clean Architecture 或 SOLID tutorial。

### 10.1 WI-1 分步实施 / 学习 Checkpoints

WI-1 仍然是一个正式 Walking Round。以下 P0～P5 不是新的 Architecture Round、不是新的
Contract、不是新的 Vertical Slice、不是新的 Software Architecture Step，也不是新的正式
WI Round。

P0～P5 只是 WI-1 内部的 Implementation / Learning Checkpoints，用于避免 Codex 一次性实现整个
WI-1，并确保每一小段实现后都能形成：

```text
Architecture
-> Code
-> Test / Run
-> Human Learning Review
-> Next Checkpoint
```

核心规则：

```text
Later Checkpoint
must not be implemented
before the current Checkpoint
has been reviewed by Human.
```

即：当前 Checkpoint 未经 Human Review，不得提前实现后续 Checkpoint。

#### P0 - Pre-Code Learning

Current Status:
COMPLETE / HUMAN REVIEWED

Goal:
先建立 WI-1 的整体 mental model，知道当前代码将解决哪些 architecture questions，但不要求
Human 在写代码前已经完全掌握所有答案。

Learning Focus:

- Q1. `BusinessWorkRequest` 为什么不等于 established Execution？
- Q2. `TaskRuntime` 和 `ResearchSkill` 分别拥有什么 authority？
- Q3. 为什么 `ResearchSkill` 不直接调用 concrete Fake Search？
- Q4. `ResearchExecutionPort` 隔离了谁和谁？
- Q5. 为什么 `SearchCapability` Protocol 不是 runtime hop？
- Q6. 为什么 `ResearchCompletion` 之后仍需要 C6 / Bundle / Record Ref / TerminalReturn？

Implementation Boundary:

```text
P0:
DO NOT WRITE CODE
```

P0 完成条件不是闭卷考试。P0 只要求 Human understands what the six questions are，并能在后续
implementation 中把它们作为 observation questions 使用。

#### P1 - Boundary Skeleton

Status:
COMPLETE FOR CHECKPOINT / HUMAN APPROVED

Goal:
只建立第一批最小 software boundaries / stable representations，让 Human 第一次看到 Architecture
如何变成 Python representation。

Learning Focus:

- 为什么有些概念是 dataclass；
- 为什么有些概念是 Protocol；
- 为什么 Protocol 是 dependency seam 而不是 runtime service；
- 为什么 stable boundary 不应直接使用 `dict[str, Any]`。

Implementation Boundary:
P1 只允许关注以下概念：

- `BusinessWorkRequest`
- `SkillDeclaration`
- `ResearchSkill` Protocol
- `ResearchExecutionPort` Protocol
- `SearchCapability` Protocol
- minimal `SearchRequest`
- minimal `SearchResult`

P1 不追求完整运行 WI-1，并明确不实现：

- full `TaskRuntime` execution loop
- Fake Search end-to-end path
- `ResearchCompletion` closure
- C6 finalization
- Local JSON Execution Bundle
- Record Ref
- CLI end-to-end
- live Provider
- TT-17

P1 完成后必须暂停，进行 Code Review、Architecture -> Code Mapping 和 Human Learning Review。
Human Review 后才能进入 P2。

P1 Runtime Evidence:

```text
N/A / NOT REQUIRED AS FULL E2E FOR THIS CHECKPOINT
```

这不将任何 Traceability concept 升级为 `RUNTIME VERIFIED`。

##### P1 Actual Evidence

**P1 Actual Files**

```text
src/ecommerce_ai_os/runtime/execution.py

src/ecommerce_ai_os/research/models.py
src/ecommerce_ai_os/research/ports.py

src/ecommerce_ai_os/search/models.py
src/ecommerce_ai_os/search/port.py

tests/unit/runtime/test_execution.py
tests/unit/research/test_boundaries.py
tests/unit/search/test_boundaries.py
```

相应 package `__init__.py` 也已建立。

**P1 Actual Symbols**

```text
BusinessWorkRequest
SkillDeclaration
ResearchSkill
ResearchExecutionPort
SearchRequest
SearchResult
SearchCapability
```

`BusinessWorkRequest` 的 `business_goal` 缺失曾是 implementation defect；该 correction 已闭合，
不是 Architecture Assumption Conflict。

**P1 Actual Architecture Mapping**

```text
A02 -> BusinessWorkRequest
A06 -> ResearchSkill
A07 -> SkillDeclaration
A08 -> ResearchExecutionPort

B01 -> SearchCapability
B02 -> SearchRequest
B03 -> SearchResult
```

**P1 Tests**

```text
PYTHONPATH=src python -m unittest discover -s tests/unit -v
-> 8 tests PASS

python -m compileall -q src tests
-> PASS / exit code 0

git diff --check
-> PASS / exit code 0
```

最初未设置 `PYTHONPATH=src` 执行 unittest 时，由于当前 `src/` layout package 未安装到
interpreter environment，出现 `ModuleNotFoundError: No module named 'ecommerce_ai_os'`。这是
Test / local execution environment fact，不是 Architecture Deviation、Architecture Assumption
Conflict 或 Business Failure；P1 不因此修改 `pyproject.toml`。

**P1 Human Learning Review**

```text
BusinessWorkRequest
= structured business request, not Execution

dataclass
= stable typed value representation

ResearchSkill
= Business Method seam

ResearchExecutionPort
= Business -> Runtime authority boundary

SearchCapability
= Runtime -> concrete Search dependency boundary

SkillDeclaration
= Declared dependency

Declared
!= Runtime Need
!= Actual Invocation

SearchRequest
= one Search need

SearchResult
= bounded typed Search outcome
!= Evidence
!= list[Video]
```

**P1 Human Delete Test**

```text
Delete ResearchExecutionPort
-> code may still run
-> C2a / C2b authority boundary weakens
-> Research may depend directly on Runtime / Capability

Delete SearchCapability
-> code may still run
-> Runtime becomes coupled to concrete Search implementation

Replace stable dataclasses with dict
-> code may still run
-> typed / stable cross-boundary semantics weaken

Delete SkillDeclaration
-> code may still run
-> declared capability dependency becomes implicit

Can run
!= Architecture boundary preserved
```

#### P2 - Core Execution Loop

Status:
COMPLETE FOR CHECKPOINT / IMPLEMENTED / TESTED / HUMAN REVIEWED / HUMAN APPROVED

Goal:
第一次真正证明 C2a / C2b / C3 fake path 的核心控制关系。

Learning Focus:

```text
TaskRuntime
= Execution / Capability Invocation Coordination Owner

ResearchSkill
= Business Method Owner

ResearchExecutionPort
= C2a <-> C2b seam

SearchCapability
= provider-neutral dependency seam

Fake Search
= concrete test implementation
```

Implementation Boundary:
目标行为只覆盖：

```text
ResearchSkill
-> ResearchExecutionPort.search(...)
-> TaskRuntime-controlled capability invocation
-> minimal SearchInvocationContext
-> SearchCapability seam
-> Fake Search concrete implementation
-> SearchResult
-> same ResearchSkill
```

P2 Entry Sequencing Refinement:

```text
B04 SearchInvocationContext
= minimal implementation allowed / required in P2

Reason:
the reviewed SearchCapability callable already requires
SearchInvocationContext,
therefore the Fake executable path cannot legally invoke C3
without a minimal representation.

WI-3
= SearchInvocationContext full C3 semantics / main verification

Implementation Sequencing Refinement
= APPROVED

Architecture Reopen
= NO

Contract Change
= NO
```

P2 只实现 Fake executable path 所需的最小合法 `SearchInvocationContext`。P2 不提前实现：

- full invocation provenance
- provider raw capture semantics
- full missingness semantics
- full time semantics
- full bounded retrieval context
- real Provider provenance
- TT-17 specific context

必须保持：

```text
ResearchSkill
must NOT directly call
the concrete Fake Search implementation.
```

P2 不提前实现：

- C6 full closure
- Local JSON Bundle full publish lifecycle
- CLI full E2E
- real Provider integration
- TT-17
- Finding / Hypothesis formation

P2 完成后必须暂停并进行 Human Learning Review，重点回看 Q2、Q3、Q4、Q5。

##### P2 Actual Evidence

**P2 Actual Production Files**

```text
src/ecommerce_ai_os/runtime/execution.py
src/ecommerce_ai_os/runtime/task_runtime.py
src/ecommerce_ai_os/search/models.py
```

**P2 Actual Test File**

```text
tests/unit/runtime/test_task_runtime.py
```

**P2 Actual Symbols**

```text
ExecutionContext
SearchInvocationContext
TaskRuntime
TaskRuntime.__init__
TaskRuntime._invoke_search
RuntimeResearchExecutionPort
RuntimeResearchExecutionPort.search

test-only:
FakeSearchCapability
request_search_through
```

**P2 Actual Tested Call Path**

```text
request_search_through
-> RuntimeResearchExecutionPort.search
-> TaskRuntime._invoke_search
-> FakeSearchCapability.search
-> SearchResult
-> original caller
```

**P2 Tests**

```text
PYTHONPATH=src python -m unittest tests.unit.runtime.test_task_runtime -v
-> 2 tests PASS

PYTHONPATH=src python -m unittest discover -s tests/unit -v
-> 10 tests PASS

python -m compileall -q src tests
-> PASS

git diff --check
-> PASS
```

P2 internal coordination path was exercised under unit test. This is not WI-1 executable-path Runtime
Evidence and does not upgrade any Traceability row to `RUNTIME VERIFIED`.

**P2 Human Review Conclusions**

- Runtime owns Search invocation coordination.
- Undeclared Search dependency is blocked before invocation.
- Fake receives the original `SearchRequest`.
- `SearchInvocationContext` carries the current `execution_id`.
- The Fake-generated `SearchResult` returns to the original caller.
- Research does not depend on Runtime.
- Runtime does not depend on a concrete `ResearchSkill`.
- Runtime does not depend on Provider implementation.
- Fake remains test-only.

**P2 Controlled Deferrals**

- `SearchFailure` handling remains deferred.
- Full `SearchInvocationContext` semantics remain in WI-3.
- Production concrete `ResearchSkill` remains deferred.
- Business Completion remains deferred to P3.
- C6 / Bundle / Record Ref remain deferred.
- Multi-Execution scheduling is not designed or implemented.

#### P3 - Business Completion

Status:
COMPLETE FOR CHECKPOINT / IMPLEMENTED / TESTED / HUMAN REVIEWED / HUMAN APPROVED

Goal:
已实现并验证：

```text
Business Completion
!= Execution Completion
```

Learning Focus:

```text
ResearchCompletion
= C2a Business Completion handoff

Runtime State
!= Stable Execution Facts
!= Finalized Execution Record

Business Completion
precedes
Execution Completion
```

**P3 Actual Production Files**

```text
src/ecommerce_ai_os/research/models.py
src/ecommerce_ai_os/research/ports.py
src/ecommerce_ai_os/research/car_vacuum_tiktok.py
src/ecommerce_ai_os/runtime/task_runtime.py
```

**P3 Actual Test Files**

```text
tests/unit/research/test_first_slice_skill.py
tests/unit/runtime/test_task_runtime.py
```

**P3 Actual Business Path**

```text
TaskRuntime._run_research_skill
-> CarVacuumTikTokResearchSkill.run
-> RuntimeResearchExecutionPort.search
-> TaskRuntime._invoke_search
-> FakeSearchCapability.search
-> SearchResult
-> CarVacuumTikTokResearchSkill.run
-> ActualSampleBoundary
-> Evidence
-> ResearchResult
-> ResearchCompletion
-> TaskRuntime._run_research_skill
```

`CarVacuumTikTokResearchSkill` uses only the provider-neutral `ResearchExecutionPort` to express its
Search need. It forms a minimal bounded synthetic result from the existing P2 `SearchResult` facts.
The zero-result path returns a valid `ResearchCompletion` with empty Evidence and an explicit
insufficient-evidence limitation; it does not manufacture an Execution failure.

**P3 Human Review Correction**

Human Review found one blocking implementation defect: Runtime could use
`ExecutionContext.skill_declaration` for capability authorization while running a different actual
bound Research Skill. The correction is now closed:

```text
Bound ResearchSkill declaration guard
= implemented / tested / closed

TaskRuntime._run_research_skill
-> verify skill.declaration == context.skill_declaration
-> only then create RuntimeResearchExecutionPort
-> only then invoke skill.run(...)
```

`TaskRuntimeCoordinationTests.test_mismatched_bound_skill_declaration_is_rejected_before_search`
proves a mismatch raises the local `RuntimeError` before Fake Search invocation
(`fake_search.calls == 0`). This was an Implementation Defect, not an Architecture Conflict,
Contract Change, or Architecture Reopen.

**P3 Executed Test Evidence**

```text
PYTHONPATH=src python -m unittest tests.unit.runtime.test_task_runtime -v
-> 4 tests PASS

PYTHONPATH=src python -m unittest tests.unit.research.test_first_slice_skill -v
-> 2 tests PASS

PYTHONPATH=src python -m unittest discover -s tests/unit -v
-> 14 tests PASS

python -m compileall -q src tests
-> PASS

git diff --check
-> PASS
```

**P3 Evidence Discipline**

```text
Business Completion
= exercised under unit test

Execution Completion
= NOT YET ESTABLISHED

WI-1 executable-path Runtime Evidence
= NOT YET ESTABLISHED

RUNTIME VERIFIED
= 0
```

C6, Local JSON Execution Bundle, required-reference validation, publish, Record Ref, TerminalReturn,
`TaskRuntime.execute()`, composition, and CLI remain deferred. P3 does not mark WI-1 complete.

#### P4 - Composition / CLI / End-to-End

Status:
COMPLETE FOR CHECKPOINT / IMPLEMENTED / TESTED / REAL FAKE RUNTIME OBSERVED / HUMAN REVIEWED / HUMAN APPROVED / PASS

Goal:
第一次从真实应用入口跑通整个 WI-1 Fake vertical slice。

Learning Focus:

- `composition.py`
- manual constructor injection
- thin CLI / `argparse`
- `BusinessWorkRequest` creation
- `TaskRuntime.execute()`
- Fake Search dependency wiring
- `TerminalReturn` presentation

Implementation Boundary:
必须保持：

```text
composition.py
= static wiring / assembly point

composition.py
!= runtime orchestrator

CLI
= thin application adapter

CLI
!= business runtime
```

目标运行路径：

```text
python -m ecommerce_ai_os.application.cli ...
```

必须真正得到：

```text
Execution Outcome
ResearchResult / Business Result
Record Ref
```

并能解析 final execution bundle。

**P4 Actual Production Files**

```text
.gitignore
src/ecommerce_ai_os/application/__init__.py
src/ecommerce_ai_os/application/cli.py
src/ecommerce_ai_os/composition.py
src/ecommerce_ai_os/research/car_vacuum_tiktok.py
src/ecommerce_ai_os/research/models.py
src/ecommerce_ai_os/research/serialization.py
src/ecommerce_ai_os/runtime/execution.py
src/ecommerce_ai_os/runtime/execution_record.py
src/ecommerce_ai_os/runtime/retention.py
src/ecommerce_ai_os/runtime/task_runtime.py
src/ecommerce_ai_os/search/fake.py
src/ecommerce_ai_os/search/serialization.py
```

**P4 Actual Test Files**

```text
tests/integration/__init__.py
tests/integration/test_fake_first_slice.py
tests/unit/runtime/test_retention.py
tests/unit/runtime/test_task_runtime.py
```

**P4 Actual End-to-End Path**

```text
CLI
-> BusinessWorkRequest
-> TaskRuntime.execute
-> ExecutionContext
-> CarVacuumTikTokResearchSkill
-> RuntimeResearchExecutionPort
-> TaskRuntime._invoke_search
-> FakeSearchCapability
-> SearchResult
-> ResearchCompletion
-> StableExecutionFacts
-> FinalizedExecutionRecord
-> required-ref validation
-> atomic publication
-> ExecutionRecordRef
-> TerminalReturn
-> CLI
```

**P4 Executed Test Evidence**

```text
PYTHONPATH=src python -m unittest discover -s tests/unit -v
-> 17 tests / PASS

PYTHONPATH=src python -m unittest discover -s tests/integration -v
-> 1 test / PASS

python -m compileall -q src tests
-> PASS

git diff --check
-> PASS

git check-ignore -v var/executions/test-placeholder
-> .gitignore:43:/var/executions/ var/executions/test-placeholder
```

**P4 Actual Runtime Evidence**

Actual command path:

```text
PYTHONPATH=src python -m ecommerce_ai_os.application.cli ...
```

Observed execution:

```text
execution_id = 08921c4e-ae46-4432-b1c2-1fde59e454ad
Execution Outcome = SUCCEEDED
Business Result = returned to CLI
Record Ref = execution://08921c4e-ae46-4432-b1c2-1fde59e454ad/execution_record.json
Record Ref resolved = YES
required references = 5
required references resolved = 5 / 5
staging execution count after publication = 0
provider_raw = ABSENT
```

Observed local review artifact:

```text
/tmp/ecommerce-ai-os-WI1-P4-runtime.W2v2Fd/executions/
08921c4e-ae46-4432-b1c2-1fde59e454ad/execution_record.json
```

The `/tmp` path is review evidence only and is not a repository artifact or durability guarantee.
No real Provider, Scrape Creators, or TT-17 fact was created or claimed.

```text
Fake CLI executable path
= ESTABLISHED

Published Bundle Runtime Evidence
= ESTABLISHED

P4 Verdict
= PASS

WI-1 Final Verdict
= NOT YET
```

#### P5 - Verification & Learning Review

Status:
NEXT / NOT STARTED

Goal:
P5 不新增业务能力，只完成验证与学习复盘。

P5 review must explicitly inspect these non-blocking P4 follow-ups:

```text
A. Reuse the same TaskRuntime for two sequential execute() calls and verify:
   distinct execution IDs;
   distinct published bundles;
   no execution-scoped state leak.

B. Treat wi1-fake-search-result as deterministic WI-1 Fake identity only.
   Full Search Result identity semantics remain deferred to WI-3.
```

These are P5 verification / learning notes, not P4 blockers and not P5 implementation started early.

Learning Focus:

- Architecture -> Code mapping
- Traceability evidence preparation
- Runtime Evidence inspection
- Delete Test / What-if
- Human Learning Review

Implementation Boundary:
P5 只做：

- unit tests
- integration tests
- architecture import-boundary tests
- real fake CLI run
- bundle inspection
- runtime evidence inspection
- Architecture -> Code mapping
- Traceability evidence preparation
- Delete Test / What-if
- Human Learning Review

必须重点执行 Delete Test / What-if，例如：

- 如果删除 `ResearchSkill` Protocol，让 Runtime 直接 import concrete skill，程序是否还能运行？架构失去了什么？
- 如果 `ResearchSkill` 直接调用 Fake Search，程序是否还能运行？`TaskRuntime` 失去了什么 authority？
- 如果 `SearchCapability` Protocol 被当成一个 runtime Service，实际多出了什么错误 runtime hop？
- 如果 `ResearchCompletion` 后直接返回，跳过 C6 / bundle publish，会破坏什么 referenceability / closure semantics？

P5 最后重新回答 P0 的六个问题。此时 Human 应从“知道这些概念存在”推进到“能根据真实代码、测试和
Runtime Evidence 解释这些边界为什么存在。”

#### Checkpoint 推进规则

```text
P0
-> Human Review
-> P1
-> Code / Test / Review
-> Human Review
-> P2
-> Code / Run / Review
-> Human Review
-> P3
-> Code / Runtime Evidence / Review
-> Human Review
-> P4
-> E2E Run / Review
-> Human Review
-> P5
-> Verification / Learning Review
-> WI-1 Round Review
```

核心约束：

```text
Do not implement later Checkpoints early.
```

即：

- P1 不得顺手实现 P2～P5。
- P2 不得顺手实现 P3～P5。
- P3 不得顺手实现 P4～P5。
- P4 不得顺手把 P5 全部完成。

P0～P5 不是独立 PASS 的 Walking Rounds。它们只是 WI-1 内部的推进节奏。最终仍然只有
WI-1 Round Review 来决定 WI-1 是否满足本 Round Record 的 Acceptance Criteria。

不要为 P0～P5 创建新的 Round Record 文件、新的 Traceability ID、新的 Contract、新的
Architecture status 或新的 commit policy。默认仍然是：

```text
One Walking Round
-> one coherent Round-level implementation/review cycle
```

除非 Human 后续明确调整 Git 策略。

## 11. 可追溯性覆盖范围（Traceability Coverage）

Planned WI-1 coverage:

- A01
- A02
- A03 - TerminalReturn partial only
- A04
- A05 - minimal success-path execution establishment / context
- A06
- A07
- A08
- A10
- B01 - Fake implementation
- B02 - minimal
- B03 - minimal
- C01 - minimal
- C02 - minimal
- C05 - minimal
- D01 - minimal
- D02 - minimal
- D03
- D04 - minimal

WI-1 明确不实现：

- A09
- B04 full C3 semantics（P2 只允许 / 要求 minimal representation）
- B05
- B06
- B07
- B08
- B09
- C03
- C04

P1～P4 Human Review 已建立当前 checkpoint 范围内的实际 code/test evidence。P4 直接建立 A01、
A03（`TerminalReturn` partial）、A04、A05、D01、D02、D03 与 D04 的 bounded runtime evidence；
其余 WI-1 coverage 不因同一条 Fake executable path 曾经过相关 representation 而机械升级。
WI-1 Fake executable-path runtime evidence 已建立，但 WI-1 final verdict 仍为 NOT YET。

## 12. 已知实施前置条件 / 缺口（Known Implementation Preconditions / Gaps）

Closed factual gap:

```text
var/executions/
    = ignored by Git through repository-root rule /var/executions/
```

P4 implementation 已使：

```text
var/executions/
```

被 source-control 排除；`git check-ignore -v var/executions/test-placeholder` 已确认该规则生效。

This is:

```text
Implementation / repository hygiene requirement
```

It is not:

```text
Architecture Assumption Conflict
```

P4 actual runtime evidence 生成在 `/tmp`，repository 中没有 runtime bundle 被 stage。

## 13. Planning 评审门（Planning Review Gate / Historical Entry Gate）

WI-1 Round Plan:
HUMAN REVIEWED / IMPLEMENTATION AUTHORIZED

Implementation:
IN PROGRESS

Python Code:
ESTABLISHED THROUGH P4

Current Internal Checkpoint:
P4 - COMPLETE / HUMAN APPROVED

P4:
COMPLETE FOR CHECKPOINT / IMPLEMENTED / TESTED / REAL FAKE RUNTIME OBSERVED / HUMAN REVIEWED / HUMAN APPROVED / PASS

P5:
NEXT / NOT STARTED

Architecture Reopen:
NO

New Contract:
NO

New Service:
NO

Live TT-17:
FORBIDDEN IN WI-1

Do not mark:

- WI-1 = PASS
- WI-1 = IMPLEMENTED
- WI-1 = FINAL VERDICT ESTABLISHED
