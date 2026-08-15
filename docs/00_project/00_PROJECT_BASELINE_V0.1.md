# Ecommerce AI OS — 项目基线 V0.1

- **版本**：V0.1
- **状态**：Draft for Human Review / 待人工审阅
- **文档类型**：Project Baseline / 项目总地图
- **项目名称**：Ecommerce AI OS
- **项目仓库**：`/Volumes/projects/andy/0813/ecommerce-ai-os`
- **当前阶段**：Architecture Baseline / Handoff Preparation
- **最后更新**：2026-08-15

---

## 0. 文档目的

这份文档是 Ecommerce AI OS 当前阶段的**项目总地图**。

它只回答：

> **我们现在在做什么？系统当前被如何理解？哪些内容已经形成工作基线，哪些仍然只是 Candidate，下一步是什么？**

这份文档负责：

- 项目身份；
- 项目为什么存在；
- 当前 Product Architecture 摘要；
- 当前 System Architecture 摘要；
- 当前 Software Architecture 状态；
- 当前 Architecture Governance 摘要；
- External / Reference Assets；
- Repository Information Architecture；
- 当前项目状态；
- 当前下一步；
- Current Authority 文档入口。

这份文档**不再承担详细架构设计**。

详细内容必须进入对应专项文档。

---

# 1. Project Identity / 项目身份

项目名称：

# **Ecommerce AI OS**

当前产品方向：

> **构建一个面向跨境电商、长期可扩展的 AI-native 工作系统。**

它需要能够逐步承载：

- 不同电商平台；
- 不同业务流程；
- 不同运营方法；
- 不同 AI Capability；
- 不同 Provider；
- 不同 Professional Skill；
- 以及未来目前还没有想到的新业务。

核心目标不是一次把所有功能做完。

而是：

> **建立一个稳定但可扩展的系统，使未来新增业务、平台、Provider、AI 模型或专业 Skill 时，不必反复推翻整个架构。**

---

# 2. Why This Project Exists / 为什么会出现 Ecommerce AI OS

项目并不是从“先做一个 AI OS”开始的。

真实演变大致是：

```text
TikTok 内容生产问题
        ↓
搜索参考视频
        ↓
发现仅找爆款参考视频不足以指导高质量内容
        ↓
Market / Product / User / Competitor / Content Research
        ↓
发现 Research 可以跨 TikTok / Amazon / Temu 等平台复用
        ↓
发现业务问题需要跨来源数据与 Evidence
        ↓
Creative Production 扩张
Script / Image / Video / Short Drama / Director / Editing
        ↓
Knowledge 复用需求
        ↓
Own-business Experiment & Validation
        ↓
发现专业运营方法会持续变化和补充
        ↓
需要：
Stable Core
+ Extensible Capability
+ Replaceable Provider
+ Pluggable Skill
        ↓
Ecommerce AI OS
```

因此：

> **Ecommerce AI OS 是真实业务需求不断扩张后形成的长期产品方向，而不是为了使用 Agent、MCP、RAG 等技术而创造的抽象平台。**

完整演变和需求边界见：

`docs/00_project/01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md`

---

# 3. Current Product Architecture / 当前产品架构

Product Architecture 只回答：

> **用户拿 Ecommerce AI OS 能完成什么类型的工作。**

当前工作模型分为两个主要维度。

## 3.1 Cross-platform Use Case Families

当前已确认的跨平台业务能力方向：

```text
Research / 研究

Creative Production / 内容与创意生产

Knowledge-assisted Work / 知识辅助工作

Experiment & Validation / 实验与验证
```

当前 Family 不是永久固定模块。

未来真实业务出现后，可以：

- 在现有 Family 下增加子能力；
- 或在满足独立、跨平台、完整业务工作的条件下，新增 Candidate Product Family。

例如：

```text
AI Voiceover
→ Creative Production
  → Audio / Voice
```

而不是因为出现一个新功能，就新增一个顶层架构模块。

---

## 3.2 Platform Adaptation Dimension

平台不是第五个 Use Case Family。

当前平台适配方向：

```text
TikTok Skill Pack
Amazon Skill Pack
Temu Skill Pack
Future Platform Skill Pack
```

其作用是：

> **把跨平台业务能力与具体平台规则、平台语境、专业运营方法和业务约束进行组合与适配。**

---

## 3.3 Concrete Workflow

具体业务可以先理解为：

```text
Use Case Family
+
Platform Adaptation
+
Business Context
=
Concrete Workflow
```

例如：

```text
Research
+ TikTok
+ US / Car Vacuum
→ TikTok Car Vacuum Content Research
```

---

## 3.4 Emerging Product Area

当前已经看到：

```text
Platform-specific Operations
```

