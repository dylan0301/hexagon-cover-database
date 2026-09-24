# Terminal nine-point enclosure

Status: Proven (exact computer-assisted tangent calculation)

## Statement

For \(0<a,b<1\), \(a+b>1\), and \(a^2+ab+b^2<1\), let
\(c_*=c_{\max}(1-b,1-a)\), \(h=\sqrt3/2\), and
\(\eta=h(1-c_*)\). With the unchanged frontier witnesses of
[31053](31053_direct_asymmetric_witness_forcing.md), put

\[
K_{\rm wit}=\mathcal D_\eta\cup\{Q_-,Q_0,Q_+\}.
\]

Then \(\Lambda(K_{\rm wit})\ge1\).

## Proof

The active complete calculation is
[3105b](3105b_explicit_comparison_enclosure.md).
When \(c_*\le2/3\), the disk alone proves the claim.
Otherwise its fixed-start Newton points satisfy
\(A\in(Q_0,Q_-)\), \(B=Q_0\), \(C\in(Q_0,Q_+)\).
Their convex hull with the actual disk is contained in
\(\operatorname{conv}(K_{\rm wit})\).
The same two frontier lines and two exposed outer tangencies give the complete
four-contact list. The line bounds are analytic. The exact explicit-comparison
verifier proves the paired tangent residuals at \(e_0\le1-c_*\), and the
radius-transfer/Gram argument gives them at the actual radius.
Every contact has support sum at least \(h\), which proves the statement.

Convexity of an open C triangle containing the original nine forced points
puts the actual disk and the three frontier points in that triangle. Compact
containment would give enclosure side less than one, so this is the terminal
contradiction used by [31058](31058_center_independent_direct_nine_point_obstruction.md).

## Historical alternative

The former junction-start construction and branchwise-radius transcript in
[31054](31054_four_cap_enclosure_reduction.md),
[31055](31055_rational_radial_envelopes_and_mixed_reduction.md), and
[31056](31056_global_analytic_mixed_positivity.md) are preserved and independently
replayed in CI. They concern their original comparison points and are not the
active certificate for the new fixed-start formulas.
