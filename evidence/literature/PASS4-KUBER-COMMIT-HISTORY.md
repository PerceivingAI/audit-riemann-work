# Comparator Commit History: Kuber Mehta (`Kuberwastaken/riemann`)

> **Comparator Provenance & Audit Metadata**  
> * **Repository**: [`https://github.com/Kuberwastaken/riemann`](https://github.com/Kuberwastaken/riemann)  
> * **Audit Date**: `2026-09-25` (Pass 4 Phase 1)  
> * **Repository Head SHA**: `94fa51e8f26794ef2d206c6c12e7adb4d85cbeaf`  
> * **Public Creation Timestamp**: `2026-07-23T10:22:27Z` (GitHub API)  
> * **Last Pushed Timestamp**: `2026-08-11T20:32:37Z` (GitHub API)  
> * **History Scope**: 419 total reachable commits across 2 primary development cycles (July 23–24 and August 11, 2026); 211 scoped commits touching tracked documentation, logs, experiments, and formal verification.  
> * **Local Mirror**: `.audit-cache/phase1/kuber-repo/` (Full Git object repository; 254 original-content text blobs retained in `evidence/phase1/kuber/objects/`).  
> * **Governing Protocol**: [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md) Section 9 & 10; [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md).

---

## 1. Executive Summary & Comparator Boundaries

`Kuberwastaken/riemann` is an open-science research archive and computational laboratory created by Kuber Mehta, containing an annotated bibliography of 178 primary sources on the Riemann Hypothesis alongside numerical and computer-assisted experiments on Weil quadratic form positivity under `experiments/weil_positivity/` and Lean 4 formalization under `formal/`.

### Key Findings:
1. **Finite-Dimensional Subspaces vs. Full-Space Theorems**:
   - In `FINDINGS.md` (commit `e5ea3e87`, July 24) and `UPDATES.md` (commit `0e90b56a`, August 11), Kuber Mehta explicitly records that his certified positive-definiteness results apply to **finite-dimensional test function families only** (14-dimensional subspaces at $L=0.45..0.60$, 22-dimensional subspace at $L=0.62$).
   - On August 11 (commits `27861654`, `9ab31fe3`), Kuber produced uncertified $\sigma$-LP pilot calculations at $L=0.40$ (+0.0046) and $L=0.42$ (+0.0320). These were explicitly treated as preliminary numerical experiments rather than certified theorems (`SHARP-FLOOR.md`: "pilot numerics are pilot numerics, certified results say certified, and none of it is RH").
   - Kuber's repository does **not** establish certified full-space $L^2([-T, T])$ theorems at any support $T > \frac{1}{2}\log 2$.
2. **Absence of Legendre Harmonic Coercivity**:
   - Kuber's mathematical framework relies on Fourier-sine series and Dirichlet band-mass estimates (Lemma H in `T1-GRADED.md`), not on Legendre polynomial expansions or Tuck's harmonic number identity ($J(P_n) = H_n \|P_n\|_2^2$).
3. **Independent Proof Architecture**:
   - Kuber's certification pipeline uses Python + Arb (`flint.arb`) interval ball arithmetic and certified Cholesky decomposition. It does not implement a zero-floating-point standalone rational verifier (`rh_cert`).
   - In Lean 4, Kuber formalizes `Lemma1.lean`, `SigmaLPAssembly.lean`, `T1Certificate.lean` (conditional on Parseval and ValidCaps), and `weil_positivity_of_RH` (via `Zeta23`), which are separate formal modules from `source/riemann-conjecture/formal/Cert/*.lean`.

---

## 2. Chronological Commit Evolution Table

The following table records every milestone development in `Kuberwastaken/riemann` with exact full commit SHAs, author/committer timestamps, affected file paths, mathematical status, and affected candidate IDs:

| Commit SHA | Author Timestamp (ISO-8601) | Committer Timestamp (ISO-8601) | File Path / Module | Milestone Description & Mathematical Status | Affected Candidate IDs | Evidence Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `2394a533b4211519b01ee7cd2264fe3ad301933c` | `2026-07-23T15:51:47+05:30` | `2026-07-23T15:51:47+05:30` | `README.md`, `CITATION.cff` | Repository scaffold and layout. Initial release date recorded as 2026-07-23. | `CLM-PRIO-001` | [`d1afa90f....md`](../phase1/kuber/objects/d1afa90ff7c6844175e75179dd74f3fb75395377.md) |
| `94de99514906d988ee420412e8853a7f06d2e6d2` | `2026-07-23T16:40:13+05:30` | `2026-07-23T16:40:13+05:30` | `experiments/weil_positivity/weil_form.py` | Implementation of $T_1$ numerical engine in sine basis, validated to $10^{-5}$ against Odlyzko zeta zeros. | `CLM-METH-001`, `CLM-VERF-001` | [`859b4a33....py`](../phase1/kuber/objects/859b4a332002d5f4ebab6803ca9337be063c22fb.py) |
| `2254645db72b530f03e00847ec84db233c53f12d` | `2026-07-23T16:47:24+05:30` | `2026-07-23T16:47:24+05:30` | `experiments/weil_positivity/RESULTS.md` | Empirical mapping of 4 regimes of Weil positivity ($L \in [0.20, 2.00]$). | `CLM-OPER-001` | [`36c86f59....md`](../phase1/kuber/objects/36c86f5923ec9ac015b034724f6398c9f5064ea9.md) |
| `af55413a4f8be1545e46b5ce1e84d02c889099ef` | `2026-07-23T17:21:17+05:30` | `2026-07-23T17:21:17+05:30` | `experiments/weil_positivity/T1-ARCHITECTURE.md` | Lemma 1 proved (1/2 dipole bound $\|g_f(a)\| \le \frac{1}{2}\|f\|^2$); spatial 2x2 architecture refuted; $\mu(L)$ invariant defined. | `CLM-OPER-002`, `CLM-OBST-001` | [`296a5993....md`](../phase1/kuber/objects/296a59932505d3ea232032a6725d1de0008862fd.md) |
| `d73801a36382be6b4b489e0f4f7a0067b90c65f6` | `2026-07-23T17:31:20+05:30` | `2026-07-23T17:31:20+05:30` | `experiments/weil_positivity/certify.py` | Introduction of Arb interval ball arithmetic (`flint.arb`) certification pipeline with certified Cholesky. | `CLM-VERF-001` | [`6f31b6e8....py`](../phase1/kuber/objects/6f31b6e8a4b7b12b47ad56c0efee2c3c3942b8f2.py) |
| `a51e3c350e6210bc492b76df5add970da9dff9ce` | `2026-07-23T17:33:12+05:30` | `2026-07-23T17:33:12+05:30` | `experiments/weil_positivity/certify_L045_output.txt` | First certified subspace result: $W \ge 0.072606 \|f\|^2$ on explicit 14-dim family at $L=0.45$ (prime 2 active). | `CLM-MATH-001..004` | [`3db55633....txt`](../phase1/kuber/objects/3db55633b58607a1ce271f928d8687ac424fb880.txt) |
| `a21f7a0176a63351a6be524cfa7c6991f8094abd` | `2026-07-23T17:41:09+05:30` | `2026-07-23T17:41:09+05:30` | `experiments/weil_positivity/certify_curve_output.txt` | Certified curve on 14-dim families: $W \ge 0.01484$ ($L=0.50$), $\ge 0.00129$ ($L=0.545$), $\ge 0.000076$ ($L=0.60, \{2,3\}$). | `CLM-MATH-005..008` | [`9c7e9270....txt`](../phase1/kuber/objects/9c7e9270d7e49c51684295bddb2fc95359823370.txt) |
| `b7be7346399e8790c07db45de4817d59ba424673` | `2026-07-23T17:47:11+05:30` | `2026-07-23T17:47:11+05:30` | `experiments/weil_positivity/rescue_certify_output.txt` | Arithmetic rescue machine-certified on 22-dim family at $L=0.62$: archimedean indefinite ($v^TGv = -0.02776$) but total $W \ge 2.06\times 10^{-5}$. | `CLM-MATH-008`, `CLM-OPER-001` | [`9e82fa42....txt`](../phase1/kuber/objects/9e82fa42d0bc19e9a2855484493d796b2d338d72.txt) |
| `e11bc5ce6be189498f58f8ff990a5dccec515ca1` | `2026-07-23T18:18:24+05:30` | `2026-07-23T18:18:24+05:30` | `experiments/weil_positivity/PROOF-c0.md` | Theorem A: explicit archimedean coercivity $c_0 \ge 0.349152$ on prime-free window ($L \le \frac{1}{2}\log 2$). | `CLM-METH-002`, `CLM-OBST-001` | [`4905c7d4....md`](../phase1/kuber/objects/4905c7d4ff2961c4badd3c1b0dfb650cbeda70fb.md) |
| `71c7076846f5ac5e37ed8ef013eea8b145afc5e1` | `2026-07-23T18:57:45+05:30` | `2026-07-23T18:57:45+05:30` | `experiments/weil_positivity/razor_certificate.txt` | Certified razor corridor: upper bound $\inf_{f \in V} W(f) \le 1.187\times 10^{-7}$ on $L=0.70$ window. | `CLM-MATH-008` | [`401a38e5....txt`](../phase1/kuber/objects/401a38e5b56eb58f86b599fe1371ec32324b68d7.txt) |
| `e5ea3e876f32fff244fcc2e51b900a27e87d9467` | `2026-07-24T02:49:07+05:30` | `2026-07-24T02:49:07+05:30` | `FINDINGS.md` | Ingestion of tiered honest ledger of results. Explicit statement: "None of it proves RH, and none of it is claimed to." | `CLM-PRIO-001..003` | [`ae9339ee....md`](../phase1/kuber/objects/ae9339ee293fa99efe1b78366d878c30dbbb8e16.md) |
| `16d6b6938c7a796a52e84afb5b9dc9f3e2683221` | `2026-08-11T10:33:02Z` | `2026-08-11T10:33:02Z` | `logs/LOG.md` | Session open: Ingestion and triage of Claude/Anthropic 2/3 critical-line theorem (`zeta-23-lean`). | `CLM-PRIO-001` | [`9c1fc0a5....md`](../phase1/kuber/objects/9c1fc0a5d211bd6b72034b86384c81dc5c3484dc.md) |
| `0e90b56a07e564061a95c6f91a8446e79de43410` | `2026-08-11T10:40:19Z` | `2026-08-11T10:40:19Z` | `UPDATES.md` | Dated adjudication layer: Notes that turning finite-dimensional results into full-space theorems requires certifying spectral caps (open). | `CLM-MATH-001..008`, `CLM-CONT-001` | [`47da3458....md`](../phase1/kuber/objects/47da34587f5106b004a6dd7889395671c8aff35f.md) |
| `c7c39a9ba9943976e8a178b0c2d05610862e54bb` | `2026-08-11T11:02:32Z` | `2026-08-11T11:02:32Z` | `experiments/weil_positivity/epsilonN_certify.py` | Implementation of $\varepsilon_N$ certification service for Connes-Consani-Moscovici (CCM 2025) Theorem 1.1 hypotheses. | `CLM-VERF-001` | [`cf54460d....py`](../phase1/kuber/objects/cf54460d9d60f449c9d9aaaec05c26d22e8105ed.py) |
| `35b28a8a716748480ee23717bdd398b6a3e8b29c` | `2026-08-11T11:13:16Z` | `2026-08-11T11:13:16Z` | `experiments/weil_positivity/EPSILON-N.md` | Rigorous Arb certification of sign, simplicity, and evenness of $\varepsilon_N$ across 5 windows ($L=0.45..0.62$) on Dirichlet sine sections. | `CLM-MATH-001..008`, `CLM-VERF-007` | [`390b25e4....md`](../phase1/kuber/objects/390b25e44ecdea3e564ebbc7b3ebca00e977aeec.md) |
| `6ac8bf987ddb3b474ab05f3a5e3abdf2af3262bb` | `2026-08-11T11:10:04Z` | `2026-08-11T11:10:04Z` | `experiments/weil_positivity/sigma_t1.py` | $\Omega_W$ identity: the 1-prime constrained Weil form is a diagonal multiplier $\Omega_W = \Omega - \sqrt{2}\log 2 \cos(r\log 2)$. | `CLM-METH-001`, `CLM-OPER-001` | [`635cb3bd....txt`](../phase1/kuber/objects/635cb3bdf62f8e4a854d051e1b9a8b5e83bdfb82.txt) |
| `2786165456621646b048f3b549519fb228879416` | `2026-08-11T11:18:34Z` | `2026-08-11T11:18:34Z` | `experiments/weil_positivity/SHARP-FLOOR.md` | Pilot numerical discovery: $\sigma$-LP crosses zero (+0.0046 at $L=0.40$, ratio 2.226). Uncertified pilot computation. | `CLM-MATH-001..002`, `CLM-CONT-001` | [`5e4b2a2a....py`](../phase1/kuber/objects/5e4b2a2a6d945d9a3170ceb60a4a72f20561ead8.py) |
| `401e98e141c6642b4a5c07922976226a4b1fd241` | `2026-08-11T11:28:38Z` | `2026-08-11T11:28:38Z` | `formal/lakefile.lean`, `formal/README.md` | Lean 4 package `RiemannFormal` scaffold, pinned to `v4.33.0-rc2` and Mathlib rev `51e6992`. | `CLM-VERF-007` | [`ff6e8721....md`](../phase1/kuber/objects/ff6e8721ba680e5233415d17d440cb0181d9b2c7.md) |
| `64d5ca0413740eb446324a6519c690e4c2fff676` | `2026-08-11T11:45:42Z` | `2026-08-11T11:45:42Z` | `formal/RiemannFormal/Lemma1.lean` | Lean 4 machine proof of Lemma 1 (half-factor prime bound $\|g_f(a)\| \le \frac{1}{2}\|f\|^2$), sorry-free. | `CLM-OPER-002`, `CLM-VERF-007` | [`74bf8b44....lean`](../phase1/kuber/objects/74bf8b44b62074b3142555b66422ac5f7925bfae.lean) |
| `7564d58cfdd056e4f7d4c025790c3af98e4283ec` | `2026-08-11T11:42:54Z` | `2026-08-11T11:42:54Z` | `formal/RiemannFormal/SigmaLPAssembly.lean` | Lean 4 machine proof of $\sigma$-LP dual assembly inequality, sorry-free. | `CLM-VERF-007` | [`1249d31c....lean`](../phase1/kuber/objects/1249d31c53e81746df7bea713618d2f21204f70e.lean) |
| `9e41beb4c4b434c629d71dc7659d6e9223da756f` | `2026-08-11T11:48:05Z` | `2026-08-11T11:48:05Z` | `formal/RiemannFormal/T1Certificate.lean` | Lean 4 theorem `T1_of_certificate`: conditional proof of full-space Weil positivity under Parseval and ValidCap hypotheses, sorry-free. | `CLM-METH-004`, `CLM-VERF-007` | [`f413089d....lean`](../phase1/kuber/objects/f413089d6a4e1b15881859102b6d03b320404cfb.lean) |
| `3f34c08ec31532cbd5f48057920d1f1676e72abe` | `2026-08-11T12:14:04Z` | `2026-08-11T12:14:04Z` | `formal/RiemannFormal/Criterion.lean` | Lean 4 theorem `weil_positivity_of_RH`: formal proof that RH implies arithmetic-side Weil positivity via `Zeta23.WeilEF.EF_lit`, sorry-free. | `CLM-VERF-007` | [`47aa7009....lean`](../phase1/kuber/objects/47aa70097604b71a1bafa236a3dd1af40e7ff87c.lean) |
| `9ab31fe3777baff196392346d37446df93e4cfd2` | `2026-08-11T13:39:01Z` | `2026-08-11T13:39:01Z` | `experiments/weil_positivity/SHARP-FLOOR.md` | Stage 7 $\sigma$-LP frontier: moves to $L=0.42$ (+0.0320, ratio 2.316); stalls at $L=0.45$ ($-0.0562$). Uncertified pilot computation. | `CLM-MATH-001..004`, `CLM-CONT-001` | [`2eda5b9a....txt`](../phase1/kuber/objects/2eda5b9a3e4aa7a8159efee4cf75470f5c2173e6.txt) |
| `3664ec9bf21735767f5a67e65130e0c31e02e201` | `2026-08-11T17:15:43Z` | `2026-08-11T17:15:43Z` | `BRIDGE.md` (v2) | Theorem S (strict window positivity under RH) and Theorem R (rigidity) proven. | `CLM-OPER-001`, `CLM-OBST-001` | [`a7d536af....md`](../phase1/kuber/objects/a7d536af882349888ffc636ba1a566712fc4f31a.md) |
| `50557c08e979fd4d3114677377924ee173ba6d82` | `2026-08-11T17:55:02Z` | `2026-08-11T17:55:02Z` | `CONTINUATION.md` | Continuation analysis in unconstrained pole-inclusive frame; first-failure zero-mode radical equation; Schur continuation theorem. | `CLM-METH-004`, `CLM-CONT-001`, `CLM-OBST-001` | [`cb068544....md`](../phase1/kuber/objects/cb06854452bb194366930fa9f9b6421c947afa1b.md) |
| `0d18760c99abb2d48a808f7252824a2f3ab93797` | `2026-08-11T18:14:03Z` | `2026-08-11T18:14:03Z` | `COLLISION.md` | Reconciliation of repository results against Suzuki (arXiv:2606.09096), CCM (arXiv:2511.22755), Bombieri (2000), Yoshida (1992). | `CLM-METH-001..004`, `CLM-OPER-001` | [`9b0f3952....md`](../phase1/kuber/objects/9b0f39522a5f8952eb72eb651895bdf86eecc280.md) |
| `4e82f27e9593c9a5c62ba7f9ce740cd79d37e27d` | `2026-08-11T18:17:42Z` | `2026-08-11T18:17:42Z` | `COLLISION.md` | Primary source audit of Yoshida 1992 Theorem 1 (positive definiteness on full prime-free class $K(\frac{1}{2}\log 2)$ via 200-mode error-bounded computation). | `CLM-METH-001`, `CLM-PRIO-004` | [`161518da....md`](../phase1/kuber/objects/161518da3fffb3ff474c630472e49effc8425ba9.md) |
| `94fa51e8f26794ef2d206c6c12e7adb4d85cbeaf` | `2026-08-11T20:32:35Z` | `2026-08-11T20:32:35Z` | `logs/LOG.md` | Terminal commit on `main` branch. Close of cycle 2. | `CLM-PRIO-001` | [`9fe9eedd....md`](../phase1/kuber/objects/9fe9eedd96ba0ff6bb11bb38c858457313b0810b.md) |

---

## 3. Mathematical Normalization & Comparison Matrix

| Mathematical Dimension | `Kuberwastaken/riemann` (Kuber Mehta) | `PerceivingAI/riemann-conjecture` (`51feb3d`) | Normalization & Comparative Finding |
| :--- | :--- | :--- | :--- |
| **Theorem Scope** | Finite-dimensional test function families (14D at $L=0.45..0.60$, 22D at $L=0.62$). Uncertified pilot LP numerics at $L=0.40, 0.42$. | Full-space $L^2([-T, T])$ unconditional certified theorems ($T=0.35..0.54$). | **Fundamental Scope Distinction**: Kuber explicitly notes in `UPDATES.md` that full-space infinite-dimensional theorems remained uncertified in his repository. |
| **High-Mode Tail Control** | Uncertified high-frequency spectral caps; Dirichlet band-mass estimates in Fourier-sine basis. | Rigorous **Legendre Harmonic Coercivity** $\mu_N = H_N - c_T - c_2 - \rho_R > 0$ derived from Tuck (1964). | **Distinct Mathematical Mechanism**: `riemann-conjecture` uses Tuck's Legendre eigenvalue identity to prove uniform positivity on all orthogonal complement modes $n > N$. |
| **Finite Reduction** | Direct Cholesky factorization on finite grid; unconstrained $\sigma$-LP cutting planes. | **3-Factor Component Tail-Gram Schur Criterion** $A_N - \frac{3}{\mu_N}(G_V + G_2 + G_R) > 0$. | `riemann-conjecture` reduces infinite-dimensional operator positivity to a finite-dimensional matrix inequality with verified rational witness. |
| **First-Prime Representation** | Discrete sum over prime evaluations / cosine multiplier $\sqrt{2}\log 2 \cos(r\log 2)$ in Fourier space. | **Thresholded Compressed Translation Operator** $P_2 = -\frac{\log 2}{\sqrt{2}} S_{T, \log 2}$ with exact norm $\|S_{T,a}\| = 2\cos\frac{\pi}{L+1}$. | Analytical physical-space operator formulation vs. Fourier-multiplier representation. |
| **Verification Engine** | Python 3 + Arb (`flint.arb`) interval ball arithmetic. | Standalone zero-floating-point Rust verifier (`rh_cert`, `BigRational` arithmetic). | Floating-point ball intervals vs. exact rational arithmetic verifier. |
| **Formal Soundness** | Lean 4 package `RiemannFormal`: Lemma 1, $\sigma$-LP assembly, conditional `T1_of_certificate`, `weil_positivity_of_RH` (via `Zeta23`). | Lean 4 package `Cert`: 36 proved lemmas across `Interval.lean`, `LDL.lean`, `Gershgorin.lean`, `EndpointAbsorption.lean`. | Distinct formalization scopes: Kuber formalizes the criterion bridge; `riemann-conjecture` formalizes arithmetic verifier soundness. |

---

## 4. Prior-Art Collision Lead Inspection

Kuber's `COLLISION.md` (commit `0d18760c`, `4e82f27e`) identifies four foundational external comparator references. As mandated by Section 10 of [`FOURTH_AUDIT.md`](../../FOURTH_AUDIT.md), these were independently inspected:

1. **Hiroyuki Yoshida (1992, Adv. Stud. Pure Math. 21, pp. 281–325)**:
   - *Title*: *On Hermitian forms attached to zeta functions*
   - *Finding*: Theorem 1 (p. 310) establishes that the pole-inclusive Weil quadratic form is positive definite on the prime-free window $K(\frac{1}{2}\log 2)$ ($L \le \frac{1}{2}\log 2 \approx 0.34657$) using a 200-mode Fourier computation with rigorous error bounds.
   - *Status*: Foundational prior art for prime-free compact Weil positivity.
2. **Enrico Bombieri (2000, Rend. Mat. Acc. Lincei 11, pp. 183–233)**:
   - *Title*: *Remarks on Weil's quadratic functional in the theory of prime numbers, I*
   - *Finding*: Theorem 12 establishes small-support coercivity with explicit constants; Theorem 3 establishes attainment of infimum on $L^2(E)$; Section 4 derives the Euler-Lagrange radical equation.
   - *Status*: Foundational mathematical prior art for variational and radical properties of the Weil functional.
3. **Alain Connes & Caterina Consani (2021, Selecta Math. 27, Paper No. 77; arXiv:2006.13771)**:
   - *Title*: *Weil positivity and trace formula, the archimedean place*
   - *Finding*: Proves positivity of the archimedean place via the semi-local trace formula, Sonin spaces, and prolate spheroidal wave functions.
   - *Status*: Conceptual prior art for archimedean-place positivity.
4. **Alain Connes, Caterina Consani, Henri Moscovici (2025, arXiv:2511.22755)**:
   - *Title*: *Zeta Spectral Triples*
   - *Finding*: Theorem 1.1 constructs self-adjoint operators from the restriction $QW_\lambda^N$ of the Weil form on $[e^{-L}, e^L]$ assuming the lowest eigenvalue $\varepsilon_N$ is simple and even.
   - *Status*: Operator-theoretic program connecting finite-section Weil positivity to zeta zeros.
