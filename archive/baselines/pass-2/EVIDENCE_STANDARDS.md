# Evidence Standards & Citation Policy

This document governs the collection, validation, and storage of evidence in this audit.

---

## 1. Hierarchy of Evidence

The audit relies strictly on verifiable, primary mathematical and historical evidence. Evidence is weighted according to the following hierarchy:

```text
Tier 1 (Authoritative Primary Sources)
  ├── Peer-reviewed journal publications (with DOI)
  ├── Official timestamped preprint versions (arXiv, HAL, Zenodo)
  ├── Cryptographically timestamped / public Git repositories (commit hashes, signed tags)
  └── Author manuscripts with verifiable institutional hosting

Tier 2 (Secondary Public Records)
  ├── Conference proceedings and public lecture slide decks
  ├── Internet Archive / Wayback Machine snapshots of public disclosures
  └── Verified public technical blogs / announcements with immutable timestamps

Tier 3 (Informal / Contextual — Ineligible for Sole Priority/Novelty Verdicts)
  ├── Personal communications
  ├── Unverified third-party summaries or social media posts
  └── AI-generated summaries or unstructured citations
```

---

## 2. Copyright & PDF Storage Policy

To comply with copyright laws and intellectual property boundaries:

1. **NO Paywalled / Proprietary PDFs**: Never commit downloaded commercial journal PDFs or proprietary documents into this repository.
2. **Permitted Documents**: Only openly licensed documents (e.g., CC-BY, public domain, or open-access preprints explicitly permitting redistribution) may be stored in `evidence/literature/`.
3. **Bibliographic Dossiers**: For all external literature, record:
   * Formal citation (BibTeX).
   * Permanent Identifier: DOI, arXiv ID, MR / zbMATH identifier.
   * Direct persistent URL.
   * Specific section, theorem, page, and equation numbers.
   * Local verification hash (`SHA-256`) of the examined document to ensure version consistency.

---

## 3. Literature Evidence Schema

Every external paper analyzed during an audit must be documented in `evidence/literature/` using the following metadata structure:

```yaml
id: "LIT-YYYY-AUTHOR-SHORTTITLE"
title: "Full Title of the Work"
authors: ["Author One", "Author Two"]
year: YYYY
venue: "Journal Name / arXiv Repository"
doi: "10.xxxx/xxxxx"
arxiv_id: "xxxx.xxxxx"
mr_number: "MRxxxxxxx"
license: "CC-BY-4.0 / All Rights Reserved / Open Access"
sha256: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
relevant_sections:
  - theorem: "Theorem 3.2"
    page: 14
    summary: "Establishes coercivity bounds on polynomial basis..."
```

---

## 4. Search Logging Standards

Every literature query performed must generate a corresponding search log in `evidence/search-records/`.

Search records must preserve:
* Exact query strings, boolean combinations, and wildcards.
* Target database/index and date accessed.
* Filters applied (e.g., subject class `math.NT`, date ranges).
* Total results returned and specific items shortlisted for detailed review.
* Null results (zero hits), serving as evidence of novelty boundaries.
