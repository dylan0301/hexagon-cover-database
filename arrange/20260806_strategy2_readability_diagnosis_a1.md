# Reviewer Report: Strategy 2 Readability and Formalization Boundary

Date: 2026-08-06

Scope: `arrange/paper_draft/`, with emphasis on the reader-facing Strategy 2
chapter, the universal transfer calculus, the signed CE1/CE2 calculus, the
consolidated Strategy 2 verification appendix, and the active numbered proof
dependencies.

## 1. Recommendation

**Recommendation: major expository revision, with no change to theorem
status.**

The active proof tree records the main theorem and all Strategy 2 terminal
dependencies as `Proven`.  The problem is not that the paper lacks a logical
route.  The problem is that the paper presents several different logical
layers at the same time:

1. geometric classification;
2. extraction of scalar demands;
3. definition of transfer functions;
4. branchwise optimization;
5. the human proof of the optimization;
6. the final case routing.

Strategy 2 is therefore much harder to read than its underlying mechanism.
The main body currently asks a reader to parse exact semialgebraic domains,
signed center variables, contact-label functions, geometric state spaces,
residual operators, five-step iterates, special placement parameters, and
replacement charts before the reader has a stable picture of what contradiction
is being sought.

The appropriate revision is not another round of local notation compression.
It is a strict separation of proof layers.

## 2. What is already mathematically sound

The following parts of the current architecture are useful and should be
retained.

- The proof tree separates the CE0 branch from the combined CE1/CE2 branch.
- The actual supercritical count $N_+$ and active-gap rank
  $\mathrm{gr}$ give a compact kernel for the all-Vd0 cases.
- The canonical transfer family
  $g_c,\widehat g_c,g_c^\vee,\widehat g_c^\vee$ correctly distinguishes raw,
  capped, defect-coordinate, and incoming-reach statements.
- The warning that $g_0$ is not the identity while $\widehat g_0$ is the
  identity is necessary.
- The center-free hypotheses of the path budget are now stated correctly.
- The exact five-V-triangle target $Z>1-H$ is correctly distinguished from
  its complement-dual three-map target $>1-X$.
- The CE2 threshold result correctly says that at least one threshold fires,
  not exactly one.
- The T3-like endpoint proof correctly retains the full four-label audit.
- The Vd1 replacement correctly uses separate local charts and preserves the
  full skeleton.

These are proof-critical distinctions.  The revision must preserve them
verbatim at the interface level even while suppressing their formulas from the
reader-facing chapter.
