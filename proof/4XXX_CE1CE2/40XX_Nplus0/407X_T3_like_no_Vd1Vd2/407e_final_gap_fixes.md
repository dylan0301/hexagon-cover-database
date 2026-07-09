# Final Gap Fixes for the $407X$ Completion

Status: Proven

This file proves the remaining local estimates needed to make the $407X$ proof package complete as written.  It supplements

- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md), and
- [`407c_detailed_gap_closure.md`](407c_detailed_gap_closure.md).

Throughout use the notation of `4073` and `407a`.  In the left-high-sheet parameterization,

$$
r=1-\lambda,
\qquad
u=\gamma_5,
\qquad
y={Y\over\lambda},
\qquad
\rho=\sqrt{r^2-r+1},
$$

$$
\beta\in\left[\max\left(r,{1\over2},{1-r^2\over1+2r}\right),1\right],
\qquad
m=\sqrt{\beta^2-\beta+1},
$$

and

$$
1-u={m\over r+\beta},
\qquad
B_5={\beta m\over r+\beta}.
$$

Set

$$
\delta={1-r\over1+\rho},
\qquad
\eta_0=1-{\sqrt3\over2},
$$

and

$$
y_*={r\over1-r}\left({m\over r+\beta}-{1\over2}-{1-r\over1+ho}\right).
$$

The inequality $S<1/2$ gives $y<y_*$ whenever $B_5=T_+^{hi}$.

## 1. The stronger high-left envelope $y_*<1/10$

### Lemma 1.1

Under the realized left-high-sheet hypotheses,

$$
\boxed{y_*<{1\over10}.}
$$

### Proof

For fixed $r$, the function

$$
\beta\mapsto {\sqrt{\beta^2-\beta+1}\over r+\beta}
$$

is decreasing on the allowed interval.  Hence $y_*$ is maximized at

$$
\beta_0(r)=\max\left(r,{1\over2},{1-r^2\over1+2r}\right).
$$

Let

$$
r_0={\sqrt3-1\over2}.
$$

### Case 1: $0<r\le r_0$

Here $m/(r+\beta)\le1$.  Also

$$
\delta={1-r\over1+ho}\ge {1\over3}.
$$

Indeed this is equivalent to $2-3r\ge\rho$, and after squaring the difference is

$$
(2-3r)^2-\rho^2=(8r-3)(r-1)\ge0
$$

because $r\le r_0<3/8$.  Therefore

$$
y_*\le {r\over1-r}\left({1\over2}-{1\over3}\right)<{3\over5}\cdot{1\over6}={1\over10}.
$$

### Case 2: $r_0\le r\le1/2$

Here $\beta_0=1/2$, so

$$
{m\over r+\beta}\le{\sqrt3\over1+2r}.
$$

We use the lower bound

$$
\delta\ge L(r):=2-\sqrt3+{1/2-r\over2}.
$$

To verify it, note that $\delta\ge L$ is equivalent to

$$
1-r\ge L(1+ho).
$$

Both sides are positive on $[r_0,1/2]$.  After squaring, the difference is

$$
(1-r-L)^2-L^2\rho^2
=-{(r-1)(2r-1)\over16}
\left(2r^2+(8\sqrt3-17)r+56-32\sqrt3\right).
$$

The quadratic factor is negative on $[r_0,1/2]$: its derivative is $4r+8\sqrt3-17<0$, and its value at $r=r_0$ is $(157-91\sqrt3)/2<0$.  Hence the squared difference is nonnegative.

Thus

$$
y_*\le G(r):={r\over1-r}\left({\sqrt3\over1+2r}-{1\over2}-2+\sqrt3-{1/2-r\over2}\right).
$$

A direct simplification gives

$$
{1\over10}-G(r)=
{P(r)\over20(r-1)(2r+1)},
$$

where

$$
P(r)=20r^3+(40\sqrt3-96)r^2+(40\sqrt3-57)r-2.
$$

The denominator is negative.  Also

$$
P'(r)=60r^2+(80\sqrt3-192)r+(40\sqrt3-57)>0
$$

on the interval, and

$$
P(1/2)=30\sqrt3-52<0.
$$

Hence $P(r)<0$, and therefore $G(r)<1/10$.

### Case 3: $1/2\le r<1$

Here

$$
{m\over r+\beta}\le {\rho\over2r}.
$$

Therefore

$$
y_*\le {r\over1-r}\left({\rho\over2r}-{1\over2}-{1-r\over1+ho}\right)
={\rho+1-3r\over2(1+ho)}.
$$

The inequality that this last expression is $<1/10$ is equivalent to

$$
15r-4\rho-4>0.
$$

The derivative is

$$
15-{2(2r-1)\over\rho}>0,
$$

because $2r-1<\rho$ for $0<r<1$.  At $r=1/2$, the expression is $7/2-2\sqrt3>0$.  Thus it is positive throughout $[1/2,1)$.

This proves $y_*<1/10$ in all cases.

## 2. The missing high-$r$ estimate in the $(T_+^{hi},T_-)$, $A_1=A_C$ subcase

### Lemma 2.1

Assume the left-high hypotheses, $r>8/15$, and $y_*>0$.  Then

$$
\boxed{r<{5\over8}},
\qquad
\boxed{\beta<{4\over5}}.
$$

Consequently,

$$
\boxed{m+2\rho-2+{r\over2}<1.}
$$

### Proof

Since $y_*>0$,

$$
{m\over r+\beta}>{1\over2}+\delta.
$$

Since $\beta\ge r$ and the function $m/(r+\beta)$ is decreasing in $\beta$,

$$
{m\over r+\beta}\le {\rho\over2r}.
$$

Thus

$$
{\rho\over2r}>{1\over2}+{1-r\over1+ho}.
$$

