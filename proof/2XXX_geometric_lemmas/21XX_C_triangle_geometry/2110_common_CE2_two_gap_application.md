# Common CE2 Two-Gap Application

Status: Proven

This note isolates the geometric application of the exact CE2 two-endpoint
capped-loss theorem.  The argument depends only on nonsupercriticality of the
five rows away from the normalized midpoint row; it does not depend on whether
row $T_0$ is nonsupercritical or uniquely supercritical.  It therefore applies
simultaneously to the $N_+=0$ all-Vd0 package and to the $N_+=1$ all-Vd0
two-gap package.

## Theorem

Assume a hypothetical cover has a CE2 center role whose two positive boundary
traces each contain a V-gap, possibly a singleton.  Normalize the unique center
midpoint to $M_0$.  Suppose rows

$$
T_1,T_2,T_3,T_4,T_5
$$

are nonsupercritical Vd0 rows.  Then the perimeter cannot be covered.

No hypothesis on $A_0+B_0$ is required.

## Proof

Use the signed center variables from
[`2109`](2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,
\qquad
W=1-R,
$$

$$
E=\sqrt{1-RW},
\qquad
\eta=1-E,
\qquad
k=\eta+\alpha+\delta.
$$

The two CE2 traces are

$$
\left[\frac{k}{W},R+\alpha\right]
\subset e_{5,0}
$$

and

$$
\left[\frac{k}{R},W+\delta\right]
\subset e_{0,1}.
$$

Put the two far-side inputs

$$
p=1-(R+\alpha)=W-\alpha,
$$

and

$$
q=1-(W+\delta)=R-\delta.
$$

Both are positive.  Since each center trace contains a V-gap, gap containment
gives

$$
b_5\ge p,
\qquad
a_1\ge q.
$$

The exact center-exit formulas give the complementary radial demands

$$
c_5=1-\frac{\alpha}{W}=\frac pW,
$$

and

$$
c_1=1-\frac{\delta}{R}=\frac qR.
$$

Let $B_5$ and $B_1$ denote the outgoing reaches of rows $T_5$ and $T_1$ on
$e_{4,5}$ and $e_{1,2}$.  Since both rows are nonsupercritical, the safe capped
map gives

$$
B_5\le F_{p/W}(p),
\qquad
B_1\le F_{q/R}(q).
$$

The exact two-endpoint theorem
[`2108`](2108_CE2_two_endpoint_capped_loss.md) gives

$$
\boxed{
F_{p/W}(p)+F_{q/R}(q)<1.
}
$$

Consequently

$$
\boxed{B_1+B_5<1.}
$$

Apply the boundary-path budget from
[`2019`](../20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
to the three middle rows $T_2,T_3,T_4$.  The two external endpoint
contributions are $B_1$ and $B_5$, so coverage forces

$$
\sum_{i=2}^4(A_i+B_i)
\ge
4-(B_1+B_5)
>3.
$$

But the three rows are nonsupercritical, hence

$$
\sum_{i=2}^4(A_i+B_i)\le3.
$$

This contradiction proves the theorem.
