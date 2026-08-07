import Mathlib

/-!
# Strategy 2 optimization problem statements

This file intentionally contains only the real-variable problem specifications
for Strategy 2.  Every theorem is closed with `sorry`; no geometric bridge and
no optimization proof is formalized here.
-/

noncomputable section

namespace HexagonCover.Strategy2Optimization

classical

open Real

structure SignedInput where
  r : ℝ
  a : ℝ
  d : ℝ

def w (s : SignedInput) : ℝ := 1 - s.r
def e (s : SignedInput) : ℝ := Real.sqrt (1 - s.r * w s)
def eta (s : SignedInput) : ℝ := 1 - e s
def p (s : SignedInput) : ℝ := e s * (1 - e s)
def k (s : SignedInput) : ℝ := eta s + s.a + s.d
def deltaR (s : SignedInput) : ℝ := p s - s.a - w s * s.d
def deltaL (s : SignedInput) : ℝ := p s - s.r * s.a - s.d

def signedDomain (s : SignedInput) : Prop :=
  0 < s.r ∧ s.r < 1 ∧ 0 < s.a ∧ 0 < s.d ∧ 0 < deltaR s

def centerCE1Domain (s : SignedInput) : Prop :=
  signedDomain s ∧ deltaL s ≤ 0

def centerCE2Domain (s : SignedInput) : Prop :=
  signedDomain s ∧ 0 < deltaL s

def oneGapCE1Domain (s : SignedInput) : Prop :=
  centerCE1Domain s ∧
    s.a < w s / 2 ∧
    s.d < s.r / 2 ∧
    w s * s.a < s.r * s.d

def lowRoot (c : ℝ) : ℝ :=
  c / 2 * (1 - Real.sqrt (4 * c^2 - 3))

def upperRoot (c : ℝ) : ℝ := c - lowRoot c

def transition (c : ℝ) : ℝ :=
  2 * c / (1 + Real.sqrt (16 * c^2 - 3))

def qMinus (c x : ℝ) : ℝ :=
  Real.sqrt (x^2 - c * x + c^2) / c - x

def discrPlus (c x : ℝ) : ℝ :=
  (2 * x * c^2 + c)^2 - 4 * (1 - c^2) * (1 - x^2) * c^2

def qPlus (c x : ℝ) : ℝ :=
  2 * (1 - x^2) * c^2 /
    (2 * x * c^2 + c + Real.sqrt (discrPlus c x))

def cappedOutput (c x : ℝ) : ℝ :=
  if c ≤ Real.sqrt 3 / 2 then
    if x ≤ 1 - c then 1 - x
    else if x < transition c then qPlus c x
    else if x = transition c then transition c
    else if x < c then qMinus c x
    else 1 - x
  else
    if x ≤ 1 - c then 1 - x
    else if x ≤ lowRoot c then qPlus c x
    else if x < upperRoot c then lowRoot c
    else if x < c then qMinus c x
    else 1 - x

def update (c x : ℝ) : ℝ := 1 - cappedOutput c x

/-! ## S2-E1 and S2-E2 -/

def e1Objective (s : SignedInput) : ℝ :=
  cappedOutput (1 - s.a / w s) (k s / s.r) +
    cappedOutput (1 - s.d / s.r) (s.r - s.d) - 1

theorem problemS2E1
    (s : SignedInput)
    (hs : oneGapCE1Domain s ∨ centerCE2Domain s) :
    e1Objective s < 0 := by
  sorry

def e2Objective (s : SignedInput) : ℝ :=
  cappedOutput ((w s - s.a) / w s) (w s - s.a) +
    cappedOutput ((s.r - s.d) / s.r) (s.r - s.d) - 1

theorem problemS2E2
    (s : SignedInput)
    (hs : centerCE2Domain s) :
    e2Objective s < 0 := by
  sorry

/-! ## S2-R1 and S2-R2 -/

def middleDefect (s : SignedInput) : ℝ :=
  min (s.a / s.r) (s.d / w s)

