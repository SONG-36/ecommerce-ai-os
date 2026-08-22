# Lifecycle Demo Harness Plan

## 0. Document identity

| Field | Value |
|---|---|
| Document Type | `Developer / Learning Tool Plan` |
| Architecture Authority | `NO` |
| Business Capability | `NO` |
| Runtime Architecture Change | `NO` |
| Design Direction | `ACCEPTED` |
| Current Status | `REVIEWED / IMPLEMENTATION-READY` |
| Implementation | `AUTHORIZED` |
| Current Next Implementation Step | `lifecycle_demo success scenario only` |
| Related Milestone | `WI-02 — Execution Lifecycle / COMPLETE / PASS` |
| Current Product Milestone | `WI-03 — Search Semantics / NEXT / NOT STARTED / NOT AUTHORIZED` |

This document is the canonical implementation plan for a small, developer-only
terminal visualization of the already-verified WI-02 lifecycle. It is not a new
Product, System, Software, Runtime, Contract, or observability architecture
specification.

## 1. Purpose

WI-02 already proves the four required Execution lifecycle paths through tests,
runtime evidence, finalized C6 records, retained artifacts, resolvable Record
Refs, and architecture-to-code traceability. Those surfaces are authoritative
engineering evidence, but they are not optimized for quick human learning.

The Lifecycle Demo Harness will provide a compact terminal view, similar to a
state/debug trace used in embedded or ADAS development:

```text
input
→ lifecycle stage
→ important function
→ success / failure
→ terminal state
→ evidence source
```

Its learning chain is:

```text
Business Meaning
↕
Lifecycle Meaning
↕
Important Python Function
↕
Evidence Source
```

The Demo is not a replacement for tests, C6, retained artifacts, or Runtime
Evidence.

## 2. Governing rule and scope

> **Observe the Runtime. Do not become the Runtime.**

The Demo executes the real current WI-02 `TaskRuntime` lifecycle implementation
and derives its report from the returned response, retained artifacts, and
strictly demo-local observations. It may use the existing Fake Search behavior
and controlled demo-local failure dependencies through existing seams.

```text
Real Runtime Lifecycle
!= Live Provider Execution
```

“Real Runtime” means the current production `TaskRuntime`, execution, C6, and
retention code paths are exercised. It does not mean live TikTok access, a live
Provider, Scrape Creators, TT-17, production data, network access, or a production
environment.

In scope:

- one small developer tool, preferably `tools/lifecycle_demo.py`;
- the four existing WI-02 paths;
- terminal timeline and final-state visualization;
- evidence-backed Record Ref and artifact checks;
- demo-local controlled failure setup;
- an `all` command with a result-derived summary matrix.

Out of scope:

- any change to production Runtime semantics or APIs;
- any new business behavior or Search semantics;
- a live Provider execution path;
- a new public response, Contract, Service, state machine, or event model;
- retry, recovery, cleanup, checkpoint, or retention policy;
- production logging, tracing, metrics, or observability infrastructure;
- WI-03 implementation.

## 3. Runtime observation provenance

```text
Semantic Flow
!= Observed Runtime Trace
```

Every displayed item must carry exactly one primary provenance label. A semantic
step must not be presented as directly observed unless the current implementation
actually exposes evidence for it.

### `[RUNTIME]`

Directly observed from the public Runtime response.

Examples:

- `PreExecutionRejection`;
- `TerminalReturn`;
- `execution_id` when present;
- `execution_outcome`;
- `business_result`;
- `record_ref`.

### `[ARTIFACT]`

Verified from retained or finalized execution artifacts.

Examples:

- final bundle exists;
- `execution_record.json` exists;
- C6 terminal outcome and path-sensitive fields;
- every required reference resolves;
- the returned Record Ref resolves;
- no final bundle or valid Record Ref exists after controlled publication
  failure.

### `[DEMO]`

Observed through a demo-local controlled dependency, wrapper, or narrowly scoped
patch.

Examples:

- Search invocation observed;
- controlled Search non-result triggered;
- Business Completion observed through a local wrapper;
- publication attempted;
- controlled publication failure triggered.

### `[SEMANTIC]`

An approved WI-02 lifecycle explanation used for learning, but not claimed as an
independently instrumented Runtime event.

Examples:

- Execution Establishment Commit;
- lifecycle ownership explanation;
- private `_ExecutionAbort` unwind;
- TaskRuntime regaining lifecycle control, when inferred from the externally
  verified post-unwind result rather than directly instrumented.

When multiple evidence sources support a stage, the timeline may show additional
supporting sources in detail, but the primary source label must remain accurate.
If a fact is inferred, it must say so.

## 4. Visualization must not drive production design

The diagram adapts to available evidence. The Runtime does not adapt to the
diagram.

If a desired stage cannot be observed using:

1. the current public Runtime response;
2. retained artifacts;
3. an existing dependency seam; or
4. a demo-local wrapper or controlled double;

the implementation must show it as `[SEMANTIC]`, omit it, or display `not
independently observed`.

It must not modify production Runtime solely to expose that stage. The following
are forbidden for this Demo:

- production observer APIs or lifecycle callbacks;
- an `EventBus`;
- a `LoggingService`;
- an Observer Contract, debug Contract, or lifecycle event Contract;
- production instrumentation hooks;
- production fault-injection flags or APIs;
- changes to `TaskRuntime` or the production CLI solely for visualization.

Human-readable labels such as `EXECUTION_ESTABLISHED` or `CLOSURE_FAILED` are
Demo labels only. They are not new Domain Events, enums, or Contracts.

## 5. The four required scenarios

The Demo covers exactly the four paths already verified by WI-02.

### 5.1 Success

Semantic flow:

```text
BusinessWorkRequest
→ Admission PASS
→ Execution Established
→ Research Started
→ Search Invoked
→ SearchResult
→ Research Completion
→ Business Completion
→ Success C6
→ Publication
→ Record Ref
→ TerminalReturn(SUCCEEDED)
```

Expected final shape:

```text
Execution           = YES
Business Result     = PRESENT
Execution Outcome   = SUCCEEDED
Clean Closure       = YES
Record Ref          = PRESENT
Record Ref Resolves = YES
```

The default composed Fake First Slice must be used. The path is real WI-02
Runtime execution with synthetic Fake Search data, not live Provider execution.

### 5.2 Pre-execution rejection

Semantic flow:

```text
BusinessWorkRequest
→ Admission REJECTED
→ STOP
```

Expected final shape:

```text
Execution       = NO
Execution ID    = ABSENT
Research Started= NO
Business Result = ABSENT
C6              = ABSENT
Record Ref      = ABSENT
```

```text
PreExecutionRejection
!= Execution Failure
```

Use an invalid First-Slice `BusinessWorkRequest` that violates the existing
reviewed admission rule. Absence of Research and Search calls may be established
through demo-local observation; absence of execution fields comes from the
public rejection response; absence of artifacts comes from the temporary root.

### 5.3 Established execution failure

Semantic flow:

```text
BusinessWorkRequest
→ Admission PASS
→ Execution Established
→ Research Started
→ Search Invoked
→ non-continuable Search outcome
→ Execution Failure
→ private ExecutionAbort
→ control unwinds to TaskRuntime
→ bounded failure facts recorded
→ Failure C6
→ Publication
→ Record Ref
→ TerminalReturn(FAILED)
```

Expected final shape:

```text
Execution           = YES
Business Result     = ABSENT
Execution Outcome   = FAILED
Failure C6          = PRESENT
Clean Closure       = YES
Record Ref          = PRESENT
Record Ref Resolves = YES
```

Human explanation:

```text
✗ Business work failed
✓ Failure itself was cleanly closed
```

Use a demo-local controlled Search capability through the existing
provider-neutral constructor seam. It should reproduce the already-tested
non-`SearchResult` outcome. Do not implement the deferred `SearchFailure`
semantics.

