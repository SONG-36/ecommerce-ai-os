# Ecommerce AI OS — Product Origin & Requirements V0.1

- **版本**：V0.1
- **状态**：Draft for Human Review / 待人工审阅
- **文档类型**：Project / Requirements
- **目标路径**：`docs/00_project/01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md`
- **项目**：Ecommerce AI OS
- **最后更新**：2026-08-14

---

## 0. 文档目的

这份文档只回答一个核心问题：

> **Ecommerce AI OS 为什么会出现？它从哪些真实业务问题一步步演变出来？当前已经确认了哪些产品需求，又有哪些需求仍然只是正在形成或未来扩展？**

它负责保存：

- 项目的真实业务起源；
- 从 TikTok 内容生产问题到 Ecommerce AI OS 的演变过程；
- 当前已经确认的业务需求；
- 正在形成中的业务需求；
- 未来必须保留的扩展空间；
- 为什么系统需要跨平台、可扩展、Provider 可替换、Skill 可插拔；
- 当前产品层的 Use Case Families；
- 当前明确的非目标。

它**不负责**设计 Kernel、Task Runtime、Skill Contract、Capability Contract、Provider Router、Agent、RAG、数据库、UI、Python 模块或 Deployment。

---

# 1. 项目不是从“做一个 AI OS”开始的

项目最初来自一个非常具体的跨境电商问题：

> **输入自己的商品信息，在 TikTok 上寻找相关参考视频，分析别人怎么拍，再辅助自己生产带货内容。**

最初工作流：

```text
Product Information
        ↓
Search TikTok Reference Videos
        ↓
Observe / Analyze
        ↓
Imitate / Adapt
        ↓
Shoot Ecommerce Content
```

这个人工流程真实执行过，因此项目的起点不是抽象架构，而是：

> **如何更高效地找到值得研究的 TikTok 内容，并转化为自己的内容生产输入。**

---

# 2. 第一次扩张：找到参考视频，并不等于会做内容

真实执行后发现：

> **找到爆款或高表现参考视频，只能回答“别人做过什么”，不能自动回答“我们应该做什么”。**

为了真正做出适合商品、市场和美国用户的内容，还需要理解：

- 市场环境；
- 产品本身；
- 用户需求与痛点；
- 竞品；
- 美国文化与语言；
- 内容表达方式；
- 评论与评价；
- 平台行为；
- 自己发布后的真实业务结果。

因此问题从：

```text
Search Reference Video
```

扩张成：

```text
Market Research
Product Research
User Research
Competitor Research
Content Research
Culture / Language Research
Comments / Reviews Research
```

项目第一次发生本质变化：

> **问题不再只是“找视频”，而是“为了做出更好的业务判断，需要研究市场、用户、商品和内容”。**

---

# 3. 第二次扩张：Research 并不属于 TikTok 独占

进一步发现，Research 并不是 TikTok 运营独有的需求。

Amazon、Temu 以及未来其他跨境电商平台，同样可能需要研究：

- 市场；
- 用户需求；
- 痛点；
- 商品；
- 竞品；
- 评论与评价；
- 内容；
- 广告；
- 创作者；
- 趋势；
- 搜索表达；
- 公开可见商品生态。

因此：

```text
TikTok Research Tool
```

不能继续作为整个项目的顶层产品定义。

更合理的理解是：

> **Research 是跨平台可复用的业务能力，而 TikTok、Amazon、Temu 是不同的平台业务语境和适配环境。**

---

# 4. 第三次扩张：业务问题开始要求跨来源数据与 Evidence

Research 深入后又出现一个现实问题：

> **真正需要回答的业务问题，往往不能只靠一个平台、一个 API、一个数据源。**

一个商品方向可能需要同时观察：

- TikTok；
- TikTok Shop；
- TikTok Ads；
- Instagram；
- YouTube；
- Facebook；
- Amazon；
- Reddit；
- Pinterest；
- Google；
- 未来其他来源。

于是问题逐渐变成：

```text
Business Question
        ↓
What Evidence is needed?
        ↓
Which Source may contain it?
        ↓
Which Provider can access it?
        ↓
How reliable is the returned data?
```

这也是后来建设 Scrape Creators Provider Lab 的原因之一。

这一阶段形成重要需求：

```text
Source ≠ Provider ≠ Capability
```

例如：

- TikTok 是 Original Source；
- Scrape Creators 是 Access Provider；
- Search / Retrieve Comments / Retrieve Product Details 等属于 Capability。

本文件只记录这一需求来源，不设计 Provider Architecture。

---

# 5. 第四次扩张：AI Creative Production 成为另一条真实业务线

项目并不只需要 Research。

实际业务中还出现了越来越多的 AI 创意生产需求：

