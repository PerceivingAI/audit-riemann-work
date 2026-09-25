# Priority and public-availability rules

## Event semantics

Priority concerns the public availability of the exact result, method, software fact, or historical record under comparison. Do not infer availability from a local commit time or compare unlike disclosure channels.

Record separate anchors for repository creation, original author and committer times, first independently witnessed public availability, archive capture, external submission, external public posting, external publication, and external code disclosure. Record the source, query, stable identifier, represented event, exact returned timestamp with offset and precision, response artifact, and result for every source examined.

A capture may prove availability no later than capture time without identifying the first push. Repository creation does not prove that all later content was public at creation. Author and committer timestamps are distinct claims within Git objects. Do not impose a presumed ordering on them.

## Decision rules

- `PRIORITY SUPPORTED` requires a normalized, content-specific comparison and independent evidence that the relevant source result was publicly available before the relevant external result. State the bounded comparison, not universal precedence over all possible work.
- An earlier local commit without a public witness may be described as `PRIORITY PLAUSIBLE` only as an inherited or explicitly qualified hypothesis. It cannot establish public priority or close that axis.
- `PRIOR ART FOUND` requires an actually inspected relevant external result and defensible chronology. Merely earlier metadata does not establish mathematical equivalence.
- Use `INCONCLUSIVE` where public availability, equivalence, or event meaning remains unresolved.

Compare arXiv public posting with source public availability; preserve submission separately. A later revised theorem carries its own version date. Treat forks, mirrors, releases, tags, and archive snapshots according to what content and time they actually establish.

## Collection

Investigate GitHub API records / `gh`, GH Archive, Software Heritage, Wayback, forks, mirrors, indexed commit URLs, and relevant release/tag metadata. Log each independently. A null query means that source did not supply evidence in the examined range; it does not prove non-occurrence.

A GH Archive investigation requires the actual event datasets or dataset query, relevant UTC hours/days, event filters including `PushEvent` and `CreateEvent`, retained executable query/script, matching or nonmatching output, and artifact hashes. A generic web search is not a GH Archive dataset investigation.

Do not reconcile arbitrary Markdown metadata clocks. When a timestamp is used as evidence, consult its authoritative source, retain its exact value, and state its event. Primary arXiv version metadata supersedes inherited audit dates when they conflict, through additive corrections to historical records.

## Candidate correspondence

`CLM-PRIO-001..003` concern public research history, negative-result history, and correction history. They are not aliases for prime-trace, shift-filter, or stationary-mode priority. Every priority candidate must be investigated under its canonical inventory proposition, with the semantic mapping review linked from `EVIDENCE_COVERAGE.md`.

Phase 0 resolves record ownership and records gaps; it does not perform or claim the Phase 5 external chronology investigation. See [FOURTH_AUDIT.md](FOURTH_AUDIT.md) for the execution plan.
