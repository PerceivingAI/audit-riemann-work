# Candidate Claims Queue & Adjudication Status

> **IMPORTANT NOTICE**  
> This queue records the formal adjudication verdicts resulting from the independent audit of [`https://github.com/PerceivingAI/riemann-conjecture`](https://github.com/PerceivingAI/riemann-conjecture) conducted per [`AUDIT_PROTOCOL.md`](AUDIT_PROTOCOL.md).

> **Queue Metadata**  
> * **Queue Initialized**: `2026-09-24T00:00:00Z`  
> * **Last Queue Update**: `2026-09-24T00:00:00Z`  
> * **Audit Status**: `AUDIT_COMPLETE`  
> * **Total Claims Evaluated**: `50` (Adjudicated: 50, In Progress: 0, Queued: 0)

---

## I. Mathematical Results (Strict Finite-Support Weil-Positivity Theorems)

| Claim ID | Source Ref | Proposition Summary / Parameters | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-MATH-001` | C-0050 | Strict localized Weil positivity at $(T, N) = (7/20, 32) = (0.35, 32)$. | `6dd1d8f0...` (2026-08-21) | `NOVELTY SUPPORTED` / `PRIORITY SUPPORTED` | `claims/mathematical/CLM-MATH-001.md` |
| `CLM-MATH-002` | C-0051 | Strict localized Weil positivity at $(T, N) = (2/5, 40) = (0.40, 40)$. | `b5405a93...` (2026-08-26) | `NOVELTY SUPPORTED` / `PRIORITY SUPPORTED` | `claims/mathematical/CLM-MATH-001.md` |
| `CLM-MATH-003` | C-0052 | Strict localized Weil positivity at $(T, N) = (17/40, 48) = (0.425, 48)$. | `b5405a93...` (2026-08-26) | `NOVELTY SUPPORTED` / `PRIORITY SUPPORTED` | `claims/mathematical/CLM-MATH-001.md` |
| `CLM-MATH-004` | C-0053 | Strict localized Weil positivity at $(T, N) = (9/20, 56) = (0.45, 56)$. | `b5405a93...` (2026-08-26) | `NOVELTY SUPPORTED` / `PRIORITY SUPPORTED` | `claims/mathematical/CLM-MATH-001.md` |
| `CLM-MATH-005` | C-0054 | Strict localized Weil positivity at $(T, N) = (19/40, 68) = (0.475, 68)$. | `b5405a93...` (2026-08-26) | `NOVELTY SUPPORTED` / `PRIORITY SUPPORTED` | `claims/mathematical/CLM-MATH-001.md` |
| `CLM-MATH-006` | C-0055 | Strict localized Weil positivity at $(T, N) = (1/2, 80) = (0.50, 80)$. | `b5405a93...` (2026-08-26) | `NOVELTY SUPPORTED` / `PRIORITY SUPPORTED` | `claims/mathematical/CLM-MATH-001.md` |
| `CLM-MATH-007` | C-0056 | Strict localized Weil positivity at $(T, N) = (21/40, 96) = (0.525, 96)$. | `b5405a93...` (2026-08-26) | `NOVELTY SUPPORTED` / `PRIORITY SUPPORTED` | `claims/mathematical/CLM-MATH-001.md` |
| `CLM-MATH-008` | C-0057 | Strict localized Weil positivity at frontier $(T, N) = (27/50, 104) = (0.54, 104)$. | `51feb3d1...` (2026-09-24) | `NOVELTY SUPPORTED` / `VERIFIED` | `claims/mathematical/CLM-MATH-008.md` |

---

## II. Exact-Prime Legendre-Schur Methodology Claims

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-METH-001` | Sec. 2 | Exact-prime finite-support Weil decomposition preserving $p=2$ translation geometry. | `3111accb...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/methodology/CLM-METH-002.md` |
| `CLM-METH-002` | C-0045 | Legendre harmonic coercivity: $J(P_n) = H_n \|P_n\|_2^2 \implies J(q) \ge H_N \|q\|_2^2$. | `3111accb...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/methodology/CLM-METH-002.md` |
| `CLM-METH-003` | C-0047 | Exact-prime high-mode complement bound: $\mu_N = H_N - c_T - c_2 - \rho_R > 0$. | `3111accb...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/methodology/CLM-METH-002.md` |
| `CLM-METH-004` | C-0048 | Component tail-Gram Schur criterion: $A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) > 0$. | `3111accb...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/methodology/CLM-METH-002.md` |
| `CLM-METH-005` | Sec. 6 | Exact proof architecture: Complement coercivity $\to$ Schur $\to$ Outward intervals $\to$ LDL/Gershgorin. | `6dd1d8f0...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/verification/CLM-VERF-001.md` |

---

