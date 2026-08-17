# Ecommerce AI OS — Current Handoff

- Project: Ecommerce AI OS
- Repository: `/Volumes/projects/andy/0813/ecommerce-ai-os`
- Document role: Current navigation and handoff state
- Authority status: Navigation only; this file is not an Architecture Authority
- Last synchronized: 2026-08-17

## 0. How To Use This Handoff

Read this file first when entering a new chat or session. It records the
current project state, architecture authority boundaries, First Research
Slice, Required Contracts, Detailed Contract package, deferred status, next
authorized stage, and the next-chat reading order.

This is a navigation layer. It intentionally does not duplicate the full
Product Architecture, System Architecture, Planning Package, Deferred
Register, D1–D5 specifications, or Consistency Review.

When this file conflicts with a Current Authority, follow that Current
Authority and synchronize this handoff. Do not silently change an authority
document while updating this file.

## 1. Current Project Identity

### Project

**Ecommerce AI OS** is a cross-platform, business-first, technology-neutral
system direction for reusable Skills, stable Core responsibilities,
extensible Capabilities, replaceable Providers, Evidence-aware Research, and
future Creative Production, Knowledge-assisted Work, and Experiment &
Validation workflows.

The project evolved from a real TikTok content-production problem:

```text
TikTok content problem
    ↓
Reference content research
    ↓
Cross-platform Research need
    ↓
Evidence-aware decision support
    ↓
Creative Production / Knowledge / Experiment extensions
    ↓
Ecommerce AI OS
```

The project is not defined by the current Provider, one platform, an API
inventory, a framework, or the current source-tree scaffold.

### Current Major Phase

```text
Minimum Scrape Creators Endpoint Selection
= AUTHORIZED NEXT
```

The current phase determines the smallest Provider endpoint subset required by
the already-defined First Research Slice and its stable Contract semantics.

### Explicit Current Status

```text
First Vertical Slice Planning
= COMPLETE

System Detailed Contract Design
= COMPLETE / CONSISTENCY REVIEWED

Detailed Contract Consistency Review
= PASS_WITH_REFINEMENTS

Consistency Refinement Sync
= COMPLETE

Consistency Re-check
= PASS

Minimum Scrape Creators Endpoint Selection
= AUTHORIZED NEXT
```

Software Architecture

```text
NOT YET DESIGNED
```

Walking Implementation

```text
NOT YET AUTHORIZED
```

This is design and selection work, not a code implementation phase.

## 2. Current Architecture Authority Status

| Area | Current Status |
|---|---|
| Product Architecture | CURRENT BASELINE |
| System Architecture V0.2 | Candidate / Human-reviewed working architecture |
| Software Architecture | See explicit status block above |
| First Research Slice Planning | COMPLETE |
| Detailed Contract Design Package | COMPLETE / CONSISTENCY REVIEWED |
| Product Architecture Reopen | NO |
| System Architecture V0.2 Reopen | NO |
| Contract Inventory Reopen | NO |
| New Contract Required | NO |
| Research system placement final resolution | NOT REQUIRED NOW |

Only new, concrete evidence that proves a conflict may reopen a frozen
decision. A new chat, model change, Provider API shape, or implementation
preference is not by itself new evidence.

System Architecture V0.2

```text
Candidate / Human-reviewed working architecture
```

Architecture approval promotion

```text
NOT PERFORMED
```

This handoff does not promote any Candidate to a higher architecture status.

## 3. Current First Vertical Slice

### 3.1 Slice Identity

```text
First Vertical Slice — Research Execution
Business Scenario — US / Car Vacuum / TikTok Content Research
```

### 3.2 Business Decision Served

The slice supports the question:

> Which hypotheses should be prioritized in next US TikTok Car Vacuum content
> experiments?

Research is Decision Support, not the Final Business Decision.

```text
Research
    → Decision Support

Operator / downstream business workflow
    → Final Test Priority Decision
```

The slice produces a human-reviewable Research Result containing, as
applicable, Evidence, Findings, Testable Hypotheses, Answerability,
Limitations, and Traceability / Provenance.

### 3.3 Start Boundary

