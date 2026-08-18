# Ecommerce AI OS — Minimal Software Architecture Phase Handoff

- **阶段**：Minimal Software Architecture
- **Status**：Phase Handoff / Consolidated Input；**Authority**：No
- **Slice**：US / Car Vacuum / TikTok Content Research
## 0. Purpose / Authority Boundary

本文件交接 First Slice 的边界、责任、Contract seam、Provider facts 与下一阶段问题空间；不决定 package、进程、数据库、事件或框架。

本交接输入把 Minimum Endpoint Selection 收口到 `{TT-17 Search by Keyword}`；仓库没有 TT-17、TT-06/07/16/18 或 `PASS_WITH_LIMITATIONS` 的匹配源，旧文档仍保留旧状态。TT-17 是交接输入而非已定位 authority；这是文档缺口，不在本轮重开架构。

## 1. Current Project Phase

```text
Product Requirements → Product Architecture → System Architecture
→ Software Architecture → Code / Schema / Tests
```

```text
First Slice Boundary / Planning = COMPLETE
Minimal Runtime Path = Candidate / Round 3 Reviewed
Detailed Contracts = COMPLETE / CONSISTENCY REVIEWED / PASS_WITH_REFINEMENTS / re-check PASS
Minimum Endpoint Screening = COMPLETE；Selection = CLOSED / SUFFICIENT FOR CURRENT FIRST SLICE
Minimal Software Architecture = AUTHORIZED NEXT DESIGN PHASE
Walking Implementation = NOT YET AUTHORIZED UNTIL REVIEW PASSES
```

Software baseline 仍为 `Not Yet Designed`。

## 2. Architecture Authority Map

`Product → System → Contracts → Software → Code`；Provider Lab 只提供 facts，无 OS authority。


## 3. Global Architecture vs First Slice

全局候选层级：`Applications / Skills / Stable Core / Capabilities / Foundation Services / Providers`；First Slice 只取最小 Research Execution，不批准完整 OS。

## 4. First Slice Business Boundary

入口：`Product/SKU + TikTok + US + Commerce Content + Research Intent`。

```text
First Slice Business End Boundary = Human-reviewable Research Result
```

同一次 Execution 完成 closure：

```text
Research Result → C2a Business Completion → C2b Execution Terminalization
→ C6 Execution Record → C1 Terminal Return
```

```text
Business End Boundary ≠ Execution Closure
```


## 5. First Slice Required Responsibility Set

Required Responsibility Set：

```text
Application Boundary
Research Skill
Task Runtime
Skill Extension Mechanism
Capability Contract
Search Capability
Evidence Boundary
Execution Record
Static Provider Resolution
Scrape Creators Adapter
Scrape Creators
```

9 Required Contracts 在 §7 单独记录。

```text
Responsibility ≠ Contract ≠ Software Component
```

```text
Skill = Business Method
Capability = System Ability
Provider = Concrete External Provider
Adapter / Connector = Ecommerce AI OS internal translation / quirk absorption boundary
Access Mechanism = API / SDK / MCP / Native Integration
C2b Task Runtime = Execution / Capability Invocation Coordination

Provider ≠ Adapter ≠ Access Mechanism

Scrape Creators = current Concrete Provider
TT-17 = current Provider endpoint / access surface used by the First Slice
```

C2a 负责 method、sampling、Finding、Hypothesis、Result；C2b 负责 execution / invocation / terminalization。Skill 不绕过 C2b 调 C3；Evidence Boundary 必需但未证明独立 Full Evidence Service hop。

## 6. Minimal Runtime Path

```text
Operator → Application → C2b Task Runtime → C2a Research Skill
C2a → Search Need → C2b → C3 → C4a → C4b → Scrape Creators / TT-17
Provider → Raw Result → C4b → C3 Result → C2b → C2a
Sampling → Actual Sample Boundary → C5a Evidence → Finding → Hypothesis
→ C5b Research Result → C2a Completion → C2b Terminalization
→ C6 Record → C1 Return
```


