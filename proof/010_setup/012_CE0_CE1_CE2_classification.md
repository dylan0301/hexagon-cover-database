# CE0/CE1/CE2 Classification

Status: Reference

For the center role $T_C$, define

$$
N_E(T_C)=\#\{i:T_C\cap e_{i,i+1}\text{ contains a positive-length interval}\}.
$$

The center-edge cases are:

$$
\mathrm{CE0}\iff N_E(T_C)=0,
$$

$$
\mathrm{CE1}\iff N_E(T_C)=1,
$$

and

$$
\mathrm{CE2}\iff N_E(T_C)=2.
$$

Point contacts, tangencies, and vertex-only contacts do not count as
positive-length edge overlaps.

The source definition and related center-triangle material are recorded in
[`200_center_triangle/201_CE_classification.md`](../200_center_triangle/201_CE_classification.md).
