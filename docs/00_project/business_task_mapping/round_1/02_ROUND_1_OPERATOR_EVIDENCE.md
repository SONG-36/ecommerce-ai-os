# Ecommerce AI OS — Business Task Mapping — Round 1 Operator Evidence

- **Document type**: Project / Requirements Evidence Record
- **Round**: Round 1 — AS-IS Validation
- **Status**: **COMPLETE FOR NORMALIZATION / NOT SATURATED**
- **Architecture authority**: No
- **Evidence form**: Supplied review notes; not a verbatim transcript

## 1. Purpose

This document preserves the operator evidence currently available for the
Amazon, Temu, and TikTok Shop Round 1 reviews. It keeps two layers separate:

1. **Operator Statement** — what the operator reported or did during review;
2. **Structured Interpretation** — what an analyst may reasonably carry into
   normalization as a Candidate conclusion or Open Question.

Structured Interpretation is not Operator Fact. It must not be quoted or
represented as though the operator said it.

## 2. Evidence Handling Rules

- The statements below are normalized summaries supplied in the Round 1
  handoff. Except where an exact phrase is explicitly shown, they are not
  verbatim quotations.
- No missing transcript detail, task name, rationale, or Candidate row is
  reconstructed.
- Operator silence is not Candidate confirmation.
- “Does not perform” is kept within the reviewed operator/company context and
  is not generalized into “the platform does not support this work.”
- An operator deletion action is evidence for a possible removal; Round 1 does
  not remove the Candidate.
- Outsourced execution remains visible as AS-IS business activity.
- Platform Capability, Company AS-IS practice, Human-performed activity, and
  Platform-automated activity are not interchangeable.

## 3. Evidence Reference Scheme

Evidence references use the following local identifiers:

```text
R1-AMAZON-01 ... R1-AMAZON-04
R1-TEMU-01   ... R1-TEMU-03
R1-TIKTOK-01 ... R1-TIKTOK-03
```

These identifiers reference statements in this document. They supplement the
materialized authoritative 89-Candidate inventory but do not replace a source
interview transcript.

## 4. Amazon

### 4.1 Operator Statement

#### R1-AMAZON-01 — Product improvement-related work

The Amazon operator treated Candidates `02-02`, `02-03`, and `02-04` as work
related to product improvement.

#### R1-AMAZON-02 — Product differentiation-related work

The Amazon operator treated Candidates `02-05`, `02-06`, and `02-07` as work
related to product differentiation.

#### R1-AMAZON-03 — High-frequency creator operations

The Amazon operator reported that they do not undertake TikTok-style
high-frequency creator operations.

This statement is bounded to the reviewed operating context. It does not state
that Amazon has no creator, influencer, or affiliate-related activity.

#### R1-AMAZON-04 — Video activity and external execution

The Amazon operator reported the existence of brand-promotion videos and
influencer-shot videos. These are usually completed by personnel outside the
domestic operating team.

### 4.2 Structured Interpretation

- `02-02` / `02-03` / `02-04` form a strong Merge Candidate around Product
  Improvement. The exact normalized boundary remains a Round 2 question.
- `02-05` / `02-06` / `02-07` form a strong Merge Candidate around Product
  Differentiation. The exact normalized boundary remains a Round 2 question.
- The two groups contribute to the finding that `02 商品研究` may be
  over-split. This does not authorize a merge in Round 1.
- The absence of TikTok-style high-frequency creator operations in this
  context indicates a Platform Variant or company operating-model difference;
  it does not justify globally removing creator-related work.
- Brand-promotion and influencer-shot video remain AS-IS business activities
  even when execution is outsourced or assigned to overseas personnel.
- Video production evidence supports reviewing the boundary between Creative
  Production and Creator / Affiliate Operations. It does not by itself decide
  their final Domain placement.

### 4.3 Open Questions for Round 2

- What exact business outcome distinguishes Product Improvement from Product
  Differentiation after normalization?
- Should the Candidates inside each group merge, and what lineage must the
  normalized task retain?
- Which video activities are Creative Production, which are Creator / Affiliate
  Operations, and which require links across both?
- How should external execution be represented without confusing task
  ownership, execution owner, execution mechanism, and business outcome?

## 5. Temu

### 5.1 Operator Statement

#### R1-TEMU-01 — Candidate `03-10`

The Temu operator described the actual work represented by `03-10` as:

> 搞一个优化方案

No broader wording or final task name is inferred from this phrase.

#### R1-TEMU-02 — High-frequency creator operations

The Temu operator reported that they do not undertake TikTok-style creator
operations.

