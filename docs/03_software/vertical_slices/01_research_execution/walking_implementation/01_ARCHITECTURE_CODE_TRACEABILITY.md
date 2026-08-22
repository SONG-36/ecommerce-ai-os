# 01 Architecture → Code Traceability

> **Living Architecture → Reviewed Software Representation → Actual Code → Test → Runtime Evidence map**
>
> 本文服务于 Ecommerce AI OS First Research Slice 的 Walking Implementation。它是架构文档与真实 Python 实现之间的长期索引和学习导航桥梁，不是新的 Architecture Specification、代码清单、API 文档，也不是 Codex 实施报告归档。

## 0. 文档目的

本文件维护当前已经审查过的架构概念如何逐步落到软件表示、真实代码、测试和运行证据。它回答的是：

```text
这个架构概念为什么存在？
Step 6 最终审查后决定怎样表示？
真实代码在哪里、由哪个 symbol 承担？
哪个测试实际证明了边界？
运行以后在哪里看到它真的发生？
```

它是 **Living Traceability Index**：每个 Walking Implementation Round 完成后，只更新当前索引和指向 Round Record 的证据，不把每轮事实报告复制进来。

## 1. 当前 Walking Implementation 状态

| 项目 | 当前值 |
|---|---|
| Walking Implementation | `AUTHORIZED` |
| Current Round | `WI-2` |
| WI-1 | `COMPLETE / PASS` |
| Current Internal Checkpoint | `WI-2 - COMPLETE / PASS` |
| P5 | `COMPLETE / TESTED / HUMAN REVIEWED / PASS` |
| WI-2 P1 | `COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS` |
| WI-2 P2 | `COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS` |
| WI-2 P3 | `COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS` |
| WI-2 P4 | `COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS` |
| WI-2 P5 | `COMPLETE / VERIFIED / HUMAN REVIEWED / PASS` |
| WI-2 | `COMPLETE / PASS` |
| Core Concepts | `9 TESTED` / `0 IMPLEMENTED` / `7 PLANNED` / `12 RUNTIME VERIFIED` |
| Actual Code Evidence | `VERIFIED THROUGH WI-2 P5 / NO NEW P5 PRODUCTION BEHAVIOR` |
| Test Evidence | `VERIFIED THROUGH WI-2 P5` |
| Runtime Evidence | `WI-1 SUCCESS + WI-2 FOUR-PATH MATRIX + SEQUENTIAL ISOLATION + P5 FAKE CLI` |
| Known Architecture Deviations | `NONE OBSERVED` |
| Current Next | `WI-03 - SEARCH SEMANTICS / NEXT / NOT STARTED` |

P1～P5 已完成。P5 的 AST import guard、sequential multi-Execution isolation、bundle inspection、
Delete Test、真实 Fake CLI rerun 与 consistency gate 均通过，因此 WI-1 final verdict 为 `PASS`。
该 PASS 只证明 reviewed First-Slice minimal software shape 可以执行；它不把 Fake evidence 强化为
real Provider / TT-17、完整 Search/C6 semantics、scale readiness 或完整 Ecommerce AI OS architecture。
WI-2 P1 已建立 Admission、`PreExecutionRejection | TerminalReturn` response distinction 与
Execution Establishment 的 actual code/test/runtime evidence，并已 Human Review `PASS`。
WI-2 P2 已建立 established non-continuable failure、private `_ExecutionAbort` unwind 与
TaskRuntime-owner catch boundary 的 actual code/test evidence，并已 Human Review `PASS`。WI-2 P3
已建立 bounded failure facts、path-sensitive failure C6、published failure Record Ref 与 failed
`TerminalReturn` 的 actual code/test/runtime evidence，并已 Human Review `PASS`。WI-2 P4 已建立
Business Completion 后 closure failure、Business Result preservation 与 no-Record-Ref 的 actual evidence，
并已 Human Review `PASS`。WI-2 P5 在不新增 production behavior 或 test 的前提下重新验证四条 lifecycle、
sequential isolation、import DAG 与 Fake CLI success，并已 Human Review `PASS`。WI-02 Final Verdict 为 `COMPLETE / PASS`；
当前导航为 WI-03 Search Semantics `NEXT / NOT STARTED`。

## 2. 本文职责与非职责

### 本文职责

- 固定 Architecture → Reviewed Software Representation → Actual Code → Test → Runtime Evidence 的长期映射。
- 区分 reviewed/planned information 与 actual evidence。
- 暴露 architecture drift、实现偏离和证据缺口。
- 为人类学习提供从设计 Why 到代码、调用链、测试、运行产物的导航入口。

### 本文非职责

- 不重新设计 `00`～`07` 已审查的架构。
- 不把预计文件、预计 class 或未来测试名称写成已实现事实。
- 不取代 `rounds/WI_xx_....md` 的每轮历史报告。
- 不成为所有 Python symbols 的 inventory 或 API reference。
- 不因代码已经能运行，或测试已经通过，就自动宣布架构正确。

四类信息源的职责如下：

```text
00_WALKING_IMPLEMENTATION_PLAN.md
= 接下来怎么走

01_ARCHITECTURE_CODE_TRACEABILITY.md
= 架构落实到哪里，以及目前有什么证据

rounds/WI_xx_....md
= 某一轮实际做了什么、跑了什么、发现了什么

src/ + tests/ + var/executions/
= 真实实现和真实运行证据
```

## 3. Traceability 核心模型

每个重要概念都沿以下学习和证据链追踪：

```text
Architecture
    → Reviewed Software Representation
        → Actual Code
            → Test
                → Runtime Evidence
```

其中：

1. **Architecture**：说明 Why、Boundary、责任、约束和来源。
2. **Reviewed Software Representation**：Step 6 审查后决定的软件形状，例如 Concrete class、Protocol、dataclass、private control signal、composition fact 或 filesystem lifecycle。
3. **Actual Code**：已经存在的 repo-relative file path 与 exact symbol；只接受可定位事实。
4. **Test**：实际执行并通过的、针对相关边界的测试证据。
5. **Runtime Evidence**：该 Round 所要求的 fake/live runtime 行为、execution record、artifact 或观察事实。

这条链是导航顺序，不是把所有概念强行变成 class。一个概念可以由 method、Protocol、dataclass、private exception/control signal、composition fact、filesystem lifecycle 或 bounded behavior 实现。

## 4. Evidence Discipline

本文件实行以下真实性纪律：

```text
Architecture intention != Implementation fact
Planned code location != Actual code evidence
Planned test != Executed test
Expected runtime path != Observed runtime evidence
PLANNED + Deviation NONE != Architecture conformity verified
Tests pass != Architecture preserved
Can run != Architecture is correct
```

初始状态下，任何未实际建立的字段必须明确写为 `NOT YET IMPLEMENTED`、`NOT YET VERIFIED` 或 `NOT YET ESTABLISHED`，不能用未来计划的文件名、symbol 或测试名冒充事实。

## 5. Traceability Status Model

Traceability status 保持简单，并按证据成熟度递进：

