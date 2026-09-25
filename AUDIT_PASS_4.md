# Audit Pass 4: evidence depth, provenance, and independent verification

## 1. Status, purpose, and authority

**Document type: initial execution-plan document, not an audit report.** Phase 0, Phase 1, and Phase 2 technical gates have passed; see the [Phase 0 report](reports/interim/PASS_4_PHASE_0_REPORT.md), [Phase 1 report](reports/interim/PASS_4_PHASE_1_REPORT.md), and [Phase 2 report](reports/interim/PASS_4_PHASE_2_REPORT.md) for evidence and limitations. The exact original plan is preserved as [FOURTH_AUDIT.md](FOURTH_AUDIT.md), the execution-plan authority. This document does not report completed Pass 4 work or authorize a consolidated final audit.

Pass 4 will test whether the audit has sufficient evidence for the classifications in `AUDIT_LEDGER.md`. It will neither defend nor reject the research project in advance. Passes 1 through 3 provide records to inspect, not authorities whose conclusions must be retained. Classifications may strengthen, weaken, remain unchanged, or become unresolved.

The decision rule is to establish what the evidence supports, with uncertainty recorded at the affected proposition and axis. A source assertion, a successful computation, a mathematical proof, a literature comparison, and a public-disclosure record answer different questions.

### Document lifecycle

The requested deliverable for this drafting task is this plan at `AUDIT_PASS_4.md`. The specification also reserves that filename for an eventual report and requests `FOURTH_AUDIT.md` as the plan. Resolve that collision explicitly at the start of execution:

1. Preserve this plan as `FOURTH_AUDIT.md`, with its originating audit commit recorded. Thereafter that file is the execution-plan authority.
2. Keep `AUDIT_PASS_4.md` visibly identified as a plan until synthesis is supported by actual evidence. Do not publish an empty report merely to occupy the filename.
3. At Phase 6, publish the report master at `reports/AUDIT_PASS_4.md` and its root copy at `AUDIT_PASS_4.md`. Preserve the plan and its history; check report content correspondence and location-dependent links.
4. Update root navigation to distinguish planned, executing, and completed work. Do not label Pass 4 complete because either filename exists.

The supplied specification ends during section 32. This plan covers its complete requirements and the visible success criterion; it does not attribute invented continuation text to the specification.

### Governing inputs

Read these together before execution:

- [README.md](README.md), current navigation and boundaries.
- [AUDIT_PROTOCOL.md](AUDIT_PROTOCOL.md), classification and normalization rules.
- [EVIDENCE_STANDARDS.md](EVIDENCE_STANDARDS.md), primary-source and citation requirements.
- [TIMELINE_RULES.md](TIMELINE_RULES.md), distinct disclosure anchors.
- [SOURCE.md](SOURCE.md), frozen target and provenance leads.
- [CLAIMS_TO_AUDIT.md](CLAIMS_TO_AUDIT.md), candidate proposition inventory.
- [AUDIT_LEDGER.md](AUDIT_LEDGER.md), classifications under examination.
- [archive/THIRD_AUDIT.md](archive/THIRD_AUDIT.md) and [reports/AUDIT_PASS_3.md](reports/AUDIT_PASS_3.md), prior commitments and reported results.

Existing policy language must not predetermine a negative or positive outcome. Phase 0 will record explicit amendments to living governance where it conflicts with this evidence-led pass. Historical policy versions remain preserved. In particular, null literature searches do not establish novelty, and local Git time does not establish public availability.

## 2. Boundaries and preservation

The target is `https://github.com/PerceivingAI/riemann-conjecture`, pinned to `51feb3d176e4a53773c22dc157567cc0486f4c71` under `source/riemann-conjecture/`.

The source checkout, its Git history, certificates, derivations, retained computations, code, and documentation are read-only. No helpful fixes, generated files, dependency updates, build outputs, caches, or new Lean proofs may be written there. Run inspection against the pin; redirect execution outputs and caches into audit-owned locations. If a tool cannot operate without writing beside its inputs, use a hash-verified audit-owned execution copy and document the copy procedure and identity. Do not silently substitute another source revision.

Record source commit, tree identity, and clean/dirty state before and after execution. Preserve pre-existing changes without overwriting them; stop affected evidence collection if identity cannot be established. Source errors become audit findings with exact commit, path, line or section, proposition, and evidence. They are not source patches.