The slice starts from existing business context and a Research Intent / Need,
not from a Provider API request and not from an isolated keyword.

```text
Product / SKU Context
+ Platform Context = TikTok
+ Market Context = US
+ Business Goal = Commerce Content
+ Research Intent / Decision Need
```

Product / SKU Context is an upstream input. The slice does not create a
complete Product Facts System, Product database, Claim Engine, or Product
ingestion workflow.

### 3.4 End Boundary

First Slice Business End Boundary

```text
Human-reviewable Research Result
```

```text
Business End Boundary
    !=
Execution Closure
```

After the Business End Boundary is satisfied, the same Execution still
continues through execution closure. Execution closure after the Research
Result does not expand the First Slice Business End Boundary.

```text
Human-reviewable Research Result
    ↓
C2a Business Completion
    ↓
C2b Execution Terminalization
    ↓
C6 Execution Record
    ↓
C1 Terminal Return
```

The slice does not own the downstream human decision of which hypothesis to
test first, and it does not claim that a public-content pattern is a validated
business truth.

### 3.5 Stable Slice Semantics

The following semantics must remain visible through later design:

- Explicit Sample Boundary;
- Actual Sample Boundary;
- Evidence References;
- Findings;
- Testable Hypotheses;
- Answerability;
- Limitations;
- Traceability / Provenance;
- post-terminal resolvability of necessary internal references.

```text
Finding
    != Creative Direction

Hypothesis
    != Script

Hypothesis
    != Validated Business Truth

Research Result
    != Final Business Decision
```

## 4. Current Global Responsibility Map

This is a concise responsibility map, not a strict software component graph.

```text
Applications
    ↓
Skills
    ↓
Stable Core
    ↓
Capabilities
    ↓
Foundation Services where independently justified
    ↓
Provider / Integration Boundary
```

### Applications

Application surfaces receive human or external workflow interaction and expose
the resulting business work request. Interaction and transport details remain
Not Yet Designed.

### Skills

```text
Skill = Business Method
```

A Skill expresses how a business method should approach a task. It must not
own Provider-specific API logic.

### Stable Core

Current Stable Core Candidate Areas:

- Task Runtime;
- Skill Extension Mechanism;
- Capability Contract;
- Runtime Governance;
- Execution Record.

Compatibility / Versioning remains cross-cutting rather than a new top-level
Core component.

### Capabilities

```text
Capability = System Ability
```

Search is the required concrete Capability for this slice. Search is
Provider-neutral and is not equivalent to Scrape Creators.

### Foundation Services

Knowledge, Evidence, and Artifact remain Candidate Foundation Service areas in
the global System Architecture. Their independent First-Slice use and detailed
software architecture are not all proven or designed.

Research is a confirmed Product Family. Its final System placement is not
required to be resolved now; the current Contract package is sufficient to
continue.

### Provider / Integration Boundary

```text
Provider Resolution
    ↓
Adapter / Connector
    ↓
Concrete Provider
    ↓
API / SDK / MCP / Native Mechanism
```

```text
Provider
    != Adapter
    != API / SDK / MCP

Provider
    = who actually provides data or capability
```

Provider-specific quirks belong behind C4b or the relevant Contract boundary,
not in the business Skill.

### Cross-cutting Definitions

```text
Agent = Execution / Decision Strategy
Tool  = Invocation / Software Representation
```

Neither Agent nor Tool is a top-level architecture layer for the current
slice.

## 5. Required Contract Inventory

The First Research Slice contains exactly these 9 Required Contracts /
Boundaries:

| ID | Contract / Boundary | Current Status |
|---|---|---|
| C1 | Task Execution Boundary | DETAILED SEMANTICS COVERED + CONSISTENCY REVIEWED |
| C2a | Skill Contract | DETAILED SEMANTICS COVERED + CONSISTENCY REVIEWED |
| C2b | Task Runtime Execution Contract | DETAILED SEMANTICS COVERED + CONSISTENCY REVIEWED |
| C3 | Search Capability Contract | DETAILED SEMANTICS COVERED + CONSISTENCY REVIEWED |
| C4a | Provider Resolution Boundary | DETAILED SEMANTICS COVERED + CONSISTENCY REVIEWED |
| C4b | Scrape Creators Adapter Contract | DETAILED SEMANTICS COVERED + CONSISTENCY REVIEWED |
| C5a | Evidence Contract | DETAILED SEMANTICS COVERED + CONSISTENCY REVIEWED |
| C5b | Research Result Contract | DETAILED SEMANTICS COVERED + CONSISTENCY REVIEWED |
| C6 | Execution Record Contract | DETAILED SEMANTICS COVERED + CONSISTENCY REVIEWED |

