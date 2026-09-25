# Primary Literature Dossier: Alain Groskin (2026)

> **Bibliographic Metadata**  
> * **Dossier ID**: `LIT-2026-GROSKIN-FINITE`  
> * **Title**: *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*  
> * **Authors**: Alain Groskin  
> * **Preprint**: `arXiv:2607.02828` (Submitted `2026-07-03T18:24:19Z`, 22 pages)  
> * **DOI**: [`10.48550/arXiv.2607.02828`](https://doi.org/10.48550/arXiv.2607.02828)  
> * **Governing Protocol**: [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 13 & 15; [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md).  
> * **Affected Candidate IDs**: `CLM-CONT-002`, `CLM-OBST-003`, `CLM-VERF-005`.

---

## 1. Primary Mathematical Framework

Groskin establishes two-sided certification rules for truncated Guinand–Weil quadratic forms on finite sections, rigorously characterizing the artifacts that arise from incomplete truncations.

### 1.1 Inconclusive Band & Spurious Negative Eigenvalues
* Proves that truncated finite sections lacking complete archimedean tail bounds produce an explicit **inconclusive band** of spurious negative eigenvalues.
* Demonstrates that finite floating-point sections without tail Gram bounds cannot reliably distinguish numerical artifacts from genuine counterexamples to RH.

---

## 2. Comparison with `riemann-conjecture` (`51feb3d`)

| Technical Aspect | Alain Groskin (2026) | `riemann-conjecture` (`CLM-CONT-002`, `CLM-OBST-003`) | Audit Analysis |
| :--- | :--- | :--- | :--- |
| **Rejection of Truncated Sections** | Theoretical analysis of the inconclusive band in finite truncations. | Explicit detection and algorithmic rejection of deceptive floating/truncated sections lacking tail Gram control (`CLM-CONT-002`). | **Consistent mathematical conclusions**. |
| **Tail Control Solution** | Theoretical error bounds. | Rigorous **3-Factor Component Tail-Gram Schur Criterion** $A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) > 0$. | `riemann-conjecture` implements an executable certificate verifier. |

---

## 3. Disposition & Novelty Verdict

* **Disposition**: `PARTIAL OVERLAP / INDEPENDENT IMPLEMENTATION`. Groskin (2026) analyzes the theoretical risk of truncated sections.
* **Audit Impact**: `riemann-conjecture` rigorously addresses this exact obstruction through its component tail-Gram Schur architecture.
