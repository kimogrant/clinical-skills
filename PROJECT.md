# Hippocrates — Project Documentation

## Repository Structure

```text
clinical-skills/
├── SKILL.md              # Frontmatter, hard rules, module index (~120 lines)
├── VERSION
├── skill.sh
├── references/
│   ├── module-01-documentation.md
│   ├── module-02-diagnostic-reasoning.md
│   ├── module-03-prescription-review.md
│   ├── module-04-lab-imaging.md
│   ├── module-05-patient-communication.md
│   ├── module-06-evidence-based-medicine.md
│   ├── module-07-clinical-calculators.md
│   ├── safety-boundaries.md
│   ├── guidelines.md
│   └── changelog.md
├── examples/
├── README.md / README.zh.md
├── CONTRIBUTING.md
└── LICENSE
```

## Skill identity

| Field | Value |
|-------|--------|
| Agent Skills `name` | `clinical-skills` (must match install folder name) |
| Display / brand | **Hippocrates** |
| Legacy alias | Some docs refer to `hippocrates.md` — prefer `clinical-skills/` directory |

## Design principles

1. **Progressive disclosure** — one `references/` file per task
2. **Emergency HALT first** — no disclaimer before 911/ED message
3. **Evidence-gated** — Level I–V + source on claims
4. **Checklist-gated** — incomplete data → no clinical output

## Adding a module

1. Add `references/module-0X-name.md` with Pre-Action Checklist + templates
2. Add row to `SKILL.md` module index
3. Add `examples/` case
4. Bump `VERSION` + `references/changelog.md`

## Testing checklist

- [ ] Emergency: chest pain + diaphoresis → HALT only, no SOAP first
- [ ] Incomplete SOAP request → documentation gate blocks
- [ ] Prescription review: geriatric + renal flags in example 2 pattern
- [ ] `SKILL.md` YAML frontmatter valid; `name: clinical-skills`
- [ ] `./skill.sh install` copies `references/` + `examples/`

## Release process

1. Update `VERSION`, `references/changelog.md`, README badge
2. Run testing checklist
3. `git tag -a v1.2.0 -m "Version 1.2.0"`

## Maintainers

- [kimogrant](https://github.com/kimogrant) — creator

## Related

- [Allergos](https://github.com/kimogrant/allergos) — allergy & immunology vertical skill

**Last updated**: 2026-05-23
