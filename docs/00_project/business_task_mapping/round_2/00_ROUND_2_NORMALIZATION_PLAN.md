# Ecommerce AI OS — Business Task Mapping — Round 2 Normalization Plan

- **Document type**: Project / Business Task Normalization Plan
- **Round**: Round 2 — Normalize & Deduplicate
- **Status**: IN PROGRESS / FULL 2A CLASSIFICATION COMPLETE / V1.1 TARGETED RE-REVIEW COMPLETE
- **Input authority**: Round 1 materialized Candidate inventory and evidence records
- **Architecture authority**: No
- **Structural disposition authority**: Round 2
- **Downstream consumer**: Round 3 Prioritization
- **2A ruleset status**: Classification Ruleset V1.1 — CALIBRATED / POST-CLASSIFICATION AUDIT REVISION
- **Calibration record**: `01_ROUND_2A_CLASSIFICATION_CALIBRATION_RECORD.md`

---

# 1. Purpose

Round 2 converts the exploratory Candidate Business Task set produced and
reviewed in Round 1 into a normalized, traceable Business Task model.

Round 1 established that the original 89 Candidate Business Tasks are
sufficiently grounded to proceed into normalization, but did not establish that:

- all 89 Candidates are valid Business Tasks;
- current Candidate boundaries are correct;
- current Domain boundaries are correct;
- all Candidates apply equally across Amazon, Temu, and TikTok Shop;
- operator evidence is saturated;
- platform-specific execution implies separate Business Tasks.

Round 2 therefore owns the formal structural analysis required to determine:

1. what each original Candidate actually represents;
2. which Candidates are true Business Tasks;
3. which Candidates are Business Tasks, Steps, Analysis Dimensions, Platform
   Execution Details, or remain Uncertain, and what Business Artifacts the
   work may produce or consume;
4. which Candidates should be merged, split, renamed, moved, removed, or
   demoted;
5. which cross-platform activities share one canonical Business Task;
6. which differences should remain Platform Variants;
7. how normalized Tasks should be organized into Domains;
8. which normalized Tasks are sufficiently stable to enter
   **Business Task Baseline V1.0**.

Round 2 is a Business Modeling exercise.

It is not an AI implementation exercise.

---

# 2. Round 2 Core Question

Round 2 answers:

> **What is the real Business Task structure behind the original 89 Candidate items?**

It does not answer:

> Which Tasks should be automated first?

That belongs to Round 3.

It also does not answer:

> Which LLM, Agent, Skill, API, MCP, browser automation, workflow engine,
> software framework, or provider should implement a Task?

Those belong to later capability and engineering work.

---

# 3. Authoritative Inputs

Round 2 uses the following Round 1 artifacts as its source package:

```text
docs/00_project/business_task_mapping/round_1/

├── 00_ROUND_1_AS_IS_VALIDATION_SUMMARY.md
├── 01_ROUND_1_REVIEWED_TASK_INVENTORY.csv
└── 02_ROUND_1_OPERATOR_EVIDENCE.md
```

The materialized inventory contains:

```text
89 original Candidate IDs
×
3 platforms
=
267 Candidate × Platform evidence rows
```

The 267 rows are an **Evidence Matrix**.

They are not 267 independent Business Tasks.

The primary structural analysis unit remains the original:

```text
89 Candidate Business Task items
```

Each Candidate may have:

- Amazon evidence;
- Temu evidence;
- TikTok Shop evidence;
- different initial applicability hypotheses;
- different AS-IS review confidence;
- different execution variants.

Platform evidence informs classification.

Platform rows do not create Task identity by themselves.

---

# 4. Evidence Constraints Inherited from Round 1

Round 2 inherits all Round 1 evidence limitations.

Current operator evidence consists of:

```text
Amazon       1 experienced operator
Temu         1 experienced operator
TikTok Shop  1 experienced operator
```

The evidence is:

> expert exploratory evidence

It is not:

> saturated or representative platform-wide evidence.

Therefore Round 2 must not silently transform:

```text
one operator's practice
```

into:

```text
universal platform truth
```

Round 2 must preserve the following distinctions:

```text
Platform Capability
≠
Company AS-IS Practice
≠
Human-performed Activity
≠
Platform-automated Activity
≠
Outsourced Activity
```

It must also preserve:

```text
Operator Statement
≠
Analyst Interpretation
≠
Normalization Decision
```

A structural decision may use analyst reasoning.

