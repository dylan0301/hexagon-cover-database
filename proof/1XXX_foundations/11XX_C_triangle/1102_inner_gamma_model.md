# Center Ray-Intersection Distance Model

Status: Definition

For each direction $\theta\in\{0,60,120,180,240,300\}$, let $r_\theta$ be the ray from $O$ in direction $\theta$ degrees. Define

$$
d_\theta=\operatorname{dist}(O,\partial T_C\cap r_\theta).
$$

The center distance tuple is

$$
d(T_C)=(d_0,d_{60},d_{120},d_{180},d_{240},d_{300}).
$$

Type 1 and Type 2 are different vertex-cone arrangements for the same kind of
six-distance data. Their algebraic varieties should be compared through these
ray-intersection distances, not through special constant tuples.

The local $V_i$-triangle radial coordinate $c_i$ is measured from $V_i$ inward. Since $r_{60i}=[O,V_i]$, the remaining radial length after the center triangle is

$$
1-d_{60i},
$$

and the local propagation argument uses

$$
c_i\le 1-d_{60i}.
$$
