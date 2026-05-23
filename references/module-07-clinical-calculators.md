## Module 7: Clinical Calculators

### Pre-Action Checklist

```
**Calculator Gate** — Confirm before computing:

- [ ] Clinical scenario is clearly identified (DVT suspicion / pneumonia severity / Afib / sepsis / etc.)
- [ ] All required inputs for the relevant calculator(s) are available
- [ ] Patient demographics (age, sex, weight if applicable) are specified
- [ ] Calculator result will directly inform a clinical decision

If any unchecked → "I need [missing item(s)] before I can compute this score."
```

Auto-calculate when relevant context triggers. Output format: **Score: [X]** → **Risk: [Low/Moderate/High]** → **Action: [clinical implication]**

---

### 7.1 Wells Criteria for DVT

| Criterion | Points |
|:---|:---:|
| Active cancer (treatment within 6 mo or palliation) | +1 |
| Paralysis, paresis, or recent plaster immobilization of lower extremity | +1 |
| Recently bedridden >=3 days or major surgery within 12 weeks requiring general/regional anesthesia | +1 |
| Localized tenderness along distribution of deep venous system | +1 |
| Entire leg swollen | +1 |
| Calf swelling >3 cm compared to asymptomatic leg (measured 10 cm below tibial tuberosity) | +1 |
| Pitting edema confined to symptomatic leg | +1 |
| Collateral superficial veins (non-varicose) | +1 |
| Previously documented DVT | +1 |
| Alternative diagnosis as likely or more likely than DVT | -2 |

| Total Score | Risk | DVT Probability | Action |
|:---:|:---|:---:|:---|
| <=0 | Low | ~3% | D-dimer; if negative, DVT excluded |
| 1-2 | Moderate | ~17% | D-dimer; if positive, venous duplex US |
| >=3 | High | ~75% | Venous duplex US (skip D-dimer) |

---

### 7.2 Wells Criteria for PE

| Criterion | Points |
|:---|:---:|
| Clinical signs of DVT (minimum leg swelling + pain with palpation of deep veins) | +3 |
| PE is #1 diagnosis, or equally likely | +3 |
| Heart rate >100 bpm | +1.5 |
| Immobilization >=3 days or surgery in previous 4 weeks | +1.5 |
| Previous DVT/PE | +1.5 |
| Hemoptysis | +1 |
| Cancer (treatment within 6 mo or palliation) | +1 |

| Total Score | Risk | PE Probability | Action |
|:---:|:---|:---:|:---|
| <2 | Low | ~3.4% | PERC rule; if PERC=0, PE excluded; if PERC>=1, D-dimer |
| 2-6 | Moderate | ~20.5% | D-dimer; if positive, CT-PA |
| >6 | High | ~66.7% | CT-PA (skip D-dimer) |

---

### 7.3 PERC Rule (PE Rule-out Criteria)

Purpose: Exclude PE without D-dimer in **low pre-test probability** patients (Wells <2).

If **ALL 8 criteria are met (all "No")**, PE is excluded (probability <2%). Do NOT order D-dimer.

| Criterion | Must Be |
|:---|:---|
| Age >=50 years | No |
| Heart rate >=100 bpm | No |
| SpO2 on room air <95% | No |
| Prior history of DVT or PE | No |
| Recent surgery or trauma (within 4 weeks) | No |
| Hemoptysis | No |
| Estrogen use (OCP, HRT) | No |
| Unilateral leg swelling (clinical DVT sign) | No |

**PERC = 0**: PE excluded in low-risk patients. **PERC >=1**: Proceed to D-dimer.

---

### 7.4 CURB-65 (Pneumonia Severity)

| Criterion | Points | Details |
|:---|:---:|:---|
| **C**onfusion (AMTS <=8 or new disorientation) | +1 | Abbreviated Mental Test Score <=8 |
| **U**rea >7 mmol/L (BUN >20 mg/dL) | +1 | |
| **R**espiratory rate >=30/min | +1 | |
| **B**lood pressure: SBP <90 mmHg or DBP <=60 mmHg | +1 | |
| age >=**65** | +1 | |

| Score | Mortality | Disposition |
|:---:|:---:|:---|
| 0-1 | <3% | Outpatient management |
| 2 | ~8% | Consider short inpatient / observation |
| 3-5 | 15-40% | Inpatient; ICU if score >=4 or bilateral/multilobar involvement |

---

### 7.5 CHA2DS2-VASc (Atrial Fibrillation Stroke Risk)

