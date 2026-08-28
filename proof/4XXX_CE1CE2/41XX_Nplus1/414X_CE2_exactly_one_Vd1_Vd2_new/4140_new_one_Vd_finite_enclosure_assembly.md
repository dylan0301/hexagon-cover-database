# $N_+=1$, Exactly One Vd1/Vd2: Finite-Enclosure Assembly

Status: Proven

## Theorem

Assume exactly one actual V role is supercritical, exactly one V role is Vd1
or Vd2, no additional T3-like role survives the common high-count pruning,
and the V roles leave at least one boundary gap.  Put

$$
R=H\setminus\bigcup_{i=0}^5U_i
$$

and

$$
K_{414}=\mathrm{vert}(\mathrm{conv}R).
$$

Then

$$
\boxed{\Lambda(K_{414})\ge1.}
$$

Consequently no open unit C triangle completes these V roles to a cover of
$H$.

## Proof

The residual contains $O$ and a boundary-gap point.  Therefore an open unit
triangle containing it is CE1 or CE2.

Suppose $\Lambda(K_{414})<1$.  The residual-hull principle
[`2608`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
produces an open unit C role containing the residual.

If this C role is CE1, the resulting cover is excluded by the CE1
boundary-length obstruction
[`4110`](../411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md).
If it is CE2, it is excluded by the complete placement assembly
[`4140`](../414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md),
including the adjacent and nonadjacent radial terminals, the Vd2 perimeter
terminal, and the corrected two-chart replacement.  These two center classes
are exhaustive in the presence of a boundary gap.  Thus
$\Lambda(K_{414})\ge1$.  $\square$

## Replacement subcase

When the two-chart theorem `4147` replaces the distinguished adjacent pair by
six nonsupercritical Vd0 roles, its output gap rank is recomputed.  Output rank
zero uses the existing boundary-complete length theorem.  Positive output
rank is routed to the new finite-enclosure terminal
[`4013_new`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md).
No preservation of the input gap rank is asserted.

## Proof ownership

The placement lemmas in the original `414X` package remain exact local
certificates.  The branch-level terminal is now the finite residual witness
$K_{414}$, with Strategy 1 retained for the already shorter perimeter and
skeleton subcases.
