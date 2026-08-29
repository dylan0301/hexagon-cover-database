# CE1/CE2 Branch

Status: Reference

The common signed center form is
[`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).
One normalized trace has positive surplus $\Delta_R$; the sign of
$\Delta_L$ distinguishes CE1 from CE2. The active proof has three strategies:
trace length, area loss, and direct finite enclosure.

## 1. Direct finite-enclosure entry

For selected boundary reaches $(a_i,b_i)$, the exact own-ray capacity is
$c_{\max}(a_i,b_i)$. If an adjacent role is actually permitted to have
positive support on $r_i$, its exact capacity is $C_+$ or $C_-$. The type-aware
maximum is $\Gamma_i$, and

$$
D_i=(1-\Gamma_i)V_i
$$

is missed by every open V role. This theorem, the support gauge, the
complementary-gap theorem, and the CE2 short-ray theorem are proved in
[`2608`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md).

No active proof composes boundary-transfer maps.

## 2. Nonzero-gap terminals

| Active package | Branch | Direct terminal | Status |
|---|---|---|---|
| [`4013_new`](40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) | $N_+=0$, all Vd0 | complementary-gap disk or CE2 short ray | Proven |
| [`4070_new`](40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) | $N_+=0$, one or two T3-like roles | type-aware neighboring support followed by the same gap terminal | Proven |
| [`4101_new`](41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md), [`4102_new`](41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md) | $N_+=1$, all Vd0 | anisotropic radial endpoints; direct CE1 reverse path or CE2 threshold dichotomy | Proven |
| [`4130_new`](41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) | $N_+=1$, exactly one T3-like role | O-side T3 endpoint and direct path budget | Proven |
| [`4140_new`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md) | CE2, $N_+=1$, exactly one Vd1/Vd2 role | radial separation, Vd1 endpoint, length deficit, or replacement to `4013_new` | Proven |

## 3. Trace-length terminals

The shorter Strategy 1 closures remain:

- `4040`, `4041`: $N_+=0$ with a Vd1/Vd2 role;
- `4110`, `4111`: CE1 one-Vd and CE2 at-least-two-Vd cases;
- `4123`: at least two T3-like roles;
- `4149`: Vd2 neighboring-midpoint perimeter deficit;
- `414a`: additional positive-support skeleton deficit;
- `4200`: $N_+\ge2$ skeleton deficit.

## 4. One-Vd placement partition

The structural placement audit remains in the established `414X` sources.
Its active mathematical endings are proved in `4140_new`. The corrected
two-chart replacement `4147` recomputes the output gap count: zero goes to
Strategy 1, one gap goes to the complementary-gap theorem, and two gaps go to
the CE2 short-ray theorem.

## 5. Provenance

The old endpoint-propagation packages remain in the corpus with their recorded
statuses as historical alternative proofs. The authenticated `407X` blobs and
the pinned scalar statement project remain verification interfaces, not active
case dependencies. Failed finite-point and unconditional-skeleton routes remain
in `9XXX_failed_ideas`.
