# Ecommerce AI OS — Product Architecture V0.1

- **版本**：V0.1
- **状态**：Draft for Human Review / 待人工审阅
- **文档类型**：Product Architecture
- **目标路径**：`docs/01_product/00_PRODUCT_ARCHITECTURE.md`
- **项目**：Ecommerce AI OS
- **最后更新**：2026-08-14

---

## 0. 文档目的

这份文档只回答：

> **用户拿 Ecommerce AI OS 能完成什么类型的工作，这些业务能力之间是什么关系。**

本文件负责：

- 定义当前产品层的业务能力组织方式；
- 区分跨平台 Use Case Family 与平台适配维度；
- 说明 Business Context 如何参与形成具体 Workflow；
- 说明当前 Product Family 如何继续扩展；
- 标记仍处于 Emerging 状态的业务方向；
- 给出 Product Architecture 到 System Architecture 的边界。

本文件不负责：

- Stable Core 设计；
- Skill Contract；
- Capability Contract；
- Provider Router；
- Knowledge / Evidence / Research 的系统实现；
- Agent；
- 数据库；
- Python 模块；
- API；
- Deployment。

---

# 1. Product Architecture 核心原则

当前 Product Architecture 采用两个主要维度：

```text
Cross-platform Use Case Families
+
Platform Adaptation Dimension
```

并通过业务上下文形成具体工作流：

```text
Use Case Family
+
Platform Adaptation
+
Business Context
=
Concrete Workflow
```

---

# 2. Cross-platform Use Case Families

当前已确认的跨平台业务能力族：

```text
Ecommerce AI OS

Cross-platform Use Case Families
│
├── Research / 研究
│   ├── Market Research / 市场研究
│   ├── User Research / 用户研究
│   ├── Product / Competitor Research / 产品与竞品研究
│   └── Content Research / 内容研究
│
├── Creative Production / 内容与创意生产
│   ├── Script / 剧本
│   ├── Product Image / 产品图
│   ├── Video / 视频
│   ├── Short Drama / 短剧
│   ├── Audio / Voice / 音频与配音
│   └── Director / Shot Planning / Editing
│
├── Knowledge-assisted Work / 知识辅助工作
│
└── Experiment & Validation / 实验与验证
```

这些 Family 回答：

> **用户想通过 Ecommerce AI OS 完成什么类型的工作。**

---

## 2.1 Research / 研究

负责帮助用户回答：

> **我们现在需要知道什么？**

当前包括：

- Market Research；
- User Research；
- Product / Competitor Research；
- Content Research。

未来可以继续增加新的 Research 子类型。

---

## 2.2 Creative Production / 内容与创意生产

负责把：

- Product Context；
- Research Finding；
- Knowledge；
- Platform Context；
- Business Goal；

转化为可执行的内容与创意产物。

当前包括：

- Script；
- Product Image；
- Video；
- Short Drama；
- Audio / Voice；
- Director；
- Shot Planning；
- Editing。

其中：

> Script / Product Image / Video / Short Drama / Audio 等都不是 TikTok 独占能力。

它们属于跨平台 Creative Production。

---

## 2.3 Knowledge-assisted Work / 知识辅助工作

产品层不提前假设某一种 Knowledge 技术实现。

这里表达的是用户需求：

> **用户和 Skill 不应该每次从零开始。**

Knowledge-assisted Work 可以横向支持：

- Research；
- Creative Production；
- Experiment & Validation；
- Future Operations。

---

## 2.4 Experiment & Validation / 实验与验证

负责回答：

> **前面的 Research、Creative 或业务判断，在自己的真实业务里是否有效。**

长期希望能够连接：

```text
Research
↓
Finding / Hypothesis
↓
Creative / Operation
↓
Execute / Publish
↓
Own Business Result
↓
Review
↓
Validated / Rejected / Unknown
```

具体 Metric、Experiment Object、Attribution 等不在 Product Architecture 中设计。

---

# 3. Current Product Families 不是永久固定模块

当前四个 Family：

```text
Research
Creative Production
Knowledge-assisted Work
Experiment & Validation
```

不是永久封闭清单。

原则：

> **Current Product Families ≠ Permanent Product Modules**