| Status | 含义 |
|---|---|
| `PLANNED` | reviewed representation 已存在，但 implementation evidence 尚未建立。 |
| `IMPLEMENTED` | 真实代码已存在，并且可以命名 exact file + symbol。 |
| `TESTED` | 相关测试已经实际执行并通过。 |
| `RUNTIME VERIFIED` | 该 Round 要求的 fake/live runtime evidence 已展示所需行为。 |

并非所有静态关注点都需要 `RUNTIME VERIFIED`。例如 dependency DAG 可以在 `TESTED` 完成，runtime evidence 标为 `N/A`；是否需要运行验证由该概念和 Round 的验证目标决定。

## 6. Architecture Deviation Model

`Architecture Deviation` 是相对于 reviewed representation 的当前判断，取值固定为：

| Value | 含义 |
|---|---|
| `NONE` | 当前尚未观察到实现与 reviewed representation 的矛盾。 |
| `FOUND` | 已发现实际代码或行为偏离 reviewed representation。 |
| `UNDER REVIEW` | 偏离已记录，正在判断是 implementation defect 还是 architecture assumption conflict。 |
| `APPROVED CHANGE` | 经过明确架构审查，已批准修改 reviewed architecture。 |

本文件的职责是暴露 drift，绝不静默把 reviewed representation 改写成 diverging code 的样子。即使测试通过，也不能消除 architecture deviation；只有显式审查和批准的 architecture change 才能改变架构基线。

## 7. Architecture → Implementation Baseline

下表是当前 28 项基线。`计划代码归属` 只表示 reviewed/planned ownership，不是已实现证据。

### A. Application / Execution Spine — 10 concepts

| ID | 架构概念 | 权威设计来源 | 已审查的软件表示 | 计划代码归属 | 首次实现 Round | 主验证 Round |
|---|---|---|---|---|---|---|
| A01 | **C1 Task Execution Boundary / 任务执行边界** | `02_EXECUTION_SPINE_SOFTWARE_DESIGN.md`；`06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md` Software Representation Mapping / S6-12；`07_MINIMAL_SOFTWARE_ARCHITECTURE_REVIEW.md` G3/G5 | concrete `TaskRuntime.execute(...)` public callable；不是 Service | `runtime/task_runtime.py` → `TaskRuntime.execute` | `WI-1` | `WI-2` |
| A02 | **BusinessWorkRequest / 业务工作请求** | `02` Execution Entry；`06` Type / Owner Mapping | runtime-owned typed C1 input；`WorkRequest != Execution` | `runtime/execution.py` → `BusinessWorkRequest` | `WI-1` | `WI-2` |
| A03 | **C1 response family / C1 返回族** | `02` pre-execution vs failure；`06` S7-R3；`07` R3/G6 | `TaskExecutionResponse = PreExecutionRejection \| TerminalReturn` | `runtime/execution.py` → response types | `WI-1`（`TerminalReturn`）；`WI-2`（完整） | `WI-2` |
| A04 | **C2b Task Runtime / 任务运行时** | `01_SOFTWARE_RESPONSIBILITY_MAPPING.md`；`02`；`06` S6-04/S6-12 | concrete `TaskRuntime`，拥有 Execution lifecycle 与 Capability invocation coordination | `runtime/task_runtime.py` → `TaskRuntime` | `WI-1` | `WI-2` |
| A05 | **ExecutionContext + Execution Establishment / 执行上下文与执行建立** | `02` Execution Establishment Commit Boundary；`06` runtime model | execution-scoped mutable context；建立前后语义明确 | `runtime/execution.py` + `runtime/task_runtime.py` | `WI-1` | `WI-2` |
| A06 | **C2a Research Skill / 研究技能** | `01` C2a responsibility；`02` Business Method Authority；`04`；`06` S6-13 | `ResearchSkill` Protocol + injected concrete First-Slice Skill | `research/ports.py` → `ResearchSkill`；`research/car_vacuum_tiktok.py` → concrete skill | `WI-1` | `WI-6` |
| A07 | **SkillDeclaration / 技能声明** | `01` Skill Extension；`02` dependency declaration；`06` S7-R1；`07` R1 | stable Research-owned `skill_id / skill_version / declared_capabilities` | `research/models.py` → `SkillDeclaration` | `WI-1` | `WI-7` |
| A08 | **C2a ↔ C2b ResearchExecutionPort / 研究执行端口** | `02` Skill/Runtime round-trip；`06` S6-15/S6-33；`07` G5 | `ResearchExecutionPort` Protocol + execution-scoped `RuntimeResearchExecutionPort` | `research/ports.py` + `runtime/task_runtime.py` | `WI-1` | `WI-2` |
| A09 | **ExecutionAbort / 执行中止控制** | `02` non-continuable failure；`06` S7-R5；`07` G6 | C2b-private unwind mechanism，不是 Contract/public error | `runtime/task_runtime.py` → private `ExecutionAbort` or equivalent | `WI-2` | `WI-2` |
| A10 | **ResearchCompletion / 研究完成交接对象** | `02` Business Completion；`04` Result semantics；`06` S7-R2/R7；`07` R2/R7 | in-memory C2a Business Completion handoff | `research/models.py` → `ResearchCompletion` | `WI-1` | `WI-6` |

### B. Search / Provider Spine — 9 concepts

| ID | 架构概念 | 权威设计来源 | 已审查的软件表示 | 计划代码归属 | 首次实现 Round | 主验证 Round |
|---|---|---|---|---|---|---|
| B01 | **C3 Search Capability / 搜索能力** | `03_SEARCH_PROVIDER_SPINE_SOFTWARE_DESIGN.md`；`06` S6-14/S6-32；`07` G7 | `SearchCapability` Protocol；typed seam，不是 SearchService/runtime hop | `search/port.py` → `SearchCapability` | `WI-1` Fake | `WI-3` |
| B02 | **SearchRequest / 搜索请求** | `03` provider-neutral request；`06` Search model strategy | provider-neutral stable request representation | `search/models.py` → `SearchRequest` | `WI-1` minimal | `WI-3` |
| B03 | **SearchResult / SearchFailure / 搜索结果与失败** | `03` Search outcome semantics；`06` S6-38 + S7-R9；`07` G6/G15 | typed C3 outcomes；bounded `SearchResult`，不是 `list[Video]` | `search/models.py` | `WI-1` minimal | `WI-3` |
| B04 | **SearchInvocationContext / 搜索调用上下文** | `03` capability context；`06` S7-R4；`07` R4/G10 | execution-scoped Search-owned narrowed context | `search/models.py` → `SearchInvocationContext` | `WI-1 / P2` minimal | `WI-3` full semantics / main verification |
| B05 | **SearchInvocationProvenance / 搜索调用来源事实** | `03` provider identity/referenceability；`05` C6 actual facts；`06` S7-R6 | provider-neutral actual invocation provenance | `search/models.py` → `SearchInvocationProvenance` | `WI-3` | `WI-5` |
| B06 | **RawProviderResultRef / 原始 Provider 结果引用** | `03` raw referenceability；`05` post-terminal refs；`06` final consistency fix；`07` R4/R6 | Search-owned provider-neutral raw-result reference | `search/models.py` → `RawProviderResultRef` | `WI-3` | `WI-5` |
| B07 | **C4a Static Provider Binding / 静态 Provider 绑定** | `03` C4a；`06` S6-07 + final consistency fix；`07` G7 | composition-time Search → Scrape Creators binding | `composition.py` | `WI-4` | `WI-5` |
| B08 | **C4b Scrape Creators Adapter / 适配器** | `03` C4b；`06` S6-16/S6-35；`07` G7/G15 | concrete `ScrapeCreatorsAdapter` behind C3 | `providers/scrape_creators/adapter.py` | `WI-4` | `WI-5` |
| B09 | **Provider Access / Provider 访问机制** | `03` Adapter != Access；`06` S6-11/S6-16/S6-30 | `ScrapeCreatorsAccess` Protocol + sync `ScrapeCreatorsHttpClient` | `providers/scrape_creators/access.py` + `http.py` | `WI-4` Access seam / `WI-5` HTTP | `WI-5` |

