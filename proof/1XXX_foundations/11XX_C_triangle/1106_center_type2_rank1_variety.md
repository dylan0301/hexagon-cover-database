# Center Type 2 Rank-One Variety

Status: Definition

Use degree-indexed ray-intersection distances. For
$\theta\in\{0,60,120,180,240,300\}$, let $e_\theta$ be the unit vector in direction $\theta$ degrees and let $r_\theta=\{te_\theta:t\ge0\}$. If

$$
\partial T_C\cap r_\theta=\{d_\theta e_\theta\},
$$

then the center triangle has six-distance tuple

$$
d_0,d_{60},d_{120},d_{180},d_{240},d_{300}.
$$

Impose positivity from the beginning.

Define

$$
M=\begin{pmatrix} d_{120} & d_0 & d_{240}\\ d_{60} & d_{300} & d_{180} \end{pmatrix}.
$$

## Euclidean derivation of the rank-one condition

Normalize Type 2 so that the vertices of $T_C$ lie in the alternating cones $C_0,C_2,C_4$. Then the three sides cut the three empty $60$-degree cones:

$$
(r_{60},r_{120}),\qquad (r_{180},r_{240}),\qquad (r_{300},r_0).
$$

In a $60$-degree cone, a line cutting the two boundary rays at distances $p$ and $q$ has its local direction determined by the ratio $q/p$. This is the elementary similar-triangle fact that all parallel cuts of the same $60$-degree cone have proportional intercepts.

The three sides of an equilateral triangle have the same local direction after rotating these three cones by multiples of $120$ degrees. Therefore the three side-intercept ratios are equal:

$$
\frac{d_{120}}{d_{60}} =\frac{d_0}{d_{300}} =\frac{d_{240}}{d_{180}}.
$$

Equivalently, the three columns

$$
\begin{pmatrix}d_{120}\\ d_{60}\end{pmatrix}, \qquad \begin{pmatrix}d_0\\ d_{300}\end{pmatrix}, \qquad \begin{pmatrix}d_{240}\\ d_{180}\end{pmatrix}
$$

are proportional. With positivity imposed, this is exactly the rank-one condition

$$
\mathrm{rank}(M)\le1.
$$

Thus

$$
M=\begin{pmatrix}a\\ b\end{pmatrix}\begin{pmatrix}x&y&z\end{pmatrix}, \qquad a,b,x,y,z\ge0.
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
S_{\mathrm{even}}=d_0+d_{120}+d_{240}, \qquad S_{\mathrm{odd}}=d_{60}+d_{180}+d_{300}.
$$

The normalization constraint is

$$
S_{\mathrm{even}}^2S_{\mathrm{odd}}^2- (S_{\mathrm{even}}^2-S_{\mathrm{even}}S_{\mathrm{odd}}+S_{\mathrm{odd}}^2)=0.
$$

When both sums are nonzero, this is equivalent to

$$
\frac1{S_{\mathrm{odd}}^2}-\frac1{S_{\mathrm{odd}}S_{\mathrm{even}}}+\frac1{S_{\mathrm{even}}^2}=1.
$$
