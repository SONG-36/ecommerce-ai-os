# Ecommerce AI OS — 项目基线 V0.1

- **版本**：V0.1
- **状态**：Draft for Human Review / 待人工审阅
- **文档权威级别**：Current Project Baseline / 当前项目总基线
- **项目名称**：Ecommerce AI OS
- **项目仓库**：`/Volumes/projects/andy/0813/ecommerce-ai-os`
- **当前阶段**：Architecture Baseline / Project Scaffold
- **最后更新**：2026-08-13
- **批准状态**：Pending Human Review / 待人工确认

---

## 0. 文档目的

这份文档是 **Ecommerce AI OS 当前阶段的顶层项目地图**。

它主要回答：

> **我们现在到底在做什么？**

它负责记录：

- 项目身份与目标；
- 当前范围与非目标；
- 当前已经形成的设计原则；
- 当前候选架构；
- 架构成熟度；
- 仓库信息架构；
- 与已有外部项目和资产的关系；
- 当前架构审计顺序；
- 仍未设计或未冻结的部分。

这份文档 **不会** 冻结详细 Schema、字段、具体工作流、Agent 拓扑、数据库、UI、具体框架、Provider 实现或 Skill 内部业务逻辑。

---

## 1. 项目身份

项目名称：

# **Ecommerce AI OS**

当前产品方向：

> **构建一个面向跨境电商、长期可扩展的 AI-native 工作系统。**

系统需要能够逐步承载：

- 不同电商平台；
- 不同运营角色；
- 不同研究方法；
- 不同内容生产流程；
- 不同 AI 能力；
- 不同 Provider；
- 不同专业 Skills；
- 以及未来现在还没有想到的新业务。

目标不是每出现一个新需求，就重新设计整个系统。

当前已知需求不应该按照“TikTok / Amazon / Temu”直接切成三套互相独立的系统。

目前更适合区分两个维度：

1. 跨平台可复用的业务能力 / Use Case Families；
2. 针对具体平台进行组合和适配的 Platform Skill Packs。

## 1.1 已知业务方向总览

当前工作模型如下：

```text
Ecommerce AI OS
│
├── Research / 研究
│   ├── 市场研究
│   ├── 用户研究
│   ├── 产品 / 竞品研究
│   └── 内容研究
│
├── Creative / 内容与创意生产
│   ├── Script / 剧本
│   ├── Product Image / 产品图
│   ├── Video / 视频
│   ├── Short Drama / 短剧
│   └── Director / Shot Planning / Editing
│
├── Knowledge / 知识
│
├── Experiment & Validation / 实验与验证
│
└── Platform Skill Packs / 平台专项 Skill Pack
    ├── TikTok
    ├── Amazon
    ├── Temu
    └── Future
```

这里需要特别区分：
• Research、Creative、Knowledge、Experiment & Validation 表示跨平台可复用的业务能力方向；
• Platform Skill Packs 表示针对具体平台，把通用能力、平台规则、专业运营方法和业务 Context 进行组合与适配；
• Script、Product Image、Video、Short Drama 等能力不属于 TikTok 独占能力；
• TikTok Skill Pack 可以组合 Research、Script、Short Drama、Video、Validation 等能力；
• Amazon Skill Pack 也可以组合 Research、Product Image、Product Video、Review Analysis 等能力；
• Temu 和未来其他平台同理；
• 当前没有假设 TikTok、Amazon、Temu 的专业运营方法已经设计完成，专业 Skill 后续仍需真实运营经验补充。

Status: Known Use Case Direction / Detailed Composition Not Yet Designed

当前已知跨平台业务能力方向：
- Research / 研究；
- Creative / 内容与创意生产；
- Knowledge / 知识；
- Experiment & Validation / 实验与验证；
- Future Business Capabilities / 未来业务能力。

当前已知平台专项扩展方向：
- TikTok Skill Pack；
- Amazon Skill Pack；
- Temu Skill Pack；
- Future Platform Skill Pack。

这些只是 Use Case Directions，不代表：
- 已经设计完成；
- 已经形成正式 Skill Contract；
- 已经批准实现；
- 已经掌握各平台完整专业运营方法。

---

## 2. 为什么要重新设计这个项目

这个项目一开始并不是为了做一个通用 AI 平台。

