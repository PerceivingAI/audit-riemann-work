# Audit Pass 2 — Adversarial Re-Audit of `riemann-conjecture`

You are conducting **Audit Pass 2** of the public research project:

`https://github.com/PerceivingAI/riemann-conjecture`

The audit repository itself is also public and contains the complete first audit pass.

## Core principle

**Do not assume Audit Pass 1 is correct.**

Pass 1 is a historical audit artifact. Preserve it exactly as part of the public audit trail, but treat every conclusion in it as a hypothesis that may need to be confirmed, narrowed, downgraded, or rejected.

Your task is to **audit the first audit**, not defend it.

The objective is to move toward the most accurate scientific assessment possible, even when that weakens claims made in Pass 1.

---

# 1. Repository and historical boundaries

The target research repository is:

`https://github.com/PerceivingAI/riemann-conjecture`

The audited closed-state research commit is:

`51feb3d176e4a53773c22dc157567cc0486f4c71`

The current Audit Pass 1 public head is:

`20b3f9d — FINAL_AUDIT.md - Document Complete - First Audit Complete`

Treat that commit and its contents as an immutable historical record of the first audit.

Do **not** rewrite Pass 1 to make it retrospectively correct.

Corrections belong in new Pass 2 artifacts.

The source research snapshot under:

`source/riemann-conjecture/`

must remain read-only.

Do not modify the source project's history, certificates, findings, claims, computations, or theorem records.

---

# 2. Audit stance

Your stance must be:

**Adversarial, independent, skeptical, evidence-driven, and correction-seeking.**

For every important Pass 1 conclusion, ask:

> What evidence would prove this conclusion wrong?

Actively search for that evidence.

Finding prior art, an earlier disclosure, an equivalent formulation, a stronger result, a methodological predecessor, a normalization error, or an unsupported timeline assumption is a **successful audit outcome**, not a failure.

Likewise, do not downgrade a claim merely because Pass 1 was overconfident. If a claim survives stronger scrutiny, record that clearly.

---

# 3. Pass 1 must not be treated as authority

The following Pass 1 outputs are evidence about what the first auditor concluded, but are **not authoritative conclusions**:

* `FINAL_AUDIT.md`
* `reports/FINAL_AUDIT.md`
* Pass 1 claim dossiers
* Pass 1 literature baseline
* Pass 1 timeline matrix
* Pass 1 novelty verdicts
* Pass 1 priority verdicts

You may cite them when explaining what is being re-examined, but never use a Pass 1 conclusion as evidence that the underlying scientific claim is true.

Return to primary sources.

---

# 4. Known Pass 1 problems that must be investigated

Audit Pass 2 begins with several known adverse findings. Verify them independently rather than accepting them blindly.

### Claim accounting

`CLAIMS_TO_AUDIT.md` contains **66 unique claim IDs**, not 50.

Recount them programmatically and establish the authoritative claim inventory.

Every one of the 66 claims must receive an explicit Pass 2 disposition.

Do not summarize 66 claims as 50.

### Audit timestamps

Pass 1 contains timestamps such as:

`2026-09-24T00:00:00Z`

that appear to predate creation of the audited closed-state commit and/or the audit repository itself.

Reconstruct the actual audit chronology from Git history.

Distinguish clearly between:

* document metadata placeholders;
* Git author time;
* Git committer time;
* actual audit-repository commit time;
* public-push evidence.

Do not silently edit historical Pass 1 timestamps.

Document the discrepancy in Pass 2.

### Incomplete claim dossiers

Pass 1 appears not to contain an individual dossier for every claim despite stating that all candidate claims were evaluated.

Determine exactly:

* how many Pass 1 dossiers exist;
* which claims had individual dossiers;
* which were only covered by aggregate reports;
* which lacked a documented evidentiary adjudication.

Pass 2 should fill those gaps.

### Literature-search coverage

Pass 1's stated audit protocol required stronger adversarial search coverage than the recorded search logs appear to demonstrate.

Re-evaluate whether the search protocol was actually satisfied.

Do not infer “comprehensive search” from a small number of broad search documents.

---

# 5. Expand the prior-art search beyond papers

Pass 2 must search **public research repositories as well as papers and preprints**.

This is mandatory.

Relevant evidence can include:

