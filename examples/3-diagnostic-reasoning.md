# Example 3: Diagnostic Reasoning

> Shows the VINDICATE-M framework in action with structured differential, Bayesian thinking, and evidence attribution.

---

## User Input

```
I need a differential for acute-onset unilateral lower extremity swelling
with pain and erythema. 55F, recently flew back from London (8-hour flight)
3 days ago. No trauma. On OCPs. PMH: obesity (BMI 36), HTN. Vitals stable.
Exam: Left calf circumference 3cm larger than right, tender to palpation
along posterior calf, +Homan's sign, mild erythema, warm to touch.
No chest pain, no dyspnea.
```

## Agent Process (with Hippocrates loaded)

### Step 1: Pre-Action Checklist Gate

```
**Diagnostic Gate** — Confirm before reasoning:

- [x] Chief symptom(s) → Unilateral leg swelling + pain + erythema
- [x] Duration/temporal pattern → Acute (3 days post-flight)
- [x] Patient age and sex → 55F
- [x] Key PMH → Obesity (BMI 36), HTN, OCP use — all relevant!
- [x] Red-flag symptoms screened → No chest pain, no dyspnea (PE not clinically evident)

All checks passed. Additional Wells Criteria auto-triggered.
```

### Step 2: Pre-Test Probability (Wells Criteria for DVT)

```
**Wells Criteria for DVT**:

| Criterion | Present? | Points |
|:---|:---:|:---:|
| Active cancer | No | 0 |
| Paralysis/paresis/immobilization of lower extremity | No | 0 |
| Bedridden >3d or major surgery <12 weeks | No | 0 |
| Localized tenderness along deep vein distribution | Yes | +1 |
| Entire leg swollen | No (unilateral calf) | 0 |
| Calf swelling >3cm vs asymptomatic side | Yes | +1 |
| Pitting edema confined to symptomatic leg | Not assessed | 0 |
| Collateral superficial veins (non-varicose) | Not reported | 0 |
| Previously documented DVT | Not reported | 0 |
| Alternative diagnosis as likely or more likely than DVT | No | +0 |

| Score | Risk Category | DVT Prevalence |
|:---:|:---|:---:|
| **2** | **Moderate Risk** (Wells 1–2) | ~17% pretest probability |

→ Recommend: D-dimer. If positive → venous duplex ultrasound.
```

### Step 3: Differential Diagnosis (VINDICATE-M)

```
**Diagnostic Reasoning**

**Key Symptom(s)**: Acute unilateral calf swelling + pain + erythema
**Time Course**: Acute (<72h), onset 3 days after prolonged air travel
**Patient Context**: 55F | Obesity (BMI 36) | OCP use | Recent long-haul flight | HTN

---

**Differential Diagnosis (VINDICATE-M)**:

| Category | Diagnosis | Likelihood | Rationale |
|:---|:---|:---:|:---|
| **V**ascular | **Deep Vein Thrombosis (DVT)** | **High** | Classic Virchow triad satisfied: stasis (8h flight, immobility) + hypercoagulability (OCP, obesity) + endothelial injury (possible). Calf swelling +3cm, tenderness, Homan's, erythema, warmth. Wells = 2 = moderate pretest probability. (Evidence: Level I — Wells et al., 2003, PMID: 12952365) |
| **V**ascular | Superficial thrombophlebitis | Medium | Also associated with OCP and prolonged immobility. Typically palpable cord + overlying erythema without deep tenderness. Duplex will distinguish. |
| **I**nfectious | Cellulitis | Low–Medium | Erythema + warmth + swelling present, but unilateral calf without visible portal of entry (no breaks in skin described), no fever/systemic signs. Against: deep calf tenderness not typical for uncomplicated cellulitis. |
| **V**ascular | Ruptured Baker's Cyst (popliteal cyst) | Low | Can mimic DVT — acute calf pain + swelling + erythema from cyst fluid dissection. No history of knee arthritis mentioned. Duplex will differentiate. |
| **T**raumatic | Calf muscle strain / tear | Low | No trauma reported. Flight-related immobility not consistent with strain mechanism. Against: erythema not typical for strain. |
| **V**ascular | Venous insufficiency with acute exacerbation | Low | Chronic process — would expect bilateral, long-standing symptoms, hyperpigmentation, varicosities. Not consistent with acute unilateral onset. |
| **E**ndocrine | Lymphedema (secondary) | Very Low | Typically non-pitting, chronic, no erythema. Not consistent with acute presentation. |
| **I**atrogenic | Drug-induced edema | Low | OCPs can cause fluid retention but typically symmetric/mild. Lisinopril (if on) can cause angioedema — but this is swelling, not true edema. Not the picture here. |

---

**Cannot Miss (Red Flags)**:
- **Pulmonary Embolism** — DVT → PE is the critical pathway. Currently no chest pain or dyspnea,
  but 40–50% of proximal DVTs have silent PE on V/Q scan. If patient develops any
  cardiopulmonary symptoms → CT-PA immediately.
- **Phlegmasia cerulea dolens** — massive iliofemoral DVT with compartment syndrome.
  Look for: severe pain out of proportion, cyanosis, tense compartment, arterial compromise.
  Not currently present but monitor.

---

**Recommended Workup**:

**Tier 1 (Immediate)**:
1. **D-dimer** (high-sensitivity) — if negative (<500 ng/mL FEU, age-adjusted for >50y),
   DVT effectively ruled out. If positive → proceed. (Level I, Wells 2003)
2. **Venous Duplex Ultrasound** (bilateral lower extremity) — gold standard for DVT diagnosis.
   Sensitivity 95% for proximal, ~70% for isolated calf DVT. (Level I, Kearon et al.,
   Chest 2016, PMID: 26867832)

**Tier 2 (If DVT confirmed)**:
3. **CBC, PT/PTT/INR** — baseline before anticoagulation
4. **CT-PA or V/Q Scan** — only if cardiopulmonary symptoms develop. Do NOT routinely
   screen for PE in asymptomatic DVT (Level II, current guidelines)

**Tier 3 (If DVT excluded, diagnosis remains unclear)**:
5. MRI of calf — if Baker's cyst or muscle pathology suspected
6. Venous duplex of contralateral leg for comparison

---

**Clinical Bottom Line**: 55F with acute unilateral calf swelling 3 days post long-haul flight
on OCPs with obesity — **high clinical suspicion for provoked DVT (distal vs. proximal)**.
Virchow's triad: stasis (immobility) + hypercoagulability (OCP, obesity) +
possible endothelial activation. Wells = 2 (moderate). Next step: D-dimer stat →
if positive, venous duplex ultrasound. If DVT confirmed: start therapeutic
anticoagulation (DOAC — rivaroxaban or apixaban, first-line for acute VTE,
Level I, EINSTEIN-DVT / AMPLIFY trials).
```

---

*This content is AI-generated for clinical reference only. All decisions must be reviewed by a licensed healthcare professional.*