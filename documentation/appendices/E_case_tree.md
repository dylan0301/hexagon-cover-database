# Overall Proof Tree for Hexagon Noncoverability

Status: Strategy

This file records the intended proof tree for the seven-triangle
noncoverability theorem.  It is not a completed proof of the main theorem.
Each branch below keeps its recorded proof status: proven local packages are
cited as such, while reductions, certificates, and inequalities not yet proved
remain targets or strategies.

## Main target

Let $H$ be the regular side-$1$ hexagon centered at

$$
O=(0,0).
$$

Its vertices are

$$
V_i=\left(\cos\frac{i\pi}{3},\sin\frac{i\pi}{3}\right), \qquad i\in\mathbb Z/6\mathbb Z.
$$

The boundary edge from $V_i$ to $V_{i+1}$ is

$$
e_{i,i+1}=[V_i,V_{i+1}].
$$

The theorem target is:

$$
\text{The side-$1$ hexagon }H\text{ cannot be covered by seven open unit equilateral triangles.}
$$

The equivalent expanded closed formulation is:

$$
\text{For every }L>1,\ H_L\text{ cannot be covered by seven closed unit equilateral triangles.}
$$

Here

$$
H_L=\operatorname{conv}\{LV_0,\dots,LV_5\}.
$$

The open/closed/scaled equivalence is proved in
[`../100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`](../100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md).

The one-dimensional targets used in local branches are

$$
S=\partial H\cup [V_0,V_3]\cup [V_1,V_4]\cup [V_2,V_5],
$$

and

$$
S_{1/2}=\partial H\cup\{O,M_0,\dots,M_5\}, \qquad M_i=\frac12V_i.
$$

Noncoverage of $S$ would imply noncoverage of $H$, but standalone
noncoverage of $S$ is refuted by the May 24 numerical counterexample in
[`../800_computation/811_skeleton_cover_counterexample.md`](../800_computation/811_skeleton_cover_counterexample.md).
Thus every use of $S$ or $S_{1/2}$ below is a local or conditional branch
obstruction, not a standalone global theorem.

## Common bookkeeping

Under a hypothetical cover, choose seven role triangles

$$
T_C,T_0,T_1,\dots,T_5.
$$

Here $T_C$ is a unit equilateral triangle containing $O$, and $T_i$ is a unit
equilateral triangle containing $V_i$.  This is bookkeeping: if more than one
triangle contains a special point, choose one representative for the role.

Write

$$
r_i=[O,V_i]
$$

for the radial segment from $O$ to $V_i$.  For the $V_i$-triangle type, the
adjacent radial segments are $r_{i-1}$ and $r_{i+1}$.

For the center triangle, define

$$
N_E(T_C)=\#\{i:T_C\cap e_{i,i+1}\text{ contains a positive-length interval}\}.
$$

The center-edge cases are

$$
\mathrm{CE0}\iff N_E(T_C)=0,
$$

$$
\mathrm{CE1}\iff N_E(T_C)=1,
$$

and

$$
\mathrm{CE2}\iff N_E(T_C)=2.
$$

Point contacts, tangencies, and vertex-only contacts do not count as
positive-length edge overlaps.

For a vertex triangle $T_i$, define

$$
o_i=\#\{\text{vertices of }T_i\text{ outside }H\},
$$

and

$$
n_i=\#\{\text{adjacent rays }r_{i-1},r_{i+1}\text{ having positive-length intersection with }T_i\}.
$$

The vertex-triangle types are

$$
\mathrm{Vd0}:(o_i,n_i)=(1,0)\text{ or }(2,0),
$$

$$
\mathrm{Vd1}:(o_i,n_i)=(1,1),
$$

$$
\mathrm{Vd2}:(o_i,n_i)=(1,2),
$$

and

$$
\mathrm{T3\text{-}like}:(o_i,n_i)=(2,1).
$$

Whenever the perimeter handoff data is represented by local rows, write

$$
(a_i,b_i)
$$

for the incoming and outgoing boundary lengths assigned to the vertex role
$T_i$ at $V_i$.  A row is called supercritical when

