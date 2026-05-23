# Hippocrates — Full-Stack Clinical Assistant for AI Agents

<p align="center">
  <img src="https://img.shields.io/badge/version-1.2.0-blue" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
  <img src="https://img.shields.io/badge/modules-7%20%2B%20calculators-orange" alt="modules">
  <img src="https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Codex%20%7C%20Cursor%20%7C%20Gemini%20CLI-purple" alt="platforms">
  <img src="https://img.shields.io/badge/language-English-red" alt="language">
</p>

> Production-grade clinical skill for AI agents — documentation, diagnosis, prescribing, labs, communication, EBM, and calculators with Pre-Action safety gates.

**Related:** [Allergos](https://github.com/kimogrant/allergos) · [CEO OS](https://github.com/kimogrant/ceo-operating-system) · [Web3 bounty PoC](https://github.com/kimogrant/web3-bounty-poc-report-skill) · [EVM audit](https://github.com/kimogrant/evm-audit-skill)

English | [简体中文](./README.zh.md)

---

## Why Hippocrates?

**Hippocrates** encodes resident-level clinical workflows into an [Agent Skill](https://agentskills.io/) package: `SKILL.md` + on-demand `references/` modules.

**Good for:** healthtech builders, trainees, researchers, and anyone who needs structured, evidence-tagged medical outputs with emergency HALT routing.

## Install (recommended)

```bash
git clone https://github.com/kimogrant/clinical-skills.git
cd clinical-skills
chmod +x skill.sh
./skill.sh install /path/to/your/project
```

Installs to: `your-project/.cursor/skills/clinical-skills/` (includes `references/` and `examples/`).

Reload Cursor → invoke **`/clinical-skills`** (skill id; display name **Hippocrates**).

### Other platforms

| Platform | Path |
|----------|------|
| Cursor (manual) | `.cursor/skills/clinical-skills/` — copy full repo skill bundle |
| Claude Code | `~/.claude/skills/clinical-skills/SKILL.md` + `references/` |
| Codex | `~/.codex/skills/clinical-skills/` |

**Do not** copy only `SKILL.md` without `references/` — module templates live there.

## Example

See [`examples/1-soap-note.md`](examples/1-soap-note.md) for Pre-Action gate → full SOAP output (heart failure case).

## Modules

| # | Module | Reference file |
|---|--------|----------------|
| 1 | Clinical documentation | `references/module-01-documentation.md` |
| 2 | Diagnostic reasoning | `references/module-02-diagnostic-reasoning.md` |
| 3 | Prescription review | `references/module-03-prescription-review.md` |
| 4 | Lab & imaging | `references/module-04-lab-imaging.md` |
| 5 | Patient communication | `references/module-05-patient-communication.md` |
| 6 | Evidence-based medicine | `references/module-06-evidence-based-medicine.md` |
| 7 | Clinical calculators | `references/module-07-clinical-calculators.md` |

## Safety

```text
Input → Emergency trigger? → YES → HALT message first (911/ED), then stop
       → NO → Pre-Action checklist → load one reference module → output
```

Details: `references/safety-boundaries.md`

## Repository layout

| Path | Purpose |
|------|---------|
| `SKILL.md` | Frontmatter, hard rules, module index |
| `references/` | Per-module templates |
| `examples/` | Case studies |
| `skill.sh` | Install helper |
| `VERSION` | Semver |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [PROJECT.md](PROJECT.md).

## License

MIT © [kimogrant](https://github.com/kimogrant/clinical-skills)

<p align="center"><sub><em>Primum non nocere</em> — first, do no harm.</sub></p>
