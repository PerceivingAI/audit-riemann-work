# Riemann Conjecture Project — Candidate Novelty, Priority, and Achievement Claims

## Purpose

This document inventories claims that the project may be entitled to make about its mathematical results, methods, computational verification, research process, novelty, or priority.

It is **not itself a novelty determination**. Claims involving words such as *first*, *new*, *novel*, *earliest*, *previously unknown*, or *strongest* require a separate comparison against the mathematical literature and other publicly disclosed work.

The entire project has been conducted publicly in the open-source repository:

`PerceivingAI/riemann-conjecture`

GitHub records the repository as **PUBLIC**, created on **2026-08-20T20:39:42Z**. The project therefore has a public Git history containing derivations, failed routes, corrections, theorem statements, source code, exact certificates, verifier outputs, formal proofs, and reproducibility records.

For priority purposes, individual public commits and their associated artifacts can be used as disclosure anchors, subject to a separate audit of exact public-push timing where necessary.

---

# I. Mathematical results the project presently claims

These are not hypothetical novelty claims. They are mathematical statements the repository currently records as `VERIFIED`.

## 1. Eight strict finite-support Weil-positivity theorems

The project claims strict positivity of Suzuki's scaled localized Weil quadratic form for every nonzero admissible localized test function at the following support/dimension pairs:

| Claim  | Support \(T\) | Dimension \(N\) |
| ------ | ------------: | --------------: |
| C-0050 |   7/20 = 0.35 |              32 |
| C-0051 |    2/5 = 0.40 |              40 |
| C-0052 | 17/40 = 0.425 |              48 |
| C-0053 |   9/20 = 0.45 |              56 |
| C-0054 | 19/40 = 0.475 |              68 |
| C-0055 |    1/2 = 0.50 |              80 |
| C-0056 | 21/40 = 0.525 |              96 |
| C-0057 |  27/50 = 0.54 |             104 |

The current independently verified finite-support frontier is therefore:

$$
(T,N)=(27/50,104).
$$

This is explicitly **not claimed to prove RH**.

### Possible novelty/priority questions

The later audit should determine whether the project can claim any of the following:

* first public proof of strict localized Weil positivity at any of these exact support values;
* first public proof beyond the traditional prime-free/restricted-support regime using this particular finite-support formulation;
* first public sequence of rigorously certified support-continuation theorems of this form;
* earliest public disclosure of a beyond-classical-support result among the 2026 work in this area.

The first theorem, `C-0050`, is present in public Git commit:

`6dd1d8f07e23dd39fcd2e36974c53a5054f810ec`

dated **2026-08-21T14:05:13Z**, containing the completed theorem, certificate, implementation, independent verification, and associated documentation.

That date should be an important anchor in the priority audit.

---

# II. Candidate novelty of the exact-prime Legendre-Schur method

This is probably the highest-priority methodological area for an external audit.

## 2. Exact-prime decomposition rather than uniform absorption

The project retains the exact first-prime compressed translation instead of absorbing it into a coarse global bound.

The method treats the localized Weil form as containing separately:

* the Legendre jump/coercive component;
* the exact \(p=2\) compressed translation;
* the finite-support Suzuki residual;
* the finite-dimensional low-mode block;
* the infinite-dimensional Legendre complement.

### Possible novelty claim

> A new exact-prime finite-support Weil-positivity method that preserves the first-prime translation geometry rather than replacing it by a global norm loss.

This should be compared against Bombieri, Connes–Consani, Suzuki, Chuk, and any 2026 computational Weil-positivity work.

---

## 3. Legendre harmonic-number coercivity for the infinite complement

`C-0045` establishes:

$$
J(P_n)=H_n\|P_n\|_2^2,
$$

and consequently

$$
J(q)\ge H_N\|q\|_2^2
$$

on the Legendre complement above mode \(N-1\).

The underlying Legendre integral identity has literature antecedents, but its use as the coercive infinite-tail mechanism in this Weil-positivity architecture is repository work.

### Possible novelty claim

