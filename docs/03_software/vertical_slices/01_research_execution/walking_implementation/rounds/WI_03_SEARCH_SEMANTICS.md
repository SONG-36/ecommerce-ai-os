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
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

Implementation
= P1-P4 COMPLETE / HUMAN REVIEWED / PASS

P5
= COMPLETE / TESTED / HUMAN REVIEWED / PASS

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

### P4 Actual Evidence — Serialization / Retained Semantics

```text
P4 — Serialization / Retained Semantics
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P4 Implementation / Tests
= COMPLETE / PASS

P4 Human Review
= PASS

Human Representation Decision
= SearchResult is the Search-owned retained artifact
= SearchFailure is a typed Search outcome projected into C6 on terminal failure

SearchFailure Separate Retained Artifact
= NOT REQUIRED

SearchResult Retained Semantics
= PASS

SearchFailure Owner-Local Serialization
= PASS

Failure C6 Path-Actual Projection
= PASS

Failure C6
= path-actual projection of stable failure / provenance facts
= kind / original code / original reason preserved
= resolved Provider ref preserved only when supplied by SearchFailure provenance
= used Provider ref preserved only when supplied by SearchFailure provenance
= no fabricated capability result ref / RawProviderResultRef

P4 Actual Production Files
= src/ecommerce_ai_os/search/serialization.py
= src/ecommerce_ai_os/runtime/task_runtime.py
= src/ecommerce_ai_os/runtime/execution_record.py

P4 Actual Test Files
= tests/unit/search/test_serialization.py
= tests/integration/test_fake_first_slice.py

SearchResult Retained Shape
= identity / returned boundary / requested bound
= ordered duplicate-preserving occurrences with item / source refs
= explicit known missingness
= distinct UTC publication / observation / collection times
= independent stop / continuation / completion / exhaustion / completeness states
= limitations and provider-neutral provenance
= RawProviderResultRef reference IDs only / no raw payload

SearchFailure Owner-Local Serialization
= kind / failure_code / reason / full provider-neutral provenance
= no SearchFailure identity / directory / retained reference

Representative Retained Runtime Evidence
= search_results/search-rich-fake.json retained A / B / A unchanged
= requested 5 / returned 3 remained distinct
= explicit missingness / distinct UTC times / independent states preserved
= actual capability_result_ref preserved; absent Provider/raw refs remained absent

Focused Search Serialization Tests
= PASS / 3 tests

Focused Search Regression Tests
= PASS / 21 tests

Focused Runtime Regression Tests
= PASS / 9 tests

Full Unit Suite
= PASS / 46 tests

Integration Suite
= PASS / 6 tests

Fake CLI
= PASS / exit 0 / SUCCEEDED / sample size 2 / published Record Ref

python -m compileall -q src tests
= PASS

git diff --check
= PASS

Information-Loss Gap On Tested Retained Paths
= NONE OBSERVED

Bounded Future Evidence Note
= failure-path capability_result_ref / raw_result_refs
= NOT EXERCISED BY CURRENT P4 RUNTIME PATH
= no fabricated refs
= re-evaluate only when real Provider / raw-capture evidence establishes them
= NOT A P4 BLOCKER

F7
= STILL DEFERRED / NOT YET PROVEN

NB-02
= untouched

NB-03
= untouched

NB-04
= untouched

P4 Architecture Deviation
= NONE OBSERVED

Completed Baseline Architecture Deviation
= FOUND / bounded deviations remain outside P4

Architecture Assumption Conflict
= NONE

P5
= NOT AUTHORIZED
```

### P5 Actual Evidence — Full Verification

```text
P5 — Full Verification
= COMPLETE / TESTED / HUMAN REVIEWED / PASS

P5 Human Review
= PASS

WI-03 — Search Semantics
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P5 Production Changes
= NONE

P5 Test Changes
= NONE
```

Final Gates:

| Gate | Actual evidence | Result |
|---|---|---|
| G1 — P1-P4 regression | focused Search / serialization / Research / Runtime and full unit / integration suites passed | `PASS` |
| G2 — Representative runtime paths | rich success, valid empty, continuable failure, non-continuable failure, and contract-invalid outcome all have executable evidence | `PASS` |
| G3 — Rich retained SearchResult | fresh rich Fake bundle retained reviewed C3 facts and resolved all five C6 references | `PASS` |
| G4 — Typed SearchFailure lifecycle | exact continuable failure returned unchanged; non-continuable failure used private unwind and path-sensitive C6 | `PASS` |
| G5 — Information integrity | no loss or false strengthening observed on tested paths | `PASS` |
| G6 — Delete Test / boundary | all eight reviewed mechanisms remain justified; no premature generic framework exists | `PASS` |
| G7 — Documentation / debt sync | NB-04 closed; NB-02/NB-03 carried; F7 deferred | `PASS` |
| G8 — Architecture review | P5 introduced no deviation; Architecture Assumption Conflict remains none | `PASS` |

Five representative paths:

