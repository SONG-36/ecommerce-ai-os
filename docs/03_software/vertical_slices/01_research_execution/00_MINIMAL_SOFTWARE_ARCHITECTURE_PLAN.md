# Ecommerce AI OS — Minimal Software Architecture Plan V0.1

- **文档类型**：Minimal Software Architecture Planning Initialization
- **Vertical Slice**：US / Car Vacuum / TikTok Content Research
- **当前阶段**：Minimal Software Architecture
- **状态**：Step 1 = CANDIDATE COMPLETE；Step 2 = NEXT；Steps 3–7 = PLANNED
- **Architecture Authority**：No
- **Walking Implementation**：NOT YET AUTHORIZED

## 0. Purpose and Boundary

本文件只初始化当前 Minimal Software Architecture 的内部工作计划。它不是新的 System Architecture Round 体系，也不是新的 Product Architecture、Contract、Endpoint Selection 或实现计划。

这不是从 0 设计。后续工作必须继承已确认的 Phase Handoff、System Architecture、Minimal Runtime Path、D1–D5、Deferred Guardrails 与 TT-17 closure。

```text
Responsibility ≠ Contract ≠ Software Component
Runtime Semantic Flow ≠ Software Call Graph
Current src scaffold ≠ Approved Software Architecture
```

当前工作计划只回答：已确认的 System Responsibilities 与 Contract semantics，如何在 First Slice 范围内形成最小、可审阅的软件结构。

## 1. Inherited Inputs

后续每一步都必须以以下材料为输入，不得重新猜测上游语义：

| Input | Authority / Role |
| --- | --- |
| `docs/03_software/01_MINIMAL_SOFTWARE_ARCHITECTURE_PHASE_HANDOFF.md` | Consolidated input / navigation；Architecture Authority = No |
| `docs/02_system/00_SYSTEM_ARCHITECTURE.md` | System responsibility and global architecture boundary |
| `docs/02_system/vertical_slices/01_research_execution/03_MINIMAL_RUNTIME_PATH.md` | First Slice runtime semantic path |
| `docs/02_system/vertical_slices/01_research_execution/contracts/01_EXECUTION_SPINE.md` | D1 execution spine |
| `docs/02_system/vertical_slices/01_research_execution/contracts/02_SEARCH_INVOCATION.md` | D2 Search / Provider Resolution |
| `docs/02_system/vertical_slices/01_research_execution/contracts/03_RESEARCH_SEMANTICS.md` | D3 Research / Evidence semantics |
| `docs/02_system/vertical_slices/01_research_execution/contracts/04_EXECUTION_RECORD.md` | D4 Execution Record |
| `docs/02_system/vertical_slices/01_research_execution/contracts/05_PROVIDER_MAPPING.md` | D5 Provider Mapping / Adapter boundary |
| `docs/02_system/vertical_slices/01_research_execution/05_DEFERRED_REGISTER.md` | Deferred / Not Yet Proven / rejected guardrails |
| Phase Handoff / Contract Index | TT-17 closure and current endpoint status record |

## 2. Seven-step Internal Work Plan

这七步是当前 Minimal Software Architecture 的内部推进顺序，不是新的 System Architecture Round，也不重新打开 Product / System / Contract semantics。

| Step | Work package | Status |
| --- | --- | --- |
| 1 | Responsibility → Software Responsibility Mapping | **CANDIDATE COMPLETE** |
| 2 | Execution Spine Software Design | **NEXT** |
| 3 | Search / Provider Spine Software Design | **PLANNED** |
| 4 | Research / Evidence Software Design | **PLANNED** |
| 5 | Execution Record / Referenceability | **PLANNED** |
| 6 | Minimal Software Architecture Assembly | **PLANNED** |
| 7 | Minimal Software Architecture Review Gate | **PLANNED** |

暂时不创建 `01`–`07` 的步骤文档。对应步骤真正开始时，才创建其受控文档。

## 3. Step 1 — Responsibility → Software Responsibility Mapping

Step 1 首先确认 System Responsibility 如何映射为候选 software responsibility，保持：

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

Step 1 不决定最终 package、module、class 或 framework。它只建立责任映射、边界归属、依赖方向问题与待审查 seam。

## 4. Step 2 — Execution Spine Software Design