### C. Research / Evidence — 5 concepts

| ID | 架构概念 | 权威设计来源 | 已审查的软件表示 | 计划代码归属 | 首次实现 Round | 主验证 Round |
|---|---|---|---|---|---|---|
| C01 | **ActualSampleBoundary / 实际样本边界** | `04_RESEARCH_EVIDENCE_SOFTWARE_DESIGN.md`；`06` Research models | Research-owned stable execution fact | `research/models.py` → `ActualSampleBoundary` | `WI-1` minimal | `WI-6` |
| C02 | **C5a Evidence / 证据** | `01` C5a；`04` Evidence admission/formalization；`06` S6-39 | `Evidence \| EvidenceInadmissible`；不是 EvidenceService | `research/models.py` | `WI-1` minimal | `WI-6` |
| C03 | **Finding / 研究发现** | `04` Finding semantics；`06` Research responsibility | stable Evidence-backed interpretation；formation belongs to Skill | model in `research/models.py`；formation in `research/car_vacuum_tiktok.py` | `WI-6` | `WI-6` |
| C04 | **Testable Hypothesis / 可检验假设** | `04` Hypothesis semantics；`06` Research responsibility | stable testable proposition；不是 validated truth | model in `research/models.py`；formation in concrete Skill | `WI-6` | `WI-6` |
| C05 | **C5b ResearchResult / 研究结果** | `01` C5b；`04` Research Result；`06` C5b representation | stable business result with refs / answerability / limitations | `research/models.py` → `ResearchResult` | `WI-1` minimal | `WI-6` |

### D. C6 / Retention / Referenceability — 4 concepts

| ID | 架构概念 | 权威设计来源 | 已审查的软件表示 | 计划代码归属 | 首次实现 Round | 主验证 Round |
|---|---|---|---|---|---|---|
| D01 | **C6 Execution Record / 执行记录** | `01` C6；`05_EXECUTION_RECORD_REFERENCEABILITY_SOFTWARE_DESIGN.md`；`06` S6-10/S6-25 | `StableExecutionFacts` + `FinalizedExecutionRecord` + bounded finalization behavior | `runtime/execution_record.py` + `runtime/task_runtime.py` | `WI-1` minimal | `WI-7` |
| D02 | **Record Ref + Post-terminal Resolvability / 记录引用与终止后可解析性** | `05` referenceability/resolvability；`06` retention closure；`07` G9 | runtime-owned stable reference semantics；returned ref resolves only after publish | `runtime/execution_record.py` / `runtime/retention.py` | `WI-1` | `WI-7` |
| D03 | **Local JSON Execution Bundle / 本地 JSON 执行包** | `05` retention requirement；`06` S6-23/S6-24 | one Execution → one local JSON bundle | `runtime/retention.py` | `WI-1` | `WI-7` |
| D04 | **STAGING → FINALIZED/PUBLISHED lifecycle / 执行包发布生命周期** | `05` finalization；`06` S6-28/S6-36；`07` G9 | staging writes → C6 last → ref validation → atomic publish | `runtime/retention.py` | `WI-1` minimal | `WI-7` |

> **重要说明：** 以上是 28 个 traceability concepts，不是 28 个 mandatory classes。概念可以由 method、Protocol、dataclass、private exception/control signal、composition fact、filesystem lifecycle 或 bounded behavior 承担。

## 8. Live Implementation Evidence Map

以下 live map 按 WI-1 P1～P5 与 WI-2 P1～P5 已确认的实际证据更新。WI-1 P4 把由实际 Fake CLI run、published bundle 与
对应 tests 直接证明的八行升级为 `RUNTIME VERIFIED`；P5 再基于 final Fake CLI 与 sequential
multi-Execution evidence 升级 B01、B03。WI-2 P1 又以 actual rejection / establishment runtime evidence
升级 A02，WI-2 P4 以 Business Completion ordering 的直接 evidence 升级 A10，当前共十二行。
WI-2 P5 重新验证现有 maturity，不机械升级任何行。未由当前 checkpoints 直接建立的行继续保持
`PLANNED` 或既有 `TESTED`，不因整条路径曾被执行而机械升级全部 28 行。

