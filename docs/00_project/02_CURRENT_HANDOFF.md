# Ecommerce AI OS — Current Handoff

- **文档类型**：Current Handoff / 新聊天交接入口
- **项目**：Ecommerce AI OS
- **项目仓库**：`/Volumes/projects/andy/0813/ecommerce-ai-os`
- **当前阶段**：Architecture Baseline / Handoff Preparation
- **最后更新**：2026-08-14
- **重要说明**：本文件是导航入口，不是 Architecture Authority

---

## 0. 这份文档怎么用

如果你是一个新的 ChatGPT / Codex 会话，接手这个项目时：

> **不要从聊天历史猜项目，不要重新设计顶层架构。**

先按照本文件给出的阅读顺序读取当前 Authority / Baseline 文档，再继续下一项工作。

如果本文件与正式 Product / System / Software / Governance 文档冲突：

> **以对应层级的 Current Authority 文档为准。**

本文件只负责：

- 告诉新会话项目现在是什么；
- 先读哪些文件；
- 当前哪些结论已经形成工作基线；
- 哪些内容仍是 Candidate；
- 哪些内容明确 Not Yet Designed；
- Provider Lab 当前冻结到哪里；
- 当前禁止做什么；
- 下一项工作是什么。

---

# 1. Project Identity

项目名称：

# **Ecommerce AI OS**

当前方向：

> **构建一个面向跨境电商、长期可扩展的 AI-native 工作系统。**

项目不是从“先做一个 AI OS”开始的。

真实演变大致是：

```text
TikTok 内容生产问题
↓
寻找参考视频
↓
发现只找爆款不足以指导高质量内容
↓
Research 扩张
↓
发现 Research 可以跨平台复用
↓
需要跨来源数据与 Evidence
↓
Creative Production 扩张
↓
Knowledge 复用
↓
Experiment & Validation
↓
专业运营 Skill 会持续变化
↓
需要稳定但可扩展的 Ecommerce AI OS
```

核心长期原则：

```text
Stable Core
+
Extensible Capability
+
Replaceable Provider
+
Pluggable Skill
```

同时保持：

- Business-first；
- Technology-neutral；
- Architecture big, implementation small；
- Provider facts must not dictate OS architecture；
- Unknown future use cases must remain possible。

---

# 2. 必须先读的文件

新会话进入项目后，按下面顺序读取。

## 2.1 项目与需求

```text
docs/00_project/00_PROJECT_BASELINE_V0.1.md
docs/00_project/01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md
```

作用：

- 理解项目是什么；
- 理解为什么会从 TikTok 内容问题演变成 Ecommerce AI OS；
- 理解当前需求边界和非目标。

---

## 2.2 Product Architecture

```text
docs/01_product/00_PRODUCT_ARCHITECTURE.md
```

只回答：

> 用户能拿这个 OS 做什么。

当前主要产品结构：

```text
Cross-platform Use Case Families
├── Research
├── Creative Production
├── Knowledge-assisted Work
└── Experiment & Validation

Platform Adaptation Dimension
├── TikTok Skill Pack
├── Amazon Skill Pack
├── Temu Skill Pack
└── Future Platform Skill Pack
```

具体业务：

```text
Use Case Family
+
Platform Adaptation
+
Business Context
=
Concrete Workflow
```

当前 `Platform-specific Operations` 仍然是 Emerging Product Area，不要提前假装完整业务结构已经设计好。

---

## 2.3 System Architecture

```text
docs/02_system/00_SYSTEM_ARCHITECTURE.md
```

只回答：

> 为了支撑 Product Architecture，系统由什么职责区域组成。

当前 Candidate Responsibility Map：

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

这不是严格 Runtime Call Graph。

---

## 2.4 Software Architecture

```text
docs/03_software/00_SOFTWARE_ARCHITECTURE.md
```

当前状态：

# **Not Yet Designed**

现有：

```text
src/ecommerce_ai_os/
├── kernel/
├── capabilities/
├── skills/
├── providers/
├── services/
└── applications/
```