* arXiv;
* journal literature;
* conference proceedings;
* MathSciNet;
* zbMATH;
* Google Scholar;
* Semantic Scholar;
* Crossref;
* author websites;
* GitHub;
* GitLab;
* public research notebooks;
* Zenodo;
* OSF;
* Software Heritage;
* Internet Archive;
* GH Archive;
* forks and mirrors;
* mailing lists;
* public issue discussions;
* preprint servers;
* institutional repositories.

A result does not cease to be relevant prior art merely because it was not formatted as a conventional paper.

---

# 6. Mandatory contemporary comparator: `Kuberwastaken/riemann`

Pass 2 must investigate the public repository:

`https://github.com/Kuberwastaken/riemann`

This source was missed in Pass 1.

Determine carefully:

* its creation/publication timeline;
* earliest relevant commits;
* what mathematical statements it actually proves;
* whether its results are finite-dimensional, full-space, conditional, numerical, or rigorous;
* its support normalization;
* its prime-entry/operator formulation;
* its use of Arb or interval arithmetic;
* its continuation strategy;
* whether any of its methods overlap with:

  * compressed prime translations;
  * support thresholds;
  * Legendre bases;
  * exact-prime treatment;
  * moving-dimension continuation;
  * finite-section positivity;
  * rigorous tail control.

Do **not** assume this repository invalidates the `riemann-conjecture` project's claims.

Normalize the mathematics first.

It may turn out to address a substantially different finite-dimensional family rather than the full-space theorem proved by `C-0050`.

The objective is accurate comparison.

---

# 7. Mandatory contemporary comparator: Marcus Chuk

Re-audit:

Marcus Chuk
arXiv:2608.24827
*Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law*

Use the actual paper, not summaries.

Establish precisely:

* arXiv submission time;
* version history;
* theorem statement;
* support normalization;
* whether the theorem is full-space or finite-dimensional;
* certification method;
* use of Legendre expansions;
* numerical precision;
* quadrature-error certification;
* Cholesky/residual certification;
* tail estimates;
* interval arithmetic;
* exact vs non-exact arithmetic distinctions.

Do not describe Chuk merely as a “floating-point matrix discretization” if the actual proof includes rigorous certified interval/error bounds.

Compare architectures accurately:

**different certified proof architecture** is acceptable wording if supported.

---

# 8. Separate four different notions of novelty

Every claim must be classified independently under these dimensions:

### A. Mathematical-result novelty

Example:

> Was strict localized Weil positivity at this support value itself previously established?

### B. Method novelty

Example:

> Was this exact-prime Legendre harmonic coercivity + tail-Gram Schur reduction previously used?

### C. Verification/software novelty

Example:

> Was a zero-floating-point standalone exact-rational verifier/certificate architecture previously used for this problem?

### D. Chronological priority

Example:

> Was this particular result or method publicly disclosed before comparable work?

Do not infer one from another.

A mathematical result may already be known while the method remains novel.

A method may be independently new even when another method proves a stronger theorem.

A Git date may establish chronology without establishing mathematical novelty.

---

# 9. Re-audit all eight theorem claims individually

Re-evaluate:

* `C-0050` — `T=7/20`, `N=32`
* `C-0051` — `T=2/5`, `N=40`
* `C-0052` — `T=17/40`, `N=48`
* `C-0053` — `T=9/20`, `N=56`
* `C-0054` — `T=19/40`, `N=68`
* `C-0055` — `T=1/2`, `N=80`
* `C-0056` — `T=21/40`, `N=96`
* `C-0057` — `T=27/50`, `N=104`

Distinguish:

**Validity** from **novelty**.

The eight retained theorem certificates may remain mathematically valid even if their novelty status changes.

Important chronological issue:

Chuk's August 25 theorem reportedly establishes positivity throughout a larger support window.

Therefore, later `C-0051..C-0057` points may be:

* independently certified results;
* important demonstrations of the exact-prime method;
* continuation evidence;

without necessarily being novel mathematical support theorems after August 25.

Determine this carefully rather than inheriting Pass 1's blanket `8/8 novelty supported` conclusion.

---

# 10. Give special attention to `C-0050`

`C-0050` is particularly important because its source commit is dated:

`6dd1d8f07e23dd39fcd2e36974c53a5054f810ec`

`2026-08-21T14:05:13Z`

This predates Chuk's August 25 arXiv submission at the Git-commit metadata level.

Pass 2 must determine whether there is independent evidence that the commit was actually publicly accessible on August 21.

Search for:

* GitHub PushEvent data;
* GH Archive;
* Software Heritage;
* Wayback Machine;
* GitHub forks;
* public mirrors;
* external clones;
* GitHub notifications;
* commit links in public communication;
* public GitHub API/event archives;
* third-party indexing;
* repository snapshots.

Do not automatically equate:

`Git commit timestamp`

with:

`verified public disclosure timestamp`.

A Git commit object is cryptographically hash-addressed, but its embedded timestamps are author-controlled metadata.

If public availability on August 21 cannot be independently demonstrated, use the audit's weaker priority category rather than overstating certainty.

If it **can** be demonstrated, record the evidence precisely.

---

# 11. Re-audit the exact-prime Legendre-Schur method

The strongest method candidate is the synthesis involving:

$$
J(q)\ge H_N\|q\|_2^2
$$

plus the exact prime/residual decomposition and component tail-Gram Schur estimate

$$
A_N-\frac{3}{\mu_N}(G_V+G_2+G_R)>0.
$$

Investigate separately:

* Legendre harmonic-number eigenvalue identity;
* use of that identity as a Weil high-mode coercivity estimate;
* exact-prime compressed translation treatment;
* residual-kernel handling;
* componentwise tail Gram construction;
* factor-3 Schur estimate;
* outward rationalization;
* exact congruence/Gershgorin certificate;
* adaptive/moving-dimension continuation.

For each component answer:

1. Is the ingredient known?
2. Is the application known?
3. Is the combination known?
4. Is the implementation/certificate architecture known?
5. What is the earliest public evidence?

Do not call standard ingredients novel.

---

# 12. Re-audit the Li/Laguerre claims much more deeply

Pass 1 treated many Li/Laguerre claims as novel after a relatively small literature survey.

Perform dedicated searches for each important cluster:

* deterministic pole mode \(1-q^n\);
* pole-subtracted Li/Laguerre sequence;
* shift filter

  $$
  (E-1)(E-q);
  $$
* RH-equivalent root-growth formulation;
* \(d(\psi-x)\) discrepancy representation;
* Airy saddle reconstruction of the pole rate;
* exact Cayley zero mode;
* critical-half-weight chirp;
* stationary frequency map;
* microlocal Dirichlet reduction;
* block-\(L^2\) equivalence;
* PNT-error obstruction;
* high-frequency endpoint merger;
* \(\sqrt n\) prime-side frequency cap;
* Vaughan/Heath-Brown obstruction;
* rank-one Hessian preservation;
* Type-II asymptotic separability;
* nonseparability threshold.

Search not just exact terminology but mathematical equivalents.

A result expressed in generating-function, saddle-point, Mellin-transform, finite-difference, or explicit-formula terminology may be equivalent despite different wording.

---

# 13. Re-audit the Li conditional-negative-definite formulation

Investigate the claim that:

$$
\psi(n)=\lambda_{|n|}
$$

is conditionally negative definite on \(\mathbb Z\) iff RH, and hence:

$$
e^{-t\lambda_{|n|}}
$$

is positive definite for all \(t>0\).

Search broadly in:

* Li coefficient literature;
* Schoenberg theory;
* negative type kernels;
* Herglotz/Bochner theory;
* infinitely divisible positive-definite sequences;
* Toeplitz kernels;
* semigroup formulations;
* harmonic analysis on \(\mathbb Z\) and \(\mathbb T\).

Do not conclude novelty merely because the phrase “conditionally negative definite Li coefficients” does not appear verbatim.

---

# 14. Re-audit obstruction claims individually

There are 15 `CLM-OBST` claims.

Do not aggregate them into “15 novel obstructions.”

Each must be individually adjudicated.

For every obstruction determine whether it is:

* an original theorem;
* a straightforward consequence of standard estimates;
* a reformulation of a known barrier;
* a new application of a known barrier;
* independently rediscovered;
* already explicit in prior work.

Particular attention:

* absolute PNT-error barrier;
* Vinogradov–Korobov insufficiency;
* block-\(L^2\) equivalence;
* Montgomery–Vaughan length barrier;
* rank-one Hessian;
* separability of Type-II boxes;
* square-root-saving threshold;
* generic Vaughan/Heath-Brown no-go;
* lossy 69% endpoint absorption.

---

# 15. Re-audit verification architecture claims

Separate **verified implementation facts** from **novelty claims**.

It is valid to verify factual statements such as:

* retained proof chain replays 8/8;
* SHA-256 hashes match;
* verifier uses `BigRational`;
* targeted theorem verification uses no floating-point arithmetic;
* malformed contract and theorem failure use separate exit codes;
* Lean modules prove specified lemmas.

