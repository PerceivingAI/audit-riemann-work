# Audit Protocol — Version 2.0.0

This document defines the operational rules, decoupled multi-axis classification taxonomy, and analytical standards governing the independent audit of [`https://github.com/PerceivingAI/riemann-conjecture`](https://github.com/PerceivingAI/riemann-conjecture).

> **Protocol Governance Metadata**  
> * **Protocol Version**: `2.0.0` (Updated for Multi-Pass Multi-Axis Governance)  
> * **Effective Date**: `2026-09-24T23:10:00Z`  
> * **Audited Closed-State Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`

---

## 1. Epistemological Stance

1. **Null Hypothesis**: The default stance for any candidate claim is **non-novelty** and **prior existence**.
2. **Burden of Proof**: The burden rests on proving novelty through exhaustive literature and code search, mathematical comparison, and structural differentiation.
3. **Hypothesis vs. Fact**: Unaudited propositions listed in `CLAIMS_TO_AUDIT.md` are hypotheses under test, not established facts.
4. **Adversarial Standard**: Negative findings, overlapping prior art, and contradictory evidence must be fully documented and given equal prominence.
5. **Non-Closure Standard**: Where evidence is incomplete or unverified (e.g. unverified public push timestamps), claims must be designated `INCONCLUSIVE` rather than forced into premature certainty.

---

## 2. Versioned 4-Axis Multi-Dimensional Taxonomy (v2.0.0)

Every claim in the authoritative ledger (`AUDIT_LEDGER.md`) MUST be independently evaluated across five orthogonal axes plus a final disposition:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Versioned 4-Axis Taxonomy                       │
├─────────────────────────────────┬──────────────────────────────────────┤
│ Axis 1: Mathematical Validity   │ • VERIFIED                           │
│                                 │ • FALSIFIED                          │
│                                 │ • UNTESTED / THEORETICAL             │
├─────────────────────────────────┼──────────────────────────────────────┤
│ Axis 2: Mathematical Result     │ • NOVEL SUPPORT BOUND                │
│         Novelty                 │ • POSSIBLY NOVEL                     │
│                                 │ • RESULT SUBSUMED BY PRIOR ART       │
│                                 │ • PRIOR ART FOUND                    │
│                                 │ • N/A (Method / Software / Barrier)  │
├─────────────────────────────────┼──────────────────────────────────────┤
│ Axis 3: Method Novelty          │ • NOVEL SYNTHESIS SUPPORTED          │
│                                 │ • KNOWN INGREDIENT / NOVEL APPL.     │
│                                 │ • KNOWN METHOD                       │
│                                 │ • N/A (Pure Math Result / Verifier)  │
├─────────────────────────────────┼──────────────────────────────────────┤
│ Axis 4: Software / Verification │ • NOVEL VERIFICATION ARCHITECTURE    │
│         Novelty                 │ • VERIFIED IMPLEMENTATION FACT       │
│                                 │ • STANDARD IMPLEMENTATION            │
│                                 │ • N/A (Analytical Claim)             │
├─────────────────────────────────┼──────────────────────────────────────┤
│ Axis 5: Chronological Priority  │ • PRIORITY SUPPORTED (Public Push)   │
│                                 │ • PRIORITY PLAUSIBLE (Commit Only)   │
│                                 │ • PRIOR ART FOUND (External Earlier) │
│                                 │ • INCONCLUSIVE                       │
├─────────────────────────────────┼──────────────────────────────────────┤
│ Axis 6: Final Disposition       │ • COMPLETE                           │
│                                 │ • CLAIM REQUIRES NARROWER WORDING    │
│                                 │ • INCONCLUSIVE — REQUIRES PASS 4     │
└─────────────────────────────────┴──────────────────────────────────────┘
```

---

## 3. Mathematical Normalization Rules

Before comparing any candidate claim to prior literature:

1. **Variable Normalization**: Align notation for intervals, support widths (e.g., support $L$ vs. half-width $T$), scaled coordinates ($[-1, 1]$ vs. $[0, 1]$), normalization constants, and Fourier transform conventions.
2. **Regime Alignment**: Distinguish between asymptotic results ($N \to \infty$, $t \to \infty$) and effective/explicit finite bounds.
3. **Operator Equivalence**: Map operators (transfer operators, Schur complements, discrete path Laplacians) to standard mathematical terminology before asserting methodological differences.

---

## 4. Multi-Anchor Chronology & Priority Standards

Priority evaluations must explicitly evaluate four independent timestamp anchors:
$$T_{\text{idea}} \le T_{\text{commit}} \le T_{\text{public\_push}} \quad \text{vs.} \quad T_{\text{ext\_post}} \le T_{\text{publication}}$$

1. **$T_{\text{commit}}$**: Author/committer timestamp inside the Git commit object.
2. **$T_{\text{public\_push}}$**: Verifiable public push timestamp evidenced by third-party witnesses (GH Archive, Software Heritage, Wayback Machine, public mirrors, forks).
3. **$T_{\text{ext\_post}}$**: Public preprint or paper submission date (e.g. arXiv submission).
4. **Standard**:
   - `PRIORITY SUPPORTED`: Requires verified $T_{\text{public\_push}} < T_{\text{ext\_post}}$.
   - `PRIORITY PLAUSIBLE`: Assigned when $T_{\text{commit}} < T_{\text{ext\_post}}$ but independent public push records are unverified.
   - `PRIOR ART FOUND`: Assigned when $T_{\text{ext\_post}} \le T_{\text{commit}}$.

---

## 5. Literature & Repository Search Standards

All literature searches must satisfy minimum evidentiary rigor per `EVIDENCE_STANDARDS.md`:

1. **Databases Searched**:
   * Mathematical indices: MathSciNet / zbMATH.
   * Preprint repositories: arXiv (math.NT, math.CA, math.FA, math.SP).
   * Academic aggregators: Google Scholar, Semantic Scholar, Crossref.
   * Open source codebases & archives: GitHub, Software Heritage, GH Archive, Zenodo.
2. **Query Logging**:
   * Every search must be logged in `evidence/search-records/` with execution timestamp, database, exact query string, filters, total results count, and shortlisted inspected items.
3. **Null Searches**:
   * Zero-hit queries must be recorded to document search boundaries.

---

## 6. Immutability & Anti-Tampering Rules

1. **Audited Target Immutability**: The target repository snapshot at commit `51feb3d176e4a53773c22dc157567cc0486f4c71` is frozen.
2. **Preservation of Prior Audit Passes**: Historical final reports (`FINAL_AUDIT.md`, `AUDIT_PASS_2.md`) remain unedited historical audit artifacts.
3. **Audit History Transparency**: Search corrections, adverse findings, and revised claim evaluations must be committed to the public Git log of this repository.
