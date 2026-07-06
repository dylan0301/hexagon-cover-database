# Ray-Slice Transition-Curve Minimum Target

Status: Lemma target

This note records the conjectural ray-slice reduction for the fixed-angle
six-point relaxed-P strategy.  It is not a proof.  The computational status and
known failures of stronger variants are recorded in
[`31018_ray_transition_computation_memo.md`](31018_ray_transition_computation_memo.md).

All points in this note are the relaxed six-point points from
[`31011_six_point_construction.md`](31011_six_point_construction.md).  In
particular, $P_3$ means $P_3^{\mathrm{rel}}$ and $P_5$ means
$P_5^{\mathrm{rel}}$.

## 1. Coordinates and transition polynomial

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

The strict far-domain is

$$
\mathcal F_{0.1}^-=
\{(p,q):0.1\le p\le q,
\ p+q<1,
\ (1-p)^2+(1-p)(1-q)+(1-q)^2<1\}.
$$

The admissible-set branch transition polynomial is

$$
T(p,q)=S^4-S^2+pq.
$$

For $p\le q$, the diagonal coordinate $c_*=c(p,q)$ is on one of the following
branches:

$$
T\ge0:
\qquad
c_*=
\frac{2q}{1+\sqrt{4S^2-3}},
$$

or

$$
T\le0:
\qquad
c_*^4-c_*^2+pc_*-p^2=0,
\qquad
c_*\ge S.
$$

The transition curve is the common branch boundary.

## 2. Geometric meaning of $T=0$

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

## 3. Ray foliation

Use the ray slices

$$
q=\kappa p,
\qquad
\kappa\ge1.
$$

Along such a ray,

$$
T(p,\kappa p)
=p^2\left((1+\kappa)^4p^2-(1+\kappa+\kappa^2)\right).
$$

Therefore the transition point on the ray is explicit:

$$
p_T(\kappa)=
\frac{\sqrt{1+\kappa+\kappa^2}}{(1+\kappa)^2},
$$

and

$$
q_T(\kappa)=\kappa p_T(\kappa).
$$

The transition point lies on the cutoff boundary $p=0.1$ when

$$
\frac{1+\kappa+\kappa^2}{(1+\kappa)^4}=0.01.
$$

Let $\kappa_{0.1}$ denote the unique solution with $\kappa\ge1$.  Numerically,

$$
\kappa_{0.1}=8.518281505052565\ldots .
$$

Thus the transition part of the far lower half is parameterized by

$$
1\le\kappa\le\kappa_{0.1}.
$$

For $\kappa>\kappa_{0.1}$, the transition point lies outside the far cutoff
$p\ge0.1$, so the relevant ray endpoint is $p=0.1$ rather than $p_T(\kappa)$.

## 4. Ray-slice functions

For a selected subset

$$
E\subseteq\{P_3^{\mathrm{rel}},P_4,P_5^{\mathrm{rel}},D_0,D_1,D_2\},
$$

define

$$
H_E(p;\kappa,\theta)=G_E(1-\kappa p,1-p,\theta),
$$

where the arguments of $G_E$ are $(a,b)$ and

$$
q=\kappa p,
\qquad
a=1-q,
\qquad
b=1-p.
$$

The admissible ray interval is

$$
p_{\rho,-}(\kappa)<p<\frac1{1+\kappa},
$$

with the far cutoff $p\ge0.1$, where

$$
p_{\rho,-}(\kappa)=
\frac{3(1+\kappa)-
\sqrt{9(1+\kappa)^2-8(1+\kappa+\kappa^2)}}
{2(1+\kappa+\kappa^2)}.
$$

## 5. Restricted ray-minimum lemma target

The current proof target is not the global all-angle version.  The computation
memo records counterexamples to that stronger statement in non-dangerous angle
regions.  The useful restricted target is the following.

### Lemma target

On each ray $q=\kappa p$ with $1\le\kappa\le\kappa_{0.1}$, the selected subset
function has its minimum at $p=p_T(\kappa)$ in the following dangerous windows:

1. For

   $$
   E=S_A=\{P_3^{\mathrm{rel}},P_5^{\mathrm{rel}},D_0,D_2\},
   \qquad
   18^\circ\le\theta\le26^\circ,
   $$

   prove

   $$
   H_{S_A}(p;\kappa,\theta)
   \ge
   H_{S_A}(p_T(\kappa);\kappa,\theta).
   $$

2. For

   $$
   E=S_C=\{P_3^{\mathrm{rel}},P_5^{\mathrm{rel}},D_1,D_2\},
   \qquad
   30^\circ\le\theta\le36^\circ,
   $$

   prove

   $$
   H_{S_C}(p;\kappa,\theta)
   \ge
   H_{S_C}(p_T(\kappa);\kappa,\theta).
   $$

3. For

   $$
   E=S_D=\{P_3^{\mathrm{rel}},P_5^{\mathrm{rel}},D_1\},
   \qquad
   36^\circ\le\theta\le40^\circ,
   $$

   prove

   $$
   H_{S_D}(p;\kappa,\theta)
   \ge
   H_{S_D}(p_T(\kappa);\kappa,\theta).
   $$

These statements would reduce the dangerous fixed-angle far-from-limit cases to
one transition-curve check in $(\kappa,\theta)$.

## 6. Monotonicity form

A stronger and more certificate-friendly form is the two-sided derivative
claim

$$
\frac{\partial}{\partial p}H_E(p;\kappa,\theta)\le0
\qquad
(p<p_T(\kappa)),
$$

and

$$
\frac{\partial}{\partial p}H_E(p;\kappa,\theta)\ge0
\qquad
(p>p_T(\kappa)),
$$

within the relevant support-pattern cell and dangerous angle window.

Because $G_E$ is a support maximum, this derivative statement should be proved
after splitting by the active supports.  On each support cell, the derivative is
algebraic.  The diagonal derivative is explicit on each branch.  On the quartic
branch,

$$
(4c_*^3-2c_*+p)\frac{dc_*}{dp}+c_*-2p=0,
$$

so

$$
\frac{dc_*}{dp}=
\frac{2p-c_*}{4c_*^3-2c_*+p}.
$$

The relaxed points are represented by the selected line-circle root equations
from the relaxed-P construction.  If the corresponding root parameters are
$\lambda$ and $\mu$, then their derivatives are obtained from

$$
F_3(\lambda,p;\kappa)=0,
\qquad
F_5(\mu,p;\kappa)=0
$$

by

$$
\lambda'=-\frac{F_{3,p}}{F_{3,\lambda}},
\qquad
\mu'=-\frac{F_{5,p}}{F_{5,\mu}}.
$$

This is the intended algebraic input for an interval proof of ray monotonicity.

## 7. Transition-curve lower-bound target

After the ray reduction, the remaining transition checks are

$$
G_{S_A}(p_T(\kappa),q_T(\kappa),\theta)>1,
\qquad
18^\circ\le\theta\le26^\circ,
$$

$$
G_{S_C}(p_T(\kappa),q_T(\kappa),\theta)>1,
\qquad
30^\circ\le\theta\le36^\circ,
$$

and

$$
G_{S_D}(p_T(\kappa),q_T(\kappa),\theta)>1,
\qquad
36^\circ\le\theta\le40^\circ,
$$

for $1\le\kappa\le\kappa_{0.1}$.  The empirical minima of these transition
checks are recorded in `31018`.
