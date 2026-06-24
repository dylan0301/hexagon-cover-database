# Maximal $B_c(a)$ Map

Status: Definition

This file records the maximal next-edge coordinate for the full local
admissible set $\mathcal A$ from
[`2004_admissible_set.md`](2004_admissible_set.md). For fixed
$c\in[0,1]$, define

$$
B_c(a)=\max\left\{b\in[0,1]:(a,b,c)\in\mathcal A\right\}.
$$

The older working notation $b(c,a)$ refers to this same maximum. The
conditions below are written only in terms of $a$, $c$, and explicitly named
candidate functions of $a$ and $c$. A branch candidate contributes to
$B_c(a)$ only when its listed domain condition holds.

## Candidate Functions

The circle-boundary candidate is

$$
b_\circ(a)=\frac{-a+\sqrt{4-3a^2}}{2}.
$$

For $0<a<1$, set

$$
m_\circ(a)=\min(a,b_\circ(a)),\qquad
M_\circ(a)=\max(a,b_\circ(a)),
$$

and

$$
c_\circ(a)=
\frac{
M_\circ(a)(2m_\circ(a)M_\circ(a)+1)
-\sqrt{M_\circ(a)^2\left((2m_\circ(a)M_\circ(a)+1)^2
-4(1-m_\circ(a)^2)(1-M_\circ(a)^2)\right)}
}{2(1-m_\circ(a)^2)}.
$$

The boundary candidate is

$$
b_F(a)=1-a.
$$

The low candidate is

$$
b_L(c)=\frac{c\left(1-\sqrt{4c^2-3}\right)}{2}.
$$

For the $T_-$ candidate, define

$$
b_-(a,c)=-a+\frac{\sqrt{a^2-ac+c^2}}{c}
$$

when $c>0$.

For the two $T_+$ candidates, define

$$
\Delta_+(a,c)=(2ac^2+c)^2-4(1-c^2)(1-a^2)c^2,
$$

and, when $c\ne1$,

$$
b_+^\pm(a,c)=
\frac{
2ac^2+c
\pm\sqrt{\Delta_+(a,c)}
}{2(1-c^2)}.
$$

For the lower-side supercritical candidate, define

$$
b_S^-(a,c)=\frac{-a^2+\sqrt{a^2-ac+c^2}}{c}
$$

when $c>0$.

For the upper-side supercritical candidate, define

$$
\mathcal R_S^+(a,c)=
\left\{\rho\in[\max(a,1-a),b_\circ(a)]:
\rho^4+(2ac-1)\rho^2+c\rho+(a^2-1)c^2=0
\right\}.
$$

When $\mathcal R_S^+(a,c)$ is nonempty, set

$$
b_S^+(a,c)=\max \mathcal R_S^+(a,c).
$$

## Candidate Domains

The circle candidate is valid on

$$
D_\circ=\left\{(a,c):0<a<1,\ 0\le c\le c_\circ(a)\right\}.
$$

The boundary candidate is valid on

$$
D_F=\left\{(a,c):0\le a\le1,\ 0\le c\le\max(a,1-a)\right\}.
$$

The low candidate is valid on

$$
\begin{aligned}
D_L=\{(a,c):\;&4c^2-3\ge0,\ 0\le b_L(c)\le a,\ a+b_L(c)\le1,\\
&(a+b_L(c))^4-(a+b_L(c))^2+a b_L(c)\le0\}.
\end{aligned}
$$

The $T_-$ candidate is valid on

$$
\begin{aligned}
D_-=\{(a,c):\;&c>0,\ 0\le b_-(a,c)\le a,\ a+b_-(a,c)\le1,\\
&(a+b_-(a,c))^4-(a+b_-(a,c))^2+a b_-(a,c)\ge0\}.
\end{aligned}
$$

Each $T_+$ candidate is valid on

$$
\begin{aligned}
D_+^\pm=\{(a,c):\;&0\le c<1,\ \Delta_+(a,c)\ge0,\
b_+^\pm(a,c)\ge a,\ a+b_+^\pm(a,c)\le1,\\
&(a+b_+^\pm(a,c))^4-(a+b_+^\pm(a,c))^2
+a b_+^\pm(a,c)\ge0\}.
\end{aligned}
$$

The lower-side supercritical candidate is valid on

$$
\begin{aligned}
D_S^-=\{(a,c):\;&c>0,\ c\le\frac12,\
0\le b_S^-(a,c)\le a,\ a+b_S^-(a,c)\ge1,\\
&a^2+a b_S^-(a,c)+(b_S^-(a,c))^2\le1\}.
\end{aligned}
$$

The upper-side supercritical candidate is valid on

$$
D_S^+=\left\{(a,c):0\le a\le1,\ 0\le c\le\frac12,\
\mathcal R_S^+(a,c)\ne\varnothing\right\}.
$$

## Piecewise Summary

Let

$$
\begin{aligned}
\mathcal B_c(a)=&
\left\{b_\circ(a):(a,c)\in D_\circ\right\}
\cup\left\{b_F(a):(a,c)\in D_F\right\}\\
&\cup\left\{b_L(c):(a,c)\in D_L\right\}
\cup\left\{b_-(a,c):(a,c)\in D_-\right\}\\
&\cup\left\{b_+^+(a,c):(a,c)\in D_+^+\right\}
\cup\left\{b_+^-(a,c):(a,c)\in D_+^-\right\}\\
&\cup\left\{b_S^-(a,c):(a,c)\in D_S^-\right\}
\cup\left\{b_S^+(a,c):(a,c)\in D_S^+\right\}.
\end{aligned}
$$

Then the actual piecewise form is

$$
B_c(a)=
\begin{cases}
\max\mathcal B_c(a),
& 0\le a\le1,\ 0\le c\le1,\ \mathcal B_c(a)\ne\varnothing,\\
\text{undefined},
& \text{otherwise}.
\end{cases}
$$

The associated defect map is

$$
g_c(a)=1-B_c(a).
$$

## Branch Warning

The Cell 1/Cell 2 separator from
[`2004_admissible_set.md`](2004_admissible_set.md) is only a switching
interface before solving for candidate values. It is not an independent
maximal branch for $B_c(a)$. After solving for the branch candidates, use the
domain conditions above.
