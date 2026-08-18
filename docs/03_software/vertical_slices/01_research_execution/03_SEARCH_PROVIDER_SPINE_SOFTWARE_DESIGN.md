# Ecommerce AI OS — First Research Slice — Search / Provider Spine Software Design V0.1

- **Phase**: Minimal Software Architecture
- **Step**: 3 — Search / Provider Spine Software Design
- **Status**: Candidate / Step 3 Complete
- **Architecture Authority**: No
- **Slice**: US / Car Vacuum / TikTok Content Research
- **Minimum Endpoint**: {TT-17 Search by Keyword}
- **Walking Implementation**: NOT YET AUTHORIZED

---

## 0. Purpose, Scope, and Boundary

本文件只负责：

> 将已经确认的 D2 / D5 / TT-17 Search semantics 转译为 First Research Slice 所需的最小 Search / Provider software spine candidate。

本文件回答：

~~~text
C2a 的 Search Need 与 C3 Search Request 如何区分？
C2b 如何依赖 provider-neutral C3 Search seam？
C3 Search Result 最少需要承载哪些语义？
C4a 的 static Search → Scrape Creators binding 在软件里如何成立？
C4b Adapter 与 Scrape Creators access mechanism 如何保持分离？
TT-17 mapping 由谁拥有？
Pagination / continuation / bounded traversal 由谁负责？
Duplicates、missingness、identity、source reference、media locator、time、region
如何不被错误增强或静默丢失？
Raw Provider Result 如何被隔离，同时保持必要的 referenceability？
Search Result、valid empty result、known missingness、resolution failure、invocation failure
如何在 software seam 上保持可区分？
~~~

本文件不负责：

~~~text
Product Architecture
System Architecture V0.2
9 Required Contracts 的重新设计
第 10 个 Contract
Research / Evidence exact software design
Execution Record exact software design
package layout
module layout
class layout
dataclass / Pydantic / JSON Schema choice
Protocol / ABC / callable choice
sync / async implementation
DB / persistence / raw payload repository
framework / transport / retry engine
router / registry / provider selector
generic transport platform
TT17Mapper architecture
97-API integration
Walking Implementation
~~~

必须继续保持：

~~~text
Responsibility ≠ Contract ≠ Software Component
Contract / Responsibility Flow ≠ Software Call Graph
Search Retrieval Semantics ≠ Research Sample Boundary
Provider ≠ Adapter ≠ Access Mechanism ≠ Endpoint
C3 Search Result ≠ Raw Provider Result
C3 Search Result ≠ Evidence
~~~

---

## 1. Inherited Inputs

本 Step 不重新设计上游语义。主要继承：

~~~text
docs/03_software/01_MINIMAL_SOFTWARE_ARCHITECTURE_PHASE_HANDOFF.md
docs/02_system/00_SYSTEM_ARCHITECTURE.md
docs/02_system/vertical_slices/01_research_execution/02_RESPONSIBILITY_COVERAGE.md
docs/02_system/vertical_slices/01_research_execution/03_MINIMAL_RUNTIME_PATH.md
docs/02_system/vertical_slices/01_research_execution/05_DEFERRED_REGISTER.md
docs/02_system/vertical_slices/01_research_execution/06_ARCHITECTURE_REVIEW.md
docs/02_system/vertical_slices/01_research_execution/contracts/00_CONTRACT_DESIGN_INDEX.md
docs/02_system/vertical_slices/01_research_execution/contracts/02_SEARCH_INVOCATION.md
docs/02_system/vertical_slices/01_research_execution/contracts/05_PROVIDER_MAPPING.md
docs/02_system/vertical_slices/01_research_execution/contracts/06_DETAILED_CONTRACT_CONSISTENCY_REVIEW.md
TT-17 Endpoint Admission / Selection Closure
~~~

本 Step 继续继承以下稳定事实：

~~~text
C1 = transport-neutral execution entry / return seam
C2b = actual Execution owner and Capability invocation coordinator
C2a = executable Research business method
C3 = provider-neutral Search Capability
C4a = current static / single-provider resolution: Search → Scrape Creators
C4b = Scrape Creators Provider translation / quirk absorption boundary
Scrape Creators = current concrete Provider
TT-17 = admitted minimum Provider endpoint: Search by Keyword
~~~

TT-17 的 admission 仍然是：

~~~text
TT-17 Endpoint Admission Review
= PASS_WITH_LIMITATIONS

Minimum Endpoint Subset
= {TT-17 Search by Keyword}
~~~

这不是 TT-17 所有 Provider semantics 已被完整认证。当前必须保留：

~~~text
region exactness = bounded / not fully proven
date_posted = observed but unverified
sort_by = observed but behavior unverified
provider hard cap = unknown
ranking semantics = unknown
global completeness = not claimable
cross-page duplicates = observed
media URL durability = not a permanent identity guarantee
metric freshness = bounded observation semantics
~~~

---

## 2. Core Search / Provider Spine Candidate

