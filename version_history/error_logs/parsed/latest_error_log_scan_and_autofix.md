# HOI4 Error Log Scan + Safe Auto-fix (latest pass)

## A. Executive summary
- **Newest logs scanned:** `version_history/error_logs/raw/error.log` (mtime: 2026-03-12 14:56:57 UTC).
- **Major issue clusters identified:** 8
- **Safe fixes applied automatically:** 10
- **Top remaining blockers:**
  1. Large volume of `Unknown modifier` / `Unknown effect-type` in idea/focus files (likely version/schema mismatch across many files).
  2. Ideology DB-id duplication from redefining vanilla ideologies in `common/ideologies/AOTA_ideologies.txt`.
  3. Character ideologies/subtypes that are not valid in current ruleset.

## B. Hard blockers found
1. **Parser break in localisation file** (`Expected colon`) caused by a non-ASCII key token in `AOTA_l_english.yml`.
2. **Malformed state history tokens** in five state files where `manpower` and `buildings_max_level_factor` were collapsed into one invalid token.
3. **Decision-file root structure errors** (`Unknown category`, `Unexpected token: decision`) from invalid top-level decision schema in CUB/ENG/RUS/TUR/China-Japan decision files.
4. **Country alias invalid tag** (`ALGX`) and alias duplication issues around Ottoman alias definitions.

## C. Major errors found
- **Decision schema issues**: files used `decision_categories`/`decisions` roots or detached category blocks incompatible with the active parser behavior seen in this mod setup.
- **Tag alias integrity issues**: invalid alias key and duplicate Ottoman alias definition generated repeated parser noise.
- **State parser syntax issues**: malformed inline assignment chains in state files produced recurring malformed token errors.
- **Localisation tokenization issue**: diacritic in key name caused YAML-like parser failure.
- **Non-auto-fixed broad compatibility noise**: many unknown modifiers/effects/triggers likely tied to HOI4 version differences or systemic ruleset drift.

## D. Safe fixes applied

### 1) Repaired malformed state history entries (5 files)
- **Issue:** `manpower=buildings_max_level_factor=...` invalid syntax.
- **Files:**
  - `history/states/471-Northwestern Canada.txt`
  - `history/states/472-Northwest Territories.txt`
  - `history/states/644-state 3.txt`
  - `history/states/876-Udachny.txt`
  - `history/states/967-Deep Amazonas.txt`
- **Change:** split into two valid keys: `manpower = 0` and `buildings_max_level_factor = 1/1.000`.
- **Why safe:** strictly parser-level repair; no ownership/core/lore change.
- **Confidence:** High.

### 2) Fixed malformed localisation key token
- **Issue:** parser error on key `SPR_guard_the_pyrénées`.
- **File:** `localisation/english/AOTA_l_english.yml`
- **Change:** renamed key to ASCII-safe `SPR_guard_the_pyrenees`.
- **Why safe:** keeps displayed text intact; only resolves key-token validity.
- **Confidence:** High.

### 3) Removed invalid alias tag block
- **Issue:** `invalid alias tag ALGX`.
- **File:** `common/country_tag_aliases/AOTA_country_tag_aliases.txt`
- **Change:** removed `ALGX` alias block.
- **Why safe:** invalid alias cannot function; removal reduces parser errors without affecting valid tags.
- **Confidence:** High.

### 4) Removed duplicate Ottoman alias file
- **Issue:** duplicate DB id for `OTT` alias.
- **File removed:** `common/country_tag_aliases/AOTA_ottoman_aliases.txt`
- **Change:** deleted redundant file defining `OTT = TUR` that overlapped with broader alias configuration.
- **Why safe:** duplicate definition is parser-noise and conflict source; canonical alias remains in the main alias file.
- **Confidence:** High.

### 5) Repaired decision schema in CUB decisions
- **Issue:** category defined twice/detached, causing unknown category errors.
- **File:** `common/decisions/AOTA_CUB_decisions.txt`
- **Change:** migrated to `categories = { ... }` structure with in-category `decision = { id = ... }` block.
- **Why safe:** structural parser fix only; preserves original decision logic/effects.
- **Confidence:** High.

