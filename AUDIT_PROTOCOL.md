# Audit protocol, version 3

## Status and scope

Pass 4 uses **five evidentiary axes plus one disposition field** under [FOURTH_AUDIT.md](archive/FOURTH_AUDIT.md). Phase 0 establishes accounting and provenance; it does not independently verify mathematics, novelty, software soundness, or priority.

The frozen target is `51feb3d176e4a53773c22dc157567cc0486f4c71`. The source checkout and its history remain read-only. Historical policy versions are preserved under `archive/baselines/`; this policy governs living Pass 4 records, not retroactive edits to earlier passes.

## Evidence-led decisions

1. Treat earlier audit classifications as hypotheses. Neither novelty nor prior existence is a predetermined verdict.
2. Identify the exact proposition and relevant axes before collecting or classifying evidence.
3. Distinguish source assertions, inspected derivations, independent derivations, machine replay, formal checking, external comparison, and public event records.
4. Give adverse and supporting evidence equal evidentiary treatment. Do not discard adverse findings from Git history.
5. Missing or inaccessible evidence stays unresolved. A null search does not establish novelty or prove non-occurrence.
6. Keep source defects as audit findings. Do not correct code, mathematics, certificates, documentation, or retained computations in the source checkout.

## Classification fields

| Field | Meaning |
| --- | --- |
| Validity / factual status | Whether the exact proposition is established within the stated scope |
| Result comparison | Relationship to external mathematical results |
| Method comparison | Relationship to existing techniques |
| Verification/software comparison | Relationship to proof architectures and implementation facts |
| Chronology / priority | Content-specific public chronological evidence |
| Evidence disposition | Completeness, unresolved evidence, or need for narrower wording |

The disposition is not a sixth evidentiary axis. Phase 0 retains all six inherited classification values in an explicitly labeled Pass 3 hypothesis view. `evidence/phase0/CANDIDATE_MAP.json` holds those immutable baseline values separately from `current_review`. A baseline `VERIFIED` or `COMPLETE` is not a Pass 4 promotion.

Current review states begin at `NOT_ADJUDICATED`, with disposition `INCONCLUSIVE — REQUIRES LATER PASS`. This records an audit-evidence gap, not a scientific reversal of the inherited classification. Any later substantive change must record old value, new value, affected axis, reason, and supporting evidence. The living inventory preserves exact canonical proposition text; narrower interpretations are separate findings.

## Verification provenance

Every current validity decision has a `Verification Basis` selected from:

- `MACHINE_REPLAY`
- `INDEPENDENT_DERIVATION`
- `FORMAL_PROOF_CHECK`
- `SOURCE_DERIVATION_REVIEW`
- `PRIMARY_LITERATURE_MATCH`
- `CODE_INSPECTION`
- `HISTORICAL_RECORD`
- `NOT_INDEPENDENTLY_VERIFIED`

A positive basis requires an evidence reference and a statement of what it checks. A theorem label, a source quotation, or a successful certificate replay does not establish every upstream mathematical implication. Mixed checked/unchecked components must be separated explicitly.

## Evidence strength

| Level | Audit evidence represented |
| --- | --- |
| E0 | Candidate or related source lead only |
| E1 | Relevant source assertion located, not independently checked |
| E2 | Source derivation or code inspected |
| E3 | Independently reproduced or rederived |
| E4 | Independently machine-verified or formally verified within declared scope |
| E5 | Independently reproduced and externally corroborated |

Record strength separately for validity, result, method, software, and priority. Levels do not rank scientific merit. An E1 source assertion does not justify `SOURCE_DERIVATION_REVIEW`; E4 finite acceptance does not certify an unreviewed infinite-dimensional reduction. Phase 0 leaves comparison and priority evidence at E0 until their evidence is examined. Historical evidence remains accessible as a lead rather than silently credited as a new check.

## Normalization and comparison

Before asserting equivalence or difference, align support width versus half-width, coordinates, Fourier conventions, constants, function spaces, admissibility constraints, operators, regimes, and effective bounds. Identify standard ingredients separately from their application or combination. Explain every shortlisted source's disposition using [EVIDENCE_STANDARDS.md](EVIDENCE_STANDARDS.md).

Public priority requires content-specific, symmetric public-disclosure evidence under [TIMELINE_RULES.md](TIMELINE_RULES.md). Do not infer public availability from author/committer time, repository creation alone, or absence of archive hits.

## Completeness and promotion

Required obligations are recorded per candidate before adjudication. An axis may be inapplicable only with an explicit reason, not because its evidence is inconvenient to obtain. Phase 0 conservatively records all five axes as pending applicability review; inherited `N/A` values are not automatically new exemptions.

A current `VERIFIED` requires proposition-appropriate evidence and a declared nonempty basis. `COMPLETE` requires all applicable obligations to be satisfied, not just replay acceptance or a matching ID count. Unchecked analytical steps, unavailable primary text, incomplete searches, or unresolved priority prevent completion where relevant.

Use `CLAIM REQUIRES NARROWER WORDING` for a supported restriction, or `INCONCLUSIVE — REQUIRES LATER PASS` for open evidence. A pass may finish while its candidates remain unresolved, provided every required procedure and gap is honestly accounted for.

## Mapping and integrity gates

The inventory ID, exact proposition, category, source reference, historical anchor, ledger row, mapping dossier, search-status record, and coverage row must correspond. Structured records bind every rationale to its subject ID and proposition digest. A machine match cannot determine mathematical meaning; the mapping dossier records semantic review and exceptions separately.

`python -B scripts/pass4_validate.py` checks Phase 0 accounting, preservation, source identity, links, and hash domains. `--completion` additionally rejects unresolved candidate obligations. `--self-test` exercises rejected mutations without modifying repository artifacts. Commands are run through `scripts/pass4_run.py` when retaining evidence.

Historical artifacts are excluded from current-document formatting/link repair. Exact restoration and declared byte-domain checks take precedence over prettifying their original defects. The preservation manifest classifies every baseline path as historical, a living-document snapshot, or repository control.

## Version 3 amendments

This revision removes the old policy's predetermined non-novelty stance, corrects axis terminology, separates inherited conclusions from current evidence, adds provenance and per-axis strength, and makes public-event semantics explicit. It does not reclassify scientific claims during the naming migration. See [Pass 3 errata](archive/ERRATA_PASS_3.md) for prior mapping and evidence-policy issues.