## 7. The 9 Required Contracts

```text
C = docs/02_system/vertical_slices/01_research_execution/contracts/
D1 = C/01_EXECUTION_SPINE.md       D2 = C/02_SEARCH_INVOCATION.md
D3 = C/03_RESEARCH_SEMANTICS.md    D4 = C/04_EXECUTION_RECORD.md
D5 = C/05_PROVIDER_MAPPING.md
```

`C1/C2a/C2b → D1`；`C3/C4a → D2`；`C5a/C5b → D3`；`C6 → D4`；`C4b → D5`。

语义为 C1 request/return/rejection、C2a method、C2b runtime、C3 neutral Search、C4a resolution、C4b mapping、C5a Evidence、C5b Result、C6 Record；不是 Python interface、DB schema 或 SDK。

## 8. Stable Cross-contract Invariants

1. 未建立 Execution 的 C1 rejection 不伪造成 C6 Record；C2a 不直调 C3，C2b 协调调用与返回。
2. C3 provider-neutral；C4a Resolution ≠ Endpoint Selection，static binding ≠ permanent policy。
3. C4b 不增强 Provider limitation；Search Result ≠ Evidence；Missing ≠ `0` / `false` / inferred。
4. Provider / Global OS / Original Source identity 分离；C6 必需 reference 须 post-terminal resolvable。
5. Referenceability ≠ raw duplication / 永久 retention；exact retention / persistence 不由 C4b 设计。
6. Research Result 是 Business End Boundary；C2a/C2b/C6/C1 是 closure。Comments = DEFERRED；不提前引入 Agent、MCP、RAG、Vector DB、Queue、Event、特定 DB。

## 9. TT-17 Endpoint Admission Closure

### 9.1 Admission

```text
Minimum Endpoint Subset = {TT-17 Search by Keyword}
Endpoint Admission Review = PASS_WITH_LIMITATIONS
Minimum Endpoint Selection = CLOSED / SUFFICIENT FOR CURRENT FIRST SLICE
```

TT-06 Detail Enrichment、TT-07 Conditional Transcript、TT-16 Optional Hashtag Discovery、TT-18 Optional Mixed-content / Top Search 均为 `NOT REQUIRED FOR MINIMUM SUBSET`。

### 9.2 Verified

- Keyword query 是 admitted / faithful core；`region=US` request 可接受；
- pagination：req1 cursor→约 30、`has_more=1`；req2 cursor→约 60、`has_more=1`；
- same-page duplicate = 0，cross-page duplicate = 3；`aweme_id` exact string；original source/video reference 可得；
- 第二页有 `desc` 缺失；metrics 是 collection-time snapshots；`create_time` 是 publication time ≠ metric observation time；`has_more=1` = traversal known incomplete；不证明 causal truth。

### 9.3 Bounded Lossy

`region=US` 不保证 exact population；media URL 是 observation-time locator，不是永久 source identity。Creator 大整数优先 exact string，numeric 不得静默 canonicalize。C4b 不删跨页重复；去重由 Research Skill 显式执行。三类 identity 分离；缺失不推断。

### 9.4 Unverified Optional Semantic

`date_posted` 已观察但 mapping 未验证，不保证时间过滤；`sort_by` 已观察但 behavior 未验证，不保证 ordering/ranking；更广泛 duplicate、跨请求排序、region semantics 未验证。

### 9.5 Known Unknown

Provider hard cap 未知；三页 reconnaissance limit 不是 hard cap。exact temporal filtering、guaranteed ordering、full enumeration、exact regional semantics、hard cap、broader duplicate behavior 不阻塞最低 admission，但需要时 reopen。

TT-17 只表示 bounded research execution，不表示完整 population、精确时间、稳定排名或无损枚举；仓库无 TT-17 source file。

## 10. Software Architecture Current Boundary

下一阶段只设计“冻结责任如何落成软件结构”；package、依赖、C2b、Skill、Capability/Provider、Evidence/Knowledge/Artifact、schema/API、deployment、persistence、DB 等均未决定。