$$
a_i+b_i>1.
$$

The main supercritical count is

$$
N_+=\#\{i:a_i+b_i>1\}.
$$

The current strategy splits first by the center type $\mathrm{CE0}$,
$\mathrm{CE1}$, or $\mathrm{CE2}$, and then by $N_+$.

## CE0 local-type shortcut

The branch

$$
T_C\text{ is CE0 and at least one }T_i\text{ is Vd1 or Vd2}
$$

is already recorded as a proven half-skeleton obstruction in
[`../600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md`](../600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md).
The proof applies to $S_{1/2}$ in the expanded closed formulation and then to
the original open formulation by the equivalence theorem.

The proof components are the rhombus geometry, frontier perturbation,
$F$-chain inequalities, midpoint-hole subcases, and assembly files
`602`-`606`.  The normalized proof chooses a Vd1/Vd2 triangle as $T_0$ and
splits according to the adjacent-ray distance

$$
x<\frac12 \qquad\text{or}\qquad x\ge\frac12.
$$

This shortcut does not close the remaining CE0 branches where no Vd1/Vd2
triangle is available.  Those branches must still be handled by the
supercritical-count tree below or by another certified argument.

## Supercritical-count proof tree

The intended global tree is:

```text
Hypothetical seven-triangle cover
  classify T_C as CE0, CE1, or CE2
  define perimeter rows (a_i,b_i) for the vertex roles
  compute N_+ = #{i : a_i+b_i > 1}

  N_+ = 0
    CE0:
      direct perimeter-length obstruction
      T_C contributes no positive boundary interval
      all vertex rows have a_i+b_i <= 1
    CE1/CE2 recorded closed branch:
      CE1/CE2 + all Vd0 + all rows non-supercritical
      -> boundary-loss contradiction under the assumptions of 551
    remaining reductions:
      justify all-Vd0 and active-interval assumptions where needed

  N_+ = 1
    target:
      reduce the full one-supercritical branch to the May 25 five-point model
      prove Lambda(K_5) > 1 in that model

  N_+ >= 2
    CE0:
      conditional area certificate from 647
      still needs local square-loss bounds for f(a,b)
    CE1/CE2:
      certificate-producing set-cover strategy from 616
      CE2 uses must state whether the CE2 one-interval lemma is assumed
```

The rest of this file makes the three $N_+$ branches explicit.

## Branch $N_+=0$

This branch separates the no-boundary-overlap CE0 case from the CE1/CE2
boundary-loss package.

### CE0 perimeter branch

In CE0, the center role $T_C$ has no positive-length overlap with
$\partial H$.  Thus the perimeter of $H$ must be covered by the six vertex
roles.

For each vertex role, the row length $a_i+b_i$ is the perimeter length assigned
to $T_i$ at the two boundary edges adjacent to $V_i$.  If $N_+=0$, then

$$
a_i+b_i\le1 \qquad i=0,\dots,5.
$$

Therefore the total assigned vertex-perimeter length is at most

$$
\sum_{i=0}^5(a_i+b_i)\le6.
$$

The boundary has length $6$.  In the open-triangle formulation, equality gives
no slack for covering the full closed boundary by open unit triangles.  Thus the
CE0, $N_+=0$ branch is intended to close by this direct perimeter-length
obstruction.  A finished proof should state the boundary-handoff convention
precisely enough to separate equality, endpoint, and open-cover cases.

### CE1/CE2 boundary-loss branch

When $T_C$ has a positive-length boundary overlap, the broad desired reduction
is that the $N_+=0$ branch can be brought into the recorded all-Vd0
boundary-loss package, after removing already-covered $C$-intervals when
appropriate.  This broad reduction is not recorded as a proven theorem in this
repository.  The recorded proven local package is narrower.

The available result is the CE1/CE2 all-Vd0 boundary-loss package in
[`../550_CE_Vd0_boundary_loss/550_index.md`](../550_CE_Vd0_boundary_loss/550_index.md).
Under the package assumptions, it proves the local implication