最初只是一个非常具体的跨境电商问题：

> **输入自己的商品信息，去 TikTok 搜索一些参考视频，再根据参考视频辅助自己拍摄带货内容。**

这个人工流程实际上跑通过。

但在真实业务中逐渐发现：

> **只找到爆款参考视频，并不足以保证自己能拍出好的内容。**

想拍出真正有差异化、适合美区用户的内容，还需要理解：

- 市场环境；
- 产品本身；
- 用户需求；
- 用户痛点；
- 竞品；
- 美国文化；
- 美国用户语言表达；
- 内容表达方式；
- 评论与评价；
- 平台行为；
- 自己发布后的真实业务结果。

于是问题从：

```text
找 TikTok 参考视频
```

逐渐扩大为：

```text
Market Research / 市场研究
```

之后又进一步发现，研究能力并不只对 TikTok 运营有用。Amazon、Temu 以及未来其他跨境电商运营，同样可能需要跨多个平台寻找和分析用户需求、痛点、趋势、竞品、评论、文化、内容、商品、广告、创作者和市场信号。

与此同时，新的 AI 业务需求也不断出现，例如：

- AI 写剧本；
- AI 做产品图；
- AI 生成视频；
- AI 做短剧；
- 婆媳类短剧；
- 爽剧；
- 龙傲天 / 爽文类带货；
- Director / Shot Planner；
- 视频生成执行；
- 剪辑；
- 未来专业运营 Skills。

因此，TikTok 单一工具已经太窄；Evidence Platform 或 Research Platform 也不足以代表最终系统。

当前项目因此升级为：

# **Ecommerce AI OS**

更完整的项目思路演变和业务需求，单独维护在：

`01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md`

---

## 3. Ecommerce AI OS 不是什么

当前 Ecommerce AI OS 不等于以下任何一个单独产品或技术：

- TikTok 单一工具；
- Amazon 单一工具；
- Temu 单一工具；
- Evidence Platform 本身；
- Research Platform 本身；
- Agent Demo；
- Multi-Agent Demo；
- RAG Demo；
- MCP Demo；
- Vector Database 项目；
- AI 图片生成器；
- AI 视频生成器；
- 短剧生成器；
- 单一 Workflow Engine；
- 纯聊天机器人；
- 对人工运营的直接替代。

这些未来都可能成为 OS 上面的 Application、Foundation Service、Capability、Provider、Skill 或某种实现技术，但它们不能单独定义整个 OS。

---

## 4. 架构状态词汇

### 4.1 Current Design Principle / 当前设计原则

表示当前已经接受为项目级方向，后续设计不能随意违背。

### 4.2 Candidate Architecture / 候选架构

表示已经值得进入正式架构审计，但还没有完全冻结。名称、边界、对象、字段、关系和实现方式都可能继续调整。

### 4.3 Not Yet Designed / 尚未设计

表示已经知道存在这个问题，但目前没有批准任何具体架构。系统必须给未来保留空间，但不能假装已经有答案。

---

# 5. 当前核心设计原则

## 5.1 Stable Core / 稳定核心

**状态：Current Design Principle**

系统需要有一个相对稳定的核心。这个核心负责系统级规则和运行秩序，而不是某个平台的具体运营玩法。

Stable Core 应该在 TikTok、Amazon、Temu、AI 模型、Agent Framework、MCP、Provider 或专业运营方法变化后仍然成立。

---

## 5.2 Extensible Capability / 可扩展能力

**状态：Current Design Principle**

上层业务不应该直接绑定某一个具体 Provider。

例如：

```text
Generate Video
```

是 Capability。

而：

```text
即梦
Kling
Sora
Future Provider
```

是具体实现。

Skill 应该表达“我需要视频生成能力”，而不是写死“我必须调用即梦”。

---

## 5.3 Replaceable Provider / 可替换 Provider

**状态：Current Design Principle**

Provider 表示某个 Capability 的具体实现者、数据来源或访问方式。

未来 Provider 可能包括：

- Scrape Creators；
- LLM Provider；
- 图片生成 Provider；
- 视频生成 Provider；
- 文件存储 Provider；
- MCP Server；
- API；
- SDK；
- 未来其他外部服务。