只是：

> **Project Scaffold / Candidate Package Boundary**

不要用现有空目录反推 System Architecture。

---

## 2.5 Architecture Governance

```text
docs/04_governance/00_ARCHITECTURE_GOVERNANCE.md
```

重点理解：

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

旁支：

```text
Rejected
Deprecated
Superseded
```

必须遵守：

> **AI / Codex 无权自行把 Candidate 升级为 Approved。**

以及：

```text
Architecture Governance
≠
Runtime Governance
```

---

## 2.6 Reference Assets

旧架构审计：

```text
docs/05_references/legacy/02_LEGACY_ARCHITECTURE_REFERENCE_AUDIT.md
```

Provider Lab 交接：

```text
docs/05_references/provider_lab/03_PROVIDER_LAB_ASSET_HANDOFF.md
```

---

# 3. 当前 Product Architecture 基线

当前跨平台 Use Case Families：

```text
Research
Creative Production
Knowledge-assisted Work
Experiment & Validation
```

注意：

> Current Product Families 不是永久固定模块。

未来真实业务出现后，可以增加新的子能力，也可以在满足“独立、跨平台、完整用户工作”的条件下提出新的 Candidate Product Family。

例如：

```text
AI Voiceover
→ Creative Production
  → Audio / Voice
```

而不是为每个新 AI 功能新建顶层模块。

Platform Skill Pack 是第二维度，而不是第五个 Product Family。

---

# 4. 当前 System Architecture 基线

当前系统层的主要 Candidate：

```text
Applications
Skills
Stable Core
Capabilities
Foundation Services
Providers
```

核心语义：

```text
Skill
= 业务上怎么做

Capability
= 系统会做什么

Provider
= 具体由谁实现 / 通过谁访问
```

---

# 5. Stable Core 当前 Candidate

当前 Stable Core 六个 Candidate Areas：

```text
Task Runtime
Extension Runtime
Capability Contract
Runtime Governance
Execution Record
Compatibility
```

注意：

> 这六个只是 Candidate Areas。

当前没有批准：

- 内部对象；
- 字段；
- Schema；
- Runtime contract；
- 具体 interface；
- storage；
- state model。

特别注意：

```text
Runtime Governance
≠
Architecture Governance
```

Runtime Governance 未来处理：

- Permission；
- Policy；
- Human Gate；
- Cost Gate；
- Risk Gate。

Architecture Governance 处理：

- Draft / Candidate / Approved；
- ADR；
- Architecture Change；
- Superseded；
- Authority。

---

# 6. Foundation Services 当前 Candidate

当前候选：

```text
Knowledge
Evidence
Research
Artifact
```

状态：

> **Candidate / Detailed Architecture Not Yet Designed**

当前不要直接继承旧 SIG 对象作为正式新 Contract。

---

# 7. Agent / MCP / RAG / Embedding / Vector DB 当前定位

当前没有：

```text
Agent Layer
```

作为顶层 System Architecture。

当前理解：

```text
Agent
→ Execution / Decision Strategy

MCP
→ Integration / Capability Access Mechanism

RAG
→ Knowledge Retrieval Pattern

Embedding
→ Semantic Representation Technique

Vector DB
→ Storage / Retrieval Implementation

LLM / Multimodal Model
→ Capability / Provider Implementation

Chat
→ Application / Interaction Surface
```

以上都不应因为当前流行就直接升级成顶层架构。

---

# 8. Legacy Architecture 当前边界

旧架构统一三分：

```text
KEEP AS PRINCIPLE
REFERENCE ONLY
DO NOT INHERIT AS AUTHORITY
```

当前主要保留原则：

- Business Question → Evidence Need；
- Answerability；
- Allowed Statement / Prohibited Overclaim；
- Raw Evidence Preservation；
- Processing Versioning；
- Traceability / Provenance；
- Missing != 0；
- Correlation != Causation；
- Public Signal != Real Business Truth；
- Knowledge Update Requires Human Review。

可以参考但不直接继承的旧对象：

