# Final Gap Fixes for the $407X$ Completion

Status: Proven

This file proves the remaining local estimates needed to make the $407X$ proof package complete as written.  It supplements

- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md), and
- [`407c_rigor_completion_details.md`](407c_rigor_completion_details.md).

Throughout use the notation of `4073` and `407a`.  In the left-high-sheet parameterization,

$$
r=1-\lambda,
\qquad
u=\gamma_5,
\qquad
y=Y/\lambda,
\qquad
\rho=\sqrt{r^2-r+1},
$$

$$
\beta\in\left[\max\left\{r,\frac12,\frac{1-r^2}{1+2r}\right\},1\right],
\qquad
m=\sqrt{\beta^2-\beta+1},
$$

and

$$
1-u=m/(r+\beta),
\qquad
B_5=\beta m/(r+\beta).
$$

Set

$$
\delta=(1-r)/(1+\rho),
\qquad
\eta_0=1-\sqrt{3}/2,
$$

and

$$
y_*=(r/(1-r))(m/(r+\beta)-1/2-(1-r)/(1+\rho)).
$$

The inequality $S<1/2$ gives $y<y_*$ whenever $B_5=T_+^{hi}$.

## 1. The stronger high-left envelope $y_*<1/10$

### Lemma 1.1

Under the realized left-high-sheet hypotheses,

$$
y_*<1/10.
$$

### Proof

For fixed $r$, the function

$$
\beta\mapsto\sqrt{\beta^2-\beta+1}/(r+\beta)
$$

is decreasing on the allowed interval.  Hence $y_*$ is maximized at

$$
\beta_0(r)=\max\left\{r,\frac12,\frac{1-r^2}{1+2r}\right\}.
$$

Let

$$
r_0=(\sqrt{3}-1)/2.
$$

#### Case 1: $0<r\le r_0$

Here $m/(r+\beta)\le1$.  Also

$$
\delta=(1-r)/(1+\rho)\ge1/3.
$$

Indeed this is equivalent to $2-3r\ge\rho$, and after squaring the difference is

$$
(2-3r)^2-\rho^2=(8r-3)(r-1)\ge0
$$

because $r\le r_0<3/8$.  Therefore

$$
y_*\le(r/(1-r))(1/2-1/3)<(3/5)(1/6)=1/10.
$$

#### Case 2: $r_0\le r\le1/2$

Here $\beta_0=1/2$, so

$$
m/(r+\beta)\le\sqrt{3}/(1+2r).
$$

We use the lower bound

$$
\delta\ge L(r):=2-\sqrt{3}+(1/2-r)/2.
$$

To verify it, note that $\delta\ge L$ is equivalent to

$$
1-r\ge L(1+\rho).
$$

Both sides are positive on $[r_0,1/2]$.  After squaring, the difference is

$$
(1-r-L)^2-L^2\rho^2
=-((r-1)(2r-1)/16)(2r^2+(8\sqrt{3}-17)r+56-32\sqrt{3}).
$$

The quadratic factor is negative on $[r_0,1/2]$: its derivative is $4r+8\sqrt{3}-17<0$, and its value at $r=r_0$ is $(157-91\sqrt{3})/2<0$.  Hence the squared difference is nonnegative.

Thus

$$
y_*\le G(r):=(r/(1-r))(\sqrt{3}/(1+2r)-1/2-2+\sqrt{3}-(1/2-r)/2).
$$

A direct simplification gives

$$
1/10-G(r)=P(r)/(20(r-1)(2r+1)),
$$

where

$$
P(r)=20r^3+(40\sqrt{3}-96)r^2+(40\sqrt{3}-57)r-2.
$$

The denominator is negative.  Also

$$
P'(r)=60r^2+(80\sqrt{3}-192)r+(40\sqrt{3}-57)>0
$$

on the interval, and

$$
P(1/2)=30\sqrt{3}-52<0.
$$

Hence $P(r)<0$, and therefore $G(r)<1/10$.

#### Case 3: $1/2\le r<1$

Here

$$
m/(r+\beta)\le\rho/(2r).
$$

Therefore

$$
y_*\le(r/(1-r))(\rho/(2r)-1/2-(1-r)/(1+\rho))=(\rho+1-3r)/(2(1+\rho)).
$$

The inequality that this last expression is $<1/10$ is equivalent to

$$
15r-4\rho-4>0.
$$

The derivative is

$$
15-2(2r-1)/\rho>0,
$$

because $2r-1<\rho$ for $0<r<1$.  At $r=1/2$, the expression is $7/2-2\sqrt{3}>0$.  Thus it is positive throughout $[1/2,1)$.

This proves $y_*<1/10$ in all cases.

## 2. The high-$r$ estimate in the $(T_+^{hi},T_-)$, $A_1=A_C$ subcase

### Lemma 2.1

Assume the left-high hypotheses, $r>8/15$, and $y_*>0$.  Then

$$
r<5/8,
\qquad
\beta<4/5.
$$

Consequently,

$$
m+2\rho-2+r/2<1.
$$

### Proof

Since $y_*>0$,

$$
m/(r+\beta)>1/2+\delta.
$$

Since $\beta\ge r$ and $m/(r+\beta)$ is decreasing in $\beta$,

$$
m/(r+\beta)\le\rho/(2r).
$$

Thus

$$
\rho/(2r)>1/2+(1-r)/(1+\rho).
$$

A direct simplification gives

