# Mathematical Validity Dossier: Analytical Obstructions OBST-A (`CLM-OBST-001..003`)

> **Validity Dossier Governance Metadata**  
> * **Dossier ID**: `PASS4-OBST-A-ENDPOINT-COERCIVITY`  
> * **Audit Phase**: Pass 4 Phase 3 (Independent Mathematical Validity Audit)  
> * **Review Group**: Group D — Obstruction Group A (Endpoint, Coercivity, Residuals)  
> * **Target Pinned Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Standards**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 7 & 8; [`AUDIT_PROTOCOL.md`](../../AUDIT_PROTOCOL.md).

---

## 1. Mathematical Scope & Group Description

Obstruction Group A evaluates candidate structural obstructions in the Weil quadratic functional relating to endpoint absorption, digamma decomposition, and finite-support residual kernel completeness.

---

## 2. Claim-by-Claim Validity Review

### CLM-OBST-001
* **Proposition**: Uniform endpoint absorption $V + P_2 \ge \frac{69}{100}V \ge 0$ is valid locally but too lossy globally.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L471-L475`, `L515-L519`
* **Independent Mathematical Check**:
  - Locally at $T=0.35$, $V(x) + P_2(x) \ge 0.69 V(x) \ge 0$.
  - However, replacing $V+P_2$ globally by $0.69V$ produces an indefinite operator: on the test polynomial $w = P_0 - P_2 = \frac{3}{2}(1-x^2)$, the lower bound $J(w) + 0.69V(w) + R_T(w) - c_T \|w\|_2^2 < 0$.
  - Proves that uniform endpoint absorption cannot be extended globally without losing positivity.
* **Verification Basis**: `[INDEPENDENT_DERIVATION, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-002
* **Proposition**: Positive-kernel decomposition of real digamma multiplier into monotone quadratic forms.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L482-L486`
* **Independent Mathematical Check**:
  - For $a_k = k+1/4$, $\text{Re}\psi(1/4+i\xi/2) - \log\pi = m_0 + \sum_{k \ge 0} [1/a_k - 4a_k/(\xi^2+4a_k^2)]$.
  - Under Fourier inversion, each term corresponds to the positive semidefinite quadratic form $\frac{1}{a_k}\|f\|_2^2 - \iint e^{-2a_k|t-s|}f(t)\overline{f(s)} dt ds \ge 0$.
  - Partial sums provide monotone lower bounds for the digamma multiplier.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-003
* **Proposition**: Detection and correction of incomplete finite-support Weil discretizations missing Suzuki residual.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L493-L497`
* **Independent Mathematical Check**:
  - Suzuki (2026) establishes that the exact finite-support Weil form contains the double-integral residual kernel $R_T(w)$ derived from the truncated screw function $r_0''(u)$.
  - Any discretization omitting $R_T$ calculates a truncated sub-operator, not the exact localized Weil functional.
* **Verification Basis**: `[PRIMARY_LITERATURE_MATCH, SOURCE_DERIVATION_REVIEW]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`
