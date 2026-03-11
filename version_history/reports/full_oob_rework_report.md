# Full OOB Rework Report

## A. Executive summary
- **Countries reviewed:** 41/41 country history files in `history/countries/`.
- **Countries reworked:** all 41 now use mod-owned land and air OOB files (`AOTA_<TAG>_land`, `AOTA_<TAG>_air`).
- **Army OOBs changed:** full pass completed across every country file.
- **Air OOBs changed:** full pass completed across every country file.
- **Naval OOBs changed:** all countries that define a naval OOB hook now use mod-owned naval files (`AOTA_<TAG>_naval`).
- **New commanders/admirals/air leaders added:** none in this implementation pass.
- **New supporting military ideas/spirits added:** none in this implementation pass.
- **Overall balance philosophy used:** asymmetrical readiness and institutional capability with country-specific force identities rooted in geography, regime type, and strategic position.

## B. Country-by-country OOB summary

### Previously custom majors retained and refined
- AUS, ENG, FRA, GER, ITA, JAP, SOV, TUR, USA keep bespoke structures from the earlier major rework: mixed readiness, uneven modernization, and doctrine-distinct army/air/navy composition.

### Newly onboarded countries now made distinct (no shared baseline model)
- **American splinters (ACC/ACG/ANA/AWU/ASL/CCW):** force structures now differentiate constitutional guard, corporate security, authority-policing, worker militia, and agrarian militia patterns.
- **European minors (BEL/BUL/FIN/GRE/HOL/HUN/LIT/POL/POR/ROM/SER/SPR/UKR/YUG/IRE):** each now has tailored mixes (fortress infantry, border cavalry, mountain guards, colonial detachments, or interior gendarmerie) tied to local geography and political posture.
- **Imperial/colonial and maritime states (AST/CAN/EGY/NZL/RAJ/SAF/MAL/INS/APF/ALG/COG):** each has region-appropriate expeditionary, coastal, desert, frontier, island, or colonial-security force balance.
- **Naval-hook countries among these** received unique task-force identities (e.g., Atlantic escort, canal defense, cape patrol, Adriatic defense) rather than generic patrol clones.

## C. Army design notes
- Land OOB ownership is fully mod-native for all tags.
- Countries added in the previous pass were rewritten away from generic templates and now have individualized template names, battalion mixes, and readiness profiles.
- Readiness remains encoded through `start_experience_factor`, `start_equipment_factor`, and `start_manpower_factor` to preserve “paper strength vs practical capability” differences.

## D. Air design notes
- Air OOB ownership is fully mod-native for all tags.
- Wing names, mission mix, and size now vary by strategic reality (home interception, frontier recon, maritime patrol, or symbolic internal-air arm).

## E. Naval design notes
- Naval hooks are normalized to mod-owned files.
- Newly onboarded naval states now have distinct role-oriented flotillas tied to their waters (Atlantic, Adriatic, canal/straits, cape, or Pacific patrol).

## F. Supporting changes
- Country history OOB pointers normalized to `AOTA_` naming for coherence and maintainability.
- This correction focused on structural and identity differentiation; no extra spirits/characters were added in this step.

## G. Technical validation
- **Files changed:** country history OOB pointers; all newly onboarded country land/air OOB files; naval OOB files for tags with naval hooks; this report.
- **Validation checks run:**
  - all countries resolve to `AOTA_<TAG>_land` and `AOTA_<TAG>_air`;
  - all referenced `AOTA_` files exist;
  - `AOTA_` naval hook references resolve;
  - brace-balance syntax sanity across `history/units/AOTA_*.txt`.
- **Remaining manual review items:** in-engine spawn location sanity and first-year AI behavior checks.

## H. Manual playtest recommendations
- Run one hands-off year focused on new minor-country OOB behavior.
- Verify each newly onboarded region presents distinct operational constraints (mountains, coasts, deserts, islands, steppe/frontier).
- Observe whether country-identity differences are felt in early wars without creating unintended runaway powers.
