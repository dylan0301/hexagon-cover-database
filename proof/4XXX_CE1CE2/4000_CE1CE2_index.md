# CE1/CE2 Branch

Status: Reference

This branch records CE1 and CE2 together.  Their common center geometry is the
signed normal form
[`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):
one normalized trace has surplus $\Delta_R>0$, while the sign of the companion
surplus $\Delta_L$ distinguishes CE1 from CE2.  All six center exits,
perimeter budgets, skeleton budgets, and local reach certificates are shared.

Every terminal branch below is proven.  Their exhaustive assembly is
[`0000`](../0XXX_main/0000_main_theorem.md).

## Three-strategy routing

The active proof has three global strategies.

1. **Trace length.**  Perimeter, radial, or skeleton contributions have strict
   total deficit.
2. **Area loss.**  Local exterior losses sum beyond the available normalized
   area.
3. **Finite enclosure.**  A finite subset of the residual left by the six V
   roles is forced into the C role, but its least enclosing equilateral
   triangle has side at least one.

The exact functions

$$
M_c(a),\qquad \overline M_c(a),\qquad \Phi_c(a)
$$

remain the canonical local reach calculus proved in
[`201d`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md).
They certify noncontainment of the nonzero-gap finite residuals; they do not
own a separate strategy.

The common logical conversion is the residual-hull principle
[`2608`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md).
For fixed V roles, let

$$
R=H\setminus\bigcup_{i=0}^5U_i,
\qquad
K_R=\mathrm{vert}(\mathrm{conv}R).
$$

If the relevant CE1/CE2 completion theorem excludes every unit C triangle
covering $R$, then $\Lambda(K_R)\ge1$.

## Nonzero-gap finite-enclosure terminals

| Active package | Recorded status | Branch | Exact certificate retained |
|---|---|---|---|
| [`4013_new`](40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) | Proven | $N_+=0$, all Vd0 | original `4013`, `2107`, `2108`, `2110` |
| [`4070_new`](40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) | Proven | $N_+=0$, one or two T3-like, no Vd1/Vd2 | authenticated `407X` four-label package |
| [`4101_new`](41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md) | Proven | $N_+=1$, all Vd0 | `4105`, `4106`, `4107`, paired two-gap certificate |
| [`4130_new`](41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) | Proven | $N_+=1$, exactly one T3-like | `4131`, `4132`, `2018` |
| [`4140_new`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md) | Proven | $N_+=1$, exactly one Vd1/Vd2 | CE1 length terminal and complete `414X` placement package |

A nonzero boundary gap forces any residual-containing unit C triangle to be
CE1 or CE2.  Singleton gaps remain included because the candidate C triangle
is open.

## Trace-length terminals retained

The following branches remain shorter under Strategy 1:

- `4040`, `4041`: $N_+=0$ with a Vd1/Vd2 role;
- `4110`, `4111`: CE1 one-Vd and CE2 at-least-two-Vd branches;
- `4123`: at least two T3-like roles;
- `4149`: Vd2 neighboring-midpoint perimeter terminal;
- `414a`: additional positive-support skeleton terminal;
- `4200`: $N_+\ge2$ skeleton terminal.

## Detailed one-Vd placement pointer

The original zero-gap state is first closed by Strategy 1.  For positive gap
rank, the proved placement partition remains in
[`4140`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md),
with assembly `4148` and audit `414b`.  The active branch wrapper is
[`4140_new`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md).

The corrected two-chart replacement `4147` does not preserve gap rank.  Its
output rank is recomputed.  Rank zero uses Strategy 1; positive rank uses
`4013_new`.

## Provenance and cautions

- The original reach packages remain in place with their recorded statuses.
- The authenticated `407X` files retain their exact bytes and notation
  crosswalk.
- The May 25 five-point route remains failed and is not revived.
- The new finite witness is the complete residual-hull vertex set, so no
  unproved claim about a smaller ad hoc point selection is required.
