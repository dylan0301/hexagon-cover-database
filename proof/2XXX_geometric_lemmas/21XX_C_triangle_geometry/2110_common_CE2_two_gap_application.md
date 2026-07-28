# Common CE2 Two-Gap Application

Status: Proven

This note isolates the geometric application of the exact CE2 two-endpoint
capped-loss theorem. The argument depends only on nonsupercriticality of the
five rows away from the normalized midpoint row; it does not depend on whether
row $T_0$ is nonsupercritical or uniquely supercritical. It therefore applies
to both the $N_+=0$ and $N_+=1$ all-Vd0 two-gap packages.

## Theorem

Assume a hypothetical cover has a CE2 center role whose two positive boundary
traces each contain a V-gap, possibly a singleton. Normalize the unique center
midpoint to $M_0$. Suppose rows

$$
T_1,T_2,T_3,T_4,T_5
$$

are nonsupercritical Vd0 rows. Then the perimeter cannot be covered. No
hypothesis on $A_0+B_0$ is required.

## Proof

Use the signed center variables from
[`2109`](2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,\qquad W=1-R,\qquad E=\sqrt{1-RW},\qquad
\eta=1-E,\qquad k=\eta+\alpha+\delta.
$$

The two CE2 traces are

$$
\left[\frac{k}{W},R+\alpha\right]\subset e_{5,0}
$$

and

$$
\left[\frac{k}{R},W+\delta\right]\subset e_{0,1}.
$$

Put

$$
p=W-\alpha,\qquad q=R-\delta.
$$

Both are positive. The far-side boundary demands left by the two center
intervals are exactly $p$ for row $T_5$ and $q$ for row $T_1$. Since each
center interval contains a V-gap, the corresponding actual endpoint reaches
are at least these demands.

The complementary radial demands at the endpoint rows are

$$
c_5=1-\frac{\alpha}{W}=rac pW,
\qquad
c_1=1-\frac{\delta}{R}=rac qR.
$$

Let $B_5^{\rm far}$ and $B_1^{\rm far}$ denote the reaches of rows $T_5$ and
$T_1$ on the two edges leading away from the center traces, namely $e_{4,5}$
and $e_{1,2}$. By reflecting the local coordinates at $T_5$ when necessary,
the safe capped map gives

$$
B_5^{\rm far}\le F_{p/W}(p),
\qquad
B_1^{\rm far}\le F_{q/R}(q).
$$

The exact two-endpoint theorem
[`2108`](2108_CE2_two_endpoint_capped_loss.md) gives

$$
\boxed{F_{p/W}(p)+F_{q/R}(q)<1,}
$$

and hence

$$
\boxed{B_1^{\rm far}+B_5^{\rm far}<1.}
$$

Apply the corrected boundary-path theorem
[`2019`](../20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
to $T_2,T_3,T_4$. Its hypotheses are explicit here: the center's only
positive boundary traces are on $e_{5,0}$ and $e_{0,1}$, so the internal path
edges $e_{2,3}$ and $e_{3,4}$ are center-free; diameter locality excludes all
nonincident vertex roles; and the complete external contributions on
$e_{1,2}$ and $e_{4,5}$ are bounded by
$B_1^{\rm far}$ and $B_5^{\rm far}$. Therefore coverage forces

$$
\sum_{i=2}^4(A_i+B_i)
\ge4-(B_1^{\rm far}+B_5^{\rm far})>3.
$$

But the three rows are nonsupercritical, so the same sum is at most three.
This contradiction proves the theorem.
