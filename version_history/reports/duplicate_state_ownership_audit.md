# Duplicate State Ownership Audit (AOTA)

## A. Executive summary

- **Total states audited:** 1046 (`history/states/*.txt`).
- **Total duplicate owner issues:** 57
  - 25 repeated `owner = <same_tag>` entries in the same file.
  - 32 multi-owner timelines in the same file (`owner` changes by date block).
- **Total duplicate controller issues:** 2
  - 0 repeated identical `controller` entries.
  - 2 multi-controller timelines in the same file.
- **Total duplicate/contradictory core issues:** 25
  - 4 repeated `add_core_of` entries.
  - 21 states where the same tag is both added and removed as core in one file (across dated blocks).
- **Total duplicate state-definition issues:** 0
  - No duplicate state IDs.
  - No duplicated state files defining the same `id`.
  - No missing IDs found in state-scope numeric ownership transfer references.
- **Total startup ownership-conflict issues:** 0 definite startup blockers.
  - One **non-startup branch divergence cluster** in USA fracture events (mutually exclusive, but messy).

### Biggest risks found

1. **Parser/lore maintenance risk (not immediate launch blocker):** many state files use layered date-history ownership/core transitions that look contradictory in a flat grep but are likely intentional timeline data.
2. **Potential gameplay intent mismatch:** USA fracture events (`aota.201` and `aota.202`) transfer overlapping states under different successor tags; this is probably intentional branch design, but the overlap is dense and should be manually verified.
3. **Data hygiene risk:** some files contain duplicate no-op ownership/core assignments (same tag repeated), which can hide real mistakes during future merges.

---

## B. Duplicate owner/controller findings

## B1. Repeated owner assignment (same tag repeated in one state file)

These are mostly harmless no-op duplicates caused by dated blocks reasserting the same owner:

- 1032 (Yanan): `PRC` repeated.
- 1037 (Chongqing): `CHI` repeated.
- 1038 (Jinan): `CHI` repeated.
- 1039 (Hebei-Chahar): `CHI` repeated.
- 1041 (Chengdu): `CHI` repeated.
- 1042 (Khotan): `SIK` repeated.
- 152 (Upper Austria): `AUS` repeated.
- 153 (Tyrol): `AUS` repeated.
- 287 (Sinkiang): `SIK` repeated.
- 4 (Austria): `AUS` repeated.
- 597 (Shandong): `CHI` repeated.
- 605 (China 5): `CHI` repeated.
- 608 (Beijing): `CHI` repeated.
- 614 (China 13): `CHI` repeated.
- 69 (Sudatenland): `AUS` repeated.
- 70 (Slovakia): `AUS` repeated.
- 71 (East Slovakia): `AUS` repeated.
- 73 (Carpathian Ruthenia): `AUS` repeated.
- 74 (East Sudatenland): `AUS` repeated.
- 744 (Xian): `CHI` repeated.
- 75 (Moravia): `AUS` repeated.
- 751 (Liangshan): `CHI` repeated.
- 752 (Chamdo): `CHI` repeated.
- 759 (Kunlun): `SIK` repeated.
- 9 (Czechoslovakia): `AUS` repeated.

**Severity:** mostly **harmless** (cleanup recommended).

## B2. Multi-owner timelines inside a single state file

States with ownership changing by date block (likely timeline-intent data, but flagged as contradictory in static audit):

- 1033 Fangchenggang: `GXC -> CHI`
- 188 Memel: `LIT -> GER`
- 271 Ethiopia: `ETH -> ITA`
- 283 China: `XSM -> CHI`
- 44 Albania: `ALB -> ITA`
- 591 Hainan: `GXC -> CHI`
- 592 Guangzhou: `GXC -> CHI`
- 593 Guangdong: `GXC -> CHI`
- 615 Shanxi: `SHX -> PRC`
- 621 China 18: `SHX -> PRC`
- 664 Southern Slovakia: `AUS -> HUN`
- 72 Zaolzie: `AUS -> POL`
- 746 Ordos: `SHX -> PRC`
- 753 Gannan: `XSM -> CHI`
- 799 Hatay: `SYR -> TUR`
- 805 Northern Epirus: `ALB -> ITA`
- 835 Haraghe: `ETH -> ITA`
- 836 Bale: `ETH -> ITA`
- 837 Sidamo: `ETH -> ITA`
- 838 Illubabor: `ETH -> ITA`
- 839 Welega: `ETH -> ITA`
- 840 Gojjam: `ETH -> ITA`
- 841 Begemder: `ETH -> ITA`
- 842 Tigray: `ETH -> ITA`
- 843 Wello: `ETH -> ITA`
- 848 Voralberg: `AUS -> GER`
- 908 Afar: `AFA -> ITA`
- 934 Shkoder: `ALB -> ITA`
- 972 South Sudetenland: `AUS -> GER`
- 975 Burgenland: `AUS -> GER`
- 976 Steiermark Karnten: `AUS -> GER`
- 992 Province of Aden: `RAJ -> ENG`

