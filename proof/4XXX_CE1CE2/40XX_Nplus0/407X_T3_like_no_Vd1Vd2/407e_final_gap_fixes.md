# Final Gap Fixes for the $407X$ Completion

Status: Proven

This file proves the remaining local estimates needed to make the $407X$ proof package complete as written.  It supplements

- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md), and
- [`407c_detailed_gap_closure.md`](407c_detailed_gap_closure.md).

Throughout use the notation of `4073` and `407a`.  In the left-high-sheet parameterization,

$$
r=1-λ,
\qquad
u=γ_5,
\qquad
y=Y/λ,
\qquad
ρ=sqrt(r^2-r+1),
$$

$$
β∈[max(r,1/2,(1-r^2)/(1+2r)),1],
\qquad
m=sqrt(β^2-β+1),
$$

and

$$
1-u=m/(r+β),
\qquad
B_5=βm/(r+β).
$$

Set

$$
δ=(1-r)/(1+ρ),
\qquad
η_0=1-sqrt(3)/2,
$$

and

$$
y_*=(r/(1-r))(m/(r+β)-1/2-(1-r)/(1+ρ)).
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
β↦sqrt(β^2-β+1)/(r+β)
$$

is decreasing on the allowed interval.  Hence $y_*$ is maximized at

$$
β_0(r)=max(r,1/2,(1-r^2)/(1+2r)).
$$

Let

$$
r_0=(sqrt(3)-1)/2.
$$

#### Case 1: $0<r≤r_0$

Here $m/(r+β)≤1$.  Also

$$
δ=(1-r)/(1+ρ)≥1/3.
$$

Indeed this is equivalent to $2-3r≥ρ$, and after squaring the difference is

$$
(2-3r)^2-ρ^2=(8r-3)(r-1)≥0
$$

because $r≤r_0<3/8$.  Therefore

$$
y_*≤(r/(1-r))(1/2-1/3)<(3/5)(1/6)=1/10.
$$

#### Case 2: $r_0≤r≤1/2$

Here $β_0=1/2$, so

$$
m/(r+β)≤sqrt(3)/(1+2r).
$$

We use the lower bound

$$
δ≥L(r):=2-sqrt(3)+(1/2-r)/2.
$$

To verify it, note that $δ≥L$ is equivalent to

$$
1-r≥L(1+ρ).
$$

Both sides are positive on $[r_0,1/2]$.  After squaring, the difference is

$$
(1-r-L)^2-L^2ρ^2
=-((r-1)(2r-1)/16)(2r^2+(8sqrt(3)-17)r+56-32sqrt(3)).
$$

The quadratic factor is negative on $[r_0,1/2]$: its derivative is $4r+8sqrt(3)-17<0$, and its value at $r=r_0$ is $(157-91sqrt(3))/2<0$.  Hence the squared difference is nonnegative.

Thus

$$
y_*≤G(r):=(r/(1-r))(sqrt(3)/(1+2r)-1/2-2+sqrt(3)-(1/2-r)/2).
$$

A direct simplification gives

$$
1/10-G(r)=P(r)/(20(r-1)(2r+1)),
$$

where

$$
P(r)=20r^3+(40sqrt(3)-96)r^2+(40sqrt(3)-57)r-2.
$$

The denominator is negative.  Also

$$
P'(r)=60r^2+(80sqrt(3)-192)r+(40sqrt(3)-57)>0
$$

on the interval, and

$$
P(1/2)=30sqrt(3)-52<0.
$$

Hence $P(r)<0$, and therefore $G(r)<1/10$.

#### Case 3: $1/2≤r<1$

Here

$$
m/(r+β)≤ρ/(2r).
$$

Therefore

$$
y_*≤(r/(1-r))(ρ/(2r)-1/2-(1-r)/(1+ρ))=(ρ+1-3r)/(2(1+ρ)).
$$

The inequality that this last expression is $<1/10$ is equivalent to

$$
15r-4ρ-4>0.
$$

The derivative is

$$
15-2(2r-1)/ρ>0,
$$

because $2r-1<ρ$ for $0<r<1$.  At $r=1/2$, the expression is $7/2-2sqrt(3)>0$.  Thus it is positive throughout $[1/2,1)$.

This proves $y_*<1/10$ in all cases.

## 2. The high-$r$ estimate in the $(T_+^{hi},T_-)$, $A_1=A_C$ subcase

### Lemma 2.1

Assume the left-high hypotheses, $r>8/15$, and $y_*>0$.  Then

$$
r<5/8,
\qquad
β<4/5.
$$

Consequently,

$$
m+2ρ-2+r/2<1.
$$

### Proof

Since $y_*>0$,

$$
m/(r+β)>1/2+δ.
$$

Since $β≥r$ and $m/(r+β)$ is decreasing in $β$,

$$
m/(r+β)≤ρ/(2r).
$$

Thus

$$
ρ/(2r)>1/2+(1-r)/(1+ρ).
$$

A direct simplification gives

