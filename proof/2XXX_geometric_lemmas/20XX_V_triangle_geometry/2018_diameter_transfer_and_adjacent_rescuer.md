# Diameter Transfer and the Common Adjacent-Rescuer Obstruction

Status: Proven

This note isolates two elementary mechanisms used repeatedly in the CE1/CE2
branches: the diameter transfer between adjacent boundary edges and the common
center-trace argument for a T3-like or Vd1 V triangle rescuing a neighboring
supercritical V triangle.

The strict-supercritical functions are written with the single canonical
envelope $g_c^{\rm sc}$ from
[`201d`](201d_raw_and_relaxed_g_chains.md). Its complementary following-demand
bound is $1-g_c^{\rm sc}$.

## 1. The diameter-transfer curve

For $0\le q\le1$, define

$$
\boxed{
\beta(q)=\frac{-q+\sqrt{4-3q^2}}2.
}
$$

This is the larger nonnegative solution of

$$
q^2+qb+b^2=1.
$$

Consequently, if a unit equilateral triangle contains points at parameters
$q$ and $b$ on the two boundary edges incident to one hexagon vertex, then

$$
q^2+qb+b^2\le1
$$

and hence

$$
\boxed{b\le\beta(q).}
$$

For every $q>0$,

$$
\sqrt{4-3q^2}<2,
$$

so

$$
\boxed{
\beta(q)<1-\frac q2,
\qquad
1-\beta(q)>\frac q2.
}
$$

The same curve is the terminal diameter bound in the one-gap proofs and the
boundary-extent curve in the one-Vd1/Vd2 obstructions.

## 2. The free supercritical $g$-envelope

For $0\le c\le1/2$, put

$$
\boxed{
g_c^{\rm sc}
=
\frac{c+\sqrt{c^2-8c+4}}2.
}
$$

The free strict-supercritical theorem
[`2010`](2010_free_supercritical_max_b.md) says that a strict-supercritical V triangle
whose own-radial demand is at least $c$ has outgoing reach strictly less than
$g_c^{\rm sc}$.

The function $c\mapsto g_c^{\rm sc}$ is strictly decreasing on $[0,1/2]$,
because

$$
\frac{d}{dc}g_c^{\rm sc}
=
\frac12\left(
1+\frac{c-4}{\sqrt{c^2-8c+4}}
\right)<0,
$$

where the sign follows from

$$
(4-c)^2-(c^2-8c+4)=12>0.
$$

## 3. Common center-hiding lemma

Use the signed center variables from
[`2109`](../21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).
Thus the possible companion trace on $e_{5,0}$ is

$$
J_L=
\left[\frac{k}{W},R+\alpha\right]
$$

when $\Delta_L>0$, and there is no positive-length companion trace when
$\Delta_L\le0$. Also

$$
d_1^C=\frac{\delta}{R}.
$$

Let a local rescuer $T_0$ have boundary trace $[0,a]$ on $e_{5,0}$ and an
adjacent-radial trace $[c,u]$ on $r_1$, measured from $V_1$ toward $O$. Put

$$
\varepsilon=1-u>0,
\qquad
\theta=\frac{a}{a+\varepsilon}.
$$

Assume

$$
\boxed{
a\le1-g_c^{\rm sc},
\qquad
\theta\le1-g_c^{\rm sc},
}
$$

and assume that the center role must cover the $O$-side radial interval of
length $\varepsilon$ before the rescuer begins. Equivalently,

$$
\boxed{d_1^C\ge\varepsilon.}
$$

Let $h$ be the boundary reach forced on the opposite endpoint role $T_5$ along
$e_{5,0}$, measured from $V_5$ toward $V_0$. Then

$$
\boxed{h\ge g_c^{\rm sc}.}
$$

### Proof

If the center has no positive companion trace, the portion after $[0,a]$
forces

$$
h\ge1-a\ge g_c^{\rm sc}.
$$

The same conclusion holds when the companion trace lies completely before or
completely after the endpoint $a$: an open boundary gap begins at $a$, or the
remaining tail begins at $a$.

It remains to consider the only hiding configuration

$$
\frac{k}{W}\le a<R+\alpha.
$$

The radial hypothesis and $d_1^C=\delta/R$ give

$$
\delta\ge R\varepsilon.
$$

The left endpoint inequality gives

$$
k=\eta+\alpha+\delta\le Wa.
$$

In particular,

$$
R\varepsilon\le Wa,
$$

and hence

$$
R(a+\varepsilon)\le a.
$$

Thus

$$
\boxed{R\le\theta.}
$$

Moreover,

$$
\alpha
\le
Wa-R\varepsilon-\eta.
$$

Therefore the far endpoint of the companion trace satisfies

$$
\begin{aligned}
R+\alpha
&\le
R+Wa-R\varepsilon\\
&=
a+R(u-a).
\end{aligned}
$$

Since the hiding case has $R+\alpha>a$, the last inequality forces $u>a$.
Using $R\le\theta$,

$$
R+\alpha
\le
a+\theta(u-a).
$$

Because $u=1-\varepsilon$,

$$
a+\theta(u-a)
=
a+\frac{a}{a+\varepsilon}(1-\varepsilon-a)
=
\frac{a}{a+\varepsilon}
=
\theta.
$$

Consequently,

$$
R+\alpha
\le
\theta
\le
1-g_c^{\rm sc}.
$$

In the hiding case $T_5$ must reach the far center endpoint, so

$$
h
\ge
1-(R+\alpha)
\ge
g_c^{\rm sc}.
$$

This completes all cases.

## 4. Common adjacent-rescuer contradiction

Assume, in addition to the hypotheses of Section 3, that:

- $T_1$ is the unique strict-supercritical V triangle;
- coverage of $r_1$ forces its own-radial reach to be at least $c$;
- $T_2,T_3,T_4,T_5$ are nonsupercritical V triangles;
- these four V triangles must cover the ordinary boundary chain from $e_{1,2}$ to
  $e_{5,0}$.

The strict-supercritical theorem and monotonicity of $g_c^{\rm sc}$ give

$$
b_1<g_c^{\rm sc}.
$$

Section 3 gives

$$
h\ge g_c^{\rm sc}>b_1.
$$

The boundary obligations are

$$
a_2\ge1-b_1,
$$

$$
b_2+a_3\ge1,
\qquad
b_3+a_4\ge1,
\qquad
b_4+a_5\ge1,
$$

and

$$
b_5\ge h.
$$

Adding them yields

$$
\begin{aligned}
\sum_{i=2}^5(a_i+b_i)
&\ge
(1-b_1)+1+1+1+h\\
&=
4+(h-b_1)\\
&>4.
\end{aligned}
$$

But nonsupercriticality gives

$$
a_i+b_i\le1
\qquad(i=2,3,4,5),
$$

so the same sum is at most $4$. This contradiction proves the common
adjacent-rescuer obstruction once the local rescuer inequalities

$$
a\le1-g_c^{\rm sc},
\qquad
\frac{a}{a+1-u}\le1-g_c^{\rm sc}
$$

have been verified for the relevant T3-like or Vd1 normal form.
