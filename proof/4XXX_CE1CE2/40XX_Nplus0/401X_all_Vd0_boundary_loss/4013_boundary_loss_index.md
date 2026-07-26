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

The proof is organized only by the number $g$ of positive center traces that
contain an active V-gap.  One has

$$
g\in\{0,1,2\},
$$

and $g\le1$ in CE1.

## 1. No active center gap

Suppose every positive center trace is already covered by its endpoint vertex
roles.  Then the six original open vertex roles alone cover $\partial H$.

For each $i$, let $U_i$ be the trace of the open role at $V_i$ on
$\partial H$.  It is relatively open and

$$
\mathcal H^1(U_i)\le a_i+b_i\le1.
$$

A finite relatively open cover of the connected polygonal circle
$\partial H$ cannot have all nonempty members pairwise disjoint.  Hence two
traces overlap in a relatively open set of positive length, and therefore

$$
\sum_{i=0}^5\mathcal H^1(U_i)
>
\mathcal H^1\left(\bigcup_{i=0}^5U_i\right)
=6.
$$

But

$$
\sum_{i=0}^5\mathcal H^1(U_i)
\le
\sum_{i=0}^5(a_i+b_i)
\le6,
$$

a contradiction.

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
u=R-\delta,
\qquad
\omega=W+\delta-\frac{k}{R}.
$$

Then

$$
s+\nu+\omega=1.
$$

Gap containment gives

$$
b_0\ge s,
\qquad
a_1\ge\nu.
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

The variables $R,s,\nu,\omega$ satisfy the hypotheses of the one-side
capped-loss theorem
[`2107`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md).
Its second radial deficit is exactly $\alpha/W$, so it gives

$$
\boxed{
F_{c_5}(s)+F_{c_1}(\nu)<1.
}
$$

Let $B_5,B_1$ be the actual outgoing reaches of rows $T_5,T_1$ on the two
outer edges of the middle boundary path.  The safe capped map gives

$$
B_5\le F_{c_5}(s),
\qquad
B_1\le F_{c_1}(\nu),
$$

and hence

$$
B_1+B_5<1.
$$

Apply the boundary-path budget
[`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
to $T_2,T_3,T_4$.  Coverage forces

$$
\sum_{i=2}^4(a_i+b_i)
\ge
4-(B_1+B_5)
>3,
$$

contrary to the three nonsupercritical row caps.

This proof is identical for CE1 and for the one-active-gap CE2 state.  The only
difference is whether the companion center trace is absent or merely gap-free.

## 3. Two active center gaps

This state is possible only in CE2.  Rows $T_1,\ldots,T_5$ are
nonsupercritical Vd0 rows, so all hypotheses of the common CE2 two-gap theorem
[`2110`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md)
are satisfied.  That theorem applies the exact paired endpoint loss `2108`
and the same three-row boundary-path budget, giving a contradiction.

The cases $g=0,1,2$ are exhaustive.  Therefore the CE1/CE2, $N_+=0$,
all-Vd0 branch is impossible.

$$
\Box
$$
