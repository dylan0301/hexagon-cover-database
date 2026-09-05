# Four-Contact Disk Enclosure and Simultaneous Radius Transfer

Status: Proven

This note specializes the disk--finite-set caliper theorem in
[`2609`](2609_simplified_finite_enclosure_lemmas.md) to a convex three-point
chain outside a centered disk. It also transfers the paired tangent
certificates from a smaller disk to the actual disk. Neither argument uses
Minkowski sums or support-cap covering.

Throughout, $h=\sqrt3/2$, $\mathsf J$ is counterclockwise rotation by $\pi/2$,
and $\mathsf R$ is counterclockwise rotation by $2\pi/3$. Write
$[X,Y]=\operatorname{cross}(X,Y)$.

## 1. The four-contact hull

Let $\eta>0$ and let the nonzero vectors $A,B,C$ have lifted arguments

$$
\theta_A<\theta_B<\theta_C<\theta_A+\pi.
$$

Assume

$$
[B-A,C-B]>0,
\qquad
d_{AB}:=\frac{[A,B]}{\|B-A\|}>\eta,
\qquad
d_{BC}:=\frac{[B,C]}{\|C-B\|}>\eta.
$$

Put

$$
K=\operatorname{conv}(\mathbb B(0,\eta)\cup\{A,B,C\}),
$$

$$
H(n)=\max\{\eta,\langle A,n\rangle,\langle B,n\rangle,
\langle C,n\rangle\},\qquad
\Psi(n)=\sum_{j=0}^2 H(\mathsf R^j n).
$$

### Theorem 1.1 (four-contact formula)

Define the two point--point normals and the two exposed point--disk normals by

$$
n_{AB}=-\frac{\mathsf J(B-A)}{\|B-A\|},\qquad
n_{BC}=-\frac{\mathsf J(C-B)}{\|C-B\|},
$$

$$
t_A=\frac{\eta A-\sqrt{\|A\|^2-\eta^2}\,\mathsf JA}{\|A\|^2},
\qquad
t_C=\frac{\eta C+\sqrt{\|C\|^2-\eta^2}\,\mathsf JC}{\|C\|^2}.
$$

Then

$$
\boxed{\Lambda(K)=\frac1h
\min\{\Psi(n_{AB}),\Psi(n_{BC}),\Psi(t_A),\Psi(t_C)\}.}
$$

### Proof

The argument order gives $[A,B],[B,C],[A,C]>0$. The turn inequality
puts $C$ strictly on the inward side of the oriented line $AB$, and $A$
strictly on the inward side of $BC$. The distances $d_{AB},d_{BC}>\eta$
put the whole disk on those inward sides as well. Thus $AB$ and $BC$ are
exposed edges of $K$.

Moreover $[C-A,B-A]=-[B-A,C-B]<0$, whereas
$[C-A,-A]=[A,C]>0$. Hence $B$ and the origin lie on opposite sides of
$AC$, so $AC$ is not exposed. The convex boundary therefore consists of
$AB$, $BC$, the two tangent segments from the disk to the outer points
$A,C$, and the remaining circular arc. At $B$ the normal cone is bounded
by the normals of $AB,BC$, and the disk is strictly behind both lines;
there is no exposed point--disk tangent at $B$. Traversing the boundary
counterclockwise selects the minus sign at $A$ and the plus sign at $C$,
which gives the displayed tangent normals. In particular $\|A\|,\|C\|>\eta$.

The only changes of the active source of $H$ occur at these four normals.
Their $\mathsf R$-orbits partition the circle of orientations for $\Psi$.
On an open cell with $k$ disk sources,

$$
\Psi(n(\theta))=k\eta+\langle v,n(\theta)\rangle.
$$

If a point source is active, its projection is greater than $\eta>0$;
therefore $\Psi''=-\langle v,n(\theta)\rangle<0$. No interior minimum
occurs. On a disk-only cell $\Psi=3\eta$, and its minimum is also attained
at a cell boundary. Such a boundary exists because $\|A\|>\eta$, so the
disk is not the sole source in every direction. The support formula in
`2609` and $\Psi(\mathsf Rn)=\Psi(n)$ reduce all boundary directions to
the four in the statement. $\square$