### 5.4 Closure failure

Semantic flow:

```text
BusinessWorkRequest
→ Admission PASS
→ Execution Established
→ Research Started
→ Search
→ Research Completion
→ Business Completion
→ Business Result exists
→ success C6 finalized in memory
→ Publication attempt
→ Publication FAILURE
→ TerminalReturn(FAILED)
```

Expected final shape:

```text
Execution         = YES
Business Result   = PRESENT
Execution Outcome = FAILED
Clean Closure     = NO
Record Ref        = ABSENT
```

Human explanation:

```text
✓ Business work succeeded
✗ Execution closure failed
```

```text
Business Completion
!= Execution Completion

Business Result
!= Execution Outcome
```

Use a demo-local controlled failure at the existing publication boundary. The
Demo may report observed staging state as a fact, but must not turn it into a
cleanup, recovery, or retention policy.

## 6. Private `_ExecutionAbort` boundary

```text
Execution Failure
!= ExecutionAbort

ExecutionAbort
= private C2b unwind mechanism
```

`_ExecutionAbort` must remain private and Runtime-owned. The Demo must not catch
it outside `TaskRuntime`, import it as an application-facing type, expose the
exception object, or add it to a public response.

Preferred display:

```text
[07] ↩ Private Execution Unwind
     mechanism: _ExecutionAbort
     visibility: PRIVATE / Runtime-owned
     source: SEMANTIC
```

Externally verifiable consequences must come from the failed `TerminalReturn`
`[RUNTIME]` and the published failure C6 / resolvable Record Ref `[ARTIFACT]`.

## 7. Controlled failure strategy

Failure injection preference is fixed in this order:

1. existing constructor or dependency-injection seam;
2. demo-local controlled test double or wrapper;
3. narrowly scoped local monkey patch, only when necessary;
4. production fault-injection API — **FORBIDDEN**.

For established execution failure, prefer a demo-local Search capability double
injected through `TaskRuntime(search_capability=...)`.

For closure failure, prefer an existing seam or demo-local wrapper. If the live
code still provides no injectable publication dependency, a narrowly scoped
stdlib `unittest.mock.patch` around `StagingExecutionBundle.publish()` is
acceptable. The patch must exist only around one scenario execution and must be
restored automatically.

Do not add any of the following to production APIs:

```text
fail_publish=True
simulate_failure=True
debug_failure=True
test_mode=True
```

The controlled failure is a Demo mechanism, not a new Runtime feature.

## 8. Evidence-derived scenario result

Each scenario should return a small demo-local result model used by both the
detailed renderer and the `all` matrix. Its fields should be derived after the
real execution, for example:

```text
scenario
execution_established
business_result_present
execution_outcome
clean_closure
record_ref_present
record_ref_resolves
observations
```

Expected scenario values are assertions against this derived result, not the
source of the displayed values. If observed values differ from expectations,
the Demo must display the mismatch and fail the harness run.

`Clean Closure` must be derived from evidence:

- success or established failure: published final bundle plus resolvable Record
  Ref and required references;
- rejection: not applicable because no Execution exists;
- closure failure: false because publication failed and no valid Record Ref was
  returned.

## 9. Terminal presentation

The default output should be deliberately visual but compact.

Symbols:

```text
✓ completed / valid / present
✗ failed
⚠ abnormal but intentionally handled
→ normal progression
↩ private/internal control unwind
○ absent / not reached / not applicable
```

ANSI colors may be used:

```text
green  = success
red    = failure
yellow = exceptional but intentionally handled
cyan   = normal flow
gray   = absent / not reached
```

Color must not be the only carrier of meaning. Output must remain understandable
when colors are unavailable or redirected.

Example shape:

```text
╔══════════════════════════════════════════════════════════════╗
║  WI-02 LIFECYCLE DEMO — EXECUTION FAILURE                  ║
╚══════════════════════════════════════════════════════════════╝

 [01] ✓ Business Work Request
      │  source: DEMO
      ▼
 [02] ✓ Admission
      │  fn: TaskRuntime._pre_execution_rejection()
      │  source: SEMANTIC
      ▼
 [03] ✓ Execution Established
      │  execution_id = ...
      │  fn: TaskRuntime.execute()
      │  source: RUNTIME
      ▼
 ...
```

The actual source label must match what the implementation can prove. A label in
this example is not permission to overclaim provenance.

Every scenario ends with a small final-state panel:

```text
──────────────────────────────────────────────────────────────
 FINAL STATE
──────────────────────────────────────────────────────────────

 Execution           ✓ YES
 Business Result     ○ ABSENT
 Outcome             ✗ FAILED
 Failure Recorded    ✓ YES
 Clean Closure       ✓ YES
 Record Ref          ✓ PRESENT
 Record Resolves     ✓ YES
```

Do not dump every object, serialized field, helper, or stack frame. A timeline
row should normally show only sequence, stage, important identity/fact, one
architecture-bearing function when useful, and provenance.

## 10. Important function mapping

Show approximately five to eight load-bearing functions per path at most. The
current verified candidate pool is:

| Function | Learning meaning |
|---|---|
| `TaskRuntime.execute()` | Execution lifecycle and coordination owner |
| `TaskRuntime._pre_execution_rejection()` | Existing pre-execution admission decision |
| `CarVacuumTikTokResearchSkill.run()` | Business Method execution and `ResearchCompletion` |
| `RuntimeResearchExecutionPort.search()` / `TaskRuntime._invoke_search()` | Runtime-controlled, provider-neutral Search invocation |
| `TaskRuntime._abort_execution()` | Initiates the private C2b unwind |
| `StableExecutionFacts.record_execution_failure()` | Promotes bounded failure facts into stable execution facts |
| `StableExecutionFacts.finalize_failure()` / `finalize_success()` | Path-sensitive terminal C6 finalization |
| `StagingExecutionBundle.publish()` | Physical bundle validation and publication |
| `LocalJsonRetention.resolve_record_ref()` | Verifies a published Record Ref resolves |

Select only the functions that carry the meaning of the current path; do not
print every helper, serializer, mapper, cast, builder, or artifact write. This is
not a Python call-trace profiler.

Exact names must be rechecked against the live repository immediately before
implementation. A stale name in this plan must not be preserved by changing
production code to fit the document.

## 11. Command surface and exit semantics

Preferred implementation file:

```text
tools/lifecycle_demo.py
```

Required commands:

```bash
PYTHONPATH=src python tools/lifecycle_demo.py success
PYTHONPATH=src python tools/lifecycle_demo.py rejection
PYTHONPATH=src python tools/lifecycle_demo.py execution-failure
PYTHONPATH=src python tools/lifecycle_demo.py closure-failure
PYTHONPATH=src python tools/lifecycle_demo.py all
```

CLI process exit semantics are about whether the Demo verified the requested
scenario, not whether the demonstrated business Execution succeeded:

- exit `0` when the real observed result matches the expected lifecycle shape;
- therefore the expected `FAILED` execution and closure-failure scenarios still
  exit `0` when correctly demonstrated;
- exit non-zero for an unexpected exception, evidence/provenance check failure,
  observed/expected mismatch, invalid command, or incomplete `all` run;
- `all` exits `0` only when all four executions and all four checks pass.

Do not make a deliberately demonstrated `TerminalReturn(FAILED)` look like a
broken Demo process.

## 12. Temporary runtime artifacts

By default, every scenario must use a stdlib `TemporaryDirectory` outside the
repository, with an `executions` child as the Local JSON retention root.

The scenario must execute, resolve references, inspect C6 and bundle state, and
derive its immutable summary while the `TemporaryDirectory` context is still
open. When that context exits, the temporary root is deleted by the standard
library. A path printed for diagnosis must therefore be labelled `temporary` and
must not be presented as durable or resolvable after the command finishes.