The current package contains no tenth Contract.

```text
Contract
    != Component
    != Service
    != Class
    != Process
    != API
```

Do not add Runtime–Skill, Capability Need / Action / Command, Concrete
Provider, Identity, Traceability, or Stable Execution Fact Contracts merely
because their concepts exist. Their necessary semantics are carried by the
existing Contracts and cross-contract obligations unless new evidence proves
otherwise.

## 6. Detailed Contract Design Package

### 6.1 Navigation

```text
docs/02_system/vertical_slices/01_research_execution/contracts/
├── 00_CONTRACT_DESIGN_INDEX.md
├── 01_EXECUTION_SPINE.md
├── 02_SEARCH_INVOCATION.md
├── 03_RESEARCH_SEMANTICS.md
├── 04_EXECUTION_RECORD.md
├── 05_PROVIDER_MAPPING.md
└── 06_DETAILED_CONTRACT_CONSISTENCY_REVIEW.md
```

### 6.2 Document Ownership

```text
01_EXECUTION_SPINE.md
    → C1 + C2b + C2a

02_SEARCH_INVOCATION.md
    → C3 + C4a

03_RESEARCH_SEMANTICS.md
    → C5a + C5b

04_EXECUTION_RECORD.md
    → C6

05_PROVIDER_MAPPING.md
    → C4b

06_DETAILED_CONTRACT_CONSISTENCY_REVIEW.md
    → Package-level Review Record
```

`06_DETAILED_CONTRACT_CONSISTENCY_REVIEW.md` is not D6, not a new Contract,
and not an Architecture Authority.

The package is complete for the current First-Slice Contract stage. This does
not mean Software Architecture, persistence architecture, or implementation
has been designed.

## 7. First Slice Planning Package

```text
docs/02_system/vertical_slices/01_research_execution/
├── 00_READ_ME_FIRST.md
├── 00_FIRST_VERTICAL_SLICE_PLANNING.md
├── 01_SLICE_BUSINESS_BOUNDARY.md
├── 02_RESPONSIBILITY_COVERAGE.md
├── 03_MINIMAL_RUNTIME_PATH.md
├── 04_CONTRACT_INVENTORY.md
├── 05_DEFERRED_REGISTER.md
├── 06_ARCHITECTURE_REVIEW.md
└── contracts/
    ├── 00_CONTRACT_DESIGN_INDEX.md
    ├── 01_EXECUTION_SPINE.md
    ├── 02_SEARCH_INVOCATION.md
    ├── 03_RESEARCH_SEMANTICS.md
    ├── 04_EXECUTION_RECORD.md
    ├── 05_PROVIDER_MAPPING.md
    └── 06_DETAILED_CONTRACT_CONSISTENCY_REVIEW.md
```

The roles are:

- `00_READ_ME_FIRST.md`: human guide to the slice package;
- upstream `00–06`: First Vertical Slice planning evidence and review;
- `contracts/01–05`: D1–D5 Detailed Contract specifications;
- `contracts/06`: package-level consistency review record.

First Vertical Slice Planning

```text
COMPLETE
```

## 8. Critical Invariants — Do Not Collapse