$$
\rho/(2r)-1/2-(1-r)/(1+\rho)=((r-1)(3r-\rho-1))/(2r(1+\rho)).
$$

Since $r-1<0$, positivity implies

$$
3r<1+\rho.
$$

Because $r>8/15>1/3$, $3r-1$ is positive.  Squaring $3r-1<\rho$ gives

$$
(3r-1)^2<r^2-r+1,
$$

which simplifies to

$$
8r^2-5r<0.
$$

Therefore $r<5/8$.

For $r<5/8$,

$$
\delta=(1-r)/(1+\rho)\ge1/5.
$$

Indeed this is equivalent to $4-5r\ge\rho$, and after squaring the difference is

$$
(4-5r)^2-\rho^2=3(8r-5)(r-1)\ge0.
$$

Hence

$$
m/(r+\beta)>1/2+1/5=7/10.
$$

Suppose for contradiction that $\beta\ge4/5$.  For $\beta\in[4/5,1]$,

$$
(49/100)(\beta+8/15)^2-(\beta^2-\beta+1)\ge0.
$$

This is a concave quadratic in $\beta$, hence its minimum on $[4/5,1]$ occurs at an endpoint.  The endpoint values are $7/225$ and $3421/22500$, both positive.  Thus

$$
m\le(7/10)(\beta+8/15).
$$

Because $r>8/15$,

$$
\beta+8/15<\beta+r,
$$

so

$$
m/(r+\beta)<7/10,
$$

contradiction.  Hence $\beta<4/5$.

Since $\beta\ge1/2$, the function $\beta^2-\beta+1$ is increasing in $\beta$.  Therefore

$$
m^2<(4/5)^2-4/5+1=21/25<225/256,
$$

so $m<15/16$.

Finally, for $8/15<r<5/8$, the function $2\rho+r/2$ is increasing, and at $r=5/8$ one has $\rho=7/8$.  Hence

$$
2\rho-2+r/2<1/16.
$$

Combining gives

$$
m+2\rho-2+r/2<15/16+1/16=1.
$$

This proves the lemma.

## 3. The lower-sheet three-range estimate

### Lemma 3.1

Assume the left lower-sheet hypotheses in the hard CE2 overlap region.  Let

$$
r_0=(\sqrt{3}-1)/2,
\qquad
\eta_0=1-\sqrt{3}/2.
$$

Then for every $r\in[r_0,1/2]$,

$$
u+(1-r)/(1+\rho)+((1-r)/r)\eta_0>7/16.
$$

### Proof

Write

$$
\delta=(1-r)/(1+\rho),
\qquad
k=(1-r)/r.
$$

We split into three intervals.

#### Case 1: $r\le7/16$

Since $\rho<1$,

$$
\delta>(1-r)/2\ge9/32,
$$

and

$$
k\ge9/7.
$$

Thus

$$
u+\delta+k\eta_0>9/32+(9/7)(1-\sqrt{3}/2)>7/16.
$$

The final inequality is equivalent to $253>144\sqrt{3}$, true after squaring.

#### Case 2: $7/16\le r\le9/20$

Again $\delta>(1-r)/2$, so

$$
\delta>11/40,
$$

and

$$
k\ge11/9.
$$

Therefore

$$
u+\delta+k\eta_0>11/40+(11/9)(1-\sqrt{3}/2)>7/16.
$$

The final inequality is equivalent to $763>440\sqrt{3}$, true after squaring.

#### Case 3: $9/20\le r\le1/2$

The lower-sheet parameterization gives

$$
1-u\le\rho/(2r)\le\sqrt{301}/18.
$$

Hence

$$
u\ge1-\sqrt{301}/18.
$$

Also

$$
\delta\ge2-\sqrt{3},
\qquad
k\ge1.
$$

Therefore

$$
u+\delta+k\eta_0\ge4-3\sqrt{3}/2-\sqrt{301}/18>7/16.
$$

For example, using $\sqrt{3}<97/56$ and $\sqrt{301}<347/20$, the difference from $7/16$ is $>1/2520$.

This proves the lemma.

### Lemma 3.2

Under the same lower-sheet hypotheses, if $y\ge\eta_0$, then

$$
S>7/16,
\qquad
A_C>7/16.
$$

### Proof

The first inequality follows directly from Lemma 3.1 because $S=u+\delta+ky$ and $y\ge\eta_0$.

For the $A_C$ bound, $S<1/2$ gives

$$
y<(1/2-u-\delta)/k.
$$

Since $A_C=(1-r)(1-y)$ and $k=(1-r)/r$,

$$
A_C>1-3r/2+ru+r\delta.
$$

If $r\le7/16$, then $1-3r/2\ge11/32$, and because $r\ge r_0$ and $\delta>(1-r)/2\ge9/32$,

$$
r\delta>9(\sqrt{3}-1)/64.
$$

Thus

$$
A_C>11/32+9(\sqrt{3}-1)/64>7/16.
$$

If $7/16\le r\le1/2$, then $u\ge1-\rho/(2r)$ and $\delta\ge(1-r)/2$.  Therefore

$$
A_C>1-r/2+r(1-r)/2-\rho/2.
$$

On this interval,

$$
1-r/2\ge3/4,
\qquad
r(1-r)/2\ge63/512,
\qquad
\rho\le\sqrt{193}/16.
$$

Hence

$$
A_C>3/4+63/512-\sqrt{193}/32=(447-16\sqrt{193})/512>7/16,
$$

because $223>16\sqrt{193}$.

This proves the lemma.
