# WI-03 Round Record — Search Semantics

## 1. Round Identity / Status

```text
Round
= WI-03 — Search Semantics

Document Type
= Walking Implementation Round Record

Round Planning
= HUMAN REVIEWED / PASS

Round Record
= CREATED / REVIEWED

P0
= NEXT / READY

Implementation
= NOT STARTED / NOT AUTHORIZED

Architecture Expansion
= NOT AUTHORIZED

Architecture Deviation
= NONE OBSERVED

Architecture Assumption Conflict
= NONE OBSERVED
```

This file is an implementation planning/history record. It is not Architecture
Authority, a Search Architecture Specification, a Master Plan, or Current
Handoff.

## 2. Live Repository Entry Facts

```text
Branch
= main

HEAD
= 639cbcf1459e18a6105f8ef56063bb66b05c7ef9

Pre-Round-Record creation worktree
= CLEAN

Current worktree fact
= WI_03_SEARCH_SEMANTICS.md is untracked
```

Relevant actual Search implementation:

```text
src/ecommerce_ai_os/search/models.py
src/ecommerce_ai_os/search/port.py
src/ecommerce_ai_os/search/fake.py
src/ecommerce_ai_os/search/serialization.py
```

Relevant Runtime integration:

```text
src/ecommerce_ai_os/runtime/task_runtime.py
```

Entry traceability:

```text
B01 SearchCapability
= existing / WI-01 Fake runtime verified

B02 SearchRequest
= existing / TESTED / minimal

B03 SearchResult
= existing / WI-01 minimal runtime verified
= full C3 semantics remain WI-03

B04 SearchInvocationContext
= existing / TESTED / minimal

B05 SearchInvocationProvenance
= NOT YET IMPLEMENTED

B06 RawProviderResultRef
= NOT YET IMPLEMENTED

B07-B09
= NOT YET IMPLEMENTED / later rounds
```

Planned files or symbols are not implementation facts.

## 3. Goal

WI-03 upgrades the existing Fake C3 path from a minimal Search result into the
First-Slice provider-neutral Search data contract required to preserve bounded
Search facts.

Core proof:

```text
SearchResult != list[Video]
```

```text
WI-03
= C3 Search semantics round

WI-03
!= Provider integration round
```

## 4. Scope + Traceability Coverage

Primary coverage:

```text
B02 SearchRequest
B03 SearchResult / SearchFailure
B04 SearchInvocationContext
B05 SearchInvocationProvenance
B06 RawProviderResultRef
```

Cross-cutting coverage:

```text
time semantics
missingness
duplicate occurrence preservation
bounded retrieval
continuation
completeness / limitation
provider-neutral provenance
```

```text
B01
= regression verification only

B07-B09
= later rounds
```

B05 and B06 may be implemented and tested in WI-03. Live Provider and live
raw-result verification remain deferred to WI-05.

## 5. Architecture Inputs + Inherited Invariants

Primary reviewed Architecture inputs:

```text
docs/03_software/vertical_slices/01_research_execution/
03_SEARCH_PROVIDER_SPINE_SOFTWARE_DESIGN.md

docs/03_software/vertical_slices/01_research_execution/
06_MINIMAL_SOFTWARE_ARCHITECTURE_ASSEMBLY.md
```

Walking baselines:

```text
docs/00_project/02_CURRENT_HANDOFF.md
walking_implementation/00_WALKING_IMPLEMENTATION_PLAN.md
walking_implementation/01_ARCHITECTURE_CODE_TRACEABILITY.md
walking_implementation/rounds/WI_01_FAKE_VERTICAL_SLICE.md
walking_implementation/rounds/WI_02_EXECUTION_LIFECYCLE.md
```

The upstream documents retain the full semantics. WI-03 inherits only these
implementation-relevant invariants:

