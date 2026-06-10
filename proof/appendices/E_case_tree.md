# Overall Proof Tree For Hexagon Noncoverability

Status: Strategy

This file records the current proof tree for the seven-triangle
noncoverability theorem. It follows the structure in the root prompt
`prompts/20260610prooftreeSketch.txt` as imported into the root `proof/`
corpus. It is not a completed proof of the main theorem.

Each branch keeps its recorded proof status: proven local packages are cited as
such, while reductions, certificates, and inequalities not yet proved remain
targets or strategies.

## Main target

The theorem target is:

$$
\text{The side-}1\text{ hexagon }H\text{ cannot be covered by seven open unit equilateral triangles.}
$$

The equivalent expanded closed formulation is:

$$
\text{For every }L>1,\ H_L\text{ cannot be covered by seven closed unit equilateral triangles.}
$$

The equivalence is proved in
[`../100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`](../100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md).

The skeleton caveat remains in force: standalone noncoverage of $S$ is refuted
by the May 24 numerical counterexample in
[`../800_computation/811_skeleton_cover_counterexample.md`](../800_computation/811_skeleton_cover_counterexample.md).

## Primary split

Under a hypothetical cover, choose role triangles

$$
T_C,T_0,\dots,T_5.
$$

Here $T_C$ contains $O$, and each $T_i$ contains $V_i$. Classify $T_C$ as
CE0, CE1, or CE2, define the vertex rows $(a_i,b_i)$, and compute

$$
N_+=\#\{i:a_i+b_i>1\}.
$$

The current proof tree splits first by $N_+$:

```text
Hypothetical seven-triangle cover
  classify T_C as CE0, CE1, or CE2
  define perimeter rows (a_i,b_i)
  compute N_+ = #{i : a_i+b_i > 1}

  N_+ = 0
  N_+ = 1
  N_+ >= 2
```

The CE0/CE1/CE2 cases are subbranches inside this $N_+$ split.

## Branch $N_+=0$

Source folder:

- [`../100_Nplus0/100_index.md`](../100_Nplus0/100_index.md)

The branch assumptions are:

$$
a_i+b_i\le1 \qquad i=0,\dots,5.
$$

### CE0

If $T_C$ is CE0, then $T_C$ contributes no positive-length boundary interval.
The intended proof is a direct perimeter-length obstruction:

$$
\sum_{i=0}^5(a_i+b_i)\le6,
$$

while $\partial H$ has length $6$. The remaining task is to write the
boundary-handoff proof with equality, endpoint, and open-cover cases separated.

Status source:

- [`../100_Nplus0/110_CE0_perimeter_length_obstruction.md`](../100_Nplus0/110_CE0_perimeter_length_obstruction.md)

### CE1/CE2

The recorded closed branch is:

$$
\mathrm{CE1/CE2}+\text{all six }T_i\text{ are Vd0}+N_+=0
\quad\Longrightarrow\quad \text{boundary-loss contradiction}.
$$

This is proved under the assumptions of
[`../550_CE_Vd0_boundary_loss/551_setup_and_reduction.md`](../550_CE_Vd0_boundary_loss/551_setup_and_reduction.md).
For CE2, the package still uses the CE2 one-interval reduction assumed there.

Status sources:

- [`../100_Nplus0/120_CE1_CE2_boundary_loss_package.md`](../100_Nplus0/120_CE1_CE2_boundary_loss_package.md)
- [`../550_CE_Vd0_boundary_loss/550_index.md`](../550_CE_Vd0_boundary_loss/550_index.md)
- [`../550_CE_Vd0_boundary_loss/556_lower_sheet_completion_proofs.md`](../550_CE_Vd0_boundary_loss/556_lower_sheet_completion_proofs.md)

Remaining reductions:

- justify all-Vd0 when applying the package;
- handle active-interval assumptions;
- keep CE2 one-interval uses explicit.

## Branch $N_+=1$

Source folder:

- [`../200_Nplus1/200_index.md`](../200_Nplus1/200_index.md)

The branch assumes exactly one supercritical row.

### CE0 + Vd1/Vd2

The branch

$$
T_C\text{ is CE0 and at least one }T_i\text{ is Vd1 or Vd2}
$$

is already recorded as a proven half-skeleton obstruction.

Status source:

- [`../200_Nplus1/210_CE0_Vd1_Vd2_obstruction/210_index.md`](../200_Nplus1/210_CE0_Vd1_Vd2_obstruction/210_index.md)
- [`../600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md`](../600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md)

### CE0 + one T3-like row + no Vd1/Vd2

The current preferred route is the conditional area certificate, not the older
bipartite or diagonal-point maximality route.

Status source:

- [`../200_Nplus1/220_CE0_one_T3_like_area_certificate/220_index.md`](../200_Nplus1/220_CE0_one_T3_like_area_certificate/220_index.md)
- [`../650_area_conjecture_T3_like/653_CE0_one_supercritical_T3_certificate.md`](../650_area_conjecture_T3_like/653_CE0_one_supercritical_T3_certificate.md)

This branch remains conditional on the local Vd0 square-loss bounds and the
full T3-like tangent-envelope conjecture.

### CE0 + all Vd0

