# Branch and Diagonal Case Notes

Status: Strategy

This file records the main branch-selection and diagonal-cut issues in the
May 25 five-point conjecture.

## $P_3$ and $P_5$ branch selection

The points $P_3$ and $P_5$ are selected from intersections of the non-axis
boundary of $R_4$ with radius-$1$ circles:

$$
C_2=\partial B(X_2,1),\qquad C_5=\partial B(X_5,1).
$$

The selected $P_3$ branch is the non-axis intersection between $\partial R_4$
and $C_2$ closest to $V_4$.  The selected $P_5$ branch is the analogous
intersection with $C_5$.

The local $R(a,b)$ predicate in `631_reduction_prompt_spec.md` gives a
semialgebraic way to test candidate intersections.  A branch proof must show
more than the existence of an algebraic root: it must verify that the root lies
on the active non-axis boundary piece, satisfies the relevant inequalities, and
is the closest valid branch to $V_4$.

## Undefined branch cases

The five-point configuration is undefined if either selected intersection does
not exist.  Such cases should not be counted as counterexamples to the May 25
conjecture, because the conjecture is only stated for parameter choices where
all five points are defined.

Tangent intersections need separate handling.  They may belong to the defined
boundary case if the selected point is still well-defined, but they should not
be folded into a strict branch argument without checking the active
inequalities.

## Diagonal endpoints

Let

$$
U=H\setminus\bigcup_{i=0}^5 R_i.
$$

If $O\notin U$, then the five-point configuration is undefined.  Otherwise

$$
D_j=\rho_jV_j,\qquad j=0,1,2,
$$

where

$$
\rho_j=\sup\{\rho\in[0,1]: \lambda V_j\in U
\text{ for every }0\le\lambda<\rho\}.
$$

Thus $D_j$ is determined by the first cut of the half-diagonal $[O,V_j]$ by
the union of all six $R_i$, not only by the local region adjacent to $V_j$.

This is the main change from the May 21/22 four-point radial construction.
The May 25 definition avoids committing to a fixed local radial point or a
preassigned Vd1/Vd2-type local pattern.  The point $D_j$ follows the actual
initial uncovered interval, so a nonlocal cut is part of the definition rather
than an exceptional failure mode.

Two common cases are:

1. No $R_i$ cuts $[O,V_j]$ before $V_j$.  Then $D_j=V_j$.
2. Some $R_i$ cuts $[O,V_j]$ before $V_j$.  Then $D_j$ is the first boundary
   point of $U$ along the ray from $O$ to $V_j$.

The source prompt emphasizes that a region such as $R_2$ may cut
$[O,V_1]$ before the usual radial point.  Such cross-cuts are part of the
definition and must be included in any proof.

## Proof strategy note

A useful implementation of the proof target should treat each $D_j$ as a
minimum over all valid cuts of the corresponding half-diagonal:

$$
\rho_j=\min\{1,\rho_{0j},\rho_{1j},\dots,\rho_{5j}\},
$$

where $\rho_{ij}$ denotes the first valid intersection of $R_i$ with
$[O,V_j]$, if it exists.  This formula is only a strategy notation here; each
$\rho_{ij}$ still requires a branch-realization proof from the exact local
predicate.
