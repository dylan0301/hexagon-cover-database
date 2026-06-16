# Inner / Outer Gamma Set Separation Postmortem

Status: Failed

The inner gamma set is the set of center-triangle distance tuples $d_0,d_{60},\dots,d_{300}$.

The outer gamma set is the set of vertex-triangle radial tuples $c_0,\dots,c_5$ produced under edge splits such as

$$
b_i+a_{i+1}=1.
$$

Both are semialgebraic subsets of $\mathbb R^6$.

The failed goal was to find a separating hyperplane or higher-degree separating hypersurface.

A kite tuple has form

$$
(x,y,0,z,0,y).
$$

If it is coverable by a triangle, then

$$
z\le\frac{\sqrt{x^2+y^2-xy}}{x}-x.
$$

This proves exclusions for some Type $211111$ examples, but Type $211311$-like examples survive.

Warning: if all $a_i$ are equal, the type assignment collapses to all Type 1, so the kite argument does not apply.
