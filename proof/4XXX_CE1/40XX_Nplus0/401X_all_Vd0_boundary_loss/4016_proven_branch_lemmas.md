# Proven Branch Lemmas for the CE1/CE2 Vd0 Boundary-Loss Reduction

Status: Proven local lemmas, with remaining branches recorded elsewhere

This file records the branch lemmas currently proved for the reduction in `551_setup_and_reduction.md`.

Throughout, use

$$
u=1-t, \qquad w=t-s, \qquad s=1-u-w,
$$

and on the main $r>1$ C-geometry branch use

$$
R={1\over r}, \qquad S=\sqrt{1-R+R^2}, \qquad \delta={R\over 1+S}.
$$

The radial exits are

$$
\gamma_1=1-ru,
$$

and

$$
\gamma_5=u-\delta-{R\over 1-R}w.
$$

The objective is

$$
F=B(s,1-\gamma_5)+B(u,1-\gamma_1)=B_5+B_1.
$$

## 1. The branch $(L,\mathrm{Full})$

### Lemma

If $B_5=L$ and $B_1=\mathrm{Full}$, then $F<1$.

### Proof

On this branch,

$$
B_5=\ell(\gamma_5), \qquad B_1=1-u.
$$

The Full condition for $B_1=B(u,1-\gamma_1)$ gives

$$
1-\gamma_1=ru\le1-u,
$$

hence

$$
u\le {1\over r+1}.
$$

The C-geometry gives

$$
\gamma_5=u-{1\over D+r}-{w\over r-1}<u-{1\over D+r}.
$$

Set

$$
\delta_r={1\over D+r}.
$$

The low branch satisfies

$$
\ell(\eta)\le2\eta+5\eta^2 \qquad(0\le\eta\le1/8).
$$

On the present branch this bound applies because $\gamma_5\le u-\delta_r\le1/(r+1)-1/(D+r)\le1/8$.  Therefore it is enough to prove

$$
2(u-\delta_r)+5(u-\delta_r)^2<u.
$$

The left side is increasing in $u$ on the allowed interval, so it suffices to check $u=1/(r+1)$.  Substitution gives

$$
2\delta_r-u-5(u-\delta_r)^2 = {2Dr+12D-2r^2+7r-11\over (D+r)^2(r+1)^2}.
$$

The denominator is positive.  Since

$$
D=\sqrt{r^2-r+1}>r-{1\over2},
$$

the numerator is greater than

$$
2r\left(r-{1\over2}\right)+12\left(r-{1\over2}\right)-2r^2+7r-11=18r-17>0.
$$

Thus $\ell(\gamma_5)<u$, and

$$
F=\ell(\gamma_5)+1-u<1.
$$

## 2. The branch $(T_-,\mathrm{Full})$

### Lemma

If $B_5=T_-$ and $B_1=\mathrm{Full}$, then $F<1$.

### Proof sketch with exact reduction

Write $B_5=b_5$.  Since $B_5=T_-$,

$$
((s+b_5)^2-1)(1-\gamma_5)^2+s(1-\gamma_5)-s^2=0.
$$

For a threshold $x$, define

$$
\Psi_5(x)=((s+x)^2-1)(1-\gamma_5)^2+s(1-\gamma_5)-s^2.
$$

Then

$$
{d\over dx}\Psi_5(x)=2(s+x)(1-\gamma_5)^2>0,
$$

so $b_5<u$ is equivalent to $\Psi_5(u)>0$.

Set

$$
K=1-\gamma_5-s, \qquad y={s\over K}.
$$

The case $y\ge1$ reduces to a two-variable calculus lemma.  Let

$$
v={\sqrt{y^2+y+1}\over y+1}, \qquad \lambda={r-1\over r}, \qquad \delta={1\over \sqrt{r^2-r+1}+r}.
$$

The $T_-$ separator gives

$$
K\le K_+:={v\over y+1}.
$$

Since

$$
w=\lambda(K-\delta),
$$

it is enough to show

$$
\lambda(K_+-\delta)<1-v.
$$

The Full condition for $B_1$ implies

$$
U(r,y):=1-y{v\over y+1}-\lambda\left({v\over y+1}-\delta\right)-{1\over r+1}\le0.
$$

The needed implication is

$$
U(r,y)\le0\quad\Longrightarrow\quad P(r,y):=1-v-\lambda\left({v\over y+1}-\delta\right)>0.
$$

In variables $R=1/r$ and $q=1/(y+1)$, this follows from:

1. $U\le0$ implies $q<R$ by monotonicity of $U$ in $q$ and the endpoint check $U(R)>0$.
2. $q\le R$ implies $P>0$ by the square-root bounds
   $$
   \sqrt{1-q+q^2}\le 1-{q\over2}+{q^2\over2}, \qquad \sqrt{1-R+R^2}\le 1-{R\over2}+{R^2\over2}.
   $$

The case $0<y<1$ is impossible.  Indeed, the Full condition forces

