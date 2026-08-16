# Universal Selected $Q_+$ Normal Form

Status: Proven

This note extracts the common nonlinear curve behind every selected $Q_+$
branch of the exact high-radial demand map in
[`2011_capped_demand_map.md`](2011_capped_demand_map.md).  It replaces
branch-specific implicit differentiation by one normalized equation, proves
strict concavity of the resulting transition map, and records an optional
rational parameter for later algebraic calculations.

## 1. Selected $Q_+$ transition equation

Fix a deficit

$$
0<d<\frac12
$$

and put

$$
c=1-d.
$$

Suppose an input $p$ lies on a genuine selected $Q_+$ branch of the high-radial map
$\Phi_c=1-\overline M_c$, and write

$$
q=\Phi_c(p),
\qquad
\nu=q-p.
$$

The exact selected quadratic from `2011` is

$$
(1-q)(q-d)=c^2\nu(2-\nu).
$$

Define the normalized output coordinate

$$
x=\frac{q-d}{c}.
$$

Every genuine selected $Q_+$ point has $0\le x\le1$.  Since

$$
q=d+cx,
\qquad
1-q=c(1-x),
$$

the selected equation reduces exactly to

$$
x(1-x)=\nu(2-\nu).
$$

The selected branch uses the smaller root in $\nu$, hence

$$
\boxed{
\nu=\psi(x):=1-\sqrt{1-x+x^2}.
}
$$

Consequently every selected $Q_+$ transition, in every high- or low-radial
regime in which it occurs, has the universal form

$$
\boxed{
q=d+(1-d)x,
\qquad
p=d+(1-d)x-\psi(x).
}
$$

All dependence on the V triangle deficit $d$ is affine.  The only nonlinear function
is the single branch-independent curve $\psi$.

## 2. Monotonicity and strict concavity

Put

$$
r(x)=1-x+x^2.
$$

Direct differentiation gives

$$
\psi'(x)=\frac{1-2x}{2\sqrt{r(x)}},
$$

and

$$
\boxed{
\psi''(x)=-\frac{3}{4r(x)^{3/2}}<0
\qquad(0\le x\le1).
}
$$

For fixed $d$, define

$$
p_d(x)=d+(1-d)x-\psi(x).
$$

Since $\psi'(x)\le1/2$ and $1-d>1/2$,

$$
p_d'(x)=1-d-\psi'(x)>0.
$$

Also

$$
p_d''(x)=-\psi''(x)=\frac{3}{4r(x)^{3/2}}>0.
$$

Thus $p_d$ is strictly increasing and strictly convex.  Its inverse $x=x(p)$
is strictly increasing and strictly concave.  Since

$$
q=d+(1-d)x
$$

is an increasing affine function of $x$, the selected transition is strictly
concave in its input:

$$
\boxed{
p\longmapsto \Phi_{1-d}(p)
\text{ is increasing and strictly concave on every selected }Q_+\text{ arc}.
}
$$

No contact-label-specific differentiation is needed.

## 3. Chord bounds

The preceding concavity gives the two chord estimates used in the CE1 and
T3-like branch proofs.

### 3.1. High-radial selected arc

Let

$$
e(d)=\ell(1-d).
$$

On the high-radial selected $Q_+$ arc the endpoint pairs are

$$
(p,q)=(d,d)
\qquad\text{and}\qquad
(p,q)=(e(d),d+e(d)).
$$

Therefore concavity gives, for every point on this arc,

$$
\boxed{
\Phi_{1-d}(p)
\ge
p+\frac{d}{e(d)-d}(p-d).
}
$$

### 3.2. Low-radial selected arc

Let

$$
t=h(1-d),
$$

where $h(c)$ is the order-transition value from `2011`.  On the low-radial
selected $Q_+$ arc the endpoint pairs are

$$
(p,q)=(d,d)
\qquad\text{and}\qquad
(p,q)=(t,1-t).
$$

Hence

$$
\boxed{
\Phi_{1-d}(p)
\ge
p+\frac{1-2t}{t-d}(p-d).
}
$$

Both estimates are consequences of the same universal curve.

## 4. Rational parameter

For $0<x<1$, put

$$
z=\frac{\psi(x)}x.
$$

The identity

$$
x(1-x)=\psi(x)(2-\psi(x))
$$

gives

$$
\boxed{
x=\frac{1-2z}{1-z^2},
\qquad
\psi(x)=\frac{z(1-2z)}{1-z^2},
\qquad
0<z<\frac12.
}
$$

Thus a selected $Q_+$ transition can also be written rationally as

$$
\boxed{
q=d+(1-d)\frac{1-2z}{1-z^2},
}
$$

and

$$
\boxed{
p=d+\frac{(1-2z)(1-d-z)}{1-z^2}.
}
$$

This rational parameter is optional.  The geometric proofs use only the
universal normal form and concavity; the rational form is useful when a later
calculation benefits from eliminating the square root
$\sqrt{1-x+x^2}$.

## 5. Translation to the historical $\beta$ parameter

Some files in the `407X` package use

$$
m_\beta=\sqrt{\beta^2-\beta+1}.
$$

Taking $x=1-\beta$ gives

$$
m_\beta=\sqrt{1-x+x^2}=1-\psi(x).
$$

With the rational parameter above,

$$
\boxed{
\beta=\frac{z(2-z)}{1-z^2},
\qquad
m_\beta=\frac{1-z+z^2}{1-z^2}.
}
$$

Hence every occurrence of the local high-sheet radical $m_\beta$ may be
replaced by one rational parameter without changing the selected component or
its endpoint conventions.