It must not rewrite that reasoning as operator evidence.

---

# 5. Round 2 Non-Scope

Round 2 does not perform:

- Business Value prioritization;
- Batch 1 / Batch 2 / Batch 3 selection;
- ROI analysis;
- AI Suitability scoring;
- Engineering Feasibility scoring;
- Skill design;
- Agent design;
- Workflow implementation;
- API selection;
- MCP selection;
- provider selection;
- software architecture redesign;
- Product Architecture redesign;
- System Architecture redesign;
- Software Architecture redesign.

Round 2 may discover implications for Product Architecture.

Such implications must be recorded as:

```text
Architecture Candidate / Governance Question
```

They must not silently modify architecture authority.

---

# 6. Round 2 Operating Model

Round 2 is executed as five ordered passes:

```text
2A — Classification Cleanup
        ↓
2B — Task Boundary Normalization
        ↓
2C — Cross-platform Canonicalization
        ↓
2D — Domain Refactor
        ↓
2E — Baseline Closure
```

The passes are intentionally ordered.

Later passes must not be used to bypass unresolved work from earlier passes.

---

# 7. Pass 2A — Classification Cleanup

## 7.1 Objective

Determine what each of the original 89 Candidate items actually represents.

Round 2 must not assume that an item called a "Task" in the original Candidate
inventory is necessarily a true Business Task.

Each Candidate must first be classified.

---

## 7.2 Primary Classification Vocabulary

The Round 2A Primary Classification vocabulary is fixed as:

```text
BUSINESS_TASK
STEP
ANALYSIS_DIMENSION
PLATFORM_EXECUTION_DETAIL
UNCERTAIN
```

### BUSINESS_TASK

A relatively self-contained unit of business work with a recognizable:

- Business Goal;
- Trigger;
- Input;
- Business Decision / Work;
- Output or Completion condition.

Example pattern:

```text
Trigger
    ↓
Business work / decision
    ↓
Recognizable business outcome
```

---

### STEP

An activity performed as part of a larger Business Task.

A Step normally does not justify an independent Business Task identity when:

- it is triggered only by the parent Task;
- it does not have an independent business outcome;
- its output only enables the next Step;
- operators would not normally initiate it as a standalone piece of work.

---

### ANALYSIS_DIMENSION

One dimension inspected during a broader analytical Task.

Typical examples may include concepts such as:

```text
Consumer Pain
Selling Point
Usage Scenario
Risk
Price
Conversion
```

A dimension may be extremely important without being a standalone Business Task.

---

### PLATFORM_EXECUTION_DETAIL

A platform-specific operation, setting, mechanism, or implementation detail that
may implement part of a Business Task without defining the Business Task itself.

Possible examples include:

```text
Bid setting
GMV Max configuration
Campaign parameter
Amazon-specific listing field
Temu-specific promotion control
```

Platform execution details may remain important Platform Variants.

They do not automatically receive canonical Business Task identity.

#### Semantic Core Rule

A Candidate must not be classified as `PLATFORM_EXECUTION_DETAIL` merely
because its execution uses platform-specific tools, fields, controls, APIs, or
UI.

First identify the semantic core of the Candidate.

If the underlying business goal remains meaningful across platforms while only
the implementation differs, the Candidate should be evaluated as a Business
Task, Step, or Analysis Dimension rather than automatically classified as
`PLATFORM_EXECUTION_DETAIL`.

`PLATFORM_EXECUTION_DETAIL` should be used when the Candidate's semantic core
itself is a platform mechanism, control, setting, or implementation construct.

Use this check:

```text
Would the business intent still exist if the platform changed?

YES
→ do not classify as PLATFORM_EXECUTION_DETAIL solely because implementation differs

NO / semantic core itself is a platform mechanism
→ PLATFORM_EXECUTION_DETAIL Candidate
```

---

### UNCERTAIN

Used when the current evidence is insufficient to classify the Candidate without
unsupported assumptions.

UNCERTAIN is a valid Round 2 result.

It must not be replaced with a forced classification merely to achieve apparent
completion.

---

## 7.3 Artifact Dimension

Business Artifact is independent from Primary Classification.

Primary Classification answers:

> What kind of work is this Candidate?

The Artifact dimension answers:

> What business object might this work produce or consume?

Round 2A records this dimension with:

```text
artifact_role
artifact_candidate
```

Allowed `artifact_role` values are:

```text
NONE
PRODUCES_BUSINESS_ARTIFACT
CONSUMES_BUSINESS_ARTIFACT
PRODUCES_AND_CONSUMES
UNKNOWN
```

`artifact_candidate` records a possible produced or consumed business object.
Schema examples include:

```text
Validated Selling Point
Consumer Pain Evidence
Product Improvement Proposal
Competitor Analysis
Differentiation Proposal
```

These are schema examples only. They are not confirmed artifacts, Candidate
classifications, or Round 2 decisions.

A Candidate whose wording appears to name an Artifact must not receive a new
Primary Classification outside the fixed vocabulary. Its work-unit identity
must still be evaluated, and ambiguity remains `UNCERTAIN`.

### Artifact Qualification Rule

Output is not automatically a Business Artifact.

A Candidate output should tend toward Business Artifact status only when one or
more of the following signals are present:

- persistent business object;
- handoff-able deliverable;
- independently consumed by downstream Tasks;
- independently reusable across time or workflows;
- stable business identity.

An ordinary state change, parameter modification, temporary result, or natural
language restatement does not automatically constitute a Business Artifact.

When the evidence is insufficient:

```text
artifact_role = UNKNOWN
```

When no independent Artifact exists:

```text
artifact_role = NONE
```

Do not invent an Artifact name merely to complete the schema.

---

# 8. Business Task Decision Rule

A Candidate should not be classified as a BUSINESS_TASK based on wording alone.

The following five dimensions must be examined:

| Dimension | Question |
|---|---|
| Goal | What business outcome is the work trying to achieve? |
| Trigger | What event or condition causes the work to begin? |
| Input | What information, evidence, state, or object is required? |
| Decision / Work | What meaningful business judgment or transformation occurs? |
| Output / Completion | What observable result means the work is complete? |

A Candidate becomes a stronger BUSINESS_TASK Candidate when these dimensions are
independently recognizable and the Observed Independence Rule is satisfied.

---

## 8.1 Observed Independence Rule

A Candidate must not be classified as `BUSINESS_TASK` merely because an analyst
can theoretically invent an independent Goal, Trigger, or Output for it.

At least one observable business signal must support independent work-unit
identity. Relevant signals may include:

- independently recognizable trigger;
- independently recognizable deliverable;
- independent business decision;
- independent owner / responsibility;
- operator treats it as a standalone piece of work;
- result is independently reused by multiple downstream tasks;
- explicit operator evidence;
- independent SOP / workflow / artifact.

Absence of evidence proving independence must not be silently converted into
independent Business Task identity.

In ambiguous cases, use:

```text
UNCERTAIN
```

rather than forcing `BUSINESS_TASK`.

### Observed Independence Evidence Rule

`observed_independence = YES` should be reserved primarily for independence
supported by direct real-world evidence, such as:

- explicit operator evidence;
- SOP;
- observed workflow;
- operational Artifact;
- independent owner / responsibility;
- explicit standalone work-unit evidence.

When independence is strongly inferred only from the Candidate's event
boundary, state transition, or Goal / Trigger / Output structure, without direct
AS-IS observation, use:

```text
observed_independence = PARTIAL
classification_confidence = MEDIUM
```

Structural clarity alone must not automatically be upgraded to `YES / HIGH`.
`PARTIAL` does not prevent classification as `BUSINESS_TASK`.

---

## 8.2 Task Test

Use the following test:

```text
Does it have an independent Business Goal?
                │
          ┌─────┴─────┐
          │           │
         NO          YES
          │           │
          ↓           ↓
   likely Step /   Does it have
   Dimension /     a recognizable Trigger?
   Uncertain            │
                  ┌─────┴─────┐
                  │           │
                 NO          YES
                  │           │
                  ↓           ↓
             likely child   Is there meaningful
             structure      Decision / Work?
                                  │
                            ┌─────┴─────┐
                            │           │
                           NO          YES
                            │           │
                            ↓           ↓
                     likely Step /    Is there
                     Execution Detail recognizable
                                     Completion?
                                         │
                                   ┌─────┴─────┐
                                   │           │
                                  NO          YES
                                   │           │
                                   ↓           ↓
                              needs review  BUSINESS_TASK
                                           Candidate
```

This is a decision aid.

It is not a mechanical scoring formula.

---

# 9. Pass 2A Output

Pass 2A produces a:

## Candidate Classification Ledger

Minimum logical fields:

```text
candidate_id
candidate_name
source_domain

primary_classification

business_goal
trigger
input
decision_or_work
output_or_completion

observed_independence
independence_evidence

artifact_role
artifact_candidate

classification_confidence
classification_rationale

evidence_refs
open_question
```

Allowed `observed_independence` values are:

```text
YES
PARTIAL
NO
UNCERTAIN
```

Allowed `classification_confidence`:

```text
HIGH
MEDIUM
LOW
```

Every original Candidate must retain its original ID.

No canonical Business Task ID is created in 2A.

---

## 9.1 Round 2A Calibration Set

Round 2A does not use a single Domain to freeze global classification rules.

It uses multiple types of calibration cases:

### Calibration Case 1 — `02 商品研究`

Purpose:

> Test `BUSINESS_TASK` vs `ANALYSIS_DIMENSION` vs Artifact relationship.

### Calibration Case 2 — `06 流量与广告`

Purpose:

> Test `BUSINESS_TASK` vs `PLATFORM_EXECUTION_DETAIL` vs platform automation.

### Calibration Case 3 — `07 内容与达人`

Purpose:

> Test Creative Production, Creator Operations, outsourced / hybrid execution,
> and mixed business concerns.

### Calibration Case 4 — `03-10` + selected `09` Candidates

Purpose:

> Test analysis vs diagnosis vs optimization planning / action boundary.

After these calibration cases, use a Domain that did not participate in rule
design:

### Holdout Validation Case — `08 订单与售后`

Purpose:

> Verify that the rules have not overfit analytical or advertising-oriented
> tasks.

---

## 9.2 Calibration Freeze Rule

Before full 89-Candidate Pass 2A classification begins, all of the following
must be true:

1. `02` calibration completed;
2. `06` calibration completed;
3. `07` calibration completed;
4. `03` ↔ `09` calibration completed;
5. `08` holdout validation completed;
6. no unresolved first-order classification schema defect remains.

Only then may the ruleset status become:

```text
2A Classification Ruleset V1.0 — CALIBRATED
```

Before this gate passes, the ruleset must not be described as frozen or
calibrated.

---

## 9.3 Rule Evolution

Even after Ruleset V1.0 is calibrated, a new structural edge case found during
full 89-Candidate classification triggers this controlled flow:

```text
pause classification
        ↓
document the edge case
        ↓
revise ruleset version
        ↓
identify previously classified Candidates affected by the rule change
        ↓
re-review only affected Candidates
```

A local rule revision does not require an unconditional rerun of all 89
Candidates. The re-review scope must follow the impact of the changed rule.

---

## 9.4 Current Ruleset Version

The post-classification audit triggered the controlled evolution:

```text
2A Classification Ruleset V1.0
        ↓
2A Classification Ruleset V1.1 — CALIBRATED / POST-CLASSIFICATION AUDIT REVISION
```

V1.1 tightens Guidance and Decision Rules only:

- Primary Classification vocabulary is unchanged;
- no new Primary Classification is introduced;
- the V1.0 calibration remains valid;
- only Candidates affected by the revised rules require targeted re-review.

---

# 10. Pass 2B — Task Boundary Normalization

## 10.1 Objective

Once Candidate types are understood, determine the correct structural treatment
of each original Candidate.

2B answers:

> What should happen to this Candidate in the normalized Business Task model?

---

## 10.2 Structural Disposition Vocabulary

Allowed Round 2 dispositions:

```text
KEEP
MERGE
SPLIT
RENAME
MOVE
REMOVE

DEMOTE_TO_STEP
DEMOTE_TO_DIMENSION
DEMOTE_TO_ARTIFACT

UNRESOLVED
```

---

### KEEP

Candidate remains materially valid as a Business Task.

Its wording and Domain placement are sufficiently appropriate for the current
normalization stage.

KEEP does not imply architecture freeze.

---

### MERGE

Two or more original Candidates represent one normalized Business Task boundary.

A Merge must preserve all source Candidate lineage.

---

### SPLIT

One original Candidate combines multiple materially independent Business Tasks.

The new normalized Tasks must retain lineage to the original Candidate.

---

### RENAME

The underlying Business Task remains valid, but its Candidate name does not
accurately express the normalized business outcome.

---

### MOVE

The Candidate remains valid but belongs to another normalized Domain.

---

### REMOVE

The Candidate should not survive as an independent element in the normalized
Business Task model.

REMOVE requires an explicit rationale.

Valid reasons may include:

