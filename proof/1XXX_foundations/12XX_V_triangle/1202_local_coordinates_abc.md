# Local Coordinates $(a,b,c)$

Status: Definition

All indices are modulo $6$. For an open or closed $V_i$-triangle $T$, the
distinguished vertex $V_i$ is part of the role data. Define its actual
maximal reach functions by

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

$A(T)$ is the incoming reach toward $V_{i-1}$, $B(T)$ is the outgoing
reach toward $V_{i+1}$, and $C(T)$ is the own-radial reach toward $O$.
If $U$ is an open $V_i$-triangle, taking its closure does not change these
suprema:

$$
A(U)=A(\overline{U}),
\qquad
B(U)=B(\overline{U}),
\qquad
C(U)=C(\overline{U}).
$$

For an indexed role $T_i$, use the compact aliases

$$
(A_i,B_i,C_i)
:=
(A(T_i),B(T_i),C(T_i)).
$$

In admissible-set and propagation files, lowercase $(a,b,c)$ denotes a
prescribed lower-bound demand triple. A closed $V_i$-triangle $T$ realizes
that triple when

$$
0\le a\le A(T),
\qquad
0\le b\le B(T),
\qquad
0\le c\le C(T).
$$

For an open role $U$, its closure realizes every triple satisfying these weak
inequalities. The open role itself realizes every triple strictly below
$(A(U),B(U),C(U))$ coordinatewise.

When actual reaches and selected demands occur together, use uppercase
$(A_i,B_i,C_i)$ for the actual reaches and lowercase $(a_i,b_i,c_i)$ for the
selected demands. A file with no selected demands may retain the older
context-local convention in which indexed lowercase coordinates denote the
actual reaches, but it must state that convention explicitly.

Row-type conditions such as $A(T)+B(T)\le1$ or $A(T)+B(T)>1$ concern the
actual reaches, not arbitrary smaller demands.

On a center-free edge, coverage by the two incident closed V-triangle traces
requires

$$
B_i+A_{i+1}\ge1.
$$

The corresponding tight closed-trace chain is

$$
B_i+A_{i+1}=1.
$$