Pass 4 must not extend support beyond T = 0.54, solve the p = 3 continuation problem, or produce new research results. Independent derivations are checks of existing propositions, not research extensions. No conclusion may imply that certificate replay proves RH.

### Historical restoration procedure

The restoration anchors supplied for this pass are Pass 1 `20b3f9d` and Pass 2 `66d70cd`. Resolve each to its full commit ID and inspect its tree before using it. Establish and record the Pass 3 completion commit from repository history rather than inventing an anchor.

1. Inventory all pass-specific reports, plans, dossiers, search records, timelines, interim reports, and computation artifacts. Follow renames and distinguish historical artifacts from living cross-pass files such as the ledger and navigation.
2. Compare each Pass 1/2 artifact with its own completion version, not merely with the immediately preceding commit. Retain a manifest of baseline commit, historical path, current path, Git blob ID, raw SHA-256, and later changes.
3. Restore altered historical artifacts to the exact original bytes from their respective baseline, including malformed characters, broken links, and other historical mistakes. Avoid line-ending conversion during extraction. Do not use a bulk checkout that can overwrite unrelated work or living documents.
4. Where one historical path has multiple pass versions, preserve each version distinctly and record the path mapping. Do not replace a Pass 1 artifact with Pass 2 contents solely because the path was reused.
5. Create `archive/ERRATA_PASS_1.md`, `archive/ERRATA_PASS_2.md`, and `archive/ERRATA_PASS_3.md`. Each entry records historical file and version, defect, corrective interpretation, discovery pass, supporting evidence, affected IDs, and restoration or correction action. Do not claim a defect was discovered in an earlier pass without evidence.
6. Freeze Pass 3 artifacts at the established baseline. Corrections to Pass 3 literature, chronology, or conclusions belong in new Pass 4 evidence and errata, not rewritten Pass 3 files.

Historical byte comparisons are release gates. Current-document link and formatting checks must exclude intentionally preserved historical defects and point readers to errata instead. A missing baseline object is an explicit restoration blocker, not permission to reconstruct history from memory.

## 3. Initial issues to resolve, not inherited verdicts

Repository inspection during plan preparation identified these concrete checks:

| Location | Observed issue | Execution response |
| --- | --- | --- |
| `AUDIT_PROTOCOL.md`, `AUDIT_LEDGER.md`, README | Four-axis terminology describes five evidentiary dimensions and a disposition | Amend living terminology without silently changing verdicts |
| `CLAIMS_TO_AUDIT.md` metadata | Reports 50 evaluated claims despite the larger table inventory | Compute actual IDs; preserve the historical metadata through the preservation policy and correct the living inventory |
| `AUDIT_LEDGER.md`, `CLM-PRIO-001..003` | Rationales discuss prime-trace, shift-filter, and stationary-mode priority while propositions concern public record, negative results, and correction history | Reconcile each rationale against its own exact proposition; do not treat a matching ID set as semantic correctness |
| `AUDIT_LEDGER.md`, `CLM-PRIO-012` | Compressed-translation proposition has a zero-float verification rationale | Require proposition-specific evidence and mapping review |
| README | Links to root `THIRD_AUDIT.md`, while the inspected plan resides at `archive/THIRD_AUDIT.md` | Repair living navigation after historical classification |
| `AUDIT_LEDGER.md`, `CLM-MATH-001` | `COMPLETE` appears alongside unverified public push evidence | Reassess relevant-axis completeness; do not resolve the priority question by renaming fields |

The specification also reports historical modifications, broad verification labels, incomplete comparator history, aggregated searches, and LF-domain replay hashes. These are investigation inputs. Preserve the actual evidence establishing their extent rather than turning the specification into a finding.

## 4. Candidate accounting and evidence model

### Inventory ownership

Extract the canonical proposition, category, source reference, and anchor for every ID from `CLAIMS_TO_AUDIT.md`, then check the frozen source. Existing verdict columns are not evidence of validity. Do not silently rewrite a proposition to match its rationale. Record disputed wording, source corrections, and any narrower replacement interpretation explicitly.

