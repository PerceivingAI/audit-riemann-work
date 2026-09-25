# Master Prior Art & Comparator Dossier (Pass 4 Synthesis)

> **Dossier Metadata**  
> * **Audit Stage**: Audit Pass 4 Phase 1 Synthesis  
> * **Date Compiled**: `2026-09-25`  
> * **Standard**: Primary Literature Evidence Standards per [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) & [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md)  
> * **Governing Principles**: Primary sources evaluated from original documents and official records; comparator self-audits used as leads only; all comparisons normalized before evaluating novelty.

---

## 1. Primary External Comparators & Baselines

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   Master Comparative Literature Matrix                 │
├──────────────────────────┬──────────────────────┬──────────────────────┤
│ Primary Source Identifier│ Official Reference   │ Relationship to      │
│                          │ & Submission Date    │ Audited Project      │
├──────────────────────────┼──────────────────────┼──────────────────────┤
│ LIT-2026-CHUK-ZHU        │ arXiv:2608.24827     │ Result Subsumption at│
│                          │ v1: 2026-08-25       │ L=0.8; Distinct Proof│
│                          │ v2: 2026-09-02       │ Architecture         │
├──────────────────────────┼──────────────────────┼──────────────────────┤
│ LIT-2026-KUBER-HISTORY   │ Kuberwastaken/riemann│ Finite Subspace Certs│
│                          │ 2026-07-23 to 08-11  │ Only; Full-Space Open│
├──────────────────────────┼──────────────────────┼──────────────────────┤
│ LIT-1964-TUCK-LEGENDRE   │ J. Fluid Mech. 18(4) │ Foundational Legendre│
│                          │ (1964), pp. 619–635  │ Eigenvalue Identity  │
├──────────────────────────┼──────────────────────┼──────────────────────┤
│ LIT-2007-LAGARIAS-LICAE  │ Ann. Inst. Fourier 57│ Explicit Prior Art   │
│                          │ (2007), pp. 1689–1717│ for Prime-Laguerre   │
├──────────────────────────┼──────────────────────┼──────────────────────┤
│ LIT-1992-YOSHIDA         │ Adv. Stud. Pure Math.│ Foundational Compact │
│                          │ 21 (1992), 281–325   │ Prime-Free Positivity│
├──────────────────────────┼──────────────────────┼──────────────────────┤
│ LIT-2000-BOMBIERI-WEIL   │ Rend. Mat. Acc. Linc.│ Variational/Radical  │
│                          │ 11 (2000), 183–233   │ Functional Theory    │
├──────────────────────────┼──────────────────────┼──────────────────────┤
│ LIT-2020-CC-ARCHIMEDEAN  │ Selecta Math. 27(4)  │ Archimedean Sonin    │
│                          │ (2021); arXiv:2006.13│ Trace Positivity     │
├──────────────────────────┼──────────────────────┼──────────────────────┤
│ LIT-2025-CCM-SPECTRAL    │ arXiv:2511.22755     │ Operator Program     │
│                          │ (2025-11-27)         │ Simple-Even Spec Gap │
├──────────────────────────┼──────────────────────┼──────────────────────┤
│ LIT-2026-SUZUKI-SCREW    │ arXiv:2606.09096     │ Screw-Function Model │
│                          │ (2026-06-12/25)      │ Residual Kernel Form │
├──────────────────────────┼──────────────────────┼──────────────────────┤
│ LIT-2026-GROSKIN-FINITE  │ arXiv:2607.02828     │ Finite Guinand-Weil  │
│                          │ (2026-07-03)         │ Truncation Estimates │
└──────────────────────────┴──────────────────────┴──────────────────────┘
```

---

## 2. Dossier Summaries & Primary Findings

### 2.1 Marcus Chuk / Xuefeng Zhu (`arXiv:2608.24827`)
* **Primary Reference**: [`PASS4-CHUK-PRIMARY-SOURCE.md`](PASS4-CHUK-PRIMARY-SOURCE.md)
* **Core Result**: Certified full-space Weil positivity on $L=0.8$ ($Q(f) \ge 8.9\times 10^{-18} \|f\|_2^2 > 0$).
* **Audit Determination**:
  - Pinned continuation theorems at $T \in [0.40, 0.54]$ (`CLM-MATH-002..008`) committed after August 25 are mathematically subsumed by Chuk/Zhu's theorem at $L=0.8$ (`RESULT SUBSUMED BY PRIOR ART`).
  - The exact-prime Legendre-Schur method, Tuck harmonic coercivity, and zero-floating-point verifier are fundamentally distinct proof and software architectures (`NOVEL SYNTHESIS SUPPORTED`, `NOVEL VERIFICATION ARCHITECTURE`).

### 2.2 Kuber Mehta (`Kuberwastaken/riemann`)
* **Primary Reference**: [`PASS4-KUBER-COMMIT-HISTORY.md`](PASS4-KUBER-COMMIT-HISTORY.md)
* **Core Result**: 14D and 22D subspace certificates at $L=0.45..0.62$; $\varepsilon_N$ verification of CCM hypotheses on finite Dirichlet sine sections.
* **Audit Determination**:
  - Explicitly leaves full-space $L^2([-T, T])$ theorems uncertified in `UPDATES.md`.
  - Does not use Legendre harmonic coercivity or the discrete component tail-Gram Schur criterion.
  - Does not invalidate `riemann-conjecture`'s full-space theorems or exact-prime methodology.

### 2.3 E. O. Tuck (1964, *Journal of Fluid Mechanics*)
* **Citation**: E. O. Tuck, *Some methods for flows past blunt slender bodies*, J. Fluid Mech. 18(4), 1964, pp. 619–635, DOI: `10.1017/S0022112064000453`.
* **Primary Identity**:
  $$\int_{-1}^1 \frac{P_n(x) - P_n(y)}{|x-y|} \, dy = 2 H_n P_n(x), \qquad H_n = \sum_{k=1}^n \frac{1}{k}$$
* **Audit Determination**:
  - The eigenvalue identity alone is classical prior art (`PRIOR ART FOUND`).
  - Applying Tuck's identity to establish high-mode Legendre complement coercivity $\mu_N = H_N - c_T - c_2 - \rho_R > 0$ for localized Weil positivity is an original application (`KNOWN INGREDIENT / NOVEL APPLICATION`, `CLM-METH-002`).

### 2.4 J. C. Lagarias (2007, *Annales de l'Institut Fourier*)
* **Citation**: J. C. Lagarias, *Li coefficients for automorphic L-functions*, Ann. Inst. Fourier (Grenoble) 57(5), 2007, pp. 1689–1717.
* **Core Result**: Explicit formula for the prime component of the generalized Li coefficients in terms of Laguerre polynomials $L_{n-1}^{(1)}(A\log m)$.
* **Audit Determination**:
  - Explicit prior art for `CLM-LAGU-001` (`PRIOR ART FOUND`).

### 2.5 H. Yoshida (1992) & E. Bombieri (2000)
* **Citations**:
  - H. Yoshida, *On Hermitian forms attached to zeta functions*, Adv. Stud. Pure Math. 21, 1992, pp. 281–325.
  - E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I*, Rend. Mat. Acc. Lincei 11, 2000, pp. 183–233.
* **Core Results**:
  - Yoshida (1992, Theorem 1): Rigorous 200-mode error-bounded computation proving positivity on the full prime-free class $T \le \frac{1}{2}\log 2 \approx 0.34657$.
  - Bombieri (2000, Theorems 3, 12): Attainment of infimum on $L^2(E)$ and quantitative small-support coercivity bounds.
* **Audit Determination**: Foundational baseline for small-support and prime-free Weil positivity.

---

## 3. Claim-by-Claim Comparison Matrix (Phase 1)

| Candidate ID | Audited Proposition | Key External Comparators | Comparator Normalized Relation | Pass 4 Phase 1 Evidence Status |
| :--- | :--- | :--- | :--- | :--- |
| `CLM-MATH-001` | Localized Weil positivity at $(T, N) = (0.35, 32)$ | Yoshida (1992) at $T \le 0.34657$; Chuk (Aug 25) at $L=0.8$; Kuber (July 23) 14D subspace. | Pre-dates Chuk submission on local Git clock (Aug 21 vs Aug 25; public push unverified). Exceeds Yoshida prime-free bound ($0.35 > 0.34657$). | `POSSIBLY NOVEL` (Result) / `NOVEL SYNTHESIS SUPPORTED` (Method) |
| `CLM-MATH-002..008` | Localized Weil positivity at $T \in [0.40, 0.54]$ | Marcus Chuk / Xuefeng Zhu (arXiv:2608.24827) at $L=0.8$. | Subsumed by Chuk/Zhu's certified full-space theorem at $L=0.8$ ($[-0.54, 0.54] \subset [-0.8, 0.8]$). | `RESULT SUBSUMED BY PRIOR ART` (Result) / `NOVEL SYNTHESIS SUPPORTED` (Method) |
| `CLM-METH-001` | Exact-prime finite-support Weil decomposition | Kuber (`sigma_t1.py`); Suzuki (2026). | Original physical-space operator formulation preserving $p=2$ compressed translation geometry. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-METH-002` | Legendre harmonic coercivity $J(P_n) = H_n \|P_n\|_2^2$ | E. O. Tuck (1964). | Tuck (1964) provides eigenvalue identity; application to high-mode Weil coercivity is novel. | `KNOWN INGREDIENT / NOVEL APPLICATION` |
| `CLM-METH-003` | High-mode complement bound $\mu_N > 0$ | None found in prior literature. | Original synthesis bounding infinite-dimensional tail via harmonic numbers and kernel bounds. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-METH-004` | Component tail-Gram Schur criterion | Standard Schur complement; Kuber (`CONTINUATION.md` Thm 4.1). | 3-factor discrete matrix reduction is unique to `riemann-conjecture`. | `NOVEL SYNTHESIS SUPPORTED` |
| `CLM-OPER-001` | Thresholded compressed translations | Bombieri (2000); Suzuki (2026); Kuber (2026). | Explicit thresholding $T > \frac{1}{2}\log m$ and compressed shift analysis. | `KNOWN INGREDIENT / NOVEL APPLICATION` |
| `CLM-OPER-002` | Shift norm formula $\|S_{T,a}\| = 2\cos\frac{\pi}{L+1}$ | Classical Chebyshev path graph spectrum. | Application of path graph Chebyshev formula to compressed translation chains. | `KNOWN INGREDIENT / NOVEL APPLICATION` |
| `CLM-LAGU-001` | Euler-product prime-Laguerre expansion | J. C. Lagarias (2007). | Explicit in Lagarias (2007, Ann. Inst. Fourier). | `PRIOR ART FOUND` |
| `CLM-VERF-001..007` | Standalone zero-float Rust verifier & Lean proof chain | Kuber (`certify.py` / `RiemannFormal`); Chuk/Zhu (`mpmath`). | Standalone exact rational verifier and interval/LDL/Gershgorin formal soundness lemmas are distinct. | `NOVEL VERIFICATION ARCHITECTURE` |
