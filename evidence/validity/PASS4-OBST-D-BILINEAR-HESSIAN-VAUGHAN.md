# Mathematical Validity Dossier: Analytical Obstructions OBST-D (`CLM-OBST-011..015`)

> **Validity Dossier Governance Metadata**  
> * **Dossier ID**: `PASS4-OBST-D-BILINEAR-HESSIAN-VAUGHAN`  
> * **Audit Phase**: Pass 4 Phase 3 (Independent Mathematical Validity Audit)  
> * **Review Group**: Group D — Obstruction Group D (Bilinear Hessian, Type-II Separability, Vaughan/Heath-Brown Barrier)  
> * **Target Pinned Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Standards**: [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 7 & 8; [`AUDIT_PROTOCOL.md`](../../AUDIT_PROTOCOL.md).

---

## 1. Mathematical Scope & Group Description

Obstruction Group D evaluates structural no-go theorems establishing why conventional Vaughan/Heath-Brown divisor splitting and bilinear phase cancellation cannot bypass the square-root barrier on Laguerre chirp sums.

---

## 2. Claim-by-Claim Validity Review

### CLM-OBST-011
* **Proposition**: Rank-one Hessian $\operatorname{Hess}(\Phi_n) = \Phi_n'' \mathbf{1}\mathbf{1}^T$ in multiplicative convolutions.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L350-L354`
* **Independent Mathematical Check**:
  - For $m = a_1 \dots a_k$ with $r_j = \log a_j$, the Laguerre phase is $F_k(r_1, \dots, r_k) = \Phi_n(r_1 + \dots + r_k)$.
  - Partial derivatives: $\frac{\partial^2 F_k}{\partial r_i \partial r_j} = \Phi_n''(r_1 + \dots + r_k)$ for all $i, j \in \{1, \dots, k\}$.
  - The Hessian matrix is $\Phi_n'' \mathbf{1}\mathbf{1}^T$, which has rank identically 1 and nullspace of dimension $k-1$ corresponding to directions preserving the product $m$. Verified in `scripts/pass4_math_checks.py`.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-012
* **Proposition**: Standard dyadic Type-II chirp boxes are asymptotically separable (phase defect $O(1/n)$).
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L361-L365`
* **Independent Mathematical Check**:
  - On a dyadic box $a \in [M, 2M], b \in [N, 2N]$, the four-corner cross phase defect is $\Delta F = F(r_M+\log 2, r_N+\log 2) - F(r_M+\log 2, r_N) - F(r_M, r_N+\log 2) + F(r_M, r_N)$.
  - By Taylor expansion, $|\Delta F| \le \|\Phi_n''\|_\infty (\log 2)^2 \le \frac{C}{n}(\log 2)^2 = O(1/n)$.
  - Hence $\exp(i\Phi_n(\log(ab))) = P(a) Q(b) [1 + O(1/n)]$, proving asymptotic bilinear phase separability.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-013
* **Proposition**: Nonseparability threshold begins only at logarithmic widths of order $\sqrt{n}$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L372-L376`
* **Independent Mathematical Check**:
  - Cross phase defect on box of widths $H_r, H_s$ is $|\Phi_n''| H_r H_s \sim \frac{c}{n} H_r H_s$.
  - Reaching nonseparability $|\Delta F| \sim \Omega(1)$ requires $H_r H_s \sim \Omega(n)$, so balanced widths require $H_r \sim H_s \sim \sqrt{n}$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-014
* **Proposition**: Exponent bookkeeping: Direct fixed-interior prime estimates require $\delta \ge 1/2$ square-root saving.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L383-L387`
* **Independent Mathematical Check**:
  - At $X = \exp(4nu/A)$, an unweighted prime discrepancy bound $O(X^{1-\delta})$ multiplied by the critical half-weight $X^{-1/2}$ yields $X^{1/2-\delta}$.
  - Reaching the required subexponential target $X^{o(1)} = \exp(o(n))$ forces $1/2 - \delta \le 0 \implies \delta \ge 1/2$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-015
* **Proposition**: Structural no-go theorem for generic Vaughan/Heath-Brown phase cancellation applied to Laguerre RH criterion.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L394-L398`
* **Independent Mathematical Check**:
  - Multiplicative convolutions preserve rank-1 phase geometry (`CLM-OBST-011`), dyadic Type-II boxes are asymptotically separable (`CLM-OBST-012`), and direct magnitude bounds require square-root savings $\delta \ge 1/2$ (`CLM-OBST-014`).
  - Therefore, generic Type-I / Type-II divisor decompositions without new arithmetic input cannot prove subexponential root growth.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`