## III. Exact Compressed-Translation & Operator Claims

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-OPER-001` | C-0039 | Weil prime powers as thresholded compressed translations active only when $T > \frac{1}{2}\log m$. | `fab5933f...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/methodology/CLM-METH-002.md` |
| `CLM-OPER-002` | C-0040 | Exact finite-chain spectral formula for compressed symmetric shifts: $\|S_{T,a}\| = 2\cos\frac{\pi}{L+1}$. | `fab5933f...` (2026-08-21) | `NOVELTY SUPPORTED` (Synthesis) | `evidence/literature/LITERATURE_BASELINE.md` |

---

## IV. Continuation & Workflow Mechanism Claims

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-CONT-001` | Sec. 9 | Moving-dimension strategy: increasing $N$ restores rigorous positivity as $T$ grows. | `b5405a93...` (2026-08-26) | `NOVELTY SUPPORTED` | `claims/mathematical/CLM-MATH-008.md` |
| `CLM-CONT-002` | Sec. 10 | Rigorous rejection of deceptive floating/truncated finite sections. | `51feb3d1...` (2026-09-24) | `NOVELTY SUPPORTED` | `claims/verification/CLM-VERF-005.md` |

---

## V. Negative Results & Structural Obstructions (Weil Side)

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-OBST-001` | Sec. 11 | Uniform endpoint absorption $V + P_2 \ge \frac{69}{100}V \ge 0$ is valid locally but too lossy globally. | `3111accb...` (2026-08-21) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-OBST-002` | C-0043 | Positive-kernel decomposition of real digamma multiplier into monotone quadratic forms. | `3111accb...` (2026-08-21) | `NOVELTY SUPPORTED` | `evidence/literature/LITERATURE_BASELINE.md` |
| `CLM-OBST-003` | Sec. 13 | Detection and correction of incomplete finite-support Weil discretizations missing Suzuki residual. | `3111accb...` (2026-08-21) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |

---

## VI. Li / Laguerre Prime-Side Results & Criteria

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-LAGU-001` | C-0006 | Euler-product prime-Laguerre component: $-A\sum_{m\ge2}\Lambda(m)m^{-s_0} L_{n-1}^{(1)}(A\log m)$. | `cc57e703...` (2026-08-20) | `PRIOR ART FOUND` (Lagarias 2007) | `evidence/literature/LIT-2007-LAGARIAS-LICAE.md` |
| `CLM-LAGU-002` | C-0009 | Isolation of exact deterministic zeta-pole mode $1 - q^n$ ($q = -s_0/(s_0-1)$). | `cc57e703...` (2026-08-20) | `NOVELTY SUPPORTED` | `claims/mathematical/CLM-LAGU-005.md` |
| `CLM-LAGU-003` | C-0010 | Pole-subtracted prime-Laguerre root criterion: $\text{RH} \iff \limsup |S_n|^{1/n} \le 1$. | `cc57e703...` (2026-08-20) | `NOVELTY SUPPORTED` | `claims/mathematical/CLM-LAGU-005.md` |
| `CLM-LAGU-004` | C-0011 | Exact representation of pole-subtracted sequence as weighted PNT discrepancy integral. | `cc57e703...` (2026-08-20) | `NOVELTY SUPPORTED` | `claims/mathematical/CLM-LAGU-005.md` |
| `CLM-LAGU-005` | C-0012 | Exact pole-annihilating shift filter $T = (E-1)(E-q)$ preserving RH root criterion. | `cc57e703...` (2026-08-20) | `NOVELTY SUPPORTED` | `claims/mathematical/CLM-LAGU-005.md` |

---

## VII. Airy / Stationary-Phase & Chirp Formulations

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-AIRY-001` | C-0014 | Smooth-density Airy saddle asymptotic rate $(s_0/(s_0-1))^n$ matching exact zeta-pole Cayley rate. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-AIRY-002` | Sec. 20 | Quantitative asymptotic tradeoff between off-critical Cayley amplification and prime scale. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-AIRY-003` | C-0019 | Exact matching between single zero modes $\rho$ and generalized Laguerre/Cayley modes $z_\rho^{-n} - 1$. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-AIRY-004` | C-0021 | Uniform stationary-frequency map between zero height $\gamma$, stationary coordinate $u$, and prime scale. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-AIRY-005` | C-0022 | Critical stationary saddle phase matches Cayley mode phase with unit leading normalization. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-AIRY-006` | C-0023 | Generalized Li prime kernel identified as critical-half-weight nonlinear Mellin chirp. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-AIRY-007` | Sec. 25 | Microlocal reduction of generalized Li kernel to short smooth critical-half-weight prime sums. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |

---

