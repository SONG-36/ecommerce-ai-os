# Ecommerce AI OS — Round 2A Classification Calibration Record

- **Document type**: Business Task Classification Calibration Record
- **Round**: Round 2A — Classification Cleanup
- **Status**: **CLASSIFICATION RULESET V1.0 — CALIBRATED**
- **Current ruleset**: **V1.1 — CALIBRATED / POST-CLASSIFICATION AUDIT REVISION**
- **V1.0 calibration-time full classification status**: NOT YET EXECUTED
- **Current full 89-Candidate classification status**: COMPLETE / V1.1 TARGETED RE-REVIEW COMPLETE
- **Architecture authority**: No
- **Plan**: `00_ROUND_2_NORMALIZATION_PLAN.md`

---

# 1. Purpose

This record explains why the current Round 2A Classification Ruleset is
sufficiently stable for subsequent full classification of the 89 original
Candidates.

Calibration did not validate the final structure of any Candidate. It tested:

- whether the Primary Classification vocabulary is sufficient;
- whether the Observed Independence Rule works in practice;
- whether Artifact and Work Classification are correctly separated;
- whether the rules remain stable across different business archetypes;
- whether any first-order classification schema defect remains.

The classifications recorded below are calibration results. They are not
canonical Business Task identities or Pass 2B structural dispositions.

---

# 2. Scope / Non-Scope

## 2.1 In Scope

- Record the current Round 2A Classification Ruleset V1.0.
- Record four calibration cases and one holdout validation case.
- Record minor guidance discovered while applying the rules.
- Decide whether the ruleset is calibrated for full Pass 2A classification.

## 2.2 Non-Scope

This calibration record does not:

- classify all 89 Candidates;
- create a Candidate Classification Ledger;
- execute Merge / Split / Remove / Move / Rename;
- create canonical Business Task IDs;
- establish final Candidate boundaries or Domain structure;
- enter Pass 2B;
- modify Product, System, or Software Architecture.

---

# 3. Classification Ruleset V1.0

## 3.1 Primary Classification

```text
BUSINESS_TASK
STEP
ANALYSIS_DIMENSION
PLATFORM_EXECUTION_DETAIL
UNCERTAIN
```

Business Artifact is not a Primary Classification. It is recorded through the
independent Artifact dimension:

```text
artifact_role
artifact_candidate
```

## 3.2 Business Task Decision Rule

Business Task evaluation must use all of the following:

```text
Goal
Trigger
Input
Decision / Work
Output / Completion
Observed Independence
```

Theoretical independence is not sufficient.

Independent Business Task identity requires observable business evidence.
When observable independence is ambiguous, the Primary Classification remains
`UNCERTAIN` rather than being forced to `BUSINESS_TASK`.

---

# 4. Calibration Case 1 — `02 商品研究`

- **Status**: **PASS_WITH_MINOR_GUIDANCE**
- **Test focus**: `BUSINESS_TASK` vs `ANALYSIS_DIMENSION` vs Artifact relationship

## 4.1 Calibration Result

| Candidate | Candidate name | Calibration classification |
|---|---|---|
| `02-01` | Review / 评论区分析 | `UNCERTAIN` |
| `02-02` | Consumer Pain 痛点提取 | `ANALYSIS_DIMENSION` |
| `02-03` | Selling Point 卖点提取与验证 | `UNCERTAIN` |
| `02-04` | 产品改良机会分析 | `BUSINESS_TASK` |
| `02-05` | 使用场景分析 | `ANALYSIS_DIMENSION` |
| `02-06` | 竞品详情页 / Listing 分析 | `UNCERTAIN` |
| `02-07` | 产品差异化机会分析 | `BUSINESS_TASK` |

## 4.2 First-Order Schema Issues Exposed and Repaired

This case first exposed two first-order schema issues that were subsequently
repaired in Ruleset V1.0:

1. `BUSINESS_ARTIFACT` must not be a Primary Classification.
2. The Observed Independence Rule is required so an analyst cannot promote an
   arbitrary Candidate to `BUSINESS_TASK` by inventing a Goal, Trigger, or
   Output.

## 4.3 Minor Guidance

```text
ANALYSIS_DIMENSION
= what dimension is being examined

STEP
= what step is being performed in a workflow
```

---

# 5. Calibration Case 2 — `06 流量与广告`

- **Status**: **PASS_WITH_MINOR_GUIDANCE**
- **Test focus**: `BUSINESS_TASK` vs `STEP` vs `PLATFORM_EXECUTION_DETAIL` vs platform automation

## 5.1 Calibration Result