> First use of Legendre harmonic-number coercivity as the analytic infinite-dimensional complement bound in a certified localized Weil-positivity proof.

Audit distinction:

* the identity itself may not be new;
* its application to this exact Weil operator may be.

Public method anchor:

`3111accb59df57d7976540bef29d38c817b80825`
2026-08-21.

---

## 4. Exact-prime high-mode complement estimate

`C-0047` derives a complement lower bound of the form

$$
\mu_N=H_N-c_T-c_2-\rho_R,
$$

with the residual controlled rigorously.

At the first theorem point, the project certified positive complement coercivity before reducing the remaining problem to finitely many modes.

### Possible novelty claim

> A rigorous analytic decomposition reducing full finite-support Weil positivity to a finite low-mode problem plus an explicitly certified Legendre high-mode complement.

This is stronger conceptually than merely checking a finite Galerkin matrix.

---

## 5. Component tail-Gram Schur criterion

`C-0048` derives the sufficient finite criterion

$$
A_N-\frac{3}{\mu_N}(G_V+G_2+G_R)>0,
$$

where each tail Gram is computed through

$$
G_X
=
P_NXQ_NXP_N
=
P_NX^2P_N-(P_NXP_N)^2.
$$

The factor \(3\) arises from controlling three component cross blocks.

### Possible novelty claim

> A componentwise tail-Gram Schur-complement reduction for certified infinite-dimensional localized Weil positivity.

The underlying Schur/Cauchy–Schwarz argument is elementary. The audit should therefore focus on whether this **particular decomposition and application** has appeared previously.

---

## 6. Combination of exact complement + tail Gram + rational congruence certificate

The project's proof architecture is not simply “compute an eigenvalue.”

It combines:

$$
\text{analytic complement coercivity}
\rightarrow
\text{finite exact Schur reduction}
\rightarrow
\text{outward rational intervals}
\rightarrow
\text{exact rational congruence}
\rightarrow
\text{Gershgorin positivity}.
$$

### Possible novelty claim

> A new certificate format for converting an infinite-dimensional Weil-positivity problem into an independently checkable exact-rational finite proof.

This is a particularly strong candidate for methodological novelty.

---

# III. Exact compressed-translation/operator claims

## 7. Weil prime powers as thresholded compressed translations

`C-0039` derives that a prime power \(m\) becomes active only when

$$
T>\frac12\log m,
$$

and represents its quadratic contribution as a compressed translation operator.

### Possible novelty claim

> An explicit compressed-translation operator representation making the prime-entry thresholds \(T=\tfrac12\log m\) transparent in the localized Weil form.

The mathematical ingredients may be implicit elsewhere. The audit should determine whether this exact operator formulation is already known.

Public anchor:

`fab5933fdcbdb69c4815e3296ace07b0df4cd277`
2026-08-21 UTC / late 2026-08-20 local time.

---

## 8. Exact norm formula for compressed symmetric shifts

`C-0040` gives, for

$$
S_{T,a}=P_T(U_a+U_a^*)P_T,
$$

the exact norm

$$
\|S_{T,a}\|
=
2\cos\frac{\pi}{L+1},
\qquad
L=\left\lceil\frac{2T}{a}\right\rceil.
$$

In the one-prime window this yields

$$
\|S_{T,\log 2}\|=1.
$$

### Possible novelty claim

> Exact finite-chain spectral formula for the compressed translation operator governing individual prime terms in localized Weil positivity.

The path-adjacency eigenvalue formula is standard. What requires auditing is whether its identification with this Weil compressed translation has appeared previously.

---

# IV. Continuation mechanism

## 9. Moving dimension restores one-prime support continuation

A fixed Legendre dimension eventually fails as support increases. The project found that increasing \(N\) restores rigorous positivity.

This produced the sequence:

$$
(0.35,32)
\rightarrow
(0.40,40)
\rightarrow
(0.425,48)
\rightarrow
(0.45,56)
\rightarrow
(0.475,68)
\rightarrow
(0.50,80)
\rightarrow
(0.525,96)
\rightarrow
(0.54,104).
$$

