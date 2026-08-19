# WI-1 Round Record - Fake First Executable Vertical Slice

## 1. Round 身份 / 状态（Round Identity / Status）

Document Type:
Walking Implementation Round Record（Walking Implementation 的 Round 实施记录）

Round:
WI-1 - Fake First Executable Vertical Slice

Current Phase:
Walking Implementation

Round Status:
ROUND PLANNING

Implementation:
NOT STARTED

Actual Code Evidence:
NOT YET ESTABLISHED

Test Evidence:
NOT YET ESTABLISHED

Runtime Evidence:
NOT YET ESTABLISHED

Architecture Deviation:
NONE OBSERVED

本文档不是 Architecture Authority、不是新的 Architecture Specification、不是新的
Contract、不是 implementation evidence、不是 code inventory，也不是
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

目前还不存在 WI-1 implementation code、test evidence、runtime evidence，或
Traceability status upgrade。

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
- B04
- B05
- B06
- B07
- B08
- B09
- C03
- C04

本 planning task 不升级任何 Traceability status。所有 actual code、test 和 runtime evidence
都保持 NOT YET ESTABLISHED，直到 implementation 真实发生并经过 review。

## 12. 已知实施前置条件 / 缺口（Known Implementation Preconditions / Gaps）

Known factual gap:

```text
var/executions/
    = currently NOT ignored by Git
```

在 WI-1 生成 runtime execution bundles 前，implementation 必须使：

```text
var/executions/
```

被 source-control 排除。

This is:

```text
Implementation / repository hygiene requirement
```

It is not:

```text
Architecture Assumption Conflict
```

本 planning task 不得修改 `.gitignore`。

## 13. Planning 评审门（Planning Review Gate）

WI-1 Round Plan:
CANDIDATE / READY FOR HUMAN REVIEW

Implementation:
NOT AUTHORIZED BY THIS ROUND RECORD YET

Python Code:
NOT STARTED

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
- WI-1 = RUNTIME VERIFIED