| Family | IDs | Count | Lead review |
| --- | --- | ---: | --- |
| MATH | `CLM-MATH-001..008` | 8 | Theorem reduction and individual certificates |
| METH | `CLM-METH-001..005` | 5 | Decomposition, coercivity, tail-Gram, proof architecture |
| OPER | `CLM-OPER-001..002` | 2 | Thresholded translations and exact shift spectrum |
| CONT | `CLM-CONT-001..002` | 2 | Existing continuation evidence and finite-section rejection |
| OBST | `CLM-OBST-001..015` | 15 | Granular obstruction proof review |
| LAGU | `CLM-LAGU-001..005` | 5 | Exact identities and root criteria |
| AIRY | `CLM-AIRY-001..007` | 7 | Individual asymptotic and mode checks |
| GRAM | `CLM-GRAM-001..003` | 3 | Gram, CND, and prime-atom propositions |
| VERF | `CLM-VERF-001..007` | 7 | Software facts and verification trust boundaries |
| PRIO | `CLM-PRIO-001..012` | 12 | Content-specific public chronology and research-history facts |
| Total | All candidate families | 66 | No omitted family |

### Five evidentiary axes plus one disposition field

Every ledger record must contain these separate fields:

| Field | Question |
| --- | --- |
| Validity / factual status | What part of the exact proposition has been checked? |
| Result comparison | How does it relate to external mathematical results? |
| Method comparison | Which techniques are known, shared, or differentiated? |
| Verification/software comparison | How does the implementation or proof architecture compare? |
| Chronology / priority | What public evidence supports the relevant historical claim? |
| Evidence disposition | Is the required evidence complete, unresolved, or supporting only narrower wording? |

Retain substantive classifications during the naming migration. Evidence-based changes require an old/new record, affected axis, reason, and new evidence links. `N/A` requires a reason; it is not a way to close an inconvenient axis.

Add `Verification Basis` using one or more of:

- `MACHINE_REPLAY`
- `INDEPENDENT_DERIVATION`
- `FORMAL_PROOF_CHECK`
- `SOURCE_DERIVATION_REVIEW`
- `PRIMARY_LITERATURE_MATCH`
- `CODE_INSPECTION`
- `HISTORICAL_RECORD`
- `NOT_INDEPENDENTLY_VERIFIED`

Attach each basis to the precise assertion it supports and to its evidence. A source theorem label or successful replay cannot independently verify upstream analysis. Source review alone must not be described as independent derivation. For partially checked compound claims, record checked and unchecked components separately; do not combine `NOT_INDEPENDENTLY_VERIFIED` with a positive basis without explaining the scope.

### Evidence strength and completeness

Record strength per relevant dimension, not as one overall score:

| Level | Meaning |
| --- | --- |
| E0 | Candidate only |
| E1 | Source assertion located |
| E2 | Source derivation or code inspected |
| E3 | Independently reproduced or rederived |
| E4 | Independently machine-verified or formally verified within stated scope |
| E5 | Independently reproduced and externally corroborated |

These levels describe audit evidence, not scientific importance. E4 replay of a finite certificate does not elevate the whole analytic theorem to E4. For literature and priority, explain how a level applies to the actual comparison or record; do not imply that searching a database formally verifies novelty. E5 requires genuinely external corroboration, not another document repeating the same source.

Before adjudication, specify the required evidence for each relevant axis. A theorem may require independent analysis, replay, normalization, comparison, and public chronology. A software implementation fact may not need priority research unless novelty or precedence is claimed. `COMPLETE` requires every applicable obligation to be satisfied. Otherwise use `CLAIM REQUIRES NARROWER WORDING` or `INCONCLUSIVE — REQUIRES LATER PASS`, with the unresolved obligation stated. An unresolved candidate can be fully accounted for in a completed audit pass; it cannot be labeled evidentially complete.

### Coverage matrix and mapping validator

Create `EVIDENCE_COVERAGE.md` with one row per candidate and these columns: ID, proposition verified, verification basis, literature searched, comparator searched, priority evidence, dedicated dossier, evidence strength by dimension, remaining work. Each positive entry links to evidence; each inapplicable entry explains why. The ledger records conclusions; coverage records their support.

Implement an audit-owned validator and retain its command, source, and output. It must join:

`inventory ID -> exact proposition -> category -> source anchor -> ledger row -> dossier section -> search record -> coverage row`.