```text
Business Work Request
    != Execution

Skill
    = Business Method

Task Runtime
    = Execution Coordination

Declared Capability Dependency
    != Runtime Capability Need
    != Actual Capability Invocation Fact

Search Capability
    != Scrape Creators

C4a
    = Provider Resolution

C4b
    = Provider Translation

Adapter
    != Concrete Provider
    != API / SDK / MCP

Current Provider Binding
    != Resolved Provider Fact
    != Actually Used Provider Fact

Raw Provider Result
    != Search Capability Result
    != Evidence
    != Finding
    != Testable Hypothesis

Search Retrieval Semantics
    != Actual Research Sample Boundary

Observed Fact
    != Research Interpretation

Missing
    != 0

Insufficient Evidence
    != Execution Failure

Business Result
    != Execution Outcome

Business Completion
    precedes Execution Completion

Execution Record
    != Runtime State
    != Trace
    != Logs
    != Evidence
    != Artifact
    != Observability
    != Evaluation

Local Ownership
    + Cross-boundary Reference

Post-terminal Resolvability
    = REQUIRED SEMANTIC OBLIGATION

Record / Reference Retention Semantics
    = REQUIRED / PARTIALLY REFINED

Exact Retention Lifecycle / Duration
    = NOT YET DESIGNED

Retention / Resolvability
    != Persistence Architecture

Retention Requirement
    != Persistence Architecture
```

## 9. Runtime Semantic Spine

```text
Operator
    ↓
Application
    ↓
C1 Task Execution Boundary
    ↓
C2b Task Runtime
    ↔
C2a Research Skill
```

When the Skill needs Search:

```text
C2a Research Skill
    ↓ provider-neutral Capability Need
C2b Task Runtime
    ↓ coordinates invocation
C3 Search Capability
    ↓ C4a Provider Resolution
C4b Scrape Creators Adapter
    ↓
Scrape Creators / Concrete API
```

Return path:

```text
Raw Provider Result
    ↓ C4b translation / normalization
C3 provider-neutral Search Capability Result
    ↓
C2b Task Runtime
    ↓
C2a Research Skill
```

Research completion path:

```text
Sampling
    → Actual Sample Boundary
    → C5a Evidence
    → Finding
    → Testable Hypothesis
    → C5b Research Result
    → C2a Business Completion
    → C2b Execution Terminalization
    → C6 Execution Record
    → C1 Terminal Return
```

```text
C2b Task Runtime
    = Execution / Capability Invocation Coordination

C2a Research Skill
    = Business Method
```

The Skill must not appear to call C3 directly. The Runtime coordinates the
Capability invocation and result return.

## 10. Detailed Contract Consistency Review Summary

### Review Result

```text
Review Result
= PASS_WITH_REFINEMENTS

Refinement Sync
= COMPLETE

Consistency Re-check
= PASS
```

### Review Gates

All review gates are PASS or PASS_WITH_REFINEMENT_RESOLVED:

1. Identity / Referenceability;
2. Context Propagation;
3. Capability / Provider Isolation;
4. Missingness Semantics;
5. Error / Failure Semantics;
6. Business / Execution Completion;
7. Research Semantic Separation;
8. Traceability / Provenance;
9. Execution Record Integrity;
10. Retention / Post-terminal Resolvability.

### Resolved Findings

```text
CR-1 Retention maturity / post-terminal inheritance
    = RESOLVED

CR-2 Task Reference ownership
    = RESOLVED

CR-3 Resolved Provider vs Actually Used Provider
    = RESOLVED

CR-4 Index stale navigation
    = RESOLVED

CR-5 Forward-reference maturity wording
    = RESOLVED
```

Architecture Reopen

```text
NO
```

Contract Inventory Reopen

```text
NO
```

New Contract Required

```text
NO
```

Research system placement resolution required now

```text
NO
```

The Review Record does not upgrade System Architecture status, create D6,
create a tenth Contract, or authorize unrelated architecture expansion.

## 11. Deferred / Not Yet Designed / Not Yet Proven / Rejected

The current Deferred Register remains the detailed status authority. This
summary is a navigation aid and is not a new backlog.

### 11.1 NOT YET DESIGNED

- Minimum Scrape Creators Endpoint Selection: authorized next, design not yet started;
- exact Search software fields and schemas;
- exact Evidence / Research Result software model;
- exact Execution Record software model;
- exact reference representation;
- exact Runtime state taxonomy;
- exact retention lifecycle and duration;
- Application interaction and transport;
- Software Architecture;
- detailed Provider endpoint subset.

