# Universal Real-Variable Strategy 2 Registry

Status: Proven

This source records the quantifier boundary for the scalar Strategy 2
problems.  The registered domains contain only real variables, explicit
radicals and rational functions, finite order cells, and objective signs.
The geometry-to-parameter bridge is used only after these universal statements
have been proved.

## Statement

Let the domains and objectives S2-E1, S2-E2, S2-R1, S2-R2, S2-T3, S2-SC,
and S2-VD be those defined in the manuscript's pure optimization appendix.
Then each required objective inequality holds for **every** point in its
stated real domain.

Equivalently, the theorem owners are:

- `thm:s2-pure-e1` and `thm:s2-pure-e2`;
- `thm:s2-pure-r1` and `thm:s2-pure-r2`;
- `thm:s2-pure-t3`;
- `thm:s2-pure-sc`;
- `thm:s2-pure-vd-adjacent` and `thm:s2-pure-vd-nonadjacent`.

## Proof decomposition

### Endpoint problems

S2-E1 is exactly the universal one-side capped-loss theorem
[`2107`](2107_one_side_capped_loss.md) after the substitutions

$$
 s=\frac{k}{r},\qquad u=r-d,\qquad
 \omega=w+d-\frac{k}{r},
$$

and the identity

$$
 u-\frac{r}{1+e}-\frac{r}{w}\omega=\frac{a}{w}.
$$

S2-E2 is the universal paired-endpoint calculation of
[`2108`](2108_CE2_two_endpoint_capped_loss.md).  Its two strict kernel
inequalities are respectively equivalent to

$$
 \Delta_L>0,\qquad \Delta_R>0.
$$

### Returned-demand problems

S2-R1 is the scalar inequality proved in
[`4106`](../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md).
S2-R2 is the scalar inequality proved in
[`4107`](../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4107_CE2_one_gap_five_map_completion.md).
The forward and reverse three-map statements are equivalent by exact capped
reflection duality.  The actual handoff argument belongs to
[`4105`](../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4105_CE1_CE2_one_gap_five_V_triangle_interface.md)
and is not used to prove the pure inequalities.

### T3 endpoint problem

The finite-cell theorem is recorded separately in
[`407e`](../../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407e_pure_finite_cell_theorem.md).
It proves the four-label inequality on the full explicit cell union, not only
on geometrically realized inputs.

### Rescuer and Vd problems

The two rescuer domains are the rational-radical source cells extracted from
[`2018`](../20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md).
The proof on each cell is purely algebraic.

The adjacent and nonadjacent Vd problems use the exact corner graph formulas
from [`2014`](../20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
and the radial margin calculations of
[`201c`](../20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md).
The nonadjacent domain explicitly includes the two center endpoint-distance
inequalities needed to prove the quarter-separation estimates.  Hence no
placement-defined supremum or unlisted geometric premise remains.

## Logical use

For every geometric branch, the bridge proves only

$$
 \text{geometric state}\Longrightarrow\text{membership in a registered domain}
$$

and the exact identity between the geometric terminal quantity and the
registered objective.  The universal theorem above then supplies the sign.
No converse realization statement is required.
