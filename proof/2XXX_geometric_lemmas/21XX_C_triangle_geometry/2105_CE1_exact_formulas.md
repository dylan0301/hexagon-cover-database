# CE1 Exact Center, Interval, Radial-Exit, and Demand Formulas

Status: Proven

This note records exact formulas for a normalized CE1 center triangle with
unique midpoint $M_0$. It uses the interval certificate in
[`2102_CE1_M0_e01_maximal_intervals.md`](2102_CE1_M0_e01_maximal_intervals.md).

## General center-and-angle model

Write

$$
u(\alpha)=(\cos\alpha,\sin\alpha).
$$

A unit equilateral triangle with centroid $z$ and angle $\theta$ has vertices

$$
z+\frac1{\sqrt3}
u\left(\theta+\frac\pi2+\frac{2\pi k}{3}\right),
\qquad k=0,1,2.
$$

Its outward normals and support constants are

$$
n_k=u\left(\theta-\frac\pi2+\frac{2\pi k}{3}\right),
$$

$$
h_k=\frac1{2\sqrt3}+n_k\mathbin{\cdot}z.
$$

Thus

$$
T_C=\left\{p:n_k\mathbin{\cdot}p\le h_k, k=0,1,2\right\}.
$$

The exact center condition is

$$
O\in T_C\quad\Longleftrightarrow\quad h_k\ge0\text{ for every }k,
$$

with strict inequalities for $O\in\mathrm{int}(T_C)$.

For the ray from $O$ toward $V_i$, the exit distance inside the unit radial
segment is

$$
d_i=
\min\left\{
1,
\min_{\substack{0\le k\le2\\n_k\mathbin{\cdot}V_i>0}}
\frac{h_k}{n_k\mathbin{\cdot}V_i}
\right\}.
$$

For a boundary edge

$$
e_i(q)=V_i+q(V_{i+1}-V_i),
\qquad 0\le q\le1,
$$

put

$$
A_{ik}=n_k\mathbin{\cdot}V_i,
\qquad
B_{ik}=n_k\mathbin{\cdot}(V_{i+1}-V_i).
$$

When every constraint with $B_{ik}=0$ satisfies $A_{ik}\le h_k$, the exact
clipped interval is

$$
s_i=
\max\left\{
0,
\max_{B_{ik}<0}\frac{h_k-A_{ik}}{B_{ik}}
\right\},
$$

$$
t_i=
\min\left\{
1,
\min_{B_{ik}>0}\frac{h_k-A_{ik}}{B_{ik}}
\right\}.
$$

It is nonempty exactly when $s_i\le t_i$.
An empty inner maximum or minimum contributes no bound.

## Normalized CE1 side model

Use affine coordinates

$$
X=V_0+b(V_1-V_0)+a(V_5-V_0).
$$

Write

$$
T_C\cap e_{0,1}=[s,t].
$$

For

$$
0<\lambda<1,
\qquad
\rho=\sqrt{1-\lambda+\lambda^2},
$$

set

$$
F_1=\lambda b+(1-\lambda)a-\lambda s,
$$

$$
F_2=-b+\lambda a+t,
$$

$$
F_0=(1-\lambda)b-a+\rho+\lambda s-t.
$$

Then

$$
T_C=\left\{F_0\ge0,F_1\ge0,F_2\ge0\right\}.
$$

Define

$$
C_0=F_0(O)=\rho+\lambda s-t-\lambda,
$$

$$
C_1=F_1(O)=1-\lambda s,
$$

$$
C_2=F_2(O)=t+\lambda-1.
$$

They satisfy

$$
C_0+C_1+C_2=\rho.
$$

## Exact CE1 domain

The normalized closed exact-$M_0$ CE1 domain is

$$
0<\lambda<1,
\qquad
0\le s<t\le1,
$$

$$
t+\lambda(1-s)\le\rho,
$$

$$
t\ge1-\lambda,
$$

$$
\lambda s\le\frac12,
$$