First Slice 的最小软件责任关系是：

~~~text
C2a Research Skill
    ↓ expresses provider-neutral Search Need / Search Request

C2b Task Runtime
    ↓ depends on

C3 Search Capability Seam
    ↓ currently provided behind the seam by

C4b ScrapeCreatorsAdapter
    ↓ uses

Scrape Creators Access Mechanism
    ↓ calls

Scrape Creators
    ↓ admitted endpoint

TT-17 Search by Keyword
~~~

返回路径是：

~~~text
TT-17 Raw Provider Result
    ↓
Scrape Creators Access Mechanism
    ↓
C4b ScrapeCreatorsAdapter
    ↓ translates / normalizes / preserves limitations
C3 provider-neutral Search Result or provider-neutral Search Failure
    ↓
C2b Task Runtime
    ↓
C2a Research Skill
~~~

### Mermaid responsibility / dependency view

~~~mermaid
flowchart TD
    C2a["C2a Research Skill<br/>Business Method"]
    C2b["C2b Task Runtime<br/>Execution Coordination"]
    C3["C3 Search Capability Seam<br/>Provider-neutral request / result"]
    C4a["C4a Static Binding<br/>Search → Scrape Creators"]
    C4b["C4b ScrapeCreatorsAdapter<br/>Translation / normalization / quirk absorption"]
    Access["Scrape Creators Access Mechanism<br/>Actual Provider access"]
    Provider["Scrape Creators<br/>Concrete Provider"]
    TT17["TT-17 Search by Keyword<br/>Minimum Endpoint"]
    Result["C3 Search Result / Failure<br/>Provider-neutral outcome"]

    C2a -->|"expresses Search Need / Request"| C2b
    C2b -->|"depends on stable seam"| C3
    C4a -.->|"static composition / binding fact"| C3
    C3 -.->|"currently provided behind seam by"| C4b
    C4b -->|"uses"| Access
    Access --> Provider
    Provider --> TT17
    TT17 --> Access
    Access --> C4b
    C4b -->|"normalizes and preserves bounded semantics"| Result
    Result --> C3
    C3 --> C2b
    C2b --> C2a
~~~

这张图是 software responsibility / dependency view，不是三个必然连续发生的 runtime service hop。

~~~text
C4a static binding ≠ mandatory runtime resolver call
C3 seam ≠ C4b semantics
C4b concrete implementation behind C3 ≠ C3 becomes Provider-specific
~~~

---

## 3. Search Need vs Search Request

### 3.1 Search Need

Search Need 是 C2a Research Skill 在当前 business method turn 中作出的业务控制判断：

~~~text
当前研究还需要 Search。
~~~

它可以由 C2a 的 research question、discovery strategy、coverage judgment、sampling strategy、evidence need 产生，但它不应携带：

~~~text
Scrape Creators
TT-17
provider cursor
HTTP request syntax
provider authentication
provider-specific parameter names
~~~

Search Need 不要求单独引入 generic Need object。

### 3.2 Search Request

Search Request 是把当前 Search Need 表达为一次 C3 provider-neutral Search invocation 所需的语义边界。

它只需要表达 Search 真正需要的 provider-neutral semantics，例如：

~~~text
query intent / keyword
requested platform context
requested market / region context
optional temporal semantics, when admitted and applicable
optional ordering semantics, when admitted and applicable
bounded retrieval request
~~~

当前不冻结字段名、类名、序列化形式或调用协议。

它不能被 TT-17 当前参数形状反向定义为：

~~~text
cursor
page
api_key
endpoint path
provider enum spelling
provider request wrapper
~~~

### 3.3 不增加通用包装层

当前不引入：

~~~text
Generic CapabilityRequest
Generic Action
Generic Command
ToolCallRequest
SearchIntentContract
~~~

C2a 的 business decision、C3 的 Search Request semantics、C2b 的 invocation coordination 已足以承载 First Slice 当前需要的关系。

---

## 4. C2b → C3 Dependency Rule

C2b Task Runtime 是 Capability invocation coordinator。它依赖：

~~~text
C3 provider-neutral Search Capability seam
~~~

它不能默认直接依赖：

~~~text
ScrapeCreatorsAdapter concrete type
TT-17 request syntax
Scrape Creators access client
raw Provider response shape
~~~

正确的软件语义是：

~~~text
C2b
↓ depends on
C3 Search semantics / callable seam
↓ currently backed by
ScrapeCreatorsAdapter
~~~

当前 C2b 的责任止于：

~~~text
确认 Search invocation 合法
协调一次逻辑 C3 Search invocation
接收 provider-neutral Search Result / Failure
保留必要的 execution-scoped invocation facts
把 outcome 返回同一 Research Execution
~~~

C2b 不负责：

~~~text
provider query translation
cursor arithmetic
research dedupe
evidence-worthiness judgment
sample sufficiency judgment
research interpretation
~~~

---

## 5. C3 Callable Seam — No Required SearchService