```text
SearchResult != Raw Provider Result
SearchResult != Evidence
Search Retrieval Bound != Research Sample Boundary
Valid Empty SearchResult != SearchFailure
Known Missingness != SearchFailure
Search Completion != Provider Exhaustion != Global Completeness
Configured Provider != Resolved Provider != Actually Used Provider
RawProviderResultRef != Raw Provider Payload
C3 preserves duplicate occurrences
Research owns research dedupe
Provider cursor does not leak above C4b
Publication / Observation / Collection Time remain distinct
SearchCapability Protocol != SearchService
SearchInvocationContext
= execution-scoped / Search-owned / narrowed
!= GlobalContext / Runtime dump
Returned occurrences preserve provider-neutral item/source referenceability;
Provider-specific identity mapping remains later-round work.
```

## 6. Expected Call Path

```text
ResearchSkill
→ ResearchExecutionPort.search(...)
→ RuntimeResearchExecutionPort
→ TaskRuntime-controlled Search invocation
→ SearchCapability seam
→ FakeSearchCapability
→ SearchResult | SearchFailure
→ existing Runtime / Research path
```

WI-03 adds no service, orchestrator, repository, or other runtime hop.

## 7. P0-P5 Checkpoint Plan

| Checkpoint | Goal | Required proof / coverage | Code boundary | Stop |
|---|---|---|---|---|
| P0 — Pre-Code Semantic Review | Human understands the reviewed C3 distinctions | Inherited invariants and round boundaries are understood | None | Human Review |
| P1 — C3 Model Closure | Implement First-Slice B02-B06 stable representations | Search model invariants and unit tests | Search models/ports only unless evidence proves otherwise | Human Review |
| P2 — Rich Fake SearchResult | Exercise realistic successful Search semantics | Duplicates, explicit missingness, valid empty, partial retrieval, continuation, bounded stop, requested US region with bounded semantics, unknown global completeness, distinct observation/collection times | Fake/Search surface | Human Review |
| P3 — Typed SearchFailure | Prove both reviewed SearchFailure paths | Continuable and non-continuable behavior; empty and missingness remain non-failures | Smallest evidence-required Search/Runtime surface | Human Review |
| P4 — Serialization / Retained Semantics | Preserve enriched C3 facts through Search-owned serialization and current retention | No information loss and no real Provider raw payload | Search serialization; retention compatibility only if proved necessary | Human Review |
| P5 — Full Verification | Verify the complete round without new production behavior | Full regression, Fake runtime evidence, bundle inspection, Delete Tests, Human Learning Review, Round Review | Verification only | Human Review |

P3 required path 1:

```text
Continuable SearchFailure
→ C3
→ C2b
→ returned to the same Research caller / same Research Execution
```

P3 required path 2:

```text
Non-continuable SearchFailure
→ existing private ExecutionAbort
→ existing WI-02 failure closure
```

P3 must preserve:

```text
Valid Empty != SearchFailure
Known Missingness != SearchFailure
SearchFailure != ExecutionAbort
SearchFailure != Raw Provider Error
```

P3 must not introduce `RetryPolicy`, `FailurePolicyEngine`,
`ContinuabilityService`, a Retry framework, or a universal error taxonomy.
The exact minimal classification mechanism is not designed in this Round
Record; P3 must determine it from actual code evidence while preserving the
reviewed semantics.

## 8. Allowed / Conditional / Forbidden Changes

Primary allowed production surface:

```text
src/ecommerce_ai_os/search/models.py
src/ecommerce_ai_os/search/port.py
src/ecommerce_ai_os/search/fake.py
src/ecommerce_ai_os/search/serialization.py
```

Primary test surface:

```text
tests/unit/search/test_boundaries.py
```

Conditional only when actual checkpoint evidence requires it:

```text
src/ecommerce_ai_os/runtime/task_runtime.py
src/ecommerce_ai_os/research/ports.py
tests/unit/runtime/test_task_runtime.py
tests/integration/test_fake_first_slice.py
tests/unit/architecture/test_import_directions.py
tests/unit/research/test_boundaries.py
tests/unit/research/test_first_slice_skill.py
```