Public continuation anchor begins with:

`b5405a9347a8b6bc6d3a8c022c4e0fa60e425361`
2026-08-26.

### Possible novelty claims

* first systematic moving-dimension continuation of a rigorous localized Weil certificate;
* discovery that fixed \(N\) failure is not necessarily support failure;
* an adaptive finite-dimensional strategy for approaching the next prime threshold.

---

## 10. Rigorous rejection of deceptive finite/truncated positives

The project documented cases in which floating/truncated reconnaissance appeared positive but the rigorous full-tail theorem calculation was negative.

Examples:

* at \(T=21/40\), \(N=88\) and \(N=92\);
* at \(T=27/50\), \(N=100\).

### Possible methodological achievement

> Demonstration, on concrete Weil-positivity calculations, that truncated or floating finite sections can give false-positive continuation evidence, together with a rigorous workflow that detects and rejects those cases.

This may be significant as a cautionary result even if it is not a standalone mathematical theorem.

---

# V. Negative result: uniform endpoint absorption is too lossy

## 11. Valid 69% bound, invalid global proof strategy

The project rigorously proves at \(T=7/20\):

$$
V+P_2\ge \frac{69}{100}V\ge0.
$$

But it then proves that substituting this bound globally destroys enough geometry that the resulting lower operator is not positive.

An explicit polynomial counterexample is given by

$$
w=P_0-P_2=\frac32(1-x^2).
$$

### Possible novelty claim

> A rigorous demonstration that a natural uniform first-prime absorption strategy is intrinsically too lossy, motivating preservation of exact prime geometry.

This is useful negative knowledge and may distinguish the project's method from simpler perturbative approaches.

---

# VI. Digamma/residual structural work

## 12. Positive-kernel decomposition of the digamma multiplier

`C-0043` derives a decomposition of the real digamma multiplier into monotone positive quadratic-form contributions involving exponential kernels.

### Possible novelty claim

> A positive-kernel decomposition useful for lower-bounding the archimedean component of the finite-support Weil operator.

The underlying digamma series and Fourier transform are standard. The novelty question is whether this exact positivity formulation/application is new.

---

## 13. Explicit residual-kernel correctness guard

The project identified that a naive multiplier-plus-prime finite matrix omits Suzuki's finite-support residual term.

That exploratory route was discarded before theorem registration.

### Achievement claim

> The project identified and corrected a structurally incomplete finite-support Weil discretization before promoting it to a theorem.

This is primarily a methodological/reproducibility achievement rather than a novelty theorem.

---

# VII. Li/Laguerre prime-side results

These constitute a substantial independent research thread and should receive their own literature audit.

## 14. Exact generalized prime-Laguerre component

`C-0006` derives the exact Euler-product contribution

$$
-A\sum_{m\ge2}\Lambda(m)m^{-s_0}
L_{n-1}^{(1)}(A\log m).
$$

### Possible novelty question

Whether this exact form is already explicit in Sekatskii or related generalized-Li literature, or whether the project's normalization/derivation adds something new.

---

## 15. Exact deterministic zeta-pole mode in the raw prime trace

`C-0009` identifies the exact pole contribution

$$
1-q^n,
\qquad
q=-\frac{s_0}{s_0-1}.
$$

This proves that the raw generalized prime-Laguerre trace is exponentially large even on RH.

### Possible novelty claim

> Explicit isolation of the deterministic zeta-pole exponential mode in the generalized prime-Laguerre sequence.

This is a high-value audit candidate because it changes how a naive prime-side Li strategy must be formulated.

---

## 16. Pole-subtracted prime-Laguerre root criterion

`C-0010` claims

$$
RH
\iff
\limsup |S_n|^{1/n}\le1
$$

after exact pole subtraction.

### Possible novelty claim

> A prime-Laguerre root-growth criterion for RH obtained by exact removal of the zeta pole.

Audit carefully against generalized Li criteria and prior generating-function work.

---

## 17. Exact \(d(\psi-x)\) discrepancy representation

`C-0011` rewrites the pole-subtracted sequence exactly as an integral against