### 11.2 NOT YET PROVEN

- Independent Analyze Capability;
- Independent Retrieve Detail Capability;
- Full Evidence Foundation Service;
- Independent Research Service;
- Skill Composition;
- Retry Engine;
- Checkpoint;
- Crash Recovery;
- Durable Execution;
- Dedicated Persistence Subsystem;
- Specific Database Technology;
- Compatibility Service;
- Provider Schema Registry;
- comprehensive Research Lens taxonomy;
- unified error taxonomy.

### 11.3 NOT REQUIRED FOR FIRST SLICE

- Knowledge Foundation Service;
- Artifact Foundation Service;
- Production Research Workspace / UI;
- active Runtime Governance gates beyond the current thin hook;
- Pause / Continue as an active First-Slice mechanism.

### 11.4 DEFERRED

- Multi-provider Routing;
- Fallback;
- Load Balancing;
- Cost-aware Routing;
- Health-aware Routing;
- Provider Ranking;
- Advanced Dynamic Resolution;
- broader Provider integration beyond the minimum endpoint subset.
- Comments as Evidence Source;
- Operational Observability / C10;

Current First Slice does not require Comments as a mandatory source. Revisit
only if public content / public performance evidence proves insufficient for
the current Research Question.

### 11.5 EXPLICITLY REJECTED FOR CURRENT SLICE

- Agent as Top-level Layer;
- Tool as Top-level Layer;
- Standalone Orchestration Layer;
- Event / Message Architecture as the required First-Slice mechanism;
- Scrape Creators 97 API Full Integration as an OS module or backlog architecture;
- Automatic Research Result → Knowledge Update;
- Dynamic Skill Discovery / Hot Reload / Marketplace.

```text
Absence Does Not Imply Gap
Deferred Does Not Imply Backlog
Not Yet Proven Must Earn Promotion
Primary Status Controls Default Action
```

If this summary conflicts with the current Deferred Register, read the
Register and synchronize this Handoff. Do not modify the Register as part of
ordinary Handoff maintenance.

## 12. Do Not Reopen Without New Evidence

Do not reopen by default:

- Documentation Architecture;
- Product Architecture;
- top-level System Architecture V0.2;
- First Research Slice Business Boundary;
- the 9 Required Contract Inventory;
- D1–D5 Detailed Contract semantics;
- C1–C6 ownership boundaries;
- the C2b-mediated Capability invocation path.

Reopening requires new evidence demonstrating a real semantic conflict,
missing responsibility, or unsatisfied business requirement. Provider API
shape, framework preference, implementation class, or a new chat is not
sufficient.

Do not default-add:

```text
Agent Layer
Tool Layer
Standalone Orchestration Layer
Runtime–Skill Contract
Capability Need / Action / Command Contract
Concrete Provider Contract
Identity Contract
Traceability Contract
Stable Execution Fact Contract
```

## 13. Provider Lab Relationship

### 13.1 Boundary

```text
Provider Lab discovers facts.
Ecommerce AI OS productizes facts.
```

Scrape Creators is currently:

```text
Current Concrete Provider
+ Provider Runtime Fact Source
```

It is not the System Architecture Authority.

### 13.2 Current Provider Facts

The Provider Lab handoff records:

- 97 inventoried unique endpoints;
- Runtime Final Disposition: 92 SUCCESS, 1 BLOCKED_PROVIDER, 1 BLOCKED_RESOURCE_UNAVAILABLE, 3 BLOCKED_SEED_UNDISCOVERABLE;
- L0 Runtime Calibration: 92 CONFIRMED, 0 CORRECTED, 5 UNKNOWN, 0 RULE_CONFLICT;
- L2 intentionally paused;
- Provider Lab freeze anchor: `1b1c35f docs: freeze l0 runtime calibration handoff`.

The 97 API inventory is a Provider fact asset:

```text
97 API Inventory
    != 97 OS Capabilities
    != 97 OS Modules
    != Implementation Backlog
```

The Provider Lab is an external verified asset. It does not define Product
Architecture, System Architecture, or the Required Contract Inventory.

### 13.3 Correct Direction

