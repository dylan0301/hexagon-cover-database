# Free Supercritical Maximal $b$ Function

Status: Definition

This file records the one-variable maximal outgoing edge coordinate when the
incoming edge coordinate is unconstrained and the local triple is required to
be supercritical.

The word free means that there is no lower-bound condition on the incoming
edge coordinate. Thus the actual incoming coordinate is existentially
quantified.

Define the strict supercritical envelope

$$
B^{\mathrm{free},+}(c)
=
\sup\left\{b:\exists x\in[0,1]\text{ with }(x,b,c)\in\mathcal A,\ x+b>1\right\}.
$$

Define also the closed supercritical envelope

$$
\overline B^{\mathrm{free},+}(c)
=
\max\left\{b:\exists x\in[0,1]\text{ with }(x,b,c)\in\mathcal A,\ x+b\ge1\right\}.
$$

Here $\mathcal A$ is the admissible set from
[`2004_admissible_set.md`](2004_admissible_set.md).

## Formula

The closed envelope is

$$
\overline B^{\mathrm{free},+}(c)
=
\begin{cases}
\dfrac{c+\sqrt{c^2-8c+4}}{2}, & 0\le c\le\dfrac12,\\
\text{undefined}, & \text{otherwise}.
\end{cases}
$$

The strict envelope is the corresponding supremum:

$$
B^{\mathrm{free},+}(c)
=
\begin{cases}
\dfrac{c+\sqrt{c^2-8c+4}}{2}, & 0\le c<\dfrac12,\\
\text{undefined}, & \text{otherwise}.
\end{cases}
$$

The realizing closed-boundary incoming coordinate is

$$
x(c)=1-\overline B^{\mathrm{free},+}(c).
$$

Thus the closed envelope is realized on the boundary

$$
x(c)+\overline B^{\mathrm{free},+}(c)=1.
$$

For $0\le c<1/2$, strict supercritical triples with $x+b>1$ approach this
boundary value from the supercritical side. At $c=1/2$, the displayed closed
value is a boundary value only.

## Derivation

On the supercritical branch with $x\le b$, the frontier equation is

$$
(x^2-1)c^2+b(2xb+1)c+(b^4-b^2)=0.
$$

On the closed envelope, the active boundary is

$$
x+b=1.
$$

Substituting $x=1-b$ gives

$$
b(b-c)(b^2-cb+2c-1)=0.
$$

The maximal admissible root is therefore the larger root of

$$
b^2-cb+2c-1=0,
$$

namely

$$
b=\frac{c+\sqrt{c^2-8c+4}}{2}.
$$