$$
K\ge K_F={1+\lambda\delta-{1\over r+1}\over y+\lambda},
$$

while $\gamma_5\ge0$ gives

$$
K\le {1\over1+y}.
$$

For $0<y<1$ one checks

$$
K_F>{1\over1+y}.
$$

The check reduces to the positivity of

$$
N(r,y)=(y+1)r^2+r+1-\sqrt{r^2-r+1}(y+1)(r+1),
$$

which is linear in $y$ and positive at $y=0$ and $y=1$ after squaring.  Hence no such point exists.

Therefore $b_5<u$, and since $B_1=1-u$, we have $F<1$.

## 3. The branch $(\mathrm{Full},L)$

### Lemma

If $B_5=\mathrm{Full}$ and $B_1=L$, then $F<1$.

### Proof status

This branch is proved by two pieces.

For the tight horn $0<r-1\le1/50$, write $r=1+e$ and $\eta=\gamma_1$.  The Low condition implies

$$
e\ge {\eta(2-\eta)\over1-2\eta},
$$

and therefore $\eta<1/100$.  The Full condition implies

$$
s\ge {\eta+e\delta\over1-e}, \qquad \delta={1\over\sqrt{1+e+e^2}+1+e}.
$$

Using

$$
\sqrt{1+e+e^2}\le1+{e\over2}+{3e^2\over8},
$$

one obtains

$$
s>2\eta+3\eta^2.
$$

The low branch satisfies

$$
\ell(\eta)<2\eta+2\eta^2 \qquad(0<\eta<1/100).
$$

Thus $\ell(\eta)<s$, and $F=1-s+\ell(\eta)<1$.

For the far region $r-1\ge1/50$, the bad set is reduced to the two inequalities

$$
\Delta(R,\eta)\le0, \qquad H(R,\eta)\ge0,
$$

where

$$
R={1\over r}, \qquad \eta=\gamma_1, \qquad u=(1-\eta)R,
$$

$$
\ell=\ell(\eta),
$$

$$
\Delta=(u+\ell)^4-(u+\ell)^2+u\ell,
$$

and

$$
H=u-\delta_R-{R(1-u)\over1-R}+\ell{2R-1\over1-R}, \qquad \delta_R={R\over\sqrt{1-R+R^2}+1}.
$$

The interval verifier in `proof/4XXX_CE1/40XX_Nplus0/401X_all_Vd0_boundary_loss/403X_boundary_loss_experiments/4034_verify_full_L_interval.py` checks that every box satisfies either $\inf\Delta>0$ or $\sup H<0$.  The recorded run has $2307$ certified boxes and no unresolved boxes.

## 4. The branch $(\mathrm{Full},T_-)$

### Lemma

If $B_5=\mathrm{Full}$ and $B_1=T_-$, then $F<1$.

### Proof

Exact Full feasibility for $B_5=B(s,1-\gamma_5)$ gives $s\le1/2$ and

$$
\gamma_5\ge s.
$$

The alternative $s>1/2$ would require $\gamma_5\ge1-s=u+w$, but

$$
\gamma_5=u-\delta-{w\over r-1}<u<u+w.
$$

So $s>1/2$ is impossible.

The right $T_-$ output $B_1=b_1$ satisfies

$$
((u+b_1)^2-1)(1-\gamma_1)^2+u(1-\gamma_1)-u^2=0.
$$

Since $1-\gamma_1=ru$, this becomes

$$
(u+b_1)^2=1-{r-1\over r^2}=S^2.
$$

Thus

$$
B_1=S-u.
$$

The Full condition $\gamma_5\ge s$ implies

$$
s\ge S-u,
$$

by the same rearrangement used in the $(\mathrm{Full},T_-)$ horn proof.  Hence $B_1\le s$, while $B_5=1-s$.  Since the non-covered case has $w>0$ and the branch is maximal, strictness gives $F<1$.

## 5. The branch $(L,T_+)$

### Lemma

If $B_5=L$ and $B_1=T_+$, then $F<1$.

### Proof status

For $r\ge10$, this is proved analytically.  Put $R=1/r$, $x=ru$, and

$$
\tau=x(1+R)-1>0.
$$

Write the right $T_+$ output as

$$
B_1=1-u-d.
$$

The $T_+$ equation gives

$$
E(d)=((1-d)^2-1)x^2+(1-u-d)x-(1-u-d)^2=0.
$$

For $R\le1/10$ one proves

$$
d\ge {\tau\over2}.
$$

The left Low term satisfies

$$
\gamma_5<u-\delta_R, \qquad \delta_R={R\over\sqrt{1-R+R^2}+1},
$$

and the quadratic Low estimate gives

$$
\ell(\gamma_5)<u+{\tau\over2}.
$$

Therefore

$$
F=\ell(\gamma_5)+1-u-d<1.
$$

