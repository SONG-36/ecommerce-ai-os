# Ecommerce AI OS — System Architecture V0.1

- **版本**：V0.1
- **状态**：Draft for Human Review / 待人工审阅
- **文档类型**：System Architecture
- **目标路径**：`docs/02_system/00_SYSTEM_ARCHITECTURE.md`
- **项目**：Ecommerce AI OS
- **最后更新**：2026-08-14

---

## 0. 文档目的

这份文档只回答：

> **为了支撑 Product Architecture，Ecommerce AI OS 从系统层应该由哪些责任区域组成，它们如何协作。**

本文件只做到框架级，不设计详细字段。

当前重点：

- Applications；
- Skills；
- Stable Core；
- Capabilities；
- Foundation Services；
- Providers；
- 六个 Stable Core Candidate Areas；
- 依赖方向；
- Agent / MCP / RAG 等技术概念的位置；
- System Architecture 与 Software Architecture 的边界。

---

# 1. System Architecture 不是严格的六层流水线

之前可以用以下模型快速理解：

```text
Applications
↓
Skills
↓
Stable Core
↓
Capabilities
↓
Foundation Services
↓
Providers
```

但这不能被理解成严格的运行时调用顺序。

例如一个 Research Skill 可能同时依赖：

```text
Search Capability
Analyze Capability
Evidence Service
Knowledge Service
```

因此，更准确的理解是：

```text
                     ┌──────────────────────┐
                     │     Applications     │
                     │ Chat / Workspace /   │
                     │ Future Applications  │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │        Skills        │
                     │ Business Know-how /  │
                     │ Platform Adaptation  │
                     └──────────┬───────────┘
                                │
                                ▼
              ┌─────────────────────────────────┐
              │           Stable Core           │
              │                                 │
              │ Task Runtime                    │
              │ Extension Runtime               │
              │ Capability Contract             │
              │ Runtime Governance              │
              │ Execution Record                │
              │ Compatibility                   │
              └─────────┬──────────────┬────────┘
                        │              │
             ┌──────────▼───────┐  ┌──▼────────────────┐
             │   Capabilities   │  │ Foundation Services│
             │                  │  │                    │
             │ Search           │  │ Knowledge          │
             │ Analyze          │  │ Evidence           │
             │ Generate         │  │ Research           │
             │ Image            │  │ Artifact           │
             │ Video            │  │ Future Services    │
             │ Future           │  │                    │
             └─────────┬────────┘  └─────────┬──────────┘
                       │                     │
                       └──────────┬──────────┘
                                  ▼
                       ┌─────────────────────┐
                       │      Providers      │
                       │ APIs / Models / SDK │
                       │ MCP / Storage / ... │
                       └─────────────────────┘
```

这是一张**责任关系图**，不是最终调用图、进程图或部署图。

---

# 2. Applications / 应用入口

Applications 表示：

> **用户真正进入 Ecommerce AI OS 的产品入口。**

未来可能包括：

- Chat；
- Research Workspace；
- Creative Workspace；
- Operator Console；
- Automation Application；
- Future Applications。

Applications 不等于 Product Use Case Family。

区别：

```text
Product Architecture
→ 用户想完成什么工作

Applications
→ 用户从什么产品入口使用这些能力
```

当前 Applications：

**Candidate / Not Yet Designed**

---

# 3. Skills / 业务方法层

System Architecture 中：

> **Skill = 业务上怎么做。**

Skill 承载：

- Business Know-how；
- Professional Method；
- Platform Adaptation；
- Domain Rules；
- Composite Workflow Method。

未来可能包括：

```text
Generic Skills
├── Research Method
├── Script Writer
├── Director
└── Critic

Commerce Skills
├── Product Grounding
├── Claim Safety
└── Selling Point Integration

Platform Skills
├── TikTok Hook
├── TikTok Pacing
├── Amazon Listing Method
└── Future

Composite Skills
└── Multiple Skill Composition
```

Skill 不负责：

- Provider API 调用细节；
- Scrape Creators 字段；
- 模型 SDK；
- 存储实现；
- 通用 Runtime 规则。

---

# 4. Capabilities / 系统能力

Capability 回答：

> **系统会做什么。**

例如：

```text
Search
Retrieve
Analyze
Generate Text
Generate Image
Generate Video
Transcribe
Translate
Future
```

Capability 不负责：

> “业务上应该怎么做。”

因此边界是：

```text
Skill
= 怎么做

Capability
= 能做什么

Provider
= 谁来做
```

这三个概念当前作为 System Architecture 的核心语义边界。

---

