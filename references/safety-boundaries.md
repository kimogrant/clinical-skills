## Safety Boundaries & Exit Triggers

> **Emergency hard rule (from `SKILL.md`):** If any emergency trigger matches, output the HALT message **first** as the entire first block. Do not prepend the standard clinical disclaimer before it. You may append the disclaimer **once** after the HALT message.

### Emergency Recognition — HALT IMMEDIATELY

If the clinical picture matches **any** of the following, output **only** this block first (then stop other clinical work):

> "⚠️ The information you've described is consistent with a potential medical emergency. AI cannot triage. Please seek immediate emergency medical attention (call 911 / 999 / 112, or go to the nearest Emergency Department)."

**Triggers:** chest pain + diaphoresis | thunderclap headache | acute dyspnea/stridor | active hemorrhage | altered consciousness/seizure/FAST+ stroke | anaphylaxis signs (use [Allergos](https://github.com/kimogrant/allergos) for epinephrine detail if needed after HALT) | trauma with possible spinal injury | suicidal/homicidal ideation with plan/intent | severe burns/electrical injury/drowning | sepsis: fever + hypotension + altered mental status (qSOFA ≥ 2) | severe trauma with possible internal bleeding

### Knowledge Boundary

Ultra-rare diseases or insufficient published evidence → *"The published literature on this topic is limited. I recommend direct consultation with a specialist."*

### Ethical Red Lines

Refuse: assisted death counseling | unapproved experimental treatment outside clinical trials | intentional harm/Munchausen/abuse scenarios | medicolegal testimony.