```text
Script / 剧本
Product Image / 产品图
Video / 视频
Short Drama / 短剧
Director
Shot Planning
Execution Prompt
Editing
```

包括：

- 根据商品信息生成带货脚本；
- 根据参考视频反推结构，再生成适配自身产品的脚本；
- 生成产品图；
- 生成短视频；
- 将商品植入短剧；
- 设计婆媳冲突、爽剧、反转、龙傲天等内容形式；
- 将剧本进一步拆成导演方案、镜头计划和执行 Prompt；
- 控制 AI 视频生成成本；
- 将生成结果与真实素材和剪辑结合。

因此形成第二个重要结论：

> **Script、Product Image、Video、Short Drama 等不是 TikTok 的专属子系统。**

它们属于：

> **Creative Production / 内容与创意生产**

TikTok 只是未来可能调用这些能力的一个平台业务场景。

---

# 6. 第五次扩张：系统不能每次都从零开始

随着 Research 和 Creative 工作增多，又暴露出一个问题：

> **如果每次研究、写脚本、做方案都从零开始，系统就无法积累。**

因此需要支持：

> **Knowledge-assisted Work / 知识辅助工作**

产品层真正需要的不是简单“做一个 Knowledge Base”，而是：

- 用户和 Skill 不应该每次从零开始；
- 之前验证过的知识应该能够被复用；
- 已知规则应该能够指导新的 Research；
- 新 Evidence 可以挑战旧知识；
- 真实业务结果可以形成新的知识候选；
- 未经审阅的新 Evidence 不应该自动覆盖正式 Knowledge；
- 正式知识应该可以被版本化和追溯。

原则：

```text
Existing Knowledge
        ↓
Guides Research / Creative / Decision

New Evidence
        ↓
May support or challenge existing Knowledge

Reviewed Evidence
        ↓
Knowledge Update Candidate

Human Review
        ↓
Approved Knowledge Update
```

本文件只记录产品需求，不设计 Knowledge Service、RAG 或数据库。

---

# 7. 第六次扩张：最终必须连接真实业务结果

如果系统最终只是：

```text
AI thinks this is good
```

或者：

```text
Public video performs well
```

就认为某个方向有效，那么它仍然只是建议工具。

真实业务最终需要回答：

- 自己的视频有没有播放？
- 用户有没有停留？
- 有没有点击、加购、成交？
- 哪种内容真的适合自己的商品？
- 市场高表现内容能不能迁移到自己的账号？
- 是方向、Hook、制作、商品还是流量问题？
- 哪些市场信号被自己的业务结果支持？
- 哪些市场信号和自己的实际结果冲突？

因此产生：

> **Experiment & Validation / 实验与验证**

长期理想闭环：

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
        ↓
Next Research
        ↓
Knowledge Candidate
```

当前只确认系统未来必须支持真实业务结果回流，不提前设计 Experiment Object、Attribution Engine、Metric Schema 或自动知识学习。

---

# 8. 第七次扩张：专业运营方法会持续变化

必须承认一个现实：

> **现在掌握的运营方法，不等于最终最专业的方法。**

未来真正专业的 TikTok、Amazon、Temu 或其他平台运营加入后，可能会带来：

- 更成熟的研究方法；
- 更专业的广告方法；
- 更完整的 Listing 工作流；
- 更成熟的内容方法；
- 更好的达人合作流程；
- 更可靠的复盘规则；
- 新的业务对象；
- 新的决策标准。

因此系统不能把当前不完整的运营方法硬编码进 Stable Core。

这一现实直接产生：

```text
Skill must be pluggable
Capability must be extensible
Provider must be replaceable
Core must remain relatively stable
```

---

# 9. 为什么最终演变成 Ecommerce AI OS

完整演变：

```text
真实 TikTok 内容生产问题
        ↓
参考视频搜索
        ↓
发现参考视频不足以指导高质量内容
        ↓
Research 扩张
        ↓
发现 Research 可以跨平台复用
        ↓
发现需要跨来源的数据获取 / Evidence 能力
        ↓
Creative Production 扩张
        ↓
Knowledge 复用需求
        ↓
Own-business Experiment & Validation
        ↓
发现专业运营方法会持续变化和补充
        ↓
需要 Skill 可插拔、Provider 可替换、Capability 可扩展
        ↓
Ecommerce AI OS
```

因此：

> **不是因为我们想先造一个“AI OS”，然后去寻找它能解决什么问题。**

而是因为真实电商工作流不断出现：

```text
Research
Creative
Knowledge-assisted Work
Experiment & Validation
Platform-specific Operation
AI Capability
Provider Replacement
Professional Skills
```

这些需求开始重复共享基础能力，并且需要长期扩展，才逐渐需要一个稳定但可扩展的 Ecommerce AI OS。

---

# 10. 当前产品能力地图

当前产品层必须区分两个不同维度：

1. **Cross-platform Use Case Families / 跨平台业务能力族**
2. **Platform Adaptation Dimension / 平台适配维度**

不能把两者简单平铺为同一种分类。

## 10.1 Cross-platform Use Case Families

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
│   └── Director / Shot Planning / Editing
│
├── Knowledge-assisted Work / 知识辅助工作
│
└── Experiment & Validation / 实验与验证
```

