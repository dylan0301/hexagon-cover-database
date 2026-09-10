# T3-like supported rescuer: actual-interval proof

Status: Proven

## Theorem and placement

Assume a skeleton cover with a nonzero actual gap, exactly one supercritical
V role, one T3-like role, and no Vd1 or Vd2 role. If the supercritical role is
center-aligned, the BC theorem in
[`2612`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md)
excludes the cover. Otherwise the supplier lemma in
[`2613`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2613_midpoint_supplier_reduction.md)
places the T3-like role at the C midpoint. Rotate and reflect so it is $T_0$,
$M_1\in U_0$, and $T_1$ is uniquely supercritical. The other four roles are
nonsupercritical Vd0.

All quantities below belong to the original triangles. We do not replace
the T3-like role by its translated closed-trace majorant.

## 1. Actual supported endpoints

Use the Type-II chart of `1201`,

$$
X=V_0+x(V_1-V_0)+y(V_5-V_0),\quad
U=\alpha_T+(1-t)x+ty,\quad V=a+tx-y,
$$

where $0<t<1$, $z=\sqrt{1-t+t^2}$, $\alpha_T>0$, and
$a=A_0>0$. The triangle is $U,V\ge0$, $U+V\le z$.
On $r_1$, whose coordinates are $(1,s)$, these give exactly

$$
c=\frac{1+\alpha_T+a-z}{1-t},\qquad u=a+t.
$$

Since $M_1\in U_0$, one has $0<c<1/2<u<1$.
Put $\varepsilon=1-u$. The supercritical own role stops before the midpoint;
all other neighboring contributions are absent. Thus $u$ is the actual total
radial endpoint, and the frontier lemma of `2612` forces
$P_T=\varepsilon V_1\in U_C$.
The near endpoint $c<1/2$ is not supplied by $U_0$, the C triangle, or a
nonlocal role; skeleton coverage gives $C_1\ge c$.

## 2. Ratio inequality for the original triangle

Put $x=a/(1-t)$ and $\theta=t/(1+z)$. Then $0<\theta<1/2$, and

$$
a+\varepsilon=1-t<1,\qquad
\frac a{a+\varepsilon}=x,\qquad
c=x+\theta+\frac{\alpha_T}{1-t}>x+\theta.
$$

The midpoint inequalities imply

$$
\frac{1-4\theta+\theta^2}{2(1-2\theta)}<x<1/2-\theta.
$$

For the lower endpoint use $t=\theta(2-\theta)/(1-\theta^2)$.
Let $Q_\theta(x)=2x^2+(\theta-1)x+\theta$.
When $0<\theta\le1/5$, the lower endpoint is to the right of the vertex,
and substitution gives

$$
Q_\theta(x)\ge
\frac{\theta(1-5\theta+11\theta^2-\theta^3)}{2(1-2\theta)^2}\ge0.
$$

For $1/5\le\theta<1/2$, its unrestricted minimum is
$(10\theta-1-\theta^2)/8>0$. Hence

$$
x^2+(c-2)x+c
=Q_\theta(x)+\frac{\alpha_T}{1-t}(x+1)>0.
$$

Here $0<x,c<1/2$. By the scalar ratio test of `2612`,

$$
x\le1-M_c^{\rm sup},\qquad
M_c^{\rm sup}=\frac{c+\sqrt{c^2-8c+4}}2.
$$

This proves the size and ratio requirements using the actual near endpoint.
Setting $\alpha_T=0$ would only give a lower bound on that endpoint. The full
range $0<t<1$ is included; no smaller orientation range is imposed.

## 3. Common four-point conclusion

The hypotheses now proved are

$$
\varepsilon V_1\in U_C,\quad C_1\ge c,\quad
a+\varepsilon\le1,\quad a/(a+\varepsilon)\le1-M_c^{\rm sup}.
$$

The common adapter in `2612`, Corollary 6.2, gives the fixed four-point set

$$
K_D=\{O,\varepsilon V_1,Y(a),Y(1-B_5)\},\qquad
Y(s)=(1-s)V_0+sV_5,
$$

with $K_D\subset U_C$ and $\Lambda(K_D)\ge1$, a contradiction to compact
containment in an open unit triangle. Both nonzero gap ranks use this same
argument. The witness and its pure geometric theorem are unchanged.
