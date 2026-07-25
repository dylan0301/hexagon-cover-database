# Signed CE1/CE2 Center Normal Form

Status: Proven

This note gives one exact normal form for both normalized CE1 and CE2 center
triangles. The two classes differ only by the sign of one companion-trace
surplus. It is a reparameterization of the edge-cut model in
[`2100`](2100_CE1_CE2_exactly_one_midpoint_lemma.md), and it subsumes the
separate radial-exit formulas in [`2105`](2105_CE1_exact_formulas.md) and
[`2106`](2106_CE2_exact_formulas.md).

## 1. Common signed variables

Use the affine coordinates

$$
X=V_0+b(V_1-V_0)+a(V_5-V_0).
$$

Normalize a positive-length center trace to $e_{0,1}$. After the reflection
used in `2100`, let

$$
0<R<1,
\qquad
W=1-R,
$$

and put

$$
E=\sqrt{1-R+R^2}=\sqrt{1-RW},
$$

$$
\eta=1-E,
\qquad
P=E(1-E).
$$

The identities

$$
RW=1-E^2=\eta(1+E)=\eta+P
$$

will be used throughout.

Let $F_0,F_1,F_2$ be the three side slacks in the edge-cut normal form and set

$$
\alpha=F_0(O),
\qquad
\delta=F_2(O),
$$

$$
k=\eta+\alpha+\delta.
$$

Then the center triangle is exactly

$$
\boxed{
T_C=\left\{F_0\ge0,F_1\ge0,F_2\ge0\right\},
}
$$

where

$$
\boxed{
\begin{aligned}
F_0&=R+\alpha-a+Wb,\\
F_1&=Rb+Wa-k,\\
F_2&=W+\delta-b+Ra.
\end{aligned}
}
$$

Indeed, the model in `2100` is

$$
F_1=Rb+Wa-Rs,
$$

$$
F_2=-b+Ra+t,
$$

$$
F_0=Wb-a+E+Rs-t.
$$

The definitions of the two center slacks give

$$
t=W+\delta,
\qquad
Rs=\eta+\alpha+\delta=k,
$$

and substitution gives the displayed common form. Also

$$
F_0+F_1+F_2=E.
$$

Thus the three side normals and the unit-side condition are exactly those of
the proved edge-cut normal form.

## 2. The active and companion traces

On $e_{0,1}$ one has $a=0$. The two active inequalities are

$$
Rb\ge k,
\qquad
b\le W+\delta.
$$

Therefore

$$
\boxed{
I_R:=T_C\cap e_{0,1}
=
\left[\frac{k}{R},W+\delta\right].
}
$$

Define the active-trace surplus

$$
\boxed{
\Delta_R=P-\alpha-W\delta.
}
$$

A direct calculation gives

$$
\left\lvert I_R\right\rvert
=
W+\delta-\frac{k}{R}
=
\frac{\Delta_R}{R}.
$$

Hence the normalized trace is positive exactly when

$$
\boxed{\Delta_R>0.}
$$

On $e_{5,0}$ one has $b=0$. The candidate companion trace is

$$
\left[\frac{k}{W},R+\alpha\right].
$$

Define the signed companion surplus

$$
\boxed{
\Delta_L=P-R\alpha-\delta.
}
$$

Its signed length is

$$
R+\alpha-\frac{k}{W}
=
\frac{\Delta_L}{W}.
$$

Consequently

$$
\boxed{
\left\lvert T_C\cap e_{5,0}\right\rvert
=
\frac{[\Delta_L]_+}{W},
}
$$

where $[x]_+=\max\{x,0\}$.

The sign of $\Delta_L$ is exactly the CE1/CE2 distinction:

$$
\boxed{
\begin{array}{c|c}
\text{center class}&\text{signed condition}\\
\hline
\mathrm{CE1}&\Delta_L\le0,\\
\mathrm{CE2}&\Delta_L>0.
\end{array}
}
$$

Equality $\Delta_L=0$ gives only a point contact on $e_{5,0}$ and is therefore
CE1 under the positive-length definition.

To see that no other positive boundary trace is omitted, first note that
$\Delta_R>0$ implies

$$
\delta<\frac{P}{W}=\frac{ER}{1+E}<\frac R2.
$$

On $e_{1,2}$, parameterized by $b=1+q$, $a=q$, one has

$$
F_2=\delta-R-Wq<0.
$$

Thus the second adjacent trace cannot occur on $e_{1,2}$. The CE
classification in [`1101`](../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md)
shows that a center triangle has at most two positive boundary traces and that
two such traces are adjacent. Therefore $e_{5,0}$ is the only possible
companion edge.

## 3. Exact domain and midpoint set

The normalized exact domain is

$$
\boxed{
0<R<1,
\qquad
\alpha>0,
\qquad
\delta>0,
\qquad
\Delta_R>0,
}
$$