# 5. Providers / 具体实现与外部接入

Provider 表示：

> **具体外部实现、模型、数据访问方式、API、SDK、MCP Server、Storage 或其他基础设施适配器。**

例如未来可能包括：

- Scrape Creators；
- OpenAI；
- Kling；
- 即梦；
- Storage Provider；
- MCP Server；
- Other APIs / SDKs；
- Future Providers。

Provider 并不只服务 Capability，也可能服务：

- Foundation Service；
- Artifact Storage；
- Integration。

核心原则：

> **Provider-specific quirks 不应该直接泄漏到业务 Skill。**

Provider Lab 提供 Provider 事实，但 Provider Lab 不定义 Ecommerce AI OS 顶层架构。

---

# 6. Stable Core / 稳定核心

Stable Core 只负责：

> **让 Task、Skill、Capability、Service、Provider 在稳定的系统规则下协作。**

Stable Core 不承载：

- TikTok 业务知识；
- Amazon 业务知识；
- Short Drama 方法；
- Research 专业方法；
- LLM Prompt；
- Scrape Creators 字段；
- 具体 Provider 业务逻辑。

当前 Stable Core 六个 Candidate Areas：

```text
Stable Core
│
├── Task Runtime
├── Extension Runtime
├── Capability Contract
├── Runtime Governance
├── Execution Record
└── Compatibility
```

状态：

**Candidate Architecture**

内部对象、字段、接口、运行时行为尚未批准。

---

## 6.1 Task Runtime

候选职责：

- Task；
- Context Envelope；
- State；
- Checkpoint；
- pause / resume；
- 长任务状态恢复。

详细设计：

**Not Yet Designed**

---

## 6.2 Extension Runtime

候选职责：

- Skill Contract；
- Extension Point；
- Composition；
- Dependency；
- Context Binding；
- Adaptation Mechanism。

原则：

> Skill 适配机制可能属于 Core，但具体业务适配规则属于 Skill。

详细设计：

**Not Yet Designed**

---

## 6.3 Capability Contract

候选职责：

- Skill 如何声明 Capability；
- Capability Interface；
- Capability Resolution Contract；
- Capability 与 Provider 的边界。

详细设计：

**Not Yet Designed**

---

## 6.4 Runtime Governance

原候选名称 `Governance` 在本基线中改名为：

> **Runtime Governance**

目的是和项目层的：

> **Architecture Governance**

严格区分。

Runtime Governance 负责系统运行时，例如：

- Permission；
- Policy Enforcement；
- Human Gate；
- Cost Gate；
- Risk Gate。

例如：

```text
高成本视频生成
↓
Human Approval
↓
Execute
```

而 Architecture Governance 负责：

- Draft；
- Candidate；
- Approved；
- ADR；
- Superseded；
- Architecture Change。

因此：

```text
Runtime Governance
≠
Architecture Governance
```

详细 Runtime Governance：

**Not Yet Designed**

---

## 6.5 Execution Record

候选职责：

- Run；
- Artifact Reference；
- Provenance；
- Trace Reference；
- 执行版本；
- 可追溯性；
- 可复现上下文。

详细设计：

**Not Yet Designed**

---

## 6.6 Compatibility

候选职责：

- Contract Version；
- Skill Version；
- Capability Version；
- Provider Version；
- Compatibility；
- Migration；
- Deprecation。

详细设计：

**Not Yet Designed**

---

# 7. Foundation Services / 基础服务

有些系统能力不是一次调用结束，而是长期维护状态、知识、证据、资产或研究上下文。

这类能力当前称为：

> **Foundation Services**

候选：

```text
Foundation Services
│
├── Knowledge
├── Evidence
├── Research
├── Artifact
└── Future Services
```

状态：

**Candidate / Detailed Architecture Not Yet Designed**

---

## 7.1 Knowledge

可能负责长期知识管理、版本、读取、更新候选和审核后的正式更新。

但当前详细系统架构未设计。

---

## 7.2 Evidence

可能负责 Evidence 的保存、引用、追溯、解释边界和来源关系。

但当前详细系统架构未设计。

---

## 7.3 Research

可能负责：

- Research Question；
- Evidence Need；
- Data Discovery；
- Research Result；
- Finding。

但当前不继承旧 SIG 对象作为正式新 OS Contract。

---

## 7.4 Artifact

可能负责：

- Script；
- Image；
- Video；
- Report；
- File；
- Other Produced Assets。

这里只确认 Artifact 是重要系统关注点，不定义存储实现。

---

# 8. Capabilities 与 Foundation Services 的区别

当前原则：