| Path | Exact executable evidence | Runtime meaning | Result |
|---|---|---|---|
| A — Rich Success | `FakeFirstSliceIntegrationTests.test_rich_fake_result_traverses_existing_execution_path`; `test_successful_fake_execution_publishes_resolvable_bundle`; fresh P5 rich Fake bundle | Research → Search → rich A/B/A SearchResult → Research completion → retained rich JSON → successful C6 / resolvable Record Ref | `PASS` |
| B — Valid Empty | `SearchBoundaryTests.test_valid_empty_result_is_not_a_search_failure`; `SearchSerializationTests.test_valid_empty_result_serializes_zero_without_invented_facts` | zero occurrences remains a valid SearchResult and is never strengthened into SearchFailure | `PASS` |
| C — Continuable SearchFailure | `TaskRuntimeCoordinationTests.test_invalid_request_failure_returns_unchanged_to_same_execution` | `INVALID_REQUEST` returns as the exact same SearchFailure to the same caller / Execution; private abort is not called | `PASS` |
| D — Non-continuable SearchFailure | `test_provider_invocation_failure_triggers_private_execution_abort`; `test_provider_resolution_failure_triggers_private_execution_abort`; `FakeFirstSliceIntegrationTests.test_established_failure_closes_with_path_sensitive_record` | provider invocation/resolution failure crosses the private unwind, closes the established Execution, and publishes resolvable failure C6 | `PASS` |
| E — Contract-invalid outcome | `TaskRuntimeCoordinationTests.test_contract_invalid_search_outcome_keeps_defensive_abort` | non-SearchResult / non-SearchFailure becomes bounded `SEARCH_OUTCOME_NOT_RESULT` defensive failure, not typed SearchFailure | `PASS` |

Cross-layer information-conservation review:

| Fact | In-memory representation | Runtime behavior | Serialized form | Retained form | Verdict |
|---|---|---|---|---|---|
| ordered occurrences | ordered tuple | same SearchResult crosses C3/C2b | ordered JSON array | same order in `search_results` | `PRESERVED` |
| duplicates | repeated occurrence allowed | A/B/A is not deduplicated | repeated array entries | A/B/A retained | `PRESERVED` |
| known missingness | `frozenset[str]` | remains absence knowledge, not a fake value | deterministic string list | explicit list per occurrence | `PRESERVED` |
| requested retrieval bound | optional positive integer | remains request bound only | `requested_item_count` | `5` distinct from returned `3` | `PRESERVED` |
| returned boundary | non-negative count equal to occurrences | drives bounded sample only | `returned_item_count` | `3` | `PRESERVED` |
| stopping reason | provider-neutral enum | limitation remains bounded stop | stable enum value | `limitation_reached` | `PRESERVED` |
| continuation | independent enum | availability does not imply completeness | stable enum value | `available` | `PRESERVED` |
| Search completion | bounded-request enum | known incomplete remains explicit | stable enum value | `known_incomplete` | `PRESERVED` |
| Provider exhaustion | independent enum | not exhausted remains distinct | stable enum value | `not_exhausted` | `PRESERVED` |
| global completeness | `UNKNOWN` only | no TikTok population claim | `unknown` | `unknown` | `PRESERVED` |
| publication time | optional UTC-aware datetime | remains distinct from observation | UTC ISO-8601 / null | exact UTC value | `PRESERVED` |
| observation time | optional UTC-aware datetime | remains distinct from publication | UTC ISO-8601 / null | exact UTC value | `PRESERVED` |
| collection time | optional UTC-aware datetime | remains result-level collection fact | UTC ISO-8601 / null | exact UTC value | `PRESERVED` |
| limitations | non-empty tuple entries | bounded caveat remains attached | JSON list | retained list | `PRESERVED` |
| resolved Provider | optional provenance fact | transferred only when actually supplied | value / null | result JSON or failure C6 only when established | `PRESERVED` |
| used Provider | optional provenance fact requiring resolved ref | never inferred from configured/resolved alone | value / null | result JSON or failure C6 only when established | `PRESERVED` |
| capability result ref | optional provenance fact | rich Fake supplies actual retained result ref | value / null | retained on rich result; failure runtime path does not exercise it | `PRESERVED / FAILURE PATH DEFERRED` |
| RawProviderResultRef | opaque reference tuple requiring used Provider | no real P5 raw capture occurred | reference IDs only; no payload | no fabricated runtime raw refs | `TESTED / LIVE EVIDENCE DEFERRED` |
| SearchFailure kind | bounded C3 enum | drives continuable vs private-abort path | stable enum value | continuable in memory; terminal kind in C6 | `PRESERVED` |
| SearchFailure code/reason | non-empty typed facts | exact facts return or cross private unwind | exact strings | exact terminal C6 facts | `PRESERVED` |

False-strengthening audit:

```text
requested market = US != proven complete US population
Provider exhausted != global TikTok completeness
known missing field != empty string / false / zero
configured Provider != resolved Provider
resolved Provider != used Provider
SearchResult != Evidence
SearchFailure != ExecutionAbort
= PASS
```

