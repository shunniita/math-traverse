# Proof audit contract

## Contents

1. Canonical artifacts
2. JSON schema
3. Verdict rules
4. Optional fields
5. Freshness and paths

## Canonical artifacts

`PROOF_AUDIT.md` is the readable record. Include scope, source hashes, reviewer mode, theorem inventory, issues, counterexample attempts, repairs, compilation results, unresolved assumptions, and final verdict.

`PROOF_AUDIT.json` is the machine-readable verdict and must always be emitted, including `NOT_APPLICABLE`, `BLOCKED`, and `ERROR` outcomes.

`PROOF_SKELETON.md` is evidence, not a verdict. It records what the proof claims to discharge; only the review phase judges mathematical validity.

## JSON schema

Use this stable core:

```json
{
  "audit_skill": "proof-checker",
  "verdict": "PASS | WARN | FAIL | NOT_APPLICABLE | BLOCKED | ERROR",
  "reason_code": "all_obligations_discharged | minor_gaps | major_gaps | critical_gap | no_proofs | source_unreadable | review_error",
  "summary": "One-line verdict with the strongest limitation.",
  "scope": {
    "paper_root": ".",
    "review_only": true,
    "options": []
  },
  "audited_input_hashes": {
    "main.tex": "sha256:..."
  },
  "reviewer": {
    "mode": "cross-model | independent-agent | single-agent",
    "model": "exact id or unknown",
    "fresh_context": true,
    "limitations": []
  },
  "generated_at": "UTC ISO-8601",
  "details": {
    "theorems_audited": 0,
    "rounds": 1,
    "issues": [
      {
        "id": "T1-H1",
        "status": "INVALID | UNJUSTIFIED | UNDERSTATED | OVERSTATED | UNCLEAR",
        "impact": "GLOBAL | LOCAL | COSMETIC",
        "severity": "FATAL | CRITICAL | MAJOR | MINOR",
        "category": "LOGICAL_GAP",
        "location": "sections/proof.tex:182",
        "statement": "...",
        "note": "...",
        "counterexample": {"status": "verified | candidate | none", "note": "..."},
        "affects": [],
        "repair_strategy": "ADD_DERIVATION | STRENGTHEN_ASSUMPTION | WEAKEN_CLAIM | ADD_REFERENCE | NONE",
        "resolution": "open | fixed | accepted-risk"
      }
    ]
  }
}
```

Use exact JSON without comments or ellipses in actual output. Omit optional keys instead of inventing values.

## Verdict rules

- `NOT_APPLICABLE`: no theorem-like claim or proof exists in the declared scope.
- `BLOCKED`: required source cannot be read or a required external premise cannot be identified well enough to review.
- `ERROR`: the review process failed and no reliable verdict can be formed.
- `FAIL`: any open FATAL or CRITICAL issue; MAJOR issues may also justify FAIL when they collectively undermine the central claim.
- `WARN`: only MINOR issues remain, or bounded MAJOR issues do not invalidate the central theorem. Explain every MAJOR-to-WARN judgment.
- `PASS`: every identified obligation is discharged, the counterexample pass completed, and no open issue remains above MINOR. State reviewer limitations even on PASS.

Do not map an unproven statement to `refuted`. Refutation requires a verified counterexample or contradiction.

## Optional fields

With `--deep-fix`, add `details.deep_fix_status` and `details.deep_fix_plans`. If plans are malformed or unavailable, use status `unavailable` with an empty list; this must not change the base verdict.

With `--restatement-check`, add `details.restatement_check_status` and `details.restatement_drift`. Keep drift separate from proof issues unless a drifted restatement is used as a premise.

When repairs occur, `PROOF_CHECK_STATE.json` should include status, rounds, fixed and open issue ids, counterexample counts, compilation status, and timestamp.

## Freshness and paths

- Hash exactly the declared theorem-bearing input set reviewed in this invocation.
- Express in-root hash keys relative to the paper root. Use absolute paths only for external files.
- Regenerate hashes after authorized edits and final re-review.
- Never reuse a prior verdict without verifying its hashes against current files.