- duplicate Business Task identity;
- invalid Candidate;
- platform-only execution detail;
- task no longer exists in the relevant normalized model;
- structural meaning is completely represented elsewhere.

Operator deletion alone is not sufficient evidence for REMOVE.

---

### DEMOTE_TO_STEP

The Candidate remains meaningful but becomes a Step inside another Business
Task.

---

### DEMOTE_TO_DIMENSION

The Candidate becomes an Analysis Dimension within another analytical Business
Task.

---

### DEMOTE_TO_ARTIFACT

The Candidate is better modeled as a reusable Business Artifact than as an
independent Business Task.

This is a future 2B structural disposition, not a 2A Primary Classification
value. The possible Artifact relationship remains recorded separately through
`artifact_role` and `artifact_candidate`.

---

### UNRESOLVED

Current evidence does not justify a stable disposition.

UNRESOLVED must retain:

- source Candidate;
- current hypotheses;
- unresolved decision;
- evidence gap;
- next evidence required.

---

# 11. Pass 2B Boundary Rules

Two Candidate items should not be merged merely because they:

- have similar names;
- use the same data;
- are performed by the same operator;
- belong to the same platform;
- occur in the same workflow;
- could be implemented by the same future Skill.

The strongest Merge signal is similarity of:

```text
Business Goal
+
Trigger
+
Decision / Work
+
Output
```

Conversely, two Tasks should remain independent when they have materially
different:

- business outcomes;
- triggers;
- decisions;
- completion conditions;
- ownership / lifecycle;
- downstream consequences.

---

# 12. Pass 2B — Known Hotspots from Round 1

Round 1 already identified high-priority normalization hotspots.

Round 2 should examine these first.

---

## 12.1 `02 商品研究`

Round 1 identified likely over-segmentation.

Two strong structural groups exist:

```text
02-02 Consumer Pain
02-03 Selling Point
02-04 Product Improvement Opportunity
```

and:

```text
02-05 Usage Scenario
02-06 Competitor Listing Analysis
02-07 Product Differentiation Opportunity
```

Round 2 must not pre-merge these groups.

2A must first determine whether each item is:

```text
BUSINESS_TASK
ANALYSIS_DIMENSION
STEP
PLATFORM_EXECUTION_DETAIL
UNCERTAIN
```

Its possible produced or consumed Artifact must be recorded separately through
`artifact_role` and `artifact_candidate`.

Only then may 2B determine the correct normalized boundary.

---

## 12.2 `03 Listing` ↔ `09 Performance Analysis`

Temu Candidate `03-10` was described by the operator as:

> 搞一个优化方案

Round 2 must determine whether the work is primarily:

```text
Listing optimization
```

or:

```text
Product performance diagnosis
        ↓
Optimization planning
```

or a linked pair of Tasks.

The current evidence does not authorize a pre-decided Move.

---

## 12.3 `06 流量与广告`

Round 1 identified material Platform Variants, especially around TikTok GMV Max.

Round 2 must distinguish:

```text
shared business intent
```

from:

```text
platform-specific execution model
```

Candidates such as Product Selection, Bid Adjustment, Campaign Setup, Budget,
ROI Target, and Traffic Optimization may have different structural roles across
platforms.

---

## 12.4 `07 内容与达人`

Round 1 identified a strong structural issue:

```text
Creative Production
```

and:

```text
Creator / Affiliate Operations
```

are currently mixed in one source Domain.

Round 2 must test whether these represent:

- separate Domains;
- separate Task families;
- linked workflows;
- shared Business Artifacts;
- platform-specific variants.

No final Domain split is assumed before 2D.

---

# 13. Pass 2B Output

Pass 2B produces a:

## Normalization Decision Ledger

Minimum logical fields:

```text
decision_id

source_candidate_id
source_classification

proposed_disposition

target_normalized_task
target_domain_candidate

decision_rationale
evidence_refs
decision_confidence

open_question
status
```

Every structural disposition must be traceable.

---

# 14. Pass 2C — Cross-platform Canonicalization

## 14.1 Objective

Determine which platform-specific manifestations represent the same underlying
Business Task and which require materially distinct normalized identities.

Round 2 must avoid two opposite errors:

### Error A — Platform Siloing

```text
Amazon task
Temu task
TikTok task
```

are treated as three separate Business Tasks merely because the platform differs.

### Error B — Over-Abstraction

Materially different Business Tasks are forced into one shared abstraction only
because their high-level goal sounds similar.