可能涉及：

- Listing；
- Ads；
- Publishing；
- Creator Collaboration；
- Pricing；
- Store Operations；
- 其他平台运营动作。

但其完整业务结构尚未成熟。

当前状态：

**Emerging Business Need / Detailed Scope Not Yet Defined**

详细 Product Architecture 见：

`docs/01_product/00_PRODUCT_ARCHITECTURE.md`

---

# 4. Current System Architecture / 当前系统架构

System Architecture 只回答：

> **为了支撑 Product Architecture，Ecommerce AI OS 从系统层应该由哪些责任区域组成。**

当前 Candidate 总图：

```text
Product Architecture
        ↓
Applications
        ↓
Skills
        ↓
Stable Core
      ↙        ↘
Capabilities  Foundation Services
      ↘        ↙
        Providers
```

注意：

> **这是一张 Responsibility Map，不是严格 Runtime Call Graph。**

---

## 4.1 Applications

表示用户真正进入系统的产品入口。

未来可能包括：

- Chat；
- Research Workspace；
- Creative Workspace；
- Operator Console；
- Future Applications。

当前详细设计：

**Not Yet Designed**

---

## 4.2 Skills

当前语义：

> **Skill = 业务上怎么做。**

Skill 负责：

- Business Know-how；
- Professional Method；
- Platform Adaptation；
- Domain Rules；
- Composite Business Method。

---

## 4.3 Capabilities

当前语义：

> **Capability = 系统会做什么。**

例如：

- Search；
- Retrieve；
- Analyze；
- Generate Text；
- Generate Image；
- Generate Video；
- Transcribe；
- Translate；
- Future Capability。

---

## 4.4 Providers

当前语义：

> **Provider = 实际提供外部数据、模型、能力或基础设施的一方。**

例如：

- Scrape Creators；
- LLM Provider；
- Image / Video Model Provider；
- Storage Provider；
- Future Provider。

必须区分：

```text
Provider
≠ Adapter / Connector
≠ API / SDK / MCP
```

当前 Candidate 依赖方向：

```text
Capability / Service Contract
        ↓
Provider Resolution
        ↓
Adapter / Connector
        ↓
Concrete Provider
        ↓
API / SDK / MCP / Native Mechanism
```

不新增顶层 Adapter Layer；Provider-specific quirks 由 Adapter / Contract Boundary 优先吸收。

核心边界：

```text
Skill
= 怎么做

Capability
= 能做什么

Provider
= 谁来做
```

---

## 4.5 Stable Core

Stable Core 当前只负责系统级运行规则，不承载 TikTok / Amazon / Short Drama 等具体业务知识。

当前 Stable Core Candidate Areas：

```text
Task Runtime
Skill Extension Mechanism
Capability Contract
Runtime Governance
Execution Record
```

Compatibility 保留为：

```text
Cross-cutting Compatibility / Versioning Concern
```

不再作为独立一级 Stable Core Area。

注意：

```text
Runtime Governance
≠
Architecture Governance
```

六个 Candidate 的详细对象、字段和 Contract：

**Not Yet Designed**

---

## 4.6 Foundation Services

当前 Candidate Foundation Services：

```text
Knowledge
Evidence
Artifact
Future Services
```

Research 仍是 Product Architecture 中的 Use Case Family，但在 System Architecture 中：

```text
Research
→ System Placement Under Review
```

它们是重要系统方向，但详细 Contract 尚未设计。

当前状态：

**Candidate / Detailed Architecture Not Yet Designed**

详细 System Architecture 见：

`docs/02_system/00_SYSTEM_ARCHITECTURE.md`

---

# 5. Current Software Architecture Status / 当前软件架构状态

当前：

# **Software Architecture = Not Yet Designed**

当前仓库中的：

```text
src/ecommerce_ai_os/
├── kernel/
├── capabilities/
├── skills/
├── providers/
├── services/
└── applications/
```

只表示：

> **Project Scaffold / Candidate Package Boundary**

不代表：

> **Approved Software Architecture**

当前尚未正式设计：

- Python package boundary；
- module dependency；
- interface implementation；
- sync / async；
- event / message；
- persistence；
- database；
- API；
- deployment；
- process topology；
- caching / queue；
- schema strategy；
- migration；
- observability；
- security implementation。

必须保持顺序：

```text
Product Requirements
        ↓
Product Architecture
        ↓
System Architecture
        ↓
Software Architecture
        ↓
Code / Schema / Tests
```

详细 Boundary Baseline 见：

`docs/03_software/00_SOFTWARE_ARCHITECTURE.md`

---

# 6. Architecture Governance / 架构治理

Architecture Governance 横向治理：