```text
Stable System Need
    ↓
Contract Semantics
    ↓
C3 / C4a / C4b obligations
    ↓
Provider Lab Facts
    ↓
Minimum Endpoint Subset
```

Do not reverse this into:

```text
97 API Inventory
    ↓
Pick interesting APIs
    ↓
Design Ecommerce AI OS around them
```

## 14. Current Next

### Minimum Scrape Creators Endpoint Selection

```text
Status
= AUTHORIZED NEXT

Goal
= Determine the smallest Scrape Creators endpoint subset required to satisfy
  the current First Research Slice.
```

The decision sequence is:

```text
Business Question
    ↓
Evidence Need
    ↓
C3 Detailed Search Contract
    ↓
C5a / C5b Evidence and Result Requirements
    ↓
C4b Adapter Obligations
    ↓
Provider Lab Facts
    ↓
Minimum Endpoint Subset
```

## 15. Questions For The Next Stage

The next chat must answer these questions. This Handoff does not answer them:

1. Which Provider Facts does the First Slice actually need?
2. Which Provider Facts are mandatory?
3. Which Provider Facts are optional or nice-to-have?
4. Which needs are explicit in the C3 Search Contract?
5. Which needs are explicit in C5a / C5b provenance and Evidence semantics?
6. What translation obligations does C4b impose on endpoint selection?
7. Which Scrape Creators endpoints provide the required Provider Facts?
8. Can one endpoint cover multiple required needs?
9. Is a detail endpoint really required?
10. Is pagination or continuation really required?
11. What are the Provider missingness, region, ID, and compatibility risks?
12. Which endpoints are genuinely non-substitutable?
13. What is the minimum endpoint subset?
14. Is that subset sufficient for the later Walking Slice?

## 16. Next Stage Prohibitions

During Minimum Endpoint Selection:

```text
DO NOT WRITE CODE

DO NOT DESIGN SOFTWARE ARCHITECTURE YET

DO NOT IMPLEMENT ALL 97 APIs

DO NOT ADD A NEW OS CAPABILITY
just because the Provider exposes an endpoint

DO NOT TURN AN ENDPOINT INTO A CONTRACT

DO NOT TURN A PROVIDER FIELD INTO OS SEMANTICS
without Contract justification
```

Endpoint selection remains downstream of stable system need and Contract
obligations.

## 17. Recommended Reading Order For A New Chat

Use these real repository paths. The order is intentionally staged.

### Tier 1 — Mandatory Orientation

1. `docs/00_project/02_CURRENT_HANDOFF.md`
2. `docs/00_project/00_PROJECT_BASELINE_V0.1.md`
3. `docs/00_project/01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md`
4. `docs/01_product/00_PRODUCT_ARCHITECTURE.md`
5. `docs/02_system/00_SYSTEM_ARCHITECTURE.md`
6. `docs/04_governance/00_ARCHITECTURE_GOVERNANCE.md`
7. `docs/02_system/vertical_slices/01_research_execution/contracts/00_CONTRACT_DESIGN_INDEX.md`
8. `docs/02_system/vertical_slices/01_research_execution/contracts/06_DETAILED_CONTRACT_CONSISTENCY_REVIEW.md`
9. `docs/05_references/provider_lab/03_PROVIDER_LAB_ASSET_HANDOFF.md`

### Tier 2 — Required For Current Endpoint Selection

10. `docs/02_system/vertical_slices/01_research_execution/contracts/02_SEARCH_INVOCATION.md`
11. `docs/02_system/vertical_slices/01_research_execution/contracts/03_RESEARCH_SEMANTICS.md`
12. `docs/02_system/vertical_slices/01_research_execution/contracts/05_PROVIDER_MAPPING.md`

### Tier 3 — Read On Demand

13. `docs/02_system/vertical_slices/01_research_execution/01_SLICE_BUSINESS_BOUNDARY.md`
14. `docs/02_system/vertical_slices/01_research_execution/04_CONTRACT_INVENTORY.md`
15. `docs/02_system/vertical_slices/01_research_execution/05_DEFERRED_REGISTER.md`
16. `docs/02_system/vertical_slices/01_research_execution/contracts/01_EXECUTION_SPINE.md`
17. `docs/02_system/vertical_slices/01_research_execution/contracts/04_EXECUTION_RECORD.md`

