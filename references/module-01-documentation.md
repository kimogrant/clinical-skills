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
