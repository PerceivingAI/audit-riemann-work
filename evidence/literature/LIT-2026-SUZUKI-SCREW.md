# Primary Literature Dossier: Masatoshi Suzuki (2026)

> **Bibliographic Metadata**  
> * **Dossier ID**: `LIT-2026-SUZUKI-SCREW`  
> * **Title**: *Weil's quadratic form via the screw function*  
> * **Authors**: Masatoshi Suzuki  
> * **Preprint**: `arXiv:2606.09096` (Submitted `2026-06-12T10:48:47Z`, revised `2026-06-25T03:52:12Z`, 35 pages)  
> * **DOI**: [`10.48550/arXiv.2606.09096`](https://doi.org/10.48550/arXiv.2606.09096)  
> * **Governing Protocol**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 13 & 15; [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md).  
> * **Affected Candidate IDs**: `CLM-MATH-001..008`, `CLM-METH-001`, `CLM-OBST-003`, `CLM-GRAM-002`.

---

## 1. Primary Mathematical Formulation

Suzuki introduces an operator-theoretic formulation of Weil's quadratic form using the Krein–de Branges theory of screw functions (Hilbert space self-adjoint extensions).

### 1.1 The Screw Function Formulation
* **The Screw Function $g(t)$**:
  $$g(t) = \frac{1}{2}|t|\log|t| + c_0 |t| + \sum_{n \ge 2} \frac{\Lambda(n)}{\sqrt{n}}(|t| - \log n)_+$$
  where $(u)_+ = \max(u, 0)$ introduces explicit non-smooth kinks at prime powers.
* **The Residual Kernel $r_0''(t)$**:
  Suzuki's exact finite-support Weil quadratic form on $L^2[-a, a]$ contains the mandatory truncated residual kernel:
  $$Q_W(f) = \langle D f, G_a D f \rangle$$
  where $G_a$ is an integral operator whose kernel combines the digamma multiplier, discrete prime translations, and a continuous double-integral residual kernel $R_T$.

### 1.2 Theorem 1.3 (Continuity & Degeneracy)
* Establishes that the localized Rayleigh quotient infimum $\lambda_a = \inf Q_W(f)/\|f\|^2$ is continuous and non-increasing in $a$.
* Proves that the first failure $a^*$ must be a degenerate ground state of the self-adjoint operator $A_a$.

---

## 2. Comparison with `riemann-conjecture` (`51feb3d`)

| Technical Aspect | Masatoshi Suzuki (2026) | `riemann-conjecture` (`51feb3d`) | Audit Analysis |
| :--- | :--- | :--- | :--- |
| **Residual Kernel Treatment** | Identifies the mandatory presence of $r_0''$ in exact finite-support forms. | Explicitly includes the Suzuki residual kernel $R_T$ in the exact-prime form (`CLM-OBST-003`). | **Consistent mathematical formulation**. |
| **High-Mode Tail Control** | Continuous-kernel Fredholm perturbation theory. | **Legendre Harmonic Coercivity** $J(P_n) = H_n \|P_n\|_2^2$ (Tuck 1964). | `riemann-conjecture` proves discrete high-mode coercivity. |
| **Numerical Certification** | Theoretical operator framework. | Standalone zero-floating-point Rust verifier checking exact rational certificates across $T=0.35..0.54$. | Standalone verified theorem chain. |

---

## 3. Disposition & Novelty Verdict

* **Disposition**: `KNOWN INGREDIENT / NOVEL SYNTHESIS SUPPORTED`. Suzuki (2026) establishes the screw function formulation and residual kernel properties.
* **Audit Impact**: `riemann-conjecture` incorporates Suzuki's mandatory residual kernel into its exact-prime Legendre-Schur synthesis (`CLM-OBST-003`), while implementing an independent numerical verification engine.
