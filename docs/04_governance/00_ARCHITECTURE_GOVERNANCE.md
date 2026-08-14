# Ecommerce AI OS — Architecture Governance V0.1

- **版本**：V0.1
- **状态**：Draft for Human Review / 待人工审阅
- **文档类型**：Architecture Governance
- **目标路径**：`docs/04_governance/00_ARCHITECTURE_GOVERNANCE.md`
- **项目**：Ecommerce AI OS
- **最后更新**：2026-08-14

---

## 0. 文档目的

这份文档只回答一个问题：

> **Ecommerce AI OS 的架构如何被提出、审阅、批准、实现、验证、修改、废弃，以及不同来源发生冲突时谁拥有权威。**

本文件治理的是：

- Product Architecture；
- System Architecture；
- Software Architecture；
- Architecture Decision Record / ADR；
- 架构状态；
- 架构变更；
- 文档权威；
- AI / Codex 的权限边界；
- 冲突处理；
- Handoff 的权威边界。

本文件不负责运行时权限、运行时审批、成本 Gate、风险 Gate 等系统执行规则。

这些属于：

> **Runtime Governance**

因此必须明确：

```text
Architecture Governance
≠
Runtime Governance
```

---

# 1. Governance Scope / 治理范围

Architecture Governance 横向治理以下架构层：

```text
Project / Requirements
        ↓
Product Architecture
        ↓
System Architecture
        ↓
Software Architecture
        ↓
Code / Schema / Tests
```

同时管理：

- Architecture Status；
- Architecture Authority；
- Human Review；
- ADR；
- Change Proposal；
- Supersede / Deprecate；
- Conflict Resolution；
- Documentation Discipline。

---

# 2. Architecture Status Model / 架构状态模型

当前统一使用以下状态：

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

---

## 2.1 Draft

表示：

> 设计刚形成，用于讨论，还没有进入正式架构审阅。

特点：

- 可以快速修改；
- 不形成实现约束；
- 不应被 AI 解释为正式架构；
- 不要求 ADR。

---

## 2.2 Candidate

表示：

> 设计已经值得进入正式架构审阅，但尚未批准。

特点：

- 名称、边界、接口仍可能变化；
- 可以用于后续讨论；
- 不应直接驱动大规模实现；
- AI / Codex 无权自行升级为 Approved。

---

## 2.3 Approved

表示：

> 当前正式接受的架构设计。

Approved 代表：

- 后续低层设计应遵守它；
- 实现不能静默绕过；
- 重大修改必须重新进入架构变更流程；
- 必要时形成 ADR。

---

## 2.4 Implemented

表示：

> 已存在对应代码、Schema、配置、运行机制或正式工作流。

Implemented 不代表已经经过充分业务验证。

---

## 2.5 Validated

表示：

> 不仅已经实现，而且经过测试、运行或真实业务验证。

Validated 的验证方式取决于对象类型，例如：

- unit / integration test；
- runtime test；
- provider certification；
- accepted business workflow；
- human review；
- production observation。

---

## 2.6 Rejected

表示：

> 方案已经被明确否决。

Rejected 的设计不能因为新聊天、模型切换或上下文缺失，被 AI 自动重新当作 Candidate。

如果未来重新考虑，必须说明：

- 为什么旧拒绝原因已失效；
- 出现了什么新事实；
- 为什么值得重新审阅。

---

## 2.7 Deprecated

表示：

> 当前仍可能存在或兼容，但不建议继续新增依赖或扩展。

---

## 2.8 Superseded

表示：

> 已被新的正式设计取代，不再拥有 Current Authority。

旧文档可以保留用于历史追溯，但必须明确指向替代方案。

---

# 3. Authority Model / 权威模型

一个问题只能有一个主要 Current Authority。

不同层分别拥有不同类型的权威。

---

## 3.1 Project / Requirements Authority

负责：

> **为什么做、真实业务问题是什么、当前需求如何演变。**

主要文档：

```text
docs/00_project/
```

例如：

- Product Origin；
- Business Need；
- Requirements；
- Current Project State。

---

## 3.2 Product Architecture Authority

负责：

> **用户能做什么，业务能力如何组织。**

