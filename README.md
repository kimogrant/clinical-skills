# Hippocrates — Full-Stack Clinical Assistant for AI Agents

<p align="center">
  <img src="https://img.shields.io/badge/version-1.1.0-blue" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
  <img src="https://img.shields.io/badge/modules-7%20%2B%20calculators-orange" alt="modules">
  <img src="https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Codex%20%7C%20Cursor%20%7C%20Gemini%20CLI-purple" alt="platforms">
  <img src="https://img.shields.io/badge/language-English-red" alt="language">
</p>

> The first open-source, production-grade clinical skill suite for AI coding agents. Give your Claude Code, Codex, or Cursor agent the clinical reasoning of a medical resident — with built-in safety guardrails.

**Related:** [Allergos](https://github.com/kimogrant/allergos) (allergy & immunology) · [CEO Operating System](https://github.com/kimogrant/ceo-operating-system) · [Web3 bounty PoC skill](https://github.com/kimogrant/web3-bounty-poc-report-skill) · [EVM audit skills](https://github.com/kimogrant/evm-audit-skill)

---

## Why Hippocrates?

AI coding agents are brilliant at writing software. But ask them to write a SOAP note, work through a differential diagnosis, or review a prescription regimen, and they fall flat — no structure, no evidence basis, dangerous gaps.

**Hippocrates** bridges that gap. It's a single `SKILL.md` file that encodes clinical workflow expertise into a format any AI agent can load and apply. Think of it as giving your AI a mini-medical residency.

**Good for**:
- Healthtech developers building clinical AI tools
- Medical students and residents using AI for study and documentation
- Clinical researchers drafting systematic reviews
- Anyone building AI agents that need to handle medical content safely and professionally

## Quick Start

### Claude Code

```bash
git clone https://github.com/kimogrant/clinical-skills.git
mkdir -p ~/.claude/skills
cp SKILL.md ~/.claude/skills/hippocrates.md
```

### Codex

```bash
cp SKILL.md ~/.codex/skills/hippocrates.md
```

### Cursor

```bash
cp SKILL.md .cursor/rules/hippocrates.md
```

### Any AI Agent (Universal)

Inject the contents of `SKILL.md` as a system prompt or skill file. Compatible with any AI tool that supports custom instructions.

## Example

```
User: Write a SOAP note. 45M, 3 months epigastric pain, worse on empty stomach,
      with heartburn. PMH: NSAID use for knee OA. No alarm symptoms.

Agent (with Hippocrates loaded):
→ Full SOAP note with:
  - HPI structured by OLDCARTS
  - Exam template with pertinent positives/negatives
  - Differential: PUD vs. GERD vs. gastritis vs. biliary
  - Plan: hold NSAIDs, start PPI trial, H. pylori testing, EGD if refractory
  - Evidence levels cited for PPI in suspected PUD (Level I, Cochrane 2022)
→ Safety disclaimer appended
```

## Modules at a Glance

| # | Module | What It Does | Example Trigger |
|:---:|:---|:---|:---|
| 1 | **Clinical Documentation** | SOAP notes, H&P, progress notes, discharge summaries, operative notes | "Write a SOAP note for..." |
| 2 | **Diagnostic Reasoning** | VINDICATE-M framework, Bayesian pre-test probability, structured DDx tables | "What's the differential for..." |
| 3 | **Prescription Review** | 5-step review: indication → DDI → dose → contraindications → monitoring. Auto-detects pregnancy/peds/geriatric/renal/hepatic | "Review this medication regimen" |
| 4 | **Lab & Imaging** | Lab interpretation with pattern recognition (AGMA, AKI, LFT patterns, anemias), serial imaging comparison | "Interpret these labs" |
| 5 | **Patient Communication** | SPIKES protocol for breaking bad news, informed consent elements, adaptive health literacy education | "How do I tell the patient..." |
| 6 | **Evidence-Based Medicine** | PICO framing, evidence tables with NNT/NNH, guideline recommendations | "What's the evidence for..." |
| 7 | **Clinical Calculators** | Wells, CURB-65, CHADS₂VASc, HAS-BLED, MELD, SOFA, GCS, ASCVD, and more | Auto-triggered by clinical context |

All modules are protected by **Pre-Action Checklists** — mandatory verification gates (superpowers-style) that prevent the agent from proceeding with incomplete patient data.

## Built-in Safety

Hippocrates is designed with safety-first architecture:

- **Auto-disclaimer**: Every clinical output is wrapped with clear AI-assistance disclaimers
- **Emergency recognition**: Automatically detects potential emergencies (chest pain + diaphoresis, thunderclap headache, active hemorrhage, etc.) and **halts output** — redirecting to 911/ED
- **Red-line refusal**: Rejects queries about assisted death counseling, Munchausen scenarios, or medicolegal testimony
- **Privacy by default**: Auto-redacts PII (name, DOB, MRN, SSN, address, phone) from any processed patient data
- **Evidence-gated**: No clinical claim without evidence level and source attribution

**Important**: This skill is an AI assistant tool and does NOT replace licensed clinical judgment. All outputs must be reviewed by a qualified healthcare professional.

## Roadmap

- [ ] Module 8: WHO Surgical Safety Checklist
- [ ] Module 9: Antimicrobial Stewardship
- [ ] Module 10: Oncology TNM Staging Reference
- [ ] Module 11: Pediatric Growth & Development
- [ ] i18n: Spanish, Mandarin, French, Arabic, Portuguese
- [ ] FHIR/HL7 structured output mode (EHR integration)
- [ ] Real-time drug interaction API integration (RxNorm + OpenFDA)
- [ ] Specialty deep-dives: Cardiology, Neurology, OB/GYN, Psychiatry

## Contributing

We welcome contributions — especially from clinicians, pharmacists, and health informaticists:

```bash
git clone https://github.com/kimogrant/clinical-skills.git
# Make your changes to SKILL.md
# Submit a PR with: [Module] Brief description
```

**Standards**:
- Clinical content must cite source (PMID / guideline + year / authoritative DB)
- Drug data must include source + last-updated date
- All new content must pass the safety boundary review

See [PROJECT.md](PROJECT.md) for detailed development guidelines.

## Star History

If this project helps you build better clinical AI, consider giving it a star. It helps others discover it.

---

## License

MIT © [kimogrant](https://github.com/kimogrant/clinical-skills)

---

<p align="center">
  <sub>Named after Hippocrates of Kos (c. 460–370 BCE). <em>Primum non nocere</em> — first, do no harm.</sub>
</p>