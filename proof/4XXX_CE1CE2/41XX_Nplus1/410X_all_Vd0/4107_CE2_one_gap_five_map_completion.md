# CE2 One-Gap Five-Map Completion

Status: Proven

This note proves both orientations of the CE2 exactly-one-gap state in `410X`.
The common center formulas, actual-row propagation, supercritical target, and
reflection order are isolated in
[`4105`](4105_CE1_CE2_one_gap_five_row_interface.md). Only the CE2 scalar
threshold argument is proved here.

## 1. Exact signed CE2 domain

Use the signed normal form
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).
Put

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
P=E(1-E),
$$

and let $\alpha,\delta>0$ be the two center slacks. Set

$$
k=\eta+\alpha+\delta.
$$

The CE2 sign conditions are exactly

$$
\boxed{
\alpha+W\delta<P,
\qquad
R\alpha+\delta<P.
}
$$

The normalized right center trace is

$$
\left[\frac{k}{R},W+\delta\right],
$$

and its far-end input is

$$
z_0=R-\delta.
$$

Put

$$
Q=\frac{k}{2R}.
$$

The five nonsupercritical demands are

$$
\begin{aligned}
c_1&=1-\frac{\delta}{R},&
c_2&=1-\delta,\\
c_3&=1-\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\},&
c_4&=1-\alpha,&
c_5&=1-\frac{\alpha}{W}.
\end{aligned}
$$

Let

$$
z_i=G_{c_i}(z_{i-1})
\qquad(1\le i\le5),
$$

and write

$$
Z_R=z_5.
$$

By `4105`, the right-gap branch is impossible once

$$
\boxed{Z_R>1-Q}
$$

is proved. The same note gives the reflected left-gap conclusion after the
explicit substitution

$$
R\longleftrightarrow W,
\qquad
\alpha\longleftrightarrow\delta.
$$

## 2. Low-root range

For

$$
0<d<1-\frac{\sqrt3}{2},
$$

put

$$
e(d)=\ell(1-d).
$$

The scalar theorem
[`2012`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md)
proves

$$
\boxed{
e(d)<\frac{2d}{1-2d}
}
$$

for

$$
0<d\le\mu,
\qquad
\mu=\frac{2\sqrt3-3}{4},
$$

and the threshold implication

$$
\boxed{
x>e(d)
\quad\Longrightarrow\quad
G_{1-d}(x)\ge1-e(d).
}
$$

Because $E\ge\sqrt3/2$ and $E(1-E)$ decreases on this interval,

$$
P\le\mu.
$$

The two strict CE2 inequalities give

$$
0<\alpha,\delta<P\le\mu,
$$

so every use of the low-root estimates below is within its proved range.

## 3. The initial threshold

The first CE2 inequality gives

$$
Wz_0
=RW-W\delta
=\eta+P-W\delta
>\eta+\alpha.
$$

We prove

$$
\frac{\eta+\alpha}{W}
>
\frac{2\alpha}{1-2\alpha}.
$$

Define

$$
\pi(q)=(\eta+q)(1-2q)-2qW.
$$

This is strictly concave. Direct simplification using
$P=\eta E$ and $E^2=1-RW$ gives

$$
\pi(0)=\eta>0,
$$

and

$$
\pi(P)=\eta\left(\eta+2ER^2\right)>0.
$$

Hence $\pi(q)>0$ for $0<q<P$. Since $\alpha<P<1/2$, this proves the displayed
comparison. The low-root upper bound now gives

$$
\boxed{
z_0
>
\frac{\eta+\alpha}{W}
>
\frac{2\alpha}{1-2\alpha}
>
e(\alpha).
}
$$

## 4. A short two-threshold lemma

Put

$$
T=\alpha+\delta.
$$

Multiply

$$
\alpha+W\delta<P
$$

by $W$, multiply

$$
R\alpha+\delta<P
$$

by $R$, and add. Since

$$
W+R^2=W^2+R=E^2,
$$

we obtain

$$
E^2T<P=E\eta.
$$

Thus

$$
\boxed{T<\frac{\eta}{E}.}
$$

Let

$$
d=\min\{\alpha,\delta\}.
$$

Then $d\le T/2$. Applying the rational upper bound to both roots and using
that $q\mapsto2q/(1-2q)$ is increasing gives

$$
\min\{e(\alpha),e(\delta)\}
<
\min\left\{\frac{2\alpha}{1-2\alpha},\frac{2\delta}{1-2\delta}\right\}
=
\frac{2d}{1-2d}
\le
\frac{T}{1-T}.
$$

It remains to compare the last expression with $Q$. Define

$$
\Phi(t)=(\eta+t)(1-t)-2Rt.
$$

The function $\Phi$ is strictly concave. Therefore its minimum on
$[0,\eta/E]$ occurs at an endpoint. One endpoint gives

$$
\Phi(0)=\eta>0.
$$

For the other endpoint put

$$
\xi=2R-1.
$$

Then

$$
E=\frac12\sqrt{3+\xi^2},
$$

and direct simplification gives

$$
\Phi\left(\frac{\eta}{E}\right)
=
\frac{RW}{2E^2(1+E)}
\left(1+\xi^2-\xi\sqrt{3+\xi^2}\right).
$$

The prefactor is positive. If $\xi\le0$, the last factor is positive
immediately. If $0<\xi<1$, then

$$
(1+\xi^2)^2-\xi^2(3+\xi^2)
=1-\xi^2>0,
$$

so again

$$
1+\xi^2>\xi\sqrt{3+\xi^2}.
$$

Thus $\Phi$ is positive at both endpoints and therefore throughout the
interval. Since $T<\eta/E$,

$$
(\eta+T)(1-T)>2RT.
$$

Equivalently,

$$
\frac{T}{1-T}
<
\frac{\eta+T}{2R}
=Q.
$$

Consequently

$$
\boxed{
\min\{e(\alpha),e(\delta)\}<Q.
}
$$

## 5. Threshold routing

Every capped map in the chain is extensive.

If

$$
e(\alpha)<Q,
$$

then the input at row $4$ is at least $z_0>e(\alpha)$. Since
$c_4=1-\alpha$, the threshold theorem gives

$$
z_4\ge1-e(\alpha)>1-Q.
$$

The final map preserves this strict inequality, so

$$
Z_R=z_5>1-Q.
$$

Suppose instead that

$$
e(\alpha)\ge Q.
$$

The two-threshold lemma gives

$$
e(\delta)<Q.
$$

Extensivity and the initial threshold yield

$$
z_1\ge z_0>e(\alpha)\ge Q>e(\delta).
$$

Since $c_2=1-\delta$, row $2$ gives

$$
z_2\ge1-e(\delta)>1-Q.
$$

Rows $3,4,5$ preserve the strict inequality. Hence in both alternatives

$$
\boxed{Z_R>1-Q.}
$$

The common interface `4105` now gives

$$
a_0\ge Z_R
>
1-Q
>
B_k\left(\frac{k}{R}\right)
\ge a_0,
$$

where the middle strict comparison is the diameter-transfer estimate in
[`2018`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md).
This contradiction eliminates the right-gap orientation.

## 6. Reflection

For a gap in the companion trace, reflect across the axis through $V_0$.
The signed center variables exchange as

$$
R\longleftrightarrow W,
\qquad
\alpha\longleftrightarrow\delta,
$$

and the row order becomes $5,4,3,2,1$. The CE2 domain, the initial-threshold
proof, and the two-threshold proof are invariant under this exchange. The
reflected form of `4105` therefore gives the same contradiction for the
left-gap orientation.

Both CE2 exactly-one-gap orientations are impossible.

$$
\Box
$$