$$
d(\psi(x)-x).
$$

### Possible novelty claim

> Exact transformation of the generalized Li prime-Laguerre sequence into a weighted prime-number-theorem discrepancy integral.

This provides the bridge from Li coefficients to analytic prime-discrepancy techniques.

---

## 18. Exact pole-annihilating shift filter

`C-0012` constructs

$$
T=(E-1)(E-q)
$$

which annihilates the deterministic pole modes while preserving the nontrivial-zero information.

Public anchor for this cluster:

`cc57e7037a407bfadac6c62c744d72dedf3e96a1`
2026-08-20.

### Possible novelty claim

> A finite-difference/shift filter that exactly removes the zeta-pole modes from the generalized prime-Laguerre sequence while preserving an RH-equivalent root criterion.

This should be specifically searched in the Li-coefficient literature.

---

# VIII. Airy/stationary-phase interpretation of the Li/Laguerre kernel

## 19. Smooth-density Airy saddle reproduces the pole exponential rate

`C-0014` derives an Airy-envelope saddle whose rate is exactly

$$
\left(\frac{s_0}{s_0-1}\right)^n.
$$

### Possible novelty claim

> Asymptotic identification of the zeta pole's exact Cayley growth rate directly from the Laguerre Airy saddle.

This is an interpretation/result worth auditing separately.

---

## 20. Generalized-center signal/prime-scale tradeoff

The project derives a quantitative relationship between off-critical Cayley amplification and the exponentially large prime scale being sampled.

### Possible novelty claim

> A quantitative asymptotic tradeoff showing that moving the generalized Li center weakens both off-line amplification and the prime scale in a precisely coupled manner.

---

## 21. Exact phase-aware single-zero transform

`C-0019` gives a nontrivial zero \(\rho\) the exact contribution

$$
z_\rho^{-n}-1.
$$

### Possible novelty claim

> Exact matching between individual explicit-formula zero modes and generalized Laguerre/Cayley modes.

This may overlap known generating-function identities; external audit required.

---

## 22. Uniform stationary-frequency map

`C-0021` derives

$$
u_\gamma=\frac{A^2}{A^2+4\gamma^2},
\qquad
\gamma(u)=\frac A2\sqrt{\frac{1-u}{u}},
$$

with the corresponding prime scale.

### Possible novelty claim

> A uniform map between zero height/Mellin frequency, Laguerre stationary coordinate, and prime scale.

Public anchor:

`64e884b89c1120161b7f67b505e7dd3c5e688286`
2026-08-20.

---

## 23. Critical stationary saddle reproduces the Cayley mode

`C-0022` shows that the stationary phase has exactly the Cayley-mode phase and leading unit normalization.

### Possible novelty claim

> A stationary-phase explanation for why critical-line zeros generate unit-modulus Cayley modes in the generalized Li sequence.

This looks particularly interesting conceptually.

---

## 24. Critical-half-weight nonlinear Laguerre chirp

`C-0023` identifies the local prime-side kernel as a nonlinear Mellin/Fourier chirp acting on

$$
e^{-y/2}\,d(\psi(e^y)-e^y).
$$

### Possible novelty claim

> Identification of the generalized Li prime kernel as a nonlinear critical-half-weight Mellin chirp.

This should be a dedicated literature-search phrase.

---

## 25. Microlocal critical-half-weight Dirichlet reduction

The project locally linearizes the chirp and obtains smooth Dirichlet-polynomial / prime-discrepancy cells near the critical half-weight.

### Possible novelty claim

> Microlocal reduction of the generalized Li/Laguerre kernel to short smooth critical-half-weight prime sums.

---

# IX. Barrier and obstruction results

These may be publishable/useful even though they describe why certain routes fail.

## 26. Absolute pointwise PNT-error bounds cannot close the Laguerre criterion unless they are RH-strength

`C-0016` demonstrates that inserting a bound

$$
|\psi(x)-x|=O(x^\theta),
\qquad \theta>1/2,
$$

absolutely into the transformed criterion leaves exponential growth.

