# Five-Point Target and Proof Obligations

Status: Lemma target

This file records the May 25 conjecture as a proof target.  No proof or
counterexample is recorded here.

## Target statement

Work in the reduced slice from `631_reduction_prompt_spec.md`.  Assume all five
points

$$
P_3,\qquad P_5,\qquad D_0,\qquad D_1,\qquad D_2
$$

are defined.  Let

$$
K_5=\{P_3,P_5,D_0,D_1,D_2\}.
$$

The May 25 target is

$$
\Lambda(K_5)>1.
$$

Equivalently, no closed unit equilateral triangle contains $K_5$.

## Required proof obligations

A proof should supply all of the following.

1. Parameter-domain reduction.

   The assumptions

   $$
   t_3=t_2,\qquad t_5=t_4,\qquad t_4>t_2,
   $$

   and

   $$
   t_0\le t_5,\qquad t_1\le t_0,\qquad t_2\le t_1
   $$

   must be the only May 25 slice assumptions, apart from explicit
   nonundefinedness of the five points.

2. Branch realization for $P_3$ and $P_5$.

   The chosen non-axis intersections must be shown to exist on the intended
   branch, satisfy the active $R_4$ boundary conditions, and be the branch
   closest to $V_4$ when several algebraic intersections exist.

3. Diagonal endpoint realization for $D_0,D_1,D_2$.

   For each $j=0,1,2$, one must identify the first point where the initial
   uncovered interval on $[O,V_j]$ stops, or prove that the whole half-diagonal
   remains uncovered and hence $D_j=V_j$.

   These points should not be replaced by the May 21/22 radial points or by a
   fixed Vd1/Vd2-style local choice.  They are defined by the actual union of
   all six $R_i$, so any earlier cross-cut of a half-diagonal changes the
   corresponding $D_j$.

4. Enclosing-triangle reduction.

   The inequality

   $$
   \Lambda(K_5)>1
   $$

   must be proved over every support-contact regime for the five-point set, or
   reduced to a finite list of certified inequalities.

5. Boundary and undefined cases.

   Cases where an intersection is tangent, a diagonal endpoint lies on
   $\partial U$, or $O\notin U$ must be separated from the strict defined
   five-point target.

## What would disprove the target

A counterexample would be a parameter choice satisfying the reduced slice, with
all five points defined, and a closed unit equilateral triangle containing

$$
P_3,\quad P_5,\quad D_0,\quad D_1,\quad D_2.
$$

Numerical data alone should be recorded as empirical unless it includes a
certificate strong enough to verify the parameter inequalities, branch choices,
diagonal endpoint definitions, and enclosing-triangle containment.

## Relation to existing tools

The support-function formula for $\Lambda(K)$ matches the formulation used in
`../500_half_skeleton_lemmas/507_minimal_enclosing_equilateral_quadrilateral_lemma.md`,
but that proven local lemma applies to convex quadrilaterals.  The May 25 set
has five points, so a separate five-point contact analysis is still required.
