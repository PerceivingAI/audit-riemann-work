# Pass 2 Search Record: PASS2-SRCH-001-COMPARATORS

> **Search Execution Metadata**  
> * **Search ID**: `PASS2-SRCH-001-COMPARATORS`  
> * **Date Executed**: `2026-09-24T20:25:00Z`  
> * **Auditor / Scope**: Pass 2 Comparative Analysis of `Kuberwastaken/riemann` and Marcus Chuk (`arXiv:2608.24827`)  
> * **Databases Queried**: GitHub, arXiv, Crossref, Google Scholar, Web

---

## 1. Query Formulations & Targets

### Target 1: `Kuberwastaken/riemann`
* **Query 1**: `"Kuberwastaken" riemann OR "kuberwastaken/riemann" OR "kuberwastaken" site:github.com`
* **Query 2**: `site:github.com/Kuberwastaken/riemann "Weil" OR "positivity" OR "Legendre" OR "Arb" OR "experiments"`
* **Target Findings**:
  - Author: Kuber Mehta
  - Release Date: `2026-07-23` (Citation CFF)
  - Scope: Research archive collecting 178 primary sources on RH.
  - Mathematical content: Computer-assisted numerical/interval experiments on compact Weil positivity in `experiments/weil_positivity/`.
  - Certified results: Verified archimedean coercivity $c_0 \ge 0.349152$; certified positivity for finite-dimensional test families at $L=0.45, 0.50, 0.545, 0.60$ and $L=0.62$ arithmetic rescue.
  - Method: Python + Arb ball arithmetic + certified Cholesky on finite-dimensional subspaces.
  - Crucial distinction: `Kuberwastaken/riemann` explicitly documents in `UPDATES.md` and `FINDINGS.md` that its certified results are **finite-dimensional**; it does not prove full-space $L^2([-T,T])$ theorems because infinite-dimensional spectral/tail bounds were left uncertified. It does not employ Legendre harmonic coercivity or exact-prime Schur reductions.

### Target 2: Marcus Chuk (`arXiv:2608.24827`)
* **Query 1**: `"2608.24827" OR "Marcus Chuk" "Weil positivity in compact windows"`
* **Target Findings**:
  - Title: *Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law*
  - Submission Date: `2026-08-25T11:42:00Z` (arXiv:2608.24827 [math.NT])
  - Theorem: Full-space unconditional certified positivity at $L=0.8$ (autocorrelation width $1.6$):
    $$Q(f) \ge 8.9 \times 10^{-18} \|f\|_2^2 \qquad \forall f \in L^2([-0.8, 0.8])$$
  - Method: Full Legendre modal expansion, Gauss-Legendre quadrature discretization, spherical-Bessel recurrences, interval arithmetic certificate of matrix positivity combined with a continuous symbol decay envelope for tail bounds.
  - Crucial comparison: Chuk proves full-space positivity at a wider support window ($L=0.8$) than `riemann-conjecture`'s $T \in [0.35, 0.54]$, but uses a numerical interval/quadrature proof architecture rather than `riemann-conjecture`'s exact-prime operator decomposition $A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) > 0$ and zero-floating-point exact-rational verification engine.
