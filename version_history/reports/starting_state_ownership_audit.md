# Starting-State Ownership Audit (Game Start)

## A. Executive summary

- **UKR (Ukraine):** has a tag, history file, capital, leader, ideas, characters, and a dedicated focus tree file, but **owns 0 states and controls 0 states at start**.
- **SER (Serbia):** has a history file, capital, leader, ideas, and a loaded focus tree, but **owns 0 states and controls 0 states at start**.
- **Intent signal check:** both UKR and SER have substantial start content (country setup + events/focus/ideas), and neither has clear event logic that spawns them later. This reads as **likely inconsistent/unfinished** rather than clearly intentional stateless design.
- **Total country history tags audited:** 41 (`history/countries/*`).
- **Total stateless country-history tags:** 12.
- **Stateless tags likely intentional (event/civil-war/releasable style):** 7 (`ACC, AWU, ANA, APF, ACG, ASL, CCW`).
- **Stateless tags that look suspicious for gamestart presence:** 4 strong (`UKR, SER, EGY, ALG`) + 1 conditional/ambiguous (`COG`, DLC-gated state transfer).
- **Biggest setup inconsistencies:**
  1. UKR/SER have full political setup and capitals with no territory.
  2. EGY/ALG have developed setup (history, focus presence, ideas/characters/cores) but no owned territory.
  3. COG ownership appears tied to `has_dlc = "Gotterdammerung"` IF-blocks in state history; this creates DLC-dependent gamestart geography.

---

## B. UKR review

### Tag/status
- Defined in mod country tags: `UKR = "countries/UKR - Ukraine.txt"`.
- Has country definition/color and country history.
- Included in scripted startup pacing and minor escalation decision visibility.

### Start content
- Country history includes:
  - `capital = 418`
  - OOB (`AOTA_UKR_land`, `AOTA_UKR_air`)
  - politics setup + country leader
  - national idea (`aota_ukr_frontier_atamanates`)
  - recruited characters
- Dedicated focus tree file exists (`AOTA_UKR.txt`), though UKR history file does not explicitly `load_focus_tree`.
- UKR startup event exists and is queued via `on_startup` logic.

### Owned/controlled states at start
- **Owned:** none found in `history/states` (`owner = UKR` absent).
- **Controlled:** none found in explicit `controller = UKR` entries.
- UKR has **23 core states** in state history, but all are owned by SOV/AUS/POL/ROM at gamestart.

### Lore/setup assessment
- Lore bible frames Ukraine as a meaningful “minor worldbuilding anchor” with active internal political currents.
- In files, UKR is treated like a participating actor (events/decisions/content), not a dormant release-only shell.
- No clear release/spawn path found for UKR in events/decisions to justify permanent stateless start.

### Should UKR have gamestart states?
- **Assessment:** likely yes.
- **Most sense based on current map logic:** core heartland around Kyiv-centered states (e.g., 193/202/203/198/199/200/201 and adjacent core belt) if intended as independent minor.
- **Conservative alternative:** if intended suppressed/dormant, files should signal that more clearly (e.g., explicit occupier-subject or delayed emergence script).

### Recommended conclusion
- **Current UKR condition is likely inconsistent with intended setup** and should be reviewed for starting ownership assignment or explicit design signaling.

---

## C. SER review

### Tag/status
- SER has a country history file and dedicated focus tree (`aota_serbia_focus`, loaded in country history).
- SER appears in event trigger logic (`tag = SER` or `SER/YUG` paths).
- SER is not added in this mod’s custom tag file, implying reliance on base-game tag definitions.

### Start content
- Country history includes:
  - `capital = 107`
  - OOB (`AOTA_SER_land`, `AOTA_SER_air`)
  - stability/war support/politics setup
  - country leader setup
  - two startup ideas
  - focus tree loaded (`load_focus_tree = aota_serbia_focus`)

### Owned/controlled states at start
- **Owned:** none found (`owner = SER` absent).
- **Controlled:** none found (`controller = SER` absent).
- SER has **6 core states** (e.g., 45/107/108/764/802/803), currently owned by YUG or AUS.

### Lore/setup assessment
- SER focus tree language references active Serbian governance and military planning, indicating a functioning state actor.
- Event text hooks target SER directly, not only as a hypothetical future releasable.
- No clear scripted release path for SER in reviewed setup files.

