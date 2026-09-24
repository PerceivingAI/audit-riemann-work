# Literature Baseline & Prior Art Synthesis

> **Audit Baseline Metadata**  
> * **Phase**: Phase 1 Deliverable  
> * **Completion Date**: `2026-09-24T00:00:00Z`  
> * **Status**: Baseline Established across Pre-2026 & 2026 Literature

---

## 1. Executive Summary of Literature Baseline

Phase 1 established the comparative state of mathematical literature across the four primary pillars of the `riemann-conjecture` project:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ Pillar 1: Finite-Support Weil Positivity                               │
│ • Foundational: Weil (1952), Bombieri (1999), Connes–Consani (2021)   │
│ • Continuous/Operator: Suzuki (arXiv:2606.09096, June 2026)            │
│ • Computational: Chuk (arXiv:2608.24827, Aug 25 2026) at L=0.8         │
└────────────────────────────────────────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ Pillar 2: Li Criterion & Generalized Laguerre Formulations             │
│ • Foundational: Li (1997), Bombieri–Lagarias (1999), Lagarias (2007)   │
│ • Asymptotics: Coffey (2005), Arias de Reyna (2011), Knessl (2011)     │
│ • Generalized Centers: Sekatskii (2013)                                │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ Pillar 3: Harmonic Analysis & Positivity Equivalences                  │
│ • Total Positivity: Gröchenig (arXiv:2007.12889, 2020)                 │
│ • Model Space Norms: Suzuki (2023, 2025)                               │
│ • CND / Schoenberg Sequence: No direct prior formulation on Z          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ Pillar 4: Methodological & Computational Frameworks                    │
│ • Standard Ingredients: Legendre polynomials, Schur complements,       │
│   Gershgorin circle theorem, path-graph spectrum, Arb intervals        │
│ • Target Repo Synthesis: Exact-prime component Schur decomposition,   │
│   Legendre harmonic coercivity J(Pn)=Hn||Pn||^2, zero-float Rust replay│
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Key Prior Art Findings by Research Pillar

### A. Finite-Support Localized Weil Positivity (Tier A)
1. **Prior Art Context**:
   * Alain Connes & Caterina Consani (*Selecta Math.* 2021) developed windowed archimedean Weil positivity via scaling operators and prolate spheroidal wave functions.
   * Masatoshi Suzuki (arXiv:2606.09096, June 2026) reformulated Weil positivity via continuous screw functions.
2. **Contemporary 2026 Work**:
   * Marcus Chuk submitted arXiv:2608.24827 on **August 25, 2026**, certifying positivity at $L=0.8$ via full Legendre matrix discretization with Gauss-Legendre quadrature.
3. **Audit Precedence & Methodological Anchor**:
   * The `riemann-conjecture` repository publicly committed theorem C-0050 ($T=0.35, N=32$) on **August 21, 2026** (commit `6dd1d8f0`), establishing that the project's exact-prime Legendre-Schur method was publicly disclosed prior to Chuk's posting.

---

### B. Li Criterion, Laguerre Polynomials & Shift Filters (Tier B)
1. **Prior Art Context**:
   * Jeffrey C. Lagarias (*Ann. Inst. Fourier* 2007) proved the structural identity connecting Li test polynomials to generalized Laguerre polynomials $P_n(x) = L_{n-1}^{(1)}(-x)$.
   * Juan Arias de Reyna (2011) and Knessl & Coffey (2011) established asymptotic properties and Laurent/Stieltjes expansions near the zeta pole at $s=1$.
2. **Audit Distinction**:
   * The representation of raw prime terms through $L_{n-1}^{(1)}$ is standard prior art (Lagarias 2007).
   * The explicit discrete extraction of the zeta-pole mode $1-q^n$ with $q=-s_0/(s_0-1)$, the discrete shift filter $T=(E-1)(E-q)$, and the pole-subtracted root-growth criterion $\limsup |S_n|^{1/n} \le 1$ represent distinct operator adaptations.

---

### C. Schoenberg & Conditionally Negative Definite Sequences (Tier B)
1. **Prior Art Context**:
   * Karlheinz Gröchenig (arXiv:2007.12889, 2020) connected RH to Schoenberg's theory of **totally positive functions** (real zero / Pólya frequency theory).
2. **Audit Distinction**:
   * Prior literature has not formulated the sequence $\psi(n) = \lambda_{|n|}$ directly as a conditionally negative definite function on $\mathbb{Z}$ yielding the Schoenberg convolution semigroup $e^{-t\lambda_{|n|}}$. This confirms the characterization in `CLM-GRAM-002` addresses an unmapped structural formulation in literature.

---

## 3. Literature Dossiers & Search Records Completed

* **Search Logs**:
  * [`evidence/search-records/SRCH-2026-001.md`](../search-records/SRCH-2026-001.md): Pre-2026 and 2026 Weil Positivity Literature.
  * [`evidence/search-records/SRCH-2026-002.md`](../search-records/SRCH-2026-002.md): Pre-2026 Li Criterion, Laguerre Polynomials & Schoenberg Equivalence.
* **Bibliographic Dossiers**:
  * [`evidence/literature/LIT-2026-CHUK-WEILPOS.md`](LIT-2026-CHUK-WEILPOS.md): Marcus Chuk (arXiv:2608.24827, Aug 25, 2026).
  * [`evidence/literature/LIT-2026-SUZUKI-WEILSCREW.md`](LIT-2026-SUZUKI-WEILSCREW.md): Masatoshi Suzuki (arXiv:2606.09096, June 8, 2026).
  * [`evidence/literature/LIT-2007-LAGARIAS-LICAE.md`](LIT-2007-LAGARIAS-LICAE.md): Jeffrey C. Lagarias (*Ann. Inst. Fourier*, 2007).

---

## 4. Phase 1 Exit Gate Sign-Off

* [x] Pre-2026 prior art mapped across Weil positivity, Li criterion, Laguerre expansions, and Schoenberg theory.
* [x] 2026 contemporary preprints identified (Suzuki June 2026, Chuk August 2026).
* [x] Mathematical normalizations established ($T=L$, operator decompositions, discrete vs. continuous formulations).
* [x] Search records and bibliographic dossiers logged with timestamped metadata.

**Phase 1 is formally COMPLETE. The audit is ready to advance to Phase 2 (Mathematical & Methodological Claim Audits).**