### Possible novelty claim

> An explicit asymptotic obstruction showing that conventional pointwise prime-error estimates cannot prove the generalized Laguerre root criterion through absolute estimation.

---

## 27. Regionwise unconditional PNT bounds remain exponentially insufficient

`C-0018` shows that current Vinogradov–Korobov-scale improvements are only \(e^{-o(n)}\) on the relevant moving exponential prime scales and cannot eliminate a positive root base.

### Possible novelty claim

> Quantitative obstruction to using current unconditional PNT-error technology directly in this Laguerre/Airy route.

---

## 28. Coefficient-block \(L^2\) reformulation is itself RH-equivalent

`C-0024` proves that the block norm

$$
M_N=\sum_{n=N}^{2N}|S_n|^2
$$

has the required subexponential root behavior if and only if RH holds.

### Possible novelty claim

> A simple block-\(L^2\) RH-equivalent formulation demonstrating that a naive Parseval or square-summability reformulation does not weaken the problem.

Compare carefully with Arias de Reyna and other Keiper–Li \(\ell^2\) criteria.

---

## 29. High-frequency stationary saddles merge into the endpoint

`C-0025` characterizes the breakdown of fixed-interior stationary phase as zero height approaches the \(n\)-scale.

### Possible novelty claim

> Precise high-frequency/left-endpoint transition for the generalized Laguerre stationary saddle.

---

## 30. Prime-side Mellin frequency cap

`C-0027` observes that because prime atoms begin at \(m=2\), the actual prime-side Mellin frequencies sampled satisfy only

$$
\gamma_{\max}(n)=O(\sqrt n).
$$

### Possible novelty claim

> A natural \(\sqrt n\)-frequency cap imposed by the first prime in the Laguerre chirp formulation.

---

## 31. Montgomery–Vaughan exponential-length barrier

The project shows that the standard mean-value length term for the resulting exponentially long Dirichlet polynomials is itself exponentially too large.

### Possible novelty claim

> A quantitative large-sieve/Dirichlet-polynomial obstruction for the generalized Li chirp route.

---

## 32. Microlocal subexponential control is already zero-sensitive

The project argues that sufficiently uniform subexponential control of matched prime cells would itself exclude off-line zeros in the corresponding frequency band.

### Possible novelty claim

> Demonstration that the apparently local analytic estimate sought by the chirp strategy is already carrying zero-free/RH-strength information.

---

# X. Bilinear/Vaughan/Heath-Brown obstruction

## 33. Finite multiplicative convolutions preserve rank-one phase geometry

`C-0031` derives

$$
\operatorname{Hess}
\Phi_n(r_1+\cdots+r_k)
=
\Phi_n''\,\mathbf1\mathbf1^T,
$$

so the Hessian has rank at most one.

### Possible novelty claim

> Finite multiplicative convolution decompositions do not create new oscillatory dimensions for the generalized Laguerre chirp.

Public anchor:

`1752f19dec983427e50eeee6cb3938a62f842d4e`
2026-08-21 UTC / late Aug. 20 local time.

---

## 34. Standard dyadic Type-II chirp is asymptotically separable

`C-0032` obtains a four-corner phase defect of only \(O(1/n)\).

### Possible novelty claim

> Standard Type-II bilinear boxes become asymptotically separable for this Laguerre product-phase kernel.

---

## 35. Nonseparability begins only at logarithmic widths of order \(\sqrt n\)

`C-0033` identifies the scale at which genuinely two-variable phase curvature becomes order one.

### Possible novelty claim

> Explicit nonseparability threshold for bilinear decompositions of the Laguerre chirp.

---

## 36. Direct fixed-interior prime estimates need square-root saving

The project derives that direct magnitude estimates need essentially \(\delta\ge1/2\) saving.

### Possible novelty claim

> A sharp exponent bookkeeping obstruction explaining why ordinary prime exponential-sum savings do not reach the RH root target in this formulation.

---

## 37. Generic Vaughan/Heath-Brown phase route is blocked