```text
Project / Requirements
Product Architecture
System Architecture
Software Architecture
Code / Schema / Tests
```

当前统一架构状态模型：

```text
Draft
↓
Candidate
↓
Approved
↓
Implemented
↓
Validated
```

旁支状态：

```text
Rejected
Deprecated
Superseded
```

核心治理原则：

1. 一个问题只有一个 Current Authority；
2. Candidate 不能被 AI / Codex 自动升级为 Approved；
3. 重大架构变化需要 Human Review；
4. 必要时通过 ADR 记录重要决定；
5. Baseline 只做地图，不复制专项设计；
6. 旧文档必须明确 Current / Reference / Superseded 等状态；
7. Code / Schema / Tests 对实现事实有权威；
8. Provider Lab 对 Provider Runtime Facts 有事实权威；
9. 低层实现不能静默推翻 Approved 高层架构；
10. Handoff 是导航，不是 Architecture Authority。

详细治理规则见：

`docs/04_governance/00_ARCHITECTURE_GOVERNANCE.md`

---

# 7. External / Reference Assets

## 7.1 Legacy Architecture

旧 SIG、N01-N18、Track A/B/C 等历史设计不全部丢弃。

当前统一分为：

```text
KEEP AS PRINCIPLE
REFERENCE ONLY
DO NOT INHERIT AS AUTHORITY
```

当前保留的重要原则包括：

- Business Question → Evidence Need；
- Answerability；
- Raw Evidence Preservation；
- Processing Versioning；
- Traceability / Provenance；
- Missing != 0；
- Correlation != Causation；
- Public Signal != Real Business Truth；
- Knowledge Update Requires Human Review。

旧顶层结构不再自动拥有 Ecommerce AI OS Current Authority。

详细审计见：

`docs/05_references/legacy/02_LEGACY_ARCHITECTURE_REFERENCE_AUDIT.md`

---

## 7.2 Scrape Creators Provider Lab

Scrape Creators Provider Lab 是独立的 External Verified Asset。

仓库：

`/Volumes/projects/andy/0810/scrape-creators-provider-lab`

核心边界：

```text
Provider Lab discovers facts.
Ecommerce AI OS consumes and productizes those facts.
```

当前冻结事实摘要：

```text
Current inventoried unique endpoints:
97

Runtime Final Disposition:
92 SUCCESS
5 non-success final dispositions

L0 Runtime Calibration:
92 CONFIRMED
0 CORRECTED
5 UNKNOWN
0 RULE_CONFLICT

UNKNOWN endpoints:
TT-04
TT-09
TT-19
SHOP-02
RD-05

Freeze commit:
1b1c35f
docs: freeze l0 runtime calibration handoff

L2:
PAUSED intentionally
```

注意：

- `97` 是当前 inventory，不代表 Provider 永远只有 97 个 API；
- Runtime `SUCCESS` 和 L0 `CONFIRMED` 是两个不同状态体系；
- Provider API Shape 不允许反向定义 Ecommerce AI OS Architecture。

未来方向：

```text
Ecommerce AI OS
        ↓
Capability / Service Contract
        ↓
Provider Adapter
        ↓
Provider Facts
        ↓
Provider Lab Runtime Evidence
```

详细 Handoff 见：

`docs/05_references/provider_lab/03_PROVIDER_LAB_ASSET_HANDOFF.md`

---

# 8. Repository Information Architecture / 当前仓库信息架构

当前 Documentation Architecture：

```text
docs/
├── 00_project/
│   ├── 00_PROJECT_BASELINE_V0.1.md
│   ├── 01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md
│   └── 02_CURRENT_HANDOFF.md
│
├── 01_product/
│   └── 00_PRODUCT_ARCHITECTURE.md
│
├── 02_system/
│   ├── 00_SYSTEM_ARCHITECTURE.md
│   ├── kernel/
│   ├── capabilities/
│   ├── skills/
│   ├── services/
│   └── providers/
│
├── 03_software/
│   └── 00_SOFTWARE_ARCHITECTURE.md
│
├── 04_governance/
│   ├── 00_ARCHITECTURE_GOVERNANCE.md
│   └── decisions/
│
└── 05_references/
    ├── legacy/
    │   └── 02_LEGACY_ARCHITECTURE_REFERENCE_AUDIT.md
    └── provider_lab/
        └── 03_PROVIDER_LAB_ASSET_HANDOFF.md
```

各层职责：

```text
00_project
→ 为什么做、当前状态、项目交接

01_product
→ 用户能做什么

02_system
→ 系统由什么组成

03_software
→ 系统如何落成软件

04_governance
→ 架构如何被批准、修改、废弃

05_references
→ 历史设计与外部事实资产
```

---

