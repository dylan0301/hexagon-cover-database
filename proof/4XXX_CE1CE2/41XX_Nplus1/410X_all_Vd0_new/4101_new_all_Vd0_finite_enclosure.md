# CE1/CE2, $N_+=1$, All Vd0: Finite-Enclosure Form

Status: Proven

## Theorem

Let the six open V roles be Vd0 and suppose exactly one actual V role is
supercritical.  Assume the V roles leave at least one boundary gap.  Put

$$
R=H\setminus\bigcup_{i=0}^5U_i
$$

and

$$
K_{410}=\mathrm{vert}(\mathrm{conv}R).
$$

Then

$$
\boxed{\Lambda(K_{410})\ge1.}
$$

Consequently no open unit C triangle completes these V roles to a cover of
$H$.

## Proof

The residual contains $O$ and a boundary-gap point.  Hence every open unit
triangle containing the residual is CE1 or CE2.  If
$\Lambda(K_{410})<1$, the residual-hull principle
[`2608`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
would produce an open unit CE1/CE2 C triangle containing the whole residual.
Together with the fixed V roles it would cover $H$.

This is excluded by the exact all-Vd0 gap-closure theorem
[`4101`](../410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md).  Its one-gap
proof uses the common five-role admissibility interface and the CE1 or CE2
scalar certificate; its two-gap proof uses the paired endpoint theorem.
Therefore $\Lambda(K_{410})\ge1$.  $\square$

## Proof ownership

The local maps $M_c$, $\overline M_c$, and $\Phi_c$ remain useful inside the
certificate proving that no unit C triangle contains $K_{410}$.  They are no
longer presented as a fourth global strategy.
