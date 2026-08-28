# CE1/CE2, $N_+=0$, All Vd0: Finite-Enclosure Form

Status: Proven

## Theorem

Let

$$
U_0,\ldots,U_5
$$

be open unit V roles of type Vd0 with

$$
A_i+B_i\le1
\qquad(i=0,\ldots,5),
$$

and suppose their boundary traces leave at least one boundary gap.  Put

$$
R=H\setminus\bigcup_{i=0}^5U_i
$$

and let

$$
K_{401}=\mathrm{vert}(\mathrm{conv}R).
$$

Then

$$
\boxed{\Lambda(K_{401})\ge1.}
$$

Consequently no open unit C triangle completes the six V roles to a cover of
$H$.

## Proof

The residual contains $O$ and at least one boundary-gap point.  Therefore any
open unit equilateral triangle containing the residual is CE1 or CE2.  If
$\Lambda(K_{401})<1$, the residual-hull principle
[`2608`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
would produce an open unit CE1/CE2 C role that, together with the six fixed V
roles, covers $H$ and hence its full skeleton.

This is excluded by the proved all-Vd0 skeleton-data theorem
[`4013`](../401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md), whose
nonzero-gap parts cover both one-gap CE1/CE2 states and two-gap CE2 states.
Thus $\Lambda(K_{401})\ge1$.  The final assertion follows because a compact
subset of an open unit equilateral triangle has enclosure number strictly
below one.  $\square$

## Proof ownership

This file is the active nonzero-gap terminal.  The exact one-side and paired
endpoint calculations in the original `401X_all_Vd0_boundary_loss` package
remain the proof certificate for the finite-enclosure inequality; they no
longer define a separate top-level propagation strategy.