它们回答：

> **用户想通过 Ecommerce AI OS 完成什么类型的工作。**

## 10.2 Platform Adaptation Dimension

平台维度不是第五个 Use Case Family。

它回答：

> **同一类通用业务能力，在不同平台语境下如何组合、适配和专业化。**

```text
Platform Adaptation Dimension
│
├── TikTok Skill Pack
├── Amazon Skill Pack
├── Temu Skill Pack
└── Future Platform Skill Pack
```

例如：

```text
Research + TikTok Skill Pack
→ TikTok Content Research
```

```text
Research + Amazon Skill Pack
→ Amazon Product / Review Research
```

```text
Creative Production + TikTok Skill Pack
→ TikTok Short-form Video / Short Drama
```

当前没有假设 TikTok、Amazon、Temu 的完整专业运营方法已经设计完成。

---

# 11. Emerging Business Family：Platform-specific Operations

除了当前四类跨平台 Use Case Families，还已经看到一个正在形成的业务方向：

> **Platform-specific Operations / 平台专项运营**

未来可能包含：

- Listing；
- 广告；
- 店铺分析；
- 价格；
- 选品；
- 达人合作；
- 发布；
- 店铺经营；
- 平台专项复盘；
- 其他运营动作。

但当前不正式把它冻结为完整 Product Family。

原因：

- 当前对 TikTok / Amazon / Temu 的完整专业运营流程还没有足够深的统一认知；
- 未来可能由真正专业运营人员补充；
- 当前过早拆出完整 Operations 架构，很容易再次基于碎片信息设计系统。

当前状态：

**Emerging Business Need / Detailed Scope Not Yet Defined**

---

# 12. 业务需求成熟度

本文件只描述业务需求成熟度：

```text
Confirmed Business Need
Emerging Business Need
Future Extension
```

Draft / Candidate Architecture / Approved / Implemented 等架构状态由 Architecture Governance 单独管理。

## 12.1 Confirmed Business Need

已经来自真实业务或明确反复出现的问题：

- TikTok 内容研究；
- 市场、用户、商品、竞品、内容、评论研究；
- 跨来源公开数据与 Evidence 获取；
- AI Script / Creative Planning；
- Product Image / Video；
- Director / Shot Planning / Editing 支持；
- Knowledge 不应每次从零开始；
- Own-business Result / Validation；
- Provider 需要可替换；
- Capability 需要可扩展；
- 专业业务 Skill 必须可继续增加。

## 12.2 Emerging Business Need

已经明确看见价值，但标准流程尚未成熟：

- Short Drama Commerce 完整标准工作流；
- 婆媳 / 爽剧 / 龙傲天等具体短剧类型的稳定生产方法；
- Amazon 完整 Professional Skill Pack；
- Temu 完整 Professional Skill Pack；
- Platform-specific Operations；
- 更完整的 Research → Creative → Publish → Result 实验闭环；
- 跨业务 Knowledge Learning Workflow；
- 更成熟的 Professional Operator Skill 体系。

## 12.3 Future Extension

- 未来未知电商平台；
- 未来未知运营角色；
- 未来未知专业 Skill；
- 未来新的 Creative Form；
- 未来新的 AI Capability；
- 未来新的 Provider；
- 未来新的数据来源；
- 当前还没有想到的 Ecommerce Workflow。

原则：

> **为未来留扩展空间，但不提前虚构未来业务。**

---

# 13. Core Product Requirements / 核心产品需求

## R1. Business-first / 业务优先

系统必须从真实电商业务问题出发，不能为了使用 Agent、MCP、RAG、Embedding、Vector DB 等技术而反向寻找业务场景。

## R2. Cross-platform / 跨平台

Research、Creative、Knowledge-assisted Work、Validation 等能力不应被某一个平台独占。

## R3. Extensible / 可扩展

系统必须允许未来出现新 Use Case、新平台、新 Professional Skill、新 Capability、新 Provider、新数据来源和新 AI 模型。

## R4. Replaceable Provider / Provider 可替换

上层业务不应该直接依赖某个具体 Provider。

## R5. Pluggable Professional Skill / 专业 Skill 可插拔

专业运营方法必须能够独立演进，不能污染 Stable Core。

## R6. Knowledge-assisted / 能积累和复用知识