together with $\Delta_L\le0$ for CE1 and $\Delta_L>0$ for CE2.

The third center slack is

$$
F_1(O)=E-\alpha-\delta.
$$

It is positive, and in fact greater than $1/2$. Indeed,

$$
W(\alpha+\delta)\le \alpha+W\delta<P,
$$

so

$$
E-\alpha-\delta
>
E-\frac{P}{W}
=
\frac{E(E-R)}{W}.
$$

Since $E^2-R^2=W$,

$$
2E(E-R)-W
=
\frac{W(E-R)}{E+R}>0.
$$

Hence

$$
F_1(O)>\frac12.
$$

Also

$$
\delta<\frac{P}{W}=\frac{ER}{1+E}<\frac R2,
$$

and

$$
\alpha<P
=
\frac{ERW}{1+E}
<\min\left\{\frac R2,\frac W2\right\}.
$$

The midpoint tests in `2100` now give

$$
\boxed{
T_C\cap\left\{M_0,\ldots,M_5\right\}=\left\{M_0\right\}.
}
$$

Conversely, the displayed side functions define the proved unit-equilateral
edge-cut model, the three center slacks are positive, the normalized trace has
length $\Delta_R/R>0$, and the preceding midpoint inequalities hold. The sign
of $\Delta_L$ then gives precisely CE1 or CE2. Thus the signed domain is both
necessary and sufficient.

## 4. One common list of radial exits

Let $d_i^C$ be the length of $T_C\cap[O,V_i]$, measured from $O$ toward $V_i$.
Substitution of the six radial parametrizations into the common side slacks
gives

$$
\boxed{
\begin{aligned}
d_0^C&=E-\alpha-\delta=1-k,\\
d_1^C&=\frac{\delta}{R},\\
d_2^C&=\delta,\\
d_3^C&=\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\},\\
d_4^C&=\alpha,\\
d_5^C&=\frac{\alpha}{W}.
\end{aligned}
}
$$

For example, on $r_1$ the decreasing slack $F_2$ is
$\delta-Rq$, while on $r_3$ the two decreasing slacks are
$\alpha-Rq$ and $\delta-Wq$. The remaining four formulas are immediate in
the same way.

The complementary vertex-side radial demands are

$$
\boxed{c_i=1-d_i^C.}
$$

The exact midpoint set gives

$$
d_0^C>\frac12,
\qquad
d_i^C<\frac12\quad(i\ne0),
$$

and hence

$$
c_0<\frac12,
\qquad
c_i>\frac12\quad(i\ne0)
$$

for closures of original open center roles.

In the CE1 sign range, $\Delta_L\le0<\Delta_R$ implies

$$
R\alpha+\delta\ge P>\alpha+W\delta,
$$

and therefore

$$
R\delta>W\alpha.
$$

Thus the minimum on $r_3$ specializes automatically to

$$
d_3^C=\frac{\alpha}{R}
$$

in CE1. No separate CE1 exit formula is needed.

## 5. Legacy-variable dictionary

The variables in `2105` are recovered by

$$
\lambda=R,
\qquad
s=\frac{k}{R},
\qquad
t=W+\delta,
$$

$$
C_0=\alpha,
\qquad
C_2=\delta.
$$

The variables in `2106` are recovered by

$$
\boxed{
x=\frac{k}{W},
\qquad
u=R+\alpha,
\qquad
y=\frac{k}{R},
\qquad
v=W+\delta,
}
$$

where $\nu$ is the far endpoint called $u$ in `2106`. Thus

$$
T_C\cap e_{5,0}=[x,\nu],
\qquad
T_C\cap e_{0,1}=[y,v].
$$

If

$$
S=x+y,
\qquad
D=\sqrt{x^2+xy+y^2},
$$

then

$$
S=\frac{k}{RW},
\qquad
D=\frac{Ek}{RW}.
$$

The CE2 coupling equation follows without a separate derivation:

$$
\begin{aligned}
(\nu+v)S-xy
&=
(1+\alpha+\delta)\frac{k}{RW}-\frac{k^2}{RW}\\
&=
\frac{Ek}{RW}\\
&=D.
\end{aligned}
$$

## 6. Common boundary contribution and reflection

The full center-boundary contribution is

$$
\boxed{
L_{\partial H}(T_C)
=
\frac{\Delta_R}{R}
+
\frac{[\Delta_L]_+}{W}.
}
$$

Reflection across the axis through $V_0$ exchanges

$$
R\longleftrightarrow W,
\qquad
\alpha\longleftrightarrow\delta,
$$

and reverses the row order $1,2,3,4,5$. Thus every left-oriented statement
is obtained from its right-oriented form by this explicit substitution; no
unlabeled symmetry convention is required.