$$
\mathrm{CE1/CE2}+\text{all six }T_i\text{ are Vd0}+N_+=0 \quad\Longrightarrow\quad \text{boundary-loss contradiction}.
$$

For CE2, this result still uses the CE2 one-interval reduction assumed in
[`../550_CE_Vd0_boundary_loss/551_setup_and_reduction.md`](../550_CE_Vd0_boundary_loss/551_setup_and_reduction.md).

The boundary-loss mechanism is as follows.  Normalize the active
$C$-boundary interval to

$$
T_C\cap e_{0,1}=[s,t], \qquad u=1-t, \qquad w=t-s>0.
$$

The adjacent maximal Vd0 contributions are

$$
B_5=B(s,1-\gamma_5), \qquad B_1=B(u,1-\gamma_1),
$$

and

$$
F=B_5+B_1.
$$

The branch analysis in `550`-`556` proves

$$
F<1.
$$

Then the remaining boundary portion assigned to $T_2,T_3,T_4$ has length
$4-F>3$, while non-supercriticality gives

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)\le3.
$$

This is the boundary-loss contradiction.

What remains open in the overall tree is any reduction that would justify
applying this local package to every $N_+=0$ branch not already satisfying the
recorded CE1/CE2 all-Vd0 assumptions.

## Branch $N_+=1$

This branch is intended to reduce to the May 25 five-point obstruction.  The
reduction from the full one-supercritical branch to the May 25 reduced slice
is a target, not a recorded proof.

After dihedral symmetry and relabeling, the reduced slice takes the unique
strict supercritical row to be $V_4$:

$$
a_4+b_4>1.
$$

Choose one boundary point on each edge,

$$
X_i=V_i+t_i(V_{i+1}-V_i), \qquad 0\le t_i\le1,
$$

and set

$$
b_i=t_i, \qquad a_i=1-t_{i-1}.
$$

Then

$$
a_i+b_i=1-t_{i-1}+t_i.
$$

The May 25 reduced slice is

$$
t_3=t_2,\qquad t_5=t_4,\qquad t_4>t_2,
$$

with

$$
t_0\le t_5,\qquad t_1\le t_0,\qquad t_2\le t_1.
$$

Equivalently, $V_4$ is the unique strict $AB$-union vertex, the neighboring
rows satisfy

$$
a_3+b_3=1,\qquad a_5+b_5=1,
$$

and the first three rows satisfy

$$
a_0+b_0\le1,\qquad a_1+b_1\le1,\qquad a_2+b_2\le1.
$$

For each $i$, define $R_i$ to be the set of points $P\in H$ such that some
closed unit equilateral triangle contains

$$
V_i,\qquad X_{i-1},\qquad X_i,\qquad P.
$$

The strict $a+b>1$ $AB$-union frontier consists of two unit-circle arcs and two
line segments; the exact formula is recorded in
[`../300_vertex_triangle/309_ab_union_curve_a_plus_b_gt_1.md`](../300_vertex_triangle/309_ab_union_curve_a_plus_b_gt_1.md).

Let

$$
U=H\setminus\bigcup_{i=0}^5R_i.
$$

Let $P_3$ be the selected non-axis intersection between the non-axis boundary
of $R_4$ and the radius-$1$ circle centered at $X_2$.  Let $P_5$ be the
selected non-axis intersection between the non-axis boundary of $R_4$ and the
radius-$1$ circle centered at $X_5$.  In both cases the selected branch is the
valid non-axis branch closest to $V_4$.

If $O\notin U$, the five-point configuration is undefined.  Otherwise, for
$j=0,1,2$, define

$$
\rho_j=\sup\{\rho\in[0,1]:\lambda V_j\in U\text{ for every }0\le\lambda<\rho\},
$$

and

$$
D_j=\rho_jV_j.
$$

Thus $D_j$ is the first endpoint of the initial uncovered interval on the
half-diagonal $[O,V_j]$.  If no region cuts the half-diagonal before $V_j$,
then $D_j=V_j$.  If a nonlocal region cuts the half-diagonal earlier, that
earlier cut defines $D_j$.

The five-point set is

