# Numerical Tests and Counterexamples

Status: Empirical

This file records numerical evidence and counterexamples found during the May 21/22 four-point investigation.

Numerical claims in this file are not proof. They are used only to guide the proven reductions in the other files.

## 1. Earlier four-point counterexamples

The original four-point statement without extra hypotheses is false. Near

$$
p=q=r=\frac12,
$$

the four points $P_3,P_5,G_0,G_2$ can be enclosed by an equilateral triangle of side $<1$.

A certified counterexample from the working notes is

$$
q=\frac{499}{1000}, \qquad p=r=\frac12.
$$

For this example, the four points fit inside an equilateral triangle of side

$$
\frac{8}{5\sqrt3}<1.
$$

The attempt to repair the four-point strategy by assuming that at least one $t_i$ lies outside $[1/3,2/3]$ is also false. A certified example is

$$
p=r=\frac13, \qquad q=\frac{3333}{10000}<\frac13.
$$

In that example, $t_2=t_3<1/3$, but the four points still fit inside an equilateral triangle of side

$$
\frac{25937}{15000\sqrt3}<1.
$$

These examples explain why the outside-quarter condition

$$
\exists i:\ t_i\notin\left[\frac14,\frac34\right]
$$

was investigated.

## 2. Outside-quarter lower region

In the constrained slice, the outside-quarter condition is

$$
q<\frac14 \qquad\text{or}\qquad r>\frac34.
$$

The lower region is

$$
q<\frac14.
$$

The upper region is expected to follow by the symmetry

$$
(q,p,r)\mapsto(1-r,1-p,1-q).
$$

No numerical counterexample was found in the lower outside-quarter region after applying the nonemptiness condition

$$
r^2+r(1-q)+(1-q)^2\le1.
$$

## 3. Reduced functions tested

After eliminating $p$, the numerical tests evaluated

$$
F_I(q,r)=\rho_2(r,q)+q-\tau(q,r)
$$

on Region I, and

$$
F_{II}(q,r)=r-\sigma(r)+\rho_2(\sigma(r),q)-\tau(q,r)
$$

on Region II.

With $q=sr$, the derivative targets tested were

$$
\widetilde F_{I,s},\quad \widetilde F_{I,r},\quad \widetilde F_{II,s},\quad \widetilde F_{II,r}.
$$

## 4. Dense mesh results

On the non-endpoint domain

$$
\frac1{200}\le r\le r_*:=\frac{\sqrt{37}-3}{8},
$$

quartic-root tracking found no sign failure.

Region I mesh tests gave approximately

$$
\min \widetilde F_I\approx 8.78\cdot10^{-4},
$$

$$
\min \widetilde F_{I,s}\approx 5.12\cdot10^{-3},
$$

and

$$
\min \widetilde F_{I,r}\approx 1.84\cdot10^{-1}.
$$

Region II mesh tests gave approximately

$$
\min \widetilde F_{II}\approx 8.61\cdot10^{-4},
$$

$$
\min \widetilde F_{II,s}\approx 7.37\cdot10^{-5},
$$

and

$$
\min \widetilde F_{II,r}\approx 1.78\cdot10^{-1}.
$$

The smallest values occur near the boundary

$$
r=\frac1{200},
$$

which is already handled by the Taylor theorem.

## 5. Code

The scripts under `computations/may21_patternA/` reproduce the numerical scan and provide prototype Bernstein tools.

- `pattern_a_numeric_scan.py` performs branch-filtered numerical scans.
- `endpoint_taylor_check.py` checks Taylor-polynomial lower bounds.
- `bernstein_bounds.py` contains prototype Bernstein bounding utilities.

These are aids only. They are not a complete certificate of the non-endpoint region.
