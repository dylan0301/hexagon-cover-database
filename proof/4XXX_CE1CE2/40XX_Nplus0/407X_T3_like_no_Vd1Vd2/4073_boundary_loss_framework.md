# Boundary-Loss Framework for the $407X$ Post-Reduction Branch

Status: Proven

This file records the boundary-loss reduction used after
[`4072_support_isolation_after_T0_T3_like.md`](4072_support_isolation_after_T0_T3_like.md).

It is a reduction statement.  It does not prove every branch inequality for the corrected $B$-map.  It proves that the relevant $B$-map inequalities imply the perimeter contradiction.

## 1. Standing branch

Assume the branch

$$
T_C\text{ is CE1 or CE2},\qquad N_+=0,
$$

with no Vd1/Vd2 rows and at least one T3-like row.  Normalize by the CE1/CE2 midpoint dependency so that

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
$$

By `4071`, $T_0$ is T3-like.  Reflect if necessary so that

$$
T_0\text{ has positive-length adjacent support on }r_1.
$$

By `4072`,

$$
r_1\text{ has positive-length support only from }T_C,T_0,T_1,
$$

and

$$
r_5\text{ has positive-length support only from }T_C,T_5.
$$

## 2. Direct $C$-triangle side model

Use local affine coordinates

$$
X_{\rm pt}=V_0+b(V_1-V_0)+a(V_5-V_0).
$$

Normalize the $C$-triangle overlap on $e_{0,1}$ as

$$
T_C\cap e_{0,1}=[s,t].
$$

Use the direct side model

$$
F_1=\lambda b+(1-\lambda)a-\lambda s,
$$

$$
F_2=-b+\lambda a+t,
$$

$$
F_0=(1-\lambda)b-a+\rho+\lambda s-t,
$$

where

$$
0<\lambda<1,\qquad \rho=\sqrt{1-\lambda+\lambda^2}.
$$

The center slacks are

$$
X:=F_0(O),\qquad Y:=F_2(O).
$$

Then

$$
t=1-\lambda+Y,
$$

$$
A_C:=1-t=\lambda-Y,
$$

and

$$
\lambda s=X+Y+1-\rho.
$$

The positive-length condition $s<t$ is equivalent to

$$
X+(1-\lambda)Y<\rho(1-\rho).
$$

The radial exits are

$$
\gamma_1=\min\left({Y\over\lambda},{\rho-X-Y\over1-\lambda}\right),
$$

and

$$
\gamma_5=\min\left({X\over1-\lambda},{\rho-X-Y\over\lambda}\right).
$$

When $T_C$ is CE2, write

$$
T_C\cap e_{5,0}=[S,T].
$$

Then

$$
S={X+Y+1-\rho\over1-\lambda},\qquad T=X+\lambda.
$$

For CE1, there is no positive-length $e_{5,0}$ interval.

## 3. T3-like $T_0$ data

Use the side-through-$V_0$ T3-like parameterization.  Let

$$
T_0\cap e_{5,0}=[0,\alpha],\qquad T_0\cap e_{0,1}=[0,p_1].
$$

There are parameters $D,R$ satisfying

$$
R^2-DR+D^2=1,\qquad D>1,
$$

and

$$
\alpha+p_1={1\over D}.
$$

Put

$$
q:=1-p_1=\alpha+{D-1\over D}.
$$

On $r_1$, measured from $V_1$ toward $O$, the $T_0$ interval is

$$
[c,u],\qquad c={Dq\over R},\qquad u=q+{1-R\over D}.
$$

In center-to-$V_1$ coordinates, this interval is

$$
[1-u,1-c].
$$

Thus $T_0$ hits the $T_C$ exit on $r_1$ iff

$$
1-u\le \gamma_1\le1-c.
$$

Otherwise it misses the exit.

## 4. Boundary requirements $A_1,A_5$

Let $J_1=T_C\cap e_{0,1}$ and $J_5=T_C\cap e_{5,0}$, with $J_5=\varnothing$ in the CE1 case.

For an initial $V_0$-side interval $[0,p]$ and a $C$-interval $J=[L,U]$, define the far-side boundary requirement

$$
\Theta(p,J)=
\begin{cases}
1-p,& J=\varnothing,\\
1-p,& p<L,\\
1-\max(p,U),& p\ge L.
\end{cases}
$$