| Criterion | Points |
|:---|:---:|
| **C**ongestive heart failure (or LVEF <=40%) | +1 |
| **H**ypertension (or on treatment) | +1 |
| **A**ge >=75 years | +2 |
| **D**iabetes mellitus | +1 |
| **S**troke / TIA / thromboembolism (prior) | +2 |
| **V**ascular disease (prior MI, PAD, aortic plaque) | +1 |
| **A**ge 65-74 years | +1 |
| **S**ex category: female | +1 |

| Score | Stroke Risk (%/year) | Recommendation |
|:---:|:---:|:---|
| 0 (male) / 1 (female) | ~0.2-1.3% | No antithrombotic / consider no therapy |
| 1 (male) / 2 (female) | ~2.2% | Consider OAC (shared decision) |
| >=2 (male) / >=3 (female) | >=2.2-15.2% | OAC recommended (DOAC preferred over warfarin) |

---

### 7.6 HAS-BLED (Anticoagulation Bleeding Risk)

| Criterion | Points | Details |
|:---|:---:|:---|
| **H**ypertension (SBP >160 mmHg) | +1 | Uncontrolled |
| **A**bnormal renal or liver function (1 point each max) | +1 or +2 | Renal: dialysis, transplant, Cr >=2.26 mg/dL or >=200 umol/L. Liver: cirrhosis, or bilirubin >2x ULN + ALT/AST/ALP >3x ULN |
| **S**troke (prior) | +1 | |
| **B**leeding history / predisposition | +1 | Prior major bleeding, anemia, severe thrombocytopenia |
| **L**abile INRs | +1 | TTR <60% (warfarin patients only) |
| **E**lderly (age >65 years) | +1 | |
| **D**rugs (antiplatelet, NSAID) or alcohol (>=8 drinks/week) | +1 or +2 | 1 point each for drugs or alcohol |

| Score | Bleeding Risk | Action |
|:---:|:---|:---|
| 0-1 | Low (<1.5%/year) | OAC generally safe |
| 2 | Moderate | OAC with caution; address modifiable risks |
| >=3 | High (>=3.7%/year) | OAC with close monitoring; modifiable risk factor correction; HAS-BLED >=3 is NOT a contraindication to OAC -- it identifies patients needing closer follow-up |

---

### 7.7 MELD / MELD-Na (Liver Disease Severity, 90-Day Mortality)

**MELD Score** = 3.78 x ln(serum bilirubin [mg/dL]) + 11.2 x ln(INR) + 9.57 x ln(serum creatinine [mg/dL]) + 6.43

- If bilirubin, INR, or creatinine <1.0, use 1.0 as the floor value.
- If creatinine >4.0 mg/dL, OR patient on dialysis >=2x in past week, cap creatinine at 4.0.
- Score capped at 40; rounded to nearest integer.

**MELD-Na Score** = MELD + 1.32 x (137 - Na) - 0.033 x MELD x (137 - Na)

- Na values <125 mmol/L -> set to 125; Na >137 mmol/L -> set to 137.

| MELD / MELD-Na | 90-Day Mortality | Clinical Implication |
|:---|:---:|:---|
| <10 | ~2-6% | Low priority |
| 10-19 | ~6-20% | Moderate priority |
| 20-29 | ~20-45% | High priority |
| 30-39 | ~45-75% | Very high priority |
| >=40 | >70% | Highest priority; transplant evaluation urgent |

---

### 7.8 SOFA (Sequential Organ Failure Assessment)

| Organ System | 0 | 1 | 2 | 3 | 4 |
|:---|:---|:---|:---|:---|:---|
| **Respiration** PaO2/FiO2 (mmHg) | >=400 | <400 | <300 | <200 with resp support | <100 with resp support |
| **Coagulation** Platelets (x10^3/uL) | >=150 | <150 | <100 | <50 | <20 |
| **Liver** Bilirubin (mg/dL) | <1.2 | 1.2-1.9 | 2.0-5.9 | 6.0-11.9 | >12.0 |
| **Cardiovascular** MAP / vasopressors | MAP >=70 | MAP <70 | Dop <=5 or any Dob | Dop >5 or Epi <=0.1 or NE <=0.1 | Dop >15 or Epi >0.1 or NE >0.1 |
| **CNS** Glasgow Coma Scale | 15 | 13-14 | 10-12 | 6-9 | <6 |
| **Renal** Creatinine (mg/dL) or urine output | <1.2 | 1.2-1.9 | 2.0-3.4 | 3.5-4.9 or UO <500 mL/d | >5.0 or UO <200 mL/d |

**Interpretation**: SOFA >=2 increase from baseline = organ dysfunction in sepsis. SOFA trends over time reflect treatment response; recalculate daily.

---

### 7.9 qSOFA (Quick SOFA -- Sepsis Screening)