Use a Markdown-aware parser or explicit structured records so mathematical absolute-value bars and escaped pipes do not shift columns. Require 66 unique inventory, ledger, and coverage rows, exact family membership, valid file and section references, and declared evidence obligations. Group dossiers need an individually addressable section for every supported ID.

A script cannot decide that free-form mathematical prose means the correct proposition. Require every rationale/evidence record to declare its subject ID and canonical proposition reference or digest. Fail on inconsistent mappings, missing or duplicate rows, absent required evidence references, broken paths/anchors, or unmatched proposition identifiers. Supplement this with a recorded human semantic check of each rationale, especially PRIO rows. Explicit unresolved records may satisfy accounting, but must fail any attempted `VERIFIED` or `COMPLETE` promotion that lacks required support.

Exercise the validator on deliberate missing-ID, duplicate-ID, wrong-proposition, missing-link, and nonexistent-file cases, then on the actual artifacts. Preserve failures and final output; do not claim semantic validation from row counts alone.

## 5. Execution sequence and gates

Phase 0 establishes preservation and schemas. Phases 1 and 2 establish comparisons; Phase 3 checks mathematical validity; Phase 4 checks the computational and formal chain; Phase 5 resolves public-evidence questions; Phase 6 reconciles conclusions. Feed newly discovered comparators or analytical issues back to the responsible phase. Collection is iterative, but no final classification bypasses an applicable gate.

Every phase records completed work, unavailable evidence, affected candidates, and its gate result. A blocked source is not a zero-hit search. No phase gate may be reported as passed by silently dropping the affected scope.

### Phase 0. Historical integrity and audit tooling

**Actions**

- Perform the restoration and freeze procedure in section 2, preserving manifests and errata.
- Establish the plan/report lifecycle, source identity record, and current artifact inventory.
- Amend living taxonomy and governance; preserve baseline classifications separately from substantive reassessment.
- Reconcile all 66 proposition mappings, create coverage rows, and implement the validator.
- Define raw and normalized hash domains and the execution-record format before collecting new evidence.
- Fix living navigation without repairing frozen historical documents in place.

**Outputs:** preserved plan, three errata files, restoration manifest, living schema updates, coverage matrix, validator and recorded output, hash policy.

**Exit gate:** every historical artifact is accounted for against its baseline; restorations match exact bytes; the source remains untouched; 66 candidate mappings and tool failure cases are checked. Evidence gaps are explicit, not fabricated to make validation pass.

### Phase 1. Comparator histories and primary-source reconstruction

#### Kuber repository

Investigate `https://github.com/Kuberwastaken/riemann` using actual Git history. Record retrieved refs, full tip SHAs, collection time, history completeness, and any shallow or unavailable range. Inspect all relevant development through the collection cutoff, with particular attention to August 2026. A current `main` snapshot cannot support a historical absence claim.

Trace additions, deletions, renames, and later revisions in at least `UPDATES.md`, `CONTINUATION.md`, `FINDINGS.md`, `logs/LOG.md`, `experiments/weil_positivity/`, and `formal/`. Locate the first relevant statement, first complete argument or artifact, and subsequent changes. Inspect developments described as full-space, certified corollary, pilot theorem, spectral cap, tail bound, continuation, operator reduction, Lean reduction, or prior-art collision audit.

Produce `evidence/literature/PASS4-KUBER-COMMIT-HISTORY.md` with a chronological table containing full commit SHA, exact author and committer timestamps with offsets, file/section, first appearance or later modification, mathematical status at that commit, affected candidate IDs, and evidence links. Separate Git event time from independently established public availability. Preserve commands and relevant diffs or object references.

Normalize function spaces, support, constants, operators, tail control, and proof scope before comparing. Later comparator developments must be examined, but cannot be retroactively attributed to an earlier commit. Comparator self-audits citing Bombieri, Suzuki, Connes–Consani, Lagarias, or others are leads only; inspect the primary sources independently.

#### Marcus Chuk and other comparators

Rebuild the comparison in `evidence/literature/PASS4-CHUK-PRIMARY-SOURCE.md` from the official arXiv record, relevant individual versions, actual papers, and associated public code/data. Treat the earlier dossier's arXiv identifier as a lookup lead whose identity must be checked. Record each version's submission and public-posting metadata separately, without inheriting earlier audit dates.

