# Mathematical Validity Dossier: Analytical Obstructions OBST-B (`CLM-OBST-004..005`)

> **Validity Dossier Governance Metadata**  
> * **Dossier ID**: `PASS4-OBST-B-PNT-MOVING-SCALE`  
> * **Audit Phase**: Pass 4 Phase 3 (Independent Mathematical Validity Audit)  
> * **Review Group**: Group D — Obstruction Group B (PNT & Moving-Scale Barriers)  
> * **Target Pinned Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Standards**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 7 & 8; [`AUDIT_PROTOCOL.md`](../../AUDIT_PROTOCOL.md).

---

## 1. Mathematical Scope & Group Description

Obstruction Group B evaluates structural barriers preventing unconditional and quasi-Riemann prime error bounds from closing the Laguerre root criterion.

---

## 2. Claim-by-Claim Validity Review

### CLM-OBST-004
* **Proposition**: Obstruction: Pointwise PNT bounds $|\psi(x)-x| = O(x^\theta)$ cannot close root criterion.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L185-L189`
* **Independent Mathematical Check**:
  - Inserting an absolute pointwise error bound $|\psi(x)-x| \le C x^\theta$ with $\theta > 1/2$ into the discrepancy integral $S_n = A \int_1^\infty f_n(x) d(\psi(x)-x)$:
  - In the uniform Airy regime, the exponential envelope of $f_n(x) x^\theta$ has maximum $\exp(n \Phi_A(u_*; \theta))$ with $\Phi_A(u_*; \theta) > 0$.
  - Absolute estimation alone yields $\limsup |S_n|^{1/n} \ge e^{\Phi_A} > 1$, leaving a strictly positive exponential growth rate.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-005
* **Proposition**: Obstruction: Vinogradov-Korobov bounds remain exponentially insufficient on moving prime scales.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L207-L211`
* **Independent Mathematical Check**:
  - The Vinogradov-Korobov error bound gives $|\psi(x)-x| \le x \exp(-c (\log x)^{3/5} (\log\log x)^{-1/5})$.
  - On the moving prime scale $\log x \sim cn$, the error factor is $\exp(-c n^{3/5}) = \exp(-o(n))$.
  - The unperturbed Laguerre density root base is $\exp(2u/A) > 1$ for any fixed pre-turning coordinate $u > 0$.
  - The relative saving $\exp(-o(n))$ cannot overcome the $O(n)$ exponential growth $\exp(c n)$, so absolute-value estimation fails.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`
