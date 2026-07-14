# Diagonal Length Bounds

Status: Proven

Let

$$
D=\bigcup_{i=0}^5r_i
=[V_0,V_3]\cup[V_1,V_4]\cup[V_2,V_5].
$$

The six unit radial arms meet pairwise only at $O$, a set of zero
$\mathcal H^1$-measure. Therefore

$$
\mathcal H^1(D)=6.
$$

For a closed triangle $T$, define

$$
L_D(T)=\mathcal H^1(T\cap D).
$$

All triangles below are closures of original open-cover roles. In particular,

$$
O\in\mathrm{int}(T_C),
\qquad
V_i\in\mathrm{int}(T_i).
$$

The interior condition on $T_C$ is essential. For example,
$\mathrm{conv}\left\{O,V_0,V_1\right\}$ has boundary-edge overlap and
diagonal trace of length $2$, but $O$ lies on its boundary rather than in its
interior.

## Theorem

The role closures satisfy the following full diagonal-trace caps.

| Role or local type | Hypothesis | Full diagonal contribution |
|---|---|---:|
| CE1/CE2 center role | $O\in\mathrm{int}(T_C)$ | strictly less than $\frac32$ |
| Vd0 vertex role | $a_i+b_i\le1$ | at most $1$ |
| Vd0 vertex role | $a_i+b_i>1$ | strictly less than $\frac12$ |
| T3-like vertex role | none beyond the type hypothesis | strictly less than $\frac12$ |

As in the boundary-length package, every assigned or reduced contribution is
a subset of the full trace and inherits these bounds.

## Vertex-role locality

Let $P=sV_j\in r_j\setminus\left\{O\right\}$, where $0<s\le1$. Then

$$
\lVert V_i-P\rVert^2
=1+s^2-2s\cos\frac{(j-i)\pi}{3}.
$$

If

$$
j\notin\left\{i-1,i,i+1\right\},
$$

then the cosine is at most $-1/2$, and therefore

$$
\lVert V_i-P\rVert^2\ge1+s+s^2>1.
$$

A unit equilateral triangle has diameter $1$. Hence a $V_i$-triangle can have
positive-length diagonal trace only on

$$
r_{i-1},
\qquad
r_i,
\qquad
r_{i+1}.
$$

Any point contacts with the other arms have zero measure.

## Vd0 caps

A Vd0 role has no positive-length trace on either adjacent arm. Vertex-role
locality therefore leaves only its own unit arm, and

$$
L_D(T_i)\le1.
$$

Suppose now that

$$
a_i+b_i>1.
$$

The midpoint self-cover lemma in
[../20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md](../20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md)
gives

$$
M_i\notin T_i.
$$

The set $T_i\cap r_i$ is a closed interval containing $V_i$. If its length
were at least $1/2$, it would contain $M_i$. Thus

$$
L_D(T_i)<\frac12
$$

for every supercritical Vd0 role.

## CE1/CE2 center cap

Normalize a positive-length center overlap to $e_{0,1}$ and use the affine
coordinates

$$
X=V_0+b(V_1-V_0)+a(V_5-V_0).
$$

The CE edge normal form proved in
[../21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md](../21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md)
gives a parameter $0<\lambda<1$ and

$$
\rho=\sqrt{1-\lambda+\lambda^2},
$$

with side slacks

$$
F_1=\lambda b+(1-\lambda)a-\lambda s,
$$

$$
F_2=-b+\lambda a+t,
$$

$$
F_0=(1-\lambda)b-a+\rho+\lambda s-t.
$$

Put

$$
C_j=F_j(O).
$$

Because $O\in\mathrm{int}(T_C)$,

$$
C_0,C_1,C_2>0,
\qquad
C_0+C_1+C_2=\rho.
$$

The positive-length condition $s<t$ gives the exact identity

$$
C_0+(1-\lambda)C_2
=\rho(1-\rho)-\lambda(t-s)
<\rho(1-\rho).
$$

Let $\gamma_i$ be the length of $T_C\cap r_i$. Since $O\in T_C$, each such
intersection is an initial interval from $O$. Direct substitution of the six
unit-speed radial parameterizations into $F_0,F_1,F_2$ gives

$$
\begin{array}{c|cccccc}
i&0&1&2&3&4&5\\
\hline
\gamma_i\text{ is at most}
&C_1&C_2/\lambda&C_2&C_0/\lambda&C_0&C_0/(1-\lambda).
\end{array}
$$

The arms overlap only at $O$, so

$$
\begin{aligned}
L_D(T_C)
&=\sum_{i=0}^5\gamma_i\\
&\le
\rho+\frac{C_2}{\lambda}
+\frac{C_0}{\lambda}
+\frac{C_0}{1-\lambda}\\
&=
\rho+
\frac{C_0+(1-\lambda)C_2}{\lambda(1-\lambda)}\\
&<
\rho+
\frac{\rho(1-\rho)}{\lambda(1-\lambda)}.
\end{aligned}
$$

