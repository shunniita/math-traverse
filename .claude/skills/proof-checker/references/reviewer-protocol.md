# Independent reviewer protocol

## Contents

1. Reviewer modes
2. Ledger extraction
3. Verdict review
4. Repair review
5. Failure handling

## Reviewer modes

Use the strongest available honest mode and record it exactly:

- `cross-model`: a fresh reviewer using a different model family from the executor.
- `independent-agent`: a fresh context or subagent, potentially using the same model family.
- `single-agent`: no independent reviewer was available; the executor performed separate construction and adversarial passes.

Never infer model identity. If it is unknown, do not call the run cross-model.

## Ledger extraction

For a large proof, the skill explicitly permits subagents to extract independent theorem or section fragments when collaboration tools are available.

Give each extraction agent only its assigned source files and this schema:

```text
{ shard_id, entries: [{ dedup_key, kind, statement, symbols, assumptions,
  claimed_discharge_locations, dependencies, source_location }] }
```

Extraction agents must not mark a claim valid, proved, false, or sound. Merge fragments, deduplicate by canonical labels or stable ids, then compute cross-section symbol consistency and the global dependency DAG in one place.

## Verdict review

Use one fresh reviewer for the complete proof when collaboration tools permit it. Supply:

- the complete declared source set;
- `PROOF_SKELETON.md` or the complete ledger;
- the mandatory checklist and issue schema;
- a request to examine every theorem application and attempt counterexamples.

Do not supply the executor’s expected verdict. Ask for file-and-line evidence. The executor must verify every reported issue against source before accepting it.

If no independent reviewer can be used, run a clearly separated adversarial pass and record `single-agent` plus the limitation in the audit summary.

## Repair review

When the user authorized repairs:

1. Keep the original reviewer context for closure questions about its issues when the available collaboration mechanism supports follow-ups.
2. Send the repaired source and a concise fix ledger; ask whether each original obligation is now discharged and whether the fix introduced new gaps.
3. For a repaired FATAL or CRITICAL issue, use a fresh reviewer that sees only the fixed statement, proof, and required dependencies. Do not reveal the prior critique or desired verdict.
4. Treat the fresh review as blind only if it actually lacked the prior discussion.

The skill explicitly permits these review subagents; do not use them for unrelated work.

## Failure handling

- Do not retry a potentially completed paid or external review after a timeout unless the system proves it never executed.
- If an independent review fails, continue only if useful, label the mode accurately, and explain the limitation.
- Do not declare an issue closed merely because the reviewer stopped mentioning it; test the exact obligation.
- A reviewer disagreement is itself an audit finding. Present the competing claims and the decisive mathematical point.
