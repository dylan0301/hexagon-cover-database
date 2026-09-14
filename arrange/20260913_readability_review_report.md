# Human-readability revision: reviewer report

## Scope and editorial decision

Base: `a98c71c12f1b521a1e58353e56b11474e1ec4f9b` on `main`.
Delivery branch: `chatgpt/human-readable-paper-20260913145427`.

This revision edits both the canonical manuscript and the immediate-proof edition. It is not another shortening pass. The goal is to make the geometric strategy understandable before the reader must follow classifications, coordinate optimizations, or exact certificates.

The principal diagnosis was a mismatch between the mathematical architecture and the reading order. The manuscript had already unified important proofs, but it often introduced a definition before explaining its purpose, or named a calculation without explaining the geometric obligation it resolves. The canonical edition also placed a detailed classification-and-routing system in the introduction; the immediate-proof edition placed the full routing table at the end and began lengthy calculations before giving a sufficiently informative overview.

The revised reading path is: prescribed points -> boundary/interior tradeoff -> geometric measurements -> precise classifications and hypotheses -> fixed witnesses -> candidate exclusion -> exhaustive assembly. The full technical proofs remain available in their existing editions.

## 1. A new opening built around the obstruction

Both editions now begin with a shared geometric overview, before the coordinate notation. It explains why total area alone does not settle the problem, why the center and six vertices force distinct triangles, why an open boundary cover needs a supercritical V triangle, and why supercriticality creates a radial-midpoint obligation.

The two principal branches are explained without requiring the reader to decode CE0/CE1/CE2, Vd0/Vd1/Vd2/T3-like, or BC/D/F first. In the zero-gap branch, multiple supercritical triangles are treated by area and a unique supercritical triangle by the nine-point enclosure. In the nonzero-gap branch, the center triangle's boundary obligation and midpoint restriction lead to the length and witness arguments.

The abstract is rewritten around the same tradeoff. It still states the point counts and the exact computer-assisted component, but no longer relies primarily on an inventory of technical method names. The introduction explicitly identifies the certificate as the final algebraic part of one enclosure argument, not a numerical search over covers.

## 2. Definitions relocated in the canonical edition

The formal center and vertex classifications, reach definitions, gap definitions, positive-support count, classification examples, and exact routing table move out of the canonical introduction into the structural section.

Their order is now tied to their use: center types before the center classification, vertex incidence before the wedge result, normalized type dictionary after the raw `(3,0)` normalization, actual reaches after that normalization, and gaps before the gap-exhaustion lemma. The exact routing table follows the midpoint structure and its associated terminology.

The raw `(3,0)` normalization is retained, including its complete calculation. A new paragraph explains why it is a trace-preserving normalization, not an enlargement of coverage. Its statement now describes the preserved sum of boundary reaches in words rather than using `A_i` and `B_i` before those symbols are introduced.

The immediate-proof edition keeps its dependency-safe calculation order and its final exact routing table. It receives the same early conceptual overview and an additional orientation paragraph at the start of common geometry. Its formal statements still have immediate proofs, with no forward proof dependencies.

## 3. The meaning of the skeleton is stated early

The original manuscript defined a skeleton cover, but a reader could miss why this weaker covering target was necessary. A shared passage now explains that a full hexagon cover implies a skeleton cover, whereas a later replacement preserves only the skeleton. This makes the stronger theorem about skeleton covers visibly necessary to the logic.

The same passage separates open triangles, which determine coverage, from closures, which are used for incidence, extrema, and upper bounds. It explicitly states that a point in a closure but outside the corresponding open triangle is not covered by that open triangle.

## 4. The boundary threshold and the budgets have visible purposes

After gap exhaustion, the paper now derives the elementary sum

`6 < sum_i (B_i + A_{i+1}) = sum_i (A_i + B_i)`

for a gap-free boundary. This motivates the supercritical threshold rather than leaving it as an unexplained definition. The explanation also preserves the distinction between strict overlap and a singleton gap at equality.

The length section is retitled **Length Budgets on the Boundary and Skeleton**. Its opening explains why open coverage requires a strictly larger sum of trace lengths than the target length, and how the local caps enter the final count. It does not assert an unrestricted center-triangle cap.

The area section now explicitly identifies the one-unit excess-area allowance. The local estimate and the cyclic step have different jobs, and the zero-gap hypothesis needed for the cyclic linkage is stated in the explanation.

## 5. Fixed witnesses and arbitrary candidates are separated

A new shared subsection introduces finite enclosure as two tasks: prove `K subset U_C` for a fixed nonempty compact witness, and prove `Lambda(K) >= 1`. It distinguishes:

- the original arrangement and its actual reach data;
- the witness set chosen from that arrangement;
- an arbitrary open enclosing candidate;
- a replacement arrangement, which is a different operation.

The candidate is required only to contain the fixed witness. It is not assumed to cover the original gaps, to complete the original skeleton cover, or to retain the original gap count. Inequalities obtained from original coverage are established before the candidate is introduced.

The text also corrects the overly broad informal description that all witness points are necessarily missed by every V triangle. A structural anchor, such as the C midpoint in the selected-gap construction, may instead be included because it already belongs to the original C triangle.

## 6. A worked explanation of the six-point construction

The selected-gap construction now includes a table identifying why each group of points belongs to the original C triangle: one structural midpoint, two actual gap endpoints, and three total radial endpoints. The prose explicitly permits coincident endpoints in a singleton gap.