For each relevant theorem record citation, version, theorem number, support convention, normalization, function space, proof architecture, numerical certification, tail/error estimates, interval-arithmetic role, formal/exact arithmetic role, affected IDs, and precise comparison result. Trace associated code by commit history where it exists. Record unavailable versions or repositories explicitly.

Apply the same version-specific standard to other material comparators discovered. Do not revise Pass 3 dossiers.

**Exit gate:** every retained comparator conclusion points to exact commits/files or paper versions and theorem locations, with normalized scope. Unavailable history or text limits the conclusion explicitly.

### Phase 2. Claim-specific search re-execution

Prioritize strong novelty labels and consequential subsumption claims. Cover every candidate's applicable result, method, software, and priority comparisons. Reuse a search only when its mathematical scope genuinely covers each listed candidate.

For high-value candidates run multiple semantic families: exact terminology; mathematical equivalents; broader operator/function theory; combinations of known ingredients; named techniques; backward/forward citation chains; and repository/code searches. For the tail-Gram criterion, include Schur complement, Feshbach reduction, block operator positivity, finite-section plus tail estimates, Legendre coercivity, Gram corrections, complement bounds, rigorous spectral enclosure, and the Weil quadratic form. Negative exact-phrase searches cannot establish novelty.

Log every database separately in `evidence/search-records/PASS4-*.md`. Cover relevant mathematical indices, preprint services, academic aggregators, and code/archive sources, including MathSciNet, zbMATH, arXiv, Google Scholar, Semantic Scholar, Crossref, GitHub, and Zenodo as applicable. Use each engine's actual accepted syntax.

Each record contains database/service, actual execution time, submitted query, filters, date range, pagination or retrieval limits, returned count where exposed, whether approximate, inspected subset, shortlist, rejected items with reasons, and affected IDs. Record unavailable counts as unavailable; access denial is not zero results. Preserve query URLs, API requests, exports, or response artifacts sufficient to repeat the search. Do not aggregate counts across engines or present dynamic search results as immutable.

Every shortlisted item receives an explained disposition: `EQUIVALENT`, `PARTIAL OVERLAP`, `KNOWN INGREDIENT`, `STRONGER RESULT / DIFFERENT METHOD`, `WEAKER RESULT / SAME METHOD`, `DIFFERENT NORMALIZATION`, `DIFFERENT FUNCTION SPACE`, `DIFFERENT REGIME`, `IRRELEVANT AFTER INSPECTION`, or `UNRESOLVED`. A normalization difference must be analyzed, not used automatically to dismiss equivalence.

Important external works require individual dossiers with complete citation/BibTeX, DOI, arXiv version, MR and zbMATH identifiers where available, stable URL, page/section/theorem/proposition/equation, normalization, candidate IDs, and raw SHA-256 of the exact examined file if legally obtained. Missing identifiers or inaccessible text must be stated. Do not commit proprietary PDFs; redistribution requires appropriate permission. `evidence/literature/PASS_4_PRIOR_ART.md` is an index and synthesis of claim-level dossiers, not their replacement.

**Exit gate:** each retained strong novelty classification has a reproducible, multi-family, per-database trail and inspected primary-source comparisons. Inadequately searched claims remain unresolved rather than retaining unsupported strength.

### Phase 3. Independent mathematical validity

Create individually addressable validity records containing exact candidate proposition; source derivation location at the pin; independent derivation or check; hypotheses; normalizations; result; limitations; verification basis; strength; and evidence links. Distinguish a source review, independent proof, algebraic check, numerical experiment, and heuristic plausibility. A numerical check cannot prove an identity or uniform asymptotic assertion.

