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
