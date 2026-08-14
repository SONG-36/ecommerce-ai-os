# Ecommerce AI OS — Scrape Creators Provider Lab Asset Handoff V0.1

- **版本**：V0.1
- **状态**：Draft for Human Review / 待人工审阅
- **文档类型**：External Verified Asset Handoff
- **目标路径**：`docs/05_references/provider_lab/03_PROVIDER_LAB_ASSET_HANDOFF.md`
- **项目**：Ecommerce AI OS
- **外部项目**：Scrape Creators Provider Lab
- **Provider Lab Repository**：`/Volumes/projects/andy/0810/scrape-creators-provider-lab`
- **最后更新**：2026-08-14

---

## 0. 文档目的

这份文档负责：

> **把 Scrape Creators Provider Lab 已经验证和冻结的 Provider 事实，安全交接给 Ecommerce AI OS。**

它不重新设计 Provider Lab。

也不允许 Provider Lab 的 API Surface 反向定义 Ecommerce AI OS 的 Product / System Architecture。

---

# 1. Provider Lab 的唯一定位

Scrape Creators Provider Lab 的职责是：

> **测试 Scrape Creators，并确定这个 Provider 实际支持什么。**

它是：

- Provider Capability / Certification Lab；
- Runtime Reconnaissance Project；
- External Verified Asset。

它不是：

- Ecommerce AI OS；
- Product Architecture；
- System Architecture；
- Evidence Platform 本身；
- TikTok Product；
- Video Direction Product；
- Product Selection Agent。

核心边界：

```text
Provider Lab discovers facts.
Ecommerce AI OS consumes and productizes those facts.
```

---

# 2. Source / Provider / Capability 必须分离

Provider Lab 已经形成的重要语义：

```text
Source
≠
Provider
≠
Capability
```

例如：

```text
TikTok
= Original Source

Scrape Creators
= Access Provider

Search / List / Get Detail / Transcript / Comments
= Capability
```

因此：

> Scrape Creators 的 API 结构不能直接成为 Ecommerce AI OS 的 Product Domain Model。

---

# 3. 当前 97 API Inventory

当前已盘点：

> **97 个 unique endpoints**

注意：

> **97 是当前 inventoried endpoint count，不代表 Scrape Creators 永远只有 97 个 API。**

当前分布：

| Surface | Count |
|---|---:|
| TikTok | 22 |
| TikTok Shop | 5 |
| TikTok Ad Library | 2 |
| Instagram | 19 |
| YouTube | 16 |
| Facebook | 11 |
| Facebook Marketplace | 2 |
| Facebook Ad Library | 5 |
| Google | 1 |
| Google Ad Library | 3 |
| Amazon Shop | 1 |
| Reddit | 6 |
| Pinterest | 4 |
| **Total** | **97** |

因此当前 Provider Lab 已经从最初的 TikTok 生态 29 endpoints 扩展为多平台 Provider Surface。

---

# 4. Runtime Final Disposition

当前最终 Runtime Disposition：

```text
Total Endpoint Coverage
97 / 97

SUCCESS
92

BLOCKED_PROVIDER
1
→ TT-19

BLOCKED_RESOURCE_UNAVAILABLE
1
→ TT-09

BLOCKED_SEED_UNDISCOVERABLE
3
→ TT-04
→ SHOP-02
→ RD-05
```

这里的：

```text
SUCCESS
```

表示 Runtime Execution 结果。

它不能与 L0 Calibration 的：

```text
CONFIRMED
```

混为同一个状态。

---

# 5. L0 Runtime Calibration

当前 L0 Runtime Calibration：

```text
CONFIRMED
92

CORRECTED
0

UNKNOWN
5

RULE_CONFLICT
0
```

5 个 UNKNOWN：

| Endpoint | Final Runtime Disposition | UNKNOWN Reason |
|---|---|---|
| TT-04 | BLOCKED_SEED_UNDISCOVERABLE | BLOCKED_SEED |
| TT-09 | BLOCKED_RESOURCE_UNAVAILABLE | BLOCKED_RESOURCE |
| TT-19 | BLOCKED_PROVIDER | BLOCKED_PROVIDER |
| SHOP-02 | BLOCKED_SEED_UNDISCOVERABLE | BLOCKED_SEED |
| RD-05 | BLOCKED_SEED_UNDISCOVERABLE | BLOCKED_SEED |

当前结果还包括：

```text
Endpoints Classified Without Rule Conflict
97 / 97

Resource / Capability Determinate
92 / 97

Generality Result
SUPPORTED_BY_FULL_RUN
```

注意：

> `SUPPORTED_BY_FULL_RUN` 只表示当前 97 endpoint full run 没有发现迫使现有分类框架系统性修改的冲突。

它不意味着该 taxonomy 永远正确。

---

# 6. Runtime Success 与 L0 Confirmed 的区别

必须长期保持：

```text
Runtime State
≠
Calibration State
```

例如：

```text
SUCCESS
```

表示：

> 本次 endpoint runtime request 成功得到正常业务响应。

而：

```text
CONFIRMED
```

表示：

> 当前 L0 Candidate Classification 在 Runtime Evidence 下得到确认。

因此：

```text
92 SUCCESS
```

和：

```text
92 CONFIRMED
```

虽然当前数字相同，但不是同一个状态体系，也不能互相替代。

---

# 7. Provider Lab 当前冻结点

当前冻结 Commit：

```text
1b1c35f
docs: freeze l0 runtime calibration handoff
```

该 Commit 作为当前 L0 Runtime Calibration Handoff 的重要锚点。

