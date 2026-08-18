# Diameter Transfer and the Common Adjacent-Rescuer Obstruction

Status: Proven

This note isolates two elementary mechanisms used repeatedly in the CE1/CE2
branches: the diameter transfer between adjacent boundary edges and the common
center-trace argument for a T3-like or Vd1 V triangle rescuing a neighboring
supercritical V triangle.

The strict-supercritical functions are written with the single canonical
envelope $M_c^{\rm sup}$ from
[`201d`](201d_raw_and_relaxed_g_chains.md). Its complementary following-demand
bound is $1-M_c^{\rm sup}$.

## 1. The zero-radial diameter-transfer envelope

For $0\le q\le1$, define

$$
\boxed{
M_0(q)=\frac{-q+\sqrt{4-3q^2}}2.
}
$$

This is the $c=0$ specialization of the exact envelope in
[`2007`](2007_max_b_map.md), using the canonical notation of
[`201d`](201d_raw_and_relaxed_g_chains.md).

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
\boxed{b\le M_0(q).}
$$

For every $q>0$,

$$
\sqrt{4-3q^2}<2,
$$

so

$$
\boxed{
M_0(q)<1-\frac q2,
\qquad
1-M_0(q)>\frac q2.
}
$$

Moreover,

$$
M_0'(q)=\frac{-1-3q/\sqrt{4-3q^2}}2<0,
$$

so $M_0$ is strictly decreasing.  It is the terminal diameter bound in the
one-gap proofs and the boundary-extent curve in the one-Vd1/Vd2 obstructions.

## 2. The free strict-supercritical envelope

For $0\le c<1/2$, put

$$
\boxed{
M_c^{\rm sup}
=
\frac{c+\sqrt{c^2-8c+4}}2.
}
$$

The free strict-supercritical theorem
[`2010`](2010_free_supercritical_max_b.md) says that a strict-supercritical V triangle
whose own-radial demand is at least $c$ has outgoing reach strictly less than
$M_c^{\rm sup}$.

The strict-supercritical feasible set is empty at $c=1/2$. When an endpoint
formula uses $M_{1/2}^{\rm sup}=1/2$, this denotes only the continuous
extension of the displayed expression, not an attained strict supremum.

The displayed expression, continuously extended to $c=1/2$, is strictly
decreasing on $[0,1/2]$, because

$$
\frac{d}{dc}M_c^{\rm sup}
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
a\le1-M_c^{\rm sup},
\qquad
\theta\le1-M_c^{\rm sup},
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
\boxed{h\ge M_c^{\rm sup}.}
$$

### Proof

If the center has no positive companion trace, the portion after $[0,a]$
forces

$$
h\ge1-a\ge M_c^{\rm sup}.
$$

The same conclusion holds when the companion trace lies completely before or
completely after the endpoint $a$: a boundary gap begins at $a$, or the
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
1-M_c^{\rm sup}.
$$

In the hiding case $T_5$ must reach the far center endpoint, so

$$
h
\ge
1-(R+\alpha)
\ge
M_c^{\rm sup}.
$$

This completes all cases.

## 4. Common adjacent-rescuer contradiction

Assume, in addition to the hypotheses of Section 3, that:

- $T_1$ is the unique strict-supercritical V triangle;
- coverage of $r_1$ forces its own-radial reach to be at least $c$;
- $T_2,T_3,T_4,T_5$ are nonsupercritical V triangles;
- these four V triangles must cover the ordinary boundary chain from $e_{1,2}$ to
  $e_{5,0}$.

Let $(A_i,B_i)$ denote the actual boundary reaches in this path. The
strict-supercritical theorem and monotonicity of $M_c^{\rm sup}$ give

$$
B_1<M_c^{\rm sup}.
$$

Section 3 gives

$$
h\ge M_c^{\rm sup}>B_1.
$$

The boundary obligations are

$$
A_2\ge1-B_1,
$$

$$
B_2+A_3\ge1,
\qquad
B_3+A_4\ge1,
\qquad
B_4+A_5\ge1,
$$

and

$$
B_5\ge h.
$$

Adding them yields

$$
\begin{aligned}
\sum_{i=2}^5(A_i+B_i)
&\ge
(1-B_1)+1+1+1+h\\
&=
4+(h-B_1)\\
&>4.
\end{aligned}
$$

But nonsupercriticality gives

$$
A_i+B_i\le1
\qquad(i=2,3,4,5),
$$

so the same sum is at most $4$. This contradiction proves the common
adjacent-rescuer obstruction once the local rescuer inequalities

$$
a\le1-M_c^{\rm sup},
\qquad
\frac{a}{a+1-u}\le1-M_c^{\rm sup}
$$

have been verified for the relevant T3-like or Vd1 normal form.
