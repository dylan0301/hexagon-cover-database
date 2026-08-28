# CE1/CE2, $N_+=0$, T3-Like: Finite-Enclosure Form

Status: Proven

## Theorem

Assume:

1. the six open V roles have $N_+=0$;
2. no V role is Vd1 or Vd2;
3. at least one V role is T3-like;
4. the V roles leave at least one boundary gap.

Put

$$
R=H\setminus\bigcup_{i=0}^5U_i
$$

and

$$
K_{407}=\mathrm{vert}(\mathrm{conv}R).
$$

Then

$$
\boxed{\Lambda(K_{407})\ge1.}
$$

Consequently no open unit C triangle completes these V roles to a cover of
$H$.

## Proof

The residual contains $O$ and a boundary-gap point, so every open unit
triangle containing it is CE1 or CE2.  If $\Lambda(K_{407})<1$, Theorem
[`2608`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
would produce an open unit CE1/CE2 C role covering the residual.

Together with the six fixed V roles this would give a hypothetical cover in
the branch excluded by the complete T3-like package
[`4070`](../407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md).
That package covers one or two T3-like roles and both possible nonzero gap
ranks.  Hence $\Lambda(K_{407})\ge1$.  $\square$

## Proof ownership

The authenticated four-label endpoint calculation remains unchanged and is
cited as the exact certificate for the finite-enclosure inequality.  The new
branch owner is the center-forced finite set $K_{407}$, not a separate
boundary-propagation strategy.
