# Example 2: Prescription Review

> Demonstrates the 5-step review framework with special population auto-detection.

---

## User Input

```
Review this regimen:

Patient: 78F, admitted for community-acquired pneumonia.
PMH: CKD stage 3 (baseline Cr 1.4, eGFR 42), atrial fibrillation on apixaban,
hypertension, type 2 diabetes.
Allergies: Penicillin → anaphylaxis (documented).

Current inpatient medications:
1. Levofloxacin 750 mg PO daily — started empirically for CAP
2. Apixaban 5 mg PO BID — continuation of home dose
3. Lisinopril 20 mg PO daily
4. Metformin 1000 mg PO BID
5. Ibuprofen 600 mg PO TID PRN — newly ordered for pleuritic chest pain

Labs: Cr 1.6 (↑ from 1.4), BUN 32, K 5.0, eGFR 35 (↓ from 42)
Weight: 64 kg
```

## Agent Process (with Hippocrates loaded)

### Step 1: Pre-Action Checklist Gate

```
**Prescribing Gate** — Confirm before reviewing:

- [x] Complete medication list → 5 drugs, all with doses/routes/frequencies
- [x] Patient age and weight → 78F, 64 kg
- [x] Allergies documented → Penicillin → anaphylaxis
- [x] Relevant labs → Cr 1.6 (↑), eGFR 35 (↓), K 5.0
- [x] Special populations flagged → Geriatric (78y, Beers Criteria applicable),
      Renal impairment (CKD stage 3b → acute-on-chronic? eGFR dropped from 42 → 35)
- [x] Female of childbearing age → No (78F, not applicable)

Two critical flags auto-detected: GERIATRIC + RENAL IMPAIRMENT.
Proceeding to full 5-step review.
```

### Step 2: Output

