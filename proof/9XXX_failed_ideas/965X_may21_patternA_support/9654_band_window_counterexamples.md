# Band-Window Counterexamples for the Four-Point Strategy

Status: Failed

This file records exact counterexamples showing that several natural band-window repairs of the May 21/22 four-point obstruction are false.

These counterexamples concern the four-point target

$$
\Lambda(P_3,P_5,G_0,G_2)\ge1
$$

for the constrained slice

$$
p=t_0=t_1,\qquad q=t_2=t_3,\qquad r=t_4=t_5,\qquad q<r,\qquad q\le p\le r.
$$

They should not be confused with a separate local-admissible-set-only midpoint-window strategy.  What fails here is the four-point obstruction or its band-based repairs.

## 1. Counterexample inside the midpoint window $[0.4,0.6]$

Take

$$
q=\frac{499}{1000},\qquad p=r=\frac12.
$$

Then

$$
q<r, \qquad q\le p\le r,
$$

and all six edge parameters lie in the midpoint window:

$$
t_0=t_1=\frac12, \qquad t_2=t_3=\frac{499}{1000}, \qquad t_4=t_5=\frac12.
$$

In particular,

$$
t_i\in[0.4,0.6]\qquad\text{for every }i.
$$

At $V_4$,

$$
a_4=1-q=\frac{501}{1000}, \qquad b_4=r=\frac12.
$$

Thus

$$
a_4+b_4=\frac{1001}{1000}>1,
$$

and the nonemptiness condition holds:

$$
r^2+r(1-q)+(1-q)^2=\frac{751501}{1000000}<1.
$$

For the selected active $P_3,P_5$ branches, the four points fit inside an equilateral triangle of side

$$
\frac{8}{5\sqrt3}<1.
$$

Therefore

$$
\Lambda(P_3,P_5,G_0,G_2)<1.
$$

Consequently, any four-point conjecture claiming $\Lambda\ge1$ throughout the midpoint window $[0.4,0.6]$ is false.

## 2. Counterexample to the $[1/3,2/3]$ outside-band repair

A later attempted repair was to assume at least one edge point lies outside

$$
\left[\frac13,\frac23\right].
$$

This also does not rescue the four-point strategy.

Take

$$
p=r=\frac13, \qquad q=\frac{3333}{10000}<\frac13.
$$

Then

$$
t_0=t_1=\frac13, \qquad t_2=t_3=\frac{3333}{10000}, \qquad t_4=t_5=\frac13.
$$

Thus $t_2$ and $t_3$ lie outside $[1/3,2/3]$.

At $V_4$,

$$
a_4=1-q=\frac{6667}{10000}, \qquad b_4=r=\frac13,
$$

so

$$
a_4+b_4=\frac{30001}{30000}>1,
$$

and

$$
r^2+r(1-q)+(1-q)^2=\frac{700050001}{900000000}<1.
$$

For the selected active branches, the four points fit inside an equilateral triangle of side

$$
\frac{25937}{15000\sqrt3}<1.
$$

Therefore

$$
\Lambda(P_3,P_5,G_0,G_2)<1.
$$

This proves that the condition

$$
\exists i:\ t_i\notin\left[\frac13,\frac23\right]
$$

is insufficient for the four-point obstruction.

## 3. Counterexample to the $[0.4,0.6]$ outside-band repair

The same example also refutes the weaker outside-band repair using $[0.4,0.6]$.

Indeed,

$$
\frac{3333}{10000}<0.4,
$$

so $t_2,t_3\notin[0.4,0.6]$, while the same certified enclosing side length satisfies

$$
\Lambda(P_3,P_5,G_0,G_2)\le\frac{25937}{15000\sqrt3}<1.
$$

Thus the condition

$$
\exists i:\ t_i\notin[0.4,0.6]
$$

also does not rescue the four-point strategy.

## 4. Consequence for the package

The band-window ideas should not be cited as valid four-point obstructions.

The current Pattern A package therefore uses the lower outside-quarter condition

$$
q<\frac14,
$$

together with the scalar reduction and endpoint theorem recorded in this folder.

The pure midpoint-window admissible-set attack is a separate strategy about local $\mathcal A$ constraints and radial residuals.  It is not proved here for the full window $[0.4,0.6]$.