def y0 (s : SignedInput) : ℝ := k s / (2 * s.r)
def y1 (s : SignedInput) : ℝ := update (1 - s.a) (y0 s)
def y2 (s : SignedInput) : ℝ := update (1 - middleDefect s) (y1 s)
def y3 (s : SignedInput) : ℝ := update (1 - s.d) (y2 s)
def returnObjective (s : SignedInput) : ℝ := w s + s.d - y3 s

theorem problemS2R1
    (s : SignedInput)
    (hs : oneGapCE1Domain s) :
    returnObjective s < 0 := by
  sorry

theorem problemS2R2
    (s : SignedInput)
    (hs : centerCE2Domain s) :
    returnObjective s < 0 := by
  sorry

/-! ## S2-T3 -/

structure T3Input where
  center : SignedInput
  tau : ℝ
  beta : ℝ

def t3z (x : T3Input) : ℝ :=
  Real.sqrt (1 - x.tau + x.tau^2)

def t3q (x : T3Input) : ℝ := 1 - t3z x + x.beta
def t3CStar (x : T3Input) : ℝ := t3q x / x.tau
def t3UStar (x : T3Input) : ℝ := 1 + x.beta - x.tau
def t3BPlus (x : T3Input) : ℝ := t3z x - x.beta

def t3A1 (x : T3Input) : ℝ :=
  let sR := k x.center / x.center.r
  let tR := w x.center + x.center.d
  if t3BPlus x < sR then t3q x
  else if t3BPlus x < tR then x.center.r - x.center.d
  else t3q x

def t3A5 (x : T3Input) : ℝ :=
  if centerCE2Domain x.center then
    let sL := k x.center / w x.center
    let tL := x.center.r + x.center.a
    if x.beta < sL then 1 - x.beta
    else if x.beta < tL then 1 - tL
    else 1 - x.beta
  else
    1 - x.beta

def t3C1 (x : T3Input) : ℝ :=
  let gamma1 := x.center.d / x.center.r
  if 1 - t3UStar x ≤ gamma1 ∧ gamma1 ≤ 1 - t3CStar x then
    t3CStar x
  else
    1 - gamma1

def t3C5 (x : T3Input) : ℝ :=
  1 - x.center.a / w x.center

def t3Domain (x : T3Input) : Prop :=
  (centerCE1Domain x.center ∨ centerCE2Domain x.center) ∧
    0 < x.tau ∧ x.tau < 1 ∧
    0 < x.beta ∧
    x.beta < x.tau * t3z x / (1 + t3z x) ∧
    0 < t3q x ∧ t3q x < 1 / 2 ∧
    0 < t3CStar x ∧ t3CStar x < t3UStar x ∧ t3UStar x < 1 ∧
    1 / 2 < t3C1 x ∧ t3C1 x < 1 ∧
    1 / 2 < t3C5 x ∧ t3C5 x < 1

def t3Objective (x : T3Input) : ℝ :=
  cappedOutput (t3C5 x) (t3A5 x) +
    cappedOutput (t3C1 x) (t3A1 x) - 1

theorem problemS2T3
    (x : T3Input)
    (hx : t3Domain x) :
    t3Objective x < 0 := by
  sorry

/-! ## S2-SC -/

def supercriticalEnvelope (c : ℝ) : ℝ :=
  (c + Real.sqrt (c^2 - 8 * c + 4)) / 2

def rescuerObjective (a c u : ℝ) : ℝ :=
  max a (a / (a + 1 - u)) + supercriticalEnvelope c - 1

structure RescuerTInput where
  theta : ℝ
  x : ℝ

def rescuerTRho (v : RescuerTInput) : ℝ :=
  (1 - 2 * v.theta) / (1 - v.theta^2)

def rescuerTLower (v : RescuerTInput) : ℝ :=
  (1 - 4 * v.theta + v.theta^2) / (2 * (1 - 2 * v.theta))