---

# 15. Canonical Task Identity Rule

Cross-platform Candidates may share one Canonical Business Task when their:

```text
Business Goal
Decision Structure
Output / Completion
```

are materially equivalent.

Differences in:

```text
data source
schema
API
platform UI
metrics
platform terminology
provider
execution mechanism
```

do not automatically create separate Business Task identities.

Those differences may instead be represented as:

> Platform Variants.

---

# 16. Platform Variant

A Platform Variant represents meaningful platform-specific execution beneath a
shared Business Task.

Example conceptual structure:

```text
Canonical Business Task
        │
        ├── Amazon Variant
        ├── Temu Variant
        └── TikTok Shop Variant
```

A Platform Variant may differ in:

- trigger implementation;
- available data;
- platform metric semantics;
- platform constraints;
- execution actions;
- workflow;
- automation level;
- operational terminology;
- risk;
- evidence quality.

Platform Variant does not imply separate Business Goal.

---

# 17. When Not to Canonicalize

Two platform activities should remain separate normalized Business Tasks when
their differences materially change:

- Goal;
- Trigger;
- Decision;
- Output;
- lifecycle;
- business ownership;
- consequence.

Cross-platform reuse is desirable.

Correct Business Modeling is more important than forced reuse.

---

# 18. Pass 2C Output

Pass 2C produces:

## Canonical Task + Platform Variant Map

Minimum logical objects:

```text
canonical_task_id
canonical_task_name
canonical_business_goal

source_candidate_ids

supported_platforms

platform_variants

canonical_trigger
canonical_input
canonical_decision
canonical_output

variant_notes

evidence_refs
normalization_confidence
```

Canonical IDs are created only after the corresponding Task boundary is
sufficiently stable.

---

# 19. Canonical Task ID Policy

Round 2 may create canonical Business Task IDs.

Suggested form:

```text
BT-001
BT-002
BT-003
...
```

The number itself carries no business semantics.

Do not encode:

- Domain;
- Platform;
- priority;
- implementation;
- Skill;
- provider;

into the Canonical Task ID.

This prevents later structural changes from invalidating identity.

---

# 20. Lineage Requirement

Every Canonical Business Task must preserve source lineage.

Example:

```text
BT-017 Product Improvement Analysis

source lineage:
├── 02-02
├── 02-03
└── 02-04
```

If source Candidates receive different dispositions, lineage must preserve that
difference.

Example:

```text
02-02
→ DEMOTE_TO_DIMENSION
→ used by BT-017

02-03
→ DEMOTE_TO_ARTIFACT
→ produced / consumed by BT-017 and other Tasks

02-04
→ normalized into BT-017
```

Round 2 must never replace lineage with only a final Task name.

---

# 21. Pass 2D — Domain Refactor

## 21.1 Objective

After Task identities are sufficiently normalized, determine whether the
original 10 Domain structure remains appropriate.

Domain design follows normalized Tasks.

Normalized Tasks must not be forced to fit the original Domain structure.

---

# 22. Domain Refactor Rules

A Domain should represent a coherent Business Responsibility Area.

Domain boundaries should be based primarily on:

- Business Goal family;
- task lifecycle;
- responsibility;
- business object;
- decision context.

Domain boundaries should not primarily be based on:

- platform UI navigation;
- software module;
- API grouping;
- current team structure;
- implementation technology.

---

# 23. Round 1 Domain Signals

Round 1 identified the following areas requiring special review:

```text
02 商品研究
→ over-segmentation / normalization pressure

03 Listing
→ possible diagnostic boundary problem

06 流量与广告
→ strong Platform Variant pressure

07 内容与达人
→ structural boundary problem

09 Performance Analysis
→ possible overlap with diagnostic work
```

Other source Domains currently have:

> no major domain-level issue observed

but they are not considered validated or frozen.

---

# 24. Pass 2D Output

Pass 2D produces a:

## Normalized Domain Model

Each Domain should include:

```text
domain_id
domain_name
domain_purpose
included_canonical_tasks
boundary_notes
source_domain_lineage
open_questions
```

The normalized number of Domains is not predetermined.

Round 2 may produce:

```text
fewer than 10
10
more than 10
```

if justified by the normalized Task structure.

---

# 25. Pass 2E — Baseline Closure

## 25.1 Objective

Determine which normalized Business Tasks and Domains are sufficiently stable to
enter:

# Business Task Baseline V1.0

