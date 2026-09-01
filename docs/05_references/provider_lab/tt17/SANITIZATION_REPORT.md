# TT-17 Canonical Fixture Sanitization Report

- Sanitization version: 1.0
- Sanitized on: 2026-09-01
- Scope: Request 01 and Request 02 successful raw responses only
- Request 03 fixture: Not created

## Method

The fixture bytes were copied from the verified historical raw JSON and then
changed only where a URL query component contained signed, expiring, or opaque
media-delivery security material. The JSON was not parsed and reserialized:
field order, array order, whitespace, escaped content, and every untouched byte
remain as observed.

The replacement is deterministic by query parameter name. It applies both to
ordinary URL query strings and to the same URLs when nested in stringified JSON
or percent-encoded share metadata.

| Query parameter | Deterministic replacement | Reason |
|---|---|---|
| `x-signature` | `REDACTED_X_SIGNATURE` | Signed CDN query value |
| `x-expires` | `REDACTED_X_EXPIRES` | Expiring CDN query value |
| `refresh_token` | `REDACTED_REFRESH_TOKEN` | Tokenized CDN query value |
| `signaturev3` | `REDACTED_SIGNATUREV3` | Signed media-playback query value |
| `pt` | `REDACTED_PT` | Opaque media-playback token value |
| `rc` | `REDACTED_RC` | Opaque media-delivery signature value |

Only the value after the named query parameter was replaced. URL field
presence, host, path, query parameter name, parameter order, encoding context,
and surrounding URL structure were preserved.

## Exact modification counts

### `region_us_page_01.json`

| Query parameter | Replacements |
|---|---:|
| `x-signature` | 1,935 |
| `x-expires` | 1,935 |
| `refresh_token` | 1,921 |
| `signaturev3` | 303 |
| `pt` | 268 |
| `rc` | 626 |
| **Total** | **6,988** |

### `region_us_page_02.json`

| Query parameter | Replacements |
|---|---:|
| `x-signature` | 1,812 |
| `x-expires` | 1,812 |
| `refresh_token` | 1,812 |
| `signaturev3` | 288 |
| `pt` | 254 |
| `rc` | 590 |
| **Total** | **6,568** |

No API key, Authorization header, Cookie value, bearer token, or authenticated
request material was present in either raw response. No Provider field was
removed merely because it appeared unused.

## Fidelity preserved

Sanitization did not change:

- result or field order;
- duplicate occurrences, including cross-page duplicates;
- Provider item IDs, creator IDs, media IDs, or cursor values;
- public metrics;
- `create_time` or any other observed time field;
- `cursor`, `has_more`, or response counts;
- field presence;
- null, absent, and empty-string distinctions;
- the observed top-level or nested Provider response shape.

The fixtures remain real Provider-shaped saved evidence. They are not deduped,
sorted, normalized, completed, or reshaped into a C3 `SearchResult`.

## Request 03

The 51-byte Request 03 artifact contains only the transport failure text
`EOF occurred in violation of protocol (_ssl.c:1129)`. It contains no JSON
Provider response and needed no credential sanitization. No failure fixture was
created because the current tests have no need for one; the bounded historical
fact is retained in `PROVENANCE.json` and the recovery record.
