# Equilateral Enclosure Gauge and Universal Radical Calculus

Status: Proven

This note collects two pieces of geometry that otherwise appear under several
names in the local demand and direct-witness arguments.  The first is the
least-side functional for enclosing equilateral triangles.  The second is the
single radical $\sqrt{1-x+x^2}$ and the four exact local frontiers derived
from it.

## 1. The equilateral enclosure gauge

Let $\mathsf R$ denote counterclockwise rotation through $2\pi/3$. For a nonempty
compact set $K\subset\mathbb R^2$, put

$$
h_K(n)=\max_{x\in K}\langle x,n\rangle
$$

and

$$
\boxed{
\Lambda(K)
=
\frac{2}{\sqrt3}
\min_{\lVert n\rVert=1}
\sum_{j=0}^2 h_K(\mathsf R^jn).
}
$$

Then $\Lambda(K)$ is exactly the least side length of a closed equilateral
triangle containing $K$.

### Proof

For a fixed unit normal $n$, the three supporting half-planes with outward
normals $n,\mathsf Rn,\mathsf R^2n$ form an equilateral triangle. The sum of their three
support numbers is

$$
\sum_{j=0}^2h_K(\mathsf R^jn),
$$

and the corresponding side length is $2/\sqrt3$ times this sum.  Minimizing
over $n$ gives the least possible side.

The functional has the following immediate properties:

$$
K\subseteq L
\quad\Longrightarrow\quad
\Lambda(K)\le\Lambda(L),
$$

$$
\Lambda(K+x)=\Lambda(K),
$$

and

$$
\Lambda(tK)=t\Lambda(K)
\qquad(t\ge0).
$$

Translation invariance follows from

$$
n+\mathsf Rn+\mathsf R^2n=0.
$$

If $K$ is the convex hull of finitely many points, the minimizing normal may
be taken perpendicular to a hull edge.  Indeed, on an open angular cell on
which the three support points are fixed, the support sum is

$$
A\cos\theta+B\sin\theta
$$

and has second derivative equal to its negative.  In the nondegenerate case
an interior critical point is therefore a maximum, so a minimum occurs at a
cell boundary, where one support line contains two hull points.  This is the
finite-caliper principle used in the exact admissible set and in the direct
nine-point obstruction.

## 2. Local admissibility as a gauge sublevel set

Let

$$
u=\left(\frac12,\frac{\sqrt3}{2}\right),
\qquad
v=\left(\frac12,-\frac{\sqrt3}{2}\right),
$$

and

$$
K(a,b,c)=\mathrm{conv}\{0,au,bv,c(u+v)\}.
$$

Then the exact local admissible set is simply

$$
\boxed{
\mathcal A
=
\{(a,b,c)\in[0,1]^3:\Lambda(K(a,b,c))\le1\}.
}
$$

The piecewise support formulas and algebraic cells are those proved in
[`2004`](2004_admissible_set.md).  Thus Strategy 2 studies monotone fibers of
the same gauge whose superlevel obstruction is used in Strategy 4.

## 3. The universal equilateral radical

For $0\le x\le1$, put

$$
\boxed{
\omega(x)=\sqrt{1-x+x^2},
\qquad
\sigma(x)=1-\omega(x).
}
$$

Then

$$
\omega(1-x)=\omega(x),
$$

and rationalization gives

$$
\boxed{
\sigma(x)=\frac{x(1-x)}{1+\omega(x)}.
}
$$

Direct differentiation yields

$$
\omega'(x)=\frac{2x-1}{2\omega(x)},
$$

and

$$
\boxed{
\sigma''(x)=-\frac{3}{4\omega(x)^3}<0.
}
$$

Thus $\sigma$ is strictly concave.  The signed center variables satisfy

$$
E=\omega(R),
\qquad
\eta=\sigma(R),
$$

while the selected-$Q_+$ increment is the same function $\sigma$ in a
different normalized coordinate.

For $0<x<1$, put

$$
z=\frac{\sigma(x)}x.
$$

The identity

$$
x(1-x)=\sigma(x)(2-\sigma(x))
$$

solves rationally as

$$
\boxed{
x=\frac{1-2z}{1-z^2},
\qquad
\sigma(x)=\frac{z(1-2z)}{1-z^2},
\qquad
0<z<\frac12.
}
$$

## 4. Four-frontier atlas for the capped local map

The exact capped nonsupercritical map has four genuine frontiers.  The
selectors and interval domains remain those of
[`2011`](2011_capped_demand_map.md); this subsection records only the common
frontier equations.

### $\mathrm{Lin}$ frontier

$$
\boxed{b=1-a.}
$$

### $\mathrm{Const}$ frontier

If $m=\min\{a,b\}$ and $t=m/c$, the exact equation

$$
c^4-c^2+mc-m^2=0
$$

reduces to

$$
\boxed{
c=\omega(t),
\qquad
m=t\omega(t).
}
$$

### $Q_-$ frontier

If $t=a/c$, then

$$
\boxed{
a+b=\omega(t),
\qquad
b=\omega(t)-tc.
}
$$

The reflected formula exchanges $a$ and $b$.

### Selected $Q_+$ frontier

For deficit $d$, input $p$, output $q=\Phi_{1-d}(p)$, and increment
$\nu=q-p$, put

$$
x=\frac{q-d}{1-d}.
$$

The selected equation is

$$
x(1-x)=\nu(2-\nu),
$$

so the genuine component is

$$
\boxed{
\nu=\sigma(x),
\qquad
q=d+(1-d)x,
\qquad
p=d+(1-d)x-\sigma(x).
}
$$

Consequently every selected $Q_+$ arc is increasing and strictly concave in
its input.  This recovers the theorem in
[`2016`](2016_universal_Tplus_normal_form.md) while making explicit that the
same radical also governs the signed center and the other exact frontiers.