| ID | Actual Code | Test Evidence | Runtime Evidence | Current Status | Architecture Deviation |
|---|---|---|---|---|---|
| A01 | `src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime.execute` | `tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_successful_fake_execution_publishes_resolvable_bundle → PASS / P4` | `rounds/WI_01_FAKE_VERTICAL_SLICE.md → P4 Actual Runtime Evidence`；actual CLI entered `TaskRuntime.execute` and returned terminal success | `RUNTIME VERIFIED` | `NONE` |
| A02 | `src/ecommerce_ai_os/runtime/execution.py → BusinessWorkRequest`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime._pre_execution_rejection`（required First-Slice context admission / WI-2 P1） | `tests/unit/runtime/test_execution.py → BusinessWorkRequestTests.test_represents_the_first_slice_business_context → PASS / WI-1 P1`<br>`tests/unit/runtime/test_execution.py → BusinessWorkRequestTests.test_is_a_frozen_stable_value → PASS / WI-1 P1`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_incomplete_request_is_rejected_before_execution_establishment → PASS / WI-2 P1` | `rounds/WI_02_EXECUTION_LIFECYCLE.md → P1 Actual Evidence`；incomplete required First-Slice context returned rejection with no execution root | `RUNTIME VERIFIED` | `NONE` |
| A03 | `src/ecommerce_ai_os/runtime/execution.py → PreExecutionRejection`<br>`src/ecommerce_ai_os/runtime/execution.py → TerminalReturn`（Business Result and Record Ref independently path-sensitive）<br>`src/ecommerce_ai_os/runtime/execution.py → TaskExecutionResponse`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime.execute` | `tests/unit/runtime/test_execution.py → BusinessWorkRequestTests.test_c1_response_family_distinguishes_rejection_from_terminal_return → PASS / WI-2 P1`<br>`tests/unit/runtime/test_execution.py → BusinessWorkRequestTests.test_terminal_return_allows_failure_without_a_business_result → PASS / WI-2 P3`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_incomplete_request_is_rejected_before_execution_establishment → PASS / WI-2 P4 regression`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_successful_fake_execution_publishes_resolvable_bundle → PASS / WI-2 P4 regression`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_established_failure_closes_with_path_sensitive_record → PASS / WI-2 P4 regression`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_business_completion_survives_controlled_closure_failure → PASS / WI-2 P4` | `rounds/WI_02_EXECUTION_LIFECYCLE.md → P4 Actual Runtime / Test Evidence`；P3 returned `FAILED + no Business Result + resolvable Record Ref`, while P4 returned `FAILED + preserved Business Result + no Record Ref`, both within `TerminalReturn` | `RUNTIME VERIFIED` | `NONE` |
| A04 | `src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime.execute`（private-abort catch, P3 failure finalization/publication, TerminalReturn）<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime._invoke_search`（controlled non-result recognition）<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime._abort_execution`（private unwind trigger）<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime._run_research_skill` | `tests/unit/runtime/test_task_runtime.py → TaskRuntimeCoordinationTests.test_non_result_search_outcome_triggers_private_execution_abort → PASS / WI-2 P3`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_established_failure_closes_with_path_sensitive_record → PASS / WI-2 P3`<br>existing coordination/success tests remain PASS | `rounds/WI_02_EXECUTION_LIFECYCLE.md → P3 Actual Runtime Evidence`；TaskRuntime regained control, finalized/published the failed Execution, and returned the existing public response family | `RUNTIME VERIFIED` | `NONE` |
| A05 | `src/ecommerce_ai_os/composition.py → build_fake_first_slice_runtime`（static concrete ResearchSkill injection）<br>`src/ecommerce_ai_os/runtime/execution.py → ExecutionContext`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime.execute`（successful `ExecutionContext` construction is the WI-2 P1 establishment commit）<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime._run_research_skill`（post-establishment declaration consistency invariant） | `tests/unit/runtime/test_task_runtime.py → TaskRuntimeCoordinationTests.test_search_traverses_runtime_and_returns_to_the_business_caller → PASS / WI-1 P2`<br>`tests/unit/runtime/test_task_runtime.py → TaskRuntimeCoordinationTests.test_mismatched_bound_skill_declaration_is_rejected_before_search → PASS / WI-1 P3 defensive invariant`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_successful_fake_execution_publishes_resolvable_bundle → PASS / WI-2 P3 regression`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_incomplete_request_is_rejected_before_execution_establishment → PASS / WI-2 P1`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_established_failure_closes_with_path_sensitive_record → PASS / WI-2 P3` | `rounds/WI_02_EXECUTION_LIFECYCLE.md → P3 Actual Runtime Evidence`；the controlled path retained the established identity/context/input fact through unwind and clean failure closure | `RUNTIME VERIFIED` | `NONE` |
| A06 | `src/ecommerce_ai_os/research/ports.py → ResearchSkill`<br>`src/ecommerce_ai_os/research/car_vacuum_tiktok.py → CarVacuumTikTokResearchSkill` | `tests/unit/research/test_first_slice_skill.py → FirstSliceResearchSkillTests.test_forms_synthetic_business_completion_from_bounded_search → PASS / P3`<br>`tests/unit/research/test_first_slice_skill.py → FirstSliceResearchSkillTests.test_empty_search_is_insufficient_evidence_not_execution_failure → PASS / P3`<br>`tests/unit/runtime/test_task_runtime.py → TaskRuntimeCoordinationTests.test_mismatched_bound_skill_declaration_is_rejected_before_search → PASS / P3` | `NOT YET VERIFIED`；concrete Research business method exercised under unit test only | `TESTED` | `NONE` |
| A07 | `src/ecommerce_ai_os/research/models.py → SkillDeclaration` | `tests/unit/research/test_boundaries.py → ResearchBoundaryTests.test_skill_declaration_preserves_declared_capability_identity → PASS / P1` | `NOT YET VERIFIED` | `TESTED` | `NONE` |
| A08 | `src/ecommerce_ai_os/research/ports.py → ResearchExecutionPort`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → RuntimeResearchExecutionPort`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → RuntimeResearchExecutionPort.search` | `tests/unit/research/test_boundaries.py → ResearchBoundaryTests.test_structural_port_stub_satisfies_the_callable_seam → PASS / P1`<br>`tests/unit/runtime/test_task_runtime.py → TaskRuntimeCoordinationTests.test_search_traverses_runtime_and_returns_to_the_business_caller → PASS / P2`<br>Independent static type-check evidence `NOT YET ESTABLISHED` | `NOT YET VERIFIED`；P2 internal coordination path exercised under unit test only | `TESTED` | `NONE` |
| A09 | `src/ecommerce_ai_os/runtime/task_runtime.py → _ExecutionAbort`（execution id + actual capability + bounded code/reason）<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime._abort_execution`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime.execute`（private catch and semantic-fact transfer） | `tests/unit/runtime/test_task_runtime.py → TaskRuntimeCoordinationTests.test_non_result_search_outcome_triggers_private_execution_abort → PASS / WI-2 P3`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_established_failure_closes_with_path_sensitive_record → PASS / WI-2 P3` | `rounds/WI_02_EXECUTION_LIFECYCLE.md → P3 Actual Runtime Evidence`；the clean failure path completed without leaking `_ExecutionAbort`; the private mechanism remains directly established by focused tests rather than mechanically promoted | `TESTED` | `NONE` |
| A10 | `src/ecommerce_ai_os/research/models.py → ResearchCompletion`<br>`src/ecommerce_ai_os/research/car_vacuum_tiktok.py → CarVacuumTikTokResearchSkill.run`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime._run_research_skill`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime.execute`（Business Result retained before closure） | `tests/unit/research/test_first_slice_skill.py → FirstSliceResearchSkillTests.test_forms_synthetic_business_completion_from_bounded_search → PASS / WI-1 P3`<br>`tests/unit/research/test_first_slice_skill.py → FirstSliceResearchSkillTests.test_empty_search_is_insufficient_evidence_not_execution_failure → PASS / WI-1 P3`<br>`tests/unit/runtime/test_task_runtime.py → TaskRuntimeCoordinationTests.test_runtime_receives_business_completion_without_terminalization → PASS / WI-1 P3`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_business_completion_survives_controlled_closure_failure → PASS / WI-2 P4` | `rounds/WI_02_EXECUTION_LIFECYCLE.md → P4 Actual Runtime / Test Evidence`；observed event order was `business_completion → closure_failure`, and the exact `ResearchCompletion.research_result` survived in the partial `TerminalReturn` | `RUNTIME VERIFIED` | `NONE` |
| B01 | `src/ecommerce_ai_os/search/port.py → SearchCapability`<br>`src/ecommerce_ai_os/search/fake.py → FakeSearchCapability`（WI-1 Fake implementation only） | `tests/unit/search/test_boundaries.py → SearchBoundaryTests.test_structural_search_stub_satisfies_the_callable_seam → PASS / P1`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_sequential_executions_are_isolated_with_deterministic_fake_id → PASS / P5`<br>Runtime structural behavior demonstrated; static type-check evidence `NOT YET ESTABLISHED` | `rounds/WI_01_FAKE_VERTICAL_SLICE.md → P5 Final Fake CLI Runtime Evidence`；the injected Fake implementation was actually invoked through the provider-neutral seam | `RUNTIME VERIFIED`（WI-1 Fake only） | `NONE` |
| B02 | `src/ecommerce_ai_os/search/models.py → SearchRequest` | `tests/unit/search/test_boundaries.py → SearchBoundaryTests.test_request_is_a_frozen_provider_neutral_value → PASS / P1` | `NOT YET VERIFIED` | `TESTED` | `NONE` |
| B03 | `src/ecommerce_ai_os/search/models.py → SearchResult`<br>P1 minimal representation; full C3 semantics deferred to `WI-3` | `tests/unit/search/test_boundaries.py → SearchBoundaryTests.test_result_has_identity_and_returned_set_boundary → PASS / P1`<br>`tests/unit/search/test_boundaries.py → SearchBoundaryTests.test_result_rejects_a_negative_returned_item_count → PASS / P1`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_sequential_executions_are_isolated_with_deterministic_fake_id → PASS / P5` | `rounds/WI_01_FAKE_VERTICAL_SLICE.md → P5 Sequential Multi-Execution Evidence`；the deterministic `wi1-fake-search-result` existed independently inside two execution-scoped bundles without cross-execution collision | `RUNTIME VERIFIED`（WI-1 minimal only；full semantics remain `WI-3`） | `NONE` |
| B04 | `src/ecommerce_ai_os/search/models.py → SearchInvocationContext`（P2 minimal representation only；WI-3 full semantics / main verification） | `tests/unit/runtime/test_task_runtime.py → TaskRuntimeCoordinationTests.test_search_traverses_runtime_and_returns_to_the_business_caller → PASS / P2` | `NOT YET VERIFIED`；P2 internal coordination path exercised under unit test only | `TESTED` | `NONE` |
| B05 | `NOT YET IMPLEMENTED` | `NOT YET VERIFIED` | `NOT YET VERIFIED` | `PLANNED` | `NONE` |
| B06 | `NOT YET IMPLEMENTED` | `NOT YET VERIFIED` | `NOT YET VERIFIED` | `PLANNED` | `NONE` |
| B07 | `NOT YET IMPLEMENTED` | `NOT YET VERIFIED` | `NOT YET VERIFIED` | `PLANNED` | `NONE` |
| B08 | `NOT YET IMPLEMENTED` | `NOT YET VERIFIED` | `NOT YET VERIFIED` | `PLANNED` | `NONE` |
| B09 | `NOT YET IMPLEMENTED` | `NOT YET VERIFIED` | `NOT YET VERIFIED` | `PLANNED` | `NONE` |
| C01 | `src/ecommerce_ai_os/research/models.py → ActualSampleBoundary`<br>`src/ecommerce_ai_os/research/car_vacuum_tiktok.py → CarVacuumTikTokResearchSkill.run`（P3 minimal bounded Fake representation） | `tests/unit/research/test_first_slice_skill.py → FirstSliceResearchSkillTests.test_forms_synthetic_business_completion_from_bounded_search → PASS / P3`<br>`tests/unit/research/test_first_slice_skill.py → FirstSliceResearchSkillTests.test_empty_search_is_insufficient_evidence_not_execution_failure → PASS / P3` | `NOT YET VERIFIED`；P3 representation exercised under unit test only | `TESTED` | `NONE` |
| C02 | `src/ecommerce_ai_os/research/models.py → Evidence`<br>`src/ecommerce_ai_os/research/car_vacuum_tiktok.py → CarVacuumTikTokResearchSkill.run`（P3 minimal synthetic Evidence only；`EvidenceInadmissible` deferred） | `tests/unit/research/test_first_slice_skill.py → FirstSliceResearchSkillTests.test_forms_synthetic_business_completion_from_bounded_search → PASS / P3`<br>`tests/unit/research/test_first_slice_skill.py → FirstSliceResearchSkillTests.test_empty_search_is_insufficient_evidence_not_execution_failure → PASS / P3` | `NOT YET VERIFIED`；P3 representation exercised under unit test only | `TESTED` | `NONE` |
| C03 | `NOT YET IMPLEMENTED` | `NOT YET VERIFIED` | `NOT YET VERIFIED` | `PLANNED` | `NONE` |
| C04 | `NOT YET IMPLEMENTED` | `NOT YET VERIFIED` | `NOT YET VERIFIED` | `PLANNED` | `NONE` |
| C05 | `src/ecommerce_ai_os/research/models.py → ResearchResult`<br>`src/ecommerce_ai_os/research/car_vacuum_tiktok.py → CarVacuumTikTokResearchSkill.run`（P3 minimal synthetic result with explicit limitations） | `tests/unit/research/test_first_slice_skill.py → FirstSliceResearchSkillTests.test_forms_synthetic_business_completion_from_bounded_search → PASS / P3`<br>`tests/unit/research/test_first_slice_skill.py → FirstSliceResearchSkillTests.test_empty_search_is_insufficient_evidence_not_execution_failure → PASS / P3`<br>`tests/unit/runtime/test_task_runtime.py → TaskRuntimeCoordinationTests.test_runtime_receives_business_completion_without_terminalization → PASS / P3` | `NOT YET VERIFIED`；Business Result exercised under unit test only | `TESTED` | `NONE` |
| D01 | `src/ecommerce_ai_os/runtime/execution_record.py → StableExecutionFacts`<br>`src/ecommerce_ai_os/runtime/execution_record.py → StableExecutionFacts.finalize_success`<br>`src/ecommerce_ai_os/runtime/execution_record.py → StableExecutionFacts.record_execution_failure`<br>`src/ecommerce_ai_os/runtime/execution_record.py → StableExecutionFacts.finalize_failure`<br>`src/ecommerce_ai_os/runtime/execution_record.py → FinalizedExecutionRecord`<br>`src/ecommerce_ai_os/runtime/execution_record.py → serialize_finalized_execution_record`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime.execute` | `tests/unit/runtime/test_retention.py → LocalJsonRetentionTests.test_terminal_c6_record_resolves_every_required_reference → PASS / WI-1 P4`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_successful_fake_execution_publishes_resolvable_bundle → PASS / WI-2 P3 regression`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_established_failure_closes_with_path_sensitive_record → PASS / WI-2 P3` | `rounds/WI_02_EXECUTION_LIFECYCLE.md → P3 Actual Runtime Evidence`；published failure C6 recorded actual input/skill/Search participation, bounded failure facts, `FAILED`, and omitted non-established success-only facts | `RUNTIME VERIFIED` | `NONE` |
| D02 | `src/ecommerce_ai_os/runtime/execution.py → TerminalReturn.record_ref`（optional only when clean closure fails）<br>`src/ecommerce_ai_os/runtime/execution_record.py → ExecutionRecordRef`<br>`src/ecommerce_ai_os/runtime/retention.py → StagingExecutionBundle.publish`<br>`src/ecommerce_ai_os/runtime/retention.py → LocalJsonRetention.resolve_record_ref` | `tests/unit/runtime/test_retention.py → LocalJsonRetentionTests.test_record_ref_is_available_only_after_successful_publish → PASS / WI-1 P4`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_successful_fake_execution_publishes_resolvable_bundle → PASS / WI-2 P4 regression`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_established_failure_closes_with_path_sensitive_record → PASS / WI-2 P4 regression`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_business_completion_survives_controlled_closure_failure → PASS / WI-2 P4` | `rounds/WI_02_EXECUTION_LIFECYCLE.md → P4 Actual Runtime / Test Evidence`；controlled publication failure returned `record_ref=None`; no final bundle existed and even a hypothetical Record Ref did not resolve | `RUNTIME VERIFIED` | `NONE` |
| D03 | `src/ecommerce_ai_os/runtime/retention.py → LocalJsonRetention`<br>`src/ecommerce_ai_os/runtime/retention.py → StagingExecutionBundle` | `tests/unit/runtime/test_retention.py → LocalJsonRetentionTests.test_terminal_c6_record_resolves_every_required_reference → PASS / P4`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_successful_fake_execution_publishes_resolvable_bundle → PASS / P4` | `rounds/WI_01_FAKE_VERTICAL_SLICE.md → P4 Actual Runtime Evidence`；one final local JSON bundle contained input, Search result, sample boundary, evidence, Research Result, and C6 | `RUNTIME VERIFIED` | `NONE` |
| D04 | `src/ecommerce_ai_os/runtime/retention.py → StagingExecutionBundle.write_json`<br>`src/ecommerce_ai_os/runtime/retention.py → StagingExecutionBundle.publish`<br>`src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime.execute`（bounded closure-failure recognition） | `tests/unit/runtime/test_retention.py → LocalJsonRetentionTests.test_missing_required_reference_rejects_publish → PASS / WI-1 P4`<br>`tests/unit/runtime/test_retention.py → LocalJsonRetentionTests.test_record_ref_is_available_only_after_successful_publish → PASS / WI-1 P4`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_successful_fake_execution_publishes_resolvable_bundle → PASS / WI-2 P4 regression`<br>`tests/integration/test_fake_first_slice.py → FakeFirstSliceIntegrationTests.test_business_completion_survives_controlled_closure_failure → PASS / WI-2 P4` | `rounds/WI_02_EXECUTION_LIFECYCLE.md → P4 Actual Runtime / Test Evidence`；publish was attempted exactly once, did not complete, final bundle stayed absent, and staging remained present as an observed fact without a new cleanup policy | `RUNTIME VERIFIED` | `NONE` |

