# Inner / Outer Gamma Separation Postmortem

Status: Failed / partial

Inner gamma is the set of six-tuples realized by center triangles.

Outer gamma is the set of six-tuples produced by vertex triangles under edge splits such as

\[
a_i+b_{i+1}=1.
\]

Both are semialgebraic subsets of \(\mathbb R^6\).

The failed goal was to find a separating hyperplane or higher-degree separating hypersurface.

A kite tuple has form

\[
(x,y,0,z,0,y).
\]

If it is coverable by a triangle, then

\[
z\le\frac{\sqrt{x^2+y^2-xy}}{x}-x.
\]

This proves exclusions for some Type \(211111\) examples, but Type \(211311\)-like examples survive.

Warning: if all \(a_i\) are equal, the type assignment collapses to all Type 1, so the kite argument does not apply.
