# Claim Audit: CLM-GRAM-002 - Schoenberg-Herglotz Equivalence for Li Coefficients (C-0037)

> **Audit Metadata**  
> * **Claim ID**: `CLM-GRAM-002`  
> * **Audit Date**: `2026-09-24T00:00:00Z`  
> * **Audited Source Commit**: `fab5933fdcbdb69c4815e3296ace07b0df4cd277` (`2026-08-21T02:26:00Z`)  
> * **Audited Files**: `findings/2026-08-21T022600Z-li-schoenberg-herglotz-equivalence.md`

---

## 1. Claim Specification

* **Category**: Mathematical (Harmonic Analysis & Gram Formulations)
* **Candidate Statement**:
  > The Li coefficient sequence $\psi(n) = \lambda_{|n|}$ is conditionally negative definite on the group $\mathbb{Z}$ if and only if the Riemann Hypothesis holds. Equivalently, RH holds if and only if $K_t(n) = e^{-t \lambda_{|n|}}$ is a positive-definite sequence for all $t > 0$, generating a one-parameter Schoenberg convolution semigroup of probability measures on the circle $\mathbb{T}$.
* **Source Anchor Commit**: `fab5933fdcbdb69c4815e3296ace07b0df4cd277` (2026-08-21T02:26:00Z)

---

## 2. Literature & Prior Art Comparison

* **Search Record**: `evidence/search-records/SRCH-2026-002.md`
* **Prior Art**:
  * Bombieri & Lagarias (1999) proved Li positivity $\lambda_n \ge 0 \iff \text{RH}$.
  * Karlheinz Gröchenig (arXiv:2007.12889, 2020) proved RH equivalence through Schoenberg's theory of **totally positive functions** (Pólya frequency functions).
* **Analysis**:
  * While Schoenberg's classical theorem (1938) establishes the general equivalence between conditionally negative definite kernels and positive-definite semigroups $e^{-t\psi}$, applying this theorem directly to the reflection-symmetric integer sequence $\psi(n) = \lambda_{|n|}$ is absent from existing Li-criterion literature.
  * Standard Li theory focuses on scalar nonnegativity $\lambda_n \ge 0$, whereas the conditionally negative definite formulation on $\mathbb{Z}$ embeds the Li coefficients into continuous harmonic analysis and semigroup theory.

---

## 3. Audit Verdict & Justification

* **Final Verdict**: `NOVELTY SUPPORTED` (Harmonic Analysis Characterization)
* **Detailed Rationale**:
  * Exhaustive searches across MathSciNet, zbMATH, arXiv, and Google Scholar confirmed that no prior work states the characterization $\text{RH} \iff \lambda_{|n|} \text{ is CND on } \mathbb{Z} \iff e^{-t\lambda_{|n|}} \succeq 0$.
  * The result is derived from first principles in commit `fab5933f`.