Round 2 completion is not measured by how much the number 89 decreases.

The goal is structural quality and traceability.

---

# 26. Business Task Baseline V1.0 Minimum Task Contract

Each Canonical Business Task admitted to the baseline should minimally define:

```text
canonical_task_id
canonical_task_name

business_goal
trigger
input
decision_or_work
output_or_completion

domain

supported_platforms
platform_variants

source_candidate_lineage

normalization_rationale
evidence_refs
confidence
open_questions
```

This is not yet the detailed Business Task Card.

Detailed Task Cards are expected primarily for high-priority Tasks selected
after Round 3.

---

# 27. Round 2 Processing Order

Round 2A starts with calibration, not full Candidate classification.

Use the ordered calibration and validation sequence:

```text
02 商品研究
        ↓
06 流量与广告
        ↓
07 内容与达人
        ↓
03-10 + selected 09 Candidates
        ↓
08 订单与售后 — Holdout Validation
```

Only after the Calibration Freeze Rule passes may full 89-Candidate Pass 2A
classification begin.

The full classification must still cover every source Domain:

```text
01 市场与选品
02 商品研究
03 Listing / 商品管理
04 定价与促销
05 库存与供应链
06 流量与广告
07 内容与达人
08 订单与售后
09 经营分析
10 店铺治理与合规
```

"No major issue observed" from Round 1 does not mean:

> structurally correct.

Every Candidate must eventually receive a Round 2A classification or explicit
`UNCERTAIN`.

Full 89-Candidate classification is authorized only after the Calibration
Freeze Rule passes. That gate is now satisfied by Classification Ruleset V1.0.

---

# 28. Evidence Reopening Rule

Round 2 does not conduct another full operator survey by default.

The workflow is:

```text
Normalization analysis
        ↓
Candidate structural hypothesis
        ↓
Is existing evidence sufficient?
        │
   ┌────┴────┐
   │         │
  YES        NO
   │         │
   ↓         ↓
Decision   Identify exact
           Evidence Gap
                ↓
        targeted evidence request
```

Possible evidence sources include:

- focused operator question;
- workflow observation;
- platform documentation;
- actual platform data;
- company SOP;
- existing operational artifact.

Only evidence necessary for the specific structural decision should be gathered.

---

# 29. Targeted Operator Question Rule

Do not ask:

> "Please review the whole inventory again."

Ask:

> "When this exact situation occurs, what do you actually do?"

Good examples:

```text
When a Temu product performs poorly,
which data do you inspect before producing the optimization plan?
```

or:

```text
When Amazon product video is outsourced,
which parts remain owned internally:
brief, creator selection, review, revision, approval, or publishing?
```

Operators provide AS-IS facts.

They are not required to design the Business Task ontology.

---

# 30. Evidence Strength

Normalization decisions should carry explicit confidence.

Suggested levels:

### HIGH

Multiple evidence sources align and the Business Task boundary is materially
clear.

### MEDIUM

The structural interpretation is strong but rests on limited evidence or one
experienced operator.

### LOW

The normalization is plausible but materially dependent on inference.

Low-confidence structural changes should normally remain:

```text
UNRESOLVED
```

or carry an explicit Open Question.

---

# 31. Decision Record Requirement

Every material:

```text
MERGE
SPLIT
REMOVE
MOVE
DEMOTE
```

must record:

```text
what changed
why
source Candidates
target Task / structure
evidence
confidence
open uncertainty
```

KEEP and simple RENAME decisions may use lighter rationale when no meaningful
structural controversy exists.

---

# 32. Prohibited Normalization Shortcuts

Round 2 must not:

- merge Candidates only because names are similar;
- merge Candidates only because one future Skill could implement them;
- split Candidates only because platforms have different APIs;
- create one Task per platform by default;
- infer AS-IS confirmation from operator silence;
- treat `initial_applicability` as operator evidence;
- treat outsourced work as nonexistent work;
- treat platform automation as proof the business need disappeared;
- remove a Candidate solely because an operator deleted it during Round 1;
- force all 89 Candidates into resolved status;
- optimize the model for AI implementation;
- optimize the model for current software architecture.

---

# 33. Required Round 2 Logical Artifacts

Round 2 must produce at least three logical data objects.

They may later be represented as files or tables.

---

## A. Candidate Classification Ledger

Purpose:

> What was each original Candidate actually classified as?

---

## B. Normalization Decision Ledger

Purpose:

> What structural decision was made for each source Candidate and why?

