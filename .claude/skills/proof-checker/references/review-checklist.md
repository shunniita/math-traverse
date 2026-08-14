# Mathematical proof review checklist

## Contents

1. Issue classification
2. Mandatory checks
3. Common theorem side conditions
4. Counterexample strategies
5. Deep-fix fields

## Issue classification

Assign a proof status:

- `INVALID`: the statement is false as written or contradicts established premises.
- `UNJUSTIFIED`: the statement may be true, but the supplied proof does not establish it.
- `UNDERSTATED`: the proof needs stronger assumptions than the statement declares.
- `OVERSTATED`: the conclusion or scope is broader than the argument supports.
- `UNCLEAR`: notation, domains, or quantifiers prevent a definite judgment.

Assign an impact:

- `GLOBAL`: breaks the main theorem or its core dependency chain.
- `LOCAL`: affects a secondary result without breaking the main theorem.
- `COSMETIC`: affects exposition only.

Derive severity:

- `FATAL`: INVALID + GLOBAL.
- `CRITICAL`: INVALID + LOCAL or UNJUSTIFIED + GLOBAL.
- `MAJOR`: UNJUSTIFIED + LOCAL or UNDERSTATED/OVERSTATED + GLOBAL.
- `MINOR`: clarity, notation, or bookkeeping that does not change a claim.

Use one or more categories:

- Logic: `UNJUSTIFIED_ASSERTION`, `UNPROVEN_SUBCLAIM`, `QUANTIFIER_ERROR`, `IMPLICATION_REVERSAL`, `CASE_INCOMPLETE`, `CIRCULAR_DEPENDENCY`, `LOGICAL_GAP`.
- Analysis: `ILLEGAL_INTERCHANGE`, `NONUNIFORM_CONVERGENCE`, `MISSING_DOMINATION`, `INTEGRABILITY_GAP`, `REGULARITY_GAP`, `STOCHASTIC_MODE_CONFUSION`.
- Model and parameters: `MISSING_DERIVATION`, `HIDDEN_ASSUMPTION`, `INSUFFICIENT_ASSUMPTION`, `DIMENSION_TRACKING`, `NORMALIZATION_MISMATCH`, `CONSTANT_DEPENDENCE_HIDDEN`.
- Scope and sources: `SCOPE_OVERCLAIM`, `REFERENCE_MISMATCH`.

## Mandatory checks

For every theorem, lemma, proposition, corollary, and nontrivial proof step:

1. Resolve every symbol to a stable type and definition.
2. Restate the claim with explicit domains and quantifiers.
3. For each application of another result, list and discharge every hypothesis at that location.
4. Check each equality and inequality for direction, absolute values, signs, domains, dimensions, and needed convexity or positivity.
5. Justify every interchange of limits, derivatives, expectations, integrals, sums, suprema, and infima.
6. Track convergence mode: almost sure, in probability, in distribution, in norm, in expectation, or high probability.
7. State the limit variable, fixed variables, uniformity set, and hidden parameter dependence for every asymptotic notation.
8. Test boundary, degenerate, zero, singular, low-rank, and non-unique cases.
9. Check dependency direction and detect forward references or circular reasoning.
10. Verify that the final conclusion matches the theorem statement exactly.
11. Verify cited results from an authoritative source when their precise hypotheses matter.
12. Treat `WLOG` as a claim requiring an invariant and a reversible reduction.

## Common theorem side conditions

- Dominated convergence: almost-everywhere convergence and one integrable dominating function independent of the limit index.
- Monotone convergence: measurable, nonnegative, monotone-increasing sequence.
- Fubini: product measurability and absolute integrability. Tonelli: measurability and nonnegativity.
- Differentiation under an integral: an appropriate derivative exists and is dominated or otherwise controlled uniformly in a neighborhood.
- Implicit function theorem: continuous differentiability and an invertible relevant Jacobian at the base point.
- Taylor expansion: sufficient differentiability on the required region and a valid remainder estimate.
- Jensen: correct convexity or concavity direction and integrability.
- Cauchy–Schwarz or Hölder: correct normed or inner-product setting and finite required norms.
- Spectral perturbation results: symmetry or normality assumptions, eigengap conditions, and correct operator norm.
- Analytic continuation: connected domain and a valid uniqueness/identity theorem setup.
- Optional stopping: explicit stopping-time, integrability, boundedness, or uniform-integrability conditions appropriate to the theorem version.

## Counterexample strategies

- Set dimension or sample size to the smallest admissible value.
- Push parameters to zero, infinity, a boundary, singularity, or a repeated eigenvalue.
- Use a two-point, atomic, heavy-tailed, or non-symmetric distribution.
- Break uniqueness by symmetry or flat directions.
- Compare the claimed uniform rate along adversarial parameter sequences.
- Substitute units and dimensions to expose impossible equalities.
- Numerically search only as a falsification aid; convert a numerical hit into an exact or rigorously bounded counterexample before calling it verified.

## Deep-fix fields

For `--deep-fix`, attach to each actionable issue:

- `corrected_statement`: paste-ready theorem or lemma statement with quantifiers and scope.
- `changed_equations`: exact before/after pairs.
- `downstream_labels`: every dependent label requiring re-check.
- `minimal_patch_plan`: ordered file, anchor, and replacement entries.
- `closure_tests`: two to five mathematical or compilation checks.
- `algebra_sanity` when relevant: symbol dimensions, factor/power count, degenerate-point check, and constant-dependence changes.
