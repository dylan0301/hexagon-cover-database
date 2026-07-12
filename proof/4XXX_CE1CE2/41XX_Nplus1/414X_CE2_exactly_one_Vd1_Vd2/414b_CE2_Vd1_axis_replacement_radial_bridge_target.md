# CE2 Vd1 Axis-Replacement Radial Bridge Target

Status: Lemma target

This note isolates the additional radial statement needed to turn the
boundary replacement in `4147` into a full reduction to `4013`.

## Statement

Use the normalized Vd1--supercritical adjacent pair of `4147`. Let $T_i$ be
the supercritical row, let $b_i$ be its outgoing boundary reach, and let
$d_i$ be the exact CE2 center-triangle exit on the radial arm from $O$ to
$V_i$. Define the complementary vertex-role demand

$$
c_i^{\mathrm{req}}=1-d_i.
$$

The proved boundary inequality $a+b_i\le1$ makes the interval

$$
[a,1-b_i]
$$

nonempty. The required bridge statement is

$$
\boxed{
\text{There exists }p\in[a,1-b_i]
\text{ such that }
c_i^{\mathrm{req}}\le\max\{p,1-p\}.
}
$$

Equivalently,

$$
c_i^{\mathrm{req}}
\le
\max\{1-a,1-b_i,b_i\}.
$$

## Why this is sufficient

For any $p\in[a,1-b_i]$, the explicit axis-aligned unit Vd0 triangle in
`4147` has boundary reaches $(p,1-p)$. These weakly preserve the incoming
reach $a$ and outgoing reach $b_i$, and its own-radial reach is

$$
\max\{p,1-p\}.
$$

The displayed bridge inequality would therefore make it realize the full
triple

$$
(p,1-p,c_i^{\mathrm{req}}).
$$

Together with the first replacement in `4147`, this would preserve all three
affected boundary edges and both radial roles after the Vd1 adjacent support
is removed. The resulting system would satisfy the all-Vd0 nonsupercritical
input of `4013`.

For the first replacement, the reduced no-additional-support hypothesis means
that no third vertex role contributes to the old Vd1 row's own radial arm.
Its original own reach therefore already meets the center-induced demand, and
the first axis replacement preserves that reach. The unresolved bridge is on
the rescued neighboring arm described above.

## What is already proved and what is not

The exact max-$B$ argument in `4147` proves, for the old supercritical row's
actual own-radial reach $c_i$,

$$
\lambda\le c_i\le\frac12,
\qquad
b_i\le1-c_i.
$$

Hence the endpoint choice $p=1-b_i$ gives

$$
\max\{1-b_i,b_i\}\ge c_i\ge\lambda.
$$

This preserves the initial radial segment formerly assigned to $T_i$. It does
not prove $c_i\ge c_i^{\mathrm{req}}$: in the original configuration, the Vd1
rescuer can cover part of the interval between the supercritical row and the
center triangle. Removing that adjacent support is precisely the unresolved
step.

A proof must combine the Vd1 corner-side constraints from `4145` with the
exact coupled CE2 exits in `2106`, or construct a different Vd0 replacement
that reaches $c_i^{\mathrm{req}}$. Boundary coverage alone does not establish
the bridge.
