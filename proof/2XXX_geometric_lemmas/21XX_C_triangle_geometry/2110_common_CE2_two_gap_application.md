# Common CE2 Two-Gap Skeleton Application

Status: Proven

This note isolates the skeleton-data application of the exact CE2 paired
endpoint theorem. No point of the two-dimensional interior $H\setminus S$ is
used.

## Theorem

Let the center role be CE2 with both positive boundary traces containing a
V-gap, possibly a singleton. Normalize its unique center midpoint to $M_0$.
Assume:

1. V triangles $T_1,\ldots,T_5$ are nonsupercritical Vd0 roles;
2. the perimeter and radial arms $r_1,r_5$ are covered by the seven open
   roles.

Then such data are impossible. No hypothesis on $A_0+B_0$ is required.

## Proof

Use the signed center variables from
[`2109`](2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,
\qquad
W=1-R,
\qquad
E=\sqrt{1-RW},
\qquad
\eta=1-E,
\qquad
k=\eta+\alpha+\delta.
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
p=W-\alpha,
\qquad
q=R-\delta.
$$

Both are positive. Since each center interval contains a V-gap, the far-side
boundary demands at $T_5$ and $T_1$ are at least $p$ and $q$, respectively.

The center exits on the two endpoint radial arms are

$$
d_5^C=\frac{\alpha}{W},
\qquad
d_1^C=\frac{\delta}{R}.
$$

Because the endpoint roles are Vd0, no adjacent vertex role has a
positive-length trace on these arms; diameter locality excludes every nonlocal
role. Coverage of $r_5$ and $r_1$ therefore forces

$$
C_5\ge c_5:=1-\frac{\alpha}{W}=\frac pW,
\qquad
C_1\ge c_1:=1-\frac{\delta}{R}=\frac qR.
$$

Let $B_5^{\rm far}$ and $B_1^{\rm far}$ denote the reaches of $T_5$ and
$T_1$ on $e_{4,5}$ and $e_{1,2}$. By reflecting the local coordinates at
$T_5$ when necessary, the safe capped map gives

$$
B_5^{\rm far}\le F_{p/W}(p),
\qquad
B_1^{\rm far}\le F_{q/R}(q).
$$

The exact paired endpoint theorem
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
to $T_2,T_3,T_4$. The center's only positive boundary traces are on
$e_{5,0}$ and $e_{0,1}$, so $e_{2,3}$ and $e_{3,4}$ are center-free.
Diameter locality excludes nonincident vertex roles. Perimeter coverage
therefore forces

$$
\sum_{i=2}^4(A_i+B_i)
\ge4-(B_1^{\rm far}+B_5^{\rm far})>3.
$$

The three V triangles are nonsupercritical, so the same sum is at most three.
This contradiction proves the theorem.

$$
\Box
$$