```text
CollectionRun
QueryExecution
RawDataset / RawRecord
ProcessingRun
MarketSignalReport
ResearchBasis
ResearchTask
Signal Layer
EvidenceComparison / ConflictFinding
```

不再继承为顶层权威：

```text
SIG-P0 → SIG-P6
N01 → N18
Track A / B / C
NormalizedVideoSignal as universal object
MarketSignalReport as universal OS output
TikTok / Video-first top-level architecture
旧目录结构
旧 cross-track message architecture
```

---

# 9. Scrape Creators Provider Lab 当前冻结事实

独立仓库：

`/Volumes/projects/andy/0810/scrape-creators-provider-lab`

定位：

```text
Provider Lab discovers facts.
Ecommerce AI OS consumes and productizes those facts.
```

当前 inventoried unique endpoints：

```text
97
```

注意：

> 97 是当前 inventory，不代表 Scrape Creators 永远只有 97 个 API。

当前 Runtime Final Disposition：

```text
92 SUCCESS

1 BLOCKED_PROVIDER
→ TT-19

1 BLOCKED_RESOURCE_UNAVAILABLE
→ TT-09

3 BLOCKED_SEED_UNDISCOVERABLE
→ TT-04
→ SHOP-02
→ RD-05
```

当前 L0 Runtime Calibration：

```text
92 CONFIRMED
0 CORRECTED
5 UNKNOWN
0 RULE_CONFLICT
```

UNKNOWN：

```text
TT-04
TT-09
TT-19
SHOP-02
RD-05
```

注意：

```text
Runtime SUCCESS
≠
L0 CONFIRMED
```

当前冻结 Commit：

```text
1b1c35f
docs: freeze l0 runtime calibration handoff
```

当前：

```text
L2 = PAUSED intentionally
```

原因：

> Ecommerce AI OS 正在先定义自己的 Capability / Service / Provider Boundary，不能让 Provider response schema 反向定义 OS。

正确未来方向：

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

---

# 10. 当前 Documentation Architecture

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
    └── provider_lab/
```

顶层分类已经确定。

不要在新聊天里重新恢复旧的：

LEGACY / DEPRECATED PATHS — DO NOT USE

以下路径仅用于记录已经废弃的旧 Documentation Architecture。
它们不是 Current Path，不得作为文件引用、导航路径或新设计目标。

```text
docs/01_kernel
docs/02_capabilities
docs/03_skills
docs/04_services
docs/decisions
```

这些旧顶层目录已经被 Documentation Architecture 重构取代。

---

# 11. 当前明确 Not Yet Designed

以下内容不要假装已经有答案：

```text
Task Runtime internal contract
Context model
Skill Contract details
Skill Composition details
Capability Contract details
Provider Resolution
Runtime Governance rules
Execution Record schema
Compatibility rules
Foundation Service contracts
Agent architecture
Python package design
Database
Persistence
Event / Message
API
UI / Workspace
Deployment
RAG / Retrieval implementation
Vector DB
Detailed multimodal implementation
Platform-specific Operations final structure
```

---

# 12. 当前禁止事项

新聊天接手后，当前不要：

- 重新设计 Documentation Architecture；
- 重新把 TikTok / Amazon / Temu 切成三套独立系统；
- 把 Script / Image / Video / Short Drama 当成 TikTok 专属能力；
- 把 Provider API Shape 当成 OS Domain Model；
- 把旧 SIG / N01-N18 自动恢复为 Current Authority；
- 把 Agent / MCP / RAG / Vector DB 提升为顶层架构；
- 从现有 `src/` scaffold 反推 Software Architecture；
- 一次开发全部 97 API；
- 开始 Production DB / UI / Agent / RAG；
- 自动把 Candidate 升成 Approved；
- 未经 Human Review 大规模修改顶层架构。

---

# 13. 当前开发哲学

保持：

> **Architecture big, implementation small.**

含义：

- 架构允许给未来留扩展空间；
- 实现必须从窄的真实业务闭环开始；
- 不因为愿景很大就一次实现所有模块；
- 新需求先判断是否能进入已有 Family / Skill / Capability / Service；
- 只有真实需求证明当前抽象不足时，才修改更高层架构。

---

# 14. 当前工作状态

当前已完成 / 已生成的 Baseline Package：

```text
00_PROJECT_BASELINE_V0.1.md