This statement is bounded to the reviewed operating context and does not prove
the absence of all creator-related platform capabilities or externally
performed work.

#### R1-TEMU-03 — AI product display images

The Temu operator reported that AI product display image production exists in
their AS-IS work.

### 5.2 Structured Interpretation

- `03-10` may describe formulation of an optimization plan rather than only a
  narrow Listing action. This creates a Candidate boundary question between
  `03 Listing` and `09 Performance Analysis`.
- The current evidence is insufficient to rename or move `03-10` in Round 1.
- The absence of TikTok-style creator operations indicates a Platform Variant
  or company operating-model difference, not a universal absence claim.
- AI product display image production is Creative Production activity within
  the observed AS-IS workflow. Its exact relationship to Listing remains a
  Round 2 boundary question.

### 5.3 Open Questions for Round 2

- What inputs trigger the `03-10` optimization plan, and what output marks its
  completion?
- Is diagnosis part of `03-10`, an upstream Performance Analysis task, or a
  linked but separate task?
- Should AI product display image production be represented as a shared
  Creative Production task with a Temu-specific context or execution variant?

## 6. TikTok Shop

### 6.1 Operator Statement

#### R1-TIKTOK-01 — Deletion actions

During review, the TikTok Shop operator deleted Candidates `06-02`, `06-06`,
and `07-13`.

These actions are preserved as operator review evidence. The Candidates remain
part of the original 89-Candidate lineage and are not removed in Round 1.

#### R1-TIKTOK-02 — Review depth

The TikTok Shop review depth was lower than the Amazon and Temu reviews.

#### R1-TIKTOK-03 — Remaining Candidates

The review did not provide enough item-level evidence to treat all remaining
Candidates as individually confirmed.

### 6.2 Structured Interpretation

- `06-02`, `06-06`, and `07-13` are removal questions for Round 2, not completed
  removals.
- Each deletion requires a reason check: the task may be absent from the
  company AS-IS workflow, performed by another role, outsourced, automated by
  the platform, duplicated elsewhere, or genuinely invalid. The current
  evidence does not select among these explanations.
- No positive review status should be inferred for other TikTok Shop rows from
  lack of edits or comments.
- TikTok GMV Max is a material Platform Variant identified by Round 1 synthesis
  for `06 流量与广告`; its detailed task mapping is not established by the
  available operator statements in this document.

### 6.3 Open Questions for Round 2

- Why did the operator delete each of `06-02`, `06-06`, and `07-13`?
- Does each deletion indicate non-applicability, duplication, automation,
  outsourcing, role separation, or a genuine removal candidate?
- Which `06 流量与广告` intents are shared across platforms, and which require
  a TikTok GMV Max execution variant?
- Which remaining TikTok Shop Candidates require focused re-review before a
  structural disposition can be made?

## 7. Cross-Platform Evidence Boundaries

The combined operator evidence supports carrying the following distinctions
into Round 2:

| Distinction | Required interpretation boundary |
|---|---|
| Platform Capability vs Company AS-IS | A platform may support work that the reviewed company does not currently perform. |
| Human-performed vs Platform-automated | Automation concerns execution mechanism; it does not automatically eliminate the business task or need. |
| In-team vs External execution | Who performs the work concerns execution owner; external execution remains part of AS-IS business work when it contributes to the business outcome. |
| Shared intent vs Platform Variant | Similar outcomes may require materially different platform execution, including TikTok GMV Max. |
| Operator Statement vs Analyst Interpretation | Only the former is operator evidence; the latter remains Candidate analysis until normalized and reviewed. |

## 8. Evidence Gaps

- Full row-level operator notes are not available here.
- Interview dates, prompts, transcripts, and participant metadata beyond
  platform and experience level are not available in the supplied evidence.
- TikTok Shop review depth is insufficient for item-by-item confirmation.
- One operator per platform cannot establish saturation.

These gaps do not block Round 2 from beginning. They must be reopened when a
normalization decision would otherwise depend on an unsupported assumption.

## 9. Relationship to the Inventory CSV

`01_ROUND_1_REVIEWED_TASK_INVENTORY.csv` materializes all 89 original
Candidates in long format across Amazon, Temu, and TikTok Shop, for 267 data
rows. Its `initial_applicability` values preserve the pre-review Candidate
hypotheses from the original table; they are not operator AS-IS evidence.

Every row:

- preserve the original Candidate ID and source lineage;
- reference applicable evidence IDs from this document;
- distinguish missing review evidence from confirmation;
- keep operator notes separate from analyst notes;
- record proposed structural treatment only as a `structure_flag` or
  `round2_question`, never as a completed Round 1 disposition.
