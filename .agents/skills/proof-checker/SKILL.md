---
name: proof-checker
description: Rigorously audit mathematical proofs in LaTeX or Markdown, build a proof-obligation ledger, search for counterexamples and hidden assumptions, classify gaps, and optionally implement and re-check authorized fixes. Use for proof checking, theorem verification, 証明の検証, 証明チェック, proof audits, or requests to repair a mathematical argument.
---

# Proof Checker

Audit a mathematical proof without overstating certainty. Separate structural extraction, mathematical judgment, and authorized repair. Preserve a reproducible trail from source claims to the final verdict.

## Operating rules

- Treat review and repair as separate permissions. A request to check, review, diagnose, or audit is read-only. Edit the proof only when the user explicitly asks to fix, revise, or implement corrections.
- Never accept “clearly,” “standard,” “WLOG,” or “it follows” without identifying the actual rule and discharging its side conditions.
- Never label a candidate counterexample as a counterexample until its algebra and domain conditions are verified.
- Never claim cross-model review unless the reviewer actually used a different model family. Record fresh-context same-model review as `independent-agent`.
- Start each top-level invocation from the current source. Prior audits are evidence, not proof that the current files remain valid.
- Stop after three review-and-repair rounds. Report unresolved obligations honestly.

## Load the references

Read these files before making a verdict:

- [references/review-checklist.md](references/review-checklist.md) for the issue taxonomy, theorem side conditions, and adversarial checks.
- [references/reviewer-protocol.md](references/reviewer-protocol.md) before using independent reviewers or parallel extraction.
- [references/audit-contract.md](references/audit-contract.md) before writing audit artifacts or assigning a verdict.

## Inputs and options

Accept a path to a `.tex` or `.md` proof, a paper directory, or proof text supplied by the user.

Support these opt-ins when requested:

- `--deep-fix`: add paste-ready corrected statements, equation replacements, downstream labels, and closure tests to each actionable issue.
- `--restatement-check`: compare canonical theorem statements with abstracts, summaries, tables, captions, and later restatements.
- `--render-report`: generate a typeset audit report after the canonical Markdown and JSON artifacts exist.

If the scope is ambiguous, inspect the project and choose the narrowest theorem-bearing input set that answers the request. State that scope in the audit.

## Phase 0: Establish the source set

1. Locate the main proof and all files it directly imports or cites for definitions, assumptions, lemmas, and theorem statements.
2. Record paths relative to the paper directory. Use absolute paths only for files outside it.
3. Read the complete theorem-bearing source set, not excerpts alone.
4. Compute SHA-256 hashes for every reviewed input.
5. Inventory definitions, assumptions, theorems, lemmas, propositions, corollaries, labels, and cited results.
6. If there are no theorem-like claims or proofs, emit `NOT_APPLICABLE` rather than silently skipping.
7. If required source is unreadable or missing, emit `BLOCKED` and name the missing material.

## Phase 1: Build the proof-obligation ledger

Create `PROOF_SKELETON.md` with:

1. A dependency DAG whose nodes are definitions, assumptions, lemmas, and theorems, and whose edges mean “uses.” Detect syntactic and semantic cycles.
2. An assumption ledger for every theorem and every application of another result. Record the claimed discharge location; `UNVERIFIED` means no discharge location was found.
3. A typed symbol table containing domain, shape, parameter dependence, and any meaning changes.
4. Canonical quantified statements with domains, quantifier order, limit order, uniformity, and constant dependence made explicit.
5. A numbered micro-claim inventory. For each nontrivial step, record context, goal, inference rule, side conditions, and claimed discharge location.
6. A limit-order map for every asymptotic claim.

For a large paper, parallelize only ledger extraction when the reviewer protocol permits it. Merge all fragments before computing the DAG, symbol consistency, or any verdict. Extraction agents must not judge validity.

## Phase 2: Adversarial mathematical review

Review every theorem application and micro-claim using the full checklist. For each issue, record:

- stable issue id;
- proof status and impact;
- derived severity;
- taxonomy category;
- exact file and line;
- claimed statement;
- why it is false, unsupported, overstated, understated, or unclear;
- counterexample status: `verified`, `candidate`, or `none`;
- downstream results affected;
- minimal repair strategy.

Use an independent reviewer when available. Give it the full proof source and the checklist, but do not reveal the executor’s expected conclusion. Treat its response as evidence to adjudicate, not as an unquestionable oracle.

## Phase 2.5: Counterexample pass

Attempt to break every FATAL or CRITICAL issue and each key lemma involving uniqueness, positivity, curvature, uniform convergence, asymptotic rates, or a convergence-mode upgrade.

Try low dimensions, degenerate parameters, boundary points, extremal distributions, adversarial scaling, and small numerical searches where appropriate. Record successful and unsuccessful attempts in `PROOF_AUDIT.md`.

## Phase 3: Repair only when authorized

If the user requested review only, skip edits and proceed to the verdict.

If repair is authorized, process issues from highest to lowest severity:

1. Choose exactly one primary strategy: `ADD_DERIVATION`, `STRENGTHEN_ASSUMPTION`, `WEAKEN_CLAIM`, or `ADD_REFERENCE`.
2. Derive the correction completely before editing.
3. Preserve labels and public notation where possible.
4. Propagate changed assumptions, quantifiers, rates, and constants to every downstream statement and restatement.
5. Record before, defect, after, new obligations, and downstream effects.
6. Compile with the project’s existing LaTeX command. If the repository’s `latex-document` skill is available and applicable, use its compile-and-render workflow. Do not install packages or change toolchains without permission.
7. Re-run affected counterexamples, dependency checks, and theorem applications.

In `--deep-fix` mode, include a repair-grade plan for each actionable issue. If a precise plan cannot be produced, mark that plan `unavailable`; do not contaminate the normal issue list.

## Phase 4: Closure review

Re-review fixes in the same independent reviewer context when possible so the reviewer can compare each original issue with the repair. For every repaired FATAL or CRITICAL issue, also request a blind review from a fresh reviewer that sees only the fixed section and its dependencies.

Check globally:

- theorem statement exactly matches the proved conclusion;
- all obligations are discharged or explicitly assumed;
- cases cover the domain, including boundaries;
- induction has a base case, valid step, and decreasing measure;
- every WLOG reduction is reversible;
- assumption changes reach all downstream claims;
- the dependency DAG remains acyclic;
- notation and parameter dependence remain consistent.

Repeat repair and closure review at most three times. Do not silently pass an unresolved proof.

## Optional restatement check

With `--restatement-check`, locate labeled canonical theorem-like environments and compare them with nearby prose around references, abstracts, introductions, summaries, tables, and captions.

Report conditional loss, scope changes, quantifier loss, regime changes, constant changes, and unexplained variable renaming. Keep restatement drift separate from proof issues unless the drift is itself used in a downstream argument.

## Outputs

Always emit these canonical artifacts beside the reviewed proof:

- `PROOF_SKELETON.md`: dependency graph, ledgers, symbols, quantified statements, and micro-claims.
- `PROOF_AUDIT.md`: scope, reviewer mode, round-by-round findings, counterexample attempts, repairs, remaining assumptions, and verdict.
- `PROOF_AUDIT.json`: machine-readable verdict conforming to the audit contract.

When repair occurs, also emit `PROOF_CHECK_STATE.json` with round count and unresolved issue ids.

Generate `proof_audit_report.tex` and PDF only with `--render-report` or an explicit user request. Treat rendering failure as non-blocking when the canonical Markdown and JSON artifacts are valid.

## Handoff

Lead with the verdict and the strongest unresolved issue. State whether source files were changed, whether compilation passed, which reviewer mode actually ran, and whether independent confirmation was unavailable. Link the generated artifacts and changed proof files.
