#!/usr/bin/env python3
"""Lightweight static checks for recurring AOTA HOI4 script regressions."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]

CHECKS = [
    (Path("common/decisions"), re.compile(r"^(decision_categories|decisions)\s*=|^category\s*=", re.M), "legacy decision root wrapper"),
    (Path("events"), re.compile(r"\badd_opinion\s*=\s*\{"), "deprecated add_opinion effect"),
    (Path("events"), re.compile(r"\bbecome_subject\s*=\s*\{"), "deprecated become_subject effect"),
    (Path("common/ideas"), re.compile(r"\b(improve_relation|coastal_bunker_cost|operative_mission_speed|army_experience_gain|navy_experience_gain|army_recovery_rate|army_attrition_factor)\s*="), "legacy idea modifier token"),
]

issues = []
for folder, pattern, label in CHECKS:
    base = ROOT / folder
    for path in sorted(base.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for m in pattern.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            issues.append(f"{path.relative_to(ROOT)}:{line}: {label}")

if issues:
    print("AOTA static lint found issues:")
    for item in issues:
        print(f" - {item}")
    sys.exit(1)

print("AOTA static lint passed: no tracked regression patterns found.")
