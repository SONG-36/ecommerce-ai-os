# Ecommerce AI OS — Legacy Architecture Reference Audit V0.1

- **版本**：V0.1
- **状态**：Draft for Human Review / 待人工审阅
- **文档类型**：Reference Audit / Legacy Architecture
- **目标路径**：`docs/05_references/legacy/02_LEGACY_ARCHITECTURE_REFERENCE_AUDIT.md`
- **项目**：Ecommerce AI OS
- **最后更新**：2026-08-14

---

## 0. 文档目的

这份文档回答：

> **过去在 SIG、N01-N18、Track A/B/C、Market Signal、ResearchBasis 等设计中形成的内容，进入 Ecommerce AI OS 后，到底应该如何处理。**

目标不是否定旧设计，也不是把旧设计全部搬进新系统。

本文件只做三件事：

1. 识别仍然值得保留的设计原则；
2. 标记可以继续参考、但不能直接继承为新 Contract 的旧对象；
3. 明确哪些旧顶层架构不再拥有 Ecommerce AI OS 的架构权威。

统一使用三类：

```text
KEEP AS PRINCIPLE
REFERENCE ONLY
DO NOT INHERIT AS AUTHORITY
```

---

# 1. Legacy Architecture 的总体定位

旧架构主要形成于更窄的业务阶段，包括：

- TikTok / Video Direction；
- Market Signal；
- SIG-P0 → SIG-P6；
- N01 → N18；
- Track A / B / C；
- ResearchBasis；
- MarketSignalReport；
- NormalizedVideoSignal；
- Knowledge Feedback；
- Public Signal / Own-business Validation。

这些工作有大量有效思想。

但当前 Ecommerce AI OS 已扩展到：

- Cross-platform Research；
- Creative Production；
- Knowledge-assisted Work；
- Experiment & Validation；
- Platform Skill Packs；
- Future Professional Skills；
- Future Unknown Use Cases。

因此：

> **旧设计不能因为曾经被批准或详细讨论过，就自动成为 Ecommerce AI OS 的 Current Authority。**

---

# 2. KEEP AS PRINCIPLE

以下内容建议继续作为 Ecommerce AI OS 的长期设计原则。

---

## 2.1 Business Question → Evidence Need

研究不能从“我有哪些 API”开始。

更合理的顺序是：

```text
Business Question
        ↓
Evidence Need
        ↓
Candidate Source / Capability
        ↓
Collection / Analysis
        ↓
Finding
```

系统应该先明确业务问题，再判断需要什么证据。

---

## 2.2 Answerability 必须显式表达

不同数据只能回答不同强度的问题。

需要明确区分：

- 当前数据可以回答；
- 只能部分回答；
- 需要未来阶段；
- 必须依赖 Own Business Data；
- 公开数据本身无法证明。

不能把“可观察”自动升级成“可证明”。

---

## 2.3 Allowed Statement / Prohibited Overclaim

重要 Finding 应区分：

```text
Allowed Statement
vs
Prohibited Overclaim
```

例如：

可以说：

> 当前样本中某类内容表现相对更高。

不能直接说：

> 这种内容一定带来更高转化。

---

## 2.4 Raw Evidence Preservation

原始证据应尽量保留。

后续：

- Normalize；
- Classification；
- Analysis；
- Finding；

都应该能够追溯回原始 Evidence。

---

## 2.5 Processing / Rule Versioning

同一批 Raw Evidence 经过不同规则处理，可能得到不同结果。

因此处理规则需要具备版本意识。

---

## 2.6 Traceability / Provenance

从：

```text
Finding
↓
Processed Result
↓
Raw Evidence
↓
Source / Provider
```

应该可以建立可追溯关系。

---

## 2.7 Missing != 0

字段缺失不能自动解释为数值 0。

例如：

```text
missing
null
not returned
not visible
0
```

必须保留语义区别。

---

## 2.8 Correlation != Causation

公开数据中观察到的相关关系不能直接表述为因果。

尤其不能仅凭公开视频指标证明：