## 2. Four sufficient contact inequalities

Assume in addition $0<\eta<h/3$, and that the ray order above fits in an
open cone of aperture $2\pi/3$. Put

$$
\Delta=[C,\mathsf RA]>0,\qquad \nu=\langle C,\mathsf RA\rangle,
\qquad N_X=\|X\|^2\quad(X=A,C),
$$

$$
P_X(\eta)=(N_X-\eta^2)\Delta^2-
\bigl((h-2\eta)N_X-\eta\nu\bigr)^2.
$$

The sign of $\Delta$ follows from
$0<\theta_A+2\pi/3-\theta_C<2\pi/3$.

### Corollary 2.1

If

$$
d_{AB},d_{BC}\ge h-2\eta,
\qquad P_A(\eta),P_C(\eta)\ge0,
$$

then $\Lambda(K)\ge1$.

### Proof

The line distances exceed $\eta$, so Theorem 1.1 applies. At the first two
contacts,

$$
\Psi(n_{AB})\ge d_{AB}+2\eta\ge h,\qquad
\Psi(n_{BC})\ge d_{BC}+2\eta\ge h.
$$

For the tangencies, choose $C$ as the support source at $\mathsf Rt_A$,
$A$ as the source at $\mathsf R^2t_C$, and the disk in the other two
directions. Direct substitution gives

$$
\Psi(t_A)\ge2\eta+
\frac{\eta\nu+\Delta\sqrt{N_A-\eta^2}}{N_A},
$$

$$
\Psi(t_C)\ge2\eta+
\frac{\eta\nu+\Delta\sqrt{N_C-\eta^2}}{N_C}.
$$

For $Z_X=(h-2\eta)N_X-\eta\nu$, the residual sign and $\Delta>0$ imply
$\Delta\sqrt{N_X-\eta^2}\ge|Z_X|\ge Z_X$. Both right sides are at least
$h$. The four-contact formula proves the result. $\square$

## 3. Simultaneous radius transfer

### Lemma 3.1

Let $X,Y$ be vectors in a normed real vector space and let $d\ge0$.
If $0\le e_0\le1/3$ and

$$
\|(1-2e_0)X-e_0Y\|\le d,
\qquad
\|(1-2e_0)Y-e_0X\|\le d,
$$

then both inequalities hold with $e_0$ replaced by every $e\in[e_0,1/3]$.

### Proof

Subtract the two vectors at $e_0$. Their difference is $(1-e_0)(X-Y)$,
so the triangle inequality gives

$$
\|X-Y\|\le\frac{2d}{1-e_0}\le3d.
$$

At $e=1/3$ the two vectors are $(X-Y)/3$ and $(Y-X)/3$, both in the
closed radius-$d$ ball. Each vector depends affinely on $e$. Convexity of
that ball gives both inequalities throughout $[e_0,1/3]$. The endpoint
case $e_0=1/3$ is immediate. $\square$

### Corollary 3.2 (paired tangent residuals)

In Section 2, suppose $0<\bar\eta\le\eta<h/3$ and
$P_A(\bar\eta),P_C(\bar\eta)\ge0$. Then
$P_A(\eta),P_C(\eta)\ge0$.

### Proof

Put $Y=\mathsf R^{-1}C$, $d=\Delta/h$ and $e=\eta/h$.
The planar Gram identity gives, for every $e$,

$$
P_A(he)=h^2N_A
\left(d^2-\|(1-2e)A-eY\|^2\right),
$$

$$
P_C(he)=h^2N_C
\left(d^2-\|(1-2e)Y-eA\|^2\right).
$$

Apply Lemma 3.1 at $e_0=\bar\eta/h$. The two residuals must be
transferred together; no monotonicity of either residual separately is
assumed. $\square$
