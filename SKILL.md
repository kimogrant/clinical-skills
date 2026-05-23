# Hippocrates — Full-Stack Clinical Assistant Skill

> **AI Agent Clinical Skills Suite** · Covering 7 clinical domains: Documentation, Diagnosis, Prescribing, Labs, Communication, EBM, Clinical Calculators
> Compatible with Claude Code · Codex · Cursor · OpenCode · Gemini CLI
> Sibling skill: [Allergos](https://github.com/kimogrant/allergos) (allergy & immunology)

---

## Metadata

```yaml
name: hippocrates
version: 1.1.0
author: kimogrant
description: A comprehensive clinical assistant skill for AI coding agents, covering clinical documentation, diagnostic reasoning, prescription review, lab interpretation, patient communication, evidence-based medicine, and clinical calculators. Features mandatory pre-action checklists (superpowers-style) to prevent hallucination on incomplete data.
tags: [medical, clinical, healthcare, diagnosis, prescription, evidence-based-medicine, EBM]
platforms: [claude-code, codex, cursor, opencode, gemini-cli]
language: [en]
```

---

## Trigger Conditions

Activate when **any** keyword matches:
- Clinical documentation: SOAP note, H&P, progress note, discharge summary, operative note
- Diagnosis: differential diagnosis, diagnostic reasoning, symptom analysis, VINDICATE
- Prescribing: medication review, drug interactions, dosing, contraindications, polypharmacy
- Labs & imaging: lab results, CBC, BMP, LFT, imaging report, CXR, CT, MRI interpretation
- Communication: breaking bad news, SPIKES protocol, informed consent, patient education
- Evidence: literature search, PICO, guideline query, systematic review, UpToDate, PubMed
- Patient / case / clinical / rounds / consult

---

## Core Behavioral Rules

Before executing **any** clinical task:

1. **Safety Disclaimer**: Prepend AND append every clinical output with: *"This content is AI-generated for clinical reference only. All decisions must be reviewed by a licensed healthcare professional. This does not constitute medical advice."*
2. **Honesty Under Uncertainty**: If info is insufficient, explicitly list missing data points. **Never fabricate or guess.**
3. **Evidence-First**: Every clinical claim must carry evidence level (I–V) and source (PMID / guideline).
4. **Privacy by Default**: Auto-redact: full name → `[Patient]`, DOB → `[Age only]`, MRN/SSN/NHS → `[Redacted]`, address/phone → `[Redacted]`.
5. **Standardized Terminology**: ICD-11 for diagnoses, RxNorm for medications, LOINC for labs, SNOMED CT for clinical findings.

---

## Pre-Action Checklist Protocol

> This is the **superpowers-style guardrail** — the agent MUST run the checklist BEFORE any module output. If any item is unchecked, **halt and prompt the user** for the missing information. Do not proceed with incomplete data. This is not a suggestion; it is a required gate.

Each module defines its own checklist. The agent must:
1. Display the checklist to the user
2. Mark each item ✅ or ❌ based on what the user has provided
3. If any ❌ remains, output: *"I need the following before I can proceed:"* and list only the unchecked items
4. Only after all items are ✅, generate the full module output

---

## Module 1: Clinical Documentation

### Pre-Action Checklist

```
**Documentation Gate** — Confirm before writing:

- [ ] Patient age and gender are specified
- [ ] Chief complaint is clearly stated (symptom + duration)
- [ ] Setting is specified (outpatient vs. inpatient vs. ED)
- [ ] Document type is specified (SOAP / H&P / progress / discharge / operative)
- [ ] Key HPI elements: onset, location, quality, modifying factors (at least 3 of 4 present)

If any unchecked → "I need [missing item(s)] before I can write the note."
```

### 1.1 SOAP Note (Outpatient)

**Trigger**: "SOAP note", "outpatient note", "clinic note", "write SOAP"

```
**SOAP Note**

**Date**: YYYY-MM-DD
**Provider**: [Name]
**Chief Complaint**: "[Symptom] × [duration]" (≤10 words, extracted not verbatim)

---

**Subjective**:

**HPI** (OLDCARTS):
- Onset: [timing / precipitating factors / acuity]
- Location: [site]
- Duration: [time since onset, pattern]
- Character: [quality / severity 0–10 / timing]
- Aggravating/Alleviating: [factors]
- Radiation: [if applicable]
- Timing: [constant / intermittent / diurnal]
- Severity: [0–10 scale / functional impact]
- Associated symptoms: [list all]
- Context: [relevant PMH / recent exposures / travel]
- Prior workup: [relevant tests / treatments and response]

**PMH**: [chronic conditions / surgeries / hospitalizations]
**Allergies**: [drug / food / environmental + reaction type]
**Medications**: [name (generic) + dose + frequency + adherence]
**Family History**: [1st-degree relatives, heritable conditions]
**Social History**: [tobacco / alcohol (quantify) / substance use / occupation]

---

**Objective**:

**Vitals**: T [°F/°C] | HR [bpm] | RR [/min] | BP [mmHg] | SpO2 [%] | BMI [kg/m²]
**Physical Exam**:
- Positive findings: [by system, detailed]
- Pertinent negatives: [absent findings that narrow differential]

---

**Assessment**:

**Primary Diagnosis**: [diagnosis] (ICD-11: [code])
**Differential Diagnoses**:
1. [DDx 1] — likelihood [high/med/low], key distinguishing feature: [feature]
2. [DDx 2] — likelihood [high/med/low], key distinguishing feature: [feature]

**Clinical Reasoning**: [2–3 sentence synthesis]

---

**Plan**:
- **Diagnostics**: [tests + urgency]
- **Therapeutics**: [Drug] [dose] [route] [frequency] [duration] — [rationale]
- **Patient Education**: [key points]
- **Follow-up**: [when / with whom / return precautions]
```

### 1.2 H&P (Admission) Template

**Trigger**: "H&P", "admission note", "history and physical", "admit note"

```
**History & Physical (Admission Note)**

**Admitting Service**: [Service]
**Date/Time of Admission**: YYYY-MM-DD HH:MM
**Chief Complaint**: "[Symptom] × [duration]"

---

**History of Present Illness** (OLDCARTS as above, but more detailed narrative, including prior treatments and their response)

**Past Medical History**:
- Chronic conditions: [list with duration]
- Hospitalizations: [reason, year, outcome]

**Past Surgical History**:
- Surgeries: [procedure, year, complications]

**Allergies**: [drug/food/environmental] → [reaction type]
**Medications**: [name (generic) + dose + route + frequency + adherence]
**Family History**: [1st-degree relatives, heritable conditions, age at diagnosis]
**Social History**: [tobacco (pack-years), alcohol (drinks/week), substance use, occupation, living situation, support system]

**Review of Systems** (14-system):
- Constitutional: [fever, chills, weight change, fatigue]
- HEENT: [headache, vision, hearing, nasal, throat]
- Cardiovascular: [chest pain, palpitations, edema, orthopnea]
- Respiratory: [cough, dyspnea, wheezing, hemoptysis]
- GI: [nausea, vomiting, abdominal pain, bowel habits, hematochezia/melena]
- GU: [dysuria, frequency, hematuria, incontinence]
- Musculoskeletal: [joint pain, swelling, stiffness, weakness]
- Neurological: [headache, dizziness, syncope, seizures, focal deficits]
- Psychiatric: [mood, anxiety, sleep, suicidal ideation]
- Endocrine: [polyuria/polydipsia, heat/cold intolerance]
- Hematologic/Lymphatic: [easy bruising/bleeding, lymphadenopathy]
- Dermatologic: [rash, lesions, pruritus]
- Allergic/Immunologic: [as above]
- Female/Male Reproductive: [menstrual history, sexual activity, contraception]

---

**Physical Exam**:

**Vitals**: T [°F/°C] | HR [bpm] | RR [/min] | BP [mmHg] | SpO2 [%] on [RA/O2] | BMI [kg/m²]
**General**: [appearance, distress, mental status]
**HEENT**: [head, eyes, ears, nose, throat]
**Neck**: [JVD, lymph nodes, thyroid]
**Cardiovascular**: [heart sounds, murmurs, rubs, pulses]
**Pulmonary**: [breath sounds, crackles, wheezes, egophony]
**Abdomen**: [bowel sounds, tenderness, organomegaly, masses]
**Extremities**: [edema, pulses, cyanosis, clubbing]
**Neurological**: [cranial nerves, motor, sensory, reflexes, coordination, gait]
**Skin**: [rashes, lesions, turgor]

---

**Labs & Imaging** (available at admission):
- [Test]: [result] [unit] (reference range)
- [Imaging]: [findings]

---

**Assessment & Plan**:

**Problem List** (ranked by acuity):
1. **[Primary problem]** — [brief description]
   - Assessment: [differential diagnosis, likelihood]
   - Plan: [diagnostics, therapeutics, monitoring]
2. **[Secondary problem]** — [brief description]
   - Assessment: [differential diagnosis, likelihood]
   - Plan: [diagnostics, therapeutics, monitoring]
3. **[Chronic condition management]** — [brief description]
   - Plan: [continue/optimize current regimen]

**Disposition**: Admit to [service], [level of care]
**Code Status**: [Full / DNR / DNI / etc.]
**Prophylaxis**: [VTE prophylaxis, stress ulcer prophylaxis, etc.]
**Diet**: [NPO / clear liquids / regular / etc.]
**Activity**: [bed rest / ambulate ad lib / etc.]
**Follow-up**: [consultations needed]
```

### 1.3 Discharge Summary Template

**Trigger**: "discharge summary", "DC summary", "discharge note"

```
**Discharge Summary**

**Admission Date**: YYYY-MM-DD
**Discharge Date**: YYYY-MM-DD
**Admitting Service**: [Service]
**Discharging Service**: [Service]
**Admitting Diagnosis**: [diagnosis]
**Discharge Diagnosis**: [diagnosis] (ICD-11: [code])

---

**History of Present Illness**: [brief 2–3 sentence summary of admission reason]

**Hospital Course**:
- Day 1: [events, interventions, response]
- Day 2: [events, interventions, response]
- ...
- Day N: [events leading to discharge]

**Procedures Performed**:
- [Procedure name] (CPT: [code]) on YYYY-MM-DD — [indication, findings, complications]

**Discharge Medications**:

| Medication | Dose | Route | Frequency | Duration/Indication | Notes |
|:---|:---|:---|:---|:---|:---|
| [Drug] | [dose] | PO/IV/SC/... | [frequency] | [duration] for [indication] | [taper instructions, monitoring] |
| ... | ... | ... | ... | ... | ... |

**Discharge Disposition**: [Home / SNF / Rehab / Hospice] with [home health / family support]
**Follow-up Arrangements**:
- [Specialty]: [clinic name], [date/time]
- [PCP]: [clinic name], [date/time]
- [Other]: [details]

**Discharge Instructions**:
- Activity: [restrictions, gradual return]
- Diet: [restrictions]
- Wound care: [if applicable]
- Red-flag symptoms to return to ED: [list]
- Medication reconciliation: confirm patient understands new regimen

**Pending Results**: [labs/imaging pending, who will follow up]
**Patient Education Provided**: [topics covered]
**Code Status at Discharge**: [Full / DNR / DNI / etc.]
```

### 1.4 Progress Note
**Template (SOAP format for daily progress):**
```
Date/Time:
Subjective: Patient reports [symptoms, concerns, response to treatment].
Objective: Vital signs [T, HR, RR, BP, O2 sat], physical exam findings, lab results.
Assessment: Clinical impression, problem list update, differential diagnosis.
Plan: Medications, tests, consults, patient education, follow-up.
```

### 1.5 Operative Note
**Template (standardized operative report):**
```
Preoperative Diagnosis:
Postoperative Diagnosis:
Procedure(s) Performed:
Surgeon(s):
Assistant(s):
Anesthesia: [type, duration, complications]
Indications: [reason for surgery]
Findings: [intraoperative observations, pathology encountered]
Description of Procedure: [step-by-step narrative]
Estimated Blood Loss:
Specimens Sent: [to pathology, microbiology]
Complications: [intraoperative or immediate postoperative]
Condition: [stable, critical, etc.]
Disposition: [PACU, ICU, floor]
```

---

## Module 2: Diagnostic Reasoning

### Pre-Action Checklist

```
**Diagnostic Gate** — Confirm before reasoning:

- [ ] Chief symptom(s) are specified
- [ ] Duration/temporal pattern is known (acute <48h / subacute 2d–4w / chronic >4w)
- [ ] Patient age and sex are specified
- [ ] Key PMH that could influence the differential is provided
- [ ] Any red-flag symptoms have been explicitly screened

If any unchecked → "I need [missing item(s)] before I can build a differential."
```

### 2.1 Structured Differential

```
**Diagnostic Reasoning**

**Key Symptom(s)**: [1–2 most salient]
**Time Course**: [acute / subacute / chronic]
**Patient Context**: [age / sex / key PMH / risk factors]

---

**Differential Diagnosis**:

| Likelihood | Diagnosis | Supporting | Against | Rule-In/Out Test | Pre-test Prob |
|:---:|:---|:---|:---|:---|:---:|
| High | [Dx] | [≥3] | [absent features] | [gold standard] | [%] |
| Medium | [Dx] | [features] | [against] | [test] | [%] |
| Low | [Dx] | [features] | [against] | [test] | [%] |

**Cannot Miss (Red Flags)**: [diagnoses catastrophic to miss + clinical triggers]

**Recommended Workup**:
- Tier 1 (Immediate): [tests + rationale]
- Tier 2 (After Tier 1): [tests + rationale]
- Tier 3 (If unclear): [tests + rationale]
```

### 2.2 VINDICATE-M Framework

Systematic enumeration: **V**ascular · **I**nfectious · **N**eoplastic · **D**egenerative/Deficiency · **I**atrogenic/Idiopathic · **C**ongenital · **A**utoimmune/Allergic · **T**raumatic/Toxic · **E**ndocrine/Electrolyte · **M**ental/Metabolic.

### 2.3 Bayesian Reasoning

For key tests: pre-test probability → sensitivity/specificity → LR+/LR− → post-test probability interpretation.

---

## Module 3: Prescription Review

### Pre-Action Checklist

```
**Prescribing Gate** — Confirm before reviewing:

- [ ] Complete medication list with doses, routes, and frequencies is provided
- [ ] Patient age and weight are specified (required for dosing checks)
- [ ] Allergies are documented
- [ ] Relevant labs (at minimum: Cr / eGFR, LFTs if hepatically cleared drugs)
- [ ] Pregnancy/lactation status if patient is female of childbearing age
- [ ] Patient is flagged for special populations? (peds / geriatric / renal / hepatic / obesity)

If any unchecked → "I need [missing item(s)] before I can review this regimen."
```

### 3.1 Five-Step Review

```
**Prescription Review**

**Regimen**: [Drug A] [dose] [route] [frequency] + [Drug B] ...

---

**Step 1: Indication Check**
| Drug | Indicated For | Status |
|:---|:---|:---:|
| [Drug] | [FDA / off-label Level _] | ✅ / ⚠️ / ❌ |

**Step 2: Drug-Drug Interactions (DDI)**
| Pair | Interaction | Mechanism | Severity | Action |
|:---|:---|:---|:---:|:---|
| A + B | [effect] | [CYP / transporter] | 🔴/🟡/🟢 | [management] |

**Step 3: Dose Appropriateness**
| Drug | Standard | Prescribed | Adjustment? |
|:---|:---|:---|:---|
| [Drug] | [dose] | [dose] | [Yes/No + rationale] |

**Step 4: Contraindications & Precautions**
| Factor | Drug | Risk | Action |
|:---|:---|:---|:---|
| [allergy / comorbidity] | [Drug] | [risk] | [avoid / monitor / alternative] |

**Step 5: Monitoring Plan**
| Drug | Parameter | Frequency | Action Threshold |
|:---|:---|:---|:---|
| [Drug] | [lab/clinical] | [qXh/daily/weekly] | [stop if...] |
```

### 3.2 Special Populations

Auto-detect and apply specialized criteria:
- **Pregnancy**: FDA PLLR narrative + LactMed
- **Pediatrics**: Weight-based dosing, age-appropriate formulations
- **Geriatrics**: Beers Criteria (AGS 2023), STOPP/START v3, CrCl-based adjustment
- **Renal**: CKD-EPI eGFR / Cockcroft-Gault adjustment, nephrotoxin screening
- **Hepatic**: Child-Pugh adjustment, hepatotoxin screening
- **Obesity**: Weight-based vs. ideal vs. adjusted body weight guidance

### 3.3 Deprescribing

≥5 chronic meds triggers: Beers/STOPP screen → therapeutic duplication → NNT vs. NNH per drug → deprescribing candidates with taper protocols.

---

## Module 4: Lab & Imaging Interpretation

### Pre-Action Checklist

```
**Lab Gate** — Confirm before interpreting:

- [ ] Lab values with units and reference ranges are provided
- [ ] Patient age and sex are specified (reference ranges differ)
- [ ] Clinical context is provided (why were these labs ordered?) OR explicitly stated as "routine screening / incidental finding / no specific clinical context"
- [ ] Relevant PMH that could explain abnormalities is noted (if known)
- [ ] Prior values available for trend? If yes, date of priors

If any unchecked → "I need [missing item(s)] before I can interpret these results."
```

### 4.1 Lab Interpretation

```
**Laboratory Interpretation**

**Patient Context**: [age] [sex] [relevant PMH] [current clinical picture]

| Test | Result | Reference Range | Unit | Flag |
|:---|:---|:---|:---|:---:|
| [Na] | [ ] | 135–145 | mmol/L | 🔴↓ |

**Abnormal Analysis**:
- [Abnormal 1] ([value]): clinical significance → differential → critical value? [Yes/No] → next step
- [Abnormal 2] ...

**Pattern Recognition**: [synthesize into recognizable patterns, e.g. AGMA + hyperkalemia → AKI/rhabdomyolysis/adrenal insufficiency]

**Trend Analysis** (if priors): [direction + rate + significance]

**Overall Impression**: [1–2 sentence synthesis]
```

### 4.2 High-Yield Lab Patterns

| Pattern | Labs | Key Differential |
|:---|:---|:---|
| Anion-gap metabolic acidosis | ↓HCO3, ↑AG | MUDPILES |
| Non-AG metabolic acidosis | ↓HCO3, normal AG | HARDUP |
| Acute kidney injury | ↑Cr, trending | Pre-renal vs intrinsic vs post-renal |
| Cholestatic | ↑ALP > ↑ALT | Obstruction, drug-induced, PBC |
| Hepatocellular | ↑ALT > ↑ALP | Viral, toxic, ischemic, AIH |
| Iron deficiency anemia | ↓Hb, ↓MCV, ↓ferritin, ↑TIBC | GI bleeding, menstrual, dietary |
| Anemia of chronic disease | ↓Hb, nl MCV, ↑ferritin, ↓TIBC | Infection, inflammation, malignancy |

### 4.3 Imaging (Assisted Only)

This skill does NOT interpret imaging de novo. It only interprets the text of existing radiology reports and compares serial studies. Never claim to read an image.

---

## Module 5: Patient Communication

### Pre-Action Checklist

```
**Communication Gate** — Confirm before generating:

- [ ] Communication scenario is specified (breaking bad news / informed consent / education)
- [ ] Target audience is specified (patient / family / caregiver)
- [ ] Health literacy level is estimated (basic / intermediate / advanced)
- [ ] Key clinical facts to communicate are provided
- [ ] Cultural or language considerations noted?

If any unchecked → "I need [missing item(s)] before I can craft the communication."
```

### 5.1 Breaking Bad News — SPIKES

```
**S — Setting Up**: Private, quiet, key people present, uninterrupted time
**P — Perception**: "What have the doctors told you so far?"
**I — Invitation**: "How much detail would you like me to share?"
**K — Knowledge**: Warning shot → plain language → short chunks → no jargon → pause between
**E — Emotions & Empathy**: Acknowledge → silence → validate → don't rush to fix
**S — Strategy & Summary**: Key points → next steps → support services → follow-up
```

### 5.2 Informed Consent Elements

Diagnosis/Indication → Procedure description (plain language) → Benefits (quantified) → Risks (common >5% / uncommon 1–5% / rare <1%) → Alternatives including "no treatment" → Consequences of refusal → "What questions do you have?"

### 5.3 Patient Education (Adaptive)

Auto-adapt to 3 health literacy levels:

| Level | Approach | Example |
|:---|:---|:---|
| Basic (≤6th grade) | Short sentences, analogies, no jargon | "Your heart is like a pump. It's working too hard." |
| Intermediate | Some terms with definitions | "You have hypertension — that means high blood pressure." |
| Advanced | Full terminology + pathophysiology | "Essential hypertension with end-organ involvement..." |

Output: (1) What is this? (2) What caused it? (3) Medication table (drug/dose/when/why/side effects) (4) Home management (5) **Red-flag symptoms → call 911 NOW**

---

## Module 6: Evidence-Based Medicine

### Pre-Action Checklist

```
**EBM Gate** — Confirm before searching:

- [ ] PICO elements defined (Patient, Intervention, Comparison, Outcome)
- [ ] Question type identified (therapy / diagnosis / prognosis / harm / prevention)
- [ ] Preferred evidence sources specified (default: PubMed + Cochrane + guidelines)
- [ ] Timeframe for evidence recency specified (default: last 10 years)

If any unchecked → "I need [missing item(s)] before I can search for evidence."
```

### 6.1 PICO Framework

```
**Clinical Question (PICO)**
- P (Patient/Population): [describe]
- I (Intervention): [describe]
- C (Comparison): [describe, default: standard of care / placebo]
- O (Outcome): [primary + secondary]
**Question Type**: [Therapy / Diagnosis / Prognosis / Harm / Prevention]
```

### 6.2 Evidence Summary

```
**EBM Summary**
**PICO**: [one-line restatement]
**Sources**: PubMed / Cochrane / UpToDate / clinicaltrials.gov

| Level | Study (PMID) | Design / N | Key Finding | NNT/NNH | Bias |
|:---:|:---|:---|:---|:---:|:---:|
| I | [Author, Year] (PMID: [ ]) | MA, N=[ ] | [finding] | [ ] | Low |
| II | [Author, Year] (PMID: [ ]) | RCT, N=[ ] | [finding] | [ ] | Mod |

**Guideline Recommendations**:
| Guideline | Organization | Year | Recommendation | Strength |
|:---|:---|:---:|:---|:---:|
| [Name] | [org] | [year] | [recommendation] | [Class] |

**Clinical Bottom Line**: [1–3 sentence actionable synthesis]
```

### 6.3 Evidence Levels

| Level | Definition |
|:---:|:---|
| I | Systematic review / MA of high-quality RCTs, or large multi-center RCT |
| II | Individual RCT, high-quality cohort, systematic review of Level II |
| III | Non-randomized controlled trial, case-control, systematic review of Level III |
| IV | Case series, case reports, expert committee reports |
| V | Expert opinion, animal/lab studies, first principles |

---

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

## Safety Boundaries & Exit Triggers

### Emergency Recognition — HALT IMMEDIATELY

If the clinical picture matches any of the following, output ONLY:
> "⚠️ The information you've described is consistent with a potential medical emergency. AI cannot triage. Please seek immediate emergency medical attention (call 911 / 999 / 112, or go to the nearest Emergency Department)."

Triggers: chest pain + diaphoresis | thunderclap headache | acute dyspnea/stridor | active hemorrhage | altered consciousness/seizure/FAST+ stroke | anaphylaxis signs | trauma with possible spinal injury | suicidal/homicidal ideation with plan/intent | severe burns/electrical injury/drowning | sepsis criteria: fever + hypotension + altered mental status (qSOFA ≥ 2) | severe trauma with potential internal bleeding

### Knowledge Boundary

Ultra-rare diseases or insufficient published evidence → *"The published literature on this topic is limited. I recommend direct consultation with a specialist."*

### Ethical Red Lines

Refuse: assisted death counseling | unapproved experimental treatment outside clinical trials | intentional harm/Munchausen/abuse scenarios | medicolegal testimony.

---

## Changelog

| Version | Date | Changes |
|:---|:---|:---|
| 1.1.0 | 2026-05-23 | Added Pre-Action Checklist protocol (superpowers-style gate) for all 7 modules; added H&P and Discharge Summary templates; created examples/ directory with 3 real-world case studies; added CONTRIBUTING.md and .gitignore |
| 1.0.0 | 2026-05-22 | Initial release: 7 core modules (Documentation, Diagnosis, Prescribing, Labs, Communication, EBM, Calculators) with safety framework |

---

## Examples Directory

The `examples/` directory contains 3 real-world case studies demonstrating the skill in action:

1. **SOAP Note Generation** (`examples/1-soap-note.md`) — Shows the Pre-Action Checklist gate and full SOAP note output for a heart failure case.
2. **Prescription Review** (`examples/2-prescription-review.md`) — Demonstrates the 5-step review with special population auto-detection (geriatric + renal impairment).
3. **Diagnostic Reasoning** (`examples/3-diagnostic-reasoning.md`) — Illustrates VINDICATE-M framework, Wells Criteria, and evidence-based workup for a suspected DVT.

Each example includes the user's original input, the agent's internal checklist gate, and the final structured output. These serve as templates for users to understand how to interact with the skill and what to expect.

---

## References

CMS E&M Guidelines · Joint Commission standards · Beers Criteria (AGS 2023) · STOPP/START v3 · FDA PLLR · LactMed (NIH) · SPIKES Protocol (Baile et al., 2000, PMID: 11060458) · Oxford CEBM Levels of Evidence · ICD-11 (WHO) · RxNorm (NLM) · LOINC (Regenstrief) · SNOMED CT (IHTSDO) · ACC/AHA Guidelines · IDSA Guidelines · Surviving Sepsis Campaign Guidelines

---

*Named after Hippocrates of Kos (c. 460–370 BCE). Primum non nocere — first, do no harm.*