# ADR-001 — System Architecture V0.2 Boundary Refinement

- **状态**：Candidate / Human Review Recorded
- **日期**：2026-08-15
- **范围**：C01-C09 System Architecture Change Set
- **Architecture Authority**：`docs/02_system/00_SYSTEM_ARCHITECTURE.md`
- **Review Evidence**：`docs/05_references/ai_architecture/04_SYSTEM_ARCHITECTURE_STRESS_TEST.md`

## Context

External AI Architecture Audit、System Architecture Stress Test 和 Repository Fact Audit 识别出若干边界需要收紧。Human Review 已接受 C01-C09；C10 Operational Observability 继续延期。

本 ADR 记录已接受的边界收敛，不把整个 System Architecture 自动升级为 Approved。

## Decision

### C01 — Provider Boundary

明确区分：

```text
Provider
≠ Adapter / Connector
≠ API / SDK / MCP
```

当前依赖方向为：

```text
Capability / Service Contract
→ Provider Resolution
→ Adapter / Connector
→ Concrete Provider
→ API / SDK / MCP / Native Mechanism
```

不新增顶层 Adapter Layer。

### C02 — Research Placement

Research 保留为 Product Architecture 的 Cross-platform Use Case Family。

在 System Architecture 中，Research 标记为：

```text
System Placement Under Review
```

不再预设 Research 是确定的 Foundation Service。

### C03 / C08 — Task Runtime and Execution Coordination

Task Runtime 当前候选职责收敛为：

```text
Task Identity
Task Lifecycle
Execution Context
Runtime State
Pause / Continue
Failure Status
Execution Coordination
```

Skill / Workflow 定义业务方法；Task Runtime 负责本次执行推进；Agent 仍是可选的 Execution / Decision Strategy。

Checkpoint Strategy、Crash Recovery、Durable Execution、Retry Engine 保留为 Advanced Runtime Concerns，当前 Not Yet Proven / Not Yet Designed。

### C04 — Skill Extension Mechanism

将 Stable Core Candidate 的名称和职责从 `Extension Runtime` 收敛为 `Skill Extension Mechanism`。

它负责 Skill Contract、Registration、Composition、Dependency Declaration、Context Binding 和 Platform / Domain Adaptation；不负责 Task Lifecycle、Runtime State、Pause / Resume 或 Recovery。

### C05 — Runtime Governance

Runtime Governance 定义为：

```text
Enforcement Mechanism
```

Concrete Policy Source 来自 Skill、Platform、Domain、Capability 或 Configuration。Stable Core 不拥有具体 TikTok / Amazon 规则、Claim Policy 内容、Business Threshold 或平台运营规则。

### C06 — Execution Record

Execution Record 仅保存稳定执行事实与引用关系，包括 Run、Task、Input、Skill、Capability、Provider、Version、Output / Artifact、Trace、Runtime Facts 和 Reproducibility References。

长期边界保持：

```text
Trace ≠ Execution Record
Evidence ≠ Execution Record
Artifact ≠ Execution Record
Observability ≠ Execution Record
Evaluation ≠ Execution Record
```

### C07 — Compatibility

Compatibility 保留为 Cross-cutting Compatibility / Versioning Concern，不再作为独立一级 Stable Core Area。

其具体归属分别落在 Capability Contract、Skill Extension Mechanism、Provider Adapter / Integration、Software Architecture 和 Architecture Governance。

### C09 — Capability Invocation Surface

Capability Contract 增加 Invocation Surface、Input / Output Boundary、Error Boundary、Context Boundary、Runtime Governance Hook 和 Provider Resolution Boundary。

Tool 仅作为未来 Runtime / Software implementation representation，不新增 Tool Layer，也不在本 ADR 中冻结 Tool Schema。

## Deferred Decision

C10 Operational Observability 继续 DEFER。

System Architecture 只保留 Traceability Requirement 和 Execution Record Boundary。Observability Service、Metrics、Logging、Tracing Backend、Alerting 及具体技术选型继续由未来 Software Architecture 决定。

## Consequences

- Current System Architecture 从 V0.1 边界基线收敛为 V0.2 Candidate / Human-reviewed working architecture。
- Product Architecture 的 Research Family 不变。
- Foundation Services 的 Research placement 保持待审。
- Software Architecture 继续为 `Not Yet Designed`。
- 不引入 Agent、MCP、RAG、Vector DB、Database、Event Bus、Queue 或 Observability Backend。
- 后续专项设计必须遵守本 ADR 记录的语义边界，除非新的 Change Proposal 经 Human Review 接受。

## Alternatives / Rejected Directions

本节记录本轮 Architecture Decision 未采用的路线，不构成永久禁止。未来如果出现新的真实业务证据，可以重新审阅。

1. **Top-level System Architecture Redesign**
   - Rejected because：当前六块 Responsibility Map 仍可承载已确认需求，本轮问题主要是 Boundary Refinement。

2. **Add Agent Layer**
   - Rejected because：Agent 仍属于 Execution / Decision Strategy，真实业务尚未证明需要独立顶层 Agent Layer。

3. **Add Tool Layer**
   - Rejected because：Invocation Surface 已进入 Capability Contract，Tool 可以作为未来 Runtime / Software representation。

4. **Add Orchestration Layer**
   - Rejected because：Execution Coordination 已进入 Task Runtime，不需要新的顶层层级。

5. **Keep Extension Runtime as-is**
   - Rejected because：当前职责主要属于 Skill Extension / Composition，未证明需要独立第二套 Runtime。

6. **Keep Compatibility as standalone Stable Core Area**
   - Rejected because：Compatibility / Versioning 是真实 concern，但当前更适合作为 Cross-cutting Concern。

7. **Keep Research as confirmed Foundation Service**
   - Rejected / Deferred because：Research Product Family 已确认，但其 System Foundation 属性尚未被证明。

8. **Add Observability Service now**
   - Deferred because：当前 Requirements 强证明的是 Traceability，Operational Observability 留到 Software Architecture。

## Revisit Conditions

以下事实出现时，应重新开启相应 Architecture Review：

- 真实 Workflow 证明需要跨进程或长时间 Durable Execution 时，重新审查 Checkpoint、Crash Recovery、Retry 和 Durable Runtime。
- Skill 扩展机制出现独立生命周期、状态或执行需求时，重新评估是否需要真正的 Extension Runtime。
- 不同 Contract、Skill、Provider 之间出现统一 Runtime Compatibility Negotiation 需求时，重新评估 Compatibility 是否需要成为独立 Core Area。
- Research 出现稳定、跨多个 Product Workflow 复用的独立生命周期和系统职责时，重新评估 Research 是否应成为 Foundation / Domain Service。
- Provider Integration 复杂度证明现有 Provider Boundary 无法承载时，重新评估 Adapter / Integration 是否需要更强独立结构。
- Software Architecture 开始设计并出现真实生产运行需求时，重新评估 Operational Observability。
- 新的真实业务需求无法被 Applications、Skills、Stable Core、Capabilities、Foundation Services、Providers 合理承载时，重新开启 Top-level System Architecture Review。

## Status Boundary

本 ADR 不代表：

- 整个 System Architecture 已 Approved；
- 任何内部 Schema 或 Runtime Contract 已冻结；
- Software Architecture 已设计；
- C10 已接受。
