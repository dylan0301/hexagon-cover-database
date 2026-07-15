# Exact CE2 Two-Gap Completion of the All-Vd0 Boundary-Loss Matrix

Status: Proven

This note proves the two-gap part of the CE2, all-Vd0, nonsupercritical
boundary-loss obstruction. Together with the no-gap proof in `4014` and the
one-gap proof in `401d`, it completes the CE2 half of `401X`.

## 1. Exact endpoint reduction

Use the exact reduction and notation from
[`401c_CE2_remaining_obligations.md`](401c_CE2_remaining_obligations.md).
After reflection, put

$$
0<w\le\frac12,
\qquad
r=1-w,
\qquad
K=\sqrt{1-wr},
$$

and

$$
z=\frac{w}{1+K},
\qquad
\zeta=\frac{r}{1+K}.
$$

Write the two far-end inputs and radial demands as

$$
p=w\alpha,
\qquad
q=r\beta.
$$

The strict CE2 endpoint inequalities are

$$
\boxed{
\beta+p>1+z,
\qquad
\alpha+q>1+\zeta.
}
$$

For

$$
\Phi_s(c)=\widehat B_c(sc),
$$

the remaining target is

$$
\boxed{
\Phi_w(\alpha)+\Phi_r(\beta)<1.
}
$$