`src/ecommerce_ai_os/` 只是 scaffold，不是 Approved Software Architecture。

## 11. Legal Question Space for Minimal Software Architecture

只回答下一阶段软件结构问题，不重定义上游。

## 12. Explicitly Out of Scope / Guardrails

不实现 TT-06/07/16/18；不把 TT-17 升级为全平台、精确区域/时间或 full enumeration；不把 Comments 变成 mandatory Evidence；`Operational Observability / C10 = DEFERRED`，不设计它或 Agent、MCP、RAG、Vector DB、Queue、Event、Microservices、自动 Knowledge update、fallback。

```text
Minimal persistence representation
= legitimate Minimal Software Architecture question

Application transport
= legitimate Minimal Software Architecture question

Dedicated Persistence Service
= NOT YET PROVEN

Specific Database Technology
= NOT YET PROVEN unless real evidence requires it

Production / general-purpose API architecture
= NOT REQUIRED FOR FIRST SLICE
```

Minimal application transport may be selected only if required for the Walking Implementation.

护栏而非 TODO backlog；Walking Implementation 等待 review。

## 13. Live Repository Scaffold Facts

```text
src/ecommerce_ai_os/{__init__.py,applications,capabilities,kernel,providers,services,skills}/
tests/.gitkeep
pyproject.toml / uv.lock
```

各 package 只有初始化文件。`pyproject.toml`：setuptools / `src` layout、`ecommerce-ai-os` `0.1.0`、Python `>=3.12,<3.13`、dependencies 为空。创建前 clean；HEAD：

```text
f7d7c29 docs: localize research contract package for chinese readability
```

创建后预期唯一变化是本文件 untracked。

## 14. What Minimal Software Architecture Must Decide Next (A–R)

**A. Package boundary**：Contract → package/module？　**B. Dependency direction**：六层责任方向？
**C. Runtime boundary**：C2b 调用/返回/terminalization/error？　**D. Execution identity**：三类 identity 如何关联？
**E. Skill boundary**：隔离 C2a method 与 C2b coordination？　**F. Capability boundary**：C3 neutral request/result？
**G. Evidence**：How should the REQUIRED Evidence Boundary be represented without assuming a Full Evidence Service?　**H. Analysis**：How should the already-required analysis activity remain inside Research Skill without prematurely creating an Independent Analyze Capability?
**I. Persistence**：C6 reference/resolvability 最小 contract？　**J. Database**：是否需要 DB、schema 与依据？
**K. Agent**：Preserve current guardrails. Do not introduce Agent as a top-level layer without new evidence + architecture review.　**L. Event / Message**：Preserve current guardrails. Do not introduce Event/Message Architecture as a required First-Slice mechanism without new evidence + architecture review.
**M. Provider routing**：TT-17 routing/adapter/limitation 如何实现？　**N. TT-17 hard cap**：未知时如何表示 incomplete traversal？
**O. Observation fields**：`date_posted`/`sort_by`/`region`/missingness 如何保留？　**P. Identity / references**：`aweme_id`/creator/source/media 如何分离？
**Q. Error / review gate**：rejection/failure/partial/limitation 如何表达？　**R. Test boundary**：哪些 invariant、TT-17 limitation、C6 seam 必须测试？

## 15. Facts / Decisions / Unknowns Matrix