The current sketch points to the algorithm-2 five-point route.

Normalize the unique supercritical row to $V_4$. The outer parameters are
$a_4,b_4$ and the remaining free variables are $a_1,b_1$. The Vd0 reduction
uses the equalities

$$
a_3+b_3=1,\qquad a_5+b_5=1.
$$

Two fixed points come from the $V_4$ strict $AB$-union frontier and radius-$1$
circles. Algorithm 1, based on local diagonal max-$c$ points and a unimodality
claim, is recorded as failed because support patterns of the enclosing
triangle change.

Algorithm 2 uses three equality-pattern diagonal choices:

$$
a_1+b_1=1,\qquad a_2+b_2=1,
$$

$$
a_0+b_0=1,\qquad a_2+b_2=1,
$$

and

$$
a_0+b_0=1,\qquad a_1+b_1=1.
$$

For $a_4,b_4\in[0.1,0.9]$, the route is currently empirical/certificate
target. Outside that central box, the sketch says a limit-shape convexity
argument should be provable; in this corpus it remains a lemma target unless a
complete proof file is added.

Status source:

- [`../200_Nplus1/230_CE0_all_Vd0_algorithm2_five_point/230_index.md`](../200_Nplus1/230_CE0_all_Vd0_algorithm2_five_point/230_index.md)
- [`../500_finite_point_algorithms/520_algorithm2_diagonal_relaxation.md`](../500_finite_point_algorithms/520_algorithm2_diagonal_relaxation.md)

### CE1/CE2 subbranches

The sketch records length and midpoint routes for:

- CE1 with at least one Vd1/Vd2;
- CE2 with at least two Vd1/Vd2;
- CE2 with exactly one Vd1/Vd2;
- CE1/CE2 with at least two T3-like rows and no Vd1/Vd2;
- CE1/CE2 with exactly one T3-like row and no Vd1/Vd2.

The first two are intended boundary-length branches. The exactly-one Vd1/Vd2
and exactly-one T3-like branches likely need discrete $S_{1/2}$ set-cover
fallbacks. These remain strategies or lemma targets until the relevant length,
midpoint, and strictness arguments are recorded.

Status sources:

- [`../200_Nplus1/240_CE1_CE2_Vd1_Vd2_length_branches/240_index.md`](../200_Nplus1/240_CE1_CE2_Vd1_Vd2_length_branches/240_index.md)
- [`../200_Nplus1/250_CE1_CE2_T3_like_midpoint_branches/250_index.md`](../200_Nplus1/250_CE1_CE2_T3_like_midpoint_branches/250_index.md)

## Branch $N_+\ge2$

Source folder:

- [`../300_Nplus_ge2/300_index.md`](../300_Nplus_ge2/300_index.md)

### CE0

The conditional area certificate proves:

$$
N_+\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5 f(a_i,b_i)<\frac{99}{20}<5
$$

under local square-loss bounds for $f(a,b)$. The square-loss bounds remain open
proof obligations.

Status sources:

- [`../300_Nplus_ge2/310_CE0_area_certificate.md`](../300_Nplus_ge2/310_CE0_area_certificate.md)
- [`../640_area_conjecture/647_CE0_conditional_area_certificate.md`](../640_area_conjecture/647_CE0_conditional_area_certificate.md)

### CE1/CE2

The sketch proposes a skeleton-length route. The intended upper bounds are:

- CE1/CE2 center role: at most $3/2$;
- Vd0 with $a+b\le1$: at most $2$;
- Vd0 with $a+b>1$: at most $3/2$;
- Vd1/Vd2: at most $3/2$;
- T3-like: at most $3/2$.

The full skeleton has total length $12$. The proposed route needs strictness:
the naive sum

$$
2+2+2+\frac32+\frac32+\frac32+\frac32=12
$$

is only an upper-bound equality, so a proof must explain why equality cannot
occur under the branch hypotheses.

Status source:

- [`../300_Nplus_ge2/320_CE1_CE2_skeleton_length_route.md`](../300_Nplus_ge2/320_CE1_CE2_skeleton_length_route.md)

The finite set-cover route remains a fallback:

- [`../300_Nplus_ge2/330_CE1_CE2_set_cover_fallback.md`](../300_Nplus_ge2/330_CE1_CE2_set_cover_fallback.md)
- [`../600_case_strategies/616_CE1_CE2_two_supercritical_set_cover_strategy.md`](../600_case_strategies/616_CE1_CE2_two_supercritical_set_cover_strategy.md)

## Remaining proof obligations

1. Finish the CE0, $N_+=0$ perimeter-handoff proof.
2. Complete or replace the CE1/CE2, $N_+=0$ reductions outside the recorded
   all-Vd0 boundary-loss package.
3. Complete the CE0 all-Vd0, $N_+=1$ algorithm-2 certificate package.
4. Prove or replace the May 25 five-point inequality where it remains used.
5. Prove the local square-loss bounds for the CE0 area certificates.
6. Prove the full T3-like tangent-envelope conjecture.
7. Prove CE1/CE2 skeleton-length bounds and strictness cases.
8. Supply set-cover certificates for the CE1/CE2 fallback branches.
