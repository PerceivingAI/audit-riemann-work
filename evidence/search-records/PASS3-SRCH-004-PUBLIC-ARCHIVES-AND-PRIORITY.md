# Pass 3 Literature & Repository Search Record: PASS3-SRCH-004-PUBLIC-ARCHIVES-AND-PRIORITY

> **Search Record Metadata**  
> * **Search ID**: `PASS3-SRCH-004-PUBLIC-ARCHIVES-AND-PRIORITY`  
> * **Standard**: Reproducible Search Record per [`EVIDENCE_STANDARDS.md`](../../EVIDENCE_STANDARDS.md) & [`THIRD_AUDIT.md`](../../THIRD_AUDIT.md)  
> * **Target Scope**: Public Push Verification for Commit `6dd1d8f0` (`C-0050`) across GitHub Events, GH Archive, Software Heritage, Wayback Machine, and Zenodo  
> * **Access Date / Time**: `2026-09-24T22:40:00Z`  
> * **Auditor**: Independent Audit Pass 3 Team

---

## 1. Search Query Executions & Null Hit Logs

### Query 4.1: Public GitHub Event & Repository Search
* **Target Engine**: GitHub Public Search & REST API
* **Exact Query String**: `"PerceivingAI/riemann-conjecture" OR "6dd1d8f07e23dd39fcd2e36974c53a5054f810ec" OR "6dd1d8f0" site:github.com`
* **Filters Applied**: `site:github.com`, Exact commit hash and repository path
* **Total Results Returned**: **0 hits (Null Search Logged)**
* **Observation**: The repository `PerceivingAI/riemann-conjecture` was not indexed publicly with third-party web crawlers at this exact hash.

### Query 4.2: Wayback Machine Historical Web Crawl
* **Target Engine**: Internet Archive Wayback Machine API
* **Exact Query String**: `url:https://github.com/PerceivingAI/riemann-conjecture*`
* **Filters Applied**: Timestamp filter $\le$ `2026-08-25T11:42:00Z`
* **Total Results Returned**: **0 snapshots prior to August 25, 2026 (Null Search Logged)**.

### Query 4.3: Software Heritage & GH Archive PushEvent Index
* **Target Engine**: Software Heritage (SWH) Archive & GH Archive PushEvents
* **Exact Query String**: `swh:1:rev:6dd1d8f07e23dd39fcd2e36974c53a5054f810ec` / `PushEvent PerceivingAI/riemann-conjecture`
* **Filters Applied**: Date: `2026-08-20` to `2026-08-25`
* **Total Results Returned**: **0 indexed push records (Null Search Logged)**.

---

## 2. Priority Adjudication Impact

Under Section 18 of `THIRD_AUDIT.md`, cryptographic Git commit timestamps demonstrate author/committer time inside the local Git object, but do not prove public disclosure without an external witness.

* $T_{\text{commit}}(\text{C-0050}) = 2026-08-21\text{T}14:05:13\text{Z}$
* $T_{\text{ext\_post}}(\text{Chuk}) = 2026-08-25\text{T}11:42:00\text{Z}$
* $T_{\text{public\_push}}(\text{C-0050}) = \text{Unverified in third-party public archives}$

**Authoritative Priority Verdict**:
* `CLM-PRIO-005` is formally classified as **`PRIORITY PLAUSIBLE`** (and assigned `INCONCLUSIVE — REQUIRES PASS 4` for third-party public push verification).
