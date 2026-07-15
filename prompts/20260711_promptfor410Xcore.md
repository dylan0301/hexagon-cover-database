# Prompt For Closing The 410X Branch

Read and analyze this repository:

https://github.com/dylan0301/hexagon-cover-database

Also inspect the Triangle mode on this branch:

https://github.com/dylan0301/hexagon-cover-visual/tree/gulgu

## Mission

Close, or make the strongest rigorous progress toward closing, the `410X`
branch: CE1/CE2, $N_+=1$, with all six vertex triangles Vd0.

The target is the `410X` branch of the full-hexagon covering problem. Begin
with a hypothetical cover of the full hexagon $H$, not merely a cover of the
skeleton $S$. State and reconcile the exact open/closed/scaled formulation
used by the corpus before starting. Do not silently strengthen or change the
theorem.

Produce a detailed mathematical report only. Do not edit or commit repository
files. Report failed arguments and counterexamples as fully as successful
ones.

## Required Reading

First read `AGENTS.md`, `README.md`, the main proof-tree and status files, the
notation dictionary, and the local `410X` note. Then inspect at least:

- `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/`
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`
- `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100` through `2103`
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md`
- both live `310X` strategies, especially the six-point and ab-union
  construction
- failed or empirical notes `9080`, `9081`, `9630`, and `9805`
- `prompts/20260705promptforcoreTheta.txt`
- `prompts/20260708promptforCE2oneVD1remaining.txt`
- `prompts/20260626proofsketch407Xprompt.txt`
- `prompts/20260616promptfor310X.txt`

Preserve every recorded proof status. A Definition, Strategy, Empirical
result, or Practically proven lemma is not automatically a proved dependency.

## Strategy To Formalize

Parameterize the center triangle $T_C$ by its centroid $z=(x,y)$ and rotation
$\theta$. Use the standard unit-equilateral formula recorded in `2014`, but do
not import the Vd1/Vd2 corner assumptions of that note. Derive exact formulas
for:

1. the valid parameter domain in which $O$ lies in $T_C$;
2. all six radial exit lengths $d_i$;
3. the relaxed radial demands $c_i=1-d_i$ for $T_i$;
4. the one CE1 or two CE2 boundary intervals;
5. the exact-$M_0$ normalization and all symmetry reductions.

Prove the relaxation $c_i=1-d_i$ using monotonicity. Do not write "by
monotonicity" without proving the relevant inclusion and inequality
directions.

For fixed radial demand $c$, use

$$
B_c(a)=\max\left\{b:(a,b,c)\text{ is admissible}\right\},
\qquad
g_c(a)=1-B_c(a).
$$

Audit whether `2007` proves every branch formula needed. If it does not, prove
the required branch completeness or retain it as an explicit dependency.
Determine whether the full map $B_c$ is a valid relaxation for all-Vd0,
$N_+=1$. If necessary, derive restricted maps for the five nonsupercritical
rows and for the unique supercritical row, and enumerate the supercritical
index.

## One Center-Interval Gap

Write a center interval on $e_{i,i+1}$, parametrized from $V_i$, as
$I=[s,t]$. The `gulgu` Triangle mode uses the counterclockwise order

$$
V_{i+1},V_{i+2},\ldots,V_i
$$

with start $x_0=1-t$ and recurrence

$$
x_{k+1}=g_{c_{i_k}}(x_k).
$$

Its necessary terminal condition is $x_6\le 1-s$. Derive this rigorously from
boundary coverage. Also derive the reverse-direction start, row order,
composition, and target.

Prove the closed-endpoint reduction carefully. If the V-triangles leave only a
subinterval of $I$ uncovered, show why replacing that gap by the whole interval
$I$ is a valid relaxation. Explain precisely which adjacent V-triangle must
cover each endpoint and why no nonlocal Vd0 triangle invalidates the row model.

## CE1 And CE2 Cases

Give an exhaustive split:

- CE1 with no V-gap in its center interval;
- CE1 with a V-gap;
- CE2 with neither center interval containing a V-gap;
- CE2 with a V-gap in exactly one center interval;
- CE2 with V-gaps in both center intervals.

For the last case, derive the correct coupled shorter propagation chains and
their endpoint inequalities. Do not force an unjustified sixfold composition.
Account for the fact that the two CE2 intervals are geometrically coupled.

## All-Boundary-Covered Reduction

If the V-triangles redundantly cover every boundary interval met by $T_C$,
then they cover all of $\partial H$. Starting from the full-$H$ cover
hypothesis, select the six boundary handoff points and construct the
corresponding ab-union sets or finite obstruction points.

Prove a precise transfer lemma to the `310X` strategy: identify every place
where `310X` uses CE0 and show that redundant V-coverage supplies the needed
hypothesis, or record the exact point where the transfer fails. Interior
ab-union points may be used here because the original hypothesis covers $H$,
not only $S$.

This reduction is conditional: `310X` is still recorded as Strategy. Do not
claim that reducing to `310X` independently proves `410X`, and do not use this
branch to claim literal skeleton noncoverage.

## Counterexample And Numerical Audit

First run and inspect the `908X` skeleton counterexample. Classify its center
triangle, all six vertex types, $N_+$, boundary intervals, and radial data.
Explain why it does or does not satisfy `410X`. Remember that floating-point
classification is empirical unless made rigorous.

Reproduce the `gulgu` Triangle-mode computations from `src/main.ts`,
`maps.ts`, `triangle.ts`, and `cover.ts`. Scan the valid CE1 and CE2
center-parameter domains, including all possible locations of the unique
supercritical row. Test both propagation directions and the two-gap CE2
inequalities. Search actively for counterexamples before attempting a proof.

Numerics are for discovery only. Convert any claimed global inequality into a
hand proof, exact algebraic certificate, interval-arithmetic certificate, or
another independently checkable rigorous argument. Give explicit domains,
branch conditions, strictness margins, and treatment of degeneracies.

## Final Report

Organize the report as:

1. repository status and dependency audit;
2. exact theorem and rephrased strategy;
3. center parameterization and endpoint lemmas;
4. CE1/CE2 exhaustive case analysis;
5. numerical experiments and counterexample search;
6. rigorous proofs or proposed certificates;
7. conditional `310X` reduction;
8. unresolved obligations and exact failure reasons;
9. strongest conclusion justified by the work.

Do not say that `410X`, `310X`, skeleton noncoverage, or the main theorem is
proved unless every required dependency has a proof-level certificate.