$$
ρ/(2r)-1/2-(1-r)/(1+ρ)=((r-1)(3r-ρ-1))/(2r(1+ρ)).
$$

Since $r-1<0$, positivity implies

$$
3r<1+ρ.
$$

Because $r>8/15>1/3$, $3r-1$ is positive.  Squaring $3r-1<ρ$ gives

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
δ=(1-r)/(1+ρ)≥1/5.
$$

Indeed this is equivalent to $4-5r≥ρ$, and after squaring the difference is

$$
(4-5r)^2-ρ^2=3(8r-5)(r-1)≥0.
$$

Hence

$$
m/(r+β)>1/2+1/5=7/10.
$$

Suppose for contradiction that $β≥4/5$.  For $β∈[4/5,1]$,

$$
(49/100)(β+8/15)^2-(β^2-β+1)≥0.
$$

This is a concave quadratic in $β$, hence its minimum on $[4/5,1]$ occurs at an endpoint.  The endpoint values are $7/225$ and $3421/22500$, both positive.  Thus

$$
m≤(7/10)(β+8/15).
$$

Because $r>8/15$,

$$
β+8/15<β+r,
$$

so

$$
m/(r+β)<7/10,
$$

contradiction.  Hence $β<4/5$.

Since $β≥1/2$, the function $β^2-β+1$ is increasing in $β$.  Therefore

$$
m^2<(4/5)^2-4/5+1=21/25<225/256,
$$

so $m<15/16$.

Finally, for $8/15<r<5/8$, the function $2ρ+r/2$ is increasing, and at $r=5/8$ one has $ρ=7/8$.  Hence

$$
2ρ-2+r/2<1/16.
$$

Combining gives

$$
m+2ρ-2+r/2<15/16+1/16=1.
$$

This proves the lemma.

## 3. The lower-sheet three-range estimate

### Lemma 3.1

Assume the left lower-sheet hypotheses in the hard CE2 overlap region.  Let

$$
r_0=(sqrt(3)-1)/2,
\qquad
η_0=1-sqrt(3)/2.
$$

Then for every $r∈[r_0,1/2]$,

$$
u+(1-r)/(1+ρ)+((1-r)/r)η_0>7/16.
$$

### Proof

Write

$$
δ=(1-r)/(1+ρ),
\qquad
k=(1-r)/r.
$$

We split into three intervals.

#### Case 1: $r≤7/16$

Since $ρ<1$,

$$
δ>(1-r)/2≥9/32,
$$

and

$$
k≥9/7.
$$

Thus

$$
u+δ+kη_0>9/32+(9/7)(1-sqrt(3)/2)>7/16.
$$

The final inequality is equivalent to $253>144sqrt(3)$, true after squaring.

#### Case 2: $7/16≤r≤9/20$

Again $δ>(1-r)/2$, so

$$
δ>11/40,
$$

and

$$
k≥11/9.
$$

Therefore

$$
u+δ+kη_0>11/40+(11/9)(1-sqrt(3)/2)>7/16.
$$

The final inequality is equivalent to $763>440sqrt(3)$, true after squaring.

#### Case 3: $9/20≤r≤1/2$

The lower-sheet parameterization gives

$$
1-u≤ρ/(2r)≤sqrt(301)/18.
$$

Hence

$$
u≥1-sqrt(301)/18.
$$

Also

$$
δ≥2-sqrt(3),
\qquad
k≥1.
$$

Therefore

$$
u+δ+kη_0≥4-3sqrt(3)/2-sqrt(301)/18>7/16.
$$

For example, using $sqrt(3)<97/56$ and $sqrt(301)<347/20$, the difference from $7/16$ is $>1/2520$.

This proves the lemma.

### Lemma 3.2

Under the same lower-sheet hypotheses, if $y≥η_0$, then

$$
S>7/16,
\qquad
A_C>7/16.
$$

### Proof

The first inequality follows directly from Lemma 3.1 because $S=u+δ+ky$ and $y≥η_0$.

For the $A_C$ bound, $S<1/2$ gives

$$
y<(1/2-u-δ)/k.
$$

Since $A_C=(1-r)(1-y)$ and $k=(1-r)/r$,

$$
A_C>1-3r/2+ru+rδ.
$$

If $r≤7/16$, then $1-3r/2≥11/32$, and because $r≥r_0$ and $δ>(1-r)/2≥9/32$,

$$
rδ>9(sqrt(3)-1)/64.
$$

Thus

$$
A_C>11/32+9(sqrt(3)-1)/64>7/16.
$$

If $7/16≤r≤1/2$, then $u≥1-ρ/(2r)$ and $δ≥(1-r)/2$.  Therefore

$$
A_C>1-r/2+r(1-r)/2-ρ/2.
$$

On this interval,

$$
1-r/2≥3/4,
\qquad
r(1-r)/2≥63/512,
\qquad
ρ≤sqrt(193)/16.
$$

Hence

$$
A_C>3/4+63/512-sqrt(193)/32=(447-16sqrt(193))/512>7/16,
$$

because $223>16sqrt(193)$.

This proves the lemma.