### 8.1 WI-2 P5 Verification Overlay

P5 adds no production behavior and no verification-only test. It re-executed the existing evidence as one coherent lifecycle matrix:

| ID | P5 actual verification | Final status |
|---|---|---|
| A03 | four response/result/reference combinations remained distinct inside `PreExecutionRejection | TerminalReturn` | `RUNTIME VERIFIED` |
| A04 | success, established failure, and closure-failure paths remained owned and terminalized by `TaskRuntime` | `RUNTIME VERIFIED` |
| A05 | rejection created no Execution; all other paths retained established execution identity | `RUNTIME VERIFIED` |
| A09 | focused private-abort unit/integration evidence passed; no independent maturity upgrade was claimed | `TESTED` |
| A10 | P4 `business_completion → closure_failure` ordering test passed again | `RUNTIME VERIFIED` |
| D01 | success and failure C6 records remained path-sensitive; failure fabricated no success-only facts | `RUNTIME VERIFIED` |
| D02 | success/failure refs resolved; closure-failure ref remained absent and hypothetical ref unresolved | `RUNTIME VERIFIED` |
| D03 | P5 Fake CLI published one final local bundle with five resolvable required references | `RUNTIME VERIFIED` |
| D04 | publish-before-reference, success staging removal, and no-final-bundle closure failure all passed | `RUNTIME VERIFIED` |