Since

$$
\lambda(1-\lambda)=1-\rho^2,
$$

we obtain

$$
L_D(T_C)<\rho+\frac{\rho}{1+\rho}.
$$

Here $0<\rho<1$, and

$$
\frac32-\rho-\frac{\rho}{1+\rho}
=\frac{(1-\rho)(2\rho+3)}{2(1+\rho)}>0.
$$

Therefore

$$
L_D(T_C)<\frac32.
$$

This proof uses the inherited interior-center condition and applies equally
to CE1 and CE2.

## T3-like cap

Rotate to $i=0$, and reflect if necessary so that the unique adjacent support
is on

$$
r_1=\left\{(1,y):0\le y\le1\right\}
$$

in the local coordinates

$$
X=V_0+x(V_1-V_0)+y(V_5-V_0).
$$

The T3-like translation normalization proved in
[../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md](../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
provides a same-orientation T3-like translate $\widehat T$ such that

$$
T_0\cap H\subseteq\widehat T\cap H
$$

and $V_0$ lies in the relative interior of one side of $\widehat T$. Since
$D\subset H$,

$$
L_D(T_0)\le L_D(\widehat T).
$$

The exhaustive Type-II form in that normalization is

$$
\widehat T=
\left\{(x,y):
\begin{array}{l}
(1-t)x+ty\ge0,\\
\beta+tx-y\ge0,\\
\beta+x-(1-t)y\le z
\end{array}
\right\},
$$

where

$$
0<t<1,
\qquad
\Delta=1-t+t^2,
\qquad
z=\sqrt\Delta,
\qquad
0<\beta<z.
$$

Its non-axis vertex in the local wedge is

$$
Q=
\left(
\frac{z-t\beta}{\Delta},
\frac{tz+(1-t)\beta}{\Delta}
\right).
$$

The two axis reaches are $z-\beta<1$ and $\beta<1$. Hence positive-length
support on $r_1$ is equivalent to $Q_x>1$, which is

$$
\beta<\frac{z-\Delta}{t}.
$$

Using

$$
t(1-t)=1-\Delta=1-z^2,
$$

this upper bound becomes

$$
\frac{z-\Delta}{t}
=\frac{(1-t)z}{1+z}
<(1-t)z.
$$

On the own arm

$$
r_0=\left\{(w,w):0\le w\le1\right\},
$$

the two possible exit parameters are

$$
\frac{\beta}{1-t}
\qquad\text{and}\qquad
\frac{z-\beta}{t}.
$$

The preceding bound shows that the first occurs first. Thus the own-arm
contribution is

$$
c=\frac{\beta}{1-t}.
$$

On $r_1$, direct substitution gives the interval

$$
\frac{\beta+1-z}{1-t}
\le y\le
\beta+t.
$$

The support bound places both endpoints strictly between $0$ and $1$, and the
interval length is

$$
d=\frac{z-\Delta-t\beta}{1-t}.
$$

No other arm contributes positive length because $\widehat T$ remains
T3-like. Therefore

$$
\begin{aligned}
L_D(\widehat T)
&=c+d\\
&=\beta+\frac{z-\Delta}{1-t}\\
&<\frac{z-\Delta}{t}+\frac{z-\Delta}{1-t}\\
&=\frac{z-\Delta}{t(1-t)}\\
&=\frac{z}{1+z}\\
&<\frac12.
\end{aligned}
$$

The final inequality is strict because $0<t<1$ gives $z<1$. Trace domination
then proves

$$
L_D(T_0)<\frac12.
$$

By symmetry, this holds for every original T3-like role.

## CE1/CE2, $N_+=1$, at least two T3-like rows

Assume there are no Vd1/Vd2 rows and let $k\ge2$ be the number of T3-like
rows. T3-like rows are nonsupercritical by
[../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md](../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md).
Thus the unique supercritical row is Vd0, $2\le k\le5$, and the remaining
$5-k$ rows are nonsupercritical Vd0. The caps above give

$$
\begin{aligned}
L_D(T_C)+\sum_{i=0}^5L_D(T_i)
&<\frac32+\frac12+\frac{k}{2}+(5-k)\\
&=7-\frac{k}{2}\\
&\le6.
\end{aligned}
$$

If the seven open roles covered $D$, passing to closures and using
subadditivity would give

$$
6=\mathcal H^1(D)
\le
L_D(T_C)+\sum_{i=0}^5L_D(T_i),
$$

a contradiction. Hence the CE1/CE2, $N_+=1$, no-Vd1/Vd2,
at-least-two-T3-like branch is impossible.
