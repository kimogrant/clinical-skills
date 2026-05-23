# Example 1: SOAP Note Generation

> This shows how Hippocrates (`clinical-skills`) processes a real scenario — Pre-Action gate → `references/module-01-documentation.md` templates → SOAP output.

---

## User Input

```
Write a SOAP note for a 62-year-old male presenting with progressive dyspnea
on exertion over the past 2 months. He gets winded walking up one flight of
stairs now. Dry cough at night. No chest pain, no fever, no hemoptysis.
PMH: hypertension, CAD s/p stent 2019. Meds: lisinopril 10mg, atorvastatin
40mg, aspirin 81mg. Former smoker (30 pack-years, quit 5 years ago). Works
as an accountant. BMI 32.
Vitals: BP 148/88, HR 92, RR 22, SpO2 93% RA, T 98.6°F.
Exam: JVD at 30 degrees, bibasilar crackles, +1 bilateral pitting edema.
```

## Agent Process (with Hippocrates loaded)

### Step 1: Pre-Action Checklist Gate

```
**Documentation Gate** — Confirm before writing:

- [x] Patient age and gender are specified → 62M
- [x] Chief complaint is clearly stated → progressive dyspnea on exertion × 2 months
- [x] Setting is specified → outpatient (clinic)
- [x] Document type is specified → SOAP note
- [x] Key HPI elements: onset (2mo, progressive), location (pulmonary, bilateral),
      quality (dyspnea on exertion), modifying factors (none reported explicitly)

All checks passed. Proceeding to SOAP note generation.
```

### Step 2: Output

```
**SOAP Note**

**Date**: 2026-05-23
**Provider**: [Name]
**Chief Complaint**: "Progressive exertional dyspnea × 2 months"

---

**Subjective**:

**HPI**:
- Onset: Gradual, over approximately 2 months, progressively worsening
- Location: Pulmonary — dyspnea reported as "can't catch my breath"
- Quality: Exertional dyspnea, now provoked by minimal activity (1 flight of stairs)
- Severity: NYHA Class II–III (mild limitation → marked limitation transition)
- Modifying factors: Worse with supine position (orthopnea implied by nighttime dry cough);
  rest partially relieves
- Associated symptoms: Dry cough, nocturnal predominance; bilateral leg swelling noted
- No: chest pain, fever, hemoptysis, palpitations, wheezing
- Context: Known CAD with prior PCI (2019), HTN, former smoker, obese
- ROS pertinent negatives: No PND explicitly reported, no syncope, no cyanosis

**PMH**: Hypertension, Coronary Artery Disease s/p DES to [vessel] (2019)
**PSH**: PCI (2019)
**Allergies**: NKDA
**Medications**: Lisinopril 10 mg PO daily, Atorvastatin 40 mg PO daily, Aspirin 81 mg PO daily
**Family History**: Not reported
**Social History**: Former smoker — 30 pack-years, quit 5 years ago. Occupation: accountant (sedentary).
  Alcohol: not reported. Denies illicit substance use.

---

**Objective**:

**Vitals**: T 98.6°F | HR 92 bpm (regular) | RR 22/min | BP 148/88 mmHg | SpO2 93% on RA | BMI 32 kg/m²
**Physical Exam**:
- General: Mild respiratory distress when speaking in full sentences
- HEENT: JVD at 30 degrees above sternal angle (elevated, suggests ↑ right-sided filling pressures)
- Chest/Lungs: Bibasilar fine inspiratory crackles (velcro-type), symmetric chest expansion,
  no wheezing, no egophony
- Cardiac: Regular rate and rhythm, no S3/S4 gallop appreciated though JVD present,
  PMI not displaced
- Abdomen: Soft, non-tender, no hepatomegaly appreciated
- Extremities: +1 bilateral pitting edema to mid-shin, warm, well-perfused
- Neurologic: Alert, oriented ×3

**Labs/Imaging**: Not yet available. Recommended: BNP, CBC, BMP, Troponin, CXR PA/Lat,
  Echocardiogram (2D + Doppler), ECG.

---

**Assessment**:

**Primary Diagnosis**: Acute-on-chronic heart failure with reduced vs. preserved ejection fraction
  — suspect ischemic cardiomyopathy given CAD history (ICD-11: BD10)

**Differential Diagnoses**:
1. COPD exacerbation — likelihood: Low. No wheezing, no hyperinflation on exam,
   smoking history but quit 5 years ago, no prior PFT data
2. Pulmonary hypertension (WHO Group 2 — left heart disease) — likelihood: Medium.
   JVD + edema suggest right heart involvement secondary to left-sided failure
3. Anemia contributing to dyspnea — likelihood: Unknown (pending CBC).
   Would exacerbate HF symptoms

**Clinical Reasoning**: 62M with known CAD + HTN + obesity presenting with 2 months of
progressive exertional dyspnea, orthopnea, JVD, bibasilar crackles, and bilateral edema —
classic clinical picture of decompensated heart failure. CAD history raises suspicion for
ischemic etiology. BNP and echocardiogram will confirm and characterize.

---

**Plan**:

**Diagnostics** (Stat):
- ECG — assess for ischemia, LVH, arrhythmia
- CXR PA/Lat — cardiomegaly, pulmonary vascular congestion, pleural effusions
- BNP/NT-proBNP — confirm HF and assess severity (Level I, ACC/AHA 2022)
- CBC, BMP (including Cr, BUN, electrolytes) — prior to diuresis
- Troponin — rule out concurrent ACS
- Transthoracic Echocardiogram (within 48h) — LVEF, wall motion, valvular assessment,
  RV function, estimate PA pressure

**Therapeutics**:
1. Furosemide 40 mg IV ×1 (or PO if outpatient management, 40 mg PO BID) —
   loop diuretic for volume overload (Level I, ACC/AHA 2022)
2. Continue Lisinopril 10 mg daily — ACEi cornerstone of GDMT, titrate upward
   as tolerated (Level I, ACC/AHA 2022)
3. Continue Atorvastatin 40 mg daily
4. Continue Aspirin 81 mg daily

**Patient Education**:
- Sodium restriction <2g/day
- Fluid restriction 1.5–2L/day
- Daily weight monitoring — same scale, same time, record; call if +2 lbs in 1 day or +5 lbs in 1 week

**Follow-up**: Cardiology clinic within 1 week. Call or return to ED for: worsening dyspnea
at rest, chest pain, palpitations/syncope, weight gain >5 lbs in one week.

**Referrals**: Cardiology (HF specialty clinic if available), Registered Dietitian (sodium/fluid education).
```

---

*This content is AI-generated for clinical reference only. All decisions must be reviewed by a licensed healthcare professional.*