Read-only Delete Test:

| Mechanism | DELETE? | Reviewed semantic lost if removed |
|---|---|---|
| `SearchResultOccurrence` | `NO` | ordered occurrence-level item/source identity, duplicates, missingness, and times collapse |
| explicit known missingness | `NO` | known absence becomes indistinguishable from false/empty/invented values |
| SearchResult bounded states | `NO` | stop, continuation, request completion, Provider exhaustion, and global completeness collapse into false certainty |
| `SearchInvocationProvenance` | `NO` | actual resolved/used/result/raw-reference facts cannot remain path-sensitive |
| `RawProviderResultRef` | `NO` | Search loses provider-neutral raw referenceability without copying Provider payload |
| typed `SearchFailure` | `NO` | valid empty, typed failure, private unwind, and raw Provider errors can no longer remain distinct |
| `RuntimeResearchExecutionPort` | `NO` | the same-Research-caller / same-Execution C2a↔C2b seam disappears |
| Search-owned serialization | `NO` | retained C3 facts regress to lossy Runtime-owned or ad hoc representation |

Absent-framework audit:

```text
SearchService = ABSENT
SearchRepository = ABSENT
SearchOrchestrator = ABSENT
ProviderRouter = ABSENT
ProviderRegistry = ABSENT
RetryPolicy = ABSENT
FailurePolicyEngine = ABSENT
ContinuabilityService = ABSENT
universal error taxonomy = ABSENT
schema registry = ABSENT
serializer registry = ABSENT
new persistence service = ABSENT
```

Deferred / debt review:

```text
NB-01
= CLOSED

NB-02
= OPEN / CARRIED FORWARD
= post-establishment unexpected software exception closure gap
= required before comprehensive / final First-Slice acceptance
= not a WI-03 blocker

NB-03
= OPEN / CARRIED FORWARD
= application presentation
= not a WI-03 blocker

NB-04
= CLOSED
= living Current Handoff + Architecture-Code Traceability synchronized

F7
= NOT YET PROVEN / DEFERRED
= no backlog commitment is created by this status
```

Executed P5 evidence:

```text
Search focused = PASS / 21 tests
Serialization focused = PASS / 3 tests
Research focused = PASS / 3 tests
Runtime focused = PASS / 9 tests
Full unit = PASS / 46 tests
Integration = PASS / 6 tests
Architecture import direction = PASS / 1 test
Fake CLI = PASS / SUCCEEDED / exit 0 / 5 of 5 required refs resolve
compileall = PASS
git diff --check = PASS
```

Fresh external bundle inspection:

```text
CLI C6
= /tmp/ecommerce-ai-os-WI3-P5-cli.Nlyh6G/executions/c3a0a204-6a68-4794-977a-fa2a4ab062e4/execution_record.json
= required refs 5 / resolved 5

Rich Fake C6
= /tmp/ecommerce-ai-os-WI3-P5-rich.sqkekI/executions/7cade270-948a-4772-8593-6496552b46de/execution_record.json
= required refs 5 / resolved 5
= execution_record / search result / sample boundary / evidence / research result all resolve
= A/B/A order, missingness, requested 5 / returned 3, bounded states,
  distinct UTC times, limitations, and Fake provenance preserved
= resolved Provider / used Provider / raw refs absent because not established
```

```text
P5-introduced Architecture Deviation
= NONE

WI-03-introduced unresolved Architecture Deviation
= NONE

Completed-baseline bounded Architecture Deviations
= NB-02 and NB-03 remain

Architecture Assumption Conflict
= NONE

NB-04
= CLOSED

WI-04 — Scrape Creators Adapter
= NEXT / NOT STARTED / NOT AUTHORIZED BY THIS CLOSURE TASK
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
= WI-04 — Scrape Creators Adapter / NEXT / NOT STARTED / NOT AUTHORIZED BY THIS CLOSURE TASK

P1 — C3 Model Closure
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P2 — Rich Fake SearchResult
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P3 — Typed SearchFailure
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P4 — Serialization / Retained Semantics
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

P4 Implementation
= COMPLETE / TESTED / HUMAN REVIEWED / PASS

P5 — Full Verification
= COMPLETE / TESTED / HUMAN REVIEWED / PASS

P5 Human Review
= PASS

WI-03 — Search Semantics
= COMPLETE / IMPLEMENTED / TESTED / HUMAN REVIEWED / PASS

NB-01
= CLOSED

NB-02
= OPEN / CARRIED FORWARD
= required before comprehensive final First-Slice acceptance
= not a WI-03 blocker

NB-03
= OPEN / CARRIED FORWARD
= application presentation
= not a WI-03 blocker

NB-04
= CLOSED

F7
= NOT YET PROVEN / DEFERRED

WI-04 — Scrape Creators Adapter
= NEXT / NOT STARTED / NOT AUTHORIZED BY THIS CLOSURE TASK

Architecture Expansion
= NOT AUTHORIZED
```
