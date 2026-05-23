# Hippocrates — Project Documentation

## Repository Structure

```
clinical-skills/
├── SKILL.md          # Core skill file (the product)
├── README.md         # GitHub project landing page
├── LICENSE           # MIT License
├── PROJECT.md        # Development documentation (this file)
├── examples/         # Usage examples
│   ├── 1-soap-note.md              # SOAP note generation example
│   ├── 2-prescription-review.md    # Medication review example
│   └── 3-diagnostic-reasoning.md   # DDx workflow example
```

## Core File: SKILL.md

The `SKILL.md` file is the sole deliverable. It follows the Anthropic Agent Skills specification:

- **Metadata block**: YAML frontmatter with name, version, author, tags, supported platforms
- **Trigger conditions**: Keyword-based auto-activation rules
- **7 modules**: Detailed instruction blocks with output templates, each protected by a Pre-Action Checklist gate
- **Safety boundaries**: Emergency recognition, red-line refusal, privacy rules

### Design Principles

1. **Self-contained**: One file. No dependencies. Load and go.
2. **Structured output**: Every module has a clear output template to enforce consistent, professional formatting
3. **Evidence-gated**: No clinical claim without evidence level + source attribution
4. **Safety-first**: Every output auto-wrapped with disclaimers; emergencies auto-detected and blocked. Mandatory Pre-Action Checklists (superpowers-style) prevent generation on incomplete data.
5. **Progressive disclosure**: Modules are independently triggerable; the agent loads only what's needed

## Development Workflow

### Adding a New Module

1. Propose the module via GitHub Issue with:
   - Clinical domain and target users
   - 3 concrete example use cases
   - Evidence sources you'll rely on
2. Draft the module using the existing template structure:
   ```
   ### X.X Module Name

   ### Pre-Action Checklist
   [mandatory gate — what must be confirmed before output]

   **Trigger**: [keywords]
   **Input requirements**: [minimum info needed]
   **Output format**: [template]
   ```
3. Add a corresponding example in `examples/`
4. Submit PR with `[Module] Brief description`
5. At least 1 reviewer with clinical background must approve

### Updating Clinical Content

- All updates must reference guidelines published within the last 3 years
- Drug interaction data must include source database + date retrieved
- Lab reference ranges must specify population (adult/pediatric) and units

### Versioning

- **Major** (X.0.0): New module, breaking format changes, new safety rules
- **Minor** (0.X.0): New content within existing modules, new calculators, new examples
- **Patch** (0.0.X): Corrections, reference updates, formatting fixes

## Testing Checklist

Before each release, verify:

- [ ] SOAP note generation: correct format, appropriate DDx, no hallucinated findings
- [ ] Prescription review: DDI detection accuracy, special population auto-detection
- [ ] Pre-Action Checklists: each module gate blocks output on incomplete data
- [ ] Emergency recognition: chest pain + diaphoresis → blocked with 911 redirect
- [ ] Privacy: PII auto-redaction when processing sample patient data
- [ ] Evidence attribution: every clinical claim has Level + source
- [ ] Cross-platform: loads without error in Claude Code, Codex, Cursor

## Release Process

1. Update version in `SKILL.md` (metadata block + changelog)
2. Update version badge in `README.md`
3. Manually verify: YAML metadata valid, no broken internal references, examples consistent with SKILL.md templates
4. Create annotated tag: `git tag -a v1.1.0 -m "Version 1.1.0"`
5. Push tag, create GitHub Release with changelog

## Contributors

- [Your Name / GitHub handle] — Project creator, initial modules
- [Contributor slots open]

## Acknowledgments

This project builds upon:
- CMS Evaluation & Management Documentation Guidelines
- Beers Criteria (American Geriatrics Society, 2023)
- SPIKES Protocol (Baile et al., 2000)
- Oxford Centre for Evidence-Based Medicine Levels of Evidence
- ICD-11 (WHO), RxNorm (NLM), LOINC (Regenstrief Institute)

---

**Last updated**: 2026-05-23