主要文档：

```text
docs/01_product/
```

它对以下问题有权威：

- Use Case Families；
- Platform Adaptation；
- Product Workflow；
- Product Boundary；
- Emerging Product Areas。

---

## 3.3 System Architecture Authority

负责：

> **为了支撑产品能力，系统由哪些职责区域组成，它们之间是什么边界。**

主要文档：

```text
docs/02_system/
```

它对以下问题有权威：

- Stable Core；
- Skills；
- Capabilities；
- Foundation Services；
- Providers；
- Applications；
- System Dependency Boundary。

---

## 3.4 Software Architecture Authority

负责：

> **系统职责如何落成软件模块、接口、Runtime、Persistence 与 Deployment。**

主要文档：

```text
docs/03_software/
```

当前 Software Architecture 仍处于：

> **Not Yet Designed / Boundary Baseline**

---

## 3.5 Code / Schema / Tests Authority

负责：

> **当前实际上已经实现了什么。**

未来一旦进入实现：

```text
Code
Schema
Tests
Runtime Configuration
```

对实现事实拥有最高权威。

例如：

如果 Software Architecture 文档写某接口存在，但代码中已经不存在，则：

> 实现事实以代码为准，文档必须更新。

但：

> 低层代码不能利用“已经实现”反向静默推翻 Approved Product / System Architecture。

如果实现与正式架构冲突，应当识别为架构偏离，而不是自动把架构改成迁就代码。

---

## 3.6 Provider Lab Authority

Provider Lab 负责：

> **Provider 的真实运行事实。**

包括：

- Request；
- Response；
- Field；
- Pagination；
- Identity；
- Missingness；
- Error；
- Cost；
- Provider limitation；
- Runtime behavior。

例如：

如果 OS 文档写某 API 有某字段，但 Provider Lab 实测不存在：

> Provider 事实以 Provider Lab 为准。

Provider Lab 不拥有：

> Ecommerce AI OS 顶层 Product / System Architecture 权威。

---

## 3.7 ADR Authority

ADR 负责记录：

> **某个重要架构决定为什么被做出。**

ADR 不替代 Product / System / Software Architecture 本身。

它主要保存：

- Decision；
- Context；
- Alternatives；
- Rationale；
- Consequences；
- Approval；
- Revisit Condition。

---

# 4. AI / Codex Governance Boundary

AI / Codex 可以：

- 提出架构建议；
- 生成 Draft；
- 做一致性审核；
- 识别冲突；
- 检查文档与代码差异；
- 机械写入批准后的内容；
- 执行格式、路径、Git、测试检查；
- 提出 ADR Candidate。

AI / Codex 不可以自行：

```text
Draft → Approved
Candidate → Approved
Deprecated → Deleted
Superseded → Purged
```

也不可以：

- 自己决定顶层架构重构；
- 静默修改 Approved Architecture；
- 把旧 Reference 文档重新提升为 Current Authority；
- 因为 Provider 返回字段方便，就让 Provider Schema 定义 OS 顶层模型；
- 自动更新正式 Knowledge；
- 把自己的推断写成已批准事实。

正式状态升级必须经过：

```text
Proposal
↓
Human Review
↓
Explicit Approval
↓
Document / ADR Update
```

---

# 5. Human Review Rule

涉及以下情况必须保留明确 Human Review：

- Candidate → Approved；
- Approved Architecture 的重大修改；
- Stable Core 责任新增或删除；
- Product Family 顶层变化；
- System Boundary 变化；
- Capability / Skill / Provider 核心定义变化；
- 依赖方向变化；
- 重大基础设施选择；
- 已 Approved 方案被 Superseded；
- 重大兼容策略变化。

Human Review 必须是：

> **明确确认**

而不是根据聊天语气自动推断。

---

# 6. ADR Rule / 什么情况下需要 ADR

不是所有修改都需要 ADR。

ADR 只用于重要、长期、会影响未来实现或理解的架构决定。

建议需要 ADR 的情况：

