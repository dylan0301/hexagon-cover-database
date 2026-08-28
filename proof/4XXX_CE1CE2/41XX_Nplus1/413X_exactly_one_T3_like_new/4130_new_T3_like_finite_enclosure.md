# CE1/CE2, $N_+=1$, Exactly One T3-Like: Finite-Enclosure Form

Status: Proven

## Theorem

Assume:

1. exactly one actual V role is supercritical;
2. exactly one V role is T3-like;
3. no V role is Vd1 or Vd2;
4. the V roles leave at least one boundary gap.

Put

$$
R=H\setminus\bigcup_{i=0}^5U_i
$$

and

$$
K_{413}=\mathrm{vert}(\mathrm{conv}R).
$$

Then

$$
\boxed{\Lambda(K_{413})\ge1.}
$$

Consequently no open unit C triangle completes these V roles to a cover of
$H$.

## Proof

The residual contains $O$ and a boundary-gap point, so any open unit triangle
containing it is CE1 or CE2.  If $\Lambda(K_{413})<1$, Theorem
[`2608`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
would produce an open unit CE1/CE2 C role containing the residual.

This would give a cover in the branch excluded by the proved exactly-one
T3-like package
[`4130`](../413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md).
That proof supplies the midpoint reduction, the exact T3-like local profile,
and the adjacent-rescuer terminal.  Hence $\Lambda(K_{413})\ge1$.  $\square$

## Proof ownership

The adjacent-rescuer inequality is retained as the local noncontainment
certificate for $K_{413}$.  The branch is now routed through one finite set
forced into the C role.