| Candidate | Candidate name | Calibration classification |
|---|---|---|
| `06-01` | 流量来源分析 | `ANALYSIS_DIMENSION` |
| `06-02` | 广告商品 / 投放机会选择 | `STEP` |
| `06-03` | 广告创建 / Campaign 结构规划 | `BUSINESS_TASK` |
| `06-04` | Keyword / Search Term 优化 | `PLATFORM_EXECUTION_DETAIL` |
| `06-05` | 广告预算分配 | `STEP` |
| `06-06` | Bid / 竞价调整 | `PLATFORM_EXECUTION_DETAIL` |
| `06-07` | 低效 / 无效流量处理 | `UNCERTAIN` |
| `06-08` | 广告表现诊断与优化 | `BUSINESS_TASK` |
| `06-09` | ROI / ROAS 复盘 | `ANALYSIS_DIMENSION` |

## 5.2 Minor Guidance

```text
STEP
= business-process dependent

PLATFORM_EXECUTION_DETAIL
= platform-mechanism dependent
```

Primary Classification remains Candidate-level.

Platform execution differences do not automatically create platform-specific
Primary Classifications. This calibration does not require
platform-conditioned classification.

---

# 6. Calibration Case 3 — `07 内容与达人`

- **Status**: **PASS_WITH_MINOR_GUIDANCE**
- **Test focus**: Creative Production, Creator Operations, outsourced execution, AI-enabled execution, mixed business concerns, and composite Candidate wording

## 6.1 Calibration Result

| Candidate | Candidate name | Calibration classification |
|---|---|---|
| `07-01` | 视频选题 | `UNCERTAIN` |
| `07-02` | Hook / 视频脚本策划 | `UNCERTAIN` |
| `07-03` | Storyboard / 拍摄方案设计 | `UNCERTAIN` |
| `07-04` | 商品素材生产 | `BUSINESS_TASK` |
| `07-05` | 素材筛选 / 剪辑 | `UNCERTAIN` |
| `07-06` | 内容发布计划 | `UNCERTAIN` |
| `07-07` | 内容表现分析 | `UNCERTAIN` |
| `07-08` | 爆款内容结构拆解 | `UNCERTAIN` |
| `07-09` | 达人发现 | `STEP` |
| `07-10` | 达人筛选 | `STEP` |
| `07-11` | 达人邀约 / 合作管理 | `UNCERTAIN` |
| `07-12` | 寄样 / Commission 管理 | `UNCERTAIN` |
| `07-13` | LIVE 策划与复盘 | `UNCERTAIN` |

## 6.2 Minor Guidance

Execution method does not determine Business Task identity.

AI-enabled, external-personnel, outsourced, and internal execution must remain
separate from Task identity.

A Candidate containing multiple lifecycle phases or business concerns may
remain `UNCERTAIN` in 2A and be evaluated for `SPLIT` in 2B.

Ruleset V1.0 does not add `COMPOSITE_TASK` as a Primary Classification.

---

# 7. Calibration Case 4 — `03-10` ↔ selected `09` Candidates

- **Status**: **PASS_WITH_MINOR_GUIDANCE**
- **Test focus**: Analysis → Diagnosis → Optimization Planning → Action

## 7.1 Calibration Result

| Candidate | Candidate name | Calibration classification | Boundary note |
|---|---|---|---|
| `03-10` | Listing 质量 / 异常诊断 | `BUSINESS_TASK` | Exact name and boundary remain unresolved. |
| `09-06` | 商品表现分析 | `UNCERTAIN` | — |
| `09-09` | 经营异常诊断 | `BUSINESS_TASK` | — |

## 7.2 Minor Guidance

Workflow adjacency does not imply Business Task identity.

Even when two units of work occur consecutively, they may remain different
Business Tasks when their Goal, Decision, and Output / Completion are materially
different.

Ruleset V1.0 does not add any of the following as Primary Classifications:

```text
ANALYSIS_TASK
DIAGNOSIS_TASK
PLANNING_TASK
ACTION_TASK
```

---

# 8. Holdout Validation — `08 订单与售后`

- **Status**: **PASS**
- **Role**: Holdout validation; Domain `08` did not participate in Ruleset design

## 8.1 Holdout Result

| Candidate | Candidate name | Holdout classification |
|---|---|---|
| `08-01` | 订单异常处理 | `BUSINESS_TASK` |
| `08-02` | 取消订单处理 | `BUSINESS_TASK` |
| `08-03` | 发货异常处理 | `BUSINESS_TASK` |
| `08-04` | 物流咨询 / 物流异常处理 | `UNCERTAIN` |
| `08-05` | 退货处理 | `BUSINESS_TASK` |
| `08-06` | 退款处理 | `BUSINESS_TASK` |
| `08-07` | 客户咨询 / 消息处理 | `BUSINESS_TASK` |
| `08-08` | 差评 / 投诉处理 | `UNCERTAIN` |