Combining the preceding results, the project closes the proposed strategy based only on finite divisor decomposition plus generic Type-I/II phase cancellation.

### Possible novelty claim

> A structural no-go result for the straightforward Vaughan/Heath-Brown phase strategy applied to the generalized Laguerre RH criterion.

The wording must remain limited: the repository explicitly does **not** claim every specialized arithmetic use of these decompositions is impossible.

---

# XI. Li Gram / harmonic-analysis reformulations

## 38. Exact Li Gram kernel equivalence

`C-0036` constructs

$$
K^{(N)}_{jk}
=
\lambda_j+\lambda_k-\lambda_{|j-k|}
$$

and proves PSD for every \(N\) is equivalent to RH.

### Possible novelty claim

> An explicit finite Gram-matrix hierarchy equivalent to Li positivity/RH.

This could easily have prior analogues and deserves careful literature comparison.

---

## 39. Li coefficients as a conditionally negative definite function on \(\mathbb Z\)

`C-0037` claims that under RH

$$
\psi(n)=\lambda_{|n|}
$$

is conditionally negative definite, yielding the Schoenberg family

$$
e^{-t\lambda_{|n|}}
$$

of positive-definite Fourier sequences / convolution-semigroup measures.

The converse recovers Li positivity.

### Possible novelty claim

> Schoenberg–Herglotz characterization of RH through conditional negative definiteness of the Li sequence.

This is a strong independent novelty-audit candidate.

---

## 40. Natural generalized prime Gram atoms are not PSD

`C-0038` shows individual prime-power contributions have a negative first diagonal and therefore cannot themselves be positive Gram pieces in the obvious generalized-Li basis.

### Possible novelty claim

> Obstruction to decomposing the generalized Li Gram kernel into independently positive prime-power atoms.

---

# XII. Exact finite-support theorem verification architecture

## 41. Exact rational theorem certificates

The project converts rigorous Arb interval calculations into exact rational/dyadic certificate data.

The independent verifier does **not** trust floating-point eigenvalues.

### Possible novelty claim

> Machine-checkable exact rational certificates for finite-support Weil positivity.

---

## 42. Independent zero-floating-point Rust replay

`rh_cert` independently reconstructs:

* the admitted theorem identity;
* complement lower bound;
* exact factor-3 Schur matrix;
* congruence witnesses;
* exact interval Gershgorin margins.

### Possible novelty claim

> First independent zero-floating-point verifier for computational localized Weil-positivity theorems.

This should be audited against other certified-numerics work.

---

## 43. Independent admission authority across multiple trust layers

The production admissible theorem pairs are independently encoded in:

* Python certificate generation;
* Python semantic validation;
* raw JSON Schema;
* Rust verification.

A shared file is deliberately **not** used as production authority.

### Possible methodological novelty

> Multi-implementation closed theorem admission designed to prevent a single shared whitelist bug from manufacturing a theorem.

This is more software-assurance novelty than mathematical novelty.

---

## 44. Explicit pre-theorem boundary

The continuation driver is forbidden from promoting a numerical candidate into theorem status.

The workflow distinguishes:

$$
\text{candidate discovery}
\neq
\text{admission}
\neq
\text{fresh proof generation}
\neq
\text{independent verification}
\neq
\text{registration}.
$$

### Possible achievement claim

> A proof-oriented computational research workflow with an explicit non-automatic theorem-promotion boundary.

---

## 45. Contract failure distinguished from theorem failure

Real certificate attacks deliberately establish that:

* malformed theorem inputs fail the **contract**;
* a structurally valid but mathematically false certificate reaches theorem verification and fails **mathematically**.

For `C-0057`, for example:

* wrong factor/mixed pairs/malformed interval/provenance/structure → exit `2`;
* exact negative diagonal perturbation → exit `1`, `passed=false`;
* unchanged certificate → exit `0`, `passed=true`.

### Possible novelty claim

> Adversarial theorem-certificate verification that explicitly separates malformed-proof rejection from genuine mathematical counterexample failure.

---

## 46. Retained proof chain with hash identities

The repository retains eight exact theorem certificates by path, claim identity and SHA-256.

