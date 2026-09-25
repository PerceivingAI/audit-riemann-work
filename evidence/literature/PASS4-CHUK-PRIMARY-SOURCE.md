# Primary Literature Dossier: Marcus Chuk / Xuefeng Zhu (`arXiv:2608.24827`)

> **Primary Source Bibliographic Metadata**  
> * **Dossier ID**: `PASS4-CHUK-PRIMARY-SOURCE`  
> * **arXiv Identifier**: `arXiv:2608.24827`  
> * **DOI**: [`10.48550/arXiv.2608.24827`](https://doi.org/10.48550/arXiv.2608.24827)  
> * **Version History (from official arXiv records)**:  
>   * **v1**: Submitted `2026-08-25T17:07:51Z` (231 KB PDF) | Author: **Marcus Chuk** | Title: *Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law* (9-page announcement).  
>   * **v2**: Submitted `2026-09-02T17:32:21Z` (460 KB PDF) | Author: **Xuefeng Zhu** (Affiliation: School of Mechanics and Aerospace Engineering, Dalian University of Technology) | Title: *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law* (34 pages, 4 figures). Comments: *"v2: full version; v1 was a 9-page announcement. Author name and affiliation updated."*  
> * **Primary License**: `http://arxiv.org/licenses/nonexclusive-distrib/1.0/` (arXiv perpetual non-exclusive license).  
> * **Audit Date**: `2026-09-25` (Pass 4 Phase 1).  
> * **Raw Archive Artifacts**: Preserved in `evidence/phase1/chuk/` (manifest SHA-256 verified).  
> * **Governing Protocol**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 11; [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md).

---

## 1. Primary Mathematical Theorems & Normalized Statements

The paper investigates the normalized infimum of the Weil quadratic functional on compact support windows:
$$\lambda^*(L) = \inf_{f \in L^2(\mathbb{R}), \, \operatorname{supp} f \subseteq [-L, L], \, \|f\|_2 = 1} Q(f)$$

### 1.1 Theorem 1.1: One-Stroke Reduction
For any $L > 0$, define the prime-comb mass $A_L = \sum_{\log n < 2L} \frac{2\Lambda(n)}{\sqrt{n}}$ and the comb-alignment frequency $T_1 = 2\pi e^{A_L}$. For any $T^\sharp > T_1$ such that $\beta^* := \log\frac{T^\sharp}{2\pi} - \frac{1}{T^\sharp} - A_L > 0$, the Weil quadratic form satisfies the lower bound:
$$Q(f) \ge R(f) := 2F(i/2)^2 + \frac{1}{\pi}\int_0^{T^\sharp} \bigl(\Psi_L(t) - \beta^*\bigr)|F(t)|^2 \, dt + \beta^* \|f\|_2^2$$
Representing $R$ in the normalized Legendre basis $\{T_n\}_{n \text{ even}}$ of $L^2_{\text{even}}[-L, L]$ yields an infinite matrix $\beta^* I + 2pp^T + C$, whose leading $N \times N$ block $M_N$ controls the full operator:
$$Q(f) \ge \bigl(\min(\lambda_{\min}(M_N), \, \beta^* - \varepsilon_D) - \varepsilon_B\bigr) \|f\|_2^2$$
where $\varepsilon_D, \varepsilon_B \le 10^{-100}$ are explicit super-exponential tail bounds when $2N \gtrsim eLT^\sharp/2$.

### 1.2 Theorem 1.2: Certified Positivity on Support 1.6 ($L=0.8$)
For every real even $f \in L^2(\mathbb{R})$ with $\operatorname{supp} f \subseteq [-0.8, 0.8]$ (autocorrelation support $\operatorname{supp}(f \star \tilde{f}) \subseteq [-1.6, 1.6]$):
$$Q(f) \ge 8.9 \times 10^{-18} \|f\|_2^2 > 0$$
Furthermore, Theorem 6.2 and Corollary 6.3 establish that:
1. Positivity holds for **arbitrary complex** test functions $f \in L^2[-0.8, 0.8]$ (since the odd parity sector satisfies $Q \ge 8.2 \times 10^{-15} \|f\|_2^2$).
2. The window ground state is strictly simple and even, with certified spectral gap $\lambda_2 - \lambda_1 \ge 8.1 \times 10^{-15}$.

### 1.3 Two-Sided Enclosure & Landau-Widom Law
At $L=0.8$, the paper combines the certified lower bound with certified variational upper bounds to establish the rigorous two-sided enclosure:
$$8.9 \times 10^{-18} \le \lambda^*(0.8) \le 2.27 \times 10^{-17}$$
Across $L \in [0.5, 2.0]$, the upper bounds obey the Landau-Widom scaling law:
$$-\ln \lambda^*(L) \simeq 2\pi^2 \frac{N(T^*)}{\ln N(T^*)}, \qquad T^*(L) = 2\pi e^{2L}$$
where $2\pi^2$ matches the eigenvalue-plunge rate of prolate time-band limiting operators.

### 1.4 Retraction of Support 2.38 Claim (Section 7)
Section 7 explicitly retracts an earlier draft claim of a certified theorem at support $2.38$ ($L=1.19$), explaining that a per-prime envelope sharpening had bounded the prime comb in the wrong direction. Lemma 3.2 proves that $\sup_t \sum \frac{2\Lambda(n)}{\sqrt{n}}\cos(t\log n) = A_L$ is optimal, making the comb threshold $T_1 = 2\pi e^{A_L}$ unavoidable for any pointwise-envelope method.

---

## 2. Technical Proof Architecture & Verification Mechanisms

```text
┌────────────────────────────────────────────────────────────────────────┐
│               Chuk / Zhu Proof Architecture (arXiv:2608.24827)         │
├──────────────────────────┬─────────────────────────────────────────────┤
│ Discretization Basis     │ Scaled Legendre polynomials T_n(x) on [-L,L]│
├──────────────────────────┼─────────────────────────────────────────────┤
│ Fourier Representation   │ Spherical Bessel functions j_n(tL)          │
├──────────────────────────┼─────────────────────────────────────────────┤
│ Tail Control Mechanism   │ Pointwise symbol envelope on [T^#, infinity)│
├──────────────────────────┼─────────────────────────────────────────────┤
│ Matrix Certificate       │ Finite N x N Legendre Galerkin matrix       │
│                          │ (N=200 even modes, T^# = 200 at L=0.8)      │
├──────────────────────────┼─────────────────────────────────────────────┤
│ Arithmetic Precision     │ High-precision floating intervals (mpmath,  │
│                          │ 50 dps for L=0.8, up to 365 dps for L=2.0)  │
├──────────────────────────┼─────────────────────────────────────────────┤
│ Acceptance Algorithm     │ Certified interval Cholesky factorization   │
└──────────────────────────┴─────────────────────────────────────────────┘
```

### Supplementary Code & Data Investigation:
In Section 17, the author states:
> *"Source for both pipelines, software versions, zero data, certified matrices and Cholesky factors, run logs, error budgets and SHA-256 hashes are provided as supplementary material, together with an independent verifier (verify_certificate.py, depending on mpmath alone)..."*

**Audit Finding on Supplementary Availability**:
- Inspection of the official arXiv e-print source archive (`https://arxiv.org/e-print/2608.24827v2`, SHA-256 `1afc4e867bc69cabf5128db8b70187af61804e55bd773a16cdf16d17c4284c73`) confirmed that the source tar contains only `00README.json`, `main.tex`, and four PNG figure files.
- No auxiliary Python scripts (`verify_certificate.py`) or matrix data files are packaged within the arXiv source tar.
- No public GitHub/GitLab repository URL is referenced in the paper text.
- Consequently, while the paper provides full mathematical specifications and formulas, the standalone executable verifier `verify_certificate.py` is currently unavailable in public repositories.

---

## 3. Comparison with `riemann-conjecture` (`51feb3d`)

| Dimension | Marcus Chuk / Xuefeng Zhu (`arXiv:2608.24827`) | `PerceivingAI/riemann-conjecture` (`51feb3d`) | Normalized Comparative Analysis |
| :--- | :--- | :--- | :--- |
| **First Public Timestamp** | **2026-08-25T17:07:51Z** (Public arXiv Submission v1) | **2026-08-21T14:05:13Z** (`6dd1d8f` Git Commit for $T=0.35$) | Commit `6dd1d8f` predates Chuk v1 by 4.1 days (local Git clock; public push unverified). Continuation points $T \in [0.40, 0.54]$ (`b5405a9`, Aug 26 to `51feb3d`, Sep 24) postdate Chuk v1. |
| **Support Domain** | $L = 0.8$ (Support $[-0.8, 0.8]$, autocorrelation $[-1.6, 1.6]$) | $T = 0.35 \dots 0.54$ (Support $[-T, T]$, autocorrelation $[-2T, 2T] = [-1.08, 1.08]$) | **Domain Inclusion**: $[-0.54, 0.54] \subset [-0.8, 0.8]$. Chuk/Zhu proves positivity over a strictly wider window than $T=0.54$. |
| **Proof Strategy** | **One-Stroke Pointwise Symbol Envelope** on $[0, T^\sharp]$ + Legendre Galerkin matrix. | **Exact-Prime Operator Decomposition** + **Tuck Legendre Harmonic Coercivity** + **3-Factor Schur Complement**. | **Two Fundamentally Distinct Mathematical Architectures**. |
| **First-Prime Treatment** | Global cosine sum $\sum \frac{2\Lambda(n)}{\sqrt{n}}\cos(t\log n)$ in Fourier multiplier. | **Thresholded Compressed Translation Operator** $P_2 = -\frac{\log 2}{\sqrt{2}} S_{T, \log 2}$ on physical space $L^2[-T, T]$. | Physical-space compressed shift analysis vs. Fourier symbol multiplier. |
| **Infinite Tail Bound** | Pointwise Binet/logarithmic envelope $\beta^* = \log(T^\sharp/2\pi) - 1/T^\sharp - A_L > 0$. | **Legendre Harmonic Number Coercivity** $\mu_N = H_N - c_T - c_2 - \rho_R > 0$ derived from Tuck (1964). | Fourier-tail envelope vs. Legendre mode eigenvalue coercivity. |
| **Verification Architecture** | Python 3 + `mpmath` / `gmpy2` floating-point interval Cholesky. | Standalone zero-floating-point Rust verifier (`rh_cert`, `BigRational` arithmetic). | High-precision floating interval certificates vs. exact rational interval certificates. |

---

## 4. Impact on Audit Claims

1. **Mathematical Result Novelty (`CLM-MATH-001..008`)**:
   - `CLM-MATH-001` ($T=0.35$): Local commit `6dd1d8f` (`2026-08-21T14:05:13Z`) pre-dates Chuk's submission. Public push remains unverified (`PRIORITY PLAUSIBLE`). Classified as `POSSIBLY NOVEL`.
   - `CLM-MATH-002..008` ($T=0.40..0.54$): Pinned commits (`b5405a93`, Aug 26 through `51feb3d1`, Sep 24) post-date Chuk's public submission on August 25. Because $T \le 0.54 < 0.80$, these theorem records are mathematically subsumed by Chuk/Zhu's $L=0.8$ theorem (`RESULT SUBSUMED BY PRIOR ART`).
2. **Method Novelty (`CLM-METH-001..005`)**:
   - Chuk/Zhu does **not** anticipate or use the exact-prime operator decomposition (`CLM-METH-001`), Tuck's Legendre harmonic coercivity (`CLM-METH-002`), exact complement bounds (`CLM-METH-003`), or the 3-component tail-Gram Schur criterion (`CLM-METH-004`).
   - The exact-prime Legendre-Schur methodology remains an **independent and novel mathematical synthesis** (`NOVEL SYNTHESIS SUPPORTED`).
3. **Software & Verification Novelty (`CLM-VERF-001..007`)**:
   - Chuk/Zhu utilizes floating-point interval arithmetic (`mpmath`). `riemann-conjecture`'s zero-floating-point standalone Rust verifier (`rh_cert`, `BigRational`) and Lean 4 formalization remain **novel verification architectures** (`NOVEL VERIFICATION ARCHITECTURE`).
