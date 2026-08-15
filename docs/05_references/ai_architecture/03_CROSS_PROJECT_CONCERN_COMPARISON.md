# Ecommerce AI OS — Cross-project Concern Comparison V0.1

**Suggested Path:** `docs/05_references/ai_architecture/03_CROSS_PROJECT_CONCERN_COMPARISON.md`  
**Status:** External Architecture Evidence / Draft  
**Architecture Authority:** No  
**Stage:** External AI Architecture Audit — Phase 3  
**Upstream References:**
- `01_AI_ARCHITECTURE_CONCEPT_MAP.md`
- `02_AI_ARCHITECTURE_LANDSCAPE.md`

---

# 0. Document Purpose

前两阶段已经完成：

```text
01 Concept Map
→ 理解 Agent / Runtime / Harness / MCP / State / Tool 等基础概念

02 Architecture Landscape
→ 观察 OpenAI Agents SDK / LangGraph / Deep Agents / MCP / AutoGen Core
   如何组合这些概念
```

本阶段不再逐个介绍 Framework。

本阶段只回答：

> **这些架构路线完全不同的真实项目中，到底有哪些工程问题反复出现？**

同时识别：

1. 多项目反复出现的真实工程问题；
2. 只属于某些架构路线的实现选择；
3. 名字相同但实际语义不同的概念；
4. 后续哪些问题值得拿回 Ecommerce AI OS 做 Architecture Stress Test。

本文件不负责：

- 修改 Ecommerce AI OS System Architecture；
- 判断某个 Framework 应不应该采用；
- 技术选型；
- Software Architecture 设计；
- Candidate → Approved。

---

# 1. Comparison Method

本阶段使用四道过滤。

```text
External Recurrence
多个独立项目是否反复遇到这个问题？
        ↓
Concept Normalization
它们说的是不是同一种问题？
        ↓
Ecommerce Relevance
Ecommerce AI OS 自己是否真的存在这个问题？
        ↓
Architecture Placement
如果存在，应该放在哪个架构层？
```

本文件当前只完成前两步：

```text
External Recurrence
+
Concept Normalization
```

后两步进入下一阶段。

---

# 2. Compared Projects

第一批样本：

```text
OpenAI Agents SDK
LangGraph
Deep Agents
MCP
AutoGen Core
```

它们并不属于同一种产品类型。

当前 Landscape 定位：

```text
OpenAI Agents SDK
→ Agent-centric Framework / Multi-Agent Workflow

LangGraph
→ Stateful Orchestration Framework

Deep Agents
→ Opinionated Agent Harness

MCP
→ Integration Protocol

AutoGen Core
→ Event-driven Distributed Multi-Agent Runtime
```

因此，本阶段比较的是：

> **工程 Concern**

而不是：

> **Framework 功能多少。**

---

# 3. Cross-project Concern Matrix

| Engineering Concern | OpenAI Agents SDK | LangGraph | Deep Agents | MCP | AutoGen Core |
|---|---|---|---|---|---|
| Agent / Decision | Core | Supported | Strong | Not responsible | Core |
| Workflow / Orchestration | Strong | Core | Strong / inherited | Not responsible | Strong |
| Runtime / Execution | Strong | Core | Inherits LangGraph | Not responsible | Core |
| State / Persistence | Sessions / run state | Core | LangGraph + backend | Protocol stateless | Agent/runtime state |
| Pause / Resume | HITL / run state | Core | Inherited / integrated | Not runtime responsibility | Pattern-dependent |
| Tool / External Capability | Core | Composable | Strong | Core protocol primitive | Strong |
| Integration / Protocol | Supports MCP etc. | Not primary | Through tools/backends | Core | Extensions available |
| Human Control | Guardrails / HITL | Interrupt / HITL | HITL / permissions | Host boundary | Runtime/security concerns |
| Memory / Context | Session / context | Strong | Strong | Not memory system | Model context / memory |
| Trace / Observability | Built-in tracing | Runtime + LangSmith ecosystem | Mostly inherited / surrounding | Not primary | Logging / telemetry |
| Multi-Agent | Strong | Possible | Subagents | Not responsible | Core |
| Distributed Runtime | Not primary | Not primary | Not primary | Not runtime | Core |

