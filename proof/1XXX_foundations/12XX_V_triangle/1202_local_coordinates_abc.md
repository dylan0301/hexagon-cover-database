# Local Reach Coordinates

Status: Definition

All indices are modulo $6$.  For an open or closed $V_i$ triangle $T$, define
its actual maximal reaches by

$$
\begin{aligned}
A(T)
&=
\sup_{\substack{t\in[0,1]\\
V_i+t(V_{i-1}-V_i)\in T}} t,\\
B(T)
&=
\sup_{\substack{t\in[0,1]\\
V_i+t(V_{i+1}-V_i)\in T}} t,\\
C(T)
&=
\sup_{\substack{t\in[0,1]\\
V_i+t(O-V_i)\in T}} t.
\end{aligned}
$$

$A(T)$ is the backward-boundary reach, $B(T)$ is the forward-boundary reach,
and $C(T)$ is the own-radial reach.  Passing from an open V triangle to its
closure does not change these suprema.

For the indexed triangles write

$$
(A_i,B_i,C_i)=(A(T_i),B(T_i),C(T_i)).
$$

A selected lower-bound triple is written $(a,b,c)$ and is realized by a closed
V triangle $T$ when

$$
0\le a\le A(T),
\qquad
0\le b\le B(T),
\qquad
0\le c\le C(T).
$$

When actual and selected data occur together, use

$$
(A_i,B_i,C_i)
\quad\text{for actual reaches},
\qquad
(a_i,b_i,c_i)
\quad\text{for selected lower bounds}.
$$

Indexed lowercase reaches are never used for actual maxima.  A local theorem
may use unindexed dummy variables $a,b,c$ for explicitly declared quantities,
but that convention does not alter the indexed notation.

Conditions such as

$$
A_i+B_i\le1
\qquad\text{or}\qquad
A_i+B_i>1
$$

always concern actual reaches.  On a center-free edge, coverage by the two
incident closed V-triangle traces requires

$$
B_i+A_{i+1}\ge1.
$$

The corresponding tight closed-trace chain is

$$
B_i+A_{i+1}=1.
$$
