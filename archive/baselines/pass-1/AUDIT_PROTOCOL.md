# Audit Protocol

This document defines the operational rules, classification taxonomy, and analytical standards governing the independent audit of the `riemann-conjecture` repository.

---

## 1. Epistemological Stance

1. **Null Hypothesis**: The default stance for any candidate claim is **non-novelty** and **prior existence**.
2. **Burden of Proof**: The burden rests on proving novelty through exhaustive literature search, mathematical comparison, and structural differentiation.
3. **Hypothesis vs. Fact**: Unaudited propositions listed in `CLAIMS_TO_AUDIT.md` are hypotheses under test, not established facts.
4. **No Confirmation Bias**: Negative findings, overlapping prior art, and contradictory evidence must be fully documented and given equal prominence.

---

## 2. Standard Outcome Taxonomy

Every completed claim evaluation in `claims/` MUST terminate in exactly one of the following standardized verdicts:

| Verdict | Definition |
| :--- | :--- |
| `PRIOR ART FOUND` | An identical or subsuming theorem, bound, or method already exists in published literature or prior public preprints. |
| `INDEPENDENT REDISCOVERY` | The result was independently derived within the project, but identical/equivalent work was previously published or publicly disclosed elsewhere. |
| `POSSIBLY NOVEL — NO PRIOR ART FOUND` | Exhaustive multi-database search protocol yielded no identical prior art, but scope/generality does not warrant an absolute novelty assertion. |
| `NOVELTY SUPPORTED` | Verified structural, quantitative, or methodological distinction relative to all known prior art. |
| `PRIORITY PLAUSIBLE` | Public Git commit timestamps precede external preprint announcements, pending verification of submission metadata. |
| `PRIORITY SUPPORTED` | Definitive public timestamp precedence over external preprints/papers/repos across all relevant disclosure channels. |
| `INCONCLUSIVE` | Ambiguity in definitions, inaccessible primary sources, or contested mathematical equivalence prevent a definitive determination. |
| `CLAIM REQUIRES NARROWER WORDING` | The broad claim fails or overlaps with existing work, but a restricted, parameterized, or conditional formulation holds. |

---

## 3. Mathematical Normalization Rules

Before comparing any candidate claim to prior literature:

1. **Variable Normalization**: Align notation for intervals, support widths (e.g., support $L$ vs. half-width $T$), scaled coordinates ($[-1, 1]$ vs. $[0, 1]$), normalization constants, and Fourier transform conventions.
2. **Regime Alignment**: Distinguish between asymptotic results ($N \to \infty$, $t \to \infty$) and effective/explicit finite bounds.
3. **Operator Equivalence**: Map operators (transfer operators, Schur complements, discrete path Laplacians) to standard mathematical terminology before asserting methodological differences.

---

## 4. Separation Principles

To ensure rigorous analysis, the auditor must enforce three structural separations:

### A. Result Novelty vs. Method Novelty
* A theorem may prove a known bound, but the proof technique (e.g., Legendre coercivity vs. contour integration) may be novel.
* Conversely, a new method may yield bounds already surpassed by alternative methods.
* The audit MUST evaluate and state result novelty and method novelty separately.

### B. Ingredients vs. Synthesis
* Standard mathematical components (e.g., Gershgorin circle theorem, Schur complement, Legendre polynomials, path graph spectra) are standard mathematical tools.
* The audit evaluates the **synthesis and specific application** of these ingredients to the target problem, not the ingredients themselves.

### C. Analytical Proof vs. Computational Certificate
* Analytical proofs with closed-form algebraic coercivity must be distinguished from computer-assisted interval arithmetic verifications.

---

## 5. Literature Search Protocol

All literature searches must satisfy minimum evidentiary rigor:

1. **Databases Searched**:
   * Mathematical indices: MathSciNet / zbMATH.
   * Preprint repositories: arXiv (math.NT, math.CA, math.FA, math.SP).
   * Academic aggregators: Google Scholar, Semantic Scholar.
   * Open source codebases: GitHub, Zenodo.
2. **Query Logging**:
   * Every search must be logged in `evidence/search-records/` using `TEMPLATES/SEARCH_RECORD_TEMPLATE.md`.
   * Record query strings, boolean operators, date filters, returned hit counts, and inspected candidate papers.
3. **Negative Evidence**:
   * Failed or zero-hit queries must be recorded to document search boundaries.

---

## 6. Immutability & Anti-Tampering Rules

1. **Audited Target Immutability**: The target repository snapshot at commit `51feb3d176e4a53773c22dc157567cc0486f4c71` is frozen.
2. **No Upstream Changes**: Under no circumstances will any write, branch, tag, or PR be created in `PerceivingAI/riemann-conjecture`.
3. **Audit History Transparency**: Search corrections, adverse findings, and revised claim evaluations must be committed to the public Git log of this repository.