OpenAI Agents SDK officially lists Agents, Tools, Handoffs, Guardrails, Human-in-the-loop, Sessions, Tracing and Sandbox Agents among its core concepts. 

LangGraph describes itself as a low-level orchestration framework for long-running, stateful agents, emphasizing durable execution, HITL and memory. 

Deep Agents explicitly separates itself from LangGraph Runtime:

```text
Deep Agents = opinionated harness
LangChain = agent abstraction
LangGraph = runtime
```

and states that Deep Agents does not introduce a new runtime. 

MCP currently uses a Host / Client / Server architecture and defines a stateless protocol for exchanging tools, resources, prompts and capabilities. 

AutoGen Core explicitly targets event-driven, distributed, scalable multi-agent systems using the Actor Model, with runtimes responsible for communication, identity and lifecycle.  

---

# 4. Category A — Strong Recurring Engineering Problems

The following problems repeatedly appear across substantially different architecture approaches.

They are therefore stronger candidates for:

> **Real AI Engineering Problems**

rather than one framework's implementation preference.

---

## 4.1 Execution / Runtime

Recurring questions:

```text
任务如何启动？
如何持续执行？
如何处理中断？
如何恢复？
如何管理执行生命周期？
```

Different projects answer these differently:

```text
OpenAI Agents SDK
→ Runner / Agent execution

LangGraph
→ State + durable execution

Deep Agents
→ Reuses underlying runtime

AutoGen Core
→ Agent Runtime + lifecycle
```

### External Evidence Verdict

```text
STRONG RECURRING PROBLEM
```

This does **not** yet mean:

```text
Ecommerce AI OS Task Runtime = Correct
```

It only means:

> Reliable AI execution is a real recurring engineering concern.

---

# 4.2 External Capability / Tool Access

Across different systems, AI execution eventually needs to access capabilities outside the model itself.

Typical pattern:

```text
Agent / Workflow
↓
Need external capability
↓
Tool / Function / Server / Model / API
↓
Execution Result
```

OpenAI Agents SDK treats Tools as a core concept. 

MCP specifically standardizes access to external tools, resources and prompts. 

Deep Agents dynamically composes tool surfaces through middleware and backends. 

### External Evidence Verdict

```text
STRONG RECURRING PROBLEM
```

What remains undecided:

```text
Tool
Capability
Provider
Adapter
Protocol
```

should not yet be assumed to have one universal architecture.

---

# 4.3 State / Context / Persistence

Recurring questions:

```text
当前任务进行到哪里？
模型当前看到什么？
中断后如何继续？
哪些信息跨步骤保留？
哪些信息需要长期持久化？
```

LangGraph makes stateful execution and durable persistence central. 

Deep Agents explicitly separates:

```text
Graph state / checkpoints
from
Filesystem / memory persistence
```

showing that even within one ecosystem, different persistence concerns remain separate. 

OpenAI Agents SDK separately exposes Sessions, HITL state and workspace-oriented Sandbox Agents. 

### External Evidence Verdict

```text
STRONG RECURRING PROBLEM
```

Important normalization:

```text
State
≠ Context
≠ Session
≠ Memory
≠ Formal Knowledge
```

---

# 4.4 Human Control / Runtime Safety

Recurring concerns include:

```text
Permission
Guardrail
Human Approval
Interrupt
Sandbox
Security Boundary
```

OpenAI Agents SDK explicitly includes Guardrails, HITL and Sandbox Agents. 

LangGraph treats human-in-the-loop as a core runtime concern. 

Deep Agents includes filesystem permission enforcement and human approval mechanisms. 

MCP assigns security, consent, authorization and connection boundaries primarily to the Host. 

AutoGen Runtime also explicitly owns security/privacy boundaries around Agent communication and lifecycle. 

### External Evidence Verdict

```text
STRONG RECURRING PROBLEM
```

The repeated problem is not:

```text
Everybody needs the same Guardrail Framework
```