# 9. Current Design Principles / 当前设计原则

当前项目级设计原则：

```text
Stable Core
+
Extensible Capability
+
Replaceable Provider
+
Pluggable Skill
```

同时保留：

> **Business-first**

> **Technology-neutral**

> **Architecture big, implementation small**

> **Provider facts must not dictate OS architecture**

> **Unknown future use cases must remain possible without assuming they are already known**

---

# 10. Current Project Status / 当前项目状态

## 10.1 已建立的 Baseline 文档

当前已经形成工作基线：

```text
Product Origin & Requirements
Product Architecture
System Architecture
Software Architecture Boundary Baseline
Architecture Governance
Legacy Architecture Reference Audit
Provider Lab Asset Handoff
```

这些文档仍需要最终一致性审核。

---

## 10.2 Candidate Architecture

当前 System Architecture 中的主要 Candidate：

```text
Applications
Skills
Stable Core
Capabilities
Foundation Services
Providers
```

Stable Core Candidate Areas：

```text
Task Runtime
Skill Extension Mechanism
Capability Contract
Runtime Governance
Execution Record
```

Cross-cutting：

```text
Compatibility / Versioning
```

Candidate Foundation Services：

```text
Knowledge
Evidence
Artifact
```

Research：

```text
System Placement Under Review
```

---

## 10.3 Not Yet Designed

当前明确未设计：

- Task Runtime internal contract；
- Advanced Runtime Concerns：Checkpoint Strategy、Crash Recovery、Durable Execution、Retry Engine；
- Skill Extension Contract details；
- Capability Invocation Schema；
- Provider Resolution；
- Runtime Governance rules；
- Execution Record schema；
- Cross-cutting Compatibility rules；
- Foundation Service contracts；
- Agent architecture；
- Software package design；
- Database；
- Persistence；
- Event / Message；
- API；
- UI / Workspace；
- Deployment；
- RAG / Retrieval implementation；
- Vector DB；
- detailed multimodal implementation。

---

# 11. Current Development Boundary / 当前开发边界

当前阶段仍然是：

# **Architecture Baseline / Handoff Preparation**

当前不进入：

- Production Agent；
- Multi-Agent；
- Production RAG；
- Vector Database；
- Production Database；
- Frontend UI；
- 97 API 全量正式接入；
- Production Provider Routing；
- TikTok / Amazon / Temu Professional Skill 全量实现；
- Production Image / Video Pipeline；
- Platform-specific Operations 全量实现。

当前主要任务是：

> **在 Human Review 接受 C01-C09、C10 继续 DEFER 的基础上，维护 Current Candidate Architecture 的边界一致性。**

---

# 12. Current Next Step / 当前下一步

当前建议顺序：

```text
1. 审核 Project Baseline
        ↓
2. 对全部 Baseline / Reference 文档做一致性审核
        ↓
3. 修复交叉引用、路径和状态冲突
        ↓
4. 生成 docs/00_project/02_CURRENT_HANDOFF.md
        ↓
5. 冻结当前 Handoff Package
        ↓
6. 新聊天继续专项 System Architecture Audit
```

进入新聊天后，不应重新设计已经完成的 Product / Documentation 层级。

新的专项设计应从当前 System Architecture Candidate 继续。

---

# 13. Current Authority Documents

当前项目应优先阅读：

```text
docs/00_project/00_PROJECT_BASELINE_V0.1.md

docs/00_project/01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md

docs/01_product/00_PRODUCT_ARCHITECTURE.md

docs/02_system/00_SYSTEM_ARCHITECTURE.md

docs/03_software/00_SOFTWARE_ARCHITECTURE.md

docs/04_governance/00_ARCHITECTURE_GOVERNANCE.md

docs/05_references/legacy/02_LEGACY_ARCHITECTURE_REFERENCE_AUDIT.md

docs/05_references/provider_lab/03_PROVIDER_LAB_ASSET_HANDOFF.md
```

新聊天的启动入口最终由：

`docs/00_project/02_CURRENT_HANDOFF.md`

负责。

但：

> **CURRENT_HANDOFF 是导航入口，不是 Architecture Authority。**

---

# 14. Human Review Gate

当前文档状态：

# **Draft for Human Review**

批准本文件只代表：

> **当前 Ecommerce AI OS 的项目身份、产品架构摘要、系统架构摘要、软件架构状态、治理边界、外部资产、当前项目状态和下一步，被接受为当前 Project Baseline。**

批准本文件不代表：

- Candidate Architecture 自动升级为 Approved；
- Stable Core 内部设计已经批准；
- Foundation Service Contract 已经批准；
- Software Architecture 已经完整设计；
- Agent / DB / UI 已批准；
- 可以开始全面实现。
