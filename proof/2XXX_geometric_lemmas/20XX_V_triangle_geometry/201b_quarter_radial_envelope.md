# Quarter Radial Envelope

Status: Proven

This note gives a short global radial envelope for the exact local admissible
set.  It is weaker than the historical coefficient $1/3$ on the half-edge
domain, but it has no half-edge hypothesis and is sufficient for the shortened
adjacent Vd1/Vd2 obstruction.

## Theorem

Suppose

$$
0\le h\le p,
\qquad
p+h<1.
$$

Then

$$
\boxed{
c_{\max}(p,h)\le1-\frac h4.
}
$$

The inequality is strict on the selected $\mathcal A_T$ component.  Equality
can occur only at $h=0$ on the $\mathcal A_L$ component.

## Proof

Put

$$
s=p+h,
\qquad
q=s^4-s^2+ph.
$$

Since $s<1$, the supercritical cell $\mathcal A_S$ is absent.  The exact
admissible-set theorem in [`2004`](2004_admissible_set.md) leaves only the two
nonsupercritical cells $\mathcal A_L$ and $\mathcal A_T$.

### The $\mathcal A_L$ cell

Because $h\le p$, the smaller boundary coordinate is $h$.  The selected radial
frontier is the unique root in $[\sqrt3/2,1]$ of

$$
P_h(c)=c^4-c^2+hc-h^2=0.
$$

Put

$$
c_0=1-\frac h4.
$$

Direct substitution gives

$$
P_h(c_0)
=
\frac h{256}
\left(h^3-16h^2-240h+128\right).
$$

The cubic in parentheses is decreasing on $[0,1/2]$, and at $h=1/2$ it equals

$$
\frac{33}{8}>0.
$$

Hence $P_h(c_0)>0$ for $h>0$.  On the other hand,

$$
P_h\left(\frac{\sqrt3}{2}\right)
=
-\left(h-\frac{\sqrt3}{4}\right)^2
\le0,
$$

and

$$
P_h'(c)=4c^3-2c+h>0
\qquad
\left(c\ge\frac{\sqrt3}{2}\right).
$$

Therefore the selected root satisfies

$$
c_{\max}(p,h)<c_0
$$

when $h>0$.  For $h=0$, the selected root is $1=c_0$.

### The $\mathcal A_T$ cell

Now $q>0$.  Put

$$
r=\sqrt{4s^2-3}.
$$

The selected radial root is

$$
c_T=\frac{2p}{1+r}.
$$

Let

$$
\gamma=\frac{p-h}{s}.
$$

The exact identity

$$
\frac q{s^2}=\frac{r^2-\gamma^2}{4}
$$

gives $0\le\gamma<r$.  Write

$$
\gamma=wr,
\qquad
0\le w<1.
$$

Then

$$
p=\frac{s(1+wr)}2,
\qquad
h=\frac{s(1-wr)}2,
$$

and

$$
c_T=\frac{s(1+wr)}{1+r}.
$$

For fixed $s,r$, define

$$
\Psi(w)=c_T+\frac h4.
$$

Differentiation gives

$$
\Psi'(w)
=
\frac{sr(7-r)}{8(1+r)}>0.
$$

Thus

$$
\Psi(w)<\Psi(1)=\frac{s(9-r)}8.
$$

Since $4s^2=r^2+3$, the inequality $s(9-r)\le8$ is equivalent to

$$
(r^2+3)(9-r)^2\le256.
$$

The difference factors as

$$
256-(r^2+3)(9-r)^2
=
(1-r)(r^3-17r^2+67r+13).
$$

The cubic is positive on $[0,1]$: its derivative is

$$
3r^2-34r+67>0
$$

there, and its value at $0$ is $13$.  Therefore

$$
c_T+\frac h4<1,
$$

which is the strict estimate

$$
c_T<1-\frac h4.
$$

The two exact nonsupercritical cells are exhausted, proving the theorem.
