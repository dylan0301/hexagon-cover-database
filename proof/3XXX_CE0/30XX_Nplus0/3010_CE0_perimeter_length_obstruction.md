# CE0 Perimeter-Length Obstruction

Status: Proven

Assume a hypothetical open-triangle cover has original roles

$$
U_C,U_0,\dots,U_5,
$$

with indices taken modulo $6$, and put $T_C=\overline{U_C}$ and
$T_i=\overline{U_i}$. Suppose

$$
T_C\text{ is CE0}
$$

and

$$
N_+=\left\lvert \left\lbrace i : A_i+B_i>1 \right\rbrace \right\rvert=0.
$$

Then the cover cannot exist.

## Proof

Because $T_C$ is CE0, the six open V roles cover $\partial H$. Indeed, a
boundary point missed by those roles cannot be a vertex, and the hypothetical
cover would place it in $U_C$. Openness would then give a positive-length
center trace on its boundary edge, contrary to CE0.

The six V roles are therefore boundary-complete. Item 1 of the
boundary-complete corollary in
[`2500`](../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md#boundary-complete-zero-gap-consequences)
excludes $N_+=0$. Hence this branch is impossible. $\square$
