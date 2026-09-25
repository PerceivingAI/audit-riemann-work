# Mathematical Validity Dossier: Airy Saddle Asymptotics & Nonlinear Chirp (`CLM-AIRY-001..007`)

> **Validity Dossier Governance Metadata**  
> * **Dossier ID**: `PASS4-AIRY-001-007-ASYMPTOTICS`  
> * **Audit Phase**: Pass 4 Phase 3 (Independent Mathematical Validity Audit)  
> * **Review Group**: Group C — Asymptotic / Stationary Phase / Airy Candidates  
> * **Target Pinned Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Standards**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 7 (Group C); [`AUDIT_PROTOCOL.md`](../../AUDIT_PROTOCOL.md).

---

## 1. Asymptotic Framework & Saddle Analysis

For the generalized prime trace, the kernel density in scaled coordinate $u = t/(4n)$ has exponential phase $\Phi_A(u) = 2\sqrt{u(u-1)} - \frac{s_0-1}{A} 4u$ for post-turning arguments $u > 1$.
* **Saddle Point**: Differentiating $\Phi_A'(u) = 0$ yields a unique maximum at $u_* = \frac{A^2}{A^2-1} > 1$.
* **Saddle Rate**: The value $\exp(n\Phi_A(u_*)) = \bigl(\frac{s_0}{s_0-1}\bigr)^n = |q|^n$, exactly matching the pole rate.
* **Pre-Turning Regime**: For $0 < u < 1$, the leading Bessel phase is $4n\xi(u) - 3\pi/4$, producing a nonlinear Mellin chirp.

---

## 2. Claim-by-Claim Validity Review

### CLM-AIRY-001
* **Proposition**: Smooth-density Airy saddle asymptotic rate $(s_0/(s_0-1))^n$ matching exact zeta-pole Cayley rate.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L163-L167`
* **Independent Derivation**: Verified in `scripts/pass4_math_checks.py`. $\Phi_A(u_*) = \log(s_0/(s_0-1))$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-AIRY-002
* **Proposition**: Quantitative asymptotic tradeoff between off-critical Cayley amplification and prime scale.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L174-L178`
* **Independent Derivation**: Off-critical Cayley amplification is $\log R_\rho = \frac{2\beta-1}{s_0} + O(s_0^{-2})$; saddle prime scale is $\log x_* = \frac{2n}{s_0} + O(ns_0^{-2})$. The ratio $\frac{\log(R_\rho^n)}{\log x_*} \to \frac{2\beta-1}{2}$ as $s_0 \to \infty$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-AIRY-003
* **Proposition**: Exact matching between single zero modes $\rho$ and generalized Laguerre/Cayley modes $z_\rho^{-n} - 1$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L218-L222`
* **Independent Derivation**: Expanding $-x^\rho/\rho$ in generalized Laguerre polynomials yields the discrete mode $z_\rho^{-n} - 1$ where $z_\rho = \frac{\rho-s_0}{\rho+s_0-1}$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-AIRY-004
* **Proposition**: Uniform stationary-frequency map between zero height $\gamma$, stationary coordinate $u$, and prime scale.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L240-L244`
* **Independent Derivation**: Stationary phase condition $\frac{d}{du}[4n\xi(u) - \gamma \log x] = 0$ yields $u_\gamma = \frac{A^2}{A^2+4\gamma^2}$, with inverse $\gamma = \frac{A}{2}\sqrt{\frac{1-u}{u}}$ and prime scale $\log x_\gamma = \frac{4nA}{A^2+4\gamma^2}$. Verified in `scripts/pass4_math_checks.py`.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-AIRY-005
* **Proposition**: Critical stationary saddle phase matches Cayley mode phase with unit leading normalization.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L251-L255`
* **Independent Derivation**: At $\rho = 1/2+i\gamma$, $4n[\gamma u_\gamma/A - \xi(u_\gamma)] = n \arg(z_\rho^{-1})$; stationary phase integration yields unit leading amplitude matching $z_\rho^{-n}$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-AIRY-006
* **Proposition**: Generalized Li prime kernel identified as critical-half-weight nonlinear Mellin chirp.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L262-L266`
* **Independent Derivation**: Phase $\Phi_n(y) = 4n\xi(Ay/(4n)) - 3\pi/4$ acting on $d\mu(y) = e^{-y/2}d(\psi(e^y)-e^y)$ has instantaneous frequency $\Phi_n'(y) = \frac{A}{2}\sqrt{(1-u)/u}$, forming a nonlinear Mellin chirp.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-AIRY-007
* **Proposition**: Microlocal reduction of generalized Li kernel to short smooth critical-half-weight prime sums.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L317-L321`
* **Independent Derivation**: Curvature $\Phi_n''(y_0) = -A^2/[16n u_0^{3/2}\sqrt{1-u_0}] \sim -c/n$. On a window $H = o(\sqrt{n})$, quadratic phase error is $O(H^2/n) = o(1)$, linearizing the chirp into a localized Dirichlet sum $\sum \Lambda(m) m^{-1/2+i\gamma_0} W((\log m - y_0)/H)$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`
