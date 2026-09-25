# Mathematical Validity Dossier: Methodology, Operators, and Continuation (`CLM-METH`, `CLM-OPER`, `CLM-CONT`)

> **Validity Dossier Governance Metadata**  
> * **Dossier ID**: `PASS4-METH-OPER-CONT-VALIDITY`  
> * **Audit Phase**: Pass 4 Phase 3 (Independent Mathematical Validity Audit)  
> * **Review Group**: Groups B & E — Methodology, Operators, and Continuation  
> * **Target Pinned Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Standards**: [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 7 & 20; [`AUDIT_PROTOCOL.md`](../../AUDIT_PROTOCOL.md).

---

## 1. Exact-Prime Methodology Candidates (`CLM-METH-001..005`)

### CLM-METH-001
* **Proposition**: Exact-prime finite-support Weil decomposition preserving $p=2$ translation geometry.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L438-L442`, `L493-L497`
* **Independent Derivation & Verification**:
  - The exact-prime decomposition partitions $Q_T(w) = J(w) + V(w) + P_2(w) + R_T(w) - c_T \|w\|_2^2$.
  - Preserves physical-space translation $P_2 = -\frac{\log 2}{\sqrt{2}} S_{T, \log 2}$ without replacing it with an approximate smooth multiplier.
* **Verification Basis**: `[INDEPENDENT_DERIVATION, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-METH-002
* **Proposition**: Legendre harmonic coercivity: $J(P_n) = H_n \|P_n\|_2^2 \implies J(q) \ge H_N \|q\|_2^2$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L504-L508`
* **Independent Derivation & Verification**:
  - Tuck (1964) proves $\int_{-1}^1 \frac{P_n(x)-P_n(y)}{|x-y|} dy = 2H_n P_n(x)$.
  - By orthogonality, for $q = \sum_{n \ge N} a_n P_n$, $J(q) = \sum_{n \ge N} |a_n|^2 H_n \|P_n\|_2^2 \ge H_N \sum_{n \ge N} |a_n|^2 \|P_n\|_2^2 = H_N \|q\|_2^2$ since $H_n$ is strictly increasing.
  - Verified by numerical quadrature in `scripts/pass4_math_checks.py`.
* **Verification Basis**: `[INDEPENDENT_DERIVATION, PRIMARY_LITERATURE_MATCH]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-METH-003
* **Proposition**: Exact-prime high-mode complement bound: $\mu_N = H_N - c_T - c_2 - \rho_R > 0$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L526-L530`
* **Independent Derivation & Verification**:
  - On $\mathcal{Q}_N$, $Q_T(q) \ge (H_N - c_T - c_2 - \rho_R)\|q\|_2^2$.
  - For $T=0.35, N=32$, $H_{32} = 4.0585$, $c_{0.35} \approx 2.45$, $c_2 \approx 0.4901$, $\rho_R \approx 0.46 \implies \mu_{32} \approx 0.658 > 0$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION, MACHINE_REPLAY]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-METH-004
* **Proposition**: Component tail-Gram Schur criterion: $A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) > 0$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L537-L541`
* **Independent Derivation & Verification**:
  - By Schur complement theorem, $Q_T(p+q) \ge \langle p, A_N p \rangle - \frac{1}{\mu_N}\|B_N p\|_2^2$.
  - Decomposing $B_N = B_V + B_2 + B_R$, Cauchy-Schwarz gives $\|(B_V+B_2+B_R)p\|^2 \le 3(\|B_V p\|^2 + \|B_2 p\|^2 + \|B_R p\|^2) = 3 \langle p, (G_V+G_2+G_R)p \rangle$.
  - Positivity of $A_N - \frac{3}{\mu_N}(G_V+G_2+G_R)$ rigorously guarantees full operator positivity.
* **Verification Basis**: `[INDEPENDENT_DERIVATION, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-METH-005
* **Proposition**: Exact proof architecture: Complement coercivity $\to$ Schur $\to$ Outward intervals $\to$ LDL/Gershgorin.
* **Pinned Source Location**: `source/riemann-conjecture/README.md#L214-L235`
* **Independent Verification**: Replay and code inspection of `rh_cert` and `scripts.cert.*`.
* **Verification Basis**: `[CODE_INSPECTION, MACHINE_REPLAY]`
* **Validity Evidence Strength**: `E4` | **Factual Status**: `VERIFIED`

---

## 2. Operator & Continuation Candidates (`CLM-OPER`, `CLM-CONT`)

### CLM-OPER-001
* **Proposition**: Weil prime powers as thresholded compressed translations active only when $T > \frac{1}{2}\log m$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L438-L442`
* **Independent Derivation**: Autocorrelation support of $f \in L^2[-T, T]$ is $[-2T, 2T]$; prime term $\log m$ enters iff $\log m < 2T \iff T > \frac{1}{2}\log m$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OPER-002
* **Proposition**: Exact finite-chain spectral formula for compressed symmetric shifts: $\|S_{T,a}\| = 2\cos\frac{\pi}{L+1}$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L449-L453`
* **Independent Derivation**: Tridiagonal path graph adjacency spectrum has eigenvalues $2\cos\frac{k\pi}{L+1}$, maximum at $k=1$. Verified in `scripts/pass4_math_checks.py`.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-CONT-001
* **Proposition**: Moving-dimension strategy: increasing $N$ restores rigorous positivity as $T$ grows.
* **Pinned Source Location**: `source/riemann-conjecture/findings/2026-08-26T171400Z-moving-dimension-restores-one-prime-continuation.md#L9-L54`
* **Independent Verification**: Evaluated finite instances $T=0.35 (N=32) \to T=0.40 (N=40) \to \dots \to T=0.54 (N=104)$. Applies to explicit admitted sequence; does not assert arbitrary-support continuation.
* **Verification Basis**: `[SOURCE_DERIVATION_REVIEW, MACHINE_REPLAY]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-CONT-002
* **Proposition**: Rigorous rejection of deceptive floating/truncated finite sections.
* **Pinned Source Location**: `source/riemann-conjecture/README.md#L214-L235`
* **Independent Verification**: Code review of verifier error handling; verified rejection of truncated sections lacking tail Gram bounds.
* **Verification Basis**: `[CODE_INSPECTION, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`
