#!/usr/bin/env python3
"""Repair HOI4 descriptor files for launcher pickup without altering gameplay metadata."""

from __future__ import annotations

import re
import sys
from pathlib import Path

TARGET_NAME = "AOTA"
TARGET_PATH = "mod/AOTA"


def read_text_no_bom(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_utf8_no_bom_unix(path: Path, text: str) -> None:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    path.write_text(normalized, encoding="utf-8", newline="\n")


def get_first_scalar(text: str, key: str) -> str | None:
    m = re.search(rf"(?m)^\s*{re.escape(key)}\s*=\s*\"([^\"]*)\"", text)
    return m.group(1) if m else None


def replace_first_scalar(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf"(?m)^(\s*{re.escape(key)}\s*=\s*)\"[^\"]*\"(\s*(?:#.*)?)$")
    if pattern.search(text):
        return pattern.sub(rf'\1"{value}"\2', text, count=1)

    # Append if absent (least invasive: add at end with newline safety)
    suffix = "" if text.endswith("\n") else "\n"
    return f"{text}{suffix}{key}=\"{value}\"\n"


def detect_root_mod(repo_root: Path) -> Path:
    mod_files = sorted(repo_root.glob("*.mod"))
    mod_files = [p for p in mod_files if p.name != "descriptor.mod"]
    if len(mod_files) == 1:
        return mod_files[0]
    if not mod_files:
        raise RuntimeError("No root .mod file found (excluding descriptor.mod).")
    raise RuntimeError(f"Multiple root .mod files found: {[p.name for p in mod_files]}")


def detect_internal_descriptor(repo_root: Path, root_mod_text: str) -> Path:
    path_val = get_first_scalar(root_mod_text, "path")
    if path_val and path_val.startswith("mod/"):
        folder_name = path_val.split("/", 1)[1]
        candidate = repo_root / folder_name / "descriptor.mod"
        if candidate.exists():
            return candidate

    # Fallback: descriptor.mod under repo, prefer non-root if present
    descriptors = sorted(repo_root.rglob("descriptor.mod"))
    if not descriptors:
        raise RuntimeError("No internal descriptor.mod found.")

    non_root = [p for p in descriptors if p.parent != repo_root]
    if len(non_root) == 1:
        return non_root[0]
    if len(non_root) > 1:
        raise RuntimeError(f"Multiple internal descriptor.mod files found: {[str(p) for p in non_root]}")

    # In-content repo fallback: root descriptor.mod is the internal descriptor
    return repo_root / "descriptor.mod"


def process_file(path: Path, updates: dict[str, str], protected_keys: tuple[str, ...]) -> tuple[str, str, dict[str, str | None], dict[str, str | None]]:
    old_text = read_text_no_bom(path)
    old_vals = {k: get_first_scalar(old_text, k) for k in (*updates.keys(), *protected_keys)}

    new_text = old_text
    for k, v in updates.items():
        new_text = replace_first_scalar(new_text, k, v)

    new_vals = {k: get_first_scalar(new_text, k) for k in (*updates.keys(), *protected_keys)}

    for k in protected_keys:
        if old_vals[k] != new_vals[k]:
            raise RuntimeError(
                f"Refusing to continue: {path} {k} would change from {old_vals[k]!r} to {new_vals[k]!r}."
            )

    write_utf8_no_bom_unix(path, new_text)
    return old_text, new_text, old_vals, new_vals


def main() -> int:
    repo_root = Path.cwd()

    root_mod = detect_root_mod(repo_root)
    root_old_text = read_text_no_bom(root_mod)
    internal_descriptor = detect_internal_descriptor(repo_root, root_old_text)

    _, _, root_old_vals, root_new_vals = process_file(
        root_mod,
        updates={"name": TARGET_NAME, "path": TARGET_PATH},
        protected_keys=("version", "supported_version"),
    )

    _, _, desc_old_vals, desc_new_vals = process_file(
        internal_descriptor,
        updates={"name": TARGET_NAME},
        protected_keys=("version", "supported_version"),
    )

    version_ok = root_old_vals["version"] == root_new_vals["version"] == desc_old_vals["version"] == desc_new_vals["version"]
    supported_ok = (
        root_old_vals["supported_version"] == root_new_vals["supported_version"] == desc_old_vals["supported_version"] == desc_new_vals["supported_version"]
    )

    print("Descriptor repair report")
    print(f"root file: {root_mod}")
    print(f"internal descriptor: {internal_descriptor}")
    print(f"old root .mod name/path: {root_old_vals['name']!r} / {root_old_vals['path']!r}")
    print(f"new root .mod name/path: {root_new_vals['name']!r} / {root_new_vals['path']!r}")
    print(f"old internal descriptor name: {desc_old_vals['name']!r}")
    print(f"new internal descriptor name: {desc_new_vals['name']!r}")
    print(f"version unchanged: {version_ok} ({root_new_vals['version']!r})")
    print(f"supported_version unchanged: {supported_ok} ({root_new_vals['supported_version']!r})")

    if not (version_ok and supported_ok):
        raise RuntimeError("version and/or supported_version mismatch detected")

    return 0


if __name__ == "__main__":
    sys.exit(main())