## VIII. Analytical Barriers & Obstructions (Prime / Laguerre Side)

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-OBST-004` | C-0016 | Obstruction: Pointwise PNT bounds $|\psi(x)-x| = O(x^\theta)$ cannot close root criterion. | `cc57e703...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-OBST-005` | C-0018 | Obstruction: Vinogradov-Korobov bounds remain exponentially insufficient on moving prime scales. | `cc57e703...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-OBST-006` | C-0024 | Coefficient block-$L^2$ norm $M_N = \sum_{n=N}^{2N} |S_n|^2$ root behavior is itself RH-equivalent. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-OBST-007` | C-0025 | High-frequency stationary saddle merge into left endpoint at $n$-scale. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-OBST-008` | C-0027 | Natural $\sqrt{n}$ Mellin frequency cap $\gamma_{\max}(n) = O(\sqrt{n})$ imposed by first prime $m=2$. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-OBST-009` | Sec. 31 | Montgomery-Vaughan mean-value length barrier for exponentially long Dirichlet polynomials. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-OBST-010` | Sec. 32 | Microlocal subexponential control of matched prime cells is already zero-sensitive. | `64e884b8...` (2026-08-20) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |

---

## IX. Bilinear / Vaughan / Heath-Brown Phase Obstructions

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-OBST-011` | C-0031 | Rank-one Hessian $\operatorname{Hess}\Phi_n = \Phi_n'' \mathbf{1}\mathbf{1}^T$ in multiplicative convolutions. | `1752f19d...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/mathematical/CLM-OBST-011.md` |
| `CLM-OBST-012` | C-0032 | Standard dyadic Type-II chirp boxes are asymptotically separable (phase defect $O(1/n)$). | `1752f19d...` (2026-08-21) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-OBST-013` | C-0033 | Nonseparability threshold begins only at logarithmic widths of order $\sqrt{n}$. | `1752f19d...` (2026-08-21) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-OBST-014` | Sec. 36 | Exponent bookkeeping: Direct fixed-interior prime estimates require $\delta \ge 1/2$ square-root saving. | `1752f19d...` (2026-08-21) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |
| `CLM-OBST-015` | Sec. 37 | Structural no-go theorem for generic Vaughan/Heath-Brown phase cancellation applied to Laguerre RH criterion. | `1752f19d...` (2026-08-21) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |

---

## X. Li Gram & Harmonic Analysis Reformulations

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-GRAM-001` | C-0036 | Li Gram matrix hierarchy $K^{(N)}_{jk} = \lambda_j + \lambda_k - \lambda_{|j-k|} \succeq 0 \iff \text{RH}$. | `fab5933f...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/mathematical/CLM-GRAM-002.md` |
| `CLM-GRAM-002` | C-0037 | Schoenberg-Herglotz characterization: $\psi(n) = \lambda_{|n|}$ conditionally negative definite on $\mathbb{Z} \iff \text{RH}$. | `fab5933f...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/mathematical/CLM-GRAM-002.md` |
| `CLM-GRAM-003` | C-0038 | Generalized prime Gram atoms have negative first diagonal and cannot be independently PSD. | `fab5933f...` (2026-08-21) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_2_INTERIM_REPORT.md` |

---

