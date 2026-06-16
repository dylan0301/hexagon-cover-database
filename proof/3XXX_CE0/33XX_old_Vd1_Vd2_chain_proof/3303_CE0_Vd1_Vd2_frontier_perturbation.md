# CE0 + Vd1/Vd2 Frontier Perturbation

Status: Proven

Let

$$
S=\{(X,Y)\in[0,1]^2:X^2+Y^2+XY=1\}.
$$

For $(X,Y)\in S$, define

$$
H_1(X,Y)=\frac{Y}{X}(X+Y-1)=\frac{Y^2}{X+Y+1},
$$

$$
H_2(X,Y)=\frac{X}{Y}(X+Y-1)=\frac{X^2}{X+Y+1}.
$$

Fix $(x,y)\in S$ and $t\ge0$. Define

$$
a(t)=H_1(x,y)+t,
$$

$$
b(t)=H_2(x,y)-t\frac{x+y}{y}.
$$

Assume $(x,y,t)$ is strictly valid, meaning $a(t)\ge0$, $b(t)\ge0$, and no degeneracy occurs.

## Lemma

There exists $(X,Y)\in S$ such that

$$
H_1(X,Y)\ge a(t),
$$

and

$$
H_2(X,Y)\ge b(t).
$$

## Proof sketch

The map $(X,Y)\mapsto(H_1,H_2)$ sends $S$ to a strictly decreasing frontier curve from $(0,1/2)$ to $(1/2,0)$.

At $t=0$, the target point lies on the frontier. As $t$ increases, the point moves along the ray of slope

$$
m_{\mathrm{ray}}=-\frac{x+y}{y}.
$$

The frontier is strictly convex, and the ray slope is strictly more negative than the tangent slope at the base point. Therefore the ray enters the feasible region below the frontier.

This proves the existence of a dominating feasible frontier point.

## Use in CE0 + Vd1/Vd2

This lemma handles the midpoint-hole subcase where one triangle covers two holes. Its $(a,b)$-data can be replaced by a stronger feasible frontier point, after which the same $F$-chain contradiction applies.