| Item | Status | Source | SA 可决定？ | Reopen |
| --- | --- | --- | --- | --- |
| Package boundary | NYD | software baseline | Yes | 上游改变 |
| Runtime / C2b | 语义定、形式 NYD | runtime path | Yes | C2b 重开 |
| Evidence Boundary | REQUIRED；软件表示 NYD | runtime path | Yes，不能假设 Full Service | 语义或 workload 改变 |
| Full Evidence Service | NOT YET PROVEN | runtime path / Deferred Register | 不得提前提升 | 新证据 + review |
| Analysis Activity | REQUIRED inside Research Skill | Research semantics / Handoff | Yes，限于 Skill 内 | 业务方法改变 |
| Independent Analyze Capability | NOT YET PROVEN | Deferred Register | 不得提前创建 | 新能力获批 |
| Minimal persistence representation | legitimate question | C6 / D4 | Yes，限最小表示 | C6 resolvability 要求 |
| Dedicated Persistence Subsystem | NOT YET PROVEN | Deferred Register | 服从 NYP，不升级为必需 | 新证据 + review |
| Specific Database Technology | NOT YET PROVEN | Deferred Register / software baseline | 仅 real evidence requires it | 真实持久化约束 |
| Agentic implementation strategy | guardrail preserved | Product/System boundary | 不改变顶层责任 | 新证据 + review |
| Agent as top-level layer | not approved | Product/System boundary | 不得引入 | 新证据 + review |
| Execution coordination | REQUIRED in C2b | D1 / runtime path | Yes，软件形式 NYD | C2b 重开 |
| Event / Message Architecture | EXPLICITLY REJECTED FOR CURRENT SLICE | Deferred Register | 不得作为必需机制 | 新证据 + review |
| Provider routing | static seam；形式 NYD | D2 | Yes | fallback 必需 |
| TT-17 hard cap | Unknown | 交接输入；无 source | Preserve unknown | full enumeration |
| date_posted / sort_by / ranking | observed；unverified | 交接输入 | Preserve unknown | exact filter/order |
| region exactness | accepted；population unproven | 交接输入 | Preserve unknown | exact regional semantics |
| Comments | DEFERRED Evidence Source | Deferred Register | No current mandatory source | public evidence不足 |
| Application transport | legitimate question；minimal only if Walking requires it | C1 / software baseline | Yes，受条件限制 | Walking 约束改变 |
| Production / general-purpose API architecture | NOT REQUIRED FOR FIRST SLICE | software boundary | 不作为当前目标 | First Slice boundary 改变 |
| Knowledge / Artifact | no auto update；lifecycle NYD | System / C6 | scope / Yes | lifecycle required |

交接输入不是仓库 authority。

## 16. Source Index

1. `docs/00_project/02_CURRENT_HANDOFF.md`；`docs/00_project/00_PROJECT_BASELINE_V0.1.md`；`docs/00_project/01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md`。
2. `docs/01_product/00_PRODUCT_ARCHITECTURE.md`；`docs/02_system/00_SYSTEM_ARCHITECTURE.md`。
3. `docs/02_system/vertical_slices/01_research_execution/02_RESPONSIBILITY_COVERAGE.md`；`03_MINIMAL_RUNTIME_PATH.md`；`05_DEFERRED_REGISTER.md`；`06_ARCHITECTURE_REVIEW.md`。
4. `docs/02_system/vertical_slices/01_research_execution/contracts/00_CONTRACT_DESIGN_INDEX.md`；`01_EXECUTION_SPINE.md`；`02_SEARCH_INVOCATION.md`；`03_RESEARCH_SEMANTICS.md`；`04_EXECUTION_RECORD.md`；`05_PROVIDER_MAPPING.md`；`06_DETAILED_CONTRACT_CONSISTENCY_REVIEW.md`。
5. `docs/03_software/00_SOFTWARE_ARCHITECTURE.md`；`docs/04_governance/00_ARCHITECTURE_GOVERNANCE.md`；`docs/05_references/provider_lab/03_PROVIDER_LAB_ASSET_HANDOFF.md`。

## 17. New Chat Starter

```text
继续 Ecommerce AI OS。当前阶段：Minimal Software Architecture。
First Slice：US / Car Vacuum / TikTok Content Research；Minimum Endpoint：
{TT-17 Search by Keyword}；PASS_WITH_LIMITATIONS，仅 bounded research execution。
先读 handoff 并说明理解，再设计；不要 walking implementation 或重开上游 semantics。确认责任、runtime、九个 Contract、TT-17 limitations、unknowns、review gate；未定位 source 的 TT-17 facts 标为交接输入。
```