A direct simplification gives

$$
{\rho\over2r}-{1\over2}-{1-r\over1+ho}
={ (r-1)(3r-ho-1)\over2r(1+ho)}.
$$

Since $r-1<0$, positivity implies

$$
3r<1+ho.
$$

Because $r>8/15>1/3$, the quantity $3r-1$ is positive.  Squaring $3r-1<\rho$ gives

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
\delta={1-r\over1+ho}\ge {1\over5}.
$$

Indeed this is equivalent to $4-5r\ge\rho$, and after squaring the difference is

$$
(4-5r)^2-ho^2=3(8r-5)(r-1)\ge0.
$$

Hence

$$
{m\over r+eta}>{1\over2}+{1\over5}={7\over10}.
$$

Suppose for contradiction that $\beta\ge4/5$.  For $\beta\in[4/5,1]$,

$$
{49\over100}\left(\beta+{8\over15}\right)^2-(\beta^2-\beta+1)\ge0.
$$

This is a concave quadratic in $\beta$, hence its minimum on $[4/5,1]$ occurs at an endpoint.  The endpoint values are $7/225$ and $3421/22500$, both positive.  Thus

$$
m\le {7\over10}\left(\beta+{8\over15}\right).
$$

Because $r>8/15$,

$$
\beta+{8\over15}<\beta+r,
$$

so

$$
{m\over r+eta}<{7\over10},
$$

contradiction.  Hence $\beta<4/5$.

Since $\beta\ge1/2$, the function $\beta^2-eta+1$ is increasing in $\beta$.  Therefore

$$
m^2<\left({4\over5}\right)^2-{4\over5}+1={21\over25}<{225\over256},
$$

so $m<15/16$.

Finally, for $8/15<r<5/8$, the function $2\rho+r/2$ is increasing, and at $r=5/8$ one has $\rho=7/8$.  Hence

$$
2\rho-2+{r\over2}< {1\over16}.
$$

Combining gives

$$
m+2\rho-2+{r\over2}<{15\over16}+{1\over16}=1.
$$

This proves the lemma.

## 3. The lower-sheet three-range estimate

### Lemma 3.1

Assume the left lower-sheet hypotheses in the hard CE2 overlap region.  Let

$$
r_0={\sqrt3-1\over2},
\qquad
\eta_0=1-{\sqrt3\over2}.
$$

Then for every $r\in[r_0,1/2]$,

$$
\boxed{u+{1-r\over1+ho}+{1-r\over r}\eta_0>{7\over16}.}
$$

### Proof

Write

$$
\delta={1-r\over1+ho},\qquad k={1-r\over r}.
$$

We split into three intervals.

### Case 1: $r\le7/16$

Since $\rho<1$,

$$
\delta>{1-r\over2}\ge {9\over32},
$$

and

$$
k\ge {9\over7}.
$$

Thus

$$
u+\delta+k\eta_0>{9\over32}+{9\over7}\left(1-{\sqrt3\over2}\right)>{7\over16}.
$$

The final inequality is equivalent to $253>144\sqrt3$, true after squaring.

### Case 2: $7/16\le r\le9/20$

Again $\delta>(1-r)/2$, so

$$
\delta>{11\over40},
$$

and

$$
k\ge {11\over9}.
$$

Therefore

$$
u+\delta+k\eta_0>{11\over40}+{11\over9}\left(1-{\sqrt3\over2}\right)>{7\over16}.
$$

The final inequality is equivalent to $763>440\sqrt3$, true after squaring.

### Case 3: $9/20\le r\le1/2$

The lower-sheet parameterization gives

$$
1-u\le {\rho\over2r}\le {\sqrt{301}\over18}.
$$

Hence

$$
u\ge1-{\sqrt{301}\over18}.
$$

Also

$$
\delta\ge2-\sqrt3,\qquad k\ge1.
$$

Therefore

$$
u+\delta+k\eta_0
\ge
4-{3\sqrt3\over2}-{\sqrt{301}\over18}>{7\over16}.
$$

For example, using $\sqrt3<97/56$ and $\sqrt{301}<347/20$, the difference from $7/16$ is $>1/2520$.

This proves the lemma.

### Lemma 3.2

Under the same lower-sheet hypotheses, if $y\ge\eta_0$, then

$$
\boxed{S>{7\over16}},\qquad
\boxed{A_C>{7\over16}}.
$$

### Proof

The first inequality follows directly from Lemma 3.1 because $S=u+\delta+ky$ and $y\ge\eta_0$.

For the $A_C$ bound, $S<1/2$ gives

$$
y<{1/2-u-\delta\over k}.
$$

Since $A_C=(1-r)(1-y)$ and $k=(1-r)/r$,

$$
A_C>1-{3r\over2}+ru+r\delta.
$$

If $r\le7/16$, then $1-3r/2\ge11/32$, and because $r\ge r_0$ and $\delta>(1-r)/2\ge9/32$,

$$
r\delta>{9(\sqrt3-1)\over64}.
$$

Thus

$$
A_C>{11\over32}+{9(\sqrt3-1)\over64}>{7\over16}.
$$

If $7/16\le r\le1/2$, then $u\ge1-ho/(2r)$ and $\delta\ge(1-r)/2$.  Therefore

$$
A_C>1-{r\over2}+{r(1-r)\over2}-{\rho\over2}.
$$

On this interval,

$$
1-{r\over2}\ge {3\over4},\qquad {r(1-r)\over2}\ge {63\over512},\qquad \rho\le {\sqrt{193}\over16}.
$$

Hence

$$
A_C>{3\over4}+{63\over512}- {\sqrt{193}\over32}
={447-16\sqrt{193}\over512}>{7\over16},
$$

because $223>16\sqrt{193}$.

This proves the lemma.