Current result:

`RETAINED PROOF CHAIN: PASS - 8/8`

### Possible achievement claim

> Publicly replayable historical theorem chain in which old proof artifacts are continuously checked against the current independent verifier.

---

## 47. Lean formalization of verifier soundness components

The Lean layer formalizes finite-dimensional soundness ingredients including interval reasoning, endpoint absorption, LDL/Gershgorin and invertible-congruence transfer.

The repository-wide `lake build` passes.

### Possible novelty claim

> Hybrid proof architecture combining certified numerical generation, an independent exact verifier, and formal proof of the verifier's mathematical soundness lemmas.

The external audit should determine whether an equivalent architecture has previously been used for Weil positivity.

---

# XIII. Research-integrity / public-science achievements

## 48. Entire research process conducted in public

The GitHub repository is recorded as:

* visibility: `PUBLIC`;
* creation: `2026-08-20T20:39:42Z`.

The research record includes successful and failed routes, not just final cleaned-up results.

### Claimable achievement

> The project is an open-source, publicly inspectable computational mathematics research program whose derivations, failures, corrections, certificates and proof machinery have been developed in public.

---

## 49. Public negative-result record

The repository preserves routes that were shown insufficient:

* raw prime-Laguerre sequence contaminated by the zeta pole;
* absolute PNT bounds too weak;
* block-\(L^2\) reformulation still RH-equivalent;
* generic Vaughan/Heath-Brown phase route blocked;
* global 69% first-prime absorption too lossy;
* floating finite sections can misidentify positive dimensions.

### Possible achievement claim

> A publicly documented map of several plausible RH approaches showing precisely where each becomes equivalent to RH, loses necessary geometry, or requires unavailable cancellation.

This may itself be useful research output.

---

## 50. Public correction trail

The project retains corrections rather than silently rewriting history—for example the factor-of-two correction in the critical-line zero contribution and discarded incomplete finite-support discretizations.

### Possible achievement claim

> Auditable scientific history in which incorrect intermediate assumptions and failed approaches remain visible alongside their corrections.

---

# XIV. Strongest possible priority claims to investigate

The external audit should explicitly test the following formulations rather than vaguely asking whether “the project is novel”:

1. **Earliest public exact-prime Legendre-Schur proof of strict localized Weil positivity beyond the prime-free regime.**

2. **Earliest public finite-support Weil-positivity theorem at \(T=7/20\)** or an equivalent normalization.

3. **Earliest public sequence of independently certified localized Weil positivity results extending through \(T=27/50\).**

4. **First use of Legendre harmonic coercivity plus component tail-Gram Schur reduction for the full Suzuki finite-support Weil operator.**

5. **First exact-prime method that retains the compressed \(p=2\) translation and the finite-support residual rather than globally absorbing/truncating them.**

6. **First exact-rational independently replayable certificate format for localized Weil positivity.**

7. **First zero-floating-point independent verifier for such certificates.**

8. **First hybrid Arb → rational certificate → Rust verifier → Lean soundness architecture for Weil positivity.**

9. **First explicit moving-dimension continuation strategy for rigorous Weil positivity.**

10. **First public demonstration, in this setting, that truncated/floating finite sections can give false-positive support-continuation evidence.**

11. **First exact pole-annihilating shift filter for generalized prime-Laguerre Li sequences.**

12. **First prime-Laguerre RH root criterion formulated after exact zeta-pole subtraction.**

13. **First stationary-phase derivation explicitly reproducing the Cayley zero mode from the generalized Laguerre kernel.**

14. **First interpretation of the generalized Li prime kernel as a critical-half-weight nonlinear Mellin chirp.**

15. **First rank-one-Hessian/separability obstruction for Vaughan/Heath-Brown decompositions of that chirp.**

16. **First conditional-negative-definite/Schoenberg characterization of RH directly from the Li coefficient sequence.**

17. **First compressed-translation operator treatment making Weil prime-entry thresholds and the exact shift norm explicit in this form.**