The P5 import guard, sequential isolation test, full unit/integration regression, and `/tmp` Fake CLI evidence are recorded in `rounds/WI_02_EXECUTION_LIFECYCLE.md → P5 Actual Evidence`. Status counts remain unchanged.

P3 Human Review identified one blocking implementation defect: Runtime did not prove that the actual
bound `ResearchSkill.declaration` matched `ExecutionContext.skill_declaration` before capability
authorization. `TaskRuntime._run_research_skill` now enforces that invariant before port creation or
Skill execution, and
`TaskRuntimeCoordinationTests.test_mismatched_bound_skill_declaration_is_rejected_before_search`
proves the mismatch is rejected before Fake Search invocation. The correction is implemented, tested,
Human approved, and closed; it did not reopen Architecture or Contracts.

未升级行的 `PLANNED + Architecture Deviation = NONE` 只表示目前尚未观察到 implementation
contradiction；它不表示 architecture conformity 已经验证。P1～P5 的已升级行也只建立对应
checkpoints 的 bounded code/test/runtime conformity，不代表 WI-1 或整体 Architecture 已完全验证。

## 9. Cross-cutting Traceability

这些是横切约束，不计入 28 个 core concepts，但会影响多个概念的实现和验证。

| 横切关注点 | 权威设计来源 | 已审查的软件表示 / 约束 | 首次实现 Round | 最终验证 Round |
|---|---|---|---|---|
| Package / Dependency DAG | `06`；`07` G10 | explicit acyclic imports；concrete assembly 只在 composition | `WI-1` | `WI-8` |
| Manual Dependency Injection | `06` S6-18/S6-19 | constructor injection；no DI framework | `WI-1` | `WI-1` / `WI-8` |
| Synchronous Execution | `06` S6-20 | sync end-to-end | `WI-1` | `WI-5` |
| Thin CLI | `06` S6-21 | stdlib `argparse` application adapter | `WI-1` | `WI-8` |
| Dataclass Model Strategy | `06` S6-17 | stdlib dataclass；stable values frozen + slots | `WI-1` | `WI-8` |
| AppConfig / Secret Narrowing | `06` S6-22/S6-43 | immutable config at composition；API key only provider access | `WI-5` | `WI-5` |
| Owner-local component versions | `05`；`06` S7-R10 | skill/capability/adapter version refs | `WI-1` partial | `WI-7` |
| Owner-local `schema_version` | `06` S6-47 | retained JSON owner-local schema version | `WI-1` | `WI-7` |
| Time Semantics | `03`,`04`；`06` S6-41 | Publication / Observation / Collection distinct | `WI-3` | `WI-6` |
| Missingness Semantics | `03`,`04`；`06` S6-42 | known missingness explicit；missing != zero | `WI-3` | `WI-6` |
| Opaque Provider IDs | `03`；`06` S6-26 | exact provider strings；no fake global ID | `WI-4` | `WI-5` |
| TT-17 Bounded Semantics | `03`,`06`,`07` G15 + provider facts | no strengthening of global completeness / exact region / sort / date semantics | `WI-3` partial | `WI-5` / `WI-8` |
| Runtime Bundle Secret Safety | `06` S7-R8 | runtime raw artifacts source-control excluded and credential-safe | `WI-1` local bundle | `WI-5` |

