# Signed CE1/CE2 Center Normal Form

Status: Proven

This note gives one exact normal form for normalized CE1 and CE2 center
triangles. The two classes differ only by the sign of one companion-trace
surplus. It is a reparameterization of the edge-cut model in
[`2100`](2100_CE1_CE2_exactly_one_midpoint_lemma.md) and subsumes the separate
radial-exit lists in [`2105`](2105_CE1_exact_formulas.md) and
[`2106`](2106_CE2_exact_formulas.md).

## 1. Common variables and side slacks

Use the affine coordinates

$$
X=V_0+b(V_1-V_0)+a(V_5-V_0).
$$

Normalize a positive-length center trace to $e_{0,1}$. After the reflection
used in `2100`, put

$$
0<R<1,
\qquad
W=1-R,
$$

$$
E=\sqrt{1-R+R^2}=\sqrt{1-RW},
$$

$$
\eta=1-E,
\qquad
P=E(1-E).
$$

The identity

$$
\boxed{RW=1-E^2=\eta(1+E)=\eta+P}
$$

will be used repeatedly.

Let $F_0,F_1,F_2$ be the three side slacks in the edge-cut normal form and set

$$
\alpha=F_0(O),
\qquad
\delta=F_2(O),
$$

$$
k=\eta+\alpha+\delta.
$$

Then

$$
\boxed{
T_C=\{F_0\ge0,F_1\ge0,F_2\ge0\},
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

### Proof of the common form

The proved edge-cut model is

$$
F_1=Rb+Wa-Rs,
$$

$$
F_2=-b+Ra+t,
$$

$$
F_0=Wb-a+E+Rs-t.
$$

The definitions of the center slacks give

$$
t=W+\delta,
\qquad
Rs=\eta+\alpha+\delta=k.
$$

Substitution gives the displayed common form. Also

$$
F_0+F_1+F_2=E,
$$

so these are exactly the three side slacks of the same unit equilateral
triangle.

## 2. Active and companion traces

On $e_{0,1}$ one has $a=0$. The active inequalities are

$$
Rb\ge k,
\qquad
b\le W+\delta.
$$

Thus

$$
\boxed{
I_R:=T_C\cap e_{0,1}
=
\left[\frac{k}{R},W+\delta\right].
}
$$

Define

$$
\boxed{\Delta_R=P-\alpha-W\delta.}
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

Define

$$
\boxed{\Delta_L=P-R\alpha-\delta.}
$$

Its signed length is

$$
R+\alpha-\frac{k}{W}
=
\frac{\Delta_L}{W}.
$$

Therefore

$$
\boxed{
\left\lvert T_C\cap e_{5,0}\right\rvert
=
\frac{[\Delta_L]_+}{W}.
}
$$

The positive right trace implies

$$
\delta<\frac{P}{W}
=
\frac{ER}{1+E}
<
\frac R2.
$$

On $e_{1,2}$, parameterized by $b=1+q$, $a=q$, one has

$$
F_2=\delta-R-Wq<0.
$$

Thus a second positive trace cannot lie on $e_{1,2}$. The exhaustive CE
classification says that a C triangle has at most two positive boundary
traces and that two such traces are adjacent. Hence $e_{5,0}$ is the only
possible companion edge.

Consequently

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

Equality $\Delta_L=0$ gives only a point contact and is therefore CE1 under
the positive-length definition.

## 3. Exact signed domain and midpoint set

For closures of original open center roles, the exact normalized signed domain
is

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

Since

$$
W(\alpha+\delta)
\le
\alpha+W\delta
<P,
$$

we obtain

$$
E-\alpha-\delta
>
E-\frac{P}{W}
=
\frac{E(E-R)}{W}.
$$

Moreover

$$
2E(E-R)-W=(E-R)^2>0,
$$

so

$$
\boxed{F_1(O)>\frac12.}
$$

Also

$$
\delta<\frac{P}{W}<\frac R2,
$$

and

$$
\alpha<P<\min\left\{\frac R2,\frac W2\right\}.
$$

The midpoint tests in `2100` therefore give

$$
\boxed{
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
}
$$

Conversely, the displayed side slacks define the proved unit-equilateral
edge-cut model, the three center slacks are positive, the right trace has
length $\Delta_R/R>0$, and the midpoint inequalities above hold. The sign of
$\Delta_L$ then gives exactly CE1 or CE2. Thus the signed domain is both
necessary and sufficient for closures of original open center roles.

For a merely closed C triangle, replace $\alpha>0$ and $\delta>0$ by the
appropriate weak inequalities; the strict versions are the ones used by the
open-cover proof tree.

## 4. One common list of radial exits

Let $d_i^C$ be the length of $T_C\cap[O,V_i]$, measured from $O$ toward $V_i$.
Substitution of the six radial parametrizations gives

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

For example, on $r_1$ the decreasing slack is $\delta-Rq$, and on $r_3$ the
two decreasing slacks are $\alpha-Rq$ and $\delta-Wq$. The remaining formulas
follow directly or by reflection.

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

In the CE1 sign range,

$$
\Delta_L\le0<\Delta_R
$$

implies

$$
R\alpha+\delta\ge P>\alpha+W\delta,
$$

and therefore

$$
R\delta>W\alpha.
$$

Thus

$$
\boxed{d_3^C=\frac{\alpha}{R}}
$$

in CE1; no separate CE1 exit calculation is needed.

## 5. Affine-chart dictionaries

### CE1

With $\kappa_j=F_j(O)$ for the auxiliary CE1 side slacks, the variables of
`2105` are

$$
\boxed{
\lambda=R,
\qquad
s=\frac{k}{R},
\qquad
t=W+\delta,
\qquad
\kappa_0=\alpha,
\qquad
\kappa_2=\delta.
}
$$

### CE2

The variables of `2106` are

$$
\boxed{
x=\frac{k}{W},
\qquad
u=R+\alpha,
\qquad
y=\frac{k}{R},
\qquad
v=W+\delta.
}
$$

In the preceding display, the signed endpoint variable is $\nu=R+\alpha$; hence

$$
T_C\cap e_{5,0}=[x,\nu],
\qquad
T_C\cap e_{0,1}=[y,v].
$$

Put

$$
S=x+y,
\qquad
D=\sqrt{x^2+xy+y^2}.
$$

Then

$$
S=\frac{k}{RW},
\qquad
D=\frac{Ek}{RW}.
$$

The CE2 coupling equation follows automatically:

$$
\begin{aligned}
(\nu+v)S-xy
&=
(1+\alpha+\delta)\frac{k}{RW}
-
\frac{k^2}{RW}\\
&=
\frac{Ek}{RW}\\
&=D.
\end{aligned}
$$

Thus the coupling is not an additional equation beyond the signed normal form.

## 6. Boundary contribution and reflection

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

and reverses the V-triangle order $1,2,3,4,5$. Every left-oriented statement is
obtained from its right-oriented form by this explicit substitution.