### Should SER have gamestart states?
- **Assessment:** likely yes.
- **Most sense from current core map:** state 107 (capital) plus central Serbian core block (107/108/803 and possibly 802/764 depending intended borders).

### Recommended conclusion
- **Current SER condition likely inconsistent/unfinished** if SER is meant to be a real gamestart actor.

---

## D. Other suspicious tags

### D1) Strongly suspicious stateless tags (content-heavy, no territory)

| Tag | Content presence | States at start | Intended for gamestart? | Should likely have states? | Confidence |
|---|---|---:|---|---|---|
| EGY | Country history, capital, OOB, loaded focus tree, ideas | 0 | Appears yes (full setup) | Probably yes | **Likely mistake** |
| ALG | Country history, capital, OOB, focus file, ideas/characters | 0 | Appears yes (minor anchor content) | Probably yes (or explicit colonial subject handling) | **Likely mistake** |
| UKR | Country history, capital, events/decisions/focus/characters | 0 | Appears yes | Probably yes | **Likely mistake** |
| SER | Country history, capital, loaded focus tree, events | 0 | Appears yes | Probably yes | **Likely mistake** |

### D2) Conditional/ambiguous

| Tag | Content presence | States at start | Intended for gamestart? | Should likely have states? | Confidence |
|---|---|---:|---|---|---|
| COG | Country history, capital, focus file, ideas/characters | 0 in static owner scan; conditional transfer in states | Appears yes | **Depends on DLC branch** (`Gotterdammerung` IF transfers ownership) | **Ambiguous / manual review** |

### D3) Likely intentional stateless tags (event/collapse entities)

| Tag(s) | Why stateless seems intentional |
|---|---|
| ACC, AWU, ANA, APF, ACG, ASL, CCW | Explicitly integrated into U.S. fracture/civil-war release and transfer logic; designed as post-collapse actors rather than baseline owners. |

---

## E. State ownership consistency notes

1. **Country-history without territory pattern (12 tags):**
   - `ACC, ACG, ALG, ANA, APF, ASL, AWU, CCW, COG, EGY, SER, UKR`.
   - For U.S. splinters this is coherent with event release design; for UKR/SER/EGY/ALG it is much less coherent.

2. **Capital/territory contradictions:**
   - UKR capital set to state 418 but UKR owns none.
   - SER capital set to state 107 but SER owns none.
   - EGY capital set to 446 but Egypt states are owner `ENG`.
   - ALG capital set to 513 but Algeria states are owner `FRA`.

3. **Core-heavy but ownerless start:**
   - UKR (23 cores), SER (6 cores), EGY (8 cores), ALG (4 cores), COG (6 cores) all have core geography but no guaranteed static start ownership.

4. **DLC-dependent ownership branch (COG):**
   - Multiple Congo-region states have `owner = BEL` with `IF { has_dlc = "Gotterdammerung" transfer_state_to = COG }`.
   - This creates divergent starts depending on DLC availability.

5. **Invalid owner/controller tags:**
   - No obvious malformed custom owner/controller references were found in reviewed state files.
   - Most non-overridden owners likely rely on vanilla tag/history definitions.

---

## F. Final recommendations

### Likely correct as-is
- U.S. splinter block (`ACC/AWU/ANA/APF/ACG/ASL/CCW`) as stateless-at-start emergent entities.
- Major/minor territorial tags that already own start states.

### Likely missing starting states
- **UKR**
- **SER**
- **EGY**
- **ALG**

### Likely future/releasable/event-only tags
- **ACC, AWU, ANA, APF, ACG, ASL, CCW** (strong evidence from event release + transfer flows).

### Manual review needed
- **COG** due DLC-gated transfer behavior.
- Any intended “occupied-but-playable without land” design for UKR/SER/EGY/ALG should be explicitly documented in scripts/lore, because current setup reads as partially implemented states.

---

## Appendix: audited country-history tags and start ownership counts

- Audited set (41): `ACC, ACG, ALG, ANA, APF, ASL, AST, AUS, AWU, BEL, BUL, CAN, CCW, COG, EGY, ENG, FIN, FRA, GER, GRE, HOL, HUN, INS, IRE, ITA, JAP, LIT, MAL, NZL, POL, POR, RAJ, ROM, SAF, SER, SOV, SPR, TUR, UKR, USA, YUG`.
- Stateless subset (12): `ACC, ACG, ALG, ANA, APF, ASL, AWU, CCW, COG, EGY, SER, UKR`.