$$
t<1-\frac\lambda2,
$$

$$
t>\rho+\lambda s-\frac{1+\lambda}{2},
$$

and

$$
t\ge\rho-\frac{\lambda^2}{1-\lambda}s.
$$

The first two nontrivial weak inequalities are $C_0\ge0$ and $C_2\ge0$.
For the closure of an open center role, replace them by

$$
C_0>0,
\qquad
C_2>0.
$$

The last inequality excludes a positive-length overlap with $e_{5,0}$.

## Ray substitutions

Let $q$ denote distance from $O$ toward $V_i$. In the affine $(b,a)$
coordinates,

$$
r_0(q)=(1-q,1-q),
\qquad
r_1(q)=(1,1-q),
$$

$$
r_2(q)=(1+q,1),
\qquad
r_3(q)=(1+q,1+q),
$$

$$
r_4(q)=(1,1+q),
\qquad
r_5(q)=(1-q,1).
$$

Substitution gives the decreasing slacks and their first zeros:

| ray | decreasing slack or slacks | first exit |
|---|---|---|
| $r_0$ | $F_1=C_1-q$ | $C_1$ |
| $r_1$ | $F_2=C_2-\lambda q$ and $F_1=C_1-(1-\lambda)q$ | $C_2/\lambda$ |
| $r_2$ | $F_2=C_2-q$ | $C_2$ |
| $r_3$ | $F_0=C_0-\lambda q$ and $F_2=C_2-(1-\lambda)q$ | $\min\{C_0/\lambda,C_2/(1-\lambda)\}$ |
| $r_4$ | $F_0=C_0-q$ | $C_0$ |
| $r_5$ | $F_0=C_0-(1-\lambda)q$ and $F_1=C_1-\lambda q$ | $C_0/(1-\lambda)$ |

For $r_1$, exact exclusion of $M_1$ gives $C_2/\lambda<1/2$, while
$M_0\in T_C$ gives $C_1/(1-\lambda)>1/2$. Thus the listed first exit is
correct. The $r_5$ statement is the reflected argument.

## Exact radial exits and demands

Therefore

$$
\boxed{
\begin{aligned}
d_0&=1-\lambda s,\\
d_1&=\frac{C_2}{\lambda},\\
d_2&=C_2,\\
d_3&=\min\left\{
\frac{C_0}{\lambda},
\frac{C_2}{1-\lambda}
\right\},\\
d_4&=C_0,\\
d_5&=\frac{C_0}{1-\lambda}.
\end{aligned}
}
$$

The complementary vertex-role radial demands are

$$
c_i=1-d_i.
$$

Explicitly,

$$
\boxed{
\begin{aligned}
c_0&=\lambda s,\\
c_1&=1-\frac{C_2}{\lambda},\\
c_2&=1-C_2,\\
c_3&=1-\min\left\{
\frac{C_0}{\lambda},
\frac{C_2}{1-\lambda}
\right\},\\
c_4&=1-C_0,\\
c_5&=1-\frac{C_0}{1-\lambda}.
\end{aligned}
}
$$

Since the midpoint subset is exactly $\{M_0\}$,

$$
d_0\ge\frac12,
\qquad
d_i<\frac12\quad(i\ne0),
$$

and hence

$$
c_0\le\frac12,
\qquad
c_i>\frac12\quad(i\ne0).
$$

## Direction of the radial relaxation

Suppose the actual radial reach of $T_i$ from $V_i$ is $\widehat c_i$. Full
coverage of $r_i$ gives

$$
\widehat c_i\ge1-d_i=c_i.
$$

If $c'\ge c$, the demand point at $c$ lies on the segment from $V_i$ to the
demand point at $c'$. Convexity therefore gives

$$
\left\{T_i:\widehat c_i\ge c'\right\}
\subset
\left\{T_i:\widehat c_i\ge c\right\}.
$$

Replacing the actual reach by $c_i=1-d_i$ enlarges the feasible row set and is
therefore a valid relaxation in the required direction.
