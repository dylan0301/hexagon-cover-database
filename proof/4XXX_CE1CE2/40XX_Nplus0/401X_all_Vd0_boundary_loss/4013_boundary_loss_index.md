# CE1/CE2 All-Vd0 Boundary-Loss Obstruction

Status: Proven

## Theorem

Assume the center role is CE1 or CE2, all six vertex roles are Vd0, and

$$
A_i+B_i\le1
\qquad(i=0,\ldots,5).
$$

Then the seven roles cannot cover the hexagon. Equivalently, every CE1/CE2
all-Vd0 cover has at least one supercritical vertex V triangle.

Let

$$
\mathrm{gr}\in\{0,1,2\}
$$

be the number of positive center traces containing a V-gap. One has
$\mathrm{gr}\le1$ for CE1. The three ranks are exhaustive.

| rank | exact data retained | relaxed interior chain | terminal contradiction |
|---|---|---|---|
| $0$ | six strict open handoffs | $\mathrm I^6$ | strict cyclic ascent |
| $1$ | two exact hatted endpoint caps | center-free $\mathrm I^3$ | one-side endpoint sum $<1$ |
| $2$ | two exact hatted endpoint caps | center-free $\mathrm I^3$ | paired CE2 endpoint sum $<1$ |

## 1. No active center gap

Suppose every positive center trace is already covered by its two endpoint
vertex roles. Then the six original open vertex traces alone cover every
boundary edge. Thus

$$
B_i>1-A_{i+1};
$$

equality would leave the common endpoint of the two open traces uncovered.
Since V triangle $T_i$ is nonsupercritical,

$$
B_i\le\widehat g_{C_i}(1-A_i).
$$

Therefore

$$
A_{i+1}>1-B_i
\ge\widehat g_{C_i}^{\vee}(A_i)
\ge A_i.
$$

Iterating gives

$$
A_0<A_1<A_2<A_3<A_4<A_5<A_0,
$$

a contradiction.

## 2. Exactly one active center gap

Use the signed center normal form
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,\qquad W=1-R,\qquad E=\sqrt{1-RW},\qquad
\eta=1-E,\qquad k=\eta+\alpha+\delta.
$$

After reflection, assume the active gap lies in

$$
I_R=\left[\frac{k}{R},W+\delta\right]\subset e_{0,1},
$$

while the companion trace on $e_{5,0}$ is absent or gap-free. Put

$$
s=\frac{k}{R},\qquad q=R-\delta,\qquad
\omega=W+\delta-\frac{k}{R}.
$$

Then $s+q+\omega=1$. Gap containment gives

$$
B_0\ge s,\qquad A_1\ge q.
$$

The companion edge has no active gap, so $A_0+B_5\ge1$. Since $T_0$ is
nonsupercritical,

$$
A_0+B_0\le1,
$$

and hence

$$
B_5\ge1-A_0\ge B_0\ge s.
$$

The complementary endpoint radial demands are

$$
c_1=1-\frac{\delta}{R},\qquad
c_5=1-\frac{\alpha}{W}.
$$

The one-side theorem
[`2107`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md)
applies to the exact signed variables and gives

$$
\boxed{
\widehat g_{c_5}(1-s)+\widehat g_{c_1}(1-q)<1.
}
$$

Let $B_5',B_1'$ be the actual outgoing reaches of the endpoint V triangles on
$e_{4,5}$ and $e_{1,2}$. Then

$$
B_5'\le\widehat g_{c_5}(1-s),
\qquad
B_1'\le\widehat g_{c_1}(1-q),
$$

so $B_1'+B_5'<1$.

Now apply the corrected path theorem
[`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
to the three V triangles $T_2,T_3,T_4$. The center's only possible positive boundary
traces are on $e_{0,1}$ and $e_{5,0}$, so the internal path edges
$e_{2,3},e_{3,4}$ are center-free; diameter locality excludes nonincident
vertex roles; and the full external contributions on the two endpoint edges
are $B_1',B_5'$. Hence coverage forces

$$
\sum_{i=2}^4(A_i+B_i)
\ge4-(B_1'+B_5')>3,
$$

contrary to the three nonsupercritical caps.

This proof is identical for CE1 and for the one-active-gap CE2 state. The
companion center trace may be nonempty in CE2, but it lies on $e_{5,0}$ and is
already absorbed into the endpoint residual; it does not occur on an internal
path edge.

## 3. Two active center gaps

This state is CE2-only. V triangles $T_1,\ldots,T_5$ are nonsupercritical Vd0, so the
common two-gap theorem
[`2110`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md)
applies. In its signed notation

$$
p=W-\alpha,\qquad q=R-\delta,
$$

and the exact paired endpoint theorem gives

$$
\widehat g_{p/W}(1-p)+\widehat g_{q/R}(1-q)<1.
$$

The same center-free three-V triangle path budget gives the contradiction.

The ranks $0,1,2$ are exhaustive, proving the theorem.

$$
\Box
$$