## XI. Verification & Software Architecture Claims

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-VERF-001` | Sec. 41 | Exact rational/dyadic theorem certificates converted from Arb interval enclosures. | `6dd1d8f0...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/verification/CLM-VERF-001.md` |
| `CLM-VERF-002` | Sec. 42 | Independent zero-floating-point Rust replay verifier (`rh_cert`) checking all theorem steps. | `6dd1d8f0...` (2026-08-21) | `NOVELTY SUPPORTED` | `claims/verification/CLM-VERF-001.md` |
| `CLM-VERF-003` | Sec. 43 | Multi-implementation closed theorem admission across Python generator, validator, schema, and Rust verifier. | `51feb3d1...` (2026-09-24) | `NOVELTY SUPPORTED` | `claims/verification/CLM-VERF-005.md` |
| `CLM-VERF-004` | Sec. 44 | Explicit pre-theorem promotion boundary separating candidate discovery from formal admission. | `b5405a93...` (2026-08-26) | `NOVELTY SUPPORTED` | `claims/verification/CLM-VERF-005.md` |
| `CLM-VERF-005` | Sec. 45 | Adversarial certificate verification distinguishing contract failure from genuine mathematical failure. | `51feb3d1...` (2026-09-24) | `NOVELTY SUPPORTED` | `claims/verification/CLM-VERF-005.md` |
| `CLM-VERF-006` | Sec. 46 | Publicly replayable retained proof chain with SHA-256 identities verified on every build (8/8 PASS). | `51feb3d1...` (2026-09-24) | `NOVELTY SUPPORTED` / `VERIFIED` | `claims/verification/CLM-VERF-006.md` |
| `CLM-VERF-007` | Sec. 47 | Lean formalization of verifier soundness ingredients (interval reasoning, LDL/Gershgorin, congruence transfer). | `51feb3d1...` (2026-09-24) | `NOVELTY SUPPORTED` | `reports/interim/PHASE_3_INTERIM_REPORT.md` |

---

## XII. Research Integrity & Priority Precedence Claims

| Claim ID | Source Ref | Proposition Summary | Source Anchor Commit | Status / Verdict | Dossier Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CLM-PRIO-001` | Sec. 48 | Fully public open-science research record since creation date `2026-08-20T20:39:42Z`. | `[Repo-Init]` | `PRIORITY SUPPORTED` / `VERIFIED` | `evidence/public-timeline/TIMELINE_MATRIX.md` |
| `CLM-PRIO-002` | Sec. 49 | Public negative-result and obstruction trail preserved alongside theorems. | `[Continuous]` | `PRIORITY SUPPORTED` / `VERIFIED` | `evidence/public-timeline/TIMELINE_MATRIX.md` |
| `CLM-PRIO-003` | Sec. 50 | Public scientific correction trail without history rewriting. | `[Continuous]` | `PRIORITY SUPPORTED` / `VERIFIED` | `evidence/public-timeline/TIMELINE_MATRIX.md` |
| `CLM-PRIO-004` | Sec. 54(1) | Earliest public exact-prime Legendre-Schur proof of strict localized Weil positivity. | `3111accb...` (2026-08-21) | `PRIORITY SUPPORTED` | `claims/priority/CLM-PRIO-004.md` |
| `CLM-PRIO-005` | Sec. 54(2) | Earliest public finite-support Weil positivity theorem at $T=7/20$ (C-0050). | `6dd1d8f0...` (2026-08-21) | `PRIORITY SUPPORTED` | `claims/priority/CLM-PRIO-005.md` |
| `CLM-PRIO-006` | Sec. 54(3) | Earliest public sequence of certified localized Weil positivity extending through $T=27/50$. | `51feb3d1...` (2026-09-24) | `PRIORITY SUPPORTED` | `claims/priority/CLM-PRIO-006.md` |
| `CLM-PRIO-007` | Sec. 54(11) | First exact pole-annihilating shift filter for generalized prime-Laguerre Li sequences. | `cc57e703...` (2026-08-20) | `PRIORITY SUPPORTED` | `claims/priority/CLM-PRIO-007.md` |
| `CLM-PRIO-008` | Sec. 54(12) | First prime-Laguerre RH root criterion after exact zeta-pole subtraction. | `cc57e703...` (2026-08-20) | `PRIORITY SUPPORTED` | `claims/priority/CLM-PRIO-008.md` |
| `CLM-PRIO-009` | Sec. 54(14) | First interpretation of generalized Li prime kernel as critical-half-weight nonlinear Mellin chirp. | `64e884b8...` (2026-08-20) | `PRIORITY SUPPORTED` | `claims/priority/CLM-PRIO-009.md` |
| `CLM-PRIO-010` | Sec. 54(15) | First rank-one Hessian / separability obstruction for Vaughan/Heath-Brown decompositions of the chirp. | `1752f19d...` (2026-08-21) | `PRIORITY SUPPORTED` | `claims/priority/CLM-PRIO-010.md` |
| `CLM-PRIO-011` | Sec. 54(16) | First conditional-negative-definite / Schoenberg characterization of RH directly from Li coefficients. | `fab5933f...` (2026-08-21) | `PRIORITY SUPPORTED` | `claims/priority/CLM-PRIO-011.md` |
| `CLM-PRIO-012` | Sec. 54(17) | First compressed-translation operator treatment making Weil prime-entry thresholds and shift norm explicit. | `fab5933f...` (2026-08-21) | `PRIORITY SUPPORTED` | `claims/priority/CLM-PRIO-012.md` |

---

## XIII. Negative Claim Boundaries Adjudication

The audit confirms that the project adheres to all negative boundary constraints:
* **NO RH PROOF CLAIM**: Verified. The repository nowhere claims to have proved the Riemann Hypothesis.
* **NO ARBITRARY SUPPORT CLAIM**: Verified. All results are strictly localized to compact supports $T \le 27/50$.
* **NO TWO-PRIME EXTENSION CLAIM**: Verified. The repository explicitly stops at $T=0.54$, acknowledging that $p=3$ activation ($T \ge 0.5493$) requires new multi-prime operator geometry.
* **NO STANDARD INGREDIENT NOVELTY CLAIM**: Verified. Standard ingredients (Tuck's Legendre identity, Gershgorin, Schur complement, Arb intervals, Schoenberg theorem) are properly cited as foundational antecedents.
