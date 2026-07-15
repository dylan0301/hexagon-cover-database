# The $(L,\mathrm{Full})$ Branch in the $407X$ Boundary-Loss Reduction

Status: Proven

This file proves the hard-region branch

$$
(B_5,B_1)=(L,\mathrm{Full})
$$

for the boundary-loss framework in
[`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md).

Throughout, use the notation of `4073`.

## 1. Statement

Assume the support-isolated $407X$ branch of `4073`, and assume the hard region

$$
A_1+A_5\le1.
$$

Assume the realized branches are

$$
B(A_5,C_5)=L,\qquad B(A_1,C_1)=\mathrm{Full}.
$$

Then

$$
B(A_5,C_5)+B(A_1,C_1)<1.
$$

Equivalently, since

$$
B(A_5,C_5)=e(\gamma_5),\qquad C_5=1-\gamma_5,
$$

and

$$
B(A_1,C_1)=1-A_1,
$$

it is enough to prove

$$
\boxed{e(\gamma_5)<A_1.}
$$

## 2. Center-geometry estimates

Use the direct $C$-side variables from `4073`:

$$
0<\lambda<1,\qquad \rho=\sqrt{1-\lambda+\lambda^2},
$$

$$
X\ge0,\qquad Y\ge0,\qquad X+(1-\lambda)Y<\rho(1-\rho),
$$

$$
A_C=1-t=\lambda-Y,
$$

$$
\gamma_1=\min\left(\frac{Y}{\lambda},\frac{\rho-X-Y}{1-\lambda}\right),
$$

and

$$
\gamma_5=\min\left(\frac{X}{1-\lambda},\frac{\rho-X-Y}{\lambda}\right).
$$

When $T_C$ is CE2 and $T_C\cap e_{5,0}=[S,T]$,

$$
S=\frac{X+Y+1-\rho}{1-\lambda}.
$$

### Lemma 2.1: core estimate

If

$$
\gamma_1\ge A_C,
$$

then

$$
e(\gamma_5)<A_C.
$$

### Proof

Since $\gamma_1\le Y/\lambda$ and $Y=\lambda-A_C$, the hypothesis implies

$$
A_C\le \frac{\lambda-A_C}{\lambda},
$$

hence

$$
A_C\le \frac{\lambda}{1+\lambda}.
$$

Put

$$
\delta=\frac{1-\rho}{1-\lambda}=\frac{\lambda}{1+\rho}.
$$

From

$$
X+(1-\lambda)Y<\rho(1-\rho)
$$

and $Y=\lambda-A_C$, one obtains

$$
X<(1-\lambda)(A_C-\delta).
$$

Therefore

$$
\gamma_5\le \frac{X}{1-\lambda}<A_C-\delta.
$$

Let $z=A_C-\delta$.  Then $0\le \gamma_5<z$.  Also

$$
z\le z_{\max}:=\frac{\lambda}{1+\lambda}-\frac{\lambda}{1+\rho}.
$$

A direct calculation gives

$$
z_{\max}< \frac{1}{8}
$$

and

$$
z_{\max}+5z_{\max}^2\le\delta.
$$

For the second inequality, after substituting $\delta=\lambda/(1+\rho)$, it reduces to

$$
2\rho(6\lambda+1)>11\lambda^2-7\lambda+2.
$$

Both sides are positive, and the squared difference is

$$
4(6\lambda+1)^2\rho^2-(11\lambda^2-7\lambda+2)^2
=\lambda(23\lambda^3+58\lambda^2+7\lambda+72)>0.
$$

The elementary Low estimate

$$
e(\eta)\le 2\eta+5\eta^2\qquad(0\le\eta\le1/8)
$$

then gives

$$
e(\gamma_5)<2z+5z^2=z+(z+5z^2)\le z+\delta=A_C.
$$

This proves the lemma.

### Lemma 2.2: $S$-estimate

Assume $T_C$ is CE2 and

$$
S\le \frac{Y}{\lambda}.
$$

Then

$$
e(\gamma_5)<S.
$$

### Proof

The hypothesis is equivalent to

$$
\lambda X+(2\lambda-1)Y+\lambda(1-\rho)\le0.
$$

Hence $0<\lambda<1/2$ and

$$
Y\ge \frac{\lambda(X+1-\rho)}{1-2\lambda}.
$$

Therefore

$$
S=\frac{X+Y+1-\rho}{1-\lambda}\ge \frac{X+1-\rho}{1-2\lambda}=:S_0.
$$

Combining the lower bound for $Y$ with $X+(1-\lambda)Y<\rho(1-\rho)$ gives

$$
X<X_*(\lambda):=\frac{(1-\rho)(\rho(1-2\lambda)-\lambda(1-\lambda))}{1-\lambda-\lambda^2}.
$$

The positivity of $X_*(\lambda)$ forces $0<\lambda<3/8$. Indeed, with
$x=\lambda$ the sign-controlling factor is

$$
\rho(1-2x)-x(1-x).
$$

Its derivative is

$$
-\frac{(1-2x)^2}{2\rho}-2\rho-1+2x<0,
$$

and its value at $x=3/8$ is $-1/64$. On this interval,

$$
\frac{X_*(\lambda)}{1-\lambda}< \frac{1}{8}.
$$

Thus

$$
\eta_0:=\frac{X}{1-\lambda}< \frac{1}{8},\qquad \gamma_5\le\eta_0.
$$

It remains to prove

$$
2\eta_0+5\eta_0^2<S.
$$

Since $S\ge S_0$, it is enough to show

$$
G_\lambda(X):=\frac{X+1-\rho}{1-2\lambda}-2\frac{X}{1-\lambda}-5\frac{X^2}{(1-\lambda)^2}>0.
$$

For fixed $\lambda$, this is concave in $X$, so it suffices to check $X=0$
and $X=X_*(\lambda)$. We give the two endpoint checks explicitly. Put

$$
x=\lambda,
\qquad
d_0=1-x-x^2,
$$

and

$$
N=(1-\rho)\left(\rho(1-2x)-x(1-x)\right),
\qquad
X_*=\frac{N}{d_0}.
$$

At the first endpoint,

$$
G_x(0)=\frac{1-\rho}{1-2x}>0.
$$

The earlier bound $X_*/(1-x)<1/8$ is equivalent to $W>0$, where

$$
W=d_0(1-x)-8N=p_1+q_1\rho,
$$

$$
p_1=9-18x+16x^2-15x^3,
\qquad
q_1=-8+8x+8x^2.
$$

The Bernstein coefficients of $p_1$ and $q_1$ on $[0,3/8]$ are respectively

$$
9,
\quad
\frac{27}{4},
\quad
\frac{21}{4},
\quad
\frac{1899}{512},
$$

and

$$
-8,
\quad
-\frac{13}{2},
\quad
-\frac{31}{8}.
$$

Thus $p_1>0$ and $q_1<0$. Moreover,

$$
p_1^2-q_1^2\rho^2=(1-x)R_5(x),
$$

where the Bernstein coefficients of $R_5$ on $[0,3/8]$ are

$$
R_5(x)=17-115x+369x^2-541x^3+383x^4-161x^5,
$$

and those coefficients are

$$
17,
\quad
\frac{67}{8},
\quad
\frac{3161}{640},
\quad
\frac{19657}{5120},
\quad
\frac{76543}{20480},
\quad
\frac{118501}{32768}.
$$

Hence $p_1>|q_1|\rho$ and $W>0$.

For the second endpoint, multiplication of $G_x(X_*)$ by the positive factor

$$
(1-2x)(1-x)^2d_0^2
$$

gives $P+Q\rho$, where

$$
P=-8+44x-98x^2+134x^3-147x^4+131x^5-102x^6+56x^7,
$$

and

$$
Q=8-40x+76x^2-82x^3+54x^4+18x^5-44x^6.
$$

Their Bernstein coefficients on $[0,3/8]$ are

$$
\begin{aligned}
P:
&-8,
-\frac{79}{14},
-\frac{883}{224},
-\frac{24151}{8960},
-\frac{255811}{143360},\\
&-\frac{258469}{229376},
-\frac{616339}{917504},
-\frac{98465}{262144},
\end{aligned}
$$

and

$$
Q:
8,
\frac{11}{2},
\frac{297}{80},
\frac{12397}{5120},
\frac{15169}{10240},
\frac{27561}{32768},
\frac{28985}{65536}.
$$

Thus $P<0<Q$. Finally,

$$
P^2-Q^2\rho^2
=x^2(1-2x)^2(1-x)^2R_8(x),
$$

where the Bernstein coefficients of $R_8$ are

$$
\begin{aligned}
R_8(x)={}&-16-16x+452x^2-1480x^3+2560x^4-2972x^5\\
&+2293x^6-1076x^7+300x^8,
\end{aligned}
$$

and those coefficients are

$$
\begin{aligned}
&-16,
-\frac{67}{4},
-\frac{6823}{448},
-\frac{45995}{3584},
-\frac{9167}{896},\\
&-\frac{3561541}{458752},
-\frac{41162803}{7340032},
-\frac{16172827}{4194304},
-\frac{10599805}{4194304}.
\end{aligned}
$$

Therefore $P^2<Q^2\rho^2$, so $Q\rho>-P$ and $G_x(X_*)>0$.

Therefore

$$
2\eta_0+5\eta_0^2<S.
$$

Using $e(\eta)\le2\eta+5\eta^2$ for $0\le\eta\le1/8$, we get

$$
e(\gamma_5)<S.
$$

This proves the lemma.

## 3. T3-like hit-overlap estimate

### Lemma 3.1

Assume $T_0$ hits the $T_C$ exit point on $r_1$, and assume

$$
\alpha\ge S.
$$

Then

$$
S\le\gamma_1\le \frac{Y}{\lambda}.
$$

### Proof

The upper bound is part of the definition of $\gamma_1$.

Let

$$
d=\frac{D-1}{D},\qquad q=\alpha+d.
$$

Since $\alpha\ge S$,

$$
q\ge S+d.
$$

The $T_0$ interval on $r_1$ in center-to-$V_1$ coordinates is

$$
[1-u,1-c],\qquad 1-u=d+\frac{R}{D}-q,\qquad 1-c=1-\frac{Dq}{R}.
$$

The hit condition gives

$$
1-u\le\gamma_1\le1-c.
$$

Combining these inequalities gives

$$
\gamma_1\ge \frac{D-1}{D-R}.
$$

Also

$$
S+d\le \frac{R(1-\gamma_1)}{D}.
$$

It follows that

$$
S\le \frac{R(1-\gamma_1)}{D}-d.
$$

The right side is at most $\gamma_1$.  Indeed this is equivalent to

$$
R-D+1\le\gamma_1(D+R),
$$

and, using $\gamma_1\ge(D-1)/(D-R)$, it reduces to

$$
(D-1)(D+R)\ge (R-D+1)(D-R),
$$

whose difference is

$$
(D-1)^2\ge0.
$$

Hence $S\le\gamma_1$.

## 4. Proof of $(L,\mathrm{Full})$

We prove

$$
e(\gamma_5)<A_1.
$$

### Case 1: $p_1<t$

Then

$$
A_1\ge A_C.
$$

If $T_0$ misses the $T_C$ exit on $r_1$, then

$$
C_1=1-\gamma_1.
$$

If $A_1\ge1/2$, the target is immediate.  If $A_1<1/2$, the Full condition gives

$$
1-\gamma_1\le1-A_1,
$$

so

$$
\gamma_1\ge A_1\ge A_C.
$$

Lemma 2.1 gives

$$
e(\gamma_5)<A_C\le A_1.
$$

If $T_0$ hits the exit and $\gamma_1\ge A_C$, Lemma 2.1 gives the same conclusion.

It remains to consider the hit subcase with $\gamma_1<A_C$.  If the $e_{5,0}$ side is overlapped, then $\alpha\ge S$, so Lemma 3.1 gives $S\le\gamma_1< A_C\le A_1$.  Lemma 2.2 gives

$$
e(\gamma_5)<S<A_1.
$$

If the $e_{5,0}$ side is non-overlap, then $A_5=1-\alpha$.  The hard-region condition gives $A_1\le\alpha$.  Since $p_1<t$, the case $p_1<s$ would give $A_1=q=\alpha+(D-1)/D>\alpha$, impossible.  Hence $s\le p_1<t$ and $A_1=A_C\le\alpha$.

If $A_C\ge1/2$, the target is immediate.  If $A_C<1/2$, the Full condition in the hit case gives

$$
\frac{Dq}{R}=C_1\le1-A_C.
$$

Using $q\ge A_C+(D-1)/D$ gives

$$
A_C\le \frac{R-D+1}{D+R}.
$$

The hit condition and $\gamma_1<A_C$ give

$$
\frac{D-1}{D-R}<A_C.
$$

Together these imply

$$
\frac{D-1}{D-R}< \frac{R-D+1}{D+R},
$$

but after clearing denominators the opposite inequality is equivalent to

$$
(D-1)^2\ge0.
$$

Contradiction.  Thus the non-overlap hit-low subcase is impossible.

### Case 2: $p_1\ge t$

If $T_C$ is CE1, then its only positive boundary interval is already covered by $T_0$.  The six vertex roles would have to cover the full perimeter.  But $T_0$ is T3-like with boundary sum $1/D<1$, and all other rows are nonsupercritical, so the total perimeter contribution is strictly less than $6$.  Contradiction.

Thus $T_C$ is CE2.  In the hard region, $A_5$ cannot be $1-\alpha$, since then

$$
A_1+A_5=q+1-\alpha=1+\frac{D-1}{D}>1.
$$

So $A_5=1-T$ and $\alpha\ge S$.  Since $A_1=q=\alpha+(D-1)/D$, we have $A_1>S$.

If $T_0$ misses the $r_1$ exit, then Full gives $\gamma_1\ge A_1>S$, so $S\le Y/\lambda$.  Lemma 2.2 gives $e(\gamma_5)<S<A_1$.

If $T_0$ hits the exit, Lemma 3.1 gives $S\le Y/\lambda$, and Lemma 2.2 again gives $e(\gamma_5)<S<A_1$.

This proves the theorem.
