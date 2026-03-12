# AOTA Kaiserreich Standards Repass and Execution

## A. Executive summary

### Overall comparison result
AOTA already has broad content depth and country/system coverage, but it still diverges from Kaiserreich-level technical discipline in parser-facing areas (effect syntax correctness, character schema consistency, and regression-prevention guardrails). This repass prioritized zero-compromise syntax and reference hygiene hardening first, then maintainability discipline.

### Biggest Kaiserreich-derived standards extracted
- Parser-safe canonical syntax over legacy shorthand.
- Stable schema usage per system file-type (focus/decision/event/character).
- Explicit anti-regression tooling for recurring fault classes.
- Branch and system integration that remains machine-parseable before any gameplay polish.

### Biggest AOTA weaknesses found
- Legacy `add_autonomy_ratio` scalar syntax persisted across multiple focus trees.
- Legacy character `portrait_path` tokens persisted in character definition files.
- Existing static lint checks did not enforce these two recurring parser-risk patterns.

### Biggest improvements applied
- Converted all detected `add_autonomy_ratio = <number>` usages to canonical effect form `add_autonomy_ratio = { value = <number> }` in affected focus trees.
- Migrated legacy character portrait definitions from `portrait_path = "..."` to modern `portraits = { civilian = { large = "..." } }` blocks in affected character files.
- Expanded `aota_static_lint.py` to block reintroduction of both anti-patterns.

### Biggest remaining risks
- Historical log inventory still includes many legacy issues outside this execution pass (ideas token drift, old one-line monolithic script style, and broader long-tail standards cleanup).
- Kaiserreich full source tree was not present in this workspace during this pass, so practical benchmark extraction was re-derived from existing in-repo Kaiserreich benchmark reports and revalidated against current AOTA code.

---

## B. Kaiserreich coding standards extracted

1. **Syntax discipline**
   - Use canonical effect/object forms where parser behavior is strict.
   - Avoid legacy shorthand that can silently fail across patches.

2. **Structural discipline**
   - Keep system files predictable by schema and purpose.
   - Avoid mixing older and newer object conventions inside the same subsystem.

3. **Anti-pattern avoidance**
   - Eliminate repeated high-risk tokens through lintable policy, not ad-hoc fixes.
   - Prevent regressions with static checks for known recurring parser failures.

4. **Maintainability discipline**
   - Treat error-log recurrence clusters as architectural debt.
   - Fix root syntax classes across all instances in a subsystem.

---

## C. Full AOTA syntax and structure findings

### What was parsed in this repass
- Whole repository inventory and script-facing content folders (`common/`, `events/`, `history/`, `localisation/`, `interface/`) were scanned.
- Latest raw error log and existing parsed-lint tooling were reviewed.
- Targeted regex-based full-tree checks were run for recurring high-severity parser patterns.

### Major syntax issues identified in current scope
1. Legacy scalar `add_autonomy_ratio` syntax in multiple national focus files.
2. Legacy `portrait_path` usage in character definition files.
3. Prior lint script did not guard against either recurrence class.

### Structure and maintainability findings
- AOTA has strong breadth and modular ambition but still carries patch-era syntax debt in older batches.
- Existing regression tooling is useful but needed expansion to cover known parser hotspots.

### AI/gating/reference concerns in this pass
- No new AI logic rewrites were required for these parser-class fixes.
- Focus/event/character key references were preserved; fixes were schema-form only.

---

## D. Gap analysis

### Already up to benchmark in touched scope
- Content organization by major HOI4 system categories exists.
- Existing static lint workflow exists and was extensible.

### Fell short in touched scope
- Non-canonical parser-sensitive syntax remained in production files.
- Regression coverage was incomplete for known recurring syntax classes.

### Needed hardening (executed)
- Canonicalized autonomy effect syntax in focus trees.
- Canonicalized character portrait schema in character files.
- Added lint enforcement for both patterns.

---

## E. Execution plan summary

### Phase order used
1. Re-extract standards baseline from existing Kaiserreich benchmark material.
2. Full-mod pattern scan with newest log correlation.
3. Execute parser-hardening fixes in highest-confidence recurring classes.
4. Expand regression lint to enforce new standards.
5. Validate and report with explicit residual-risk listing.

### Why this order
- Parser correctness and hard failures were prioritized ahead of softer style cleanup.
- Global anti-pattern classes were fixed before documenting follow-on manual/lore-sensitive work.