For $1<r<10$, the corrected interval verifier `proof/4XXX_CE1/40XX_Nplus0/401X_all_Vd0_boundary_loss/403X_boundary_loss_experiments/4031_attempt_interval_L_Tplus_loss_exact_corrected.py` uses the exact loss equation

$$
E(d)=y\tau-Ad-(1-c^2)d^2
$$

and certifies all boxes by either $\ell<u$ or $E(\ell-u)>0$, with no unresolved boxes in the recorded run.

## 6. Left $T_+^{hi}$ frontier lemma

### Lemma

If the left branch $B_5=B(s,1-\gamma_5)$ is realized as $T_+^{hi}$, then

$$
w\le1-S.
$$

Equivalently,

$$
s\ge S-u.
$$

### Proof

Let $c_L(x)$ be the unique root of

$$
c^4-c^2+xc-x^2=0
$$

on the relevant frontier.  A left $T_+^{hi}$ branch is realized only if

$$
c_5(s):=1-\gamma_5\le c_L(s).
$$

The function $c_5(s)$ is affine decreasing in $s$.

The function $c_L(s)$ is convex.  Indeed, implicit differentiation of

$$
f(c,s)=c^4-c^2+sc-s^2=0
$$

gives $c_L''(s)>0$ on the branch $\sqrt3/2\le c\le1$.

Assume $w>1-S$, equivalently $s<S-u$.  Put $X=S-u$.  One checks that

$$
c_5(0)\ge c_L(0)
$$

and

$$
c_5(X)\ge c_L(X).
$$

The second endpoint check reduces to the positivity of a polynomial

$$
P(R,S)=A(R)S+B(R),
$$

where

$$
A(R)=-8R^5+20R^4-42R^3+46R^2-34R+10,
$$

and

$$
B(R)=8R^6-24R^5+55R^4-73R^3+71R^2-39R+10.
$$

Both the needed positivity of $B$ and the inequality $B>|A|S$ are checked by Bernstein-positive polynomial expansions on $0<R<1$.

Since $c_5-c_L$ is concave and nonnegative at $0$ and $X$, it is nonnegative throughout $[0,X]$, and strictly positive in the interior.  Hence for $s<X$, one has $c_5(s)>c_L(s)$, contradicting left $T_+^{hi}$ realization.  Therefore $s\ge X=S-u$.

## 7. Consequences for left $T_+$ branches

### $(T_+,\mathrm{Full})$

This branch is impossible.  If $B_1=\mathrm{Full}$, then $u\le1/(r+1)$.  If $B_5=T_+$, then $s\le1/2$, hence $w\ge1/2-u$.  But $\gamma_5\ge0$ gives $w\le(r-1)(u-\delta)$.  Combining the inequalities would imply

$$
\sqrt{r^2-r+1}\ge r+2,
$$

which is impossible.

### $(T_+^{hi},L)$

This branch is proved.  If $B_1=L=\ell(\gamma_1)$, set $C=1-\gamma_1$ and $L=Ck$.  The Low realization gives

$$
k\le R\le1-k.
$$

The same convexity/endpoint comparison used for $c_L$ shows that $s<L$ would force

$$
c_5(s)>c_L(s),
$$

contradicting $T_+^{hi}$ realization.  Hence $s\ge L$, and since left $T_+$ is non-Full,

$$
F=B_5+L<(1-s)+s=1.
$$

### $(T_+^{lo},L)$

On the lower sheet,

$$
B_5\le{1-\gamma_5\over2}\le{1\over2}.
$$

Also

$$
\ell(\gamma_1)\le{\sqrt3\over4}.
$$

Thus

$$
F\le{1\over2}+{\sqrt3\over4}<1.
$$

### $(T_+^{hi},T_-)$

By the left $T_+^{hi}$ frontier lemma,

$$
s\ge S-u.
$$

For the right $T_-$ branch, the output is exactly

$$
B_1=S-u.
$$

Therefore $B_1\le s$, while $B_5<1-s$.  Hence $F<1$.

### $(T_+^{hi},T_+^{hi})$

This branch is impossible.  Right $T_+^{hi}$ gives

$$
u\le\min(RS,S/2).
$$

Under this bound, the left radial requirement satisfies

$$
c_5(s)>c_L(s)
$$

for all $0\le s\le1/2$, by another convexity/endpoint comparison.  This contradicts left $T_+^{hi}$ realization.

## 8. Remaining branches

The only branches in this package not yet certified are lower-sheet $T_+$ branches:

$$
(T_+^{lo},T_-), \qquad (T_+^{lo},T_+^{hi}), \qquad (T_+^{lo},T_+^{lo}).
$$

Numerical sampling finds these branches but with visible gap.  A typical best sample has

$$
(T_+^{lo},T_+^{hi}),\qquad F\approx0.91965,
$$

so

$$
1-F\approx0.08035.
$$

No proof of a uniform analytic bound is included here.  This is the main remaining obligation for the full $F<1$ branch proof.