| Review group | Required work and coverage |
| --- | --- |
| A: certified theorems | Review `CLM-MATH-001..008` individually. Link each theorem to its certificate, verifier acceptance, and analytical reduction. Include relevant VERF evidence from Phase 4 without treating replay as the whole proof. |
| B: exact analysis | Independently derive `CLM-LAGU-001..005`, `CLM-GRAM-001..003`, and `CLM-OPER-001..002`. Check convergence, exchanges of sums/integrals/limits, parameter exclusions, both directions of equivalences, shift filtering, spectral endpoints, and normalization. |
| C: asymptotics | Review `CLM-AIRY-001..007` separately. Check saddle equations, regime, uniformity, branches, errors, scaling, transition region, Cayley-mode identification, and prime-scale mapping. Shared source text is not seven independent validations. |
| D: obstructions | Audit all 15 OBST propositions using the granular scheme below. Separate theorem, conditional barrier, and heuristic limitation. |
| E: methodology and continuation | Check `CLM-METH-001..005` and `CLM-CONT-001..002` against exact decomposition, coercivity, complement bounds, Schur reduction, and retained continuation evidence. Do not generalize finite successful instances into arbitrary-support guarantees. |

For obstructions use these dossier groups only where the proof machinery is genuinely shared:

- OBST-A, `CLM-OBST-001..003`: endpoint absorption, coercivity, and residual completeness.
- OBST-B, `CLM-OBST-004..005`: PNT/discrepancy estimates and moving-scale insufficiency.
- OBST-C, `CLM-OBST-006..010`: block norms, endpoint stationary behavior, frequency caps, and mean-value barriers.
- OBST-D, `CLM-OBST-011..015`: bilinear Hessian, Type-II separability, and square-root thresholds.

Every obstruction needs its own proposition, hypotheses, proof location, independent check, relevant standard theorem, literature search, limitation, and verification basis. Check the advertised scope, omitted regimes, and possible counterexamples. A failure of one proposed method is not a universal impossibility theorem. If a proof cannot be independently checked, say `NOT_INDEPENDENTLY_VERIFIED` and retain an unresolved disposition.

**Outputs:** `evidence/validity/PASS4-MATH-*.md`, `PASS4-LAGU-*.md`, `PASS4-AIRY-*.md`, `PASS4-OBST-*.md`, `PASS4-GRAM-*.md`, plus METH, OPER, and CONT dossiers or explicit candidate sections in genuinely shared dossiers.

**Exit gate:** every candidate called `VERIFIED` has proposition-matched support and a declared basis. All seven AIRY and all fifteen OBST claims have individual outcomes; no family-wide blanket verification.

### Phase 4. Verification-chain and computational audit

Separate four obligations: certificate acceptance, generator correctness, analytical reduction correctness, and formal verification coverage. Audit `CLM-VERF-001..007` individually and link dependent MATH/METH/CONT candidates.

Create `evidence/validity/PASS4-VERF-TRUST-CHAIN.md` with the dependency chain:

```text
analytic theorem
  -> finite reduction
  -> certificate generator
  -> certificate schema
  -> Rust verifier
  -> exact matrix/rational acceptance
```

This describes proof obligations, not an assertion that downstream acceptance proves every upstream arrow. For each arrow record the exact implication, inputs, hypotheses, source location, candidate IDs, supporting evidence, and status: independently checked, formally proved, tested, trusted, or unresolved. Represent multiple statuses with explicit scope.

Inspect how Python/Arb enclosures are formed and rounded, what the schema admits, what `rh_cert` actually checks, and which assumptions enter as trusted certificate data. Trace the acceptance path for exact arithmetic rather than relying on a token search for floating-point types. Check malformed-input rejection, mathematical rejection, and promotion boundaries without modifying retained certificates. Any adversarial input is an audit-owned copy with its own identity.

For Lean, create a module-to-proposition correspondence table: definitions, theorem statements, assumptions/axioms, proof-check command/result, Rust/Python objects represented, certificate fields mapped to hypotheses, finite-matrix soundness connection, and analytical reductions outside formal coverage. A compiled lemma count is not pipeline verification. Record missing links instead of adding proofs to the source.

Replay the retained theorem certificates individually and run the relevant existing Rust/Python/Lean checks needed to substantiate current claims. Discover commands and toolchain requirements from the pinned project rather than copying unverified commands from earlier reports. Preserve failures, environmental blockers, and successful runs. Reuse old logs as historical evidence only after checking identity and scope; they are not new independent executions.

#### Run record and hashing contract

Every run retains exact command and arguments; working directory; source commit and tree; source clean/dirty state; execution-copy identity if used; OS/architecture; tool and dependency versions; harness-generated start/end timestamps with timezone; stdout; stderr; and exit code. Each certificate gets its own original path and raw SHA-256, linked to its candidate and verifier result.

