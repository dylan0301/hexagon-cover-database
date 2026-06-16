# Center Type 1 Parameterization

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

The geometric domain is

$$
0\le d_\theta\le1 \qquad (\theta\in\{0,60,120,180,240,300\}).
$$

## Initial variety

$$
d_{180}d_{240}-d_{120}d_{300}=0,
$$

$$
d_0d_{120}-d_0d_{180}-d_{120}d_{300}=0,
$$

$$
(d_0+d_{240})d_{300}-d_0d_{240}=0.
$$

## Euclidean derivation of the initial variety

Normalize Type 1 so that one side of $T_C$ cuts the three rays

$$
r_{240},\qquad r_{300},\qquad r_0,
$$

and the adjacent side cuts

$$
r_{120},\qquad r_{180}.
$$

Set

$$
u=d_0,\qquad v=d_{120},\qquad x=d_{180},\qquad w=d_{240},\qquad z=d_{300}.
$$

First consider the side cutting $r_{240},r_{300},r_0$. In the $120$-degree wedge between $r_{240}$ and $r_0$, the intermediate ray $r_{300}$ splits the wedge into two $60$-degree wedges. The two triangles cut off by the side are similar, so

$$
\frac{z}{u}=\frac{w-z}{w}.
$$

Equivalently,

$$
z=\frac{uw}{u+w},
$$

which is

$$
(d_0+d_{240})d_{300}-d_0d_{240}=0.
$$

The adjacent side of the equilateral triangle is obtained from this side direction by a $60$-degree rotation. Since the ray configuration is also spaced by $60$ degrees, the same similar-triangle ratio gives

$$
\frac{x}{v}=\frac{u}{u+w}.
$$

Thus

$$
x=\frac{uv}{u+w}.
$$

Combining the two formulas gives

$$
\frac{x}{v}=\frac{z}{w},
$$

hence

$$
d_{180}d_{240}-d_{120}d_{300}=0.
$$

It also gives

$$
uv=ux+vz,
$$

which is

$$
d_0d_{120}-d_0d_{180}-d_{120}d_{300}=0.
$$

The remaining coordinate $d_{60}$ lies on the third side of $T_C$ and enters through the secondary equilateral-side constraint below.

## Rational parameterization

Set

$$
d_0=u,\qquad d_{60}=s,\qquad d_{120}=v,\qquad d_{240}=w.
$$

Then

$$
d_{180}=\frac{uv}{u+w}, \qquad d_{300}=\frac{uw}{u+w},
$$

with

$$
u+w\ne0.
$$

## Secondary constraint

The Type 1 subvariety is defined by

$$
\Delta(u,s,v,w)=0,
$$

where

$$
\Delta(u,s,v,w)=(s(u+w)+u(v+w))^2-(u^2+uw+w^2).
$$
