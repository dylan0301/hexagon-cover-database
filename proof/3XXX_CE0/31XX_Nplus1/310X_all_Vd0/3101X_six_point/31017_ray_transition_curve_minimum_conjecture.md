# Algebraic Slice Transition-Curve Targets

Status: Lemma target

This file generalizes the original ray-slice note.  The file name is kept for
continuity, but the contents now record the algebraic slice families tested for
the fixed-angle and optimized six-point relaxed-P strategy.

All points in this note are the relaxed six-point points from
[`31011_six_point_construction.md`](31011_six_point_construction.md).  In
particular, $P_3$ means $P_3^{\mathrm{rel}}$ and $P_5$ means
$P_5^{\mathrm{rel}}$.  No statement here concerns the older five-point
actual-center points.

The computational status of the slice families is recorded in
[`31018_ray_transition_computation_memo.md`](31018_ray_transition_computation_memo.md).
The constant-difference target is recorded separately in
[`31019_constant_difference_slice_minimum_target.md`](31019_constant_difference_slice_minimum_target.md).
A concise success/failure table is recorded in
[`3101a_slice_family_status_catalog.md`](3101a_slice_family_status_catalog.md).

## 1. Ideal minimum relation

Let $E$ be a nonempty selected subset of

$$
\left\{P_3,P_4,P_5,D_0,D_1,D_2\right\}.
$$

Let $F_E(a,b)$ be the selected-point side-length surface from
[`31013_core_surface_definition.md`](31013_core_surface_definition.md).  Let
$\Omega\subseteq\mathcal D$ be the domain under consideration.  An
$E$-admissible slice partition of $\Omega$ is a family $\mathscr S$ of nonempty
subsets of $\Omega$ such that

$$
\bigcup_{\Sigma\in\mathscr S}\Sigma=\Omega,
$$

and

$$
\Sigma_1\cap\Sigma_2=\emptyset
\qquad(\Sigma_1\ne\Sigma_2),
$$

with $F_E$ available somewhere on every $\Sigma\in\mathscr S$.

For a slice $\Sigma\in\mathscr S$, define

$$
\mu_E(\Sigma)=\inf_{(a,b)\in\Sigma}F_E(a,b).
$$

The slice minimizer relation is

$$
\mathcal M_E(\Sigma)=
\left\{(a,b)\in\Sigma:F_E(a,b)=\mu_E(\Sigma)\right\}.
$$

The minimum relation for the partition is

$$
\mathcal M_E(\mathscr S)=
\bigcup_{\Sigma\in\mathscr S}\mathcal M_E(\Sigma).
$$

For the default all-six graph, write $\mathcal M_6(\mathscr S)$ for the
relation obtained from
$E=\left\{P_3,P_4,P_5,D_0,D_1,D_2\right\}$.

## 2. Common coordinates

Use

$$
p=1-b,
\qquad
q=1-a,
\qquad
S=p+q.
$$

Work first in the lower symmetric half

$$
p\le q.
$$

The strict branch and supercritical conditions are

$$
(1-p)^2+(1-p)(1-q)+(1-q)^2<1,
\qquad
S<1.
$$

The diagonal coordinate is

$$
c_*=c(p,q),
$$

and

$$
D_j=(1-c_*)V_j,
\qquad j=0,1,2.
$$

The admissible-set branch transition polynomial is

$$
T(p,q)=S^4-S^2+pq.
$$

For a chosen slice partition $\mathscr S$, the working minimum-curve conjecture
is that $\mathcal M_6(\mathscr S)$ is obtained by intersecting the slices of
$\mathscr S$ with the algebraic transition curve

$$
T(1-b,1-a)=0
$$

inside the domain under consideration, with the reflected half treated by
symmetry from the lower symmetric half $p\le q$.  This identification is
conjectural; it does not prove that $F_6$ has a unique minimizer on each slice
of the chosen partition, that $\mathcal M_6(\mathscr S)$ is continuous, or that
the algebraic transition curve gives the exact global minimum relation.

For $p\le q$, the diagonal value has the two recorded branch descriptions

$$
T\ge0:
\qquad
c_*=
\frac{2q}{1+\sqrt{4S^2-3}},
$$

and

$$
T\le0:
\qquad
c_*^4-c_*^2+pc_*-p^2=0,
\qquad
c_*\ge S.
$$

## 3. Meaning of $T=0$

The equality

$$
T(p,q)=0
$$

is equivalent to

$$
c_*=S=p+q.
$$

Indeed, on the quartic branch, substituting $c=S$ into

$$
c^4-c^2+pc-p^2=0
$$

gives

$$
S^4-S^2+pS-p^2
=
S^4-S^2+pq
=T(p,q).
$$

On the mixed branch, write

$$
D=\sqrt{4S^2-3}.
$$

If $T=0$, then

$$
pq=S^2(1-S^2).
$$

Therefore

$$
(q-p)^2=S^2-4pq=S^2(4S^2-3)=S^2D^2.
$$

Since $q\ge p$, this gives

$$
q-p=SD.
$$

Hence

$$
2q=S+SD=S(1+D),
$$

and therefore

$$
\frac{2q}{1+D}=S.
$$

Thus $c_*=S$ on the mixed branch as well.

Let

$$
R=1-c_*.
$$

The supercritical row gap is

$$
\varepsilon=a+b-1=1-p-q=1-S.
$$

Thus

$$
T=0
\quad\Longleftrightarrow\quad
R=\varepsilon.
$$

The transition curve is therefore the locus where the diagonal radius equals
the supercritical row gap.

## 4. Constant-difference slices

Set

$$
d=q-p.
$$

Then

$$
p=\frac{S-d}{2},
\qquad
q=\frac{S+d}{2},
$$

and