C3 必须有明确的可调用软件边界：

~~~text
C3 Search Capability
= stable provider-neutral callable seam
~~~

First Slice 不要求这个 seam 外面再包一层独立的 SearchService、SearchApplicationService、SearchOrchestrator 或 SearchWorkflow。

当前最小候选可以是：

~~~text
C2b
↓
C3 stable callable seam
↓ currently implemented / provided by
ScrapeCreatorsAdapter
~~~

这不表示：

~~~text
C3 = C4b
~~~

而表示：

~~~text
C3 = provider-neutral semantic boundary
C4b = concrete Provider translation implementation
~~~

未来是否使用 callable、Protocol、ABC、object、function、module boundary 或其他表示，留到后续整体软件架构阶段决定。

---

## 6. C4a Static Binding Semantics

### 6.1 Current binding

First Slice 当前是：

~~~text
Search Capability
→ Scrape Creators
~~~

这是：

~~~text
STATIC / SINGLE-PROVIDER RESOLUTION
~~~

C4a 当前只需要承载该 binding responsibility，不负责 endpoint mapping、API key、cursor、provider params、request syntax、HTTP client、retry、provider scoring 或 provider selection policy。

### 6.2 Configured Binding ≠ Resolved Provider ≠ Actually Used Provider

三个事实必须分开：

~~~text
Configured Binding
= 当前 software / composition 所声明或配置的 Search → Scrape Creators 关系

Resolved Provider
= 本次 invocation 合法形成的 Provider resolution fact

Actually Used Provider
= 本次真实 invocation 中确实被调用的 Provider fact
~~~

因此不能把 configured、resolved、used 当作同一事实：

~~~text
configured binding exists ≠ provider invocation necessarily happened
provider resolved ≠ access invocation necessarily succeeded
invocation succeeded → may establish actually-used Provider fact
~~~

### 6.3 C4a is not a runtime resolver component

当前不引入：

~~~text
ProviderResolverService
ProviderRouter
ProviderRegistry
ProviderSelector
ProviderScoringEngine
Dynamic Provider Marketplace
~~~

C4a 的语义可以由 static wiring / composition fact 承载。C4a 是 semantic/static binding responsibility，不是必须经过的一次 runtime hop。

---

## 7. C4b Adapter vs Concrete Scrape Creators Access Mechanism

### 7.1 C4b Adapter

C4b 是 Provider translation / quirk absorption boundary。当前 admitted TT-17 slice 中，C4b owns：

~~~text
provider-neutral request → TT-17 request translation
TT-17 response → provider-neutral result translation
Provider error → provider-neutral failure translation
Provider continuation → C3 continuation semantics
Provider missingness → normalized missingness
Provider region / filter quirks → bounded semantics
Provider ID representation → exact Provider identity preservation
Provider limitation → explicit limitation / unknown
~~~

C4b 必须受 C3 / D5 semantics 驱动，而不能让 Provider response shape 反向定义 OS boundary。

### 7.2 Access Mechanism

Scrape Creators Access Mechanism owns the concrete act of reaching the current Provider, including only the Provider-specific access responsibility needed by this slice。

它可以处理：

~~~text
actual Provider request dispatch
Provider authentication / access prerequisites
Provider response receipt
~~~

但它不拥有 C3 business semantics，也不拥有 Research Method judgment。

### 7.3 Separation rule

不能把所有责任压成一个不可区分的对象：

~~~text
ScrapeCreatorsAdapter
= HTTP
= auth
= network
= TT-17 mapping
= C3 normalization
= research interpretation
~~~

也不能把 Adapter 误认为 Provider 本身：

~~~text
Provider ≠ Adapter
Adapter ≠ Access Mechanism
Access Mechanism ≠ Endpoint
~~~

当前不要求这一定落成两个大型 class/service。要求的是责任边界必须存在。

---

## 8. TT-17 Mapping Is Internal to C4b

Minimum Endpoint 已收口为：

~~~text
{TT-17 Search by Keyword}
~~~

TT-17 的 admitted mapping 由 C4b 内部拥有：

~~~text
ScrapeCreatorsAdapter
    └── admitted TT-17 request / response / error / continuation translation
~~~

当前不单独引入：

~~~text
TT17Mapper
TT17RequestMapper
TT17ResponseMapper
TT17PaginationMapper
TT17IdentityMapper
~~~

如果未来真实复杂度证明 C4b 内部必须分拆，这是后续被证据推动的内部重构问题，不是当前 Step 3 的 architecture component。

C4b 只能实现：

~~~text
admitted semantics faithfully
or
explicitly bounded / lossy semantics
or
explicitly unsupported / unverified semantics
~~~

不得把 Provider unknown 增强成 OS guarantee。

---

## 9. Pagination Ownership and Bounded Traversal

### 9.1 Logical Search invocation may contain multiple Provider requests

必须保持：

~~~text
1 C3 logical Search invocation ≠ 1 Provider HTTP request
~~~