- 真实购买人群；
- 真实转化率；
- 广告归因；
- 达人 GMV 归因；
- 自然流归因；
- 某创意一定成功。

---

## 2.9 Public Signal != Real Business Truth

公开数据更适合：

- 描述市场样本；
- 发现线索；
- 形成假设；
- 发现值得进一步研究的方向。

真实业务效果需要 Own Business Data 进一步验证。

---

## 2.10 Knowledge Update Requires Human Review

新 Evidence 可以：

- 支持旧知识；
- 挑战旧知识；
- 形成 Knowledge Update Candidate。

但是：

> **新 Evidence 不应该自动覆盖正式 Knowledge。**

正式知识更新必须保留人工审阅和版本化。

---

# 3. REFERENCE ONLY

以下旧对象仍然有设计参考价值，但不能直接成为 Ecommerce AI OS 的正式 Contract。

---

## 3.1 CollectionRun

旧设计用于表达一次数据采集边界。

未来 Task / Run / Research 设计时可以参考：

- 执行边界；
- 查询配置；
- 采集时间；
- 数据来源；
- 运行结果。

但当前不直接继承名称、字段或生命周期。

---

## 3.2 QueryExecution

旧设计用于表达单次查询执行。

未来 Research / Capability Execution 可以参考：

- query；
- provider call；
- status；
- pagination；
- response reference；
- error。

但不直接继承旧 Contract。

---

## 3.3 RawDataset / RawRecord

保留“Raw Evidence / Raw Record”思想。

但未来是否继续使用：

```text
RawDataset
RawRecord
```

以及它们的具体字段，由新的 Evidence / Research Architecture 决定。

---

## 3.4 ProcessingRun

旧设计中的规则版本、处理过程和输出追溯值得参考。

但不自动成为 Stable Core 的 Run Object。

---

## 3.5 MarketSignalReport

可以参考：

- sample boundary；
- limitations；
- source refs；
- descriptive findings；
- prohibited overclaim。

但是：

> **MarketSignalReport 不再是 Ecommerce AI OS 的通用顶层输出对象。**

---

## 3.6 ResearchBasis

可以参考它在旧架构中承担的：

- Research context；
- supporting evidence；
- research justification。

但未来新的 Research / Task Context 不自动沿用 `ResearchBasis` 名称或字段。

---

## 3.7 ResearchTask

可以参考“人工拥有研究任务”的思想。

但新的 Task Runtime 仍然需要在 Stable Core 专项审计中重新设计。

---

## 3.8 Signal Layer

旧 L1 / L2 / L3 / L4 分层对理解：

- Public Content Supply；
- Public Performance；
- Public Commercial Visibility；
- Own Business Validation；

有参考价值。

但不直接把旧 Signal Layer 作为整个 Ecommerce AI OS 的通用数据架构。

---

## 3.9 EvidenceComparison / ConflictFinding

旧 SIG-P5 中“公开证据与自有业务结果可以比较并发现冲突”的思想值得保留。

未来 Experiment & Validation / Evidence Service 可以参考。

---

# 4. DO NOT INHERIT AS AUTHORITY

以下内容不能自动继承为 Ecommerce AI OS 的正式顶层架构。

---

## 4.1 SIG-P0 → SIG-P6

旧 SIG 阶段划分解决的是 Market Signal / Evidence 演进问题。

它不是 Ecommerce AI OS 的通用 Product / System Lifecycle。

因此：

```text
SIG-P0 → SIG-P6
```

只保留历史参考。

---

## 4.2 N01 → N18

旧 N01-N18 是 Video Direction Workbench 时代的业务流程结构。

它不能直接定义 Ecommerce AI OS 的通用工作流。

---

## 4.3 Track A / B / C

旧 Track 划分服务于当时：

- ResearchTask；
- Knowledge Catalog；
- Market Signal；

的并行开发。

当前新的 Product / System Architecture 已经重新分层，因此不继承旧 Track 为顶层结构。

---

## 4.4 NormalizedVideoSignal as Universal Core Object

`NormalizedVideoSignal` 明显属于 Video / Public Content 问题域。

它不能成为跨：