P4 已为以下既有横切关注点建立 bounded actual evidence：

| 既有横切关注点 | P4 Actual Evidence |
|---|---|
| Package / Dependency DAG | `tests/unit/architecture/test_import_directions.py → ImportDirectionTests.test_reviewed_import_dag_holds_for_the_current_source_tree → PASS / P5`；stdlib AST 实际解析当前 `src` tree，composition 保持 concrete assembly owner。 |
| Manual Dependency Injection | `src/ecommerce_ai_os/composition.py → build_fake_first_slice_runtime` 以 constructor injection 组装 Fake Search、Research Skill、Retention 与 Task Runtime；无 DI framework。 |
| Synchronous Execution | actual CLI 在单一同步调用中完成 `TaskRuntime.execute`、publish 与 `TerminalReturn`。 |
| Thin CLI | `src/ecommerce_ai_os/application/cli.py → main` 仅解析输入、调用 composed runtime 并呈现 terminal result。 |
| Dataclass Model Strategy | P4 的 `TerminalReturn`、`ExecutionRecordRef` 与 `FinalizedExecutionRecord` 使用 reviewed dataclass representation。 |
| Owner-local `schema_version` | runtime、research 与 search owner-local serializers 写入 schema version `1`。 |
| Runtime Bundle Secret Safety | `.gitignore` 排除 `/var/executions/`；actual Fake bundle 不含 `provider_raw`、real Provider、Scrape Creators 或 TT-17 facts。 |

这些证据不建立 `AppConfig / Secret Narrowing`、live Provider、完整 owner-local component version 或
TT-17 runtime semantics；相应 final verification Round 保持不变。

P5 additionally verified the existing cross-cutting constraints without creating new concepts:

- Manual DI / Composition：same composed `TaskRuntime` executed two isolated sequential Executions。
- Synchronous Execution：two calls completed sequentially; no async, queue, scheduler, or concurrency mechanism。
- Thin CLI：actual CLI rerun returned `SUCCEEDED`, Research Result summary, and resolvable Record Ref。
- Runtime Bundle Secret Safety：temporary bundle had no `provider_raw`, secret-like value, Scrape Creators claim, or TT-17 claim。
- Architecture Import Guard：all reviewed forbidden directions were absent in the current source tree。

## 10. Round → Traceability Coverage Map

| Round | 主要覆盖范围 |
|---|---|
| `WI-1` | A01,A02,A03 `TerminalReturn` partial,A04,A05,A06,A07,A08,A10；B01 Fake；B02/B03 minimal；B04 minimal in P2；C01/C02/C05 minimal；D01-D04 minimal |
| `WI-2` | A03 full response family；A05 Execution Establishment；A09 ExecutionAbort；D01 failure record；D02 failure referenceability |
| `WI-3` | B02-B06 full C3 semantics；time / missingness / bounded retrieval |
| `WI-4` | B07 C4a；B08 C4b；B09 Access seam；Provider ID / mapping / fixture translation |
| `WI-5` | B09 `HttpClient`；B05/B06 live provenance；AppConfig / secrets；real TT-17 |
| `WI-6` | A06 concrete Research Method；A10 complete ResearchCompletion；C01-C05 |
| `WI-7` | A07 version refs；D01-D04 complete；RecordRef；resolvability；reproducibility |
| `WI-8` | global import DAG；E2E；architecture consistency；final runtime verification |

Round coverage is not proof by itself. Each covered row must still be updated with exact actual code, executed test, runtime observation and deviation classification as applicable.

## 11. Architecture Source Locator Rule

`权威设计来源` 必须指向已有 reviewed architecture documents、section、Contract ID、S6/S7 rule 或 `07` review finding。Source locator 用来回答 **Why / Boundary / Constraint**，不能被实现文件反向替代。

当一个概念有多个来源时，保留决定其边界的主要来源和用于一致性审查的 supporting source。若来源之间发生矛盾，遵循第 18 节，不静默选择更符合当前代码的一份。

## 12. Planned vs Actual Code Rule / Code Symbol Locator Rule

### Planned code

`计划代码归属` 是 reviewed software representation 的预计 ownership。它可以在代码尚未存在时出现，但必须保持计划性质。

### Actual code

当实现真正存在后，`Actual Code` 必须使用：

```text
repo-relative/file/path.py → ExactSymbol
```

例如：

```text
src/ecommerce_ai_os/runtime/task_runtime.py → TaskRuntime.execute
```

仅写模块名、目录名、预计 class 名、commit message 或“已实现”都不构成 code evidence。若一个概念由 filesystem lifecycle、composition fact 或 bounded behavior 实现，应定位到相应的 exact function、composition symbol、artifact path 或行为记录。

## 13. Test Evidence Rule

`Test Evidence` 只有在相关测试实际执行并返回 PASS 后才能更新。它必须包含：

```text
test file + exact test function + executed PASS result + WI Round
```

初始文档不得发明未来 test function 名称；预计测试主题只能保留在 Round 计划或设计来源中。测试应证明对应边界、failure semantics、ownership、serialization 或 lifecycle，而不是仅证明 import 能成功。

## 14. Runtime Evidence Rule

`Runtime Evidence` 必须指向：

- 对应的 Round Record；
- 必要时的实际 `execution_id`；
- local artifact path，例如 `var/executions/<execution_id>/execution_record.json`；
- 一句简短的 observed fact。

不要把 raw JSON 粘贴进本文。本文只保留长期可导航的事实和链接/定位；原始输出由 Round Record、execution bundle 或其他真实 artifact 保存。

Expected runtime path 不能代替 observed runtime evidence。Fake runtime evidence 可以证明本 Round 约定的行为，但不得未经说明地升级为 live provider fact。

## 15. Round Update Procedure

每一轮按以下顺序更新：

1. 先建立该 Round 的 `Round Record`，记录实际 scope、commands、tests、outputs、failures 和 observations。
2. 把 Codex Implementation Evidence Report 作为该轮的 per-round factual raw material；它不是 `01` 的替代品。
3. 只有确认 file、symbol、executed PASS 和 runtime observation 后，才把对应 `Live Implementation Evidence Map` 行从 `PLANNED` 推进为 `IMPLEMENTED`、`TESTED` 或 `RUNTIME VERIFIED`。
4. 对照 reviewed representation 检查 drift；若有偏离，先标记 `FOUND` 或 `UNDER REVIEW`，保留架构事实和实现事实两边的记录。
5. 更新 `Round → Traceability Coverage Map` 的实际 coverage，但不把覆盖范围当作完成证明。
6. 若完成了真正的架构审查并批准变更，才将 deviation 更新为 `APPROVED CHANGE`，并回链变更记录。

职责分工保持固定：

