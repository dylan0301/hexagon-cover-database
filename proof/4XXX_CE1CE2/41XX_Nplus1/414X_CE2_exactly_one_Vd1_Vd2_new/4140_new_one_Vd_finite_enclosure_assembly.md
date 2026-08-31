# CE2, $N_+=1$, Exactly One Vd1/Vd2: Direct Finite-Witness Assembly

Status: Proven

Every displayed boundary gap uses actual maximal incident reaches.  If
$J=X_i([\ell,r])\subset e_{i,i+1}$, then

$$
\boxed{\ell=B_i,\qquad r=1-A_{i+1}.}
$$

For selected opposite-side lower bounds, the local closed footprints of the
incident roles lie in the trace-exact AB envelopes
$\mathcal E_i^{\rightarrow}(a_i\mid\ell)$ and
$\mathcal E_{i+1}^{\leftarrow}(1-r\mid b_{i+1})$ from
[`2009e`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/2009e_trace_exact_ab_envelopes.md).  The Vd1/Vd2 support restrictions are
imposed inside this endpoint-conditioned source family.  No affine clipping
of an ordinary AB-union is used.

This package closes the nonzero-gap CE2 branch with exactly one Vd1/Vd2
role without invoking a boundary-transfer composition.  The surviving
placements are separated by the locations of the unique supercritical role
$T_\sigma$ and the unique Vd1/Vd2 role $T_\tau$.  Each placement ends in one
of four geometric terminals:

1. one radial witness lies beyond the corresponding CE2 center exit;
2. the O-side endpoint of a Vd1 trace forces an impossible boundary path;
3. the Vd2 perimeter contribution is too small;
4. the corrected two-chart replacement produces an all-Vd0 state, which is
   sent to the new gap-enclosure proof.

The common signed center notation is that of
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,
\qquad
W=1-R,
\qquad
E=\sqrt{1-RW},
$$

$$
\eta=1-E,
\qquad
P=E(1-E),
\qquad
k=\eta+\alpha+\delta.
$$

The CE2 intervals are

$$
I_L=\left[\frac{k}{W},R+\alpha\right]
\subset e_{5,0},
\qquad
I_R=\left[\frac{k}{R},W+\delta\right]
\subset e_{0,1},
$$

and the three transverse center exits are

$$
d_2^C=\delta,
\qquad
d_3^C=\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\},
\qquad
d_4^C=\alpha.
\tag{1}
$$

## 1. Exhaustive placement reduction

Normalize the unique center midpoint to $M_0$.  A Vd1/Vd2 role is
nonsupercritical, so $\sigma\ne\tau$.  If an additional role has positive
support on an adjacent radial arm, then

$$
N_++N_{\mathrm{sp}}\ge3,
$$

and the common skeleton-length theorem
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
gives a strict length-$12$ deficit.  We therefore assume that every role
other than $T_\tau$ is Vd0.

If $\sigma=0$, then $\tau$ is adjacent or nonadjacent to $0$.  If $\tau=0$,
the midpoint $M_\sigma$ must be rescued by $T_0$, so $\sigma\in\{1,5\}$.
If neither index is zero, midpoint rescue forces $\sigma$ and $\tau$ to be
adjacent.  These alternatives are disjoint and exhaustive.

## 2. $T_0$ supercritical and the Vd role adjacent

After reflection let $\tau=1$.  Let $(A_0,B_0)$ be the actual boundary
reaches of the supercritical role.  Define the residual reaches left by
$T_0$ and the two center intervals by

$$
\rho_R=\mathcal R_{I_R}(B_0),
\qquad
\rho_L=\mathcal R_{I_L}(A_0),
\tag{2}
$$

where, for a center interval $J=[L,U]$ on an edge parametrized from its
left endpoint,

$$
\mathcal R_J(p)=
egin{cases}
1-p,&p<L,\[1mm]
1-\max\{p,U\},&p\ge L.
\end{cases}
$$

This is the uncovered far-side reach after adjoining the connected component
of $[0,p]\cup J$ containing the left endpoint. Boundary coverage gives

$$
A_1\ge\rho_R,
\qquad
B_1\ge\rho_L.
$$

