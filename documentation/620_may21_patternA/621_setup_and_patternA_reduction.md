# Setup and Pattern A Reduction

Status: Proven local lemma

This file defines the May 21/22 four-point Pattern A target and proves the scalar reduction used by the rest of this folder.

## 1. Constrained slice

The May 21/22 slice is

$$
p=t_0=t_1,\qquad q=t_2=t_3,\qquad r=t_4=t_5,
$$

with

$$
q<r,\qquad q\le p\le r.
$$

The strict AB-union vertex is $V_4$:

$$
a_4=1-q,\qquad b_4=r,\qquad a_4+b_4=1-q+r>1.
$$

The required nonemptiness condition for $R_4=R(a_4,b_4)$ is

$$
r^2+r(1-q)+(1-q)^2\le1.
$$

In the lower outside-quarter region

$$
q<\frac14,
$$

this implies

$$
0\le q\le p\le r\le r_*:=\frac{\sqrt{37}-3}{8}<\frac25.
$$

## 2. Local coordinates and branch definitions

At $V_4$, use local coordinates $(u,v)$ with $u$ toward $V_5$ and $v$ toward $V_3$.  The metric is

$$
\|(u,v)\|^2=u^2+v^2-uv.
$$

Put

$$
\alpha=r,\qquad \beta=1-q.
$$

The exact nondegenerate strict $AB$-union frontier formula for these local
axis lengths is recorded in
[`../300_vertex_triangle/309_ab_union_curve_a_plus_b_gt_1.md`](../300_vertex_triangle/309_ab_union_curve_a_plus_b_gt_1.md).

The local-to-global map is

$$
T(u,v)=\left(-\frac12+u-\frac v2,\ -\frac{\sqrt3}{2}+\frac{\sqrt3}{2}v\right).
$$

### $P_3$ branch

The $C_2$ circle has local center $(\beta,\beta+1)$.  Define

$$
D_A^2=(u-\alpha)^2+v^2-(u-\alpha)v,
$$

$$
P_A=\alpha(\alpha-u+v)+\beta v,\qquad Q_A=\alpha(\alpha-u),
$$

$$
S_A=\alpha(\alpha+\beta-u)+\beta(v-u).
$$

The selected $P_3$ branch satisfies

$$
F_A(u,v):=P_A^2-D_A^2=0,
$$

and

$$
C_2(u,v):=(u-\beta)^2+(v-\beta-1)^2-(u-\beta)(v-\beta-1)-1=0,
$$

with

$$
P_A\ge0,\qquad Q_A\ge0,\qquad S_A\ge0,\qquad D_A^2\le1.
$$

### $P_5$ branch

The $C_5$ circle has local center $(\alpha+1,\alpha)$.  Define

$$
D_B^2=u^2+(v-\beta)^2-u(v-\beta),
$$

$$
P_B=\beta(\beta-v+u)+\alpha u,\qquad Q_B=\beta(\beta-v),
$$

$$
S_B=\beta(\alpha+\beta-v)+\alpha(u-v).
$$

The selected $P_5$ branch satisfies

$$
F_B(u,v):=P_B^2-D_B^2=0,
$$

and

$$
C_5(u,v):=(u-\alpha-1)^2+(v-\alpha)^2-(u-\alpha-1)(v-\alpha)-1=0,
$$

with

$$
P_B\ge0,\qquad Q_B\ge0,\qquad S_B\ge0,\qquad D_B^2\le1.
$$

When multiple algebraic roots exist, the branch used here is the active root closest to $V_4$ in the local metric $u^2+v^2-uv$.

Write

$$
P_3=T(u_3,v_3),\qquad P_5=T(u_5,v_5).
$$

## 3. Radial residuals

For a lower-region radial pair

$$
(a,b)=(1-A,B),\qquad 0\le B\le A<\frac25,
$$

define

$$
\rho(A,B)=1-c^{\max}(1-A,B).
$$

Then

$$
G_0=\rho(r,p)V_0,\qquad G_2=\rho(p,q)V_2.
$$

The Cell $1/2$ switch is

$$
\Phi(A,B)=(1-A+B)^4-(1-A+B)^2+B(1-A).
$$

For each $A\in(0,2/5)$, there is a unique $\sigma(A)\in(0,A)$ satisfying

$$
\Phi(A,\sigma(A))=0.
$$

For $B<\sigma(A)$,

$$
\rho(A,B)=\rho_1(B)=1-c_1(B),
$$

where $c_1(B)$ is the largest root in $[0,1]$ of

$$
c^4-c^2+Bc-B^2=0.
$$

For $B>\sigma(A)$,

$$
\rho(A,B)=\rho_2(A,B)=1-\frac{2(1-A)}{1+\sqrt{4(1-A+B)^2-3}}.
$$

Cell $3$ cannot occur for $G_0$ or $G_2$ in the lower region because $(1-r)+p\le1$ and $(1-p)+q\le1$.

## 4. Pattern A scalar reduction

Pattern A is the support contact structure

$$
(S_0,S_1,S_2)=\bigl(\{G_2\},\{P_3,P_5\},\{G_0\}\bigr).
$$

Set

$$
\Delta u=u_3-u_5,\qquad \Delta v=v_3-v_5,
$$

$$
D=\sqrt{\Delta u^2-\Delta u\Delta v+\Delta v^2},
$$

and

$$
N_0=\Delta v(1-u_5)-\Delta u(1-v_5).
$$

Let

$$
R=\rho(r,p)+\rho(p,q).
$$

A direct support-function computation gives

$$
L_A=\frac{N_0+R(\Delta v-\Delta u)}{D}.
$$

On the selected lower-region branch, $\Delta v-\Delta u>0$.  Hence

$$
L_A\ge1
$$

is equivalent to

$$
R\ge \tau(q,r),
$$

where

$$
\tau(q,r)=\frac{D-N_0}{\Delta v-\Delta u}.
$$

Thus Pattern A reduces to

$$
\rho(r,p)+\rho(p,q)\ge\tau(q,r).
$$
