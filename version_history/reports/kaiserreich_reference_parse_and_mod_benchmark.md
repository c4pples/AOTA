# Kaiserreich Reference Parse and AOTA Benchmark (HOI4 Structure/Scripting)

## A. Executive summary

### What was learned from Kaiserreich as a benchmark
Kaiserreich demonstrates a mature large-mod pattern built around:
- strict namespace discipline for events,
- modular split by country/system across `common/*`, `events/*`, and localisation folders,
- predictable trigger/effect reuse through scripted triggers/effects,
- explicit AI-facing logic (`ai_will_do`, AI scripted triggers/plans),
- decision/focus gating that avoids contradictory path states,
- and consistent relation between script keys and localisation keys.

### Biggest practical standards extracted
1. **Parser-safe syntax beats clever compacting**: avoid malformed wrappers and avoid unsupported trigger scopes in restricted blocks.
2. **Branch integrity is explicit**: gate by prerequisite + mutually exclusive + visibility + one-time flags.
3. **AI support is first-class**: every meaningful branch/decision has explicit AI pathing logic.
4. **Cross-system coherence is deliberate**: focus/event/decision/idea/character keys are joined by stable IDs and scripted helpers.
5. **Maintainability comes from structure, not just content quality**: files are split by domain/country and named for discoverability.

### Biggest weaknesses found in AOTA versus that standard
Using newest raw logs as source-of-truth plus previous parsed logs as historical context, recurring weak points were:
- malformed/invalid `country_tag_aliases` schema,
- decision category schema instability tied to restricted-token misuse in `allowed` blocks,
- invalid legacy event effects (`become_subject`, `add_opinion`),
- duplicate ideology DB collisions due base+mod ideology load overlap,
- and recurrent parser errors concentrated in decisions/events integration hotspots.

### Biggest fixes applied in this pass
- normalized aliases to parser-safe `ALIAS = TAG` form,
- removed unsafe `allowed` blocks from dynamic decision categories and kept gating in `visible/available`,
- replaced invalid diplomacy effect usage (`add_opinion`) with opinion modifiers,
- removed invalid `become_subject` effect while retaining valid autonomy assignment,
- added `replace_path = "common/ideologies"` to descriptor files to prevent ideology DB duplication in mixed-load contexts.

---

## B. Kaiserreich-derived HOI4 standards

### 1) Repository and file structure
**Observed KR patterns:**
- country/system-specific files under `common/national_focus`, `common/decisions`, `events`, `common/scripted_triggers`, `common/scripted_effects`.
- broad, explicit directory taxonomy under `common/*` (AI, diplomacy, mechanics, content systems).
- localisation split into domain-specific files/folders, not monolithic dumps.

**Actionable standard for AOTA:**
- keep country-specific content segmented by file and avoid overloading single files with unrelated systems,
- continue using system-focused folders (`common/scripted_effects`, `common/scripted_triggers`, `common/opinion_modifiers`) and tie new mechanics to those rather than embedding repeated inline logic.

### 2) Scripting syntax and safety
**Observed KR patterns:**
- event files use explicit namespace declarations (`add_namespace`) and consistent event IDs.
- decisions rely on valid category structure and legal trigger scopes in `allowed`, with dynamic gating mostly in `visible/available`.
- effects use current valid API primitives and avoid deprecated aliases.

**Actionable standard for AOTA:**
- use `visible`/`available` for dynamic state checks and keep `allowed` conservative,
- avoid deprecated/invalid effects and migrate to supported equivalents (`add_opinion_modifier`, valid autonomy effects),
- keep one parser-safe object model per file type.

### 3) Branch/ideology gating quality
**Observed KR patterns:**
- parallel branch discipline: prerequisites + exclusivity + state flags + ai weights.
- branch lock-ins are explicit, avoiding dead paths and contradictory unlock states.

**Actionable standard for AOTA:**
- every ideological branch should include clear lock/entry conditions and explicit mutual exclusion or cancellation points,
- branch follow-up decisions/events should reference the same canonical country flags.

### 4) AI support patterns
**Observed KR patterns:**
- scripted AI triggers centralize complex selection logic,
- `ai_will_do` blocks are present at focus/decision level, often with modifiers tied to game state.

**Actionable standard for AOTA:**
- preserve and expand AI weights where content branches diverge,
- push repeated AI eligibility logic into scripted triggers for consistency and easier refactors.

### 5) Localisation/reference hygiene
**Observed KR patterns:**
- localization keys are scoped and grouped by content domain,
- parser-sensitive YAML format is consistent,
- script keys and localisation keys track each other tightly.

**Actionable standard for AOTA:**
- keep key naming predictable (`aota_*`, country prefixes),
- prevent orphan keys by matching newly added decisions/events/focuses with localisation entries in the same pass.

### 6) Character/idea/diplomacy integration
**Observed KR patterns:**
- character/idea effects are integrated into focus and event outcomes with stable IDs,
- diplomacy relies on opinion modifiers and clear effect chains.