**Severity:** mostly **intentional but messy**; no immediate parser risk seen.

## B3. Multi-controller timelines

- **State 746 (Ordos):** `controller = JAP` in one dated block, later `controller = MEN` in another dated block.
  - **Severity:** **suspicious** (likely intentional wartime progression, but review recommended for final date consistency).
- **State 972 (South Sudetenland):** `controller = AUS` baseline, later `controller = GER` at dated block.
  - **Severity:** **intentional but messy**.

---

## C. Duplicate state-definition findings

- No duplicate state IDs in `history/states`.
- No duplicate files defining the same state ID.
- No malformed state-id ownership transfer references found in scanned gameplay logic (`events`, `decisions`, `focus`, `scripted_effects`, `scripted_triggers`, `on_actions`, `history/countries`, `bookmarks`).

**Conclusion:** no duplicate-definition blockers found.

---

## D. Core/claim duplication findings

## D1. Repeated identical cores (same tag added twice)

- 350 Diyarbekir: duplicate `add_core_of = KUR`
- 352 Hakkari: duplicate `add_core_of = KUR`
- 353 Erzurum: duplicate `add_core_of = KUR`
- 800 Van: duplicate `add_core_of = KUR`

**Severity:** **harmless** duplicate data (cleanup recommended).

## D2. Core add/remove contradiction within same file (timeline-style)

21 states contain tags that are both `add_core_of` and `remove_core_of` within the same file, generally inside different dated blocks:

1033, 1037, 1040, 1041, 1042, 1044, 1045, 283, 287, 591, 592, 593, 594, 605, 616, 744, 751, 752, 753, 756, 759.

Most are China-region dynamic timeline states (warlord/core reshuffling).

**Severity:** **intentional but messy** in most cases; manual lore/gameplay consistency review advised.

## D3. Claim add/remove contradiction within same file

- 44 Albania (`ITA` claim added then removed)
- 664 Southern Slovakia (`HUN` claim added then removed)
- 73 Carpathian Ruthenia (`HUN` claim added then removed)
- 805 Northern Epirus (`ITA` claim added then removed)
- 934 Shkoder (`ITA` claim added then removed)

**Severity:** **intentional timeline** (not a parser issue).

---

## E. Startup logic conflict findings

### E1. Direct startup systems reviewed

Reviewed:
- `common/on_actions/*`
- `common/bookmarks/AOTA_bookmark.txt`
- ownership-changing logic in `events`, `common/scripted_effects`, `common/national_focus`, `common/decisions`.

### E2. Results

- **No direct on-startup ownership transfer conflicts** found.
- `on_startup` blocks mostly queue intro/escalation events and ideas, not state ownership rewrites.
- Bookmark is standard 1936 setup and does not layer conflicting ownership scripts itself.

### E3. Near-start/gameplay branch ownership cluster (manual review)

- `aota.200` routes to either `aota.201` or `aota.202` (mutually exclusive branch), both performing heavy `transfer_state` + `add_core_of` operations for US splinter tags.
- Overlapping states are assigned differently between the two branches (e.g., 364/365/366 are transferred to **ASL** in one branch and **ANA** in the other).
- Because routing is exclusive, this is not an immediate duplicate-execution conflict, but **design intent should be manually validated**.

**Severity:** **suspicious but likely intentional branch logic**.

---

## F. Final recommendations

## Safe as-is

- No duplicate state IDs.
- No conflicting startup ownership rewrite stack in on_actions/bookmark systems.
- Most owner/controller/core contradictions appear date-scoped and intentionally historical/alt-history.

## Cleanup recommended

- Remove no-op duplicate `owner` and duplicate `add_core_of` lines (especially KUR set in 350/352/353/800).
- Optionally annotate heavy timeline files with comments clarifying intended date progression.

## Likely bug

- None identified as certain from static audit alone.

## Likely launch/parser risk

- None identified as definite blockers.

## Manual review needed

1. China-region states with frequent add/remove core churn (21-state set listed above).
2. State 746 controller progression (`JAP` then `MEN`) and ownership progression (`SHX` to `PRC`) for intended chronology.
3. USA fracture branch ownership mappings (`aota.201` vs `aota.202`) to ensure overlap is intentional and balanced.

---

## Audit method (for reproducibility)

- Parsed all `history/states/*.txt` for `id`, `owner`, `controller`, `add_core_of`, `remove_core_of`, `add_claim_by`, `remove_claim_by`.
- Checked duplicate IDs and per-file duplicate/contradictory ownership/core/claim patterns.
- Scanned cross-systems (`history/countries`, `events`, `decisions`, `focus`, `scripted_effects`, `scripted_triggers`, `on_actions`, bookmarks) for state ownership/control operations and startup interactions.
- Validated that numeric state-scope transfer references map to existing state IDs.
