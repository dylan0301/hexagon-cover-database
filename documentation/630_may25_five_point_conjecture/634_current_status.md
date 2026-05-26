# Current Status of the May 25 Five-Point Package

Status: Reference

## Recorded definitions

The reduced slice is recorded in `631_reduction_prompt_spec.md`:

$$
t_3=t_2,\qquad t_5=t_4,\qquad t_4>t_2,
$$

with

$$
t_0\le t_5,\qquad t_1\le t_0,\qquad t_2\le t_1.
$$

The five-point set is

$$
K_5=\{P_3,P_5,D_0,D_1,D_2\}.
$$

## Open target

The main open target in this folder is

$$
\Lambda(K_5)>1.
$$

No proof, disproof, complete branch analysis, or finite certificate is recorded
in this package.

## Dependencies and unresolved gaps

| Item | Status |
|---|---|
| Reduced May 25 slice specification | Reference |
| Exact local $R(a,b)$ predicate | Reference |
| $P_3,P_5$ selected branch realization | Open |
| Diagonal endpoint realization for $D_0,D_1,D_2$ | Open |
| Five-point enclosing-triangle contact analysis | Open |
| Certified inequality proving $\Lambda(K_5)>1$ | Open |
| Counterexample with certified branch and containment data | None recorded |

## Relation to older targets

The May 25 conjecture is a focused finite-point obstruction.  It should not be
read as reviving the standalone full-skeleton noncoverage target, which is
refuted empirically in
`../800_computation/811_skeleton_cover_counterexample.md`.

The closest existing package is `../620_may21_patternA/`, which handles a
four-point Pattern A reduction under stronger equality structure.  The May 25
target removes the assumption $a_1+b_1=1$ and introduces the three
union-defined diagonal points $D_0,D_1,D_2$.  These three points are intended
to use the actual first uncovered endpoints on the diagonals, rather than a
fixed May 21/22 radial choice or a preassigned Vd1/Vd2-type local pattern.
