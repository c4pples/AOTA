# Duplicate State Ownership Fixes Implemented (AOTA)

## A. Executive summary

- **Total audit findings addressed in this pass:** 29
  - **Duplicate owner issues fixed:** 25 (all repeated same-tag owner reassertions listed in the audit’s B1 section).
  - **Duplicate controller issues fixed:** 0 (none of the audit’s controller findings were identical duplicates; they were timeline/controller progressions and were left intact).
  - **Duplicate state-definition issues fixed:** 0 (audit confirmed none existed).
  - **Duplicate/contradictory core issues fixed:** 4 (duplicate `add_core_of = KUR` entries in 350/352/353/800).
  - **Startup ownership-conflict issues fixed:** 0 (audit identified no definite startup ownership-conflict blocker).
- **Remaining manual review items:** 3 clusters (timeline-heavy ownership/core transitions, state 746 controller chronology, USA fracture branch mapping overlap).

## B. State-by-state fix log

### Duplicate owner cleanup (same-tag reassertions)

For each state below, duplicate same-tag `owner` entries in dated blocks were removed to keep one coherent owner definition while preserving dated controller/core content and lore setup.

- **1032 – Yanan**
  - Issue: repeated `owner = PRC`.
  - Files: `history/states/1032 - Yanan.txt`.
  - Change: removed dated duplicate owner line (`1938.10.25`).
  - Why: no-op duplicate; baseline owner already defines state ownership.
  - Status: resolved.

- **1037 – Chongqing**
- **1038 – Jinan**
- **1039 – Hebei-Chahar**
- **1041 – Chengdu**
- **1042 – Khotan**
- **152 – Upper Austria**
- **153 – Tyrol**
- **287 – Sinkiang**
- **4 – Austria**
- **597 – Shandong**
- **605 – China 5**
- **608 – Beijing**
- **614 – China 13**
- **69 – Sudatenland**
- **70 – Slovakia**
- **71 – East Slovakia**
- **73 – Carpathian Ruthenia**
- **74 – East Sudatenland**
- **744 – Xian**
- **75 – Moravia**
- **751 – Liangshan**
- **752 – Chamdo**
- **759 – Kunlun**
- **9 – Czechoslovakia**
  - Issue: repeated same-tag owner assignment in state history file.
  - Files: corresponding `history/states/<id>-*.txt` file.
  - Change: removed redundant dated `owner` reassertion while retaining dated event/timeline logic.
  - Why: conservative de-duplication with no border/lore redesign.
  - Status: resolved.

### Duplicate core cleanup (KUR duplicates)

- **350 – Diyarbekir**
- **352 – Hakkari**
- **353 – Erzurum**
- **800 – Van**
  - Issue: duplicate `add_core_of = KUR` via DLC split blocks.
  - Files: `history/states/350-Diyarbekir.txt`, `history/states/352-Hakkari.txt`, `history/states/353-Erzurum.txt`, `history/states/800-Van.txt`.
  - Change: consolidated to one unconditional `add_core_of = KUR`; preserved non-DLC `add_core_of = TUR` path.
  - Why: removes duplicate core assignment while preserving intended vanilla/BftB compatibility behavior.
  - Status: resolved.

## C. Startup/system logic fixes

- No startup system rewrites were required.
- No `on_actions`, bookmark, event startup stack ownership conflicts were found that needed intervention in this pass.
- Branch-dependent ownership changes (including USA fracture branches) were preserved unchanged pending design-level manual confirmation.

## D. Remaining ambiguous cases

1. **China-region timeline core churn (21-state set from audit)**
   - Left unchanged because transitions appear timeline-intent driven and not a confirmed technical duplicate bug.
2. **State 746 controller chronology (`JAP -> MEN`)**
   - Left for manual review due to possible intentional wartime progression.
3. **USA fracture branch ownership overlap (`aota.201` vs `aota.202`)**
   - Left unchanged because branch routing appears mutually exclusive and likely intentional.

## E. Technical notes

- **Files changed:** 29 state history files under `history/states/` plus this report.
- **Validation notes:**
  - Re-ran duplicate scan for `owner`, `controller`, and repeated `add_core_of`; no remaining repeated same-file duplicates found.
  - No new state IDs or transfer references were introduced.
- **Remaining risk:** primarily design-intent ambiguity in timeline branches, not parser-format duplication.