- 改变顶层架构层级；
- 改变核心边界；
- 新增 / 删除 Stable Core 责任；
- 改变 Skill / Capability / Provider 的核心定义；
- 改变 System Dependency Direction；
- 引入重大基础设施；
- 改变长期兼容策略；
- 推翻已经 Approved 的设计；
- 选择一个长期难以逆转的实现方向。

通常不需要 ADR：

- 文案修改；
- 拼写修复；
- 文件名微调；
- 内部函数重命名；
- 小型 Refactor；
- 尚处 Draft 的普通讨论；
- 不改变架构边界的机械整理。

原则：

> **ADR 记录重要决定，不记录所有讨论。**

---

# 7. Documentation Discipline / 文档纪律

为了防止 Documentation Architecture 再次演变成文档屎山，冻结以下规则。

---

## Rule 1. 一个问题只有一个 Current Authority

同一问题不能长期存在两份互相竞争的正式文档。

如果新文档取代旧文档：

> 旧文档必须标记 Superseded / Reference / Archived。

---

## Rule 2. Baseline 只做地图

顶层 Baseline 负责：

- 当前项目是什么；
- 当前状态；
- 当前重要边界；
- 当前 Authority；
- 当前 Next Step。

Baseline 不复制所有详细设计。

---

## Rule 3. 详细设计进入专项文档

例如：

```text
00_SYSTEM_ARCHITECTURE.md
```

只保存系统总图。

Task Runtime 的详细设计应进入：

```text
docs/02_system/kernel/
```

而不是不断扩张 `00_SYSTEM_ARCHITECTURE.md`。

---

## Rule 4. 上级文档引用，不复制

如果某一专项设计已有 Current Authority：

> 上级文档只引用或摘要，不重复维护完整内容。

---

## Rule 5. 旧文档必须明确状态

旧设计不能因为仍然存在于仓库中，就自动拥有权威。

必须明确：

```text
Current
Reference
Deprecated
Superseded
Archived
```

---

## Rule 6. 实现事实不要重复人工维护

能从：

```text
Code
Schema
Tests
Generated API Reference
```

自动得到的实现事实，不应该再长期手写一份容易失真的副本。

---

## Rule 7. 文档重点保存“为什么”

架构文档应该重点保存：

- Why；
- Boundary；
- Decision；
- Constraint；
- Status；
- Trade-off；
- Revisit Condition。

而不是重复代码本身。

---

## Rule 8. 不为了“完整”而虚构未来

规则：

```text
Known
→ 写清楚

Candidate
→ 明确标记

Unknown
→ Not Yet Designed
```

不要因为担心未来遗漏，就提前设计没有真实业务依据的完整体系。

---

# 8. Conflict Resolution / 冲突处理

发生冲突时，不直接选择“最新文件”或“代码优先”。

先判断冲突属于哪一层。

标准流程：

```text
Conflict Detected
        ↓
Classify Layer
        ↓
Find Current Authority
        ↓
Compare Implementation / External Facts
        ↓
Determine Conflict Type
        ↓
Human Review if Architecture Impact
        ↓
Fix Document / Code / Provider Assumption / Architecture
```

---

## 8.1 软件文档与代码冲突

例如：

Software Architecture 说某接口存在，但代码里已经不存在。

如果这是已经批准后的合法实现变更：

> Code / Schema / Tests 代表当前实现事实，Software 文档需要同步。

---

## 8.2 实现违反 Approved System Architecture

例如：

```text
TikTok Skill
↓
直接调用 Scrape Creators SDK
```

但 Approved System Architecture 要求：

```text
Skill
↓
Capability Contract
↓
Provider
```

此时：

> 代码属于架构偏离。

不能因为代码已经写了，就静默修改系统架构迁就实现。

---

## 8.3 OS 文档与 Provider Lab 冲突

如果 OS 文档假定某 Provider 有某字段，但 Provider Lab 实测不存在：

> Provider 运行事实以 Provider Lab 为准。

然后决定：

- Adapter 修正；
- Capability Contract 修正；
- OS 假设修正；
- 或重新验证 Provider。

---

## 8.4 新 Evidence 与旧架构冲突

新业务事实可以触发架构重审。

但：

> 新 Evidence 不自动修改 Approved Architecture。

必须进入 Change Process。

---