Provider Lab 的 Git / Runtime 状态在未来继续工作前仍应重新审计，而不是仅依赖本 Handoff 猜测当前 Working Tree。

---

# 8. L2 当前状态

当前：

```text
L2 = PAUSED intentionally
```

原因不是 Provider Lab 失败。

而是：

> Ecommerce AI OS 正在重新定义自己的 Capability / Foundation Service / Provider Boundary。

如果此时继续让 Provider response schema 主导更高层设计，容易出现：

```text
Provider API Shape
↓
OS Domain Model
```

这种反向依赖。

因此当前正确选择是：

> 先收敛 Ecommerce AI OS 的 System Architecture，再决定如何消费 Provider Lab 的 L2 事实。

---

# 9. 正确未来依赖关系

当前建议：

```text
Ecommerce AI OS
        ↓
Capability / Service Contract
        ↓
Provider Adapter
        ↓
Scrape Creators Provider Facts
        ↓
Provider Lab Runtime Evidence
```

不是：

```text
97 Scrape Creators APIs
        ↓
97 OS Modules
        ↓
Ecommerce AI OS Architecture
```

---

# 10. Provider-specific Quirks 的处理原则

Provider-specific quirks 应尽量被：

```text
Adapter
+
Capability / Service Contract Boundary
```

吸收。

例如：

- 参数命名；
- provider-specific ID；
- pagination token；
- missing field；
- region quirks；
- credits；
- provider error shape；
- cache behavior；
- special filter syntax。

这些不应该直接传播到：

- Product Architecture；
- Professional Skill；
- Platform Skill Pack；
- Stable Core Domain Semantics。

---

# 11. Provider Lab 可以向 Ecommerce AI OS 提供什么

未来 Ecommerce AI OS 可以消费的 Provider Lab 资产包括：

- Request Contract；
- Response Contract；
- Field Dictionary；
- Identity Map；
- Pagination Contract；
- Time Semantics；
- Missingness Semantics；
- Error Semantics；
- Cost / Credits Map；
- Region / Filter Behavior；
- Provider Limitations；
- Capability Verdict；
- Capability Manifest；
- Adapter Contract；
- Runtime Evidence。

这些资产的实际成熟度可能因 endpoint 不同而不同。

不能因为存在一个 Deliverable 名称，就假设所有 97 endpoint 都已经完成相同深度的 Contract Verification。

---

# 12. Provider Lab 不拥有的权威

Provider Lab 不负责决定：

- Ecommerce AI OS Product Family；
- System Architecture；
- Stable Core；
- Skill Architecture；
- Knowledge Architecture；
- Evidence Architecture；
- Research Architecture；
- Product Recommendation；
- Creative Strategy；
- Business Decision。

因此：

```text
Provider Lab
对 Provider Runtime Facts
= Fact Authority

Provider Lab
对 Ecommerce AI OS Architecture
= No Architecture Authority
```

---

# 13. Evidence Authority 原则

当 Provider 事实冲突时，应优先使用更强的 Runtime Evidence。

当前已形成的基本权威顺序可概括为：

```text
Immutable Raw Runtime Evidence
        ↓
Redacted Runtime Evidence
        ↓
Observed Request Surface Evidence
        ↓
Compact Reference Summary
        ↓
Planning / Candidate Assumption
```

因此：

> 规划文档不能覆盖真实 Runtime Evidence。

---

# 14. 当前 Ecommerce AI OS 应如何使用 Provider Lab

当前阶段只做：

```text
Reference
+
Boundary Definition
+
Future Contract Input
```

暂时不做：

- 97 API 正式接入；
- 97 Adapter 实现；
- Provider Router；
- Response Schema 映射；
- L2 全量字段语义；
- Production Provider Integration。

这些必须等 System Architecture 和 Software Architecture 进一步收敛。

---

# 15. Current Frozen Facts

当前交接给 Ecommerce AI OS 的冻结事实：

```text
1. Provider Lab 是独立外部项目。

2. Provider Lab 的职责是发现和认证 Provider 事实。

3. 当前 inventoried unique endpoints = 97。

4. 97 不是 Scrape Creators 永久 API 总数声明。

5. Runtime Final Disposition:
   92 SUCCESS
   1 BLOCKED_PROVIDER
   1 BLOCKED_RESOURCE_UNAVAILABLE
   3 BLOCKED_SEED_UNDISCOVERABLE

6. L0 Runtime Calibration:
   92 CONFIRMED
   0 CORRECTED
   5 UNKNOWN
   0 RULE_CONFLICT

7. UNKNOWN endpoints:
   TT-04
   TT-09
   TT-19
   SHOP-02
   RD-05

8. Freeze commit:
   1b1c35f
   docs: freeze l0 runtime calibration handoff

9. L2 当前 intentionally paused。

10. Provider quirks 应被 Adapter / Contract Boundary 吸收。

11. Provider Lab 不定义 Ecommerce AI OS 顶层架构。

12. 正确方向：
    OS → Contract → Adapter → Provider Facts
```

---

# 16. Human Review Gate

当前状态：

# **Draft for Human Review**

批准本文件只代表：

> **Scrape Creators Provider Lab 当前已经验证和冻结的 Provider 事实、边界、97 endpoint inventory、Runtime Disposition、L0 Calibration、Freeze Commit 以及未来接入方向，被接受为 Ecommerce AI OS 的 External Verified Asset Handoff。**

它不代表：

- L2 已完成；
- 97 个 endpoint 已经全部达到 Production Contract 深度；
- Ecommerce AI OS 已批准 Provider Adapter 设计；
- 97 API 可以开始全面接入；
- Provider Lab 获得 Ecommerce AI OS 架构权威。
