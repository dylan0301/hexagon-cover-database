# Piecewise Formula for $c(a,b)$

Status: Computational formula

Let

$$
s=a+b,
\qquad
m=\min(a,b),
\qquad
M=\max(a,b),
$$

and

$$
q=(a+b)^4-(a+b)^2+ab.
$$

If

$$
a^2+ab+b^2>1,
$$

then $c(a,b)$ is undefined.

If $s>1$, then

$$
c=\frac{M(2mM+1)-\sqrt{M^2((2mM+1)^2-4(1-m^2)(1-M^2))}}{2(1-m^2)}.
$$

If $s=1$, then

$$
c=M.
$$

If $s<1$ and $q\ge0$, then

$$
c=\frac{2M}{1+\sqrt{4s^2-3}}.
$$

If $s<1$ and $q<0$, then $c$ is the unique root in $(0,1]$ of

$$
c^4-c^2+mc-m^2=0.
$$

This is a computational boundary formula. Branch completeness and uniqueness are separate proof obligations.