The Vd half-unit boundary cap gives

$$
\boxed{\rho_R+\rho_L<\frac12.}
\tag{3}
$$

The exact CE2 slack calculation in the signed domain gives

$$
\alpha+\delta<\frac16\min\{R,W\}
$$

and the two possible formulas for the positive residual $\rho_L$ give

$$
\boxed{4\delta<\rho_L.}
\tag{4}
$$

For completeness, if $\rho_L=W-\alpha$, then

$$
4\delta+\alpha\le4(\alpha+\delta)<\frac{2W}{3}<W.
$$

If $\rho_L=1-A_0$, the other residual must be
$\rho_R=1-(W+\delta)$; otherwise the endpoint-distance inequality would give
$A_0+B_0>3/2$.  Put $y=k/R$.  The diameter transfer from the points with
reaches $1-\rho_L$ and $y$ gives

$$
\rho_L>\frac{y}{2}>\frac{\eta}{2R}.
$$

The inequality $\rho_R+\rho_L<1/2$ gives

$$
\delta>R-\frac12+\frac{\eta}{2R}.
$$

The right side is strictly increasing in $R$ and equals $1/24$ at
$R=3/8$.  Since the signed domain gives $\delta<1/24$, one has $R<3/8$.
Then $E<2-3R$ and

$$
\rho_L>\frac{\eta}{2R}>\frac16>4\delta.
$$

This proves (4).

Consider the ray $r_2$.  Its center trace ends at distance $\delta$ from $O$,
so the center begins from the vertex side at the local coordinate

$$
q_2=1-\delta.
$$

If $T_1$ has positive support on $r_2$, the exact Vd supported-arm margin
[`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md)
gives

$$
u_{1\to2}<1-\rho_L<1-\delta=q_2.
\tag{5}
$$

For the ordinary role $T_2$, coverage of $e_{1,2}$ and the Vd boundary cap
give

$$
A_2>\frac12+\rho_R,
\qquad
B_2\ge\rho_L.
$$

Put $p=1/2+\rho_R$.  The quarter radial envelope
[`201b`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md)
and (4) give

$$
C_2\le c_{\max}(p,\rho_L)
\le1-\frac{\rho_L}{4}
<1-\delta=q_2.
\tag{6}
$$

Equations (5)--(6) show that neither local role reaches the center interval.
All other roles are excluded from a positive interval of $r_2$ by Vd0 and
diameter locality.  Hence $r_2$ is uncovered.  This closes the adjacent
placement by the single finite radial witness at the first point between the
V traces and the center trace.

## 3. $T_0$ supercritical and the Vd role nonadjacent

Let $\tau\in\{2,3,4\}$.  Put

$$
T=\alpha+\delta.
$$

Let $B$ and $U$ be the far extents already covered by $T_0$ together with
$I_R$ and $I_L$, and define

$$
\rho_R=1-B,
\qquad
\rho_L=1-U.
$$

The intervening nonsupercritical Vd0 roles give

$$
A_\tau\ge\rho_R,
\qquad
B_\tau\ge\rho_L,
\qquad
\rho_R+\rho_L<\frac12.
\tag{7}
$$

Let

$$
M_0(q)=\frac{-q+\sqrt{4-3q^2}}2.
$$

Writing $x=k/W$ and $y=k/R$, the endpoint-distance inequality gives

$$
B\le M_0(x),
\qquad
U\le M_0(y).
$$

Since $1-M_0(q)>q/2$ and the common center-slack lemma gives

$$
T<\frac12\min\{x,y\},
$$

we obtain

$$
\boxed{T<\min\{\rho_R,\rho_L\}.}
\tag{8}
$$

Every center exit in (1) is at most $T$.  The Vd own-radial margin `201c`,
applied to (7), gives

$$
C_\tau<1-\min\{\rho_R,\rho_L\}.
$$

Thus the radial point

$$
D_\tau=\min\{\rho_R,\rho_L\}V_\tau
$$

lies beyond the own Vd trace and beyond the center exit.  Neighboring Vd0
roles and nonlocal roles cannot contain it.  Hence $D_\tau$ is an explicit
uncovered point, a contradiction.

## 4. The Vd role is $T_0$

Midpoint rescue forces $\sigma\in\{1,5\}$; reflect to $\sigma=1$.

### 4.1. $T_0$ is Vd2

A Vd2 role containing a neighboring midpoint has boundary contribution
strictly below $1/3$.  The center contributes strictly below $1/2$, the
supercritical role at most $2/\sqrt3$, and the remaining four roles at most
one each.  Therefore the total available perimeter is strictly below

$$
\frac12+\frac13+\frac2{\sqrt3}+4<6.
$$

This is the Strategy 1 terminal.

### 4.2. $T_0$ is Vd1

Use the exact Vd1 corner normal form
[`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md).
Let its boundary reaches be $a,b$, and write the supported interval on $r_1$,
measured from $V_1$ toward $O$, as