Preserve raw output bytes. Use `raw_file_sha256` for the exact file bytes and, where needed, `normalized_sha256` for the stated CRLF-to-LF transformation. A normalization policy must specify that no other bytes, encoding, whitespace, or final newline are changed. A Git object ID is separate from a SHA-256 content digest.

Investigate the supplied Pass 3 LF-hash observation with both domains; explain discrepancies additively without rewriting old logs or manifests. New manifests declare `hash_domain` and `line_ending_normalization` explicitly. Independently recompute hashes from stored artifacts and retain the checking command/output. No bare digest without its byte-domain definition.

**Outputs:** VERF dossiers, trust-chain graph and edge table, Lean correspondence record, individual certificate inventory, `evidence/computation-logs/PASS4-*` raw outputs and manifest.

**Exit gate:** exact acceptance is distinguished from generator and analytic correctness; every replay and formal claim is scoped to observed evidence; logs and certificate hashes are independently checked; source immutability holds.

### Phase 5. Public chronology and priority

Investigate `CLM-PRIO-001..012` according to their own propositions and every other candidate whose priority axis matters. Do not substitute chronology of a nearby theorem for research-integrity claims. Bound claims about unrewritten public history to the observable records; inability to detect rewriting is not proof that it never happened.

Use Git/GitHub and `gh`, GH Archive, Software Heritage, Wayback, forks, mirrors, externally indexed commit URLs, archive snapshots, and relevant release/tag records. Record each source separately with submitted query, stable identifier, event represented, exact timestamp returned, response artifact, and result. Preserve original offset/precision; UTC conversion is an additional field. Separate event time from retrieval time and Git author/committer time from public availability.

Search GH Archive event data, not merely web pages mentioning it. Identify candidate UTC hours/days, record the search interval and why it was selected, and retrieve or query the actual datasets for `PushEvent`, `CreateEvent`, and other relevant repository events. Retain the executable query/script, dataset identity, matching or nonmatching output, and hashes. Report coverage limits and inaccessible partitions. Do not write “GH Archive searched” if no dataset query succeeded.

Public snapshots may establish availability no later than capture time without identifying the first push. Match content to the exact proposition and commit. Compare symmetric disclosure events with official arXiv posting/version records, not a local commit date against journal publication. Do not infer a temporal ordering merely from an equation in an old protocol.

A null result means that source did not provide evidence in the examined range. It never proves that an event did not occur. Do not reconcile arbitrary Markdown timestamps; only examine a timestamp when it serves as evidence, using its authoritative source.

**Output:** `evidence/public-timeline/PASS_4_TIMELINE.md`, source-by-source candidate tables, raw/archive records, and retained queries.

**Exit gate:** every priority-relevant proposition has a source-specific trail with exact event semantics, supported bounds, and unresolved gaps. No public-availability verdict rests solely on local Git time or a null search.

### Phase 6. Evidence reconciliation and publication

For each of the 66 candidates, reconcile validity, comparison, verification architecture, and chronology without allowing one axis to decide the others. Publish an old/new classification table with evidence references, unchanged conclusions included. Any narrowed wording remains traceable to the original proposition.

Update the living ledger, coverage matrix, governance/navigation, and claim mappings. Publish the Pass 4 report master and root copy only after the evidence can support an honest account of completed work and unresolved items. Reports must distinguish completed audit procedures from unverified research claims and unavailable evidence.

Do not create a consolidated final audit without both genuine evidentiary convergence and a later explicit instruction. Do not overwrite Pass 1/2/3 reports or source artifacts during synthesis.

**Exit gate:** the release checklist in section 7 passes, or the report is explicitly interim with failed gates and blockers. A filename or a planned deliverable never counts as completion.

## 6. Artifact and commit plan

All paths below are execution outputs, not assertions that those files already exist.

