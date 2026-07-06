# Constant-Difference Slice Minimum Target

Status: Lemma target

This file records the primary optimized-slice target suggested by the six-point
fixed-angle experiments.  It concerns the optimized value $F_6$, not the
stronger false statement that every fixed-angle function $G_6(\theta)$ is
minimized at the transition point.

All points are the relaxed six-point points from
[`31011_six_point_construction.md`](31011_six_point_construction.md).  In
particular, $P_3$ means $P_3^{\mathrm{rel}}$ and $P_5$ means
$P_5^{\mathrm{rel}}$.

## 1. Target statement

Use

$$
p=1-b,
\qquad
q=1-a,
\qquad
S=p+q,
\qquad
d=q-p.
$$

Work in the lower symmetric half $p\le q$, so $d\ge0$.

For fixed $d\in[0,1)$, define

$$
F_d(S)=F_6(a,b),
$$

where

$$
a=1-\frac{S+d}{2},
\qquad
b=1-\frac{S-d}{2}.
$$

The constant-difference slice minimum target is

$$
\boxed{
F_d(S)\ge F_d(S_T(d))
}
$$

for every admissible $S$, where

$$
S_T(d)=
\sqrt{\frac{3+\sqrt{9+16d^2}}8}.
$$

Equivalently,

$$
p_T(d)=\frac{S_T(d)-d}{2},
\qquad
q_T(d)=\frac{S_T(d)+d}{2},
$$

and the target is

$$
F_6(p,q)\ge F_6(p_T(d),q_T(d))
\qquad(q-p=d).
$$

This file does not prove the boxed target.  It proves the exact slice geometry
and finite support reduction, and records the support-branch certificate plan.

## 2. Strict slice interval

Since

$$
a=1-\frac{S+d}{2},
\qquad
b=1-\frac{S-d}{2},
$$

put

$$
m=1-\frac S2,
\qquad
 e=\frac d2.
$$

Then

$$
a=m-e,
\qquad
b=m+e.
$$

The strict branch condition is

$$
a^2+ab+b^2<1.
$$

Expanding,

$$
(m-e)^2+(m-e)(m+e)+(m+e)^2=3m^2+e^2.
$$

Thus the strict branch condition is

$$
3\left(1-\frac S2\right)^2+\frac{d^2}{4}<1.
$$

Solving for $S$, the lower boundary is

$$
S_\rho(d)=
2\left(1-\sqrt{\frac{1-d^2/4}{3}}\right).
$$

The supercritical condition is

$$
a+b>1.
$$

Since $a+b=2-S$, this becomes

$$
S<1.
$$

Hence the strict constant-difference slice is

$$
S_\rho(d)<S<1.
$$

## 3. Unique transition point on the slice

The transition polynomial is

$$
T(p,q)=S^4-S^2+pq.
$$

On a fixed-$d$ slice,

$$
p=\frac{S-d}{2},
\qquad
q=\frac{S+d}{2},
$$

so

$$
pq=\frac{S^2-d^2}{4}.
$$

Therefore

$$
T(S,d)=S^4-\frac34S^2-\frac14d^2.
$$

The equation $T=0$ is

$$
4S^4-3S^2-d^2=0.
$$

With $X=S^2$, this is

$$
4X^2-3X-d^2=0.
$$

The positive root is

$$
X_T(d)=\frac{3+\sqrt{9+16d^2}}8.
$$

Thus

$$
S_T(d)=\sqrt{X_T(d)}
=
\sqrt{\frac{3+\sqrt{9+16d^2}}8}.
$$

To prove uniqueness, differentiate:

$$
\frac{\partial T}{\partial S}
=4S^3-\frac32S
=S\left(4S^2-\frac32\right).
$$

On the strict slice,

$$
S>S_\rho(d)\ge S_\rho(0)=2\left(1-\frac1{\sqrt3}\right)>\sqrt{\frac38}.
$$

Therefore

$$
\frac{\partial T}{\partial S}>0.
$$

At $S=1$,

$$
T(1,d)=\frac{1-d^2}{4}>0.
$$

At the lower strict-branch boundary,

$$
3\left(1-\frac S2\right)^2+\frac{d^2}{4}=1,
$$

so

$$
d^2=-3S^2+12S-8.
$$

Substitution gives

$$
T=S^4-3S+2=(S-1)(S^3+S^2+S-2).
$$

On the relevant lower boundary, the second factor is positive and $S<1$;
hence $T<0$.  Since $T$ is strictly increasing, $S_T(d)$ is the unique zero of
$T$ on the strict constant-difference slice.

## 4. Transition meaning

At $T=0$, the diagonal value satisfies

$$
c_*=S=p+q.
$$

Thus, with

$$
R=1-c_*,
$$

and with the supercritical row gap

$$
\varepsilon=a+b-1=1-S,
$$

one has

$$
T=0
\quad\Longleftrightarrow\quad
R=\varepsilon.
$$

The transition point is therefore where the diagonal radius equals the
supercritical row gap.

## 5. Finite support-tie reduction

For a finite set $K$, define

$$
G_K(\theta)=
\frac2{\sqrt3}\sum_{j=0}^2\max_{P\in K}n_j(\theta)\cdot P.
$$

On a support cell where the maximizing point for each normal $n_j(\theta)$ is
fixed, say $Q_j$, one has