def rescuerTA (v : RescuerTInput) : ℝ := v.x * rescuerTRho v
def rescuerTC (v : RescuerTInput) : ℝ := v.x + v.theta
def rescuerTU (v : RescuerTInput) : ℝ :=
  1 - rescuerTRho v + rescuerTA v

def rescuerTDomain (v : RescuerTInput) : Prop :=
  0 ≤ v.theta ∧ v.theta ≤ 2 - Real.sqrt 3 ∧
    rescuerTLower v ≤ v.x ∧ v.x ≤ 1 / 2 - v.theta ∧
    0 < rescuerTA v ∧
    0 ≤ rescuerTC v ∧ rescuerTC v ≤ 1 / 2 ∧
    1 / 2 ≤ rescuerTU v ∧ rescuerTU v < 1

theorem problemS2SCT
    (v : RescuerTInput)
    (hv : rescuerTDomain v) :
    rescuerObjective (rescuerTA v) (rescuerTC v) (rescuerTU v) ≤ 0 := by
  sorry

structure RescuerVInput where
  t : ℝ
  a : ℝ
  b : ℝ

def cornerDelta (t : ℝ) : ℝ := Real.sqrt (t^2 + t + 1)
def rescuerVC (v : RescuerVInput) : ℝ :=
  v.t * (1 - v.b) / (v.t + 1)
def rescuerVU (v : RescuerVInput) : ℝ :=
  (cornerDelta v.t - v.a - v.t * v.b - 1) / v.t

def rescuerVDomain (v : RescuerVInput) : Prop :=
  1 ≤ v.t ∧
    0 < v.a ∧ v.a < 1 ∧
    0 < v.b ∧ v.b < 1 ∧
    0 ≤ rescuerVC v ∧ rescuerVC v ≤ 1 / 2 ∧
    rescuerVC v < rescuerVU v ∧ rescuerVU v < 1 ∧
    v.a + v.t * v.b ≤ cornerDelta v.t - 1 - v.t / 2 ∧
    cornerDelta v.t - v.a - v.t * v.b - v.t ≤ (1 - v.a) / (v.t + 1)

theorem problemS2SCV
    (v : RescuerVInput)
    (hv : rescuerVDomain v) :
    rescuerObjective v.a (rescuerVC v) (rescuerVU v) ≤ 0 := by
  sorry

/-! ## S2-VD -/

def componentEnd (L U x : ℝ) : ℝ :=
  if x < L then x else if x ≤ U then U else x

def residual (L U x : ℝ) : ℝ := 1 - componentEnd L U x

structure VdAdjacentInput where
  center : SignedInput
  p0 : ℝ
  q0 : ℝ
  t : ℝ
  p1 : ℝ
  q1 : ℝ

def vdAdjA (v : VdAdjacentInput) : ℝ :=
  residual (k v.center / v.center.r) (w v.center + v.center.d) v.q0

def vdAdjH (v : VdAdjacentInput) : ℝ :=
  residual (k v.center / w v.center) (v.center.r + v.center.a) v.p0

def vdAdjLambda (v : VdAdjacentInput) : ℝ :=
  v.t * (1 - v.q1) / (v.t + 1)

def vdAdjU (v : VdAdjacentInput) : ℝ :=
  (cornerDelta v.t - v.p1 - v.t * v.q1 - 1) / v.t

def vdAdjBaseDomain (v : VdAdjacentInput) : Prop :=
  centerCE2Domain v.center ∧
    0 < v.p0 ∧ v.p0 < 1 ∧
    0 < v.q0 ∧ v.q0 < 1 ∧
    1 < v.p0 + v.q0 ∧
    v.p0^2 + v.p0 * v.q0 + v.q0^2 ≤ 1 ∧
    0 < vdAdjH v ∧ 0 ≤ vdAdjA v ∧ vdAdjA v + vdAdjH v < 1 / 2 ∧
    v.center.a + v.center.d < 1 / 24 ∧
    v.center.a + v.center.d < min v.center.r (w v.center) / 6 ∧
    0 < v.t ∧
    0 < v.p1 ∧ v.p1 < 1 ∧
    0 < v.q1 ∧ v.q1 < 1 ∧
    vdAdjA v ≤ v.p1 ∧ vdAdjH v ≤ v.q1 ∧
    v.p1 + v.q1 < 1 / 2