```text
Upstream:
D1 = C1 + C2b + C2a
```

Step 2 只处理：

```text
Business Work Request
→ C1 Task Execution Boundary
→ C2b Task Runtime
↔ C2a Research Skill
→ C2a Business Completion
→ C2b Execution Terminalization
→ C1 Terminal Return semantics
```

允许提到：C2b terminalization → downstream C6 closure seam。

以下统一留给 Step 5 — Execution Record / Referenceability：

```text
C6 representation
C6 referenceability
C6 retention
C6 finalization representation
```

必须保持：C2b 是 Execution / Capability Invocation Coordination；C2a 是 Business Method。Runtime Semantic Flow 不自动等于 Software Call Graph。

## 5. Step 3 — Search / Provider Spine Software Design

Step 3 继承 D2 / D5 与 TT-17 closure，研究最小 Search / Provider software seam：

```text
C2a Search Need → C2b Coordination → C3 Search Capability
→ C4a Static Provider Resolution → C4b Scrape Creators Adapter
→ Scrape Creators
→ TT-17 Search by Keyword
```

Provider、Adapter / Connector 与 Access Mechanism 必须分离：

```text
Provider = Concrete External Provider
Adapter / Connector = Internal translation / quirk absorption boundary
Access Mechanism = API / SDK / MCP / Native Integration
Provider ≠ Adapter ≠ Endpoint / Access Mechanism
```

TT-17 仍是当前 First Slice 的 admitted Provider endpoint / access surface，不能升级为更强的 temporal、ranking、regional 或 completeness guarantee。

## 6. Step 4 — Research / Evidence Software Design

Step 4 只研究如何表示已要求的 Research / Evidence semantics：

- Research Skill 保持 business method、sampling、Finding、Hypothesis 与 Result 责任；
- REQUIRED Evidence Boundary 必须可表示；
- 不假设建立 Full Evidence Service；
- Analysis Activity 保持在 Research Skill 内，不提前创建 Independent Analyze Capability；
- Missingness、provenance、sample boundary、lossy Provider fact 必须保留其语义等级。

## 7. Step 5 — Execution Record / Referenceability

Step 5 继承 D4 / C6 与 D5 referenceability seam：

```text
Required internal reference
→ post-terminal resolvability obligation
```

这不等于 Raw Payload Duplication、永久 Raw Payload Retention 或 C4b-owned Retention Policy。Minimal persistence representation 可以是合法软件架构问题；Dedicated Persistence Service 与 Specific Database Technology 仍保持 `NOT YET PROVEN`，除非真实证据要求。

## 8. Step 6 — Minimal Software Architecture Assembly

Step 6 将 Steps 1–5 的候选边界组装成 First Slice 的最小软件架构候选，并检查：

- Responsibility、Contract、Software Component 是否保持三者分离；
- C2b coordination 是否被错误替换为 C2a 直接调用 Capability；
- Provider limitation、TT-17 bounded semantics、missingness 与 referenceability 是否被保留；
- Application transport 是否只在 Walking Implementation 确有需要时选择；
- Deferred / Not Yet Proven / Explicitly Rejected 状态是否未被提升成默认实现 backlog。

## 9. Step 7 — Minimal Software Architecture Review Gate

Step 7 是进入 Walking Implementation 前的人工 Review Gate，不是新的 architecture round。Review 至少确认：

```text
First Slice scope preserved
System Architecture semantics preserved
D1–D5 semantics preserved
Deferred guardrails preserved
TT-17 limitations preserved
Current src scaffold not treated as authority
```

只有 Minimal Software Architecture Review 通过后，Walking Implementation 才可能获得新的明确授权；当前仍为：

```text
Walking Implementation = NOT YET AUTHORIZED
```

## 10. Current Status Summary

```text
Minimal Software Architecture
= AUTHORIZED NEXT DESIGN PHASE

Step 1
= CANDIDATE COMPLETE

Step 1 Output
= 01_SOFTWARE_RESPONSIBILITY_MAPPING.md

Step 2
= NEXT

Steps 3–7
= PLANNED

Walking Implementation
= NOT YET AUTHORIZED
```

本文件不创建 `01`–`07` 空文档，不写代码，不修改 Product Architecture、System Architecture、D1–D5、`src/` 或 `tests/`。
