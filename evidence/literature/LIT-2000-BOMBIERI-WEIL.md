# Primary Literature Dossier: Enrico Bombieri (2000)

> **Bibliographic Metadata**  
> * **Dossier ID**: `LIT-2000-BOMBIERI-WEIL`  
> * **Title**: *Remarks on Weil's quadratic functional in the theory of prime numbers, I*  
> * **Authors**: Enrico Bombieri  
> * **Publication**: *Atti della Accademia Nazionale dei Lincei. Classe di Scienze Fisiche, Matematiche e Naturali. Rendiconti Lincei. Matematica e Applicazioni*, Serie 9, Vol. 11, Fasc. 3 (2000), pp. 183–233  
> * **Stable URL**: [`http://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0`](http://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0)  
> * **Governing Protocol**: [`archive/FOURTH_AUDIT.md`](../../archive/FOURTH_AUDIT.md) Section 13 & 15; [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md).  
> * **Affected Candidate IDs**: `CLM-MATH-001`, `CLM-METH-001`, `CLM-OPER-001`, `CLM-OBST-001`.

---

## 1. Primary Mathematical Theorems & Results

Bombieri systematically develops the variational and spectral theory of Weil's quadratic functional on compact and general domains.

$$\lambda f(x) = (\mathcal{L} f)(x) \qquad \text{on } (-t, t)$$
* **Lemma 3**: Logarithmic-weighted moment bound exploiting the structure of the archimedean place at infinity.
* **Theorem 3**: Proves that the localized quadratic functional attains its minimum on the unit sphere of $L^2(E)$ for any compact interval $E$.

### 1.2 Section 4: The Euler-Lagrange Radical Equation
Derives the exact Euler-Lagrange integral equation for the extremizers / radical of the Weil functional on compact intervals:
$$\lambda f(x) = (\mathcal{L} f)(x) \qquad \text{on } (-t, t)$$
where $\mathcal{L}$ combines the singular archimedean convolution, the rank-2 pole boundary terms, and discrete prime translations.

### 1.3 Theorem 12: Quantitative Small-Support Coercivity
Establishes an explicit lower bound on the coercivity of the functional for test functions supported on small intervals of length $|I|$:
$$Q(f) \ge \bigl(\log(1/|I|) - \log\log(1 + 1/|I|) - O(1)\bigr) \|f\|_2^2$$
proving that small-support test functions are always strictly positive.

---

## 2. Comparison with `riemann-conjecture` (`51feb3d`)

| Technical Aspect | Enrico Bombieri (2000) | `riemann-conjecture` (`51feb3d`) | Audit Analysis |
| :--- | :--- | :--- | :--- |
| **Variational Foundation** | Proves attainment, compactness, and radical equation for localized functional. | Uses localized variational framework on $[-T, T]$. | **Foundational theoretical baseline** (`KNOWN INGREDIENT`). |
| **Active-Prime Thresholding** | General formulation of prime shift distributions. | Explicit compressed translation operator $P_2 = -\frac{\log 2}{\sqrt{2}} S_{T, \log 2}$ with norm $\|S_{T,a}\| = 2\cos\frac{\pi}{L+1}$. | Analytical isolation of first prime power. |
| **Numerical Certification** | Theoretical bounds and asymptotic analysis; Section 13 reports exploratory numerics. | Standalone zero-floating-point verifier checking exact rational certificates across $T=0.35..0.54$. | Standalone verified theorem chain. |

---

## 3. Disposition & Novelty Verdict

* **Disposition**: `KNOWN INGREDIENT / FOUNDATIONAL BASELINE`. Bombieri (2000) provides the theoretical variational framework for localized Weil functionals.
* **Audit Impact**: `riemann-conjecture`'s exact-prime Legendre-Schur synthesis builds upon the variational foundation established by Bombieri and Yoshida.
