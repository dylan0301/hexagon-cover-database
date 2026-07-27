# CE1/CE2 All-Vd0 Boundary-Loss Obstruction

Status: Proven

## Theorem

Assume the center role is CE1 or CE2, all six vertex roles are Vd0, and

$$
a_i+b_i\le1
\qquad(i=0,\ldots,5).
$$

Then the seven roles cannot cover the hexagon.  Equivalently, every CE1/CE2
all-Vd0 cover has at least one supercritical vertex row.

The proof is organized only by the active-gap rank

$$
\mathrm{gr}\in\{0,1,2\},
$$

the number of positive center traces that contain a V-gap.  One has
$\mathrm{gr}\le1$ in CE1.  The common chain notation and the identity
relaxation are proved in
[`201d`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md).

The three signatures are

| rank | exact data retained | relaxed interior chain | terminal contradiction |
|---|---|---|---|
| $\mathrm{gr}=0$ | six strict open handoffs | $\mathrm I^6$ | strict cyclic ascent |
| $\mathrm{gr}=1$ | two exact endpoint capped maps | $\mathrm I^3$ | one-side endpoint sum $<1$ |
| $\mathrm{gr}=2$ | two exact endpoint capped maps | $\mathrm I^3$ | paired CE2 endpoint sum $<1$ |

## 1. No active center gap: the strict identity cycle

Suppose every positive center trace is already covered by its endpoint vertex
roles.  Then the six original open vertex roles alone cover every boundary
edge.

Let $c_i$ be the actual own-radial reach of row $T_i$.  Since the two incident
open traces cover $e_{i,i+1}$, their endpoints overlap strictly:

$$
b_i>1-a_{i+1}.
$$

Equality would leave their common endpoint uncovered.  Hence

$$
a_{i+1}>1-b_i.
$$

Row $T_i$ is nonsupercritical, so the safe capped-map theorem gives

$$
b_i\le F_{c_i}(a_i).
$$

Therefore

$$
a_{i+1}
>
1-b_i
\ge
1-F_{c_i}(a_i)
=
G_{c_i}(a_i)
\ge
a_i.
$$

The last inequality is the identity relaxation
$G_{c_i}\ge\mathrm I$.  Iterating around the six rows yields

$$
a_0<a_1<a_2<a_3<a_4<a_5<a_0,
$$

a contradiction.  In the chain notation this is

$$
\mathscr C\!\left[
a_0;\,
\mathrm I^6;\,
a_0>a_0
\right].
$$

Thus the rank-zero proof is the strict cyclic identity relaxation of the exact
six-row capped chain.

## 2. Exactly one active center gap

Use the signed center normal form
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,
\qquad
W=1-R,
\qquad
E=\sqrt{1-RW},
\qquad
\eta=1-E,
$$

$$
k=\eta+\alpha+\delta.
$$

After reflection, assume the active gap lies in

$$
I_R=\left[\frac{k}{R},W+\delta\right]
\subset e_{0,1},
$$

while the companion trace is empty or gap-free.  Put

$$
s=\frac{k}{R},
\qquad
q=R-\delta,
\qquad
\omega=W+\delta-\frac{k}{R}.
$$

Then

$$
s+q+\omega=1.
$$

Gap containment gives

$$
b_0\ge s,
\qquad
a_1\ge q.
$$

Since the companion edge has no active gap,

$$
a_0+b_5\ge1.
$$

Row $T_0$ is nonsupercritical, so

$$
a_0+b_0\le1,
$$

and consequently

$$
b_5\ge1-a_0\ge b_0\ge s.
$$

The exact complementary radial demands at the two endpoint rows are

$$
c_1=1-\frac{\delta}{R},
\qquad
c_5=1-\frac{\alpha}{W}.
$$

The variables $R,s,q,\omega$ satisfy the hypotheses of the one-side
capped-loss theorem
[`2107`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md).
Its second radial deficit is exactly $\alpha/W$, so it gives

$$
\boxed{
F_{c_5}(s)+F_{c_1}(q)<1.
}
$$

Let $B_5,B_1$ be the actual outgoing reaches of rows $T_5,T_1$ on the two
outer edges of the middle boundary path.  The endpoint maps remain exact:

$$
B_5\le F_{c_5}(s),
\qquad
B_1\le F_{c_1}(q).
$$

Thus $B_1+B_5<1$.  The three interior rows $T_2,T_3,T_4$ use only the
identity relaxation.  Equivalently, the boundary-path budget
[`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
gives

$$
\sum_{i=2}^4(a_i+b_i)
\ge
4-(B_1+B_5)
>3,
$$

contrary to their three nonsupercritical caps.

The chain signature is therefore

$$
\mathscr C\!\left[
(q,s);\,
\mathrm I^3;\,
F_{c_1}(q)+F_{c_5}(s)<1
\right].
$$

This proof is identical for CE1 and for the one-active-gap CE2 state.  The only
difference is whether the companion center trace is absent or merely gap-free.

## 3. Two active center gaps

This state is possible only in CE2.  Rows $T_1,\ldots,T_5$ are
nonsupercritical Vd0 rows, so all hypotheses of the common CE2 two-gap theorem
[`2110`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md)
are satisfied.

With

$$
p=W-\alpha,
\qquad
q=R-\delta,
$$

the exact endpoint inputs and radial demands are

$$
(p,p/W),
\qquad
(q,q/R).
$$

The paired endpoint theorem `2108` gives

$$
F_{p/W}(p)+F_{q/R}(q)<1.
$$

The three middle rows again contribute only $\mathrm I^3$, and the same
boundary-path budget gives the contradiction.  Its signature is

$$
\mathscr C\!\left[
(p,q);\,
\mathrm I^3;\,
F_{p/W}(p)+F_{q/R}(q)<1
\right].
$$

The cases $\mathrm{gr}=0,1,2$ are exhaustive.  Therefore the CE1/CE2,
$N_+=0$, all-Vd0 branch is impossible.

$$
\Box
$$
