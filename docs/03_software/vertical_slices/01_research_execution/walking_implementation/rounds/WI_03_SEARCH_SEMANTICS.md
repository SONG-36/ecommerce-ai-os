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
= COMPLETE / HUMAN REVIEWED / PASS

P0 Human Learning
= SUFFICIENT TO PROCEED THROUGH IMPLEMENTATION-DRIVEN LEARNING
= NOT CLAIMED AS COMPLETE MASTERY

P1 — C3 Model Closure
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

WI-03
= IN PROGRESS

Implementation
= P1 COMPLETE / P2 COMPLETE + HUMAN REVIEWED + PASS / P3+ NOT AUTHORIZED

Architecture Expansion
= NOT AUTHORIZED

Architecture Deviation
= NONE OBSERVED

Architecture Assumption Conflict
= NONE
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

### P1 Actual Evidence — C3 Model Closure

```text
P1 — C3 Model Closure
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P2 — Rich Fake SearchResult
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P2 Implementation
= COMPLETE
```

P1 Actual Production Files:

```text
src/ecommerce_ai_os/search/models.py
src/ecommerce_ai_os/search/port.py
src/ecommerce_ai_os/search/fake.py
→ compatibility correction only
```

P1 Actual Test Files:

```text
tests/unit/search/test_boundaries.py
tests/unit/runtime/test_task_runtime.py
tests/unit/research/test_first_slice_skill.py
```

P1 Actual Symbols:

```text
SearchRequest
SearchResultOccurrence
SearchResult
SearchFailure
SearchFailureKind
SearchStopReason
ContinuationState
SearchCompletionState
ProviderExhaustionState
GlobalCompletenessState
SearchInvocationContext
RawResultCapture
SearchInvocationProvenance
RawProviderResultRef
SearchCapability.search
```

Actual B02-B06 symbols and bounded proof:

| ID | Actual symbols | Executed invariant evidence |
|---|---|---|
| B02 | `SearchRequest` | `test_request_is_frozen_provider_neutral_and_can_be_bounded`; `test_provider_mechanics_do_not_leak_into_stable_models`; `test_negative_counts_and_bounds_are_rejected` |
| B03 | `SearchResultOccurrence`; `SearchResult`; `SearchFailure`; `SearchFailureKind`; `SearchStopReason`; `ContinuationState`; `SearchCompletionState`; `ProviderExhaustionState`; `GlobalCompletenessState`; `FakeSearchCapability.search` | `test_result_preserves_bounded_retrieval_states`; `test_duplicate_occurrences_remain_ordered_without_dedupe`; `test_known_missingness_is_explicit_without_a_fake_value`; `test_valid_empty_result_is_not_a_search_failure`; `test_search_failure_is_a_distinct_frozen_c3_outcome`; `test_publication_observation_and_collection_times_remain_distinct`; `test_time_fields_reject_naive_datetimes`; `test_result_count_must_match_explicit_occurrences`; `test_nonzero_result_rejects_empty_occurrences` |
| B04 | `RawResultCapture`; `SearchInvocationContext` | `test_invocation_context_is_narrow_and_carries_opaque_capture` |
| B05 | `SearchInvocationProvenance` | `test_invocation_provenance_preserves_actual_path_facts`; `test_raw_result_refs_require_an_actually_used_provider` |
| B06 | `RawProviderResultRef` | `test_raw_provider_result_ref_is_reference_only` |

Port closure:

```text
SearchCapability.search(
    SearchRequest,
    SearchInvocationContext,
) -> SearchResult | SearchFailure
```

Executed validation:

```text
PYTHONPATH=src python -m unittest tests.unit.search.test_boundaries -v
= PASS / 17 tests

PYTHONPATH=src python -m unittest discover -s tests/unit -v
= PASS / 34 tests

PYTHONPATH=src python -m unittest discover -s tests/integration -v
= PASS / 5 tests

python -m compileall -q src tests
= PASS

git diff --check
= PASS

PYTHONPATH=src python -m ecommerce_ai_os.application.cli \
  --request-id request-wi3-p1-closure \
  --product-context "Car Vacuum" \
  --market US \
  --platform TikTok \
  --business-goal "Commerce Content" \
  --research-question "What content patterns merit human review?" \
  --output-root /tmp/ecommerce-ai-os-WI3-P1-closure.DJUOti/executions
= PASS / exit 0 / SUCCEEDED / sample size 2 / published Record Ref
```

Compatibility evidence:

```text
Transitional compatibility gap
= CLOSED

SearchResult structural coherence
= len(occurrences) == returned_item_count / ALWAYS REQUIRED

FakeSearchCapability
= deterministic provider-neutral occurrence count matches returned_item_count

Existing non-Search unit tests
= PASS / 17 tests

Production Runtime / Research files changed
= NO

P2 rich Fake reality-matrix behavior / SearchFailure runtime control / serialization completion
= P2 RICH FAKE REALITY MATRIX IMPLEMENTED / P3 SEARCHFAILURE RUNTIME
  CONTROL DEFERRED / P4 SERIALIZATION COMPLETION DEFERRED
```