系统不能每次从零开始，经过管理的知识应该能够支持新的 Research、Creative 和 Decision。

## R7. Evidence-aware / 证据意识

系统需要区分公开观察、Evidence、Hypothesis、Finding、Own-business Result 和 Knowledge Candidate，不能把公开相关性直接表述成业务因果。

## R8. Human-reviewable / 可人工审阅

重要业务判断、正式知识更新、高成本执行或高风险动作，需要保留 Human Review / Human Gate 的空间。

## R9. Traceable / 可追溯

未来的重要 Research、Finding、Creative、Execution 和 Knowledge Update，应能够追溯到输入、Evidence、版本和业务结果。

## R10. Real-business-validation capable / 能连接真实业务验证

系统不能只依赖公开市场数据或 AI 判断，未来必须能够接入和比较自己的真实业务结果。

## R11. Technology-neutral / 技术中立

系统不应由当前流行的 AI 技术名词定义，技术应服务于业务和系统需求。

## R12. Unknown-future-use-case tolerant / 对未知未来需求保持容忍

顶层架构不能建立在“当前业务列表已经完整”的假设上。

---

# 14. 当前明确非目标

当前项目不是要：

- 一次做完 TikTok / Amazon / Temu 所有功能；
- 一次完成所有跨境电商运营流程；
- 自动取代专业运营人员；
- 直接构建一个全自动 Agent 公司；
- 一次接入全部 97 个 Provider API；
- 一次完成 Knowledge / Evidence / Research 最终架构；
- 一次完成 RAG、Vector Database、Agent、Multi-Agent、UI、Production Database；
- 一次完成 Image / Video Production Pipeline；
- 现在就定义完整 Platform-specific Operations；
- 因为某个 AI 技术流行就强行加入系统；
- 根据当前碎片化运营知识假装已经掌握所有平台专业流程。

当前原则：

> **Architecture big, implementation small.**

即：

- 顶层为未来保留合理扩展空间；
- 具体实现从窄的真实业务闭环开始；
- 不因为长期愿景很大，就同时开发所有模块。

---

# 15. Product Requirements 与其他架构层的边界

本文件只负责：

```text
Why
+
Business Need
+
Product Requirement
+
Use Case Direction
```

后续层级分别回答：

```text
Product Architecture
→ 用户能做什么，产品业务能力如何组织

System Architecture
→ 为了支撑产品能力，系统由什么组成、如何协作

Software Architecture
→ System Architecture 最终如何落成代码、模块、接口和运行时

Architecture Governance
→ 上述架构如何批准、变更、废弃、追踪权威
```

因此：

> **Product Requirement 不直接指定 System Component。**

例如“用户不应该每次从零开始”是 Product Requirement；至于未来由 Knowledge Service、RAG、Database、Embedding、Vector Store 或 LLM 中的哪一种或哪几种实现，应由后续 System / Software Architecture 决定。

---

# 16. 当前结论

当前产品级结论：

```text
1. Research 是跨平台能力，不是 TikTok 专属。

2. Creative Production 是跨平台能力，
   Script / Product Image / Video / Short Drama
   不属于 TikTok 独占。

3. Knowledge 在产品层表达为 Knowledge-assisted Work，
   不提前假设具体 Knowledge 技术架构。

4. Experiment & Validation 必须保留，
   因为最终需要连接真实业务结果。

5. Platform Skill Pack 是平台适配维度，
   不是和 Research / Creative 同类型的 Use Case Family。

6. Platform-specific Operations 已经出现，
   但当前只作为 Emerging Business Need。

7. Provider 会变化，AI 技术会变化，
   专业运营方法也会变化。

8. 因此系统需要：
   Stable Core
   + Extensible Capability
   + Replaceable Provider
   + Pluggable Skill

9. 系统必须允许未来未知业务进入，
   而不是假设今天已经知道所有需求。
```

---

# 17. Human Review Gate

当前文档状态：

# **Draft for Human Review**

批准本文件只代表：

> **Ecommerce AI OS 的产品起源、需求演变、当前 Use Case Families、Platform Adaptation 维度、业务需求成熟度和核心产品要求，被接受为后续 Product Architecture 与 System Architecture 的需求输入。**

批准本文件不代表：

- Product Architecture 已经最终设计完成；
- System Architecture 已经批准；
- Stable Kernel 已经批准；
- Skill Contract 已经批准；
- Capability Contract 已经批准；
- Provider Routing 已经批准；
- Knowledge / Evidence / Research 系统架构已经批准；
- Agent / RAG / DB / UI 已经批准；
- 可以开始全面实现。

后续流程：

```text
Product Origin & Requirements
        ↓
Human Review
        ↓
Product Architecture
        ↓
System Architecture
        ↓
Software Architecture
        ↓
Approved Implementation Slice
```
