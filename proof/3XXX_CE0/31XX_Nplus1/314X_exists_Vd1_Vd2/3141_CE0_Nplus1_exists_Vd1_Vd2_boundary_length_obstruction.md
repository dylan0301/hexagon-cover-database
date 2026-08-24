# CE0, $N_+=1$, Exists Vd1/Vd2 Boundary-Length Obstruction

Status: Proven

Assume a hypothetical seven-open-unit-triangle cover has original roles

$$
U_C,U_0,\dots,U_5,
$$

and put $T_C=\overline{U_C}$ and $T_i=\overline{U_i}$. Assume

$$
T_C\text{ is CE0},
$$

$$
N_+=\left\lvert \left\lbrace i : A_i+B_i>1 \right\rbrace \right\rvert=1,
$$

and at least one $V_i$-triangle is Vd1 or Vd2.

This branch is obstructed by boundary length.

## Proof

Because $T_C$ is CE0, the six open V roles cover $\partial H$. Indeed, a
boundary point missed by those roles cannot be a vertex, and the hypothetical
cover would place it in $U_C$. Openness would then give a positive-length
center trace on its boundary edge, contrary to CE0.

The six V roles are therefore boundary-complete. Item 2 of the
boundary-complete corollary in
[`2500`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md#boundary-complete-zero-gap-consequences)
excludes $N_+=1$ with a Vd1/Vd2 role. Hence this branch is impossible.
$\square$