未来出现新业务需求时：

```text
新业务需求
↓
是否只是已有 Family 的一种工作？
├── YES → 加入已有 Family
└── NO
    ↓
是否形成独立、跨平台、完整的一类用户工作？
├── YES → Candidate New Use Case Family
└── NO → 先作为 Emerging / 子能力
```

例如：

```text
AI 配音
→ Creative Production
  → Audio / Voice
```

而不是因为出现“AI 配音”就新增一个顶层 Family。

未来如果出现真正独立、跨平台、完整的新业务，例如 Finance & Business Intelligence，则可以评估是否升级为新的 Product Family。

---

# 4. Platform Adaptation Dimension / 平台适配维度

平台不是第五个 Use Case Family。

它表示：

> **同一类通用业务能力，在不同平台语境下如何组合、适配和专业化。**

当前平台适配方向：

```text
Platform Adaptation Dimension
│
├── TikTok Skill Pack
├── Amazon Skill Pack
├── Temu Skill Pack
└── Future Platform Skill Pack
```

Platform Skill Pack 未来可以包含：

- 平台规则；
- 平台内容结构；
- 平台用户表达；
- 平台专业运营方法；
- 平台 Business Context；
- 通用 Skill 的组合与适配。

当前没有假设 TikTok、Amazon、Temu 的完整专业运营方法已经设计完成。

---

# 5. Business Context / 业务上下文

同一个 Use Case Family 和同一个 Platform Skill Pack，在不同业务上下文里会形成不同工作流。

当前 Business Context 可以包括：

```text
Product / SKU
Market / Region
Audience
Business Goal
Account / Shop
Campaign
Constraints
```

例如：

```text
Research
+
TikTok Skill Pack
+
US / Car Vacuum / Commerce Content Goal
↓
TikTok Car Vacuum Content Research
```

又例如：

```text
Creative Production
+
TikTok Skill Pack
+
US / Car Vacuum
↓
TikTok Car Vacuum Short-form Video / Short Drama
```

再例如：

```text
Research
+
Amazon Skill Pack
+
US / Car Vacuum
↓
Amazon Product / Review / Competitor Research
```

Business Context 是具体 Workflow 的重要输入。

但当前不把它升级为新的 Product Architecture 顶层。

---

# 6. Use Case Family 与 Platform Skill Pack 的关系

产品架构中的关系可以概括为：

```text
Cross-platform Use Case Family
        +
Platform Adaptation
        +
Business Context
        ↓
Concrete Product Workflow
```

因此：

```text
Research
+ TikTok
→ TikTok Content Research
```

```text
Research
+ Amazon
→ Amazon Product / Review Research
```

```text
Creative Production
+ TikTok
→ TikTok Short-form Video / Short Drama
```

```text
Creative Production
+ Amazon
→ Amazon Product Image / Product Video
```

平台不是通用能力的所有者，而是业务适配维度。

---

# 7. Use Case Families 之间不是固定流水线

当前不把四个 Family 定义成固定：

```text
Research → Creative → Knowledge → Validation
```

实际关系更接近：

```text
               Knowledge-assisted Work
                 ↕             ↕
                 ↕             ↕
Research ↔ Creative Production ↔ Experiment & Validation
```

其中：

- Research 可以读取已有 Knowledge；
- Creative 可以读取 Research Finding 和 Knowledge；
- Validation 可以验证 Research / Creative 假设；
- Validation 结果可以产生下一轮 Research；
- Reviewed Result 可以形成 Knowledge Candidate。

具体 System Service 如何实现这些关系，由 System Architecture 设计。

---

# 8. Product Workflow 长期闭环

长期产品闭环：

```text
Research
   ↓
Finding / Hypothesis
   ↓
Creative Production
   ↓
External Execution / Platform Operation
   ↓
Own Business Result
   ↓
Experiment & Validation
   ↓
Next Research
   ↓
Knowledge Candidate
```

其中：

```text
External Execution / Platform Operation
```

当前属于 Emerging Boundary。

发布、广告、Listing、达人合作、价格、店铺操作等完整专业运营体系还没有正式设计完成。

---

# 9. Emerging Product Area：Platform-specific Operations