Compatibility-only, not default:

```text
src/ecommerce_ai_os/research/car_vacuum_tiktok.py
src/ecommerce_ai_os/research/models.py
src/ecommerce_ai_os/runtime/retention.py
src/ecommerce_ai_os/runtime/execution_record.py
src/ecommerce_ai_os/composition.py
```

Any compatibility change requires exact blocking evidence, the smallest
possible change, and no ownership expansion.

Forbidden production surface:

```text
src/ecommerce_ai_os/providers/**
```

Do not implement:

```text
ScrapeCreatorsAdapter
ScrapeCreatorsAccess
ScrapeCreatorsHttpClient
SearchService
SearchRepository
SearchOrchestrator
ProviderRouter
ProviderRegistry
PaginationService
MissingnessService
ProvenanceService
RetryPolicy
FailurePolicyEngine
ContinuabilityService
GlobalContext
UniversalReference
new Contract
new Service
```

## 9. Not In Scope

```text
real Scrape Creators
live TT-17
TT-17 fixture translation
C4a implementation
C4b implementation
Provider Access
Provider cursor mechanics
real raw Provider capture
real Provider error mapping
Research sampling
Research dedupe implementation
Finding
Hypothesis
full Research Method
full C6
Retry / Recovery / Checkpoint
Async / Queue / Scheduler
Database / Repository Layer
Agent / MCP
Architecture expansion
```

## 10. Acceptance Criteria

| Gate | Acceptance requirement |
|---|---|
| G1 Scope Integrity | Only WI-03 semantics are implemented; no later-round Provider or Research work. |
| G2 B02-B06 Representation | Required First-Slice representations exist at planned maturity. |
| G3 Rich SearchResult | SearchResult is richer than a list; ordered occurrences and returned-set boundary survive. |
| G4 Duplicate / Missingness Integrity | Duplicates are preserved; known missingness is explicit; missing is not converted to `0`, `false`, `""`, or inference. |
| G5 Empty / Failure Distinction | Valid empty remains SearchResult; SearchFailure remains distinct. |
| G6 Bounded Retrieval Integrity | Requested bound, actual returned boundary, stop reason, continuation, and completeness limitation are representable; Search Completion, Provider Exhaustion, and Global Completeness remain distinct. |
| G7 Time Semantics | Publication, Observation, and Collection remain distinct. |
| G8 SearchFailure Behavior | Continuable failure returns to the same Research caller/execution; non-continuable failure uses existing private ExecutionAbort; no new Retry/error architecture. |
| G9 Provenance / RawRef Integrity | B05/B06 are implemented without false live Provider claims or raw payload leakage. |
| G10 Serialization / Retained Integrity | Required C3 facts survive JSON and retained representation. |
| G11 Runtime / Dependency Regression | WI-02 lifecycle, import DAG, and existing Fake executable path remain intact. |
| G12 Final Review | Required tests/runtime evidence and Human Learning Review complete; no unresolved Architecture Assumption Conflict; Traceability changes only after actual evidence exists. |

## 11. Learning Focus + Architecture Conflict Rule

Learning focus:

```text
Data Contract
Boundary Model
Information Loss
Missingness
Pagination / Continuation
Bounded Completeness
Provenance
```

Architecture conflict rule:

```text
Code / Test / Runtime Evidence
→ Record contradiction
→ classify:
   Implementation Defect
   or Architecture Assumption Conflict
→ Human Review
→ Architecture change only if explicitly approved
```

```text
Evidence first.
Architecture change second.
```

The following do not automatically constitute an Architecture Assumption
Conflict:

```text
field naming difficulty
serializer omission
legacy constructor compatibility
test fixture inconvenience
minimal Runtime type handling
```

## 12. Current Next

```text
Current Next
= P0 — Pre-Code Search Semantics Review

P0
= NO Python changes
= NO test changes
= NO Provider work
```

```text
P0
→ Human Review
→ explicit P1 authorization
→ implementation only after P1 authorization
```
