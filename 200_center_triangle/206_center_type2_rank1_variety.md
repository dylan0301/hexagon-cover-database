# Center Type 2 Rank-One Variety

Status: Definition / algebraic characterization

Use degree-indexed variables

$$
d_0,d_{60},d_{120},d_{180},d_{240},d_{300}.
$$

Impose positivity from the beginning.

The point

$$
\left(\frac13,\dots,\frac13\right)
$$

means that the center triangle includes all six points at distance $1/3$ from the center along the six rays.

Define

$$
M=\begin{pmatrix}
d_{120} & d_0 & d_{240}\\
d_{60} & d_{300} & d_{180}
\end{pmatrix}.
$$

Type 2 imposes

$$
\operatorname{rank}(M)\le1.
$$

Thus

$$
M=\begin{pmatrix}a\\ b\end{pmatrix}\begin{pmatrix}x&y&z\end{pmatrix},
\qquad a,b,x,y,z\ge0.
$$

Equivalently,

$$
d_{120}=ax,\quad d_0=ay,\quad d_{240}=az,
$$

$$
d_{60}=bx,\quad d_{300}=by,\quad d_{180}=bz.
$$

Let

$$
S_{\mathrm{even}}=d_0+d_{120}+d_{240},
\qquad
S_{\mathrm{odd}}=d_{60}+d_{180}+d_{300}.
$$

The normalization constraint is

$$
S_{\mathrm{even}}^2S_{\mathrm{odd}}^2-
(S_{\mathrm{even}}^2-S_{\mathrm{even}}S_{\mathrm{odd}}+S_{\mathrm{odd}}^2)=0.
$$

When both sums are nonzero, this is equivalent to

$$
\frac1{S_{\mathrm{odd}}^2}-\frac1{S_{\mathrm{odd}}S_{\mathrm{even}}}+\frac1{S_{\mathrm{even}}^2}=1.
$$
