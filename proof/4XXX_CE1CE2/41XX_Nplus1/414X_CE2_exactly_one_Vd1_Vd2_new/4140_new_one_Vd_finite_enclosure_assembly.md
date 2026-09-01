# CE2, $N_+=1$, Exactly One Vd1/Vd2: Simplified Placement Assembly

Status: Proven

This is the active finite-witness assembly for the exactly-one-Vd1/Vd2
branch. The exhaustive placement partition is the proved re-audit
[`414b`](../414X_CE2_exactly_one_Vd1_Vd2/414b_complete_placement_reaudit.md).
The simplifications are:

- the adjacent placement uses the one-third radial envelope from
  [`2609`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md);
- the Vd1 neighboring-midpoint placement uses the common rescuer-tail theorem
  from the same file;
- the nonadjacent, Vd2, and replacement placements retain their shorter
  one-point, perimeter, and rerouting terminals.

## Theorem

Assume the C triangle is CE2, $N_+=1$, exactly one V role is Vd1 or Vd2,
and at least one actual V-gap is present. Then the original open roles cannot
cover the hexagon skeleton.

Let $T_\sigma$ be the unique supercritical V role and $T_\tau$ the unique
Vd1/Vd2 role. They are distinct. If a further V role has positive adjacent
support, the common skeleton-length theorem gives the contradiction.
Therefore assume every other V role is Vd0.

## 1. $T_0$ supercritical and the Vd role adjacent

After reflection, let $\sigma=0$ and $\tau=1$. Let
$\rho_R,\rho_L$ be the two residual boundary reaches of the proved adjacent
placement. The exact residual calculation in
[`4144`](../414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md)
gives

$$
\rho_R+\rho_L<\frac12,
\qquad
4\delta<\rho_L.
\tag{1}
$$

The Vd supported-arm margin gives

$$
u_{1\to2}<1-\rho_L<1-\delta.
\tag{2}
$$

Boundary coverage at the ordinary role $T_2$ gives

$$
A_2>\frac12+\rho_R,
\qquad
B_2\ge\rho_L.
$$

Apply Theorem 3.1 of `2609` with

$$
M=\frac12+\rho_R,
\qquad
m=\rho_L.
$$

The hypotheses follow from (1): $M\ge1/2$, $0<m<M$, and $M+m<1$.
Coordinatewise antitonicity of $c_{\max}$ gives

$$
C_2
\le
c_{\max}(M,m)
<
1-\frac{\rho_L}{3}
<
1-\delta.
\tag{3}
$$

Equations (2)--(3) show that neither local V role reaches the C interval on
$r_2$, whose vertex-side entry is $1-\delta$. All other roles are excluded
by Vd0 locality and diameter. A point of $r_2$ is uncovered.

This improves the former coefficient $1/4$ to $1/3$; the already proved
residual estimate $4\delta<\rho_L$ is more than sufficient.

## 2. $T_0$ supercritical and the Vd role nonadjacent

Let $\tau\in\{2,3,4\}$. The exact calculation in
[`4146`](../414X_CE2_exactly_one_Vd1_Vd2/4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md)
gives

$$
\alpha+\delta<\min\{\rho_R,\rho_L\}.
$$

Every relevant C exit is at most $\alpha+\delta$, while the Vd own-radial
margin gives

$$
C_\tau<1-\min\{\rho_R,\rho_L\}.
$$

Therefore

$$
D_\tau=\min\{\rho_R,\rho_L\}V_\tau
$$

lies beyond both the Vd trace and the C trace. Its adjacent roles are Vd0,
and the nonlocal roles are excluded by diameter. Thus $D_\tau$ is uncovered.

## 3. The Vd role is $T_0$

Midpoint rescue forces $\sigma\in\{1,5\}$; reflect to $\sigma=1$.

If $T_0$ is Vd2, the neighboring-midpoint perimeter theorem cited in `414b`
gives the Method 1 contradiction.

Assume $T_0$ is Vd1. Write its supported interval on $r_1$ as

$$
[c,u],
\qquad
c\le\frac12\le u,
$$

and put

$$
P_{\rm Vd1}=(1-u)V_1,
\qquad
\varepsilon=1-u.
$$

The endpoint is missed by the open Vd1 role, by the adjacent supercritical
role, and by all Vd0 or nonlocal roles. Hence

$$
P_{\rm Vd1}\in U_C.
\tag{4}
$$

The exact Vd1 calculation in
[`4143`](../414X_CE2_exactly_one_Vd1_Vd2/4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md)
proves, with $M=M_c^{\rm sup}$,

$$
a\le1-M,
\qquad
\frac{a}{a+\varepsilon}\le1-M.
\tag{5}
$$

The Vd half-unit cap gives $a<1/2$, while $u\ge1/2$ gives
$\varepsilon\le1/2$; hence $a+\varepsilon<1$. Equations (4)--(5) meet all
hypotheses of the common rescuer-tail theorem in `2609`. That theorem forces
the far boundary demand on $T_5$ to be at least $M$, while the adjacent
supercritical role has $B_1<M$. The four ordinary path roles would then have

$$
\sum_{i=2}^5(A_i+B_i)>4,
$$

contrary to nonsupercriticality.

## 4. Neither distinguished role is $T_0$

The placement re-audit `414b` shows that $T_\sigma$ and $T_\tau$ are adjacent.

If the exceptional role is Vd2, use the same neighboring-midpoint perimeter
terminal.

If it is Vd1, the corrected two-chart replacement
[`4147`](../414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md)
preserves the covered skeleton and produces six nonsupercritical Vd0 roles.
Recompute the output gap rank:

- rank zero is excluded by the boundary-complete length theorem;
- rank one is excluded by the common radial disk and complementary-gap
  theorem;
- rank two is excluded by the short CE2 theorem in `2609`.

No preservation of the input gap rank is asserted.

The placements in Sections 1--4 are exhaustive by `414b`. $\square$