01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md

00_PRODUCT_ARCHITECTURE.md

00_SYSTEM_ARCHITECTURE.md

00_SOFTWARE_ARCHITECTURE.md

00_ARCHITECTURE_GOVERNANCE.md

02_LEGACY_ARCHITECTURE_REFERENCE_AUDIT.md

03_PROVIDER_LAB_ASSET_HANDOFF.md

02_CURRENT_HANDOFF.md
```

这些文档在正式换聊天前应完成：

> **Final Consistency Audit**

重点检查：

- 路径；
- 状态；
- Candidate / Approved 语义；
- Runtime Governance 命名；
- Product / System / Software 边界；
- Legacy / Provider Lab Authority；
- 交叉引用；
- README / AGENTS 是否需要同步最小导航信息。

---

# 15. Git 状态

本文件不写死当前 Ecommerce AI OS 的最新 Commit Hash。

原因：

> Final Handoff Package 尚需完成一致性审核和最后一次 Git Freeze。

新聊天开始前或最终 Freeze 时，必须由 Codex / Git 真实检查：

```bash
git status --short
git log -1 --oneline
```

不要从旧聊天或本文件猜当前 HEAD。

Provider Lab 的独立冻结锚点仍为：

```text
1b1c35f
docs: freeze l0 runtime calibration handoff
```

---

# 16. 下一项唯一任务

当前下一步不是立即开始实现。

下一项任务：

# **Final Baseline Consistency Audit**

审核对象：

```text
docs/00_project/00_PROJECT_BASELINE_V0.1.md
docs/00_project/01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md
docs/01_product/00_PRODUCT_ARCHITECTURE.md
docs/02_system/00_SYSTEM_ARCHITECTURE.md
docs/03_software/00_SOFTWARE_ARCHITECTURE.md
docs/04_governance/00_ARCHITECTURE_GOVERNANCE.md
docs/05_references/legacy/02_LEGACY_ARCHITECTURE_REFERENCE_AUDIT.md
docs/05_references/provider_lab/03_PROVIDER_LAB_ASSET_HANDOFF.md
docs/00_project/02_CURRENT_HANDOFF.md
```

审核通过并 Freeze 后：

> **换新聊天继续 System Architecture 专项审计。**

优先从当前 Stable Core Candidate / System Boundary 继续，而不是重新讨论 Product / Documentation 顶层结构。

---

# 17. 新聊天启动提示

建议新聊天第一条使用：

```text
继续 Ecommerce AI OS。

项目路径：

/Volumes/projects/andy/0813/ecommerce-ai-os

先完整阅读：

docs/00_project/02_CURRENT_HANDOFF.md

然后按照 Handoff 中的顺序读取当前 Authority / Baseline 文档。

不要重新设计 Documentation Architecture。
不要重新定义 Product Architecture。
不要把 Candidate 自动升级为 Approved。
不要从旧 SIG / N01-N18 恢复旧顶层架构。
不要从 src scaffold 反推 Software Architecture。
不要让 Provider API Shape 定义 Ecommerce AI OS。

当前先基于仓库真实状态做审计，再继续 Handoff 指定的下一项 System Architecture 工作。
```

---

# 18. Handoff Authority Boundary

再次明确：

> **CURRENT_HANDOFF 是导航，不是 Architecture Authority。**

当内容冲突时：

```text
Product 问题
→ Product Architecture

System 问题
→ System Architecture

Software 问题
→ Software Architecture

Architecture State / Change
→ Architecture Governance

Provider Runtime Fact
→ Provider Lab

Implementation Fact
→ Code / Schema / Tests
```

不要让 Handoff 自己演变成第二份“大一统架构文档”。