## 8.2 Validation Result

The holdout result shows no evident overfitting of Ruleset V1.0 to analytical,
advertising-oriented, or Creative work.

## 8.3 Minor Guidance

An externally or event-bounded state transition is a strong Observed
Independence signal.

Examples of triggers include:

```text
refund request
return request
cancellation request
order exception
customer inquiry
```

When such a trigger initiates work that produces a recognizable state such as:

```text
resolved
rejected
completed
refunded
cancelled
escalated
```

the observable trigger and state transition provide a strong `BUSINESS_TASK`
signal.

---

# 9. Calibration Summary

| Case | Status |
|---|---|
| `02 商品研究` | **PASS_WITH_MINOR_GUIDANCE** |
| `06 流量与广告` | **PASS_WITH_MINOR_GUIDANCE** |
| `07 内容与达人` | **PASS_WITH_MINOR_GUIDANCE** |
| `03-10` ↔ selected `09` Candidates | **PASS_WITH_MINOR_GUIDANCE** |
| `08 订单与售后` Holdout | **PASS** |

After Calibration Case 1 exposed and drove repair of the Artifact and Observed
Independence issues, the later calibration cases and holdout validation exposed
no new first-order classification schema defect.

---

# 10. Calibration Decision

# **2A Classification Ruleset V1.0 — CALIBRATED**

This means:

> Ruleset V1.0 is sufficiently stable to begin full 89-Candidate Pass 2A
> classification.

It does not mean:

- all 89 Candidates have been classified;
- calibration classifications are the final canonical structure;
- Pass 2B dispositions have been completed;
- Business Task Baseline V1.0 has been formed;
- Product, System, or Software Architecture has changed.

`CALIBRATED` does not mean permanently immutable. Rule Evolution remains
available for newly discovered edge cases.

---

# 11. Rule Evolution

If a new structural edge case appears during full 89-Candidate classification:

```text
pause classification
        ↓
document the edge case
        ↓
revise ruleset version
        ↓
identify affected prior classifications
        ↓
re-review affected Candidates only
```

A local rule revision does not require an unconditional rerun of all
Candidates.

---

# 12. Next Step at V1.0 Calibration Closure

At the time Ruleset V1.0 calibration closed, the formal next step was:

# **Pass 2A — Full Candidate Classification**

Input:

```text
89 original Candidate IDs
+
Round 1 Evidence Matrix
+
2A Classification Ruleset V1.0
```

Output:

```text
Candidate Classification Ledger
```

Pass 2B remains out of scope and is not authorized by this calibration record.

---

# 13. V1.0 Calibration Closure Boundary

The original calibration record closed Ruleset V1.0 calibration only.

It creates no canonical ID, executes no structural disposition, changes no
Round 1 artifact, and changes no Product, System, or Software Architecture
authority.

---

# 14. Post-Classification Audit / Rule Evolution

The completed 89-Candidate classification was audited against the calibrated
Ruleset V1.0. The audit identified three guidance-level edge cases:

## Edge Case 1 — Platform Implementation vs Semantic Identity

Platform-specific implementation was being confused with platform-specific
semantic identity.

The revised Semantic Core Rule requires classification to start from the
underlying business intent. Platform-specific tools, fields, controls, APIs, or
UI do not by themselves justify `PLATFORM_EXECUTION_DETAIL`.

## Edge Case 2 — Inferred vs Observed Independence

Structurally strong independence inference was being over-recorded as directly
observed independence.

V1.1 reserves `observed_independence = YES` primarily for direct real-world
evidence of independence. Strong structural inference without direct AS-IS
observation is recorded as `PARTIAL`, normally with `MEDIUM` classification
confidence.

## Edge Case 3 — Output vs Business Artifact

Ordinary task outputs were being over-promoted to Business Artifacts.

V1.1 requires persistence, handoff, downstream independent consumption, reuse,
or stable business identity before an output tends toward Business Artifact
status. Insufficient evidence remains `UNKNOWN`; an ordinary state or parameter
change with no independent Artifact is `NONE`.

## 14.1 Ruleset Evolution Decision

```text
Ruleset V1.0
        ↓
Ruleset V1.1 — CALIBRATED / POST-CLASSIFICATION AUDIT REVISION
```

This revision:

- keeps the Primary Classification vocabulary unchanged;
- tightens Guidance and Decision Rules;
- adds no new Primary Classification;
- does not invalidate the historical V1.0 calibration results;
- requires targeted re-review only for affected Candidates.

The historical calibration and holdout classifications above are unchanged.