```text
Capabilities
≠
Foundation Services
```

一个 Capability 更接近：

```text
Input
↓
Perform Capability
↓
Output
```

例如：

```text
Generate Video
```

而 Foundation Service 更可能涉及：

- 长期状态；
- 生命周期；
- 版本；
- 查询；
- 更新；
- 审核；
- 追溯。

例如：

```text
Knowledge Service
```

最终哪些东西属于 Capability、哪些属于 Service，后续专项审计。

---

# 9. Agent 的位置

当前不建立：

```text
Agent Layer
```

作为顶层 System Architecture。

Agent 当前理解为：

> **Execution / Decision Strategy**

未来可能参与：

- Application；
- Skill Orchestration；
- Task Runtime；
- Future Runtime Strategy。

但具体位置：

**Not Yet Designed**

因此：

```text
Agent
≠ Stable Core 本身
≠ 顶层 Architecture Layer
```

---

# 10. MCP / RAG / Embedding / Vector DB / LLM 的位置

这些都不是当前顶层 System Architecture Layer。

当前理解：

- MCP = Integration / Capability Access Mechanism；
- RAG = Knowledge Retrieval Pattern；
- Embedding = Semantic Representation Technique；
- Vector DB = Storage / Retrieval Implementation；
- LLM = Provider / Capability Implementation；
- Multimodal Model = Capability Implementation；
- Chat = Application / Interaction Surface。

具体采用与否由后续业务和软件需求决定。

---

# 11. 依赖原则

当前建议冻结一个 System Architecture 原则：

> **Business logic should depend on stable contracts, not concrete Providers.**

不推荐：

```text
TikTok Script Skill
↓
Scrape Creators API
↓
Kling API
```

推荐：

```text
TikTok Script Skill
↓
Capability / Service Contract
↓
Provider Resolution
↓
Concrete Provider
```

这样：

```text
Scrape Creators → Future Provider
Kling → 即梦 → Future Video Model
```

不会迫使业务 Skill 整体重写。

---

# 12. Product Architecture 到 System Architecture 的映射

Product Architecture：

```text
Research
Creative Production
Knowledge-assisted Work
Experiment & Validation
Platform Adaptation
```

并不直接等于 System Component。

例如：

```text
Creative Production
```

可能由：

- Skills；
- Capabilities；
- Stable Core；
- Foundation Services；
- Providers；

共同支撑。

因此：

> **Product Family 不直接映射成同名 System Module。**

---

# 13. System Architecture 总图

```text
Product Architecture
│
│ 用户能做什么
│
▼
Applications
│
▼
Skills
│
▼
Stable Core
│
├───────────────┐
▼               ▼
Capabilities    Foundation Services
│               │
└───────┬───────┘
        ▼
     Providers
```

注意：

> 这是一张 Responsibility Map，不是严格 Runtime Call Graph。

---

# 14. 当前架构状态

### Candidate Architecture

- Applications；
- Skills；
- Stable Core；
- Capabilities；
- Foundation Services；
- Providers。

### Stable Core Candidate Areas

- Task Runtime；
- Extension Runtime；
- Capability Contract；
- Runtime Governance；
- Execution Record；
- Compatibility。

### Candidate Foundation Services

- Knowledge；
- Evidence；
- Research；
- Artifact。

### Not Yet Designed

- Task Object；
- Skill Contract Details；
- Capability Schema；
- Provider Resolution；
- Runtime Governance Rules；
- Execution Record Schema；
- Compatibility Rules；
- Foundation Service Contracts；
- Agent Architecture；
- Event / Message Architecture；
- Persistence；
- Database；
- UI。

---

# 15. System Architecture 与 Software Architecture 的边界

System Architecture 回答：

> **系统由什么职责区域组成，边界是什么。**

Software Architecture 回答：

> **这些职责最终如何落成代码、模块、接口、运行时和部署结构。**

因此：

```text
System Architecture
        ↓
Software Architecture
```

不能反过来通过当前空 Python 目录推导 System Architecture。

---

# 16. Human Review Gate

当前文档状态：

# **Draft for Human Review**

批准本文件只代表：

> **当前 Ecommerce AI OS 的 System Architecture 责任区域、核心语义边界、六个 Stable Core Candidate、Candidate Foundation Services，以及 Provider / Capability / Skill 的基本关系，被接受为后续专项架构审计的工作基线。**

不代表：

- Stable Core 内部字段已批准；
- Foundation Service Contract 已批准；
- Agent 已批准；
- Database 已批准；
- Software Architecture 已批准；
- 可以全面实现。