$$
[c,u],
\qquad c\le\frac12\le u.
$$

The O-side endpoint

$$
P=(1-u)V_1
$$

is missed by the Vd1 role, by the adjacent supercritical role, and by every
Vd0 role.  Hence $P\in U_C$.

For the unique shape parameter $t>0$, put

$$
d=\sqrt{t^2+t+1}.
$$

The exact endpoint formulas are

$$
c=\frac{t(1-b)}{t+1},
\qquad
u=\frac{d-a-tb-1}{t}.
$$

The one-sided Vd1 hypothesis gives $t\ge1$.  Let

$$
M_c^{\rm sup}=\frac{c+\sqrt{c^2-8c+4}}2
$$

be the free strict-supercritical outgoing envelope.  Direct differentiation
in the corner form gives

$$
\boxed{
a\le1-M_c^{\rm sup},
\qquad
\frac{a}{a+1-u}\le1-M_c^{\rm sup}.
}
\tag{9}
$$

Indeed, the endpoint inequalities give

$$
a\le d-1-\frac{3t}{2}+c(t+1)
\le\sqrt3-\frac52+2c=:L(c),
$$

and the quadratic comparison

$$
20c^2+(18\sqrt3-52)c+47-24\sqrt3>0
$$

on $[0,1/2]$ yields $2L(c)\le1-M_c^{\rm sup}$.  The hiding-ratio inequality
follows from the same bound and the identity

$$
1-u=\varepsilon_0+\frac at,
\qquad
\varepsilon_0>0.
$$

If the companion center trace does not hide the boundary endpoint $a$, the
far-side demand on $T_5$ is at least $1-a$.  If it does hide $a$, containment
of $P$ gives $\delta/R\ge1-u$, while the near endpoint gives $k\le Wa$.
Therefore

$$
R+\alpha\le\frac{a}{a+1-u}.
$$

In both cases (9) gives a far-side demand

$$
h\ge M_c^{\rm sup}.
\tag{10}
$$

The adjacent supercritical role has outgoing reach

$$
B_1<M_c^{\rm sup}.
\tag{11}
$$

The four ordinary roles $T_2,T_3,T_4,T_5$ cover the center-free boundary path
between these two endpoints.  Adding the four edge-cover inequalities gives

$$
\sum_{i=2}^5(A_i+B_i)
\ge4+h-B_1>4,
$$

contrary to nonsupercriticality of all four roles.  This closes the Vd1 rescue
placement without a map composition.

## 5. Neither distinguished role is $T_0$

Midpoint rescue makes $T_\sigma$ and $T_\tau$ adjacent.

If $T_\tau$ is Vd2, the perimeter argument of Section 4.1 applies.  If it is
Vd1, apply the corrected two-chart replacement
[`4147`](../414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md).
The replacement preserves the covered skeleton and produces six
nonsupercritical Vd0 roles.  Recompute their output gap rank
$N'_{\rm gap}$:

- if $N'_{\rm gap}=0$, the boundary-complete length theorem `2500` gives the
  contradiction;
- if $N'_{\rm gap}=1$ or $2$, apply the explicit gap-enclosure proof
  [`4013_new`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md).

No preservation of the input gap rank is asserted or needed.

The alternatives in Sections 2--5 are exhaustive, so the branch is
impossible.

$$
\Box
$$
