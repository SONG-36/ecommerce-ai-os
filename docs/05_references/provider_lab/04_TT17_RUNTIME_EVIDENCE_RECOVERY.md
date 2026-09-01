# TT-17 Runtime Evidence Recovery

- Evidence record version: 1.0
- Record status: Recovered evidence / pending Human Review
- Recovery date: 2026-09-01
- Provider: Scrape Creators
- Endpoint identity: TT-17 Search by Keyword
- Historical provider path: `/v1/tiktok/search/keyword`
- Architecture authority: No

## 0. Purpose and authority boundary

This record canonicalizes surviving historical TT-17 runtime evidence for a
later WI-04 Entry Audit. It is not that audit, an Adapter implementation, an
Endpoint Selection architecture document, or a replacement for any Contract
or Architecture authority.

No standalone historical TT-17 admission / endpoint-selection closure
document was found. This record was created on 2026-09-01 and must not be read
as a backdated closure document or as historical authority.

The original raw files were local historical runtime artifacts in
`video-direction-workbench`; they were not originally committed into the
Ecommerce AI OS repository. The canonical fixtures are sanitized derivatives,
not the original raw files. Exact source and fixture hashes are recorded in
[`tt17/PROVENANCE.json`](tt17/PROVENANCE.json), with the transformation
documented in [`tt17/SANITIZATION_REPORT.md`](tt17/SANITIZATION_REPORT.md).

## A. Historical facts recovered now

The source hashes were reverified before repository modification. Request
semantics, HTTP status, and the Request 03 transport classification were
cross-checked against the surviving historical redacted request summaries;
their paths and hashes are retained in `PROVENANCE.json`. Response shape and
content fidelity come from the verified raw response artifacts.

### Request 01

- request semantics: `query=car vacuum`, `region=US`;
- HTTP status: 200;
- Provider response: `success=true`;
- returned occurrences: 30, in observed Provider order;
- `cursor=30`;
- `has_more=1`;
- `desc`: 0 absent, 0 null, 0 empty string;
- `create_time`: 0 absent, 0 null.

### Request 02

- request semantics: `query=car vacuum`, `region=US`, `cursor=30`;
- this was the continuation request from Request 01;
- HTTP status: 200;
- Provider response: `success=true`;
- returned occurrences: 30, in observed Provider order;
- `cursor=60`;
- `has_more=1`;
- `desc`: 0 absent, 0 null, 1 empty string;
- `create_time`: 0 absent, 0 null.

Across Request 01 and Request 02, three Provider item occurrences repeat by
`aweme_info.aweme_id`. The saved fixtures retain all three cross-page duplicate
occurrences; no deduplication or sorting was performed.

### Request 03

- attempted request semantics: `query=car vacuum`, `region=US`,
  `date_posted=last-3-months`;
- no HTTP status or JSON Provider response was observed;
- the surviving raw artifact records `EOF occurred in violation of protocol
  (_ssl.c:1129)`;
- the historical runtime summary classifies this as `URLError / SSLEOFError`;
- semantic interpretation: UNKNOWN.

Request 03 is recorded as bounded transport-error evidence only. It has not
been converted into a successful fixture or a Provider error-response fixture.
The transport failure does not prove parameter rejection, an invalid
parameter, or any Provider semantic behavior.

## B. Existing Architecture / Contract decisions

This recovery does not change the existing decisions:

```text
TT-17 Endpoint Admission Review
= PASS_WITH_LIMITATIONS

Minimum Endpoint Subset
= {TT-17 Search by Keyword}
```

Existing C3, C4a, C4b, C5, Provider Mapping, and Software Architecture
semantics remain unchanged. Provider-shaped fixtures are evidence inputs at
the Adapter boundary; they are not normalized C3 `SearchResult` values and do
not define Ecommerce AI OS domain semantics.

## C. New documentation action performed now

On 2026-09-01, this repository gained:

- two deterministic, sanitized, Provider-shaped fixtures derived from the
  historical Request 01 and Request 02 raw responses;
- a machine-readable provenance record connecting every request to its
  original source artifact and, where applicable, its canonical fixture;
- an exact sanitization report;
- a fixture-integrity test that checks hashes, response shape, counts,
  pagination values, duplicates, missingness, time presence, and secret-risk
  markers.

This is a present-day evidence recovery action. It does not create or imply a
historical admission or endpoint-selection authority that did not exist.

## D. Still-unverified Provider semantics

The recovered evidence does not prove:

- Provider hard cap;
- pagination termination or Provider exhaustion;
- global completeness;
- full enumeration;
- `date_posted` behavior;
- `sort_by` behavior;
- ranking semantics or ranking stability;
- exact `region=US` population effect.

The following distinctions remain mandatory:

```text
pagination continuation observed
!= pagination termination proven

has_more=1
!= global completeness knowledge

region=US request accepted
!= exact US population semantics

transport error
!= Provider rejection
```

## Review gate

The runtime material needed to conduct the WI-04 Entry Audit is now available
canonically, subject to Human Review of this recovery. WI-04 remains not
started and not authorized by this record.
