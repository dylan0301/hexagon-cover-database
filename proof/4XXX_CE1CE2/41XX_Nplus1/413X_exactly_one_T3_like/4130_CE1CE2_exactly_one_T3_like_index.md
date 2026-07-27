# CE1/CE2, $N_+=1$, Exactly One T3-Like Row

Status: Proven

This branch is closed by one midpoint reduction, one rationalized local
T3-like inequality, and the class-independent adjacent-rescuer theorem.

## Common $g$-chain signature

The raw and relaxed transfer notation is proved in
[`201d`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md).
After reflection, the midpoint reduction places the T3-like rescuer at $T_0$
and the unique supercritical row at $T_1$.

Let $c$ be the radial demand forced on $T_1$.  The free envelope of the raw
$g_c$ graph gives

$$
b_1<B_{\rm sc}(c),
\qquad
a_2>A_{\rm sc}(c).
$$

Thus the source transfer is

$$
\mathsf S_c=A_{\rm sc}(c).
$$

Rows $T_2,T_3,T_4$ are ordinary nonsupercritical rows and are relaxed to
$\mathrm I^3$.  Hence

$$
a_5>A_{\rm sc}(c).
$$

The terminal nonsupercritical cap at $T_5$ gives

$$
b_5\le1-a_5<B_{\rm sc}(c).
$$

On the other hand, the two local rescuer inequalities and the common
center-hiding theorem force the far-side requirement

$$
h\ge B_{\rm sc}(c).
$$

Therefore $b_5<h$, a contradiction.  The common signature is

$$
\boxed{
\mathscr C\!\left[
A_{\rm sc}(c);\,
\mathrm I^3;\,
b_5<B_{\rm sc}(c)\le h
\right].
}
$$

The T3-like-specific calculation does not change the chain.  Its only role is
to verify

$$
a\le A_{\rm sc}(c),
\qquad
\frac{a}{a+1-u}\le A_{\rm sc}(c),
$$

which makes the common far-side envelope applicable.  The Vd1 rescue branch
`4143` has exactly the same chain and differs only in this local verification.

## Files

| File | Recorded status | Role |
|---|---|---|
| [`4131_midpoint_forcing_reduction.md`](4131_midpoint_forcing_reduction.md) | Proven | Proves the midpoint-forcing reduction: after normalizing $T_C\cap\{M_0,\dots,M_5\}=\{M_0\}$, the unique T3-like row is $T_0$, it may be reflected so that $M_1\in T_0$, and the unique supercritical row is $T_1$. |
| [`4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md`](4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md) | Proven | Rationalizes the translated T3-like normal form, proves the two local rescuer inequalities, and invokes the common adjacent-rescuer theorem. |
| [`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md) | Proven | Supplies the center-hiding argument, the free $g_c$-envelope comparison, and the terminal boundary-chain contradiction shared with the Vd1 rescue branch. |

## Result

Under the standing reductions excluding the Vd1/Vd2 branches and the
at-least-two-T3-like branch, the CE1/CE2, $N_+=1$, exactly-one-T3-like branch
cannot cover the hexagon perimeter.