# 9. Architecture Change Process / 架构变更流程

当出现：

- 新业务需求；
- 新平台；
- 新 Professional Skill；
- 新 Provider；
- 新 AI Capability；
- 新运行事实；
- 旧设计无法承载的新问题；

先执行：

```text
New Requirement / New Evidence
        ↓
Impact Classification
        ↓
属于哪一层？
Product?
System?
Software?
Governance?
        ↓
Existing Architecture Supports It?
        │
        ├── YES
        │    ↓
        │  Extend Existing Design
        │
        └── NO
             ↓
Architecture Change Proposal
             ↓
Human Review
             ↓
ADR if Significant
             ↓
Approved
             ↓
Implementation
             ↓
Validation
```

核心原则：

> **新业务需求先尝试进入现有结构，只有真实需求证明现有抽象不足时，才修改更高层架构。**

---

# 10. Handoff Governance

`docs/00_project/02_CURRENT_HANDOFF.md` 的职责是：

> **当前阶段导航和新聊天启动说明。**

它可以记录：

- 先读哪些文件；
- 当前 Git / Commit；
- 当前 Approved / Candidate；
- 当前阻塞；
- 当前下一任务；
- 禁止重新设计什么；
- 当前外部资产状态。

但：

> **CURRENT_HANDOFF 不是架构 Authority。**

如果 Handoff 与正式 Product / System / Software / Governance 文档冲突：

> 正式架构文档优先。

因此 Handoff 应该尽量短，并主要通过引用 Current Authority 工作。

---

# 11. Current Authority Map

当前建议的权威关系：

```text
Project / Requirements
docs/00_project/
        │
        ▼
Product Architecture
docs/01_product/
        │
        ▼
System Architecture
docs/02_system/
        │
        ▼
Software Architecture
docs/03_software/
        │
        ▼
Code / Schema / Tests

Architecture Governance
docs/04_governance/
        │
        └── 横向治理上述层级

References
docs/05_references/
        │
        ├── Legacy
        └── Provider Lab
```

其中：

```text
Provider Lab
→ 对 Provider 实测事实有权威

Legacy
→ 默认只有 Reference Authority
```

---

# 12. Architecture Governance 与 Runtime Governance

必须长期保持：

```text
Architecture Governance
≠
Runtime Governance
```

Architecture Governance 管理：

- Draft；
- Candidate；
- Approved；
- ADR；
- Architecture Change；
- Superseded；
- Authority。

Runtime Governance 管理系统执行时的：

- Permission；
- Policy；
- Human Gate；
- Cost Gate；
- Risk Gate；
- Execution Approval。

两者名称、文档和实现不得混用。

---

# 13. 当前确认的 Governance 原则

```text
1. 一个问题只有一个 Current Authority。

2. Product / System / Software 分层治理。

3. AI / Codex 无权自行把 Candidate 升级为 Approved。

4. 重大架构决定由 Human Review 控制。

5. ADR 只记录重要决定，不记录所有讨论。

6. Baseline 只做地图，不承担所有详细设计。

7. Superseded / Deprecated / Rejected 必须明确标记。

8. Code / Schema / Tests 对实现事实拥有权威，
   但不能静默推翻 Approved 高层架构。

9. Provider Lab 对 Provider 实测事实拥有权威，
   但不定义 Ecommerce AI OS 顶层架构。

10. 新需求先判断能否进入现有结构，
    只有真实需求证明抽象不足时才改高层。

11. Handoff 是导航，不是架构 Authority。

12. Architecture Governance 与 Runtime Governance 严格分离。
```

---

# 14. Human Review Gate

当前文档状态：

# **Draft for Human Review**

批准本文件只代表：

> **Ecommerce AI OS 的架构状态模型、Authority Model、AI / Codex 权限边界、ADR 规则、文档纪律、冲突处理、架构变更流程和 Handoff 边界，被接受为后续架构设计与 Vibe Coding 协作的治理基线。**

批准本文件不代表：

- 当前所有 Product / System / Software Candidate 都自动升级为 Approved；
- Runtime Governance 已经设计；
- 任何尚未设计的软件实现已经获批；
- AI / Codex 获得架构最终决策权。
