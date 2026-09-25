# Pass 2 errata recorded during Pass 4

Historical baseline: `66d70cd1d1de4e31cfacc902eddb225ba1b77c79`. Restored contents include original control characters, line endings, and broken links. Interpretations below are additive; they do not establish the truth of the affected mathematical statements.

## File-specific restoration record

All entries below were inspected in Pass 4 by comparing the Pass 2 completion blob with the pre-Pass-4 version. The later corrections occurred in Pass 3. That change history establishes when an edit occurred, not when a defect was first noticed.

| Historical file | Historical defect / later edit | Corrective interpretation |
| --- | --- | --- |
| `AUDIT_PASS_2.md` | Root copy contains parent-relative links, form-feed bytes before fraction commands, and a bell byte near the approximation command; Pass 3 repaired links and some characters | Use the archived Pass 2 plan and preserved Pass 2 ledger. Read the displayed fractions as mathematical fractions; do not infer a theorem from repairing typesetting |
| `reports/AUDIT_PASS_2.md` | Plan link and malformed fraction/approximation text were changed | Same interpretation as the root report; its historical bytes are independently preserved |
| `evidence/literature/PASS_2_PRIOR_ART.md` | Plan relocation link; tab/form-feed/bell damage in multiplication, universal quantifier, fraction, approximation, and Hessian text | Intended notation is `\times`, `\forall`, `\frac`, `\approx`, and `\text`; primary-source comparison remains a later-pass obligation |
| `evidence/public-timeline/PASS_2_TIMELINE.md` | Plan link was changed after archival relocation | Resolve the plan to `archive/SECOND_AUDIT.md` through current navigation; do not edit the historical link |
| `evidence/search-records/PASS2-SRCH-001-COMPARATORS.md` | Damaged multiplication, universal quantifier, and fraction commands | Read the intended notation only as the historical comparison assertion, not verified primary-source evidence |
| `evidence/search-records/PASS2-SRCH-002-MATHEMATICAL-METHOD.md` | Original CRLF bytes, malformed fractions, and a carriage return in the intended rho term; later normalization also introduced a split `ho_R` line | Restore exact original bytes. Intended complement term is `\rho_R`, subject to analytical checking. Neither malformed version is a new formula |
| `evidence/search-records/PASS2-SRCH-003-LI-LAGUERRE-SCHOENBERG.md` | Tab corruption in the intended RH text command | Interpret the intended label as RH; retain original bytes |
| `evidence/search-records/PASS2-SRCH-004-OBSTRUCTIONS-AND-VERIFICATION.md` | Tab corruption in the intended Hessian text command | Interpret the intended operator label as Hessian; proof scope remains unverified in Phase 0 |
| `reports/interim/PASS_2_PHASE_0_REPORT.md` | Plan link changed | Follow the archived plan through living navigation |
| `reports/interim/PASS_2_PHASE_1_REPORT.md` | Plan link and multiplication/fraction notation changed | Preserve original text; use additive interpretation and later primary-source review |
| `reports/interim/PASS_2_PHASE_2_REPORT.md` | Plan link, fraction, and Hessian notation changed | Preserve original text; family-wide obstruction assertions require individual review |
| `reports/interim/PASS_2_PHASE_3_REPORT.md` | Plan link, Schur fraction, and endpoint text subscript changed | Preserve original text; a lemma count is not evidence of end-to-end formal verification |
| `reports/interim/PASS_2_PHASE_4_REPORT.md` | Plan link changed | Follow the archived plan through living navigation |

The inherited Pass 1 plan and search record are handled by [Pass 1 errata](ERRATA_PASS_1.md), not assigned a new Pass 2 baseline. The Pass 2 plan is preserved at `archive/SECOND_AUDIT.md`. The Pass 2 ledger and living-document versions are preserved under `archive/baselines/pass-2/`. All 13 Pass 2-specific files listed above were restored to their completion blobs. Together with the two Pass 1 restorations, this accounts for 15 historical content restorations.

## Scope and evidence

Do not spend audit time reconciling document metadata clocks. Their historical values are preserved; any timestamp used as evidence requires the appropriate primary event record.

Affected propositions include the MATH, METH, OPER, LAGU, GRAM, OBST, VERF, and PRIO families discussed in these reports. Restoring text changes none of their substantive classifications.

Evidence: [preservation manifest](../evidence/phase0/PRESERVATION_MANIFEST.json) records full commit IDs, blob IDs, paths, hashes, and later history for each version; [execution record](../evidence/computation-logs/PASS4-PHASE0-PRESERVATION.run.json) retains the restoration output. Pass 3 versions of changed historical files remain separately available under `archive/baselines/pass-3/` and in Git history.