18. **First openly developed research program to combine all of these theorem, certificate, adversarial, retained-proof and formal-verification layers in a single public RH project.**

Every one of these should be treated as a **question for audit**, not yet as a publication-ready priority assertion.

---

# XV. Public priority anchors already available in the repository

Important Git anchors for the later audit include:

| Research cluster                                            | Public Git anchor                                         | Commit time   |
| ----------------------------------------------------------- | --------------------------------------------------------- | ------------- |
| Pole-subtracted Li/Laguerre criterion and shift-filter work | `cc57e7037a407bfadac6c62c744d72dedf3e96a1`                | 2026-08-20    |
| Stationary-map / nonlinear chirp work                       | `64e884b89c1120161b7f67b505e7dd3c5e688286`                | 2026-08-20    |
| Bilinear/Vaughan obstruction                                | `1752f19dec983427e50eeee6cb3938a62f842d4e`                | 2026-08-20/21 |
| Li Gram / compressed-translation operator work              | `fab5933fdcbdb69c4815e3296ace07b0df4cd277`                | 2026-08-21    |
| Legendre coercivity / component Schur method                | `3111accb59df57d7976540bef29d38c817b80825`                | 2026-08-21    |
| First completed exact-prime theorem C-0050                  | `6dd1d8f07e23dd39fcd2e36974c53a5054f810ec`                | 2026-08-21    |
| Moving-dimension continuation                               | `b5405a9347a8b6bc6d3a8c022c4e0fa60e425361` and successors | 2026-08-26    |
| C-0057 full proof-bearing closure                           | `51feb3d176e4a53773c22dc157567cc0486f4c71`                | 2026-09-24    |

The repository itself was public from its creation on **2026-08-20**.

For a formal priority audit, each candidate claim should be tied to the earliest commit containing enough information for an independent reader to understand or reproduce that claim, rather than simply using the later polished theorem record.

---

# XVI. Claims the project should NOT make

The audit should also preserve strict negative boundaries.

The project should not presently claim:

* a proof of RH;
* positivity for arbitrary support;
* positivity past the \(p=3\) structural threshold;
* a world-record support bound without comparison to contemporary 2026 work;
* that every repository-derived identity is novel;
* that standard ingredients such as Schur complements, Gershgorin, Legendre identities, path-graph eigenvalues, Arb interval arithmetic or Schoenberg theory were invented here;
* that a Git commit date alone automatically proves legal/academic priority over every external source;
* that the one-prime method automatically extends unchanged once \(p=3\) enters;
* that computational scout positivity constitutes a theorem;
* that the eight finite-support theorems imply RH.

The strongest defensible statement before the external audit is:

> **The public repository contains a substantial body of independently derived mathematical results, eight rigorously retained finite-support Weil-positivity theorems, several structural and obstruction results, and a distinctive exact-certificate verification architecture. A number of these results and methods are plausible novelty or priority candidates and warrant a dedicated comparison against the prior and contemporary literature.**

# Recommended audit structure

For the separate audit, I would investigate the candidates in this order:

**Tier A — highest significance:** C-0050 and its Aug. 21 public disclosure; Legendre harmonic coercivity applied to Weil positivity; component tail-Gram Schur reduction; exact-prime certificate architecture; moving-dimension continuation.

**Tier B — potentially independent mathematical novelty:** pole-subtracted Laguerre root criterion; exact pole-annihilating filter; critical-half-weight chirp/stationary-map interpretation; rank-one convolution/Vaughan obstruction; Li conditional-negative-definite formulation.

**Tier C — methodological/software novelty:** zero-float Rust verifier; independent theorem admission layers; adversarial contract-vs-theorem failure; retained 8/8 certificate replay; Lean-backed verifier soundness.

**Tier D — useful but likely combinations of known ingredients:** compressed-shift norm formula, positive digamma-kernel decomposition, endpoint absorption estimates, individual numerical support points once a stronger continuous support theorem is already known elsewhere.

The audit should search both **pre-2026 literature** and **contemporaneous 2026 public disclosures**, and it should compare actual public dates rather than publication dates alone.