Then

$$
A_1=\Theta(p_1,J_1),\qquad A_5=\Theta(\alpha,J_5).
$$

In particular, for $J_1=[s,t]$,

$$
A_1=\begin{cases}
q,& p_1<s,\\
1-t=A_C,& s\le p_1<t,\\
q,& p_1\ge t.
\end{cases}
$$

For CE2, if $J_5=[S,T]$, then

$$
A_5=\begin{cases}
1-\alpha,& \alpha<S,\\
1-T,& S\le\alpha<T,\\
1-\alpha,& \alpha\ge T.
\end{cases}
$$

Only the first two cases usually occur in the hard branch; the formula above is the definition used for the reduction.

## 5. Radial requirements $C_1,C_5$

Since $r_5$ has positive-length support only from $T_C,T_5$, the $T_5$ radial requirement is

$$
C_5=1-\gamma_5.
$$

For $r_1$ there are two cases.

### Case 1: $T_0$ hits the $T_C$ exit on $r_1$

If

$$
1-u\le\gamma_1\le1-c,
$$

then $T_C\cup T_0$ covers $r_1$ from $O$ up to the far endpoint of $T_0$.  The $T_1$ radial requirement is

$$
C_1=c.
$$

Equivalently,

$$
1-C_1=1-c.
$$

### Case 2: $T_0$ misses the $T_C$ exit on $r_1$

Then the remaining gap from the $V_1$ side forces

$$
C_1=1-\gamma_1.
$$

Equivalently,

$$
1-C_1=\gamma_1.
$$

## 6. Corrected $B$-map and the constrained $r_0$ variant

Use the corrected nonsupercritical $B$-map

$$
B(a,c)=\max\{b\in[0,1-a]:(a,b,c)\in\mathcal A\}.
$$

The explicit branch candidates and corrected branch-realization convention are recorded in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md)
and
[`../401X_all_Vd0_boundary_loss/4015_B_map_branch_realization.md`](../401X_all_Vd0_boundary_loss/4015_B_map_branch_realization.md).

If $T_1$ supports $r_0$, the right-side output must be bounded by the stricter constrained map

$$
B^{r_0}(A_1,C_1,d_0)
=
\max\{b:(A_1,b,C_1)\in\mathcal A,\ A_1+b\le1,\ C_-(A_1,b)\ge d_0\},
$$

where

$$
d_0=1-\gamma_0.
$$

Here $C_-$ is the lower-neighbor version of the adjacent-ray maximum from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md).

Since

$$
B^{r_0}(A_1,C_1,d_0)\le B(A_1,C_1),
$$

any inequality proved with $B(A_1,C_1)$ also proves the corresponding $r_0$-support branch.

## 7. Boundary-loss contradiction

### Theorem 7.1

Assume the support-isolated $407X$ branch above.  If

$$
B(A_5,C_5)+B(A_1,C_1)<1,
$$

then the seven triangles cannot cover the hexagon perimeter in this branch.

The same conclusion holds if $B(A_1,C_1)$ is replaced by the constrained map $B^{r_0}(A_1,C_1,d_0)$.

### Proof

The edge $e_{1,2}$ is covered from the $V_1$ side by $T_1$ by at most

$$
B_1:=B(A_1,C_1),
$$

or by the corresponding constrained value in the $r_0$-support case.  Hence $T_2$ must cover at least

$$
1-B_1
$$

from the $V_2$ side on $e_{1,2}$.

The middle edges require

$$
b_2+a_3\ge1,\qquad b_3+a_4\ge1.
$$

On the $e_{4,5}$ side, $T_5$ covers at most

$$
B_5:=B(A_5,C_5),
$$

so $T_4$ must cover at least

$$
1-B_5.
$$

Adding the four boundary requirements assigned to $T_2,T_3,T_4$ gives

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)
\ge
(1-B_1)+1+1+(1-B_5)
=4-(B_1+B_5).
$$

If

$$
B_1+B_5<1,
$$

then

$$
4-(B_1+B_5)>3.
$$

But $N_+=0$ gives

$$
a_i+b_i\le1\qquad(i=2,3,4),
$$

and therefore

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)\le3.
$$

This is a contradiction.  Hence perimeter coverage is impossible.
