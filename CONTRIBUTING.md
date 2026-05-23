# Contributing to Hippocrates

We welcome contributions — especially from clinicians, pharmacists, and health informaticists.

## How to Contribute

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/kimogrant/clinical-skills.git
   ```
3. **Create a branch**:
   ```bash
   git checkout -b feature/your-module-name
   ```
4. **Make your changes**:
   - Clinical templates → edit the relevant `references/module-*.md`
   - Triggers / hard rules / index → edit `SKILL.md` only
   - New module: add `references/module-0X-*.md`, index row in `SKILL.md`, example in `examples/`
   - Bump `VERSION` and `references/changelog.md`
5. **Commit** with a descriptive message:
   ```bash
   git commit -m "[Module] Brief description of change"
   ```
6. **Push** and open a Pull Request

## Standards

- **Clinical content must cite source**: PMID + year, or guideline name + issuing body + year, or authoritative database + retrieval date
- **Drug data must include source**: RxNorm / DailyMed / OpenFDA + date retrieved
- **Lab reference ranges**: must specify population (adult / pediatric) and unit system
- **All new content must pass the safety boundary review**: no hallucinated claims, no unqualified clinical advice, all outputs wrapped with disclaimer protocol
- **Pre-Action Checklists are mandatory for all modules**: every module must define what information the agent must confirm before generating output

## Review Process

- At least 1 reviewer with clinical background must approve PRs affecting `references/` clinical content or `SKILL.md` safety rules
- Non-clinical PRs (typos, formatting, README updates) may be self-reviewed by maintainers
- All PRs must pass the testing checklist in `PROJECT.md`

## Code of Conduct

- Be respectful and constructive
- Debate clinical content on its merits — cite evidence, not authority
- Patient safety is the highest priority. When in doubt, err on the side of caution.
- This project adheres to a "do no harm" principle. Contributions that could enable unsafe clinical AI practices will not be merged.

## Regenerating references (maintainers)

After editing a monolithic draft only:

```bash
python scripts/split_skill.py
```

Canonical source is `references/*.md`, not a single giant `SKILL.md` body.

## Related

- [Allergos](https://github.com/kimogrant/allergos) — allergy & immunology skill

## Questions?

Open an Issue with the tag `question` or start a Discussion.