Provider 应该能够被替换。Provider 的特殊字段、限制和 quirks，不应该自动污染 Ecommerce AI OS 的上层通用语义。

---

## 5.4 Pluggable Skill / 可挂载 Skill

**状态：Current Design Principle**

具体业务方法和专业经验应该尽量进入 Skill，而不是写死到 Stable Core。

未来 Skill 可能包括：

- Generic Skill；
- Commerce Skill；
- TikTok Skill；
- Amazon Skill；
- Temu Skill；
- Research Skill；
- Script Skill；
- Director Skill；
- Shot Planner Skill；
- Short Drama Skill；
- 专业运营 Skill；
- 第三方 Skill；
- 公司内部沉淀出来的新 Skill。

当前必须承认：很多专业运营方法还没有真正进入系统。因此当前架构不能把现在基于碎片信息整理出来的方法，误认为是最终专业方法，然后硬编码进 Core。

---

# 6. 当前顶层工作模型

**状态：Candidate Architecture**

```text
┌──────────────────────────────────────┐
│                Skills                │
│ Generic / Commerce / Platform /      │
│ Composite / Future Professional      │
│ Skills                               │
├──────────────────────────────────────┤
│             Stable Core              │
│ 系统级执行、扩展、治理、记录、兼容规则 │
├──────────────────────────────────────┤
│            Capabilities              │
│ Search / Analyze / Generate /        │
│ Image / Video / Files / Future       │
├──────────────────────────────────────┤
│              Providers               │
│ APIs / Models / MCP / SDKs /         │
│ External Services / Future Providers │
└──────────────────────────────────────┘
```

这个图只是 Working Abstraction，不是最终实现图。

---

# 7. Stable Kernel 当前候选职责

**状态：Candidate Architecture**

目前第一次 Kernel 审计形成了 6 个候选职责：

1. Task Runtime
2. Extension Runtime
3. Capability Contract
4. Governance
5. Execution Record
6. Compatibility

这些名称已经进入正式审计范围，但内部对象、字段、关系、接口尚未批准。

### 7.1 Task Runtime

候选关注点：Task、Context Envelope、State、Checkpoint、pause / resume、长任务状态恢复。

**详细对象和字段：Not Yet Designed**

### 7.2 Extension Runtime

候选关注点：Skill Contract、Extension Contract、Extension Point、Skill Composition、Dependency Handling、Context Binding、Adaptation Mechanism。

当前方向：Skill 的适配机制可能属于 Core，但某个商品如何适配某个短剧、TikTok、Amazon 的具体业务规则，不属于 Core。

**详细架构：Not Yet Designed**

### 7.3 Capability Contract

候选关注点：Skill 如何声明所需 Capability、Capability Interface、Capability Resolution、Capability 与 Provider 的边界、Provider 替换原则。

**详细 Contract：Not Yet Designed**

### 7.4 Governance

候选关注点：Permission、Policy Enforcement、Approval、Human Gate、Cost Boundary、Risk Boundary。

**详细 Governance Model：Not Yet Designed**

### 7.5 Execution Record

候选关注点：Run、Artifact Reference、Provenance、Trace Reference、执行版本、可追溯性、可复现上下文。

**详细对象模型：Not Yet Designed**

### 7.6 Compatibility

候选关注点：Contract Version、Skill Version、Capability Version、Provider Version、Compatibility、Migration、Deprecation。

**详细版本和迁移策略：Not Yet Designed**

---

# 8. Kernel 边界原则

**状态：Current Design Principle under continued audit**

Kernel 不能变成“所有通用功能的大合集”。

某个东西是否进入 Kernel，要看它是不是跨平台、Skill、Provider、AI 模型、Agent 和业务场景都仍然必须存在的系统级规则。

当前预计不直接进入 Kernel 本体的重要组件包括：

- Knowledge Base；
- Evidence System；
- Research System；
- Provider Registry 的具体实现；
- Artifact Storage 的具体实现；
- LLM；
- Agent；
- RAG；
- Embedding；
- Vector Database；
- MCP；
- Chat UI；
- Workflow UI。

这些可能属于 Foundation Service、Capability、Provider、Application 或具体技术实现。

---

# 9. Knowledge / Evidence / Research 的位置