一个有界的 C3 Search invocation 可以内部包含多个 TT-17 page requests。C2b 协调的是 one logical C3 Capability invocation，不是每一页独立产生一个 Task、Execution 或 Capability invocation。

### 9.2 Responsibility split

~~~text
C2a Research Skill
= decides whether business research needs another Search invocation

C3 Search Capability
= owns provider-neutral bounded retrieval semantics and logical stop condition

C4b Adapter
= translates provider-neutral continuation into TT-17 continuation mechanics

Scrape Creators Access Mechanism
= sends the actual next TT-17 request

TT-17
= returns cursor / has_more / page results
~~~

因此：

~~~text
Research Skill does not see provider cursor.
~~~

Provider cursor is a Provider mechanism, not stable C3 semantics.

### 9.3 No default infinite traversal

错误方案：

~~~text
C4b
↓
while has_more:
    keep requesting forever
~~~

不能作为默认模型，因为 Adapter 不能自行吞掉 Search Retrieval Bound、Research Method judgment、Research Sample Boundary 或 stop policy。

First Slice 当前 hard cap 仍然是 UNKNOWN。因此软件语义必须支持：

~~~text
bounded traversal
continuation available
continuation unavailable
continuation unknown
known incomplete
bounded complete for current request
provider exhaustion, only if actually known
~~~

不得默认翻到世界尽头。

### 9.4 Retrieval bound vs research sample bound

~~~text
C3 Search retrieval bound
= 当前一次 Search 需要取得多少 / 以什么界限取得结果

C2a Research Sample Boundary
= 研究最终选择哪些 returned occurrences / items 作为实际样本
~~~

正确关系是：

~~~text
C3 returns bounded Search Result
↓
C2a interprets coverage and sampling need
↓
C2a may request another business-valid Search
~~~

C3 不负责 sampling judgment；C2a 不负责 Provider cursor mechanics。

---

## 10. Search Completion vs Provider Exhaustion vs Global Completeness

这三个概念必须保持独立：

~~~text
Search Completion
= 当前有界 C3 Search request 已经满足其请求边界

Provider Exhaustion
= Provider traversal 已经明确没有 continuation，或 Provider 明确表示 traversal ended

Global Completeness
= 对目标平台 / 市场 / 全局研究空间的完整覆盖
~~~

因此：

~~~text
Search Completion ≠ Provider Exhaustion ≠ Global Completeness
~~~

当前真实 TT-17 evidence 已观察到：

~~~text
page 1 → 30 items → cursor 30 → has_more=1
page 2 → 30 items → cursor 60 → has_more=1
~~~

这证明 continuation semantics 可被保留，但不证明：

~~~text
60 results = complete market
has_more eventually ends
Provider hard cap = 60
Provider hard cap = 3 test pages
~~~

Provider Lab 的 reconnaissance test cap 也不能升级为 Provider hard cap。

---

## 11. Duplicates Are Preserved; Research Layer Owns Dedupe

TT-17 实测已发现跨页重复。当前 software semantics 必须把返回结果表示为 returned occurrences，而不是提前唯一化的 unique items only。

必须能够表达：

~~~text
Occurrence 1 → item A
Occurrence 2 → item B
Occurrence 3 → item A again
~~~

C4b / C3 不得静默 drop duplicate、merge duplicate、overwrite occurrence order 或 claim unique result count。

正确责任分配是：

~~~text
C4b = preserve Provider returned-set occurrences
C3 = preserve occurrences in provider-neutral Search Result
C2a Research Skill = decide whether research sample dedupe is needed
~~~

Provider duplicate occurrence 不是自动的 Search Failure，也不是自动的 data corruption。

---

## 12. Missingness Normalization

C4b 必须把 Provider-side missingness 归一为 provider-neutral missingness，同时不伪造值。

需要能区分的 Provider-side cases 包括：

~~~text
missing
null
absent
unavailable
not returned
~~~

绝不能：

~~~text
missing → 0
missing → false
missing → empty string
missing → inferred value
~~~

责任分配：

~~~text
C4b = normalize missingness
C3 = carry normalized missingness and collection context
C2a = interpret research impact of missingness
~~~

例如：

~~~text
30 videos returned
1 description missing
~~~

仍然是合法 Search Result，内部带有 known missingness；不是 Search Failure。

---

## 13. Provider Identity vs Global / Source Identity

TT-17 的 aweme_id 可以作为 Provider-side item identity candidate，但必须保持：

~~~text
Provider ID ≠ Global OS Identity
~~~

Provider IDs 应按 opaque exact identifiers 处理：

~~~text
exact string representation first
~~~

不能因为它看起来像数字就静默做 numeric canonicalization 或 precision-losing conversion。Creator identity 的 numeric-looking representation 已显示出大整数表示风险，因此 exact string preservation 是 C4b 责任。

每个可引用 item 至少要能关联：

~~~text
Provider-side exact identity
Original TikTok source reference
necessary observed item facts
~~~