### 6) Repaired decision root key in ENG overhaul decisions
- **Issue:** root used `decision_categories` leading to parser rejection in this mod's schema.
- **File:** `common/decisions/AOTA_ENG_overhaul_decisions.txt`
- **Change:** changed root to `categories = { ... }`.
- **Why safe:** consistent with other working mod decision files.
- **Confidence:** High.

### 7) Repaired RUS decisions schema and category attachment
- **Issue:** mixed `decision_categories` + detached `decisions` root caused all decisions to be ignored.
- **File:** `common/decisions/AOTA_RUS_decisions.txt`
- **Change:** rebuilt file into `categories` with decisions attached to relevant categories (`reunification`, `red_black`, `borderlands`).
- **Why safe:** preserves all original decision content while restoring parse validity.
- **Confidence:** Medium-High.

### 8) Repaired TUR decisions schema
- **Issue:** categories declared without valid root; decisions emitted as unexpected tokens.
- **File:** `common/decisions/AOTA_TUR_decisions.txt`
- **Change:** wrapped categories in `categories = { ... }` and normalized `decision = { id = ... }` blocks.
- **Why safe:** parser/structure-only normalization.
- **Confidence:** High.

### 9) Repaired China-Japan decisions root schema
- **Issue:** category file lacked root wrapper and was treated as unknown category.
- **File:** `common/decisions/AOTA_china_japan_interaction_decisions.txt`
- **Change:** wrapped existing category under `categories = { ... }`.
- **Why safe:** no gameplay redesign; structural validity fix.
- **Confidence:** High.

## E. Issues not auto-fixed
1. **`Unknown modifier` across many idea files**
   - **Why not auto-fixed:** high ambiguity whether intended modifiers are from another game version, custom script layer, or typos.
   - **Next step:** run a version-aware modifier audit and map each invalid key to supported equivalents.
2. **`Unknown effect-type` across many focus files**
   - **Why not auto-fixed:** can require broad mechanical translation (`add_army_experience` vs other canonical forms) and may alter balance.
   - **Next step:** batch-validate focus effects against current HOI4 script reference.
3. **Ideology duplicate DB ids in `AOTA_ideologies.txt`**
   - **Why not auto-fixed:** potentially foundational design choice (overriding base ideologies) with many downstream dependencies.
   - **Next step:** redesign as additive custom ideologies/subtypes or fully replace with explicit compatibility framework.
4. **Character subtype/ideology validity errors**
   - **Why not auto-fixed:** may require coordination with ideology definitions and character progression content.
   - **Next step:** align character ideology tokens to valid ideology/subtype keys after ideology audit.

## F. Likely noise / low-priority warnings
- One-off parser complaints from external/user `settings.txt` are outside mod content.
- Repeated duplicates of the same root parser errors (decision schema, malformed state token, alias duplication) were deduplicated and addressed where safe.

## G. Files changed
- `history/states/471-Northwestern Canada.txt`
- `history/states/472-Northwest Territories.txt`
- `history/states/644-state 3.txt`
- `history/states/876-Udachny.txt`
- `history/states/967-Deep Amazonas.txt`
- `localisation/english/AOTA_l_english.yml`
- `common/country_tag_aliases/AOTA_country_tag_aliases.txt`
- `common/country_tag_aliases/AOTA_ottoman_aliases.txt` (removed)
- `common/decisions/AOTA_CUB_decisions.txt`
- `common/decisions/AOTA_ENG_overhaul_decisions.txt`
- `common/decisions/AOTA_RUS_decisions.txt`
- `common/decisions/AOTA_TUR_decisions.txt`
- `common/decisions/AOTA_china_japan_interaction_decisions.txt`

## H. Top priority remaining work
1. Global idea-modifier compatibility pass.
2. Global focus-effect compatibility pass.
3. Ideology architecture cleanup to eliminate duplicate DB IDs.
4. Character ideology token cleanup after ideology pass.
5. Re-run game with fresh logs and confirm parser-error reduction delta.