**状态：Important Requirement / Architecture Not Yet Designed**

Knowledge、Evidence、Research 仍然是 Ecommerce AI OS 未来非常重要的组成部分，但不再默认等于整个系统本身。

当前方向：

```text
Knowledge
→ 指导工作与研究

Research
→ 为问题寻找新的数据和证据

Evidence
→ 支撑 Finding、判断和决策

Reviewed Evidence
→ 可以挑战旧知识，也可以产生 Knowledge Update Candidate
```

原则：

- Knowledge guides research；
- 旧知识不能自动压过新的真实 Evidence；
- 新 Evidence 也不能自动修改正式 Knowledge；
- 正式知识更新预计仍需要 Evidence → Candidate → Human Review → Approved Knowledge Update。

新的 Knowledge / Evidence / Research 具体架构：

**Not Yet Designed**

---

# 10. 已验证的外部 Provider 资产

**状态：Existing Verified External Asset**

当前 Ecommerce AI OS 已经有一个独立上游项目：

# **Scrape Creators Provider Lab**

独立仓库路径：

`/Volumes/projects/andy/0810/scrape-creators-provider-lab`

Provider Lab 的职责是：

> **发现并验证 Scrape Creators 这个 Provider 到底真实支持什么。**

它不负责决定 Ecommerce AI OS 应该长什么样。

当前高价值资产包括：

- 97 API Inventory；
- Runtime Reconnaissance；
- Endpoint Execution Evidence；
- Request / Response Observations；
- Seed Registry；
- Identity Findings；
- Runtime Final Disposition；
- L0 Runtime Calibration。

当前冻结结果：

```text
97 API Inventory

Runtime Final Disposition:
92 SUCCESS
5 non-success final dispositions

L0 Runtime Calibration:
CONFIRMED 92
CORRECTED 0
UNKNOWN 5
RULE_CONFLICT 0
```

当前 5 个 non-success / UNKNOWN 相关 Endpoint：

```text
TT-04
TT-09
TT-19
SHOP-02
RD-05
```

当前 L0 Freeze Commit：

```text
1b1c35f
docs: freeze l0 runtime calibration handoff
```

目前 Provider Lab 的 L2 暂停。原因不是 Provider Lab 失败，而是 Ecommerce AI OS 正在重新定义自己的 Capability、Domain 和 Platform Boundary。

正确关系：

```text
Ecommerce AI OS
        ↓
Capability Contract
        ↓
Provider Adapter
        ↓
Scrape Creators Provider Facts
```

而不是：

```text
97 APIs
↓
反推出整个 Ecommerce AI OS
```

详细 Provider Lab 状态维护在：

`03_PROVIDER_LAB_ASSET_HANDOFF.md`

---

# 11. Legacy Architecture / 旧架构定位

**状态：Legacy Reference Only**

之前已经积累了大量设计工作，包括：

- SIG Market Signal Architecture；
- Business Question → Evidence Need；
- Raw / Processing / Normalized；
- ResearchBasis；
- MarketSignalReport；
- Knowledge Feedback；
- N01-N18；
- Track A / B / C；
- TikTok Video-oriented Signal Design。

这些内容不全部丢弃，但也不再自动拥有 Ecommerce AI OS 的最高架构权威。

后续旧设计统一进入三类：

```text
KEEP AS PRINCIPLE
REFERENCE ONLY
DO NOT INHERIT AS AUTHORITY
```

当前预计保留为原则：

- Business Question → Evidence Need；
- Raw Evidence Preservation；
- Processing Versioning；
- Traceability；
- Missing != 0；
- Correlation != Causation；
- Public Signal != Real Conversion Truth；
- Knowledge Update Requires Review。

可继续作为 Reference Only 的旧对象包括：

```text
CollectionRun
QueryExecution
ProcessingRun
MarketSignalReport
ResearchBasis
```

当前不能自动继承为最高架构权威的包括：

```text
SIG-P0 → P6
N01-N18
Track A / B / C
NormalizedVideoSignal 作为通用核心对象
TikTok Video-first 的整体架构
```

详细 Legacy Audit 维护在：

`02_LEGACY_ARCHITECTURE_REFERENCE_AUDIT.md`

---

# 12. Repository Information Architecture / 仓库信息架构

