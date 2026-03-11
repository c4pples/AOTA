# Major Nations Name/Color Flavor Pass (Lore-Bible Grounded)

## A. Executive summary

### Major nations reviewed
- Germany (GER)
- France (FRA)
- Britain (ENG)
- Austria-Hungary / Danubia (AUS)
- Russia (SOV + RUS cosmetics)
- Ottoman Empire (TUR + OTT cosmetics)
- Italy (ITA)
- United States (USA)
- Japan (JAP)

### Change totals
- **Default names changed:** 17 key overrides
- **Adjectives changed/added:** 20 key overrides/additions
- **Cosmetic tags/names expanded:** RUS and OTT families normalized with missing adjective coverage and full path identities
- **Base colors changed:** 9 major tags now have explicit AOTA palette overrides
- **Dynamic/path identity additions:** RUS path name support completed; Ottoman and existing major cosmetics now have adjective/DEF support where missing

### Flavor philosophy used
- Follow canon baseline: the world is an unstable post-armistice order where major states are **institutional projects under stress**, not meme states.
- Preserve existing path structure and content; only identity presentation was corrected or strengthened.
- Prefer color choices that communicate geopolitical identity while staying readable against neighboring majors and existing AOTA atmosphere.

---

## B. Major-by-major review

## Germany (GER)
- **Previous presentation:** Democratic and fascist variants read somewhat generic relative to lore’s constitutional bargaining + coercive revisionism framing.
- **Changes made:**
  - Democratic renamed to **German Constitutional Commonwealth**.
  - Fascist renamed to **German National Directorate**.
  - Communist punctuation normalized to **Workers' Federation**.
  - Added DEF/ADJ support for existing major cosmetic lines (constitutional and sacred variants).
- **Lore rationale:** Emphasizes legal-institutional legitimacy struggle and directorate logic described in canon.
- **Color rationale:** Base gray retained in spirit but tuned for higher readability and easier contrast versus France/Britain.
- **Type:** Default + path-supporting localization.

## France (FRA)
- **Previous presentation:** Neutrality name (**French Communal State**) did not match canon emphasis on republican legality vs disciplinarian security-state competition.
- **Changes made:**
  - Neutrality renamed to **French State**.
  - Communist renamed to **French Workers' Republic**.
  - Added full loc support for **FRA_christian_communes** cosmetic identity.
- **Lore rationale:** Better tracks state-legitimacy conflict and social fracture language in the bible.
- **Color rationale:** Blue retained but deepened for stronger metropole identity and map separation from Danubian and Russian palettes.
- **Type:** Default + path cosmetic support.

## Britain (ENG)
- **Previous presentation:** Start name was acceptable, but fascist naming under-signaled regime form.
- **Changes made:**
  - ENG democratic DEF normalized to include article form.
  - Fascist renamed to **British National Authority**.
  - Existing hope-path cosmetic adjective adjusted for clearer diplomatic text output.
- **Lore rationale:** Reflects committee-state continuity at start and authoritarian emergency trajectory on villain turns.
- **Color rationale:** Maintains red imperial identity with readable UI gold-tinted contrast.
- **Type:** Default + path loc refinement.

## Austria-Hungary / Danubia (AUS)
- **Previous presentation:** Danubian naming was broadly aligned, but adjective at game-start underplayed explicit imperial identity.
- **Changes made:**
  - Neutrality adjective changed to **Austro-Hungarian**.
  - Democratic route refined to **Danubian Constitutional Federation**.
  - Added DEF/ADJ support for Danubian federation cosmetic usage.
- **Lore rationale:** Better distinguishes start empire from post-reform federal constitutional project.
- **Color rationale:** Lavender family retained and softened for multiethnic imperial readability.
- **Type:** Default + path loc support.

## Russia (SOV + RUS cosmetics)
- **Previous presentation:** Default ideology names were partially serviceable, but dynamic RUS cosmetic tags lacked localization coverage.
- **Changes made:**
  - Neutrality renamed to **Russian Provisional State**.
  - Fascist renamed to **Russian National Union State**.
  - Added complete localization (name/DEF/ADJ) for:
    - RUS_republic
    - RUS_restoration
    - RUS_workers_republic
    - RUS_free_territories
    - RUS_national_union
