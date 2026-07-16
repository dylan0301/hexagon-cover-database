# T3-Like Area Package

Status: Proven

This folder proves the CE0 branch with exactly one supercritical vertex row,
at least one T3-like vertex row, and no Vd1/Vd2 rows.

The branch assumptions are:

$$
T_C\text{ is CE0},
$$

$$
\left\lvert
\left\lbrace
i:A_i+B_i>1
\right\rbrace
\right\rvert=1,
$$

and every vertex row is Vd0 or T3-like, with at least one T3-like row.
Here $A_i,B_i$ are the actual maximal boundary reaches used in the definition
of $N_+$.

No midpoint condition is imposed on T3-like rows.  The T3-like hypothesis means

$$
(o,n)=(2,1).
$$

## Proof route

The original coordinatewise tangent-envelope conjecture is false.  Its exact
counterexample and failure analysis are recorded in
[`3172_full_T3_like_tangent_envelope_conjecture.md`](3172_full_T3_like_tangent_envelope_conjecture.md)
(Status: Failed).

The branch is instead closed by two unconditional area results:

1. The strict boundary-handoff theorem
   [`../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md`](../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
   selects lower-bound demands
   $$
   (a_i,b_i)=(1-x_{i-1},x_i)
   $$
   realized by the actual triangles and proves that their unique selected
   supercritical index is the unique actual one.
2. [`../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md`](../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md)
   proves for every local row
   $$
   G\ge\min(a,b)^2,
   $$
   and for every supercritical row
   $$
   G\ge\max(a,b)^2.
   $$
3. [`3175_direct_T3_like_area_loss.md`](3175_direct_T3_like_area_loss.md)
   proves directly that T3-like rows are nonsupercritical and that
   $$
   a,b\ge m
   \quad\Longrightarrow\quad
   G_{\mathrm{T3}}(a,b)\ge2m-4m^2.
   $$

The global assembly in
[`3174_CE0_one_supercritical_T3_certificate.md`](3174_CE0_one_supercritical_T3_certificate.md)
then proves

$$
\boxed{
\sum_{i=0}^5G_i>1.
}
$$

Therefore the six vertex triangles contribute less than five normalized
unit-triangle areas inside $H$.  A CE0 center triangle contributes at most one,
so the seven triangles contribute less than the normalized area $6$ of $H$.

## Files

| File | Recorded status | Notes |
|---|---|---|
| [`3172_full_T3_like_tangent_envelope_conjecture.md`](3172_full_T3_like_tangent_envelope_conjecture.md) | Failed | Gives an exact T3-like counterexample to coordinatewise tangent domination and records why that route fails. |
| [`3173_T3_like_loss_from_envelope.md`](3173_T3_like_loss_from_envelope.md) | Proven | Retains correct one-dimensional tangent-branch algebra and the conditional consequences of the failed envelope assumption; it is not used in the final proof. |
| [`3174_CE0_one_supercritical_T3_certificate.md`](3174_CE0_one_supercritical_T3_certificate.md) | Proven | Unconditional global CE0 one-supercritical assembly. |
| [`3175_direct_T3_like_area_loss.md`](3175_direct_T3_like_area_loss.md) | Proven | Direct orientation reduction and T3-like area-loss theorem replacing the failed envelope. |

## Conclusion

The `317X` branch is closed unconditionally.  The failed tangent-envelope
domination statement is retained as a warning, but no final dependency uses it.