```text
ecommerce-ai-os/
│
├── docs/
│   ├── 00_system_baseline/
│   ├── 01_kernel/
│   ├── 02_capabilities/
│   ├── 03_skills/
│   ├── 04_services/
│   └── decisions/
│
├── src/
│   └── ecommerce_ai_os/
│       ├── kernel/
│       ├── capabilities/
│       ├── skills/
│       ├── providers/
│       ├── services/
│       └── applications/
│
├── tests/
├── examples/
└── pyproject.toml
```

### `docs/00_system_baseline/`

负责整个 OS 的总基线、项目身份、来源、当前全局架构、状态、旧架构处理、Provider Lab 资产交接和新聊天 Handoff。

### `docs/01_kernel/`

负责 Stable Kernel Audit、Task Runtime、Extension Runtime、Kernel 相关 Capability Contract、Governance、Execution Record、Compatibility 和 Kernel vs Foundation Service 边界。

### `docs/02_capabilities/`

负责抽象 Capability，例如 Search、Analyze、Generate、Image、Video、Files。描述“OS 要求系统做什么”，而不是“具体让谁来做”。

### `docs/03_skills/`

负责 Generic / Commerce / TikTok / Amazon / Temu / Composite / Professional Operator Skills。Skill 负责业务上怎么做。

### `docs/04_services/`

负责 Kernel 之外的重要 Foundation Services，例如 Knowledge、Evidence、Research、Artifact。最终清单尚未冻结。

### `docs/decisions/`

负责正式 Architecture Decision Record / ADR，记录决定、原因、替代方案、代价、影响、批准状态和允许重审的条件。

### `src/ecommerce_ai_os/kernel/`

只用于已经批准到可以实现的 Stable Kernel 代码。

### `src/ecommerce_ai_os/capabilities/`

用于已批准的 Capability Contract 和抽象实现。

### `src/ecommerce_ai_os/skills/`

用于已批准的 Skill 与 Skill Composition。

### `src/ecommerce_ai_os/providers/`

用于具体 Provider Adapter / Implementation，例如 Scrape Creators、LLM、Image、Video、Storage、MCP-backed Provider、API / SDK Integration。

### `src/ecommerce_ai_os/services/`

用于 Kernel 外 Foundation Service 的正式实现。

### `src/ecommerce_ai_os/applications/`

用于用户真正使用的 Application、Workspace、Productized Workflow 和顶层 Use Case。

---

# 13. Documentation vs Implementation Rule

项目明确区分：

```text
docs/
= 当前已经讨论、审计、记录到哪里

src/
= 已经批准到可以实现什么
```

因此，`src/` 中存在目录，不代表已经允许开发这个模块。

---

# 14. Technology Neutrality / 技术中立

**状态：Current Design Principle**

Ecommerce AI OS 不应该被当前流行技术名词定义。

- MCP 是接入或协议机制之一；
- Agent 是执行与决策机制之一；
- RAG 是 Knowledge Retrieval 的实现方式之一；
- Embedding 是语义检索的一种底层技术；
- Vector Database 是存储和检索实现之一；
- Multimodal Model 是某种 Capability 的实现；
- Chat 是前端交互入口之一；
- LangGraph / Future Agent Framework 属于未来实现选型。

原则：

> **先有真实业务或架构问题，再选择技术。**

---

# 15. 产品与架构开发原则

**状态：Current Design Principle**

> # **Architecture big, implementation small.**
>
> **架构可以为未来留足扩展空间，但每一次实现必须尽量小、尽量真实。**

含义：

- 顶层架构允许考虑未来很多场景；
- 具体开发从窄的真实业务闭环开始；
- 不能因为愿景很大，就一次开发所有模块；
- 新需求先判断是否能放进已有边界；
- 一个新 Use Case 不应该自动导致顶层重构；
- 只有真实需求证明现有抽象不足时，才修改更高层架构。

---

# 16. 当前 Architecture Audit 顺序

1. Stable Kernel Boundary
2. Task Runtime
3. Extension Runtime
4. Capability Contract
5. Governance
6. Execution Record
7. Compatibility
8. Kernel vs Foundation Services Boundary
9. Skills
10. Capabilities
11. Providers
12. Knowledge / Evidence / Research Services
13. Agent / UI