---

## F. Full fix log

### Cluster 1: Legacy autonomy effect syntax
- **Issue:** `add_autonomy_ratio` used scalar syntax, matching historical parser complaints.
- **Affected systems/files:** Colonial and related focus trees in `common/national_focus/` (14 total replacements).
- **Change:** Replaced scalar form with canonical object form.
- **Standards alignment:** Matches strict parser-safe effect structure used in mature large mods.
- **Resolution status:** **Resolved** for current detected occurrences.

### Cluster 2: Legacy character portrait schema
- **Issue:** Character files still used legacy `portrait_path` entries.
- **Affected files:** `common/characters/AOTA_v10_characters.txt`, `common/characters/AOTA_v13_characters.txt`.
- **Change:** Migrated to `portraits = { civilian = { large = "..." } }` schema while preserving existing asset references.
- **Standards alignment:** Uses modern, explicit character portrait structure for compatibility and maintainability.
- **Resolution status:** **Resolved** for current detected occurrences.

### Cluster 3: Regression-prevention gap
- **Issue:** Static lint did not block recurrence of the two syntax classes above.
- **Affected files:** `version_history/error_logs/parsed/aota_static_lint.py`.
- **Change:** Added checks for scalar `add_autonomy_ratio` and `portrait_path` token usage.
- **Standards alignment:** Mirrors professional large-mod discipline by institutionalizing recurring parser fixes.
- **Resolution status:** **Resolved**.

---

## G. Structural and standards improvements

### Syntax discipline improvements
- Canonicalized autonomy effect forms in focus rewards.
- Canonicalized portrait definition structure in character files.

### Anti-pattern removals
- Removed two recurring legacy parser-risk token classes from active files.

### Branch/gating improvements
- No branch semantics were altered; syntax-safe execution preserved existing gating intent.

### Localisation/reference hygiene improvements
- Key references were preserved; no key deletions or renames introduced.

### AI support improvements
- No direct AI logic rewrites in this execution window.

### Maintainability improvements
- Expanded static lint coverage to prevent regressions in newly-fixed parser-risk classes.

---

## H. Issues not fully resolved

1. **Historical long-tail parser debt (manual/batch follow-up needed)**
   - Remaining historical log clusters include old idea modifier token compatibility and other archival syntax debt not fully in current execution scope.
   - **Type:** Technical debt; mostly non-lore-sensitive.
   - **Recommended next step:** Run a focused “idea modifier modernization” batch with engine-version token validation map.

2. **Large one-line script formatting in many files**
   - Reduces readability and diff safety.
   - **Type:** Maintainability quality issue.
   - **Recommended next step:** Country-by-country multiline normalization without semantic edits.

3. **Kaiserreich source parity re-parse limitation**
   - KR full source tree unavailable in this workspace for direct fresh full parse.
   - **Type:** Environment/reference limitation.
   - **Recommended next step:** Re-run standards extraction against a local KR checkout for direct side-by-side rule sampling.

---

## I. Files changed
- `common/national_focus/AOTA_ALG.txt`
- `common/national_focus/AOTA_AST.txt`
- `common/national_focus/AOTA_CAN.txt`
- `common/national_focus/AOTA_COG.txt`
- `common/national_focus/AOTA_EGY.txt`
- `common/national_focus/AOTA_INS.txt`
- `common/national_focus/AOTA_MAL.txt`
- `common/national_focus/AOTA_NZL.txt`
- `common/national_focus/AOTA_RAJ.txt`
- `common/national_focus/AOTA_SAF.txt`
- `common/national_focus/AOTA_SER.txt`
- `common/characters/AOTA_v10_characters.txt`
- `common/characters/AOTA_v13_characters.txt`
- `version_history/error_logs/parsed/aota_static_lint.py`

---

## J. Validation notes
- Static lint passed after changes.
- Targeted grep checks confirm removal of scalar `add_autonomy_ratio` and `portrait_path` in touched scopes.
- Braces integrity quick-check passed across `.txt` script files.

---

## K. Final readiness assessment
This repass materially improves AOTA’s parser reliability and scripting hygiene in high-impact recurring failure classes and adds enforceable anti-regression controls. AOTA is closer to Kaiserreich-level technical discipline in touched systems, but a further multi-batch standards pass (ideas token modernization, one-line file normalization, and direct KR source-side comparative extraction) is still needed for full parity.