The origin-hull identity is worked through as a positive-coefficient convex combination. This explains why the origin is not a seventh witness. The walkthrough then distinguishes fixed original data from the candidate's variable parameters and explains why the original tail inequality must be retained even when the candidate does not cover the other incident edge.

The headings now lead with geometric content: **A selected gap forces six points (BC)** and **A supported midpoint forces four points (D)**. The established short labels remain for source correspondence, rather than being silently renamed throughout certificates and historical proofs.

## 7. Actual radial endpoints, capacities, and the four-point ratio

A shared passage explains the difference between an actual total radial endpoint and a bound computed from selected demands. It records why the bounded point lies at least as far toward the center and why an own-ray endpoint alone may miss a neighboring triangle's contribution.

The four-point section now explains the job of the ratio hypotheses: the convex combination produces a point on the radius at distance at least one half from the origin, which forces the midpoint into the candidate. The other boundary point then demands a trace that the candidate cannot supply.

The established distinction between actual uppercase reaches and selected lowercase lower bounds remains intact. No change is made to the definition of `N_+`.

## 8. Majorants, candidates, and replacements are not interchangeable

The replacement discussion now states what changes and what survives. In the relevant unique-supercritical case, the two-chart replacement yields a skeleton cover without a supercritical V triangle, contradicting the previously established skeleton theorem. Neither the full hexagon cover nor the original gap count is claimed to survive.

The discussion also identifies the earlier translated closed-trace majorant as a different object: it is not an admissible new open role because its distinguished vertex lies on its boundary. Both replacement charts and their strict margins remain in the proof.

## 9. The zero-gap argument has three visible stages

The new zero-gap introduction separates forcing the original points, simplifying the set to be enclosed, and verifying the supporting-contact bounds. It emphasizes that exclusion from the supercritical triangle alone does not force a point into the C triangle: all other V triangles must also be excluded.

The finite set `K_F` is distinguished from the disk comparison `K_wit`. Their containment and enclosure monotonicity are displayed explicitly. The disk need not be missed by all V triangles; its containment in the C triangle comes from convexity of the six forced radial points.

The Newton points remain exact inner comparison points. They do not redefine the original frontier witnesses `Q_-`, `Q_0`, and `Q_+`. An explanatory paragraph precedes the Newton formulas, stating why moving inward preserves candidate containment and why the tangent intercept simplifies the algebra.

The exact certificate and its provenance are unchanged. A new scope paragraph distinguishes the exact residual verification from the written geometric reduction and from formal verification of the entire theorem.

## 10. Preservation and layout safeguards

The existing inline audit remains active. It accounts for 97 canonical statements, 83 immediate-proof statements, 14 declared consolidations, and 81 retained canonical proof bodies.

A new independent readability-preservation audit compares both editions with a baseline inventory taken from the original commit. It checks all 97 canonical statements and 96 canonical proof environments, all 83 inline statements and proof environments, and an aggregate fingerprint of 365 proof/certificate files. Only two exact nonmathematical statement rephrasings are normalized: the location of the vertex dictionary and the normalization consequence's deferred reach symbols. Every original proof environment is retained.

Two existing source checks require maintenance because of the editorial relocation. The routing-table check reads its new structural-section location without relaxing the one-row condition. The normalization fingerprint check reverses the one declared wording substitution before testing its original hash; it does not exempt the normalization calculation from verification.

New reader headings use explicit bold run-in formatting with spacing. Table text and mathematical typography remain in the manuscript's established style. The immediate-proof edition's page-break protection is strengthened so that a final displayed equation cannot leave the proof heading alone on the following page. The render audit checks this property.

No existing geometric figure is removed or redrawn. The new aids are explanatory text, two reader tables, visible headings, and displayed logical relations; no sampled geometry is promoted to proof evidence.

## Validation and scope of the claim

The release pipeline runs the repository source checks, the inline-order and preservation audit, the new baseline audit, both exact zero-gap programs, dependency-graph regeneration and validation, trace-asset checks, interactive audits, pinned TeX Live 2025 builds, PDF render checks, and whitespace checks. The final pinned-build results are recorded below by the release job only after these checks succeed.

The pre-review PDFs had 69 and 64 pages. The reviewed local builds have 75 and 73 pages. This increase is intentional: explanations and proof-start protection take precedence over a shortening target. The final pinned counts are authoritative. The canonical page-count guard is adjusted to the new edition, not used as a reason to remove explanations.

This is an editorial revision with mathematical-content preservation checks. It is not a claim that a proof assistant has verified the full theorem, nor a fresh independent proof of every inherited local lemma. The CE1 return and zero-gap optimization remain technically demanding. The revision makes their purposes, inputs, and relationship to the main proof more explicit without suppressing those calculations.


## Pinned publication results

Validated by GitHub Actions run 34765602787 using Python 3.12 and the repository-pinned TeX Live 2025 image.

Both source audits, the independent baseline-preservation audit, both exact zero-gap programs, dependency-graph regeneration, trace-asset checks, interactive checks, whitespace checks, both manuscript builds, all-page render scans, and the inline proof-start audit passed before publication.

Pinned page counts: canonical **75**; immediate-proof edition **73**.

`arrange/paper_draft/main.pdf`: SHA-256 `1bb9696c0ae45c4a3a4cc422d0005ef788c5ee8c31a1e5093646432cb7eaeb73`.

`arrange/paper_draft/inline_proofs/main.pdf`: SHA-256 `9e587fab5776e7a715a6ce354f4185de9f7dad254b3082ba5907a982d68fa58f`.