### P2 Actual Evidence — Rich Fake SearchResult

```text
P2 — Rich Fake SearchResult
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

Reality Matrix
= S1-S8 VERIFIED
= N1-N2 VERIFIED REJECTED
= U1-U4 DEFERRED / NOT ENCODED

P2 Actual Production Files
= src/ecommerce_ai_os/search/models.py
= src/ecommerce_ai_os/search/fake.py

P2 Actual Test Files
= tests/unit/search/test_boundaries.py
= tests/integration/test_fake_first_slice.py

Model Guardrails
= AVAILABLE + EXHAUSTED → ValueError
= NO_MATCHES + nonzero returned count → ValueError

Fake Configuration
= optional configured provider-neutral SearchResult
= exact immutable result returned through the existing C3 seam
= default deterministic WI-1 Fake behavior preserved

Rich Runtime Evidence
= test_rich_fake_result_traverses_existing_execution_path / PASS
= ordered A, B, A occurrences and explicit description missingness reached the
  existing Runtime / Research path unchanged

Focused Search Tests
= PASS / 21 tests

Full Unit Suite
= PASS / 38 tests

Integration Suite
= PASS / 6 tests

Fake CLI
= PASS / exit 0 / SUCCEEDED / sample size 2 / published Record Ref

python -m compileall -q src tests
= PASS

git diff --check
= PASS

Production Research Changed
= NO

Production Runtime Changed
= NO

Serialization / Retention Changed
= NO

P3 Implementation
= NOT AUTHORIZED
```

```text
Architecture Deviation
= NONE OBSERVED

Architecture Assumption Conflict
= NONE
```

### P3 Actual Evidence — Typed SearchFailure

```text
P3 — Typed SearchFailure
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P3 Implementation / Tests
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P3 Human Review
= PASS

P3 Actual Production Files
= src/ecommerce_ai_os/research/ports.py
= src/ecommerce_ai_os/runtime/task_runtime.py

P3 Actual Test Files
= tests/unit/research/test_boundaries.py
= tests/unit/runtime/test_task_runtime.py
= tests/integration/test_fake_first_slice.py

First-Slice Runtime Classification
= INVALID_REQUEST → CONTINUABLE → original SearchFailure returned unchanged
= PROVIDER_RESOLUTION → NON-CONTINUABLE → existing private _ExecutionAbort
= PROVIDER_INVOCATION → NON-CONTINUABLE → existing private _ExecutionAbort
= malformed / unsupported SearchFailure.kind → bounded defensive private
  _ExecutionAbort → no uncontrolled RuntimeError escape

Continuable Path
= same caller / same execution id / exact SearchFailure object preserved
= kind / failure_code / reason / provenance preserved
= private _ExecutionAbort not invoked

Non-Continuable Path
= original failure_code / reason preserved through private _ExecutionAbort
= existing WI-02 failed TerminalReturn / path-sensitive C6 / resolvable Record Ref
= no fabricated ResearchResult / Evidence

Contract-Invalid Outcome Defense
= SEARCH_OUTCOME_NOT_RESULT preserved for non-SearchResult / non-SearchFailure values

SearchFailure Provenance
= preserved in memory on the continuable SearchFailure path
= current failure C6 persistence NOT IMPLEMENTED / DEFERRED

Focused Research Boundary Tests
= PASS / 3 tests

Focused Runtime Tests
= PASS / 9 tests

Focused Search Regression Tests
= PASS / 21 tests

Full Unit Suite
= PASS / 43 tests

Integration Suite
= PASS / 6 tests

Fake CLI
= PASS / exit 0 / SUCCEEDED / sample size 2 / published Record Ref

python -m compileall -q src tests
= PASS

git diff --check
= PASS

NB-01
= CLOSED

F7
= STILL DEFERRED / NOT YET PROVEN

NB-02
= lifecycle hardening / untouched / required before final First-Slice acceptance

NB-03
= application presentation / untouched

NB-04
= P5 / final synchronization / untouched

P3 Architecture Deviation
= NONE OBSERVED

Completed Baseline Architecture Deviation
= FOUND / bounded deviations remain outside P3

Architecture Assumption Conflict
= NONE

P4 Implementation
= NOT AUTHORIZED BY THIS CLOSURE TASK
```

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
= P4 — Serialization / Retained Semantics

P1 — C3 Model Closure
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P2 — Rich Fake SearchResult
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P3 — Typed SearchFailure
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P4 — Serialization / Retained Semantics
= NEXT / NOT STARTED

P4 Implementation
= NOT AUTHORIZED BY THIS CLOSURE TASK

Architecture Expansion
= NOT AUTHORIZED
```
