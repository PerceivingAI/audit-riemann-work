# Pass 3 Literature & Repository Search Record: PASS3-SRCH-003-LI-LAGUERRE-SCHOENBERG

> **Search Record Metadata**  
> * **Search ID**: `PASS3-SRCH-003-LI-LAGUERRE-SCHOENBERG`  
> * **Standard**: Reproducible Search Record per [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md) & [`THIRD_AUDIT.md`](../../THIRD_AUDIT.md)  
> * **Target Scope**: Li Coefficients, Schoenberg Semigroups, Pole Subtraction & Shift Filters  
> * **Access Date / Time**: `2026-09-24T22:35:00Z`  
> * **Auditor**: Independent Audit Pass 3 Team

---

## 1. Search Query Executions & Hit Counts

### Query 3.1: Li Coefficients & Conditionally Negative Definite Sequences
* **Database / Engine**: MathSciNet, zbMATH, arXiv (math.NT, math.CA), Wiley Online Library
* **Exact Query String**: `"Li coefficients" "conditionally negative definite" OR "negative definite" OR "Schoenberg" OR "Herglotz" "Riemann"`
* **Filters Applied**: All dates through 2026
* **Total Results Returned**: **55 hits**
* **Shortlisted Items Inspected**:
  1. I. J. Schoenberg, *Metric spaces and positive definite functions*, Trans. Amer. Math. Soc. 44(3), 522–536 (1938).
  2. X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory 65(1), 96–119 (1997).
  3. E. Bombieri & J. C. Lagarias, *Complements to Li's criterion for the Riemann hypothesis*, Acta Arith. 90(2), 177–187 (1999).
  4. K. Gröchenig, *Schoenberg's Theory of Totally Positive Functions and the Riemann Zeta Function*, arXiv:2007.12889 (2020).
  5. M. Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, J. London Math. Soc. 107(4), 1363–1396 (2023).
* **Adjudication**:
  - Standard Li criterion $\lambda_n \ge 0$ is a scalar sequence condition.
  - Proving $\psi(n) = \lambda_{|n|}$ is conditionally negative definite on $\mathbb{Z} \iff 	ext{RH}$ (and hence $e^{-t\lambda_{|n|}}$ is positive definite for all $t > 0$ via Schoenberg 1938) is an original structural synthesis (`NOVEL SYNTHESIS SUPPORTED`).

### Query 3.2: Laguerre Prime Expansions, Pole Subtraction & Shift Filters
* **Database / Engine**: MathSciNet, Google Scholar, arXiv
* **Exact Query String**: `"Li coefficients" "pole" "shift operator" OR "E-1" OR "Laguerre" "discrepancy"`
* **Filters Applied**: Date: `1997-01-01` to `2026-09-24`
* **Total Results Returned**: **23 hits**
* **Shortlisted Items Inspected**:
  1. J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*, Ann. Inst. Fourier 57(5), 1689–1740 (2007).
  2. M. W. Coffey, *Relations and positivity properties of the Li coefficients and prime numbers*, J. Math. Phys. 46(6), 062109 (2005).
  3. J. Arias de Reyna, *Asymptotics of Li's coefficients for the Riemann xi function*, arXiv:1102.3275 (2011).
* **Logged Null Query**: `"pole-annihilating shift filter" "(E-1)(E-q)"` $	o$ **0 hits (Null Search Logged)**.
* **Adjudication**:
  - Prime-Laguerre expansion $\lambda_n^{(p)}$: `PRIOR ART FOUND` (Lagarias 2007).
  - Exact pole mode $1-q^n$ isolation and second-order shift filter $T=(E-1)(E-q)$: `NOVEL SYNTHESIS SUPPORTED`.