$$
K_5=\{P_3,P_5,D_0,D_1,D_2\}.
$$

For a finite set $K\subset\mathbb R^2$, define

$$
h_K(n)=\max_{x\in K}n\cdot x.
$$

For an angle $\theta$, let

$$
n_k(\theta)=\left(\cos\left(\theta+\frac{2\pi k}{3}\right),\sin\left(\theta+\frac{2\pi k}{3}\right)\right), \qquad k=0,1,2.
$$

The side length of the smallest equilateral triangle with these outward
normal directions containing $K$ is

$$
L_K(\theta)=\frac{2}{\sqrt3}\sum_{k=0}^2h_K(n_k(\theta)).
$$

The optimized enclosing side length is

$$
\Lambda(K)=\inf_{\theta\in[0,2\pi/3)}L_K(\theta).
$$

The May 25 finite-point target is

$$
\Lambda(K_5)>1.
$$

Equivalently, no closed unit equilateral triangle contains all five points in
$K_5$.

The current proof obligations for this branch are:

1. Reduce every full one-supercritical branch to the May 25 slice, or split
   off the branches that do not reduce.
2. Prove branch realization for $P_3$ and $P_5$: existence on the intended
   active non-axis frontier piece, validity of all inequalities, and closest
   valid branch selection.
3. Prove diagonal endpoint realization for $D_0,D_1,D_2$ using the actual
   union of all six regions $R_i$.  A useful local ingredient is the proven
   neighboring-ray maximum formula in
   [`../300_vertex_triangle/310_neighbor_ray_max_c_formula.md`](../300_vertex_triangle/310_neighbor_ray_max_c_formula.md),
   but it does not by itself prove the global first-cut statement for $D_j$.
4. Prove $\Lambda(K_5)>1$ across every support-contact regime, or reduce it to
   a finite certified inequality list.
5. Separate tangent, endpoint, undefined, and boundary cases.

The recorded May 25 package is
[`../630_may25_five_point_conjecture/630_index.md`](../630_may25_five_point_conjecture/630_index.md).
Its target and obligations are recorded in
[`../630_may25_five_point_conjecture/632_five_point_target_and_obligations.md`](../630_may25_five_point_conjecture/632_five_point_target_and_obligations.md).

## Branch $N_+\ge2$

This branch splits by center type.

### CE0 area route

In CE0, choose one cut point on each edge:

$$
X_i=V_i+x_i(V_{i+1}-V_i), \qquad 0\le x_i\le1.
$$

The induced rows are

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Thus

$$
a_i+b_i=1-x_{i-1}+x_i.
$$

Let $f(a,b)$ be the normalized maximum area inside $H$ for a unit vertex
triangle forced to contain the corresponding local boundary data.  The CE0
area target is

$$
N_+\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5f(a_i,b_i)<5.
$$

If this strict inequality is proved under the correct CE0 hypotheses, then
the six vertex triangles contribute less than five unit-triangle areas inside
$H$, while $T_C$ contributes at most one unit-triangle area.  The total
contribution is then less than the area of $H$, contradicting a cover.

The current recorded analytic result is conditional.  The file
[`../640_area_conjecture/647_CE0_conditional_area_certificate.md`](../640_area_conjecture/647_CE0_conditional_area_certificate.md)
proves the stronger bound

$$
N_+\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5f(a_i,b_i)<\frac{99}{20}<5
$$

under the local square-loss hypotheses

$$
a+b\le1 \quad\Longrightarrow\quad f(a,b)\le1-\min(a,b)^2,
$$

and

$$
a+b>1 \quad\Longrightarrow\quad f(a,b)\le1-\max(a,b)^2.
$$

Those local square-loss bounds remain open proof obligations.  Therefore the
CE0 $N_+\ge2$ branch is conditionally closed by `647`, not unconditionally
closed.

### CE1 and CE2 set-cover route

For CE1, the center triangle has one positive-length boundary interval.  For
CE2, the current reduced model assumes the CE2 one-interval lemma: one of the
two CE2 boundary intervals is already covered by adjacent vertex triangles, so
the remaining active interval can be treated by a seven-point perimeter model.

