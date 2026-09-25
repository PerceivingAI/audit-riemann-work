# Literature Dossier: LIT-2026-CHUK-V2 (Marcus Chuk, arXiv:2608.24827)

> **Bibliographic Metadata**  
> * **Dossier ID**: `LIT-2026-CHUK-V2`  
> * **Title**: *Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law*  
> * **Author**: Marcus Chuk  
> * **Venue**: arXiv Preprint (`math.NT`, `math.CA`)  
> * **arXiv Identifier**: `arXiv:2608.24827`  
> * **Submission Timestamp (v1)**: `2026-08-25T11:42:00Z`  
> * **Revision Timestamp (v2)**: `2026-09-04T18:15:00Z`  
> * **Attribution Note**: Primary author is Marcus Chuk (some web mirrors display automated scrapers attributing to Xuefeng Zhu).

---

## 1. Primary Mathematical Theorem & Scope

Marcus Chuk establishes the first unconditional computer-assisted certificate of localized Weil positivity on a compact support window $L = 0.8$ (corresponding to autocorrelation support width $2L = 1.6$).

### Primary Theorem Statement:
Let $Q(f)$ denote Weil's quadratic functional on test functions $f \in L^2([-L, L])$. For $L = 0.8$:
$$\lambda^*(0.8) = \inf_{f \in L^2([-0.8, 0.8]), \|f\|_2=1} Q(f) \ge 8.9 \times 10^{-18} > 0.$$
Furthermore, Chuk establishes the rigorous two-sided enclosure:
$$8.9 \times 10^{-18} \le \lambda^*(0.8) \le 2.27 \times 10^{-17}.$$

---

## 2. Technical Proof Architecture

### 2.1 Discretization Strategy
* **Modal Expansion**: Full modal expansion in Legendre polynomials $\{P_n\}_{n=0}^N$ scaled to $[-L, L]$.
* **Quadrature Certification**: Gauss-Legendre quadrature combined with spherical Bessel recurrence relations for operator matrix elements.
* **Continuous Tail Decay Envelope**: The infinite-dimensional tail is controlled by deriving a continuous pointwise decay envelope for the Weil symbol in Fourier space, proving that modes $n > N$ decay at a certified exponential rate.

### 2.2 Numerical Verification Engine
* **Precision**: High-precision floating-point interval arithmetic using MPFI / Arb.
* **Certificate Matrix**: Bounding the minimum eigenvalue of the certified interval matrix via certified interval Cholesky factorization.

---

## 3. Comparison with `riemann-conjecture` (`C-0050..0057`)

| Technical Dimension | Marcus Chuk (`arXiv:2608.24827`) | `PerceivingAI/riemann-conjecture` (`C-0050..C-0057`) | Audit Analysis |
| :--- | :--- | :--- | :--- |
| **First Public Timestamp** | **2026-08-25T11:42:00Z** (Public arXiv Submission) | **2026-08-21T14:05:13Z** (`6dd1d8f` Git Commit) | Git commit pre-dates Chuk by 3.9 days; public push unverified. |
| **Support Parameter** | $L = 0.8$ ($[-0.8, 0.8]$, width $1.6$) | $T = 0.35 	o 0.54$ ($[-T, T]$) | Chuk proves positivity across a wider support domain than $T=0.54$. |
| **Proof Architecture** | Full numerical discretization + continuous Fourier decay envelope | Exact-prime operator decomposition + Tuck harmonic coercivity + Schur complement | **Two fundamentally distinct mathematical proof architectures.** |
| **First-Prime Handling** | Global numerical quadrature integral | Explicit compressed translation operator $P_2 = -\frac{\log 2}{\sqrt{2}} S_{T, \log 2}$ | `riemann-conjecture` isolates analytical prime geometry. |
| **Verification Engine** | Floating-point interval arithmetic (Arb/MPFI) | Zero-floating-point standalone Rust verifier (`rh_cert`, `BigRational`) | Exact rational certificates vs. floating interval certificates. |

---

## 4. Priority & Novelty Impact on Audit Claims

1. **Result Novelty Impact on `C-0051..C-0057`**:
   Because Marcus Chuk publicly submitted a certified full-space theorem at $L=0.8$ on August 25, 2026, subsequent repository continuation points $T \in [0.40, 0.54]$ (`C-0051..C-0057`) committed between August 26 and September 24 do **not** constitute novel support boundary records. They are classified as `RESULT SUBSUMED BY PRIOR ART` (valid method demonstrations).
2. **Method & Verification Novelty**:
   The exact-prime Legendre-Schur synthesis and zero-floating-point exact rational verifier remain **fully independent and novel methodologies**.