这个顺序当前属于 Working Design Sequence，可以经过人工决定调整。

---

# 17. 当前开发边界

当前阶段：

# **Architecture Baseline**

当前暂时不进入以下正式开发：

- Production Agent；
- Multi-Agent Orchestration；
- RAG；
- Vector Database；
- MCP Architecture；
- Production Database；
- Frontend UI；
- TikTok Skill 正式实现；
- Amazon Skill 正式实现；
- Temu Skill 正式实现；
- Short Drama Skill 正式实现；
- Provider Lab 正式接入；
- 97 API 正式接入；
- Production Image Pipeline；
- Production Video Pipeline。

当前工作重点：

- 项目总基线；
- 架构边界；
- Repository Governance；
- Controlled Architecture Audit；
- 旧设计审计；
- 已验证外部资产记录；
- 为后续实现建立清晰、可追溯的决策路径。

---

# 18. Change Discipline / 变更纪律

1. 不允许静默继承旧项目架构。
2. Candidate Architecture 未经人工确认，不允许自动升级为 Approved Architecture。
3. 不因为某个框架流行，就把它引入系统。
4. Provider Response Schema 不允许直接定义 OS 顶层 Domain Model。
5. 平台专项业务知识不能写死进 Stable Kernel。
6. 在真正专业运营没有加入前，不假装 TikTok / Amazon / Temu 专业工作流已经完整。
7. 低层实现不能悄悄重新定义高层已经批准的架构。
8. 重要架构决定进入 `docs/decisions/`。
9. 当出现新业务需求时，首先判断它属于 Existing Skill、New Skill、Capability、Provider、Foundation Service、Application，还是暴露了真正的 Kernel 缺陷。
10. 只有在现有抽象被真实需求证明不够时，才修改更高层架构。

---

# 19. Related Baseline Documents

这份文档必须配合以下文件阅读：

- `01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md`
- `02_LEGACY_ARCHITECTURE_REFERENCE_AUDIT.md`
- `03_PROVIDER_LAB_ASSET_HANDOFF.md`
- `04_NEW_CHAT_HANDOFF.md`
- 根目录 `AGENTS.md`
- 根目录 `README.md`

---

# 20. Current Baseline State / 当前基线状态

## 20.1 Current Design Principles

- Stable Core；
- Extensible Capability；
- Replaceable Provider；
- Pluggable Skill；
- Technology Neutrality；
- Architecture big, implementation small；
- Provider Facts 不得反过来决定 OS Architecture。

## 20.2 Candidate Architecture

- Task Runtime；
- Extension Runtime；
- Capability Contract；
- Governance；
- Execution Record；
- Compatibility。

## 20.3 Important but Not Yet Designed

- Task Object；
- Context Model；
- Skill Contract 详细字段；
- Skill Composition 详细规则；
- Capability Schema；
- Provider Routing；
- Knowledge Architecture；
- Evidence Architecture；
- Research Architecture；
- Artifact Architecture；
- Agent Architecture；
- Frontend / Workspace Model；
- Persistence Model；
- Database；
- RAG / Retrieval Architecture；
- Detailed Multimodal Architecture。

## 20.4 Existing Verified External Asset

- Scrape Creators Provider Lab；
- 97 API Inventory；
- Runtime Evidence；
- L0 Calibration；
- 独立 Provider Lab Repository。

这些资产继续保留，但不负责决定 Ecommerce AI OS 顶层架构。

---

# 21. Human Review Gate

当前文档状态：

# **Draft for Human Review**

只有在项目负责人明确确认后，才能将本文件升级为当前正式 Working Baseline。

批准这份文档只代表：

> **当前 Ecommerce AI OS 的项目地图、顶层设计原则、候选架构边界、仓库信息架构和后续审计方向被接受。**

它不代表：

- 六个 Kernel Candidate 内部设计已经批准；
- Task 字段已经批准；
- Skill Contract 已经批准；
- Capability Contract 已经批准；
- Knowledge / Evidence / Research 架构已经批准；
- Agent / UI 已经批准；
- 可以开始全面实现。

后续仍然按照：

```text
讨论
↓
专项审计
↓
Human Review
↓
Approved Slice
↓
Implementation
```

逐步推进。