The exact four-label theorem in
[`2011_capped_demand_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md),
together with the branch eliminations in `401c`, leaves only

$$
(T_+^{hi},L),
\qquad
(L,T_+^{hi}),
\qquad
(T_+^{hi},T_-),
\qquad
(T_+^{hi},T_+^{hi}).
$$

We prove all four below.

Throughout, set

$$
h(t)=\sqrt{1-t+t^2}.
$$

The identity

$$
h(t)=h(1-t)
$$

will be used without further comment.

## 2. Selected branch parametrizations

On an $L$ frontier, if the output-to-radial ratio is $k$, then

$$
c=h(k),
\qquad
B=kh(k),
\qquad
0\le k\le\frac12.
$$

For the small-side $L$ label, the ordered Cell-$L$ half gives $k\le w$.
For the large-side label, put $X=r+k$ and $C=h(k)^2$. The exact transition
factorization is

$$
\frac qC=(X-1)G_k(X)=(k-w)G_k(X),
$$

where

$$
G_k(X)=CX^3+CX^2-k(1-k)X+k^2.
$$

The proof in `401b`, Section 3 shows $G_k(X)>0$ for $X\ge k$: for $k>0$,

$$
G_k'(X)
\ge
k(1+2k-k^2+3k^3)>0,
$$

and $G_k(k)>0$; the case $k=0$ is immediate. Thus the Cell-$L$ selector
$q\le0$ gives $k\le w$ on the large side as well. Consequently both
remaining $L$ labels satisfy

$$
0\le k\le w.
$$

On the small-side $T_+^{hi}$ frontier, write

$$
\alpha=\frac{h(x)}{w+x},
\qquad
\Phi_w(\alpha)=x\alpha.
$$

The genuine high-component selector gives $x\ge1/2$. The Cell-$T$ selector
polynomial is

$$
q=h(x)^2x
\left(
\frac{w}{(w+x)^2}-(1-x)
\right).
$$

Its numerator factors as

$$
w-(1-x)(w+x)^2
=(x-r)(x^2+wx-w).
$$

The second factor is nonnegative when $x\ge1/2$ and $w\le1/2$. Therefore
$q\ge0$ gives $x\ge r$. The nonsupercritical cap gives $x\le1$, with
$x=1$ assigned to Full. Thus a non-Full high label has

$$
r\le x<1.
$$

Similarly, the large-side high frontier has

$$
\beta=\frac{h(y)}{r+y},
\qquad
\Phi_r(\beta)=y\beta,
\qquad
r\le y<1.
$$

Here the ordered half gives $y\ge r\ge1/2$, so the genuine component selector
is automatic. The Cell-$T$ selector numerator factors as

$$
(y-w)(y^2+ry-r),
$$

and

$$
y^2+ry-r\ge r(2r-1)\ge0.
$$

Finally, the large-side $T_-$ frontier has

$$
\beta=\frac{K}{r+y},
\qquad
\Phi_r(\beta)=y\beta=K-r\beta.
$$

Its selector factors as

$$
q=K^2r
\left(
\frac{y}{(r+y)^2}-w
\right),
$$

and

$$
y-w(r+y)^2=(y-w)(r^2-wy).
$$

Since the second factor is nonnegative for $y\le r$, the selected range is

$$
w\le y\le r.
$$

The component selector is also automatic here because the larger demand
coordinate is $r\beta$ and $r\ge1/2$.

These are selected geometric components of the exact safe map; no formal
root from the discarded high sheet is used.

## 3. The pair $(L,T_+^{hi})$

Parameterize the small $L$ and large high labels by

$$
\alpha=h(k),
\qquad
\Phi_w(\alpha)=kh(k),
\qquad
0\le k\le w,
$$

and

$$
\beta=\frac{h(t)}{r+t},
\qquad
\Phi_r(\beta)=\frac{th(t)}{r+t},
\qquad
r\le t<1.
$$

Put

$$
f(k)=kh(k),
\qquad
d_r(t)=\frac{h(t)}{r+t},
\qquad
g_r(t)=\frac{th(t)}{r+t}.
$$

Direct differentiation gives

$$
f'(k)=\frac{4k^2-3k+2}{2h(k)}>0.
$$

The derivative of $d_r$ has the sign of

$$
t(2r+1)-(r+2)<0
$$

for $t\le1$, while the numerator controlling $g_r'$ is

$$
r(4t^2-3t+2)+t^2(2t-1)>0
$$

for $t\ge r\ge1/2$. Thus $f$ and $g_r$ increase, while $d_r$ decreases.

### 3.1. The range $0<w\le2/5$

Monotonicity gives

$$
\Phi_w(\alpha)+\Phi_r(\beta)
<wK+\frac1{2-w}.
$$

Since

$$
K=\sqrt{1-wr}\le1-\frac{wr}{2},
$$

it is enough to check

$$
w\left(1-\frac{wr}{2}\right)+\frac1{2-w}<1.
$$

After multiplication by $2(2-w)$, the positive gap is

$$
P(w)=w^4-3w^3+4w^2-6w+2.
$$

On $[0,2/5]$,

$$
P'(w)=4w^3-9w^2+8w-6<0,
$$

because

$$
P'(w)
\le
4(2/5)^3+8(2/5)-6<0.
$$

Moreover,

$$
P(2/5)=\frac{46}{625}>0.
$$

Hence the target holds in this range.

### 3.2. The range $2/5\le w\le1/2$

The first strict endpoint inequality and $\alpha\le1$ give

$$
\beta>1+z-w=r+z.
$$

Since $z\ge w/2$,

$$
r+z\ge1-\frac w2\ge\frac34.
$$

At $t=3/4$,

$$
d_r(3/4)
=
\frac{\sqrt{13}}{7-4w}
\le
\frac{\sqrt{13}}5
<\frac34.
$$

Because $d_r$ decreases, the strict endpoint inequality forces

$$
t<\frac34.
$$

Therefore

$$
\Phi_w(\alpha)+\Phi_r(\beta)
<
\frac{\sqrt3}{4}
+
\frac{3\sqrt{13}}{20}
<1.
$$

The last inequality follows from

$$
5\sqrt3<9,
\qquad
3\sqrt{13}<11.
$$

This proves $(L,T_+^{hi})$.

## 4. The pair $(T_+^{hi},T_-)$

Use the parameters $x$ and $y$ from Section 2. Since both

$$
\alpha=\frac{h(x)}{w+x}
$$

and

$$
\beta=\frac{K}{r+y}
$$

decrease in their parameters,

$$
\alpha\le K,
\qquad
\beta\le K.
$$

The first endpoint inequality gives

$$
\alpha>
\frac{1+z-K}{w}
=
\frac{1+r}{1+K}
=:a_0.
$$

Thus $K>a_0$, equivalently

$$
K>1-w^2.
$$

This forces $w>1/3$. Indeed, for $w\le1/3$,

$$
(1-w^2)^2-K^2=w(w^3-3w+1)\ge0.
$$

At $x=2/3$,

$$
\alpha(2/3)=\frac{\sqrt7}{2+3w}<a_0.
$$

To see this, $w\ge1/3$ gives $K\le\sqrt7/3$, and hence

$$
\sqrt7(1+K)
\le
\sqrt7+\frac73
<5
\le
(2-w)(2+3w).
$$

Because $\alpha(x)$ decreases, $\alpha>a_0$ forces

$$
x<\frac23.
$$

Put

$$
G(x)=
\Phi_w(\alpha)+\alpha
=
\frac{(1+x)h(x)}{w+x}.
$$

The derivative has the sign of

$$
N(x,w)=
2x^3+(4w-1)x^2+(1-w)x+w-2.
$$

This polynomial increases in both $x$ and $w$ on the current rectangle, while

$$
N(2/3,1/2)=-\frac7{54}<0.
$$

Therefore $G$ decreases on $[r,2/3]$, so

$$
G(x)\le G(r)=(1+r)K.
$$

The second strict endpoint inequality and

$$
\Phi_r(\beta)=K-r\beta
$$

now give

$$
\begin{aligned}
\Phi_w(\alpha)+\Phi_r(\beta)
&<\Phi_w(\alpha)+\alpha+K-1-\zeta\\
&\le(2+r)K-1-\zeta.
\end{aligned}
$$

It remains to prove

$$
(2+r)K<2+\zeta.
$$

After multiplication by $1+K$, the positive difference is

$$
r(3w-w^2-K).
$$

For $w>1/3$,

$$
(3w-w^2)^2-K^2
=
w^4-6w^3+8w^2+w-1.
$$

This polynomial has value $1/81$ at $w=1/3$ and derivative

$$
4w^3-18w^2+16w+1>0
$$

on $[1/3,1/2]$; for example, it is at least

$$
4w^3+7w+1>0.
$$

Thus the required difference is positive and

$$
\Phi_w(\alpha)+\Phi_r(\beta)<1.
$$

## 5. The pair $(T_+^{hi},T_+^{hi})$

Write

$$
\alpha=\frac{h(x)}{w+x},
\qquad
\Phi_w(\alpha)=x\alpha,
$$

and

$$
\beta=\frac{h(y)}{r+y},
\qquad
\Phi_r(\beta)=y\beta,
$$

where $r\le x,y<1$. Then

$$
\alpha\le K,
\qquad
\beta\le\frac{K}{2r}.
$$

### 5.1. The forced range $w>2/5$

If $w\le2/5$, then

$$
K\left(w+\frac1{2r}\right)\le1+z,
$$

contradicting the first strict endpoint inequality. For completeness,
multiplying the displayed gap by $2r(1+K)$ gives

$$
E(w)=
K(2w^2-4w+1)
+2w^4-4w^3+w^2-w+1.
$$

If $2w^2-4w+1\ge0$, then

$$
2w^4-4w^3+w^2-w+1
=
1-w+w^2(2w^2-4w+1)>0.
$$

If $2w^2-4w+1<0$, use $K\le1$ to get

$$
E(w)
\ge
2w^4-4w^3+3w^2-5w+2.
$$

The derivative of the last polynomial is

$$
8w^3-12w^2+6w-5<0
$$

on $[0,2/5]$, and its value at $2/5$ is $172/625$. Thus it is positive
throughout that interval.
Therefore a realized high--high pair has

$$
w>\frac25.
$$

### 5.2. Endpoint envelopes

For

$$
F_a(t)=\frac{(1+t)h(t)}{a+t},
\qquad
t\ge\frac12,
$$

the derivative has the sign of

$$
N_a(t)=
2t^3+(4a-1)t^2+(1-a)t+a-2.
$$

On the present range $a\ge2/5$ and $t\ge1/2$, so

$$
N_a'(t)
=
6t^2+2(4a-1)t+1-a
>0.
$$

Thus $F_a$ has at most one interior minimum, and its maximum on a closed
interval occurs at an endpoint. Consequently

$$
\Phi_w(\alpha)+\alpha
=F_w(x)
\le\frac2{1+w},
$$

and

$$
\Phi_r(\beta)+\beta
=F_r(y)
\le\frac2{1+r}.
$$

The nontrivial endpoint comparisons are certified by

$$
4-(1+r)^2(1+w)^2K^2
=
-w^2(w-1)^2(w^2-w-3)>0,
$$

and

$$
16r^2-(1+r)^4h(r)^2
=
(1-r)
\left(
r^5+4r^4+7r^3+9r^2-4r-1
\right)>0.
$$

The bracket in the last line is increasing on $[1/2,1]$ and equals $13/32$
at $r=1/2$. Indeed, its derivative is increasing termwise and is already
positive at $r=1/2$.

### 5.3. Coupled endpoint loss

Multiply the first and second strict endpoint inequalities by $w/K^2$ and
$r/K^2$, respectively. Since

$$
w^2+r=r^2+w=K^2,
$$

this gives

$$
\alpha+\beta>
\frac{2K+1}{K(1+K)}.
$$

Therefore

$$
\Phi_w(\alpha)+\Phi_r(\beta)
<
\frac2{1+w}
+
\frac2{1+r}
-
\frac{2K+1}{K(1+K)}.
$$

The gap between one and the right side is

$$
\frac{3Kwr-Q(w)}
{K(1+K)(1+w)(2-w)},
$$

where

$$
Q(w)=w^4-2w^3+7w^2-6w+2.
$$

Since

$$
Q'(w)=2(2w-1)(w^2-w+3)\le0,
$$

we have

$$
Q(w)\ge Q(1/2)=\frac9{16}>0.
$$

Also

$$
(3Kwr)^2-Q(w)^2=D(w),
$$

where

$$
D(w)=
-w^8+4w^7-9w^6+13w^5-41w^4+65w^3-55w^2+24w-4.
$$

Direct differentiation gives

$$
D'(w)=(1-2w)H(w),
$$

where

$$
H(w)=
4w^6-12w^5+21w^4-22w^3+71w^2-62w+24.
$$

On $[2/5,1/2]$,

$$
71w^2-62w+24\ge\frac{743}{71},
$$

while

$$
w^3(4w^3-12w^2+21w-22)\ge-\frac{11}{4}.
$$

For the latter bound,

$$
4w^3-12w^2+21w=w(4w^2-12w+21)\ge0
$$

and $w^3\le1/8$. Hence $H(w)>0$, so $D$ is increasing. Since

$$
D(2/5)=\frac{4904}{390625}>0,
$$

we have

$$
3Kwr>Q(w)>0.
$$

The displayed gap is positive, proving the high--high pair.

## 6. The pair $(T_+^{hi},L)$

This is the limiting pair as $w\to0^+$ and requires a sharper coupled
endpoint argument.

Parameterize the small high branch and the large $L$ branch by

$$
\alpha=\frac{h(t)}{w+t},
\qquad
p=w\alpha,
\qquad
b=t\alpha,
\qquad
\frac12\le t<1,
$$

and

$$
\beta=h(k),
\qquad
B_L=kh(k),
\qquad
0\le k\le w.
$$

Put

$$
H=h(k).
$$

The first strict endpoint inequality is

$$
H+p>1+z.
$$

Since $p+b=h(t)$,

$$
1-(b+kH)
>
2+z-h(t)-(1+k)H
=:G.
$$

We prove $G\ge0$.

Set

$$
P=1+z-p,
\qquad
p_0=1+z-K=\frac{w(2-w)}{1+K}.
$$

The function

$$
p(t)=\frac{wh(t)}{w+t}
$$

is strictly decreasing on $[0,1]$. Indeed, the sign of its derivative is the
sign of

$$
t(2w+1)-(w+2)\le w-1<0.
$$

The functions $h(t)$ on $[1/2,1]$ and

$$
g(k)=(1+k)h(k)
$$

on $[0,1/2]$ are increasing, with

$$
g'(k)=\frac{1-k+4k^2}{2h(k)}>0.
$$

### 6.1. Endpoint lemma at $P=K$

Let $t_0$ be the unique point in $(1/2,1)$ such that

$$
p(t_0)=p_0,
$$

and put

$$
b_0=\frac{t_0p_0}{w}.
$$

We claim

$$
\boxed{
b_0<1-wK.
}
$$

The point $t_0$ exists because $p(1)<p_0<p(1/2)$. The first comparison is
equivalent to

$$
1+w-w^2>K,
$$

whose squared difference is

$$
w(1-w)(3+w-w^2)>0.
$$

For the second comparison, squaring positive sides gives

$$
3(1+K)^2-(1+2w)^2(2-w)^2
=
6K-4w^4+12w^3+2w^2-15w+2.
$$

Using $K\ge1-w/2$, the last expression is at least

$$
L(w)=8-18w+2w^2+12w^3-4w^4.
$$

Here

$$
L''(w)=4+72w-48w^2>0,
\qquad
L'(1/2)=-9,
$$

so $L'<-7$ on $[0,1/2]$. Moreover,

$$
L(1/2)=\frac34>0.
$$

Now put

$$
b_*=1-wK,
\qquad
T_*=\frac{wb_*}{p_0}.
$$

Then $0<T_*<1$. For the upper bound, one uses

$$
(2-w)-(1-wK)(1+K)
=
1-(1-w)(K+w^2)>0.
$$

A direct reduction using $K^2=1-w+w^2$ gives

$$
p_0^2(w+T_*)^2-w^2h(T_*)^2
=
-\frac{w^3(KE(w)+J(w))}
{(1+K)^2(2-w)^2},
$$

where

$$
E(w)=2w^5+3w^3-20w^2+23w-6,
$$

and

$$
J(w)=w^6+8w^5-22w^4+12w^3+6w^2+2w-6.
$$

The polynomial $J$ is negative on $[0,1/2]$: remove the negative term
$-22w^4$ and evaluate every remaining positive monomial at $1/2$ to obtain

$$
J(w)\le-\frac{111}{64}<0.
$$

If $E\le0$, then $KE+J<0$. If $E>0$, use $K<1$ and

$$
KE+J<E+J.
$$

The polynomial

$$
E+J
=
w^6+10w^5-22w^4+15w^3-14w^2+25w-12
$$

is increasing: after using $-88w^3\ge-44w^2$, its derivative is at least

$$
25-28w>0.
$$

Moreover,

$$
(E+J)(1/2)=-\frac{139}{64}<0.
$$

Thus $KE+J<0$, and the displayed square difference is positive. Hence

$$
p(T_*)<p_0=p(t_0).
$$

The strict decrease of $p$ on $[0,1]$ gives $t_0<T_*$. Therefore

$$
b_0
=
\frac{t_0p_0}{w}
<
\frac{T_*p_0}{w}
=b_*,
$$

proving the endpoint lemma.

### 6.2. The range $P<K$

Here $p>p_0$, so $t<t_0$. Also $k\le w$. Hence

$$
\begin{aligned}
G
&>2+z-h(t_0)-(1+w)K\\
&=1-b_0-wK\\
&>0.
\end{aligned}
$$

### 6.3. The range $P\ge K$

The endpoint inequality gives $P<H$. Since $t<1$ and $p$ decreases,

$$
p(t)>p(1)=\frac{w}{1+w},
$$

so $P<P_1$. Also $K\ge w$ gives $z\le w/(1+w)$, hence $P_1\le1$.
Therefore

$$
K\le P\le
P_1:=1+z-\frac{w}{1+w}
\le1,
$$

there is an $a\in[0,w]$ with

$$
h(a)=P.
$$

Because $h$ decreases on $[0,1/2]$, $P<H=h(k)$ gives $k<a$. Therefore

$$
(1+k)H
<(1+a)P
=P+\ell(P),
$$

where

$$
\ell(P)=
\frac P2
\left(
1-\sqrt{4P^2-3}
\right).
$$

Consequently

$$
G>1-b(P)-\ell(P)=:D(P).
$$

We prove that $D$ is positive on $[K,P_1]$. First, it is concave. Indeed,

$$
\ell''(P)
=
\frac{2P(9-8P^2)}{(4P^2-3)^{3/2}}>0.
$$

The high-branch output $b$ is convex as a function of $p$, hence also as a
function of $P=1+z-p$. With

$$
A=2+w-(1+2w)t>0
$$

and

$$
Q=8wt^2+4t^2-8wt-13t-w+4,
$$

direct implicit differentiation gives

$$
\frac{d^2b}{dp^2}
=
-\frac{2h(t)(t+w)^3Q}{w^2A^3}.
$$

Here

$$
Q_t\le8w-5\le-1,
\qquad
Q(1/2)=-3w-\frac32,
$$

so $Q<0$ and $b''>0$. Thus $D''<0$. The endpoint $K=\sqrt3/2$ follows by
continuous extension.

At $P=K$,

$$
\ell(K)=wK,
$$

and the endpoint lemma gives

$$
D(K)=1-b_0-wK>0.
$$

At $P=P_1$, put

$$
\kappa=\frac{w}{1+(1+w)z}.
$$

Then

$$
\kappa P_1=\frac{w}{1+w}.
$$

The exact Full--$L$ factor proved in `401c` gives

$$
P_1>h(\kappa).
$$

Since $h$ decreases,

$$
\ell(P_1)
<
\kappa P_1
=
\frac{w}{1+w}.
$$

At this endpoint $t=1$, so

$$
b(P_1)=\frac1{1+w}.
$$

Therefore $D(P_1)>0$. Concavity places $D$ above the chord joining its two
positive endpoint values, so $D(P)>0$ throughout $[K,P_1]$. This proves

$$
G>0
$$

and hence the pair $(T_+^{hi},L)$.

## 7. Assembly

The pairs proved in Sections 3--6 are exactly the four pairs left open in
`401c`. Therefore every genuine selected label pair satisfies

$$
\Phi_w(\alpha)+\Phi_r(\beta)<1.
$$

Returning to the original CE2 endpoint variables,

$$
\boxed{
\widehat B_{p/(1-R)}(p)
+
\widehat B_{q/R}(q)
<1.
}
$$

As proved in `401c`, this leaves boundary length

$$
4-
\widehat B_{p/(1-R)}(p)
-
\widehat B_{q/R}(q)
>3
$$

for the three rows $T_2,T_3,T_4$, contradicting their three nonsupercritical
row caps. Thus an all-Vd0 CE2 two-gap cover with $N_+=0$ is impossible.

$$
\Box
$$
