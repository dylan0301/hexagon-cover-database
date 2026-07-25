# Exact Disk-Plus-Point Equilateral Enclosure

Status: Proven

This note records an optional preliminary enclosure test for the direct
nine-point strategy.  It is not used by the canonical `31051`--`31059` proof
and is not a manuscript dependency.  The result evaluates exactly the least
equilateral-triangle side needed to contain a centered disk together with one
point.

## 1. Support formula

Put

$$
h=\frac{\sqrt3}{2},
$$

and let $R$ denote counterclockwise rotation through $2\pi/3$.  For a compact
plane set $K$, the least side length of a closed equilateral triangle
containing $K$ is

$$
\Lambda(K)
=
\frac1h
\min_{\lVert n\rVert=1}
\sum_{j=0}^2 h_K(R^j n),
$$

where

$$
h_K(n)=\max_{Y\in K}\langle Y,n\rangle.
$$

Let

$$
K=\mathcal D_\eta\cup\{X\},
\qquad
\mathcal D_\eta=\{Y:\lVert Y\rVert\le\eta\},
\qquad
r=\lVert X\rVert.
$$

Then

$$
h_K(n)=\max\{\eta,\langle X,n\rangle\}.
$$

## 2. Exact formula

### Theorem

For every $\eta\ge0$ and every point $X$ of norm $r$,

$$
\boxed{
\Lambda\left(\mathcal D_\eta\cup\{X\}\right)
=
\begin{cases}
\dfrac{3\eta}{h},&r\le2\eta,\\[3mm]
\dfrac{3\eta+\sqrt{3(r^2-\eta^2)}}{2h},&r>2\eta.
\end{cases}
}
$$

### Proof

For a unit vector $n$, put

$$
s_j=\langle X,R^j n\rangle
\qquad(0\le j\le2).
$$

The three directions sum to zero, so

$$
s_0+s_1+s_2=0.
$$

The support sum is

$$
\Sigma(n)=\sum_{j=0}^2\max\{\eta,s_j\}.
$$

Assume first that $r\le2\eta$.  Every summand is at least $\eta$, hence

$$
\Sigma(n)\ge3\eta.
$$

Choose the orientation for which the three projections are

$$
\frac r2,
\qquad
\frac r2,
\qquad
-r.
$$

The first two are at most $\eta$, so equality holds:

$$
\min_n\Sigma(n)=3\eta.
$$

Now assume $r>2\eta$ and put

$$
k=\frac\eta r<\frac12.
$$

On any open angular cell on which the active support labels are fixed,
$\Sigma$ is a constant plus either one point projection or the sum of two
point projections.  With one active point projection, every interior critical
point is a maximum of that cosine.  With two active point projections, their
sum is the negative of the inactive projection, so again every interior
critical point is a maximum.  Therefore a minimum occurs on a switching
boundary where one normalized point projection equals $k$.

At such a boundary, let the other two normalized projections be $y,z$.  They
satisfy

$$
y+z=-k.
$$

The standard identity for three $120$-degree projections gives

$$
k^2+y^2+z^2=\frac32.
$$

Solving these two equations yields

$$
\{y,z\}
=
\left\{
\frac{-k+\sqrt{3(1-k^2)}}2,
\frac{-k-\sqrt{3(1-k^2)}}2
\right\}.
$$

Because $k<1/2$, the first value is greater than $k$ and the second is less
than $k$.  Thus exactly one of the other two point projections is active, and
the support sum at the minimizing switching boundary is

$$
2\eta
+
\frac r2\left(-k+\sqrt{3(1-k^2)}\right).
$$

Since $rk=\eta$, this is

$$
\frac{3\eta+\sqrt{3(r^2-\eta^2)}}2.
$$

Dividing by $h$ proves the second formula. $\square$

## 3. Strategy 4 consequence

In the direct nine-point package, the six radial witnesses force the centered
disk of radius

$$
\eta=h(1-c_*).
$$

Assume the nonautomatic regime

$$
c_*>\frac23.
$$

For any one of the forced asymmetric witnesses $Q\in\{Q_-,Q_0,Q_+\}$, the
theorem gives

$$
\Lambda\left(\mathcal D_\eta\cup\{Q\}\right)\ge1
$$

whenever

$$
\boxed{
\lVert Q\rVert^2\ge1-3c_*+3c_*^2.
}
$$

Indeed the displayed norm inequality is exactly the square of

$$
3\eta+\sqrt{3(\lVert Q\rVert^2-\eta^2)}\ge2h.
$$

Moreover,

$$
1-3c_*+3c_*^2-4\eta^2=3c_*-2>0,
$$

so this criterion automatically lies in the second branch
$\lVert Q\rVert>2\eta$ of the exact formula.

Consequently,

$$
\boxed{
\max_{\nu\in\{-,0,+\}}\lVert Q_\nu\rVert^2
\ge1-3c_*+3c_*^2
\quad\Longrightarrow\quad
\Lambda(K_{\mathrm{wit}})\ge1.
}
$$

This closes a genuine subregion using the disk and only one asymmetric
witness.  The inequality is not asserted on the full strict handoff domain,
and the canonical proof continues to use all three asymmetric witnesses and
the Newton four-cap certificate.