For `all`, each scenario should remain isolated. Its compact derived result may
survive in memory after that scenario's temporary directory is cleaned; raw
artifact paths must not be used after cleanup.

The Demo must not:

- write bundles into tracked repository paths;
- imply durability beyond the current Local JSON representation;
- add a retention-duration or cleanup policy;
- preserve failed staging data as a new policy decision.

## 13. `all` summary matrix

`all` must execute all four real scenarios and derive the final matrix from the
four scenario results produced by those executions.

Expected semantic shape:

```text
Scenario             Execution   Biz Result   Outcome     Record Ref
--------------------------------------------------------------------
Success              YES         YES          SUCCEEDED   YES
Rejection            NO          NO           N/A         NO
Execution Failure    YES         NO           FAILED      YES
Closure Failure      YES         YES          FAILED      NO
```

The matrix must not be a hard-coded fake result pretending execution occurred.
Hard-coded expected values may be used only to validate actual derived values.

## 14. Implementation constraints

Prefer the Python standard library:

- `argparse` for the command surface;
- `tempfile` and `pathlib` for temporary artifact roots;
- `unittest.mock` only for a narrowly scoped closure-failure patch when needed;
- small local formatting helpers for symbols and optional ANSI color.

Do not add `rich` or another formatting dependency. Do not introduce an
`EventBus`, `LoggingService`, Observer Contract, observability subsystem, plugin
system, or framework.

The tool should mainly:

1. build a request;
2. compose current Runtime components;
3. supply a demo-local controlled dependency where required;
4. execute the real Runtime;
5. inspect the public response and temporary retained artifacts;
6. create a compact derived scenario result;
7. render the timeline, final state, and matrix.

It must not become another Runtime, orchestration layer, lifecycle
implementation, testing framework, or production CLI.

## 15. Implementation order

Implementation must proceed in this order:

```text
success
→ rejection
→ execution-failure
→ closure-failure
→ all
```

Each step should reuse the same small result/provenance model and be checked
before the next scenario is added. This order starts from the existing composed
path, then adds progressively narrower demo-local control.

## 16. Validation and acceptance

Before implementation is presented for review, verify at minimum:

- all five required commands run;
- each scenario executes the current Runtime path rather than printing a
  prewritten answer;
- every displayed fact has accurate provenance;
- the four final-state combinations match the WI-02 matrix;
- returned Record Refs resolve exactly where expected;
- closure failure returns no fabricated Record Ref;
- `_ExecutionAbort` remains private and is not caught or exposed by the Demo;
- controlled patches are scenario-local and automatically restored;
- temporary artifacts are inspected before cleanup and not described as durable;
- expected failed lifecycle scenarios use process exit `0`;
- production Python and production CLI are unchanged;
- existing tests still pass;
- no WI-03 behavior is introduced;
- the diff contains only the explicitly authorized Demo implementation and any
  separately authorized developer-tool tests or documentation;
- `git diff --check` passes.

## 17. Human Review Gate

Current gate:

```text
Design Direction
= ACCEPTED

Canonical Plan Wording
= REVIEWED / IMPLEMENTATION-READY

Implementation
= AUTHORIZED
```

Human Review result:

```text
Plan Fidelity                         = PASS
Semantic Flow / Observed Trace Split = PASS
Provenance Model                     = PASS
Private _ExecutionAbort Boundary     = PASS
Production Design Protection         = PASS
Architecture Deviation               = NONE
Architecture Assumption Conflict     = NONE
Explicit Implementation Authorization= GRANTED

Current Next Implementation Step
= lifecycle_demo success scenario only
```

After implementation, return the uncommitted Demo and evidence for Human Review.
Do not commit or push without separate authorization.

## 18. Final boundary

The intended result is one small learning surface over the already-proven WI-02
implementation:

```text
Real WI-02 Runtime execution
+ accurate provenance
+ compact human visualization
+ result-derived four-path matrix
```

It does not reopen WI-02, start WI-03, create a business capability, or acquire
architecture authority.