$$
pq=\frac{S^2-d^2}{4}.
$$

Therefore on a fixed-$d$ slice,

$$
T(S,d)=S^4-\frac34S^2-\frac14d^2.
$$

The equation $T=0$ is

$$
4S^4-3S^2-d^2=0.
$$

Thus the unique positive transition value is

$$
S_T(d)=
\sqrt{\frac{3+\sqrt{9+16d^2}}8},
$$

and

$$
p_T(d)=\frac{S_T(d)-d}{2},
\qquad
q_T(d)=\frac{S_T(d)+d}{2}.
$$

This is the primary slice-minimum target for the optimized six-point function.
The conjectured theorem is

$$
F_6(p,q)\ge F_6(p_T(d),q_T(d))
\qquad(q-p=d).
$$

The proof target and partial reductions are recorded in `31019`.

## 5. Ray slices

Use

$$
q=\kappa p,
\qquad \kappa\ge1.
$$

Then

$$
T(p,\kappa p)
=p^2\left((1+\kappa)^4p^2-(1+\kappa+\kappa^2)\right).
$$

Hence the transition point is explicit:

$$
p_T(\kappa)=
\frac{\sqrt{1+\kappa+\kappa^2}}{(1+\kappa)^2},
\qquad
q_T(\kappa)=\kappa p_T(\kappa).
$$

Ray slices remain useful, but the unrestricted fixed-angle claim is false:
for some fixed $\theta$, the minimum of $G_E$ along a ray occurs away from
$T=0$.  The restricted dangerous-window version remains a working target.

## 6. Constant local-metric slices

Set

$$
L=p^2-pq+q^2.
$$

In $(S,d)$ coordinates,

$$
L=\frac{S^2+3d^2}{4}.
$$

Thus

$$
d^2=\frac{4L-S^2}{3}.
$$

Substitution into $T$ gives

$$
T(S,L)=S^4-\frac23S^2-\frac13L.
$$

The transition equation is

$$
3S^4-2S^2-L=0.
$$

Letting $X=S^2$, the positive root is

$$
S_T(L)=
\sqrt{\frac{1+\sqrt{1+3L}}3}.
$$

Then

$$
d_T(L)=\sqrt{\frac{4L-S_T(L)^2}{3}},
$$

and

$$
p_T(L)=\frac{S_T(L)-d_T(L)}2,
\qquad
q_T(L)=\frac{S_T(L)+d_T(L)}2.
$$

This slice is algebraically simple and geometrically natural because it uses
the same minus quadratic form as the local metric

$$
Q(u,v)=u^2+v^2-uv.
$$

However, the global optimized $T=0$ minimum statement is empirically false very
near the symmetric endpoint $L=3/16$.  It may still be useful after removing a
small initial interval.

## 7. General quadratic slices

For

$$
Q_\lambda(p,q)=p^2+\lambda pq+q^2=K,
$$

we have

$$
Q_\lambda=
\frac{(2+\lambda)S^2+(2-\lambda)d^2}{4}.
$$

Assume $\lambda<2$.  Solving for $d^2$ and substituting into $T$ gives

$$
T=0
\quad\Longleftrightarrow\quad
(2-\lambda)X^2+(\lambda-1)X-K=0,
\qquad X=S^2.
$$

Thus

$$
S_T(\lambda,K)=
\sqrt{
\frac{1-\lambda+
\sqrt{(\lambda-1)^2+4(2-\lambda)K}}
{2(2-\lambda)}
}.
$$

Then

$$
d_T(\lambda,K)=
\sqrt{\frac{4K-(2+\lambda)S_T(\lambda,K)^2}{2-\lambda}},
$$

and

$$
p_T=\frac{S_T-d_T}{2},
\qquad
q_T=\frac{S_T+d_T}{2}.
$$

Computations suggest that negative $\lambda$ values are often viable, while
nonnegative $\lambda$ values begin to fail.  The special case $\lambda=-1$ is
most natural geometrically but has a small symmetric-endpoint failure.

## 8. Slices not recommended

The following slices have simple $T=0$ intersections but produced optimized
or fixed-angle failures and are not recommended as global slice-minimum routes.

### Constant product

For

$$
pq=P,
$$

one gets

$$
S_T(P)=\sqrt{\frac{1+\sqrt{1-4P}}2}.
$$

Product slices failed near the symmetric regime.

### Constant sum

For

$$
S=p+q,
$$

one gets

$$
d_T(S)=S\sqrt{4S^2-3}.
$$

Constant-sum slices failed strongly, even in the near-limit support branch.

### Euclidean quadratic

For

$$
p^2+q^2=M,
$$

one gets

$$
S_T(M)=\sqrt{\frac{1+\sqrt{1+8M}}4}.
$$

This slice had small but genuine failures.

### Plus quadratic

For

$$
p^2+pq+q^2=K,
$$

one gets

$$
S_T(K)=K^{1/4}.
$$

Despite its admissible-set appearance, this slice failed repeatedly.

## 9. Finite support-branch proof route

For fixed $(p,q)$, the optimized value

$$
F_6(p,q)=\inf_\theta G_{K_6^{\mathrm{rel}}}(p,q,\theta)
$$

occurs at a support-tie angle.  Therefore every slice-minimum target can in
principle be reduced to finitely many branch inequalities.

For the constant-difference target, the observed transition support regimes are

$$
(D_1),(P_3),(P_5,D_0),
$$

$$
(D_2),(P_3),(P_5,D_0),
$$

$$
(D_1),(P_3,D_2),(P_5),
$$

and

$$
(D_0),(D_2),(P_4,P_5).
$$

The last branch is the near-limit support pattern involving

$$
D_0,D_2,P_4,P_5.
$$

A proof should certify each support branch against the transition value on the
same slice.
