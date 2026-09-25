# Mathematical Validity Dossier: Prime-Laguerre & Li-Gram Criteria (`CLM-LAGU`, `CLM-GRAM`)

> **Validity Dossier Governance Metadata**  
> * **Dossier ID**: `PASS4-LAGU-GRAM-VALIDITY`  
> * **Audit Phase**: Pass 4 Phase 3 (Independent Mathematical Validity Audit)  
> * **Review Group**: Group B — Exact Mathematical Identities / Criteria  
> * **Target Pinned Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Standards**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 7 (Group B); [`AUDIT_PROTOCOL.md`](../../AUDIT_PROTOCOL.md).

---

## 1. Prime-Laguerre Series & Shift Filters (`CLM-LAGU-001..005`)

### CLM-LAGU-001
* **Proposition**: Euler-product prime-Laguerre component: $-A\sum_{m\ge2}\Lambda(m)m^{-s_0} L_{n-1}^{(1)}(A\log m)$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L75-L79`
* **Independent Derivation**: Follows from logarithmic derivative expansion of Euler product $\sum_p \log(1-p^{-s})^{-1}$ evaluated at $s = s_0 + \frac{A z}{1-z}$ with generating function $(1-z)^{-2}\exp\bigl(\frac{x z}{z-1}\bigr) = \sum L_n^{(1)}(x) z^n$. Explicit in Lagarias (2007).
* **Verification Basis**: `[PRIMARY_LITERATURE_MATCH, INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-LAGU-002
* **Proposition**: Isolation of exact deterministic zeta-pole mode $1 - q^n$ ($q = -s_0/(s_0-1)$).
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L108-L112`
* **Independent Derivation**: The pole of $\xi(s)$ at $s=1$ under transformation $s(z) = s_0 + \frac{A z}{1-z}$ corresponds to $z_1 = \frac{1-s_0}{s_0} = q^{-1}$. Expanding $\log(1 - z/z_1) = -\sum \frac{q^n}{n} z^n$ yields the exact discrete pole mode $1 - q^n$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-LAGU-003
* **Proposition**: Pole-subtracted prime-Laguerre root criterion: $\text{RH} \iff \limsup |S_n|^{1/n} \le 1$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L119-L123`
* **Independent Derivation**: Once the geometric pole mode $q^n$ is subtracted ($S_n = P_n - (1-q^n)$), the remaining spectrum of zeros $\rho$ contributes $\sum (z_\rho^{-n}-1)$. Under RH, $|z_\rho| = 1 \implies |S_n|^{1/n} \le 1$. If RH fails, $\exists \rho$ with $\text{Re}(\rho) > 1/2 \implies |z_\rho| < 1 \implies \limsup |S_n|^{1/n} = |z_\rho|^{-1} > 1$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-LAGU-004
* **Proposition**: Exact representation of pole-subtracted sequence as weighted PNT discrepancy integral.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L130-L134`
* **Independent Derivation**: Integrating by parts against $d(\psi(x)-x)$: $\int_1^\infty f_n(x) d(\psi(x)-x) = \sum \Lambda(m) f_n(m) - \int_1^\infty f_n(x) dx$. The continuous density integral $\int_1^\infty x^{-s_0} L_{n-1}^{(1)}(A\log x) dx$ evaluates analytically to $\frac{1-q^n}{A}$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-LAGU-005
* **Proposition**: Exact pole-annihilating shift filter $T = (E-1)(E-q)$ preserving RH root criterion.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L141-L145`
* **Independent Derivation**: For $x_n = 1 - q^n$, $(E-1)x_n = -q^n(q-1)$, and $(E-q)[-q^n(q-1)] = -q^{n+1}(q-1) + q \cdot q^n(q-1) = 0$. Verified algebraically in `scripts/pass4_math_checks.py`.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

---

## 2. Li Gram Matrices & Schoenberg Equivalence (`CLM-GRAM-001..003`)

### CLM-GRAM-001
* **Proposition**: Li Gram matrix hierarchy $K^{(N)}_{jk} = \lambda_j + \lambda_k - \lambda_{|j-k|} \succeq 0 \iff \text{RH}$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L405-L409`
* **Independent Derivation**: Under RH, $\lambda_n = \sum_\rho [1 - (1-1/\rho)^n]$. The vectors $v_j(\rho) = 1 - (1-1/\rho)^j$ satisfy $\langle v_j, v_k \rangle = \lambda_j + \lambda_k - \lambda_{|j-k|}$, so $K^{(N)}$ is a sum of Gram matrices, hence PSD. Conversely, $K_{nn} = 2\lambda_n \ge 0 \implies \text{RH}$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-GRAM-002
* **Proposition**: Schoenberg-Herglotz characterization: $\psi(n) = \lambda_{|n|}$ conditionally negative definite on $\mathbb{Z} \iff \text{RH}$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L416-L420`
* **Independent Derivation**: Schoenberg (1938) proves that a sequence $\psi(n)$ on a group is CND iff $\exp(-t\psi(n))$ is positive definite for all $t > 0$. For $\psi(n) = \lambda_{|n|}$, $K_{jk} = \lambda_j + \lambda_k - \lambda_{|j-k|} \ge 0 \iff \psi(n)$ is CND.
* **Verification Basis**: `[INDEPENDENT_DERIVATION, PRIMARY_LITERATURE_MATCH]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-GRAM-003
* **Proposition**: Generalized prime Gram atoms have negative first diagonal and cannot be independently PSD.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L427-L431`
* **Independent Derivation**: A single prime atom contributes $-c_m [B_j + B_k - B_{|j-k|}]$ with $c_m > 0$. The $(1,1)$ entry is $-2c_m B_1 = -2c_m < 0$, so individual prime atoms are not PSD.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`