The upstream package guide is:
`docs/02_system/vertical_slices/01_research_execution/00_READ_ME_FIRST.md`.

## 18. Suggested New Chat Starter

```text
Continue Ecommerce AI OS.

Repository:
/Volumes/projects/andy/0813/ecommerce-ai-os

Read docs/00_project/02_CURRENT_HANDOFF.md first, then follow its
Recommended Reading Order For A New Chat.

Do not redesign Documentation Architecture, Product Architecture, System
Architecture V0.2, or the 9 Required Contracts.

Current completed stage:
System Detailed Contract Design = COMPLETE / CONSISTENCY REVIEWED

Current next:
Minimum Scrape Creators Endpoint Selection

Do not write code.
Do not design Software Architecture yet.

First report your understanding of:
- current project state;
- architecture authority;
- First Research Slice;
- 9 Contract status;
- consistency review result;
- deferred / NYD / NYP boundaries;
- endpoint-selection decision process.

Do not modify the repository until alignment is confirmed.
```

## 19. Recent Milestone Commits

The following hashes were read from the current Ecommerce AI OS Git history:

```text
8b37338 docs: complete research contract consistency review
2702f9f docs: align research contract consistency semantics
0eb9f3d docs: define scrape creators provider mapping contract
58fe910 docs: define research execution record contract
```

These are navigation anchors only. Inspect live Git state before describing
current changes or deciding whether a file is clean.

The Provider Lab has a separate repository and separate freeze anchor. Its hash
must not be confused with an Ecommerce AI OS commit.

## 20. Handoff Update Rules

When synchronizing this file:

1. Read the current authority files from the repository.
2. Confirm live Git status before editing.
3. Update this existing Handoff rather than creating a second Handoff.
4. Preserve the single-authority model.
5. Keep status words explicit and conservative.
6. Record actual commit hashes only when confirmed by `git log`.
7. Keep Provider Lab facts separate from OS architecture decisions.
8. Keep Deferred / Not Yet Designed / Not Yet Proven distinctions intact.
9. Do not turn a Handoff summary into a replacement architecture document.
10. Validate that only the intended Handoff changed.

The following statements must remain true unless new evidence changes the
authority documents:

```text
System Architecture V0.2
    = Candidate / Human-reviewed working architecture

Software Architecture
    = NOT YET DESIGNED

Walking Implementation
    = NOT YET AUTHORIZED

Detailed Contract Design Package
    = COMPLETE / CONSISTENCY REVIEWED

Minimum Scrape Creators Endpoint Selection
    = AUTHORIZED NEXT
```

## 21. Authority Boundary

```text
Project identity / requirements
    → docs/00_project/00_PROJECT_BASELINE_V0.1.md
    → docs/00_project/01_PRODUCT_ORIGIN_AND_REQUIREMENTS.md

Product question
    → docs/01_product/00_PRODUCT_ARCHITECTURE.md

System responsibility question
    → docs/02_system/00_SYSTEM_ARCHITECTURE.md

Architecture status / change governance
    → docs/04_governance/00_ARCHITECTURE_GOVERNANCE.md

First-Slice business boundary
    → docs/02_system/vertical_slices/01_research_execution/01_SLICE_BUSINESS_BOUNDARY.md

Contract inventory / maturity
    → docs/02_system/vertical_slices/01_research_execution/04_CONTRACT_INVENTORY.md
    → docs/02_system/vertical_slices/01_research_execution/05_DEFERRED_REGISTER.md

Detailed Contract semantics
    → docs/02_system/vertical_slices/01_research_execution/contracts/

Provider runtime fact
    → docs/05_references/provider_lab/03_PROVIDER_LAB_ASSET_HANDOFF.md

Implementation fact
    → src/ / tests/ and the live repository state
```

This Handoff is the starting point for navigation. It is not a second Product
Architecture, System Architecture, Software Architecture, Contract, Provider
Lab, or Deferred Register.
