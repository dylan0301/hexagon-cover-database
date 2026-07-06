# Fixed-Angle Enclosing-Triangle Strategy For The Six-Point Core

Status: Strategy

This note records the fixed-angle version of the six-point obstruction target
for the CE0, $N_+=1$, all-Vd0 relaxed-P package.  It is a strategy note, not a
proof of the final inequality.  The selected points are the relaxed six-point
points from [`31011_six_point_construction.md`](31011_six_point_construction.md),
not the earlier five-point actual-center points.

## 1. Six-point target

Let

$$
K_6^{\mathrm{rel}}(a,b)=
\{P_3^{\mathrm{rel}},P_4,P_5^{\mathrm{rel}},D_0,D_1,D_2\}
$$

be the strict-branch relaxed set from `31011`.  On the boundary
$\rho=a^2+ab+b^2=1$, the point $P_4$ is omitted as in that file.  The graph
domain is

$$
\mathcal D=
\{(a,b):0\le a\le1,\ 0\le b\le1,\ a+b>1,\ a^2+ab+b^2\le1\}.
$$

For a finite selected set

$$
E\subseteq\{P_3^{\mathrm{rel}},P_4,P_5^{\mathrm{rel}},D_0,D_1,D_2\},
$$

define the fixed-angle enclosing side-length function by

$$
G_E(a,b,\theta)=
\frac{2}{\sqrt3}
\sum_{j=0}^2
\max_{P\in E} n_j(\theta)\cdot P,
$$

where

$$
n_j(\theta)=
\left(\cos\left(\theta+\frac{2\pi j}{3}\right),
\sin\left(\theta+\frac{2\pi j}{3}\right)\right).
$$

The six-point side-length surface is

$$
F_6(a,b)=\inf_{\theta\in[0,2\pi/3)}G_{K_6^{\mathrm{rel}}}(a,b,\theta).
$$

Thus the remaining six-point inequality is implied by

$$
G_{K_6^{\mathrm{rel}}}(a,b,\theta)>1
$$

for every admissible $(a,b)$ and every $\theta$ in one fundamental orientation
period.

## 2. Subset lower bounds

If

$$
E\subseteq K_6^{\mathrm{rel}}(a,b),
$$

then

$$
G_{K_6^{\mathrm{rel}}}(a,b,\theta)\ge G_E(a,b,\theta).
$$

Therefore it is enough, on any case of the parameter domain, to prove

$$
G_E(a,b,\theta)>1
$$

for some selected subset $E$ that is convenient on that case.

Even more locally, if $Q_0,Q_1,Q_2\in E$, then

$$
G_E(a,b,\theta)
\ge
\frac{2}{\sqrt3}
\sum_{j=0}^2 n_j(\theta)\cdot Q_j(a,b).
$$

A fixed support assignment therefore reduces the proof to one explicit
algebraic inequality.

## 3. Finite support-angle observation

For fixed $(a,b)$ and fixed finite $E$, the function
$\theta\mapsto G_E(a,b,\theta)$ is the maximum-support sum of finitely many
linear trigonometric expressions.  On an open interval where the supporting
point for each $n_j(\theta)$ is constant, say $Q_j$, one has

$$
G_E(a,b,\theta)=
\frac{2}{\sqrt3}\sum_{j=0}^2 n_j(\theta)\cdot Q_j
=A\cos\theta+B\sin\theta.
$$

Thus an optimized enclosing triangle can be searched by support cells and
support-tie angles.  A support-tie angle satisfies

$$
(P-Q)\cdot n_j(\theta)=0
$$

for two points $P,Q\in E$ and some $j\in\{0,1,2\}$.  This gives the finite
support-pattern framework for both numerical search and later interval
certificates.

## 4. Far-from-limit coordinates

For the far-from-limit strategy use

$$
p=1-b,
\qquad
q=1-a.
$$

The lower symmetric half is

$$
p\le q.
$$

The far-from-limit cutoff used in the numerical strategy is

$$
p\ge0.1.
$$

The strict branch and supercritical conditions become

$$
(1-p)^2+(1-p)(1-q)+(1-q)^2<1,
$$

and

$$
p+q<1.
$$

The diagonal coordinate is still the six-point relaxed value

$$
c_*=c(p,q),
$$

and

$$
D_j=(1-c_*)V_j,
\qquad
j=0,1,2.
$$

The relaxed points are

$$
P_3^{\mathrm{rel}}
\quad\text{from the center}\quad
X_2^{\mathrm{rel}}(b),
$$

and

$$
P_5^{\mathrm{rel}}
\quad\text{from the center}\quad
X_5^{\mathrm{rel}}(a),
$$

as defined in `31011`.  No assertion in this note concerns the older
five-point actual-center points.

## 5. Current fixed-angle case split

The following split is the working far-from-limit fixed-angle plan in the lower
half $p\le q$.

Let

$$
S_A=\{P_3^{\mathrm{rel}},P_5^{\mathrm{rel}},D_0,D_2\},
$$

$$
S_C=\{P_3^{\mathrm{rel}},P_5^{\mathrm{rel}},D_1,D_2\},
$$

and

$$
S_D=\{P_3^{\mathrm{rel}},P_5^{\mathrm{rel}},D_1\}.
$$

The proposed fixed-angle lower-bound cases are:

| Case | Angle range | Selected subset | Intended method |
|---|---:|---|---|
| A0 | $0^\circ\le\theta\le18^\circ$ | $S_A$ | coarse lower bound |
| A1 | $18^\circ\le\theta\le26^\circ$ | $S_A$ | ray reduction toward $T=0$ |
| A2 | $26^\circ\le\theta\le30^\circ$ | $S_A$ | coarse lower bound or ray reduction |
| C | $30^\circ\le\theta\le36^\circ$ | $S_C$ | ray reduction toward $T=0$ |
| D1 | $36^\circ\le\theta\le40^\circ$ | $S_D$ | ray reduction toward $T=0$ |
| D2 | $40^\circ\le\theta\le60^\circ$ | $S_D$ | coarse lower bound |

The full six-point function dominates each selected subset function, so this
case split is sufficient if every displayed subset inequality is proved.

The reflected half $q\le p$ should be handled by the symmetry exchanging

$$
P_3^{\mathrm{rel}}\leftrightarrow P_5^{\mathrm{rel}},
\qquad
D_0\leftrightarrow D_2,
\qquad
D_1\leftrightarrow D_1.
$$

## 6. Algebraic certificate target

A proof of a fixed support subcase should introduce

$$
x=\cos\theta,
\qquad
y=\sin\theta,
$$

with

$$
x^2+y^2=1.
$$

The angle ranges become semialgebraic inequalities in $x,y$.  The relaxed
points $P_3^{\mathrm{rel}}$ and $P_5^{\mathrm{rel}}$ are represented by the
selected line-circle root equations from `31012`, and $c_*=c(p,q)$ is split by
the admissible-set transition polynomial described in
[`31017_ray_transition_curve_minimum_conjecture.md`](31017_ray_transition_curve_minimum_conjecture.md).

After choosing one support point for each side, the target is always an
inequality of the form

$$
\frac{2}{\sqrt3}
\left(n_0\cdot Q_0+n_1\cdot Q_1+n_2\cdot Q_2\right)-1>0.
$$

This is the intended endpoint for either a hand algebraic proof or a finite
interval arithmetic certificate.