**Actionable standard for AOTA:**
- avoid ad-hoc direct relation mutations that are version-unstable,
- prefer defined opinion modifiers and scripted helper effects to keep behavior reusable and debuggable.

### 7) Validation-minded maintainability
**Observed KR patterns:**
- large systems are split into manageable units and commented/sectioned,
- repeated logic is extracted to scripted triggers/effects,
- parser-invalid constructs are aggressively avoided.

**Actionable standard for AOTA:**
- prioritize parser stability and schema correctness before balance/content additions,
- treat every recurring log error as a system smell requiring root-cause elimination, not per-instance patching.

---

## C. Anti-patterns to avoid
1. Invalid schema wrappers or object models in decision/event files.
2. Unsupported tokens in restricted trigger contexts (especially category `allowed` misuse).
3. Legacy/invalid effects that silently fail and desync intended design (`become_subject`, direct invalid opinion effects).
4. Duplicate database IDs from partial overwrite without `replace_path` or equivalent load strategy.
5. One-line mega-definitions for complex events (hard to audit, easier to break).
6. Repeating AI logic inline across dozens of files instead of scripted trigger centralization.
7. Adding content without synchronizing localisation and references.

---

## D. Benchmark comparison against this mod

### Where AOTA is already strong
- Broad system coverage across major HOI4 content planes (focuses, ideas, decisions, characters, AI strategy).
- Strong thematic country flavor depth and bespoke systems.
- Existing use of scripted triggers/effects and opinion modifiers indicates good architectural intent.

### Where AOTA falls short vs benchmark
- Parser-sensitive files still contain historical schema drift and version-mismatch patterns.
- Some decision categories were using unsafe `allowed` token patterns.
- Event API usage included known-invalid effects from logs.
- Ideology loading collided with base IDs without explicit replacement guard.

### Where cleanup/hardening was needed most
- `common/country_tag_aliases`
- high-traffic decision category files (China unification/presence/systems)
- diplomacy-heavy events (Ottoman and China unification event chains)
- launcher descriptor integration for ideology override strategy

### Recurring hotspot pattern from historical logs
Old and new parsed logs repeatedly pointed to the same classes of faults:
- decision parser cascades from category schema/gating mistakes,
- invalid effect/modifier tokens in older script segments,
- duplicated DB entities where overwrite strategy was ambiguous.
This indicates not isolated typos, but repeatable integration-pattern debt.

---

## E. Fixes applied to this mod

1. **Country tag alias parser hardening**
- File: `common/country_tag_aliases/AOTA_country_tag_aliases.txt`
- Change: switched to parser-safe alias assignments (`ALIAS = TAG`).
- Why aligned: avoids trigger-parser misread and matches practical large-mod schema expectations.

2. **Decision category gating hardening**
- Files:
  - `common/decisions/AOTA_china_unification_decisions.txt`
  - `common/decisions/AOTA_country_presence_resolution_decisions.txt`
  - `common/decisions/AOTA_systems.txt`
- Change: removed risky `allowed` blocks for dynamic conditions; preserved behavior through `visible/available` conditions.
- Why aligned: keeps category schema stable and reduces parser rejection for unsupported allowed-scope tokens.

3. **Diplomacy/event effect modernization**
- Files:
  - `events/AOTA_china_unification_events.txt`
  - `events/AOTA_TUR_events.txt`
  - `common/opinion_modifiers/AOTA_ottoman_opinions.txt`
- Change:
  - removed invalid `become_subject` effects while retaining valid `set_autonomy` outcomes,
  - replaced invalid direct opinion mutation with `add_opinion_modifier` and a dedicated modifier (`aota_ottoman_war_alarm`).
- Why aligned: uses current stable effect patterns and keeps diplomacy behavior explicit and reusable.

4. **Ideology DB collision prevention**
- Files:
  - `descriptor.mod`
  - `AOTA.mod`
- Change: added `replace_path = "common/ideologies"`.
- Why aligned: explicit overwrite strategy prevents duplicate ideology DB collisions in base+mod load.

---

## F. Remaining recommended work

### Must-fix next
1. **Legacy idea modifiers cleanup**: map each unknown modifier to current HOI4-valid equivalents.
2. **Decision parser full re-validation**: run log pass after this patch and verify category errors collapsed.
3. **Duplicate character/entity checks**: resolve any remaining duplicate character tags and ID collisions.

### Strongly recommended
1. Expand scripted trigger library for repeated branch-gating logic.
2. Reformat remaining one-line event files into multiline sections for maintainability and review safety.
3. Add a lightweight static lint script in `version_history/error_logs/parsed` workflow for repeated regression checks.

### Optional polish
1. Country-by-country localisation namespace normalization pass.
2. Add internal contributor guidelines for file naming, event ID ranges, and branch gating policy.
3. Periodic AI weight audits for newly added branches.