| Criterion | Points |
|:---|:---:|
| Respiratory rate >=22/min | +1 |
| Altered mentation (GCS <15) | +1 |
| Systolic BP <=100 mmHg | +1 |

**qSOFA >=2** in setting of suspected infection -> high risk for poor outcome. Prompt escalation: evaluate for sepsis, obtain blood cultures + lactate, start empiric antibiotics within 1 hour.

---

### 7.10 Glasgow Coma Scale (GCS)

| Response | Finding | Score |
|:---|:---|:---:|
| **Eye Opening (E)** | Spontaneous | 4 |
| | To speech | 3 |
| | To pain | 2 |
| | None | 1 |
| **Verbal (V)** | Oriented | 5 |
| | Confused | 4 |
| | Words (inappropriate) | 3 |
| | Sounds (incomprehensible) | 2 |
| | None | 1 |
| **Motor (M)** | Obeys commands | 6 |
| | Localizes pain | 5 |
| | Withdraws from pain | 4 |
| | Flexion (decorticate) | 3 |
| | Extension (decerebrate) | 2 |
| | None | 1 |

| GCS Total | Severity |
|:---:|:---|
| 13-15 | Mild |
| 9-12 | Moderate |
| 3-8 | Severe (intubate if GCS <=8) |

---

### 7.11 NEXUS Low-Risk Criteria (C-Spine Imaging)

C-spine imaging can be **safely omitted** if **ALL 5** criteria are met:

| Criterion | Required |
|:---|:---|
| No posterior midline cervical-spine tenderness | Yes |
| No evidence of intoxication | Yes |
| Normal level of alertness (GCS 15) | Yes |
| No focal neurologic deficit | Yes |
| No painful distracting injury | Yes |

**NEXUS all negative -> no imaging needed.** Any "No" -> c-spine CT.

### 7.11b Canadian C-Spine Rule (Alternative)

High-risk factors that mandate imaging: **Age >=65**, **dangerous mechanism** (fall from >=1m/5 stairs, axial load, high-speed MVC, bicycle collision, motorized recreational vehicle), **paresthesias in extremities**.

Low-risk factors that allow safe ROM assessment: **simple rear-end MVC**, **sitting position in ED**, **ambulatory at any time**, **delayed onset of neck pain**, **absence of midline c-spine tenderness**.

If no high-risk factors AND >=1 low-risk factor -> assess active neck rotation (45 degrees left and right). If able to rotate -> no imaging.

---

### 7.12 Centor Criteria (Strep Pharyngitis)

| Criterion | Points |
|:---|:---:|
| Fever >38 C (100.4 F) | +1 |
| Tonsillar exudates | +1 |
| Tender anterior cervical lymphadenopathy | +1 |
| Absence of cough | +1 |
| **Age** 3-14 years | +1 |
| **Age** 15-44 years | 0 |
| **Age** >=45 years | -1 |

| Total Score | Strep Probability | Action |
|:---:|:---:|:---|
| <=0 | 1-2.5% | No testing, no antibiotics |
| 1 | 5-10% | No testing, no antibiotics |
| 2 | 11-17% | Rapid antigen test; treat if positive |
| 3 | 28-35% | Rapid antigen test OR empiric antibiotics |
| >=4 | 51-53% | Empiric antibiotics (no testing needed) |

---

### 7.13 ASCVD Risk Estimator (10-Year Atherosclerotic CVD Risk)

Uses Pooled Cohort Equations (ACC/AHA 2013). Full computation requires dedicated software. The agent should cite the AHA/ACC calculator (https://tools.acc.org/ASCVD-Risk-Estimator).

**Required Inputs**: Age, sex, race (White / African American / Other), total cholesterol (mg/dL), HDL cholesterol (mg/dL), systolic BP (mmHg), treated hypertension (Yes/No), diabetes (Yes/No), current smoker (Yes/No).

**Risk Categories & Statin Recommendations**:
| 10-Year ASCVD Risk | Category | Recommendation |
|:---|:---|:---|
| <5% | Low | Lifestyle; consider statin if risk enhancers present |
| 5-7.5% | Borderline | Consider moderate-intensity statin + risk enhancer evaluation |
| 7.5-20% | Intermediate | Moderate-to-high-intensity statin |
| >=20% | High | High-intensity statin + lifestyle |

**Risk Enhancers** (may shift decision upward): Family history premature ASCVD, LDL-C >=160, metabolic syndrome, CKD, chronic inflammatory conditions, premature menopause, pre-eclampsia, triglycerides >=175, elevated hs-CRP/Lp(a)/apoB, ankle-brachial index <0.9.

---
