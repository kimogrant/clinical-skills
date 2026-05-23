"""Split monolithic SKILL.md into references/."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
parts = re.split(r"(?=^## Module \d+:|^## Safety Boundaries)", text, flags=re.M)

MODULE_FILES = {
    1: "module-01-documentation.md",
    2: "module-02-diagnostic-reasoning.md",
    3: "module-03-prescription-review.md",
    4: "module-04-lab-imaging.md",
    5: "module-05-patient-communication.md",
    6: "module-06-evidence-based-medicine.md",
    7: "module-07-clinical-calculators.md",
}

refs = ROOT / "references"
refs.mkdir(exist_ok=True)

for part in parts[1:]:
    part = part.strip()
    if part.startswith("## Safety"):
        (refs / "safety-boundaries.md").write_text(part + "\n", encoding="utf-8")
        continue
    m = re.match(r"^## Module (\d+):", part)
    if m:
        n = int(m.group(1))
        fname = MODULE_FILES.get(n, f"module-{n:02d}.md")
        (refs / fname).write_text(part + "\n", encoding="utf-8")
        print(f"wrote {fname}")

tail = re.search(r"^## Changelog", text, re.M)
if tail:
    (refs / "changelog.md").write_text(text[tail.start() :].strip() + "\n", encoding="utf-8")
    print("wrote changelog.md")