---

## C. Canonical Business Task Baseline

Purpose:

> What normalized Business Task model will Round 3 consume?

---

# 34. Optional Supporting Artifact

A fourth supporting object may be created if needed:

## Platform Variant Matrix

Purpose:

```text
Canonical Task
×
Amazon
×
Temu
×
TikTok Shop
```

It should make platform similarities and execution differences explicit without
duplicating canonical Task identity.

---

# 35. Round 2 Completion Gate

Round 2 may close only when all of the following are true.

### Gate 1 — Source Coverage

Every one of the original 89 Candidate IDs has:

- a Round 2 classification;
- or explicit `UNCERTAIN`.

---

### Gate 2 — Disposition Coverage

Every original Candidate has:

- a structural disposition;
- or explicit `UNRESOLVED`.

---

### Gate 3 — Lineage

Every normalized Task can trace back to all relevant original Candidate IDs.

No Candidate silently disappears.

---

### Gate 4 — Canonical Identity

Every accepted Canonical Business Task has:

- a unique canonical ID;
- a stable normalized name;
- a defined Business Goal;
- recognizable Trigger;
- recognizable Output / Completion.

---

### Gate 5 — Platform Model

Cross-platform reuse and Platform Variants are explicitly represented.

Platform difference alone must not create separate Business Task identity.

---

### Gate 6 — Domain Model

Canonical Tasks are organized into a coherent normalized Domain model.

Source Domain lineage remains visible.

---

### Gate 7 — Evidence

All material structural decisions have:

- rationale;
- evidence reference;
- confidence.

---

### Gate 8 — Uncertainty

Unsupported cases remain explicitly unresolved.

Round 2 does not force false certainty.

---

### Gate 9 — Architecture Boundary

No Product, System, or Software Architecture baseline is silently changed by the
normalization work.

Architecture implications, if any, are recorded separately for governed review.

---

# 36. Round 2 Closure Status

The intended successful Round 2 closure status is:

# **COMPLETE FOR PRIORITIZATION**

This means:

> The normalized Business Task model is sufficiently stable and traceable to
> begin Round 3 prioritization.

It does not mean:

- every platform operating model has been exhaustively discovered;
- all evidence gaps are permanently resolved;
- Business Task Baseline V1.0 can never evolve;
- every baseline Task will become a Skill or Agent;
- Product Architecture has automatically changed.

---

# 37. Round 3 Handoff

Round 3 receives:

```text
Business Task Baseline V1.0
+
Platform Variant Model
+
Normalization Lineage
+
Remaining Open Questions
```

Round 3 then evaluates Tasks using dimensions such as:

```text
Business Value
Frequency / Labor Cost
AI Suitability
Engineering Feasibility
Risk
```

and produces:

```text
Batch 1
Batch 2
Batch 3
```

Only after Round 3 prioritization should detailed Task Cards and downstream
Capability / Skill / Agent engineering be concentrated on the Tasks selected for
implementation work.

---

# 38. Round 2 Execution Summary

```text
Round 1
89 Candidate Tasks
        │
        ▼
2A Classification Cleanup
        │
        │ Task?
        │ Step?
        │ Analysis Dimension?
        │ Platform Detail?
        │ Uncertain?
        │
        │ Separate Artifact role / candidate?
        ▼
2B Boundary Normalization
        │
        │ Keep
        │ Merge
        │ Split
        │ Rename
        │ Move
        │ Remove
        │ Demote
        ▼
2C Cross-platform Canonicalization
        │
        │ Canonical Task
        │ +
        │ Platform Variants
        ▼
2D Domain Refactor
        │
        ▼
Normalized Business Domain Model
        │
        ▼
2E Baseline Closure
        │
        ▼
Business Task Baseline V1.0
        │
        ▼
Round 3 Prioritization
```

---

# 39. Current Next Step

Round 2A calibration is complete and recorded in:

```text
01_ROUND_2A_CLASSIFICATION_CALIBRATION_RECORD.md
```

Current ruleset status:

```text
2A Classification Ruleset V1.1 — CALIBRATED / POST-CLASSIFICATION AUDIT REVISION
```

The full 89-Candidate classification and V1.1 targeted re-review are complete.
The current 2A output is:

```text
02_ROUND_2A_CANDIDATE_CLASSIFICATION_LEDGER.csv
```

No subsequent pass is authorized by this ruleset-evolution update. Pass 2B
remains out of scope.
