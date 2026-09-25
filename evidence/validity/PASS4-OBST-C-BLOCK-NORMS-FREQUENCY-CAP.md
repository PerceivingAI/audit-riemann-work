# Mathematical Validity Dossier: Analytical Obstructions OBST-C (`CLM-OBST-006..010`)

> **Validity Dossier Governance Metadata**  
> * **Dossier ID**: `PASS4-OBST-C-BLOCK-NORMS-FREQUENCY-CAP`  
> * **Audit Phase**: Pass 4 Phase 3 (Independent Mathematical Validity Audit)  
> * **Review Group**: Group D — Obstruction Group C (Block Norms, Stationary Endpoints, Frequency Caps)  
> * **Target Pinned Commit**: `51feb3d176e4a53773c22dc157567cc0486f4c71`  
> * **Governing Standards**: [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 7 & 8; [`AUDIT_PROTOCOL.md`](../../AUDIT_PROTOCOL.md).

---

## 1. Mathematical Scope & Group Description

Obstruction Group C evaluates structural barriers related to $L^2$ block norms, high-frequency stationary phase coalescing, prime-imposed Mellin frequency caps, and Dirichlet polynomial length barriers.

---

## 2. Claim-by-Claim Validity Review

### CLM-OBST-006
* **Proposition**: Coefficient block-$L^2$ norm $M_N = \sum_{n=N}^{2N} |S_n|^2$ root behavior is itself RH-equivalent.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L273-L277`
* **Independent Mathematical Check**:
  - If $\limsup |S_n|^{1/n} \le 1$, then $M_N \le (N+1) \max_{N \le n \le 2N} |S_n|^2 \implies \limsup M_N^{1/(2N)} \le 1$.
  - Conversely, $|S_n|^2 \le M_n \implies \limsup |S_n|^{1/n} \le \limsup M_n^{1/(2n)} \le 1$.
  - Hence block-$L^2$ subexponentiality is strictly equivalent to pointwise subexponentiality and to RH.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-007
* **Proposition**: High-frequency stationary saddle merge into left endpoint at $n$-scale.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L284-L288`
* **Independent Mathematical Check**:
  - The Gaussian relative width at stationary point $u_\gamma$ satisfies $\sigma_u / u_\gamma = \sqrt{2\gamma / (An)}$.
  - For $\gamma \sim n$, $\sigma_u / u_\gamma \sim O(1)$, so the saddle point coalesces with the left boundary $u=0$ and standard interior stationary phase loses uniformity.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-008
* **Proposition**: Natural $\sqrt{n}$ Mellin frequency cap $\gamma_{\max}(n) = O(\sqrt{n})$ imposed by first prime $m=2$.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L306-L310`
* **Independent Mathematical Check**:
  - The first prime atom occurs at $x=2 \implies u_2 = \frac{A\log 2}{4n}$.
  - Inverse frequency map $\gamma(u) = \frac{A}{2}\sqrt{\frac{1-u}{u}}$ decreases in $u$.
  - Largest Mellin frequency evaluated at prime atoms is $\gamma_2(n) = \frac{A}{2}\sqrt{\frac{4n}{A\log 2}-1} \sim \sqrt{\frac{An}{\log 2}} = O(\sqrt{n})$. Verified in `scripts/pass4_math_checks.py`.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-009
* **Proposition**: Montgomery-Vaughan mean-value length barrier for exponentially long Dirichlet polynomials.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L328-L332`
* **Independent Mathematical Check**:
  - A fixed-interior chirp cell centered at $u_0 > 0$ has Dirichlet polynomial length $N = \exp(4nu_0/A + o(n))$.
  - The Montgomery–Vaughan mean-value theorem $\int_0^T |\sum a_n n^{-it}|^2 dt = \sum |a_n|^2 (T + O(N))$ yields an unavoidable length term $O(N)$.
  - The RMS scale is at best $\exp(2nu_0/A)$, yielding an exponential root base $\exp(2u_0/A) > 1$ that cannot reach the RH root target $\le 1$.
* **Verification Basis**: `[INDEPENDENT_DERIVATION, PRIMARY_LITERATURE_MATCH]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`

### CLM-OBST-010
* **Proposition**: Microlocal subexponential control of matched prime cells is already zero-sensitive.
* **Pinned Source Location**: `source/riemann-conjecture/docs/CLAIMS.md#L339-L343`
* **Independent Mathematical Check**:
  - Under the smooth explicit formula, an off-critical zero $\rho = \beta + i\gamma_0$ ($\beta > 1/2$) responds to a local cell centered at $X = \exp(4nu_0/A)$ at scale $X^{\beta-1/2} = \exp(4nu_0(\beta-1/2)/A)$.
  - Subexponential control $O(e^{o(n)})$ over matched local cells would force $\beta \le 1/2$, proving that local cell estimates are already zero-sensitive.
* **Verification Basis**: `[INDEPENDENT_DERIVATION]`
* **Validity Evidence Strength**: `E3` | **Factual Status**: `VERIFIED`