```
**Prescription Review**

**Regimen**: Levofloxacin 750 mg + Apixaban 5 mg BID + Lisinopril 20 mg +
Metformin 1000 mg BID + Ibuprofen 600 mg TID PRN

**Special Populations Active**: Geriatric (Beers Criteria), Renal Impairment (eGFR 35)

---

**Step 1: Indication Check**

| Drug | Indicated For | Status |
|:---|:---|:---:|
| Levofloxacin | CAP empiric therapy — appropriate per IDSA/ATS 2019 guidelines | ✅ |
| Apixaban | Non-valvular Afib, stroke prevention — continuation of home regimen | ✅ |
| Lisinopril | Hypertension — continuation | ✅ |
| Metformin | Type 2 DM — continuation | ⚠️ (see renal concerns below) |
| Ibuprofen | Pleuritic chest pain — PRN indication reasonable | ⚠️ (see interactions) |

---

**Step 2: Drug-Drug Interactions**

| Pair | Interaction | Mechanism | Severity | Action |
|:---|:---|:---|:---:|:---|
| Ibuprofen + Lisinopril | Reduced antihypertensive efficacy of ACEi | NSAID blunts ACEi vasodilation | 🟡 | Monitor BP; prefer acetaminophen if BP uncontrolled |
| Ibuprofen + Apixaban | **Increased bleeding risk** — NSAID + anticoagulant | Platelet inhibition + factor Xa inhibition → synergistic | 🔴 | **STRONG AVOID.** Replace ibuprofen with acetaminophen 650–1000 mg TID PRN |
| Ibuprofen + Metformin | NSAID can worsen renal function → metformin accumulation → lactic acidosis risk | ↓ GFR → ↓ metformin clearance | 🔴 | See Step 3 |
| Levofloxacin + Apixaban | Fluoroquinolones may slightly increase anticoagulant effect | Possible CYP / P-gp interaction | 🟡 | Monitor for bleeding; no dose adjustment required per current evidence |
| Lisinopril + Metformin | No direct interaction | — | 🟢 | — |

---

**Step 3: Dose Appropriateness (Renal Adjustment — eGFR 35)**

| Drug | Standard Dose | Renal Adjustment (eGFR 35) | Current Dose | Action |
|:---|:---|:---|:---|:---|
| Levofloxacin | 750 mg daily | 750 mg ×1 then 500 mg q48h (eGFR 20–49) | 750 mg daily | ⚠️ **Overdose.** Adjust to 500 mg q48h |
| Apixaban | 5 mg BID | 5 mg BID (no adjustment for eGFR >15 on standard criteria; CKD stage 3b is borderline — check if Afib dosing uses 2.5 mg BID per age≥80/weight≤60/Cr≥1.5 criteria) | 5 mg BID | ⚠️ **Check:** Patient has Cr 1.6 ≥1.5 → meets 1 of 3 criteria for dose reduction to 2.5 mg BID. But age 78 (<80) and weight 64 kg (>60). **Only 1 of 3 criteria met → continue 5 mg BID.** Document rationale. |
| Lisinopril | 10–40 mg daily | Continue, monitor K (already 5.0) and Cr | 20 mg daily | ⚠️ **Hold if K >5.5 or Cr rises >30%.** Current K 5.0 — borderline. Recheck tomorrow. |
| Metformin | 500–1000 mg BID | **CONTRAINDICATED when eGFR <30.** eGFR 35 = caution zone: reduce to max 1000 mg/day | 1000 mg BID | 🔴 **Overdose.** Hold metformin during acute illness. Restart at 500 mg BID when Cr returns to baseline. Lactic acidosis risk elevated with concurrent AKI + possible sepsis. |
| Ibuprofen | 400–600 mg TID PRN | **AVOID in CKD** — NSAIDs cause afferent arteriole vasoconstriction → ↓GFR, Na/H2O retention, ↑K | 600 mg TID | 🔴 **DISCONTINUE.** Triple risk: (1) nephrotoxic in CKD, (2) bleeding risk with apixaban, (3) likely contributed to AKI (Cr 1.4→1.6). Replace with acetaminophen 650–1000 mg TID PRN. |

---

**Step 4: Contraindications & Precautions**

| Patient Factor | Relevant Drug | Concern | Action |
|:---|:---|:---|:---|
| Penicillin → anaphylaxis | All drugs checked | No cross-reactivity with fluoroquinolones, DOACs, ACEi, biguanides, or NSAIDs | ✅ No contraindication from allergy |
| eGFR 35 (AKI on CKD) | Ibuprofen | NSAID nephrotoxicity — afferent arteriole constriction + salt/water retention | 🔴 **Stop immediately.** Document as probable contributor to AKI |
| eGFR 35 + acute illness | Metformin | Lactic acidosis risk elevated with AKI + possible sepsis context | 🔴 **Hold.** Document. Restart when Cr <1.5 and patient stable |
| Age 78 (geriatric) | Ibuprofen | Beers Criteria: avoid chronic NSAID use in elderly (GI bleed, CKD, HTN worsening) | 🔴 Consistent with other flags — discontinue. Use acetaminophen |
| K 5.0 (upper-normal) | Lisinopril | ACEi can cause hyperkalemia, especially with AKI | ⚠️ Recheck K tomorrow. If >5.5, hold lisinopril. Low-potassium diet counseling. |
| K 5.0 | Ibuprofen | NSAIDs worsen hyperkalemia via ↓ renin → ↓ aldosterone | 🔴 Additional reason to discontinue |

---

**Step 5: Monitoring Plan**

| Drug | Parameter | Frequency | Threshold |
|:---|:---|:---|:---|
| Levofloxacin (adjusted to 500 mg q48h) | Cr, K | Daily | Stop if Cr↑ >30% or K>5.5. Watch for QTc prolongation (ECG if concern) |
| Apixaban 5 mg BID | Hb, Cr, bleeding signs | Daily Hb | Hold if Hb drop >2g/dL or active bleeding. Reassess dose criteria (Cr≥1.5 is 1/3 criteria — currently still 5 mg BID) |
| Lisinopril 20 mg | K, Cr, BP | Daily | Hold if K>5.5 or Cr rises >30% from baseline |
| Metformin | — | — | **HELD.** Restart criteria: Cr ≤1.5, eGFR ≥45, acute illness resolved |
| Ibuprofen | — | — | **DISCONTINUED.** Replace with acetaminophen. Document AKI. Monitor Cr trend |

---

**Summary of Actions**:

🔴 **CRITICAL — STOP immediately**: Ibuprofen (nephrotoxicity + bleeding risk + likely AKI contributor)
🔴 **Dose adjustment required**: Levofloxacin 750→500 mg q48h (renal)
🔴 **Hold**: Metformin (AKI + acute illness → lactic acidosis risk)
⚠️ **Monitor closely**: Lisinopril (K 5.0 trending), Apixaban (bleeding risk, borderline dose criteria)
✅ **Continue unchanged**: None — all 5 medications require intervention
```

---

*This content is AI-generated for clinical reference only. All decisions must be reviewed by a licensed healthcare professional.*