- Amazon；
- Research；
- Image；
- Audio；
- Short Drama；
- Future Operations；

的通用 OS 核心对象。

---

## 4.5 MarketSignalReport as Universal OS Output

MarketSignalReport 可以继续作为某种研究结果参考，但不能假设所有 Product Workflow 都输出 MarketSignalReport。

---

## 4.6 TikTok / Video-first Top-level Architecture

Ecommerce AI OS 当前已经明确：

```text
Research
Creative Production
Knowledge-assisted Work
Experiment & Validation
Platform Adaptation
```

因此不再使用 TikTok / Video 作为顶层架构中心。

---

## 4.7 旧目录结构

旧项目中的：

- tracks；
- SIG docs；
- N01-N18 文档层级；
- 旧 baseline 目录；

不再拥有新仓库的信息架构权威。

---

## 4.8 旧 Cross-track Message Architecture

旧 Track 之间的消息结构只适用于旧架构。

未来 Skill / Capability / Service / Task 之间的 Contract 必须重新设计。

---

# 5. 旧设计中仍值得长期引用的解释边界

未来在 Research / Evidence / Validation 设计中，应继续参考以下解释纪律：

```text
Public Data
→ Observation / Signal / Hypothesis

Own Business Data
→ Validation Evidence

One Test
≠ Universal Rule

High Public Performance
≠ Guaranteed Creative Success

Product Link Present
≠ Click / Add-to-cart / Purchase

Creator Audience Estimate
≠ True Buyer Audience

Public Ad Visibility
≠ Ad Spend / Sales Scale

Correlation
≠ Causation
```

---

# 6. Legacy Object Reuse Rule

未来如果新的设计想重新使用旧对象名称，例如：

```text
ResearchTask
ProcessingRun
MarketSignalReport
```

必须重新回答：

1. 它是否仍然符合当前 Product Architecture？
2. 是否跨平台成立？
3. 是否跨 Provider 成立？
4. 是否和 Stable Core / Foundation Service 边界冲突？
5. 是否只是因为“旧文档已经写过”才想继续用？

如果只是第五种情况：

> 不应继承。

---

# 7. Legacy Document Authority

旧文档默认：

```text
Reference Authority
```

而不是：

```text
Current Architecture Authority
```

如果旧文档和当前：

- Product Architecture；
- System Architecture；
- Software Architecture；
- Architecture Governance；

冲突：

> 当前新架构文档优先。

如果旧文档包含经过真实运行验证的 Provider 事实：

> 应进一步回到 Provider Lab / Runtime Evidence 判断，而不是直接使用 Legacy Architecture 文档。

---

# 8. Legacy Audit 总结

```text
KEEP AS PRINCIPLE
├── Business Question → Evidence Need
├── Answerability
├── Allowed Statement / Prohibited Overclaim
├── Raw Evidence Preservation
├── Processing Versioning
├── Traceability / Provenance
├── Missing != 0
├── Correlation != Causation
├── Public Signal != Real Business Truth
└── Knowledge Update Requires Human Review

REFERENCE ONLY
├── CollectionRun
├── QueryExecution
├── RawDataset / RawRecord
├── ProcessingRun
├── MarketSignalReport
├── ResearchBasis
├── ResearchTask
├── Signal Layer
└── EvidenceComparison / ConflictFinding

DO NOT INHERIT AS AUTHORITY
├── SIG-P0 → SIG-P6
├── N01 → N18
├── Track A / B / C
├── NormalizedVideoSignal as universal object
├── MarketSignalReport as universal OS output
├── TikTok / Video-first top-level architecture
├── old repository information architecture
└── old cross-track message architecture
```

---

# 9. Human Review Gate

当前状态：

# **Draft for Human Review**

批准本文件只代表：

> **旧架构中的原则、参考对象和不再继承的顶层结构已经完成初步分类，可作为 Ecommerce AI OS 后续专项设计的 Reference Boundary。**

它不代表：

- 旧对象自动进入新 System Architecture；
- 旧 Contract 自动恢复；
- 旧 SIG / N01-N18 重新获得 Current Authority。