The CE1/reduced-CE2 two-supercritical strategy is recorded in
[`../600_case_strategies/616_CE1_CE2_two_supercritical_set_cover_strategy.md`](../600_case_strategies/616_CE1_CE2_two_supercritical_set_cover_strategy.md).
It proposes a certificate-producing finite set-cover route for

$$
T_C\text{ is CE1 or CE2}, \qquad N_+\ge2.
$$

The intended certificate chooses a finite test set

$$
Q\subset S_{1/2}
$$

and enumerates admissible masks for one center-triangle role and six
vertex-triangle roles, subject to

$$
N_+\ge2.
$$

An infeasible finite set-cover instance becomes proof-level only after adding:

1. exact or interval-certified coverage masks for every point of $Q$;
2. a dominance certificate showing that the finite candidate list dominates
   the relevant continuous triangle families;
3. a set-cover infeasibility certificate;
4. separate treatment of equality cases $a_i+b_i=1$ and boundary
   degeneracies;
5. an explicit statement of whether CE2 assumes the CE2 one-interval lemma.

Until such a certificate is supplied, this branch remains a strategy.

## Dependency summary

The current tree has the following recorded statuses.

| Branch or dependency | Source | Recorded status |
|---|---|---|
| Open/closed/scaled equivalence | [`../100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`](../100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md) | Proven |
| CE0 + Vd1/Vd2 half-skeleton obstruction | [`../600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md`](../600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md) | Proven |
| CE1/CE2 all-Vd0 boundary-loss package | [`../550_CE_Vd0_boundary_loss/550_index.md`](../550_CE_Vd0_boundary_loss/550_index.md) | Proven local lemma |
| CE2 one-interval lemma | [`../500_half_skeleton_lemmas/504_CE2_one_interval_lemma.md`](../500_half_skeleton_lemmas/504_CE2_one_interval_lemma.md) | Target lemma |
| Neighboring-ray maximum formula | [`../300_vertex_triangle/310_neighbor_ray_max_c_formula.md`](../300_vertex_triangle/310_neighbor_ray_max_c_formula.md) | Proven local lemma |
| May 25 five-point inequality $\Lambda(K_5)>1$ | [`../630_may25_five_point_conjecture/632_five_point_target_and_obligations.md`](../630_may25_five_point_conjecture/632_five_point_target_and_obligations.md) | Lemma target |
| CE0 two-supercritical final inequality under square-loss bounds | [`../640_area_conjecture/647_CE0_conditional_area_certificate.md`](../640_area_conjecture/647_CE0_conditional_area_certificate.md) | Proven analytic inequality, conditional |
| Local square-loss bounds for $f(a,b)$ | [`../640_area_conjecture/641_area_function_and_monotonicity.md`](../640_area_conjecture/641_area_function_and_monotonicity.md) | Lemma target / strategy |
| CE1/CE2 two-supercritical set-cover certificate | [`../600_case_strategies/616_CE1_CE2_two_supercritical_set_cover_strategy.md`](../600_case_strategies/616_CE1_CE2_two_supercritical_set_cover_strategy.md) | Strategy |

## Remaining global proof obligations

To turn this strategy tree into a proof of the main theorem, the following
gaps must be closed without weakening the stated hypotheses.

1. Complete or replace the broad CE1/CE2 $N_+=0$ reduction outside the recorded
   all-Vd0 boundary-loss package, and write the CE0 perimeter-handoff argument
   with endpoint and open-cover cases separated.
2. Prove the full reduction from every $N_+=1$ branch to the May 25 reduced
   slice, or add the missing sibling branches.
3. Prove the May 25 branch-realization, diagonal-endpoint, and enclosing
   triangle obligations.
4. Prove or certify the local square-loss bounds for $f(a,b)$ needed by the
   CE0 area certificate.
5. Supply a proof-level CE1/CE2 $N_+\ge2$ certificate, with CE2 one-interval
   assumptions stated explicitly.
6. Preserve the distinction between half-skeleton obstructions and full
   hexagon noncoverage whenever a branch uses $S_{1/2}$.