- **Lore rationale:** Canon explicitly frames Russia as unfinished statehood with rival reconsolidation myths; path names now communicate that.
- **Color rationale:** Base slate-blue/steel tone supports “unfinished center” identity and separates from GER/AUS.
- **Type:** Default + major dynamic-path completion.

## Ottoman Empire (TUR + OTT)
- **Previous presentation:** Tag-level defaults risked vanilla Turkey framing despite lore requiring Ottoman continuity at game start.
- **Changes made:**
  - Added full TUR ideology naming set centered on Ottoman continuity (including constitutional, imperial, and workers variants).
  - Added missing OTT adjective support for base and path cosmetics.
- **Lore rationale:** Canon unambiguously identifies the Ottoman Empire as a surviving major with multiple legitimacy formulas.
- **Color rationale:** Base deep maroon chosen to signal imperial continuity while staying distinct from ENG and FRA.
- **Type:** Start identity correction + path adjective completion.

## Italy (ITA)
- **Previous presentation:** Mostly aligned; fascist label read too republican for AOTA’s directorate-heavy emergency grammar.
- **Changes made:**
  - Fascist renamed to **Italian National Directorate**.
- **Lore rationale:** Better reflects militarized corporative command trajectories.
- **Color rationale:** Green retained but tuned toward muted strategic palette aligned with Mediterranean system tone.
- **Type:** Default refinement.

## United States (USA)
- **Previous presentation:** Baseline was close, but fascist variant could more clearly reflect authority-state framing.
- **Changes made:**
  - Fascist renamed to **American National Authority**.
  - Added DEF/ADJ support for corporate commonwealth cosmetic identity.
- **Lore rationale:** Fits canon line that rival projects claim “true America” via competing sovereign forms.
- **Color rationale:** Federal blue strengthened for readability against Canada/Atlantic and to preserve recognition.
- **Type:** Default + path loc refinement.

## Japan (JAP)
- **Previous presentation:** Relied heavily on vanilla defaults rather than AOTA-specific framing.
- **Changes made:**
  - Added full JAP ideology naming set emphasizing imperial continuity, commercial-statist variants, and militarized directorate path identity.
- **Lore rationale:** Canon positions Japan as imperial center balancing diplomatic commerce and expansionist officer-business blocs.
- **Color rationale:** Earth-toned imperial palette chosen for distinction from China/Russia while retaining East Asian readability.
- **Type:** Default identity expansion.

---

## C. Dynamic identity additions

### New/expanded cosmetic name coverage
- Added complete localization bundles for all major Russian consolidation outcomes (`RUS_*`).
- Added missing adjective support for Ottoman cosmetic branches (`OTT_*`).
- Added DEF/ADJ completion for several active major cosmetic tags used by decisions/focuses.

### New path-based names
- Russia path names now explicitly communicate restoration, republican, workers, and free-territory outcomes.
- Germany/France/Italy/USA authoritarian labels were tightened where old names under-signaled regime form.

### New path-based colors
- No new trigger-gated recolor scripts were added in this pass.
- Existing path-color systems were preserved.
- Major base-map readability was improved via explicit tag color overrides.

### Trigger logic used
- Existing focus/event/decision `set_cosmetic_tag` logic was preserved.
- This pass provides localization and base presentation alignment; it does not alter path unlock scripts.

---

## D. Technical notes

### Files changed
- `localisation/english/AOTA_v50_major_identity_l_english.yml` (new)
- `common/countries/AOTA_major_colors.txt` (new)

### Localisation added
- Major-country default names/adjectives for lore alignment.
- Missing `RUS_*` and `OTT_*` dynamic cosmetic support.
- Additional DEF/ADJ support for active major cosmetic tags.

### Cosmetic logic added
- No new set_cosmetic_tag triggers required.
- Existing cosmetic-tag references were integrated by supplying missing loc coverage.

### Remaining manual review items
- In-game map test should confirm final visual separation in crowded Europe (GER/FRA/AUS/ENG overlap zones).
- If desired in a follow-up, villain/hope branches could receive one additional color step at consolidation moments (kept out here to avoid over-recoloring).