But novelty requires external prior-art comparison.

Search for comparable proof-certificate systems in:

* computer-assisted number theory;
* interval-arithmetic proof certificates;
* exact rational certificates;
* independent checker architectures;
* formalized numerical proofs;
* Arb-based theorem generation;
* Lean/Coq/HOL verification of numerical certificates.

Do not conclude “first” simply because Chuk uses a different implementation.

---

# 16. Verify the “zero floating point” statement precisely

Audit the exact scope.

Determine whether:

* certificate generation uses floating/Arb arithmetic;
* certificate verification uses no IEEE floating-point;
* all mathematical acceptance decisions in `rh_cert` use exact integers/rationals;
* parsing, logging, conversions, diagnostics or unrelated utilities use floats anywhere.

Use precise wording such as:

> The theorem-verification acceptance path uses exact arbitrary-precision rational arithmetic and does not rely on floating-point acceptance tests.

if that is what the code supports.

Avoid broader wording than the implementation justifies.

---

# 17. Correctly describe formal verification scope

Do not state or imply that Lean proves the entire `C-0050..C-0057` theorem chain unless it actually does.

Determine exactly which lemmas/modules are formalized:

* interval arithmetic;
* Gershgorin;
* LDL/congruence;
* endpoint absorption;
* related soundness statements.

Then state clearly which parts remain outside Lean:

* analytic derivation;
* certificate generator;
* Rust implementation correspondence;
* schema/admission logic;
* full end-to-end theorem proof.

---

# 18. Timeline evidence rules

For every priority claim maintain separate fields:

$$
T_{\text{idea}},
T_{\text{commit}},
T_{\text{public push}},
T_{\text{external post}},
T_{\text{publication}}.
$$

Never collapse them.

Use priority verdicts such as:

* `PRIOR ART FOUND`
* `PRIORITY NOT SUPPORTED`
* `PRIORITY PLAUSIBLE`
* `PRIORITY SUPPORTED`
* `INCONCLUSIVE`

`PRIORITY SUPPORTED` should require externally verifiable evidence of public availability, not only an internally timestamped Git object.

---

# 19. Novelty verdict taxonomy

Use conservative verdicts.

Recommended outcomes:

* `PRIOR ART FOUND`
* `INDEPENDENT REDISCOVERY`
* `KNOWN INGREDIENT / NOVEL APPLICATION`
* `KNOWN INGREDIENTS / NOVEL SYNTHESIS SUPPORTED`
* `POSSIBLY NOVEL — NO PRIOR ART FOUND`
* `NOVELTY SUPPORTED`
* `PRIORITY PLAUSIBLE`
* `PRIORITY SUPPORTED`
* `INCONCLUSIVE`
* `CLAIM REQUIRES NARROWER WORDING`
* `CLAIM NOT SUPPORTED`

Reserve `NOVELTY SUPPORTED` for claims that survive substantial claim-specific search.

Absence of a search hit is not automatically proof of novelty.

---

# 20. All 66 claims need Pass 2 dispositions

Build an authoritative ledger such as:

`AUDIT_LEDGER.md`

Include:

| Claim | Pass 1 Verdict | Pass 2 Verdict | Changed? | Reason | Evidence |
| ----- | -------------- | -------------- | -------- | ------ | -------- |

All **66** claim IDs must appear.

No claim may disappear merely because it was omitted from Pass 1's individual dossiers.

If a claim cannot be adequately audited in Pass 2, mark:

`INCONCLUSIVE — REQUIRES PASS 3`

rather than inventing certainty.

---

# 21. Preserve Pass 1 historical integrity

Do not overwrite:

`FINAL_AUDIT.md`

or:

`reports/FINAL_AUDIT.md`

as though Pass 1 never happened.

Instead create new Pass 2 artifacts, for example:

```text
AUDIT_LEDGER.md
reports/AUDIT_PASS_2.md
reports/interim/PASS_2_*.md
evidence/search-records/PASS2-*.md
claims/... additional or revised Pass 2 dossiers
```

If useful, add a small notice near current navigation documentation stating that Pass 1 is historical and has been superseded for current conclusions by later passes.

But do not alter the substance of Pass 1.

---

# 22. Record corrections explicitly

For every changed verdict record:

* Pass 1 conclusion;
* new evidence;
* Pass 2 conclusion;
* why the change occurred.

Example:

```text
CLM-PRIO-005

Pass 1:
PRIORITY SUPPORTED

Pass 2:
PRIORITY PLAUSIBLE

Reason:
The Aug. 21 Git commit object is verified, but independent evidence
of public push/accessibility on Aug. 21 has not yet been located.
Commit metadata alone is insufficient under TIMELINE_RULES.md.
```

Or, if external evidence is found:

```text
Pass 2:
PRIORITY SUPPORTED

New evidence:
GH Archive PushEvent ...
Software Heritage snapshot ...
public fork containing commit ...
```

---

# 23. Search-record requirements

Every substantial novelty determination must have a reproducible search record containing:

* date/time actually performed;
* databases searched;
* exact queries;
* query variants;
* normalization synonyms;
* relevant hits;
* relevant negative searches;
* papers/repos inspected;
* why candidate prior art was or was not equivalent.

Do not use fabricated or placeholder timestamps.

Use actual execution time.

---

# 24. Literature evidence standards

Prefer primary sources.

For each relevant source record:

* title;
* author;
* publication/preprint date;
* version date;
* DOI/arXiv/repository identifier;
* stable URL;
* exact theorem/page/section;
* quoted or closely paraphrased mathematical statement;
* normalization mapping to project notation;
* method comparison;
* relevance to specific claim IDs.

Do not rely solely on abstracts or search snippets for a novelty verdict.

---

# 25. Do not confuse stronger later results with prior art for earlier priority

Be precise chronologically.

If the project publicly disclosed a theorem on August 21 and a stronger theorem appeared publicly on August 25, the later theorem does not retroactively erase the earlier disclosure.

But you must establish that August 21 **public disclosure** occurred.

Similarly, later project continuation points after August 25 may not themselves constitute result novelty if already subsumed by the stronger external theorem.

Separate those issues.

---

# 26. No RH overclaim

Maintain the existing boundary throughout.

The project does **not** prove RH.

It proves finite-support localized Weil positivity statements and develops several RH-equivalent reformulations/obstructions.

Do not convert an RH-equivalent criterion into progress toward proving that criterion unless an independent estimate actually advances it.

---

# 27. Pass 2 deliverables

At minimum produce:

```text
AUDIT_LEDGER.md
reports/AUDIT_PASS_2.md
evidence/public-timeline/PASS_2_TIMELINE.md
evidence/literature/PASS_2_PRIOR_ART.md
evidence/search-records/PASS2-*.md
```

Create individual Pass 2 dossiers for high-impact claims where necessary.

`AUDIT_PASS_2.md` should contain:

* scope;
* corrections to Pass 1;
* claim-accounting correction;
* chronology correction;
* missed prior art;
* theorem-validity findings;
* novelty findings;
* priority findings;
* verification findings;
* claims upgraded;
* claims unchanged;
* claims downgraded;
* claims marked inconclusive;
* unresolved questions for Pass 3.

---

# 28. Pass 2 must not call itself the final audit

Do **not** create or overwrite:

`CONSOLIDATED_FINAL_AUDIT.md`

unless specifically instructed later.

Pass 2 is another adversarial stage.

The purpose is convergence, not closure.

End with a section:

## Required Pass 3 Investigations

List every claim that still deserves deeper investigation.

---

# 29. Commit discipline

The audit repository is itself part of the evidence.

Make logically separated public commits where practical, for example:

```text
Audit Pass 2 - Correct claim inventory and chronology
Audit Pass 2 - Expand Weil positivity prior art
Audit Pass 2 - Reassess theorem and method novelty
Audit Pass 2 - Reassess Li Laguerre claims
Audit Pass 2 - Reassess verification architecture
Audit Pass 2 - Publish second-pass audit report
```

Do not squash away corrections.

The history is part of the scientific record.

---

# 30. Final objective

The objective is **not** to maximize the number of novel claims.

The objective is to determine as accurately as possible:

* what the project actually proved;
* what was already known;
* what was independently rediscovered;
* what appears to be genuinely new;
* what methodological synthesis is new;
* what verification architecture is new;
* what was publicly disclosed first;
* what priority cannot yet be established;
* and what remains uncertain.

A Pass 2 conclusion that substantially weakens Pass 1 is acceptable.

A Pass 2 conclusion that strengthens a claim is also acceptable.

Evidence decides.

The standard for success is:

> **A reader hostile to the project's claims should still be able to follow the evidence trail and understand why each surviving conclusion was reached.**