$$
G_K(\theta)=\frac2{\sqrt3}\sum_{j=0}^2 n_j(\theta)\cdot Q_j
=A\cos\theta+B\sin\theta.
$$

Thus

$$
G_K''(\theta)=-G_K(\theta).
$$

Since $G_K(\theta)>0$, an interior critical point of a support cell cannot be a
local minimum.  Hence an optimized angle occurs at a support-tie angle,
namely an angle satisfying

$$
(P-Q)\cdot n_j(\theta)=0
$$

for some distinct $P,Q\in K$ and some $j\in\{0,1,2\}$.

For

$$
K=K_6^{\mathrm{rel}}(S,d),
$$

this reduces the target theorem to finitely many support-branch inequalities.

## 6. Observed transition support regimes

The following support regimes are empirical.  They are included to guide the
certificate but are not proof-level branch decompositions until verified by
interval arithmetic.

Along the $T=0$ curve, using $d=q-p$ as parameter, the observed transition
support patterns are approximately:

| Range | Support pattern | Support set |
|---:|---|---|
| $d=0$ | $(D_1),(P_3,D_2),(P_5)$ | $\{D_1,D_2,P_3,P_5\}$ |
| $0<d\lesssim0.0648$ | $(D_1),(P_3),(P_5,D_0)$ | $\{D_0,D_1,P_3,P_5\}$ |
| $0.0648\lesssim d\lesssim0.1005$ | $(D_2),(P_3),(P_5,D_0)$ | $\{D_0,D_2,P_3,P_5\}$ |
| $0.1005\lesssim d\lesssim0.545$ | $(D_1),(P_3,D_2),(P_5)$ | $\{D_1,D_2,P_3,P_5\}$ |
| $0.545\lesssim d<1$ | $(D_0),(D_2),(P_4,P_5)$ | $\{D_0,D_2,P_4,P_5\}$ |
| $d\to1$ | extra diagonal degeneracies | limiting set $\{D_0,D_2,P_4,P_5\}$ |

The contact pattern usually does not change exactly at $T=0$ along a slice.
The better interpretation is that $T=0$ is a diagonal-radius balance point
inside a stable support branch.

## 7. Analytic cusp from the diagonal branch

The branch change of $c_*$ creates a derivative jump at $T=0$.

Let

$$
D=\sqrt{4S^2-3}.
$$

On $T=0$ one has

$$
d=SD.
$$

On the quartic side $T<0$,

$$
c_*^4-c_*^2+pc_*-p^2=0,
\qquad
p=\frac{S-d}{2}.
$$

Differentiating with respect to $S$ at fixed $d$ and evaluating at $T=0$ gives

$$
c'_-= -\frac{D}{2D^2+3-D}.
$$

On the mixed side $T>0$,

$$
c_*=rac{S+d}{1+\sqrt{4S^2-3}},
$$

and evaluation at $T=0$ gives

$$
c'_+=-rac{D^2-D+3}{D(1+D)}.
$$

For $0<D<1$,

$$
c'_+<c'_-,
$$

so

$$
R'_+>R'_-,
\qquad R=1-c_*.
$$

This proves that the diagonal radius has an upward derivative jump at the
transition.

## 8. Near-limit branch formula

On the near-limit support branch

$$
(D_0),(D_2),(P_4,P_5),
$$

the right strict-line side has local direction

$$
W=\delta e_+-\gamma e_-,
$$

where $\gamma,\delta>0$ are the strict-line coefficients from `31012`.
Let

$$
N=\sqrt{\delta^2+\delta\gamma+\gamma^2}.
$$

The branch value for the side through $P_4,P_5$ and opposite supports $D_0,D_2$
is

$$
B_{0245}(S,d)=
\frac{(2R+1)(\delta+\gamma)-\delta s}{N},
$$

where

$$
R=1-c_*,
\qquad
s=a=1-\frac{S+d}{2}.
$$

Across $T=0$, the quantities $\delta,\gamma,s,N$ are smooth, while $R$ has the
one-sided derivative jump above.  Therefore

$$
B'_{0245,+}-B'_{0245,-}
=
\frac{2(\delta+\gamma)}{N}(R'_+-R'_-)>0.
$$

This proves the cusp mechanism for the near-limit branch.  It does not prove
the global branch inequality.

## 9. Remaining certificate obligations

To prove the target theorem, it remains to certify that every finite support
branch satisfies

$$
B_\alpha(S,d)\ge F_d(S_T(d)).
$$

The currently recommended branch split is:

1. the small nonsymmetric branch $(D_1),(P_3),(P_5,D_0)$;
2. the small nonsymmetric branch $(D_2),(P_3),(P_5,D_0)$;
3. the intermediate branch $(D_1),(P_3,D_2),(P_5)$;
4. the near-limit branch $(D_0),(D_2),(P_4,P_5)$;
5. endpoint degeneracies at $d=0$ and $d\to1$.

An interval certificate should use algebraic variables for

$$
S,d,c_*,\Delta,\lambda,\mu,x,y,
$$

where $\lambda$ and $\mu$ are the selected relaxed line-circle root parameters
for $P_3^{\mathrm{rel}}$ and $P_5^{\mathrm{rel}}$, and

$$
x=\cos\theta,
\qquad
 y=\sin\theta.
$$

Until these branch inequalities are certified, the constant-difference slice
minimum remains a lemma target.