当前已经看到一个正在形成中的业务方向：

> **Platform-specific Operations / 平台专项运营**

可能包括：

- Listing；
- Ads；
- Publishing；
- Creator Collaboration；
- Pricing；
- Store Operations；
- Other Platform Operations。

当前状态：

**Emerging Business Need / Detailed Scope Not Yet Defined**

当前不决定它最终是：

- 一个新的跨平台 Use Case Family；
- 多个 Product Family；
- Platform Skill Pack 的一部分；
- 或其他结构。

后续由更成熟的真实运营流程决定。

---

# 10. User Role 不是当前顶层架构轴

未来用户可能包括：

- 运营；
- 编剧；
- 剪辑；
- 研究员；
- 广告投手；
- 老板；
- 其他角色。

但当前 Product Architecture 不按岗位切割系统。

原因：

- 一个人可能承担多个角色；
- 团队组织结构会变化；
- Role 不应导致重复建设相同业务能力。

后续具体 Use Case 可以绑定 Operator Role，但当前不以岗位作为顶层 Product Architecture。

---

# 11. Product Outputs 只定义概念，不定义 Schema

Product Architecture 只定义概念级产物，例如：

```text
Research
→ Finding / Research Result

Creative Production
→ Script / Image / Video / Creative Plan

Experiment & Validation
→ Validation Result / Review

Knowledge-assisted Work
→ Knowledge Reference / Knowledge Candidate
```

当前不定义：

- 字段；
- ID；
- JSON；
- Schema；
- 存储格式；
- Version Object。

这些属于后续 System / Software Architecture。

---

# 12. Product Architecture 总图

```text
Ecommerce AI OS
│
├── Cross-platform Use Case Families
│   │
│   ├── Research
│   │   ├── Market Research
│   │   ├── User Research
│   │   ├── Product / Competitor Research
│   │   └── Content Research
│   │
│   ├── Creative Production
│   │   ├── Script
│   │   ├── Product Image
│   │   ├── Video
│   │   ├── Short Drama
│   │   ├── Audio / Voice
│   │   └── Director / Shot Planning / Editing
│   │
│   ├── Knowledge-assisted Work
│   │
│   └── Experiment & Validation
│
├── Platform Adaptation Dimension
│   ├── TikTok Skill Pack
│   ├── Amazon Skill Pack
│   ├── Temu Skill Pack
│   └── Future Platform Skill Pack
│
└── Emerging Product Areas
    └── Platform-specific Operations
```

具体 Workflow：

```text
Use Case Family
+
Platform Adaptation
+
Business Context
=
Concrete Workflow
```

---

# 13. Product Architecture Boundary

Product Architecture 回答：

> **用户能做什么，业务能力如何组织。**

它不回答：

> **系统内部由哪些组件实现这些能力。**

因此：

```text
Product Architecture
        ↓
System Architecture
```

Product Architecture 不直接指定：

- Stable Core；
- Skill Runtime；
- Capability Interface；
- Foundation Service；
- Provider；
- Agent；
- Database；
- Python package。

---

# 14. 当前状态

### Confirmed Product Structure

- Cross-platform Use Case Families；
- Platform Adaptation Dimension；
- Business Context 参与 Concrete Workflow；
- Product Family 可以继续扩展；
- Product Architecture 不按岗位切系统；
- Product Outputs 只定义概念；
- Platform-specific Operations 保持 Emerging。

### Detailed Design Not Yet Defined

- 各 Platform Skill Pack 的完整内容；
- 完整 Professional Operator Workflow；
- Product Output Schema；
- Platform-specific Operations 最终结构；
- UI；
- User Role Model。

---

# 15. Human Review Gate

当前文档状态：

# **Draft for Human Review**

批准本文件只代表：

> **当前 Ecommerce AI OS 的 Product Architecture 分类方式、跨平台 Use Case Families、Platform Adaptation 维度、Business Context 和 Emerging Product Area 被接受为 System Architecture 的产品输入。**

不代表：

- Platform Skill Pack 已经完整设计；
- Product Workflow 已经全部实现；
- System Architecture 已经批准；
- Software Architecture 已经批准。