| Artifact | Role / producing phase |
| --- | --- |
| `FOURTH_AUDIT.md` | Preserved execution plan, Phase 0 |
| `AUDIT_PASS_4.md`, `reports/AUDIT_PASS_4.md` | Root report and report master at Phase 6, following the lifecycle above |
| `EVIDENCE_COVERAGE.md` | One evidence-coverage row per candidate, maintained from Phase 0 |
| `archive/ERRATA_PASS_1.md`, `archive/ERRATA_PASS_2.md`, `archive/ERRATA_PASS_3.md` | Additive corrections and historical interpretation |
| `evidence/literature/PASS_4_PRIOR_ART.md` | Claim-indexed comparison synthesis, Phases 1/2 |
| `evidence/literature/PASS4-KUBER-COMMIT-HISTORY.md` | Actual chronological commit table, Phase 1 |
| `evidence/literature/PASS4-CHUK-PRIMARY-SOURCE.md` | Official version-specific comparison, Phase 1 |
| `evidence/literature/PASS4-*.md` | Additional primary-source dossiers |
| `evidence/search-records/PASS4-*.md` | Per-database queries and item dispositions, Phases 2/5 |
| `evidence/validity/PASS4-MATH-*.md`, `PASS4-LAGU-*.md`, `PASS4-AIRY-*.md`, `PASS4-OBST-*.md`, `PASS4-GRAM-*.md`, `PASS4-VERF-*.md` | Individual or explicitly grouped validity trails, Phases 3/4 |
| `evidence/validity/PASS4-METH-*.md`, `PASS4-OPER-*.md`, `PASS4-CONT-*.md` | Remaining mathematical families when not covered by identified shared sections |
| `evidence/public-timeline/PASS_4_TIMELINE.md` | Source-driven public chronology, Phase 5 |
| `evidence/computation-logs/PASS4-*` | Run records, raw streams, hash manifests, validation output |
| Audit-owned scripts and preservation manifest | Mapping validator, replay harness, chronology queries, historical byte checks; select paths after inspecting existing tooling |

Use separate commits for meaningful stages: historical restoration/errata; coverage and validation tooling; comparator histories; claim-specific searches; analytical review; verification trust chain; public chronology; report publication. Keep evidence and the classifications it changes traceable together. Do not amend, squash, or discard adverse findings. Commit timestamps are audit-history records, not substitutes for the external event times being investigated.

## 7. Completion checklist

Pass 4 can be marked complete only when all of the following are satisfied:

- [ ] All 66 IDs occur exactly once in the inventory, ledger, and coverage matrix, with correct family counts and source anchors.
- [ ] Every rationale has passed semantic proposition review, not merely an ID-presence check.
- [ ] Every `VERIFIED` label has a proposition-appropriate verification basis and linked evidence. Partial verification remains explicitly partial.
- [ ] AIRY and OBST outcomes are individual; METH, OPER, CONT, and research-history propositions are not omitted.
- [ ] Strong novelty conclusions have per-database, multi-family query records, counts where available, shortlists, inspected primary sources, and explained dispositions.
- [ ] Important external sources have version-specific citations and exact mathematical locations wherever obtainable; unavailable details limit the conclusions.
- [ ] Comparator repository conclusions cite exact full SHAs and files, including relevant later developments and history coverage limits.
- [ ] The analytical, generator, schema, verifier, and Lean trust boundaries are explicit and supported at the claimed level.
- [ ] Raw computational logs and individual certificate identities are retained; hash domains are defined and hashes independently recomputed.
- [ ] Pass 1/2 historical contents match their own completion baselines, Pass 3 is frozen, and all later corrections are additive.
- [ ] The source snapshot and source Git history remain unchanged, including generated outputs and caches.
- [ ] Priority conclusions identify source, event, exact timestamp or supported bound, and content; absence of evidence has not become evidence of absence.
- [ ] Every applicable open axis prevents candidate-level `COMPLETE`; access and tool failures remain visible.
- [ ] Ledger changes cite new evidence; coverage agrees with dossiers, searches, chronology, and reports.
- [ ] Validator output, historical integrity checks, report correspondence, and living navigation checks are preserved.
- [ ] The report states completed procedures, unresolved candidates, and any failed gates without claiming a consolidated final audit.

The practical acceptance test is traceability: a separate auditor can select any candidate, recover its exact proposition and frozen source location, distinguish what was independently checked from what was trusted, inspect normalized external comparisons, reproduce the recorded computations and searches as far as the services permit, identify the public chronology evidence, and see why each axis is classified as it is. Where that chain breaks, the break must remain visible in the coverage matrix and disposition.