It is:

> Autonomous execution requires explicit control boundaries.

---

# 4.5 Trace / Observability

Recurring questions:

```text
AI 到底执行了什么？
调用了哪个 Tool？
执行路径是什么？
哪里失败？
状态如何变化？
系统现在健康吗？
```

OpenAI Agents SDK includes tracing as a built-in core feature. 

LangGraph explicitly points to execution path, state transition and runtime visibility in its ecosystem. 

AutoGen Core lists observability / debuggability and provides logging / telemetry concerns in Core. 

### External Evidence Verdict

```text
STRONG RECURRING PROBLEM
```

But:

```text
Trace
≠ Execution Record
≠ Observability
≠ Evaluation
```

They remain different concerns.

---

# 5. Category B — Real Problems but Architecture Route Choices

The following concepts are real and useful, but evidence does not support treating them as universal top-level requirements.

---

## 5.1 Graph

LangGraph strongly uses:

```text
Graph
Node
Edge
State Transition
```

But OpenAI Agents SDK, MCP and AutoGen do not require this abstraction.

Verdict:

```text
ARCHITECTURE ROUTE
not
UNIVERSAL CORE REQUIREMENT
```

---

## 5.2 Actor Model

AutoGen Core uses Actor Model as a primary architectural foundation.

Other samples do not.

Verdict:

```text
ARCHITECTURE ROUTE
```

---

## 5.3 Harness

Deep Agents explicitly identifies as an Agent Harness. 

But not every system requires a distinct Harness architecture.

Verdict:

```text
OPTIONAL WORKING-ENVIRONMENT PATTERN
```

---

## 5.4 MCP

MCP solves a real integration problem.

But:

```text
MCP
≠ Integration itself
```

Other approaches remain possible:

```text
SDK
API
Direct library integration
Custom adapters
Other protocols
```

Verdict:

```text
PROTOCOL CHOICE
not
UNIVERSAL ARCHITECTURE LAYER
```

---

## 5.5 Multi-Agent

OpenAI Agents SDK and AutoGen support multi-agent systems strongly.

Deep Agents supports subagents.

LangGraph can orchestrate multiple agents.

But:

> This demonstrates that Multi-Agent is useful when a problem requires it.

It does not demonstrate:

```text
Every AI system needs Multi-Agent architecture
```

Verdict:

```text
EXECUTION / ORGANIZATION STRATEGY
```

---

## 5.6 Handoff

Handoff is one way to coordinate agents.

Alternatives include:

```text
Agent as Tool
Supervisor
Shared Workflow
Message Routing
Central Orchestration
```

Verdict:

```text
COORDINATION MECHANISM
```

---

## 5.7 Distributed Runtime

AutoGen Core strongly supports distributed runtime. 

The other first-wave samples do not treat it as a universal requirement.

Verdict:

```text
SCALE-DEPENDENT ARCHITECTURE CHOICE
```

---

# 6. Category C — Same Name, Different Meaning

This category presents one of the largest architecture-review risks.

---

# 6.1 Capability

MCP includes:

```text
Capability Negotiation
```

but this means:

> Which protocol features the Client / Server supports.

Ecommerce AI OS currently defines:

```text
Capability
= 系统会做什么
```

fileciteturn0file4L197-L233

Therefore:

```text
MCP Capability
≠ Ecommerce AI OS Capability
```

---

# 6.2 Skill

Deep Agents has a concept named:

```text
Skills
```

but those Skills belong to an Agent Harness mechanism.

Ecommerce AI OS currently defines Skill around:

```text
Business Know-how
Professional Method
Platform Adaptation
Domain Rules
Composite Workflow Method
```

fileciteturn0file4L149-L187

Therefore:

```text
Deep Agents Skill
≠ Ecommerce AI OS Skill
```

---

# 6.3 Memory

External frameworks often use Memory to mean:

```text
Conversation History
Agent Working Memory
Cross-session Context
Persistent Agent State
```

Ecommerce AI OS currently has a stronger business requirement around Knowledge:

```text
managed
versioned
traceable
reviewed
evidence-aware
```

and formal knowledge updates require Human Review. fileciteturn0file2L227-L264

Therefore:

```text
Agent Memory
≠ Ecommerce Knowledge
```

---

# 7. Current External Concern Map

Current first-wave external evidence can now be compressed into three categories.

```text
A. STRONG RECURRING PROBLEMS

Runtime / Execution
External Capability Access
State / Context / Persistence
Human Control / Runtime Safety
Trace / Observability


B. ARCHITECTURE ROUTE CHOICES

Graph
Actor Model
Harness
MCP
Multi-Agent
Handoff
Distributed Runtime


C. SAME-NAME / SEMANTIC RISKS

Capability
Skill
Memory
```

This is the main Phase 3 result so far.

---

# 8. What This Does NOT Prove

External recurrence does not prove:

```text
Ecommerce AI OS needs this exact component.
```

For example:

```text
External projects use HITL
```

only establishes:

> Human control is a recurring AI engineering concern.

The next questions are:

```text
Does Ecommerce AI OS have a real business need for it?

If yes:
Where should it live?

Stable Core?
Skill?
Capability?
Foundation Service?
Application?
Software implementation?
```

Likewise:

```text
LangGraph has Checkpoints
```

does not mean:

```text
Ecommerce AI OS must use LangGraph.
```

It only strengthens the evidence that:

> Long-running state recovery is a real Runtime concern.

---

# 9. Next-stage Input

The next stage begins the actual Ecommerce AI OS architecture audit.

Inputs:

```text
Current Authority / Baseline Package

1. 02_CURRENT_HANDOFF.md
2. 00_PROJECT_BASELINE_V0.1.md
3. 01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md
4. 00_PRODUCT_ARCHITECTURE.md
5. 00_SYSTEM_ARCHITECTURE.md
6. 00_SOFTWARE_ARCHITECTURE.md
7. 00_ARCHITECTURE_GOVERNANCE.md
8. 02_LEGACY_ARCHITECTURE_REFERENCE_AUDIT.md
9. 03_PROVIDER_LAB_ASSET_HANDOFF.md

+

01_AI_ARCHITECTURE_CONCEPT_MAP.md

+

02_AI_ARCHITECTURE_LANDSCAPE.md

+

03_CROSS_PROJECT_CONCERN_COMPARISON.md
```

The next audit applies:

```text
External Recurrence
↓
Concept Normalization
↓
Ecommerce Business Relevance
↓
Architecture Placement
```

---

# 10. Phase 3 Boundary

This document remains:

```text
External Architecture Evidence
```

It is not:

```text
System Architecture Authority
```

It cannot directly modify:

```text
Applications
Skills
Stable Core
Capabilities
Foundation Services
Providers
```

or the Stable Core Candidate Areas:

```text
Task Runtime
Extension Runtime
Capability Contract
Runtime Governance
Execution Record
Compatibility
```

Those remain Candidate architecture in the current System Architecture baseline. fileciteturn0file4L724-L765

Any architecture change must continue to follow the existing Governance process:

```text
New Requirement / Evidence
↓
Impact Classification
↓
Existing Architecture Supports It?
↓
Architecture Change Proposal if necessary
↓
Human Review
↓
Approval
```

fileciteturn0file6L702-L750

---

# 11. Phase 3 Conclusion

The first external comparison phase does **not** suggest:

> “follow the hottest Agent framework.”

Instead it suggests a more stable principle:

> **The stable part of AI architecture is often the recurring engineering problem, not the current framework used to solve it.**

Current strongest recurring problems are:

```text
Reliable execution

External capability access

State and persistence

Human control

Traceability / observability
```

while:

```text
Graph
Actor Model
Harness
MCP
Multi-Agent
Handoff
```

currently appear more like possible architecture mechanisms or routes.

The next stage therefore stops studying frameworks as the primary object.

It returns to:

# **Ecommerce AI OS itself.**

The next question is:

> **Which of these recurring engineering problems are actually required by Ecommerce AI OS's confirmed business needs, and where should they live in the current architecture?**