当前不创建：

~~~text
GlobalVideoId
CanonicalContentId
GlobalCreatorId
~~~

如果未来需要跨 Provider global identity，那是新的真实语义问题，不由 TT-17 admission 或 Step 3 擅自推导。

---

## 14. Source Reference vs Media Locator

~~~text
Original Source Reference
= 原始 TikTok 来源 / source identity 的 reference

Media Locator
= 在观察 / collection 时可访问某个 media representation 的 locator
~~~

TT-17 返回的 video URL、play URL、download URL、cover URL、subtitle URL 不能全部被当作永久 source identity。Media locator 可能是 signed、expiring、CDN-specific 或 temporary。

不能：

~~~text
media_url = source identity
hash(media_url) = global content id
~~~

正确边界是：

~~~text
source reference = identity / provenance basis
media locator = observation-time access information
~~~

---

## 15. Publication Time vs Observation / Metric Snapshot Time

TT-17 的 create_time 只能承载其已观察到的 publication-time semantics：

~~~text
create_time = publication time, where Provider fact supports that interpretation
~~~

Public metrics 应理解为：

~~~text
public metric values observed during Search collection
~~~

至少要能保留：

~~~text
publication time
observation / collection time
metric snapshot observation context
~~~

不能把 create_time 重用成 metric observation time、historical performance time 或 exact Provider-defined freshness time。当前不声称 historical metric trajectory、metric value at publish time、conversion 或 causal performance。

---

## 16. Bounded Region Semantics

First Slice 请求上下文是：

~~~text
Market / Region = US
~~~

当前事实只证明 Provider 接受 region=US 并在该请求下返回结果。没有证明 strict regional filtering、exact US population membership、audience location truth 或 complete US TikTok market coverage。

因此 C4b 可以表达：

~~~text
requested region = US
Provider request used region=US
returned set was retrieved under that Provider region context
exact region semantics = not fully proven
~~~

不能增强成：

~~~text
all returned videos are definitively representative of the complete US TikTok population
~~~

---

## 17. date_posted / sort_by Observed-but-Unverified Rule

Provider surface 观察到 date_posted 与 sort_by，但当前：

~~~text
date_posted = attempted / transport error / behavior unverified
sort_by = surface observed / behavior unverified
~~~

因此：

~~~text
Observed Provider parameter ≠ admitted OS semantic support
~~~

当前处理：

~~~text
query = admitted
region=US = bounded admitted semantics
date_posted = unverified optional behavior
sort_by = unverified optional behavior
~~~

如果未来 Research Need 要求 exact last 3 months 或 guaranteed most-liked ordering，C4b 必须报告 unsupported / unverified / bounded，而不能传了 Provider 参数后假装 C3 guarantee 已成立。

---

## 18. Raw Provider Payload Boundary and Referenceability

Raw Provider payload 不以 C3 semantics 形式一路上返：

~~~text
TT-17 raw payload
↓
C4b translation boundary
↓
C3 provider-neutral Search Result
~~~

C2b / C2a 不应依赖 TT-17 response shape。Raw Provider errors 也不能直接进入 Skill。

但 C4b 仍必须使必要的：

~~~text
Raw Provider Result Reference
Provider invocation reference
Capability Result reference
Original Source reference
~~~

能够在需要时关联，供后续 Evidence / Execution Record referenceability 使用。

必须保持：

~~~text
Raw-result referenceability ≠ raw payload duplication
Raw-result referenceability ≠ permanent raw payload retention
Raw-result referenceability ≠ raw payload repository
~~~

本 Step 不决定 raw payload 的 retention、storage、database 或 repository 形式。

---

## 19. Minimum C3 Search Result Semantic Categories

C3 Search Result 不能只是 list[Item]，也不能变成 TT17Response wrapper。

当前最小 semantic categories 是：

1. **Result-level identity / referenceability** — 这是哪一次逻辑 Search Capability Result，而不是哪个 HTTP response。
2. **Returned item occurrences** — 保留 Provider 返回顺序、occurrence 与重复 occurrence。
3. **Item identity / source reference** — Provider-side exact identity、Original source reference 与必要 observed facts。
4. **Actual returned-set semantics** — requested bound、actual returned occurrences、returned-set scope 与停止原因。
5. **Continuation / completeness / limitation** — continuation available / unavailable / unknown，bounded complete，known incomplete，Provider exhaustion if known，global completeness not claimable。
6. **Missingness / collection context** — normalized missingness、publication time、observation / collection context、metric snapshot semantics 与 Provider limitations。

这些是 semantic categories，不是当前冻结的 Python 字段、schema、enum 或 class。

---

## 20. Search Result vs Search Failure

当前最小逻辑 outcome：

~~~text
Search Invocation Outcome

├── Search Result
│   ├── non-empty result
│   └── valid empty result
│
└── Search Failure
    ├── invalid / unsupported Search invocation
    ├── Provider Resolution Failure
    └── normalized Provider Invocation Failure
~~~

这只是 software outcome semantics，不是新 Contract，也不批准当前创建 enum、exception hierarchy 或 result wrapper。

~~~text
合法 Search invocation + 没有匹配项
= Search Result

合法 Search invocation + known missingness
= Search Result with known missingness

没有形成合法 Provider binding
= Provider Resolution Failure

Provider 已 resolved，但 access / invocation 失败
= normalized Provider Invocation Failure
~~~

必须保持：

~~~text
Search Result ≠ Search Failure
Valid Empty Result ≠ Search Failure
Known Missingness ≠ Search Failure
Provider Resolution Failure ≠ Provider Invocation Failure
Raw Provider error ≠ C3 outcome
~~~

---

## 21. Full Step 3 Stress-Test Summary

本 Step 通过 20 个压力测试，覆盖 S3-01 至 S3-30。每个压力测试可以包含一个或多个 Candidate Decision。

| Pressure Test | Focus | Candidate Decisions | Result |
|---|---|---|---|
| 1 | Search Need 是否需要独立通用对象 | S3-01, S3-02 | PASS |
| 2 | Search Request 是否被 Provider 参数反向定义 | S3-03, S3-04 | PASS |
| 3 | C2b 是否直接依赖 concrete Provider | S3-05, S3-06 | PASS |
| 4 | C3 seam 与 C4b translation 是否混为一层 | S3-07 | PASS |
| 5 | C4a 是否变成 runtime Router / Resolver | S3-08, S3-09 | PASS |
| 6 | Adapter 与 concrete Access 是否混合 | S3-10, S3-11 | PASS |
| 7 | TT-17 mapping 是否吞掉 C3 semantics | S3-12 | PASS |
| 8 | Pagination 到底谁循环、谁停止 | S3-13, S3-14 | PASS |
| 9 | Duplicate 是否在 Adapter / C3 被消除 | S3-15 | PASS |
| 10 | Missingness 是否被补值或伪装 | S3-16 | PASS |
| 11 | Provider ID 是否被做成 Global ID | S3-17 | PASS |
| 12 | Source reference 是否与 media locator 混合 | S3-18 | PASS |
| 13 | Publication time 是否被复用为 metric time | S3-19 | PASS |
| 14 | region=US 是否被增强为 exact population | S3-20 | PASS |
| 15 | date_posted / sort_by 是否被假装已验证 | S3-21 | PASS |
| 16 | Raw Provider payload 是否一路上返 | S3-22 | PASS |
| 17 | C3 Result 是否过弱或过强 | S3-23 | PASS |
| 18 | C3 / C4a / C4b 是否机械变成三个 runtime service | S3-24, S3-25, S3-26 | PASS |
| 19 | Result、empty、missingness、failure 是否混淆 | S3-27, S3-28, S3-29, S3-30 | PASS |
| 20 | Delete Tests 是否证明最小 spine 足够 | Delete Tests A–G | PASS |

压力测试最终保留的关键边界：

~~~text
Search Need ≠ Search Request ≠ Actual Invocation Fact
Search Retrieval Bound ≠ Research Sample Boundary
Search Completion ≠ Provider Exhaustion ≠ Global Completeness
Provider ID ≠ Global OS Identity
Original Source Reference ≠ Media Locator
Publication Time ≠ Observation / Metric Snapshot Time
Observed Provider Parameter ≠ Guaranteed C3 Support
Raw Provider Payload ≠ C3 Search Result
Search Result ≠ Search Failure
~~~

---

## 22. Delete Tests

### Delete Test A — 删除独立 SearchService

保留：

~~~text
C3 stable callable seam
+
ScrapeCreatorsAdapter concrete implementation
~~~

First Slice 仍然可以形成 Search path。

结论：

~~~text
Independent SearchService = NOT REQUIRED
~~~

不能删除 C3 Search seam，否则 C2b 会直接依赖 concrete Provider。

### Delete Test B — 删除 ProviderResolverService

改为：

~~~text
static wiring
Search → Scrape Creators
~~~

仍然满足当前 C4a static / single-provider resolution。

结论：

~~~text
ProviderResolverService
ProviderRouter
ProviderRegistry
= NOT REQUIRED
~~~

但 configured binding、resolved Provider fact、actually-used Provider fact 的区分不能删除。

### Delete Test C — 删除 TT17Mapper component

将 admitted TT-17 mapping 留在 C4b / ScrapeCreatorsAdapter，当前 Slice 仍然可以表达 request、response、error、pagination、missingness 与 identity translation。

结论：

~~~text
TT17Mapper component = NOT REQUIRED
~~~

但 TT-17 translation responsibility 不能删除。

### Delete Test D — 删除 Adapter / Access Mechanism 分离

把 HTTP、auth、network、Provider semantic mapping 与 C3 normalization 全部压进一个 Provider client，短期可能能跑，但会破坏 C4b 与 Access 的责任边界。

结论：

~~~text
Adapter / Access separation = REQUIRED
~~~

这不要求两个大型 class/service，但必须保留责任边界。

### Delete Test E — 删除 C4a 独立 runtime hop

如果 C4a 是 static binding / composition fact，而不是每次调用 resolver.resolve("search")，当前语义没有损失。

结论：

~~~text
C4a semantic responsibility = REQUIRED
C4a independent runtime hop = NOT REQUIRED
~~~

### Delete Test F — 删除 provider-neutral C3 Search Result

让 Adapter 直接返回 TT17Response 会把 Provider shape 泄漏给 C2b / C2a。

结论：

~~~text
provider-neutral C3 Search Result = REQUIRED
~~~

### Delete Test G — 删除 Raw-result Referenceability

只保留 normalized result，不留任何 Raw / Provider / Capability linkage，后续 provenance path 会断：

~~~text
Evidence
→ Capability Result
→ Raw Provider Result
→ Original Source
~~~

结论：

~~~text
Raw-result Referenceability = REQUIRED
Raw Payload Repository = NOT REQUIRED
~~~

---

## 23. Sufficiency Gate

| Gate | Result |
|---|---|
| C2b 是否只依赖 provider-neutral C3 Search seam？ | PASS |
| C3 是否有明确 callable software boundary？ | PASS |
| 是否需要独立 SearchService？ | NO — not required / not proven |
| C4a static binding 是否有软件承载？ | PASS |
| 是否引入 Provider Router / Registry / Selector？ | NO |
| Configured / Resolved / Actually Used Provider 是否分离？ | PASS |
| C4b 是否负责 Provider translation / quirk absorption？ | PASS |
| C4b 是否吞掉 Research Method judgment？ | NO |
| Adapter 与 Access Mechanism 是否分离？ | PASS |
| TT-17 mapping 是否有明确 owner？ | PASS — C4b |
| 是否提前创建 TT17Mapper architecture？ | NO |
| C3 是否保留 bounded traversal / continuation semantics？ | PASS |
| Provider cursor 是否泄漏给 Research Skill？ | NO |
| Search Completion / Provider Exhaustion / Global Completeness 是否分开？ | PASS |
| Duplicates 是否保留到研究层？ | PASS |
| Missingness 是否被归一且不伪造？ | PASS |
| Provider identity 是否与 Global identity 分开？ | PASS |
| Source reference 是否与 media locator 分开？ | PASS |
| Publication / observation / metric snapshot time 是否分开？ | PASS |
| region=US 是否保持 bounded semantics？ | PASS |
| date_posted / sort_by 是否遵守 observed-but-unverified？ | PASS |
| Raw payload 是否隔离且 referenceable？ | PASS |
| C3 Search Result 是否 richer than list、narrower than Provider wrapper？ | PASS |
| Search Result 与 Search Failure 是否可区分？ | PASS |
| Valid Empty Result / Known Missingness 是否仍是成功 Result？ | PASS |
| Provider Resolution Failure 与 Invocation Failure 是否区分？ | PASS |
| 是否新增第 10 个 Contract？ | NO |
| 是否授权 Walking Implementation？ | NO |

结论：

~~~text
Step 3 semantic/software spine is sufficient as a Candidate.
Exact representation and implementation choices remain deferred.
~~~

---

## 24. Candidate Decisions S3-01 … S3-30

~~~text
S3-01
Search Need is a business-control decision; First Slice does not require a separate generic Need object.

S3-02
Do not establish a Generic CapabilityRequest / Action / Command / ToolCall wrapper.

S3-03
Search Request contains only provider-neutral Search-required semantics.

S3-04
Provider parameters do not define C3 Search Request semantics in reverse.

S3-05
C2b depends on the C3 Search seam and does not directly depend on the concrete Provider.

S3-06
C3 callable seam is required; an independent SearchService is not required or proven.

S3-07
C3 Search semantics and C4b Provider translation remain distinct even when C4b sits behind the C3 seam.

S3-08
C4a is static / single-provider binding for the First Slice; no Router is required.

S3-09
Configured Binding ≠ Resolved Provider ≠ Actually Used Provider.

S3-10
C4b ScrapeCreatorsAdapter ≠ Concrete Scrape Creators Access Mechanism.

S3-11
The current Access Mechanism can remain Scrape Creators-specific; no generic transport platform is required.

S3-12
TT-17 mapping implements admitted / bounded semantics only; Provider limitations are not enhanced into OS guarantees.

S3-13
C3 owns bounded logical traversal; C4b owns translation of Provider pagination / continuation mechanics.

S3-14
Search Completion ≠ Provider Exhaustion ≠ Global Completeness.

S3-15
Duplicates survive C4b / C3 retrieval; research-layer dedupe belongs to C2a.

S3-16
Missingness is first-class provider-neutral information: Missing ≠ zero ≠ false ≠ empty ≠ inferred.

S3-17
Provider IDs are opaque exact identifiers; aweme_id is not a Global canonical content identity.

S3-18
Original Source Reference ≠ Media Reference / Locator; media locators are observation-time access information.

S3-19
Publication Time ≠ Observation Time ≠ Metric Snapshot Time semantics.

S3-20
Requested Region = US ≠ Exact Population Membership; C4b preserves bounded Provider region semantics.

S3-21
Observed Provider parameter ≠ admitted OS semantic support; date_posted / sort_by remain unverified optional behavior.

S3-22
Raw Provider Payload stays below C4b; C3 receives normalized result plus necessary provenance / raw-result references.

S3-23
C3 Search Result must be richer than list[Item] but narrower than a Provider response wrapper.

S3-24
C4a semantics do not require an independent runtime resolver component; static wiring can carry Search → Scrape Creators.

S3-25
C4b may serve as the concrete implementation behind the stable C3 seam; C3 and C4b semantics remain distinct.

S3-26
TT-17 endpoint mapping is currently an internal C4b responsibility, not a separate architecture component.

S3-27
Search Result and Search Failure must remain distinguishable.

S3-28
Valid Empty Result and Known Missingness remain successful Search-result semantics.

S3-29
Provider Resolution Failure ≠ Normalized Provider Invocation Failure.

S3-30
Raw Provider errors do not cross the C4b / C3 boundary.
~~~

---

## 25. Explicitly Non-Introduced Items

This Step deliberately does not introduce:

~~~text
Product Architecture redesign
System Architecture redesign
10th Contract
SearchService
ProviderResolverService
ProviderRouter
ProviderRegistry
ProviderSelector
ProviderScoring Engine
Generic CapabilityRequest
Generic Action / Command layer
Generic transport platform
TT17Mapper architecture
TT17RequestMapper / TT17ResponseMapper component set
Raw Payload Repository
Raw Payload Database
EvidenceService
ResearchService
Analyze Capability
Retry Engine
Checkpoint / Crash Recovery
Event / Message Architecture
Durable Execution
97-API Integration
Global Identity Service
Global Completeness Service
Research Sample Service
Walking Implementation
~~~

这些项目不是被宣称为全局不存在，而是当前 Step 3、当前 First Slice、当前证据都没有授权把它们引入本 Candidate。

---

## 26. Representation Questions Deferred

本 Step 只冻结 semantic categories 和 responsibility boundaries，不冻结以下表示问题：

~~~text
Search Request exact field names
Search Result exact field names
Search Failure exact representation
Continuation exact representation
Completeness exact representation
Missingness exact representation
Provider Binding exact representation
Provider Fact exact representation
Raw Result Reference exact representation
Item occurrence exact representation
Metric snapshot exact representation
Region limitation exact representation
~~~

同样 deferred：

~~~text
dataclass vs Pydantic vs other representation
Protocol vs ABC vs callable vs object
module / package / class placement
constructor / dependency injection shape
sync vs async implementation
transport / framework choice
retry behavior
storage / persistence / retention mechanism
raw payload lifecycle
~~~

Deferred 不等于 backlog，也不等于下一步自动必须决定。它们必须在后续软件架构步骤中由真实需求和 Sufficiency Gate 推动。

---

## 27. Step 3 Verdict

~~~text
Step 3 — Search / Provider Spine Software Design
= CANDIDATE / COMPLETE

Architecture Authority
= NO

Minimum Endpoint
= {TT-17 Search by Keyword}

TT-17 Admission
= PASS_WITH_LIMITATIONS

C3 Search seam
= required and provider-neutral

C4a
= semantic/static binding responsibility

C4b
= concrete Scrape Creators translation boundary behind C3 seam

Pagination / continuation
= bounded, provider-neutral, cursor-hidden from Skill

Duplicates / missingness / identity / time / region / raw referenceability
= preserved as explicit bounded semantics

Walking Implementation
= NOT YET AUTHORIZED
~~~

The Candidate is sufficient to proceed to the next design step without inventing a larger Search platform or a new Contract surface.

---

## 28. Current Next

~~~text
Step 4 — Research / Evidence Software Design
~~~

Step 4 will determine how the provider-neutral Search Result enters：

~~~text
C2a sampling
→ Actual Sample Boundary
→ C5a Evidence formalization
→ Research interpretation
→ Finding
→ Testable Hypothesis
→ C5b Research Result
~~~

Step 4 must continue to respect the Step 3 boundaries：

~~~text
C3 Search Result ≠ Evidence
Raw Provider Result ≠ Evidence
Search Retrieval Bound ≠ Actual Research Sample Boundary
Missingness ≠ evidence interpretation
~~~

---

## Final One-line Conclusion

~~~text
Step 3 is complete as a minimal Candidate Search / Provider software spine: C2b depends on a provider-neutral C3 Search seam, C4a remains static binding, C4b owns bounded TT-17 translation behind that seam, Provider mechanics stay below the boundary, and no Walking Implementation is authorized.
~~~
