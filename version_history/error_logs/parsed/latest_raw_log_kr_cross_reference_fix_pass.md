# AOTA Latest Raw Log KR Cross-Reference Fix Pass (Follow-up)

## A. Executive summary
- **Newest raw log used as source-of-truth:** `version_history/error_logs/raw/error.log`.
- **Follow-up objective from review comments:** resolve previously deferred items (custom ideology compatibility, focus construction scope errors, unknown modifier keys, duplicate character tag).
- **Additional safe fixes applied in this follow-up:**
  1. Added legacy ideology compatibility layer while preserving AOTA custom ideology set.
  2. Refactored country-scope construction rewards to state scope via `capital_scope` wrapping in AOTA focus/decision files.
  3. Normalized/remapped unknown modifier keys in AOTA idea files to valid or maintainable equivalents.
  4. Removed duplicate character tag collision by renaming AOTA-specific Chamberlain character key.

## B. Root-cause clusters and status

### 1) Custom ideology compatibility vs legacy references
- **Issue summary:** Large-volume `is not a valid ideology` / `Not a valid value` spam came from legacy ideology names used by character/scripted-localisation content.
- **Fix status:** **Fixed in this pass**.
- **Action:** Added compatibility ideologies (`marxism`, `stalinism`, `despotism`, `nazism`, `fascism_ideology`, `liberalism`, etc.) as explicit ideology entries in `common/ideologies/AOTA_ideologies.txt`, preserving existing custom AOTA ideology blocks.
- **Why safe:** Adds compatibility without deleting AOTA custom ideologies.

### 2) Focus/decision construction scope errors
- **Issue summary:** `add_building_construction` was repeatedly used in country scope and logged as invalid scope.
- **Fix status:** **Fixed in this pass**.
- **Action:** Wrapped AOTA focus/decision construction effects in `capital_scope = { add_building_construction = { ... } }`.
- **Why safe:** Enforces legal state scope and keeps original building intent.

### 3) Unknown modifier keys in idea files
- **Issue summary:** Multiple idea modifiers were unknown to current parser.
- **Fix status:** **Fixed in this pass**.
- **Action:** Replaced/remapped keys:
  - `improve_relation_modifier` → `improve_relation_factor`
  - `army_experience_gain_factor` → `experience_gain_army_factor`
  - `navy_experience_gain_factor` → `experience_gain_navy_factor`
  - `air_experience_gain_factor` → `experience_gain_air_factor`
  - `resource_gain_factor` → `local_resources_factor`
  - `entrenchment_factor` → `max_dig_in_factor`
  - `naval_base_speed_factor` → `naval_speed_factor`
  - removed unsupported `coastal_bunker_construction_speed_factor` and `operative_mission_speed_factor`
- **Why safe:** Keeps closest-equivalent gameplay intent while restoring parser-valid modifier keys.

### 4) Duplicate character tag collision
- **Issue summary:** Duplicate tag `ENG_neville_chamberlain` conflicted with existing character database content.
- **Fix status:** **Fixed in this pass**.
- **Action:** Renamed AOTA key to `AOTA_ENG_neville_chamberlain` and added matching localisation key.
- **Why safe:** Removes hard collision while retaining AOTA-specific character entry.

## C. Kaiserreich benchmark usage in follow-up
- **Pattern used:** compatibility-first scripting hygiene (explicit, structured data compatibility instead of silent removal), schema-safe effect scoping, and key normalization discipline for large mod maintenance.
- **AOTA application:**
  - explicit ideology compatibility registry
  - deterministic state-scoped building effects via consistent wrapper pattern
  - centralized modifier key normalization
  - unique character key namespace to avoid collisions

## D. Files changed in follow-up
- `common/ideologies/AOTA_ideologies.txt`
- `common/national_focus/AOTA_*.txt` (AOTA focus trees with construction rewards)
- `common/decisions/AOTA_v14_us_splinters.txt`
- `common/ideas/AOTA_ENG_overhaul_ideas.txt`
- `common/ideas/AOTA_RUS_ideas.txt`
- `common/ideas/AOTA_country_presence_resolution_ideas.txt`
- `common/ideas/AOTA_flagship_formables_ideas.txt`
- `common/ideas/AOTA_ideas.txt`
- `common/ideas/AOTA_v12_ideas.txt`
- `common/ideas/AOTA_v14_ideas.txt`
- `common/ideas/AOTA_v17_world_ideas.txt`
- `common/ideas/AOTA_v34_minor_worldbuilding_ideas.txt`
- `common/characters/AOTA_ENG_overhaul_characters.txt`
- `localisation/english/AOTA_ENG_overhaul_l_english.yml`

## E. Verification
- Static lint re-run passed (`aota_static_lint.py`).
- Post-change scan confirms removal of previously logged unknown modifier keys from AOTA idea files.
- Post-change scan confirms `add_building_construction` usage in touched AOTA focus/decision files is now wrapped with `capital_scope`.

## F. Remaining manual review
- Re-run full in-game log generation to confirm the high-volume ideology and scope warnings are eliminated in runtime context.
- Balance tuning pass may be desired after compatibility remaps (values preserved, key semantics nearest-match but not guaranteed identical to legacy behavior).
