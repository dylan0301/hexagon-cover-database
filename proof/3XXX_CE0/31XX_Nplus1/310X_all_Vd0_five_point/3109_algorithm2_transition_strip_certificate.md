# Algorithm-2 Transition Strip Certificate Outline

Status: Empirical / certificate outline

This file records the current certified-by-computation outline for the algorithm-2 transition strip. It is not a repository-grade certificate file: the interval subdivision data and verifier code are not included here. Therefore this file should not be cited as `Proven`.

The results here are conditional on the algorithm-2 construction, the strict line-branch realization from [`3105_strict_branch_line_realization.md`](3105_strict_branch_line_realization.md), and the convex cyclic order from [`3108_convex_order_from_line_branches.md`](3108_convex_order_from_line_branches.md).

## Transition Strip

Use

$$
p=1-b_4,\qquad q=1-a_4,\qquad p\le q.
$$

The transition strip is

$$
0.1\le p\le0.15.
$$

Let

$$
T(p,q)=(p+q)^4-(p+q)^2+pq.
$$

Let $q_0(p)$ be the unique root of $T(p,q)=0$. On $p=0.1$, the transition point is

$$
q_\eta=0.8518281505\ldots.
$$

The branch widths used in the interpolation certificate are

$$
q_0(p)-q_-(p)\le0.03174845,
$$

and

$$
1-p-q_0(p)\le0.07010087,
$$

where

$$
q_-(p)=\frac{3-p-\sqrt{1+6p-3p^2}}2.
$$

## Dangerous Edge

For the dangerous edge $P_3P_5$, the side-length branch is denoted $F(p,q)$. Numerical interval work in this chat supported the envelope

$$
F(p,q)\ge F_\eta+0.15(p-0.1)+0.25|T(p,q)|,
$$

where

$$
F_\eta=F(0.1,q_\eta)=1.0031590223\ldots.
$$

This gives $F>1$ on the transition strip, conditional on the recorded interval certificate.

## Non-Dangerous Edges

Under convex cyclic order, only the hull edges matter:

$$
D_0D_1,\qquad D_1D_2,\qquad D_2P_3,\qquad P_3P_5,\qquad P_5D_0.
$$

The edge $P_3P_5$ is the dangerous edge above. The other four are handled by lower bounds.

For $D_0D_1$,

$$
B_{01}=1+2r-v_5.
$$

For $D_1D_2$,

$$
B_{12}=1-u_3+\frac32r+\frac12(u_5-v_5).
$$

For $D_2P_3$,

$$
B_{23}=\frac{A_{23}}{\sqrt{L_{23}}},
$$

where

$$
A_{23}=r^2+rs-rt-ru-rv+2r+su-sv+tv-t-u+1,
$$

and

$$
L_{23}=r^2+ru-2rv+r+u^2-uv-u+v^2-v+1.
$$

For $P_5D_0$, use the stronger lower bound

$$
B_{40}^{(2)}=\frac{A_{40}^{(2)}}{\sqrt{L_{40}}},
$$

where

$$
A_{40}^{(2)}=-2rt-ru+rv+2r+su-sv+tv-t-u+1,
$$

and

$$
L_{40}=r^2-2rs+rt+r+s^2-st-s+t^2-t+1.
$$

The support split condition for this stronger bound was checked numerically on the strip through

$$
s-t-r>0.
$$

## Denominator-Free Checks

For $B_{23}$, it is enough to prove

$$
G_{23}:=A_{23}^2-L_{23}>0.
$$

For $B_{40}^{(2)}$, it is enough to prove

$$
G_{40}^{(2)}:=(A_{40}^{(2)})^2-L_{40}>0.
$$

The interpolation certificate used a coarse curvature bound

$$
|G_{23,qq}|\le1000,\qquad |G_{40,qq}^{(2)}|\le1000.
$$

On the quartic branch, the vertical interval was divided into $4$ pieces. On the mixed branch, it was divided into $12$ pieces. Endpoint curve lower bounds recorded in the computation were:

$$
G_{23}\ge0.0431230626,\qquad G_{40}^{(2)}\ge0.0103524421
$$

on the quartic endpoint curves, and

$$
G_{23}\ge0.0403426738,\qquad G_{40}^{(2)}\ge0.0077528147
$$

on the mixed endpoint curves.

The interpolation losses were bounded by

$$
\frac{1000}{8}\left(\frac{0.03174845}{4}\right)^2<0.007875,
$$

and

$$
\frac{1000}{8}\left(\frac{0.07010087}{12}\right)^2<0.004267.
$$

Thus the recorded interval computation gives positive lower bounds for $G_{23}$ and $G_{40}^{(2)}$ on the transition strip.

## Numerical Values At The Critical Point

At $(p,q)=(0.1,q_\eta)$, the recorded values are

$$
B_{23}=1.0610893569\ldots,
$$

and

$$
B_{40}^{(2)}=1.0470973033\ldots.
$$

For the dangerous edge,

$$
F=1.0031590223\ldots.
$$

## Status

This file records a certificate outline and numerical constants. To upgrade this to `Proven analytic inequality`, the repository still needs the actual verifier code or certificate data for the interval enclosures, including the selected-root branch checks for the 309 line-circle equations.