```text
Codex Implementation Evidence Report
= per-round factual raw material

Round Record
= per-round historical record

01 Traceability
= long-lived current index
```

## 16. Human Learning Usage Guide

学习任意一个概念时，按下面顺序走，不要只从代码猜架构：

1. 在 `01` 找到概念 ID。
2. 打开 Architecture Source，理解 Why、Boundary 和约束。
3. 阅读 `Reviewed Software Representation`，确认 Step 6 最终决定的软件形状。
4. 打开 `Actual Code` 及 exact symbol；若仍是 `NOT YET IMPLEMENTED`，停在计划层，不把计划当事实。
5. 沿 collaborators 和 call path 追踪责任如何流动。
6. 阅读 `Test Evidence`，确认边界是否被实际测试覆盖。
7. 检查 `Runtime Evidence`，观察真实行为、execution record 和 artifact。
8. 做一次 Delete Test / What-if，思考删除或移动该边界后会发生什么。

这份顺序的目的，是把“我看懂了一段 Python”推进为“我能解释架构意图、软件表示、运行责任和证据闭环”。

## 17. Delete Test / What-if Guide

Delete Test 的核心原则是：

```text
Can run != Good boundary
```

可以针对每个概念提出“删除、替换或越界调用”问题。例如：

### What-if 1：删除 `ResearchSkill` Protocol

直接让 runtime import concrete skill 可能仍然能运行，但会把 C2b 与具体业务方法耦合，失去 C2a ↔ C2b 的 reviewed port boundary。

### What-if 2：Research Skill 直接实例化 `ScrapeCreatorsAdapter`

调用可能仍然成功，但 provider-specific infrastructure 会泄漏进 business method，破坏 Research ownership、composition-time binding 和 C3/C4a/C4b 分层。

### What-if 3：把 `SearchResult` 改成 `list[Video]`

短期代码可能更短，但会丢失 bounded retrieval、provenance、missingness 和 failure semantics，使 C3 outcome 边界无法表达。

### What-if 4：在 STAGING 文件写完就返回 Record Ref

单次运行可能看似成功，但终止后 ref 可能无法解析，破坏 D02 的 post-terminal resolvability 和 D04 的 atomic publish 语义。

每个 What-if 都应追问：谁获得了不该获得的知识？哪个 Contract ID 或 ownership boundary 被削弱？哪些测试和运行证据会失效？

## 18. Architecture Contradiction Handling

当 reviewed representation 与 actual code diverge 时，遵循以下流程：

```text
Evidence
  → classify: implementation defect vs architecture assumption conflict
    → explicit review
      → approved architecture change only if needed
```

具体规则：

1. 保留 reviewed representation 原文意义和 actual code 的事实，不能用代码覆盖架构基线。
2. 将 `Architecture Deviation` 标为 `FOUND` 或 `UNDER REVIEW`，并在 Round Record 记录证据。
3. 判断是实现没有遵守已审查边界，还是原架构假设与新事实发生冲突。
4. 若是 implementation defect，修代码或测试，不改写架构。
5. 若确实需要改变架构，进行显式 review；只有批准后才使用 `APPROVED CHANGE`，同时保留变更前后的可追溯性。
6. `Tests pass` 不会自动消除 deviation；测试通过只说明被测行为通过，不说明 architecture preserved。

## 19. Learning Card Extraction Rule

从本文件或 Round Record 提取学习卡片时，每张卡只围绕一个概念，并使用以下固定字段：

```text
Concept
Why
Architecture
Code
Test
Runtime Evidence
Counterexample
Consequence
```

不要预先生成大量 cards。只有当该概念已经有足够的 architecture、code、test 或 runtime evidence 时，才提取可复用的 card；没有证据的字段保持未建立，而不是用推测补齐。

## 20. Current Coverage State

截至 `WI-1` P5 final closure 与 `WI-2` P1～P5 actual evidence，coverage 为：

| 维度 | 当前状态 |
|---|---|
| Architecture baseline | `28 core concepts` |
| Current Status Count | `9 TESTED` / `0 IMPLEMENTED` / `7 PLANNED` / `12 RUNTIME VERIFIED` |
| TESTED | `A06`, `A07`, `A08`, `A09`, `B02`, `B04`, `C01`, `C02`, `C05`（`9` 项） |
| IMPLEMENTED | `NONE` |
| PLANNED | `B05`-`B09`, `C03`, `C04`（`7` 项） |
| RUNTIME VERIFIED | `A01`, `A02`, `A03`, `A04`, `A05`, `A10`, `B01`, `B03`, `D01`, `D02`, `D03`, `D04`（`12` 项） |
| Reviewed Software Representation | 已冻结为本文第 7 节内容 |
| Actual Code | `VERIFIED THROUGH WI-2 P5 / NO NEW P5 PRODUCTION BEHAVIOR` |
| Test Evidence | `VERIFIED THROUGH WI-2 P5` |
| Runtime Evidence | `WI-1 SUCCESS + WI-2 FOUR-PATH MATRIX + SEQUENTIAL ISOLATION + P5 FAKE CLI` |
| Architecture Deviation | `NONE OBSERVED` |
| Architecture conformity | `WI-1 MINIMAL SHAPE + WI-2 P1-P5 VERIFIED / WI-02 COMPLETE / PASS` |

WI-2 P4 的 actual evidence 补强 A03、A10、D02 与 D04；A10 因直接观察到
`business_completion → closure_failure` 与 Business Result preservation 而升级为 `RUNTIME VERIFIED`。
其余行不因 P5 重新执行整条路径而机械升级。尤其 A09 的 private control mechanism 仍保持 `TESTED`，B03 的 deterministic Fake identity
不是 final SearchResult identity proof，B04/B05/B06 与完整 C3 semantics 仍由 WI-3 验证；Research
与 C6 的 full semantics 仍分别保留给 WI-6 / WI-7。

## 21. Current Next

```text
WI-2 - Execution Lifecycle
P1 COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS
P2 COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS
P3 COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS
P4 COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS
P5 COMPLETE / VERIFIED / HUMAN REVIEWED / PASS
P5 FINAL VERDICT PASS
WI-02 COMPLETE / PASS
CURRENT NEXT WI-03 SEARCH SEMANTICS / NEXT / NOT STARTED
```

WI-1 P0～P5 已完成，WI-1 final verdict 为 `PASS`。WI-2 P1 admission、rejection response 与
Execution establishment 的 bounded actual evidence 已通过 Human Review。Focused audit 确认 actual
ResearchSkill 在 composition time 已静态绑定，后续 declaration equality check 只是 defensive invariant；
classification 为 `NO ISSUE`。WI-2 P3 与 P4 已通过 Human Review。WI-2 P5 已重新验证
four-path lifecycle matrix、path-sensitive C6 / referenceability、sequential isolation、import DAG 与 Fake CLI success，
并已 Human Review `PASS`。无 production behavior 或 verification-only test 新增；WI-02 Final Verdict 为
`COMPLETE / PASS`，当前导航为 WI-03 Search Semantics `NEXT / NOT STARTED`。
