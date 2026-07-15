# Archived Prompt For Proving The 410X One-Gap Five-Map Targets

Archive note, 2026-07-15: all three historical `4103` targets below are now
proved in `4106_CE1_one_gap_five_map_completion.md` and
`4107_CE2_one_gap_five_map_completion.md`.  The reduction file `4103` was
absorbed into those proofs and deleted.  The current package ledger is
`4101_CE1CE2_Nplus1_all_Vd0_strategy.md`; the sole open target is `4104-F`.
The remainder of this file is preserved as the historical task specification.

Read and analyze this repository:

https://github.com/dylan0301/hexagon-cover-database

You may inspect the Triangle mode in the following visual repository for
geometric intuition, but its old raw admissible-set predicate is not
proof-safe:

https://github.com/dylan0301/hexagon-cover-visual/tree/gulgu

## Mission

Prove the remaining exactly-one-gap five-map targets in the `410X` branch:

$$
T_C\text{ is CE1 or CE2},
\qquad
N_+=1,
$$

with all six vertex roles Vd0.

Focus on:

1. Target `4103-CE1`;
2. Target `4103-CE2-R`; and
3. Target `4103-CE2-L`, preferably by a fully audited reflection of the
   right-gap proof.

Produce a detailed mathematical report only. Do not edit or commit repository
files. Include failed approaches and counterexamples as fully as successful
arguments.

This task does not include proving Target `4104-F`. Even if all three five-map
targets are proved, state clearly that the full `410X` branch still depends on
the all-boundary six-point target recorded in `4104`.

## Current Resolution

The current `410X` package records:

- `4101_CE1CE2_Nplus1_all_Vd0_strategy.md` is now the current Strategy ledger.
- `4102_CE2_two_gap_completion.md` is Proven and eliminates the CE2 two-gap
  state.
- The former one-gap reduction was a Reduction to the three historical
  targets in this prompt; its routing is now incorporated into proved `4106`
  and `4107`.
- `4104_all_boundary_transfer_to_310X.md` is a Reduction to Target `4104-F`.

Do not redo the center parameterization, monotonicity reduction, exhaustive
gap split, CE2 two-gap proof, or all-boundary transfer unless you find a
specific error. Treat a `Reduction` as a proved routing statement, not as a
proof of its terminal target.

## Required Reading

First read `AGENTS.md`, `README.md`, the main proof-tree and status files, the
notation dictionary, and all four files in:

`proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/`

Then inspect at least:

- `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md`
- `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md`
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md`
- the exact CE1 and CE2 endpoint theorems cited by `4102` and `4103`
- the exact shortcut counterexamples in Section 5 of `4103`

Preserve every recorded proof status. In particular, numerical evidence is
Empirical until converted into an independently checkable certificate.

## Proof-Safe Maps

For each nonsupercritical row $i\ne0$, use

$$
F_i(a)=\min\left\{B_{c_i}(a),1-a\right\},
\qquad
G_i(a)=1-F_i(a).
$$

Equivalently,

$$
G_i(a)=\max\left\{1-B_{c_i}(a),a\right\}.
$$

Here $B_c(a)$ is the exact selected support-contact map proved in `2007`, not
the obsolete unselected candidate list and not the old raw Cell-2 polynomial
from the visual code.

For the unique strict-supercritical row $T_0$, retain the exact common-row
bound $B_{c_0}$ and, when useful, the proved free envelope

$$
S_+(c)=\frac{c+\sqrt{c^2-8c+4}}2,
\qquad
0\le c<\frac12.
$$

Do not identify a radial demand with the actual radial reach of a realizing
triangle. Follow the demand semantics and feasible-set inclusions proved in
`4101` and `4103`.

Whenever a piece of $B_c(a)$ is used, prove all of the following:

- its selector and contact type hold on the stated parameter cell;
- the selected radical or algebraic root is the geometrically valid root;
- every denominator and squared quantity has the required sign; and
- transitions, undefined regions, and equality faces are handled.

## Target 4103-CE1

Use the exact CE1 variables and strict domain from `2105`:

$$
T_C\cap e_{0,1}=[s,t],
\qquad
u=1-t.
$$

The proved survivor reduction restricts the domain by

$$
B_{c_0}(s)>1-s.
$$

Define

$$
Z_{\mathrm{CE1}}
=
(G_5\circ G_4\circ G_3\circ G_2\circ G_1)(u).
$$

Prove throughout the entire strict survivor domain that

$$
\boxed{
Z_{\mathrm{CE1}}>B_{c_0}(s).
}
$$

The direct two-adjacent-row shortcut is false. The exact CE1 witness in
Section 5.1 of `4103` proves that $G_2,G_3,G_4$ cannot simply be discarded.

## Targets 4103-CE2-R And 4103-CE2-L

Use the exact coupled CE2 interval domain from `2106`:

$$
T_C\cap e_{5,0}=[x,u],
\qquad
T_C\cap e_{0,1}=[y,v].
$$

For a unique gap in the right interval, define

$$
Z_{\mathrm{CE2}}^R
=
(G_5\circ G_4\circ G_3\circ G_2\circ G_1)(1-v).
$$

On the proved survivor domain

$$
B_{c_0}(y)>\max\left\{u,1-y\right\},
$$

prove

$$
\boxed{
Z_{\mathrm{CE2}}^R>B_{c_0}(y).
}
$$

Then reflect the complete proof, including the center variables, radial
demands, map order, selector conditions, and strict inequalities, to obtain

$$
Z_{\mathrm{CE2}}^L
=
(G_1\circ G_2\circ G_3\circ G_4\circ G_5)(1-u)
>
B_{c_0}(x)
$$

on the reflected survivor domain

$$
B_{c_0}(x)>\max\left\{v,1-x\right\}.
$$

The exact CE2 witness in Section 5.2 of `4103` rules out the corresponding
two-adjacent-row shortcut. It is not a counterexample to the five-map target.

## Recommended Proof Program

### 1. Reduce the exact domains

Use the equations and strict inequalities in `2105` and `2106` to eliminate
dependent variables and reduce dimension where possible. Record a complete
semialgebraic description of each survivor domain. Do not replace coupled CE2
variables by independent interval bounds unless the relaxation direction is
proved sufficient for the target.

### 2. Build the selected-branch catalog

Starting with the exact input, propagate through $G_1,\ldots,G_5$. Partition the
center domain according to:

- the selected piece of each $B_{c_i}$;
- whether $G_i(a)=a$ or $G_i(a)=1-B_{c_i}(a)$; and
- every transition surface crossed by the composition.

Prune empty cells rigorously. Look for monotonicity, invariant intervals,
telescoping bounds, or geometric coupling that can avoid a full branch
enumeration.

### 3. Perform proof-safe numerical exploration

Implement or directly evaluate the exact `2007` map, including its selectors.
Do not use the old `gulgu` `maps.ts` predicate as ground truth. Search for the
minimum margins

$$
Z_{\mathrm{CE1}}-B_{c_0}(s)
$$

and

$$
Z_{\mathrm{CE2}}^R-B_{c_0}(y)
$$

over their exact survivor domains. Identify limiting boundary families,
near-zero margins, active map sequences, and any genuine counterexample.

If a target is numerically false, give explicit center parameters, all radial
demands, every map value and selector, and an independently reproducible
verification. Do not continue trying to prove a false inequality.

### 4. Produce a rigorous certificate

Prefer a short analytic proof when the selected branches reveal one. Otherwise
construct a finite interval-arithmetic certificate. A certificate must record:

- a finite covering of the full survivor domain;
- outward-rounded enclosures for radicals and compositions;
- proof that each box satisfies the asserted selectors or a subdivision at
  selector boundaries;
- treatment of strict-domain limits and all boundary faces; and
- a verifier specification, source code, and reproducible output in the
  report.

A floating-point grid, optimizer output, plot, or reported positive sample
margin is not a proof.

## Forbidden Shortcuts And Warnings

- Do not use the false two-adjacent-row inequalities refuted in `4103`.
- Do not use the obsolete high-$c$ sheet accepted by the old visual predicate.
- Do not assume the free supercritical envelope alone excludes the survivor
  thresholds; Section 4 of `4103` proves that it does not.
- Do not assume CE2 interval variables are independent.
- Do not replace strict open-cover conditions by closed equalities without a
  limit argument and the correct inequality direction.
- Do not claim the `908X` skeleton example is a `410X` counterexample; the
  current package records its center role as empirically CE0.
- Do not work on `4104-F` unless a fact about it is necessary to state the
  remaining status accurately.

## Final Report

Organize the report as:

1. status and dependency audit;
2. exact restatement of the three targets;
3. reduced CE1 and CE2 survivor domains;
4. selected-map branch catalog;
5. numerical search and active limiting configurations;
6. analytic proof or rigorous certificate for `4103-CE1`;
7. analytic proof or rigorous certificate for `4103-CE2-R`;
8. audited reflection proving `4103-CE2-L`;
9. failures, counterexamples, or remaining gaps; and
10. strongest justified conclusion for the `410X` package.

If all three targets are proved, conclude only that the exactly-one-gap CE1
and CE2 subcases are closed. State that the full `410X` branch remains open
until Target `4104-F` is also proved. Do not upgrade any proof status beyond
what the completed arguments justify.