def vdAdjSupportDomain (v : VdAdjacentInput) : Prop :=
  vdAdjBaseDomain v ∧
    0 ≤ vdAdjLambda v ∧ vdAdjLambda v < vdAdjU v ∧ vdAdjU v ≤ 1

def vdAdjNoSupportDomain (v : VdAdjacentInput) : Prop :=
  vdAdjBaseDomain v ∧ vdAdjU v ≤ vdAdjLambda v

def vdAdjSupportObjective (v : VdAdjacentInput) : ℝ :=
  max (v.center.d - vdAdjH v / 4) (vdAdjU v - 1 + v.center.d)

def vdAdjNoSupportObjective (v : VdAdjacentInput) : ℝ :=
  v.center.d - vdAdjH v / 4

theorem problemS2VDAdjacentSupport
    (v : VdAdjacentInput)
    (hv : vdAdjSupportDomain v) :
    vdAdjSupportObjective v < 0 := by
  sorry

theorem problemS2VDAdjacentNoSupport
    (v : VdAdjacentInput)
    (hv : vdAdjNoSupportDomain v) :
    vdAdjNoSupportObjective v < 0 := by
  sorry

structure VdNonadjacentInput where
  center : SignedInput
  p0 : ℝ
  q0 : ℝ
  t : ℝ
  pv : ℝ
  qv : ℝ
  index : ℕ

def vdNonA (v : VdNonadjacentInput) : ℝ :=
  residual (k v.center / v.center.r) (w v.center + v.center.d) v.q0

def vdNonH (v : VdNonadjacentInput) : ℝ :=
  residual (k v.center / w v.center) (v.center.r + v.center.a) v.p0

def vdNonC (v : VdNonadjacentInput) : ℝ :=
  (cornerDelta v.t - v.pv - v.t * v.qv) / (v.t + 1)

def vdNonExit (v : VdNonadjacentInput) : ℝ :=
  if v.index = 2 then v.center.d
  else if v.index = 3 then min (v.center.a / v.center.r) (v.center.d / w v.center)
  else v.center.a

def vdNonDomain (v : VdNonadjacentInput) : Prop :=
  centerCE2Domain v.center ∧
    (v.index = 2 ∨ v.index = 3 ∨ v.index = 4) ∧
    0 < v.p0 ∧ v.p0 < 1 ∧
    0 < v.q0 ∧ v.q0 < 1 ∧
    1 < v.p0 + v.q0 ∧
    v.p0^2 + v.p0 * v.q0 + v.q0^2 ≤ 1 ∧
    0 < vdNonA v ∧ 0 < vdNonH v ∧ vdNonA v + vdNonH v < 1 / 2 ∧
    v.center.a + v.center.d < (k v.center / w v.center) / 2 ∧
    v.center.a + v.center.d < (k v.center / v.center.r) / 2 ∧
    0 < v.t ∧
    0 < v.pv ∧ v.pv < 1 ∧
    0 < v.qv ∧ v.qv < 1 ∧
    vdNonA v ≤ v.pv ∧ vdNonH v ≤ v.qv ∧
    0 ≤ vdNonC v ∧ vdNonC v ≤ 1

def vdNonObjective (v : VdNonadjacentInput) : ℝ :=
  let sigma := v.center.a + v.center.d
  let m := min (vdNonA v) (vdNonH v)
  max (max (sigma - vdNonA v) (sigma - vdNonH v))
    (max (vdNonExit v - m) (vdNonC v - 1 + m))

theorem problemS2VDNonadjacent
    (v : VdNonadjacentInput)
    (hv : vdNonDomain v) :
    vdNonObjective v < 0 := by
  sorry

end HexagonCover.Strategy2Optimization
