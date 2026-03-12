# AOTA Map Modification Audit

## A. Executive summary

- **Direct map file edits (`map/`, map bitmaps, strategic regions, supply areas):** **No** direct map files are present in this mod package.
- **State/territorial setup edits:** **Yes**. The mod fully overrides `history/states` (via `replace_path`) and includes 1,046 state files.
- **Indirect scripted map-behavior edits:** **Yes**. Events, scripted effects, and some focus trees include state transfer, core/claim manipulation, annexation, release/splinter logic, autonomy/puppet setup, and wargoal generation.
- **Largest risk areas:**
  1. `replace_path = "history/states"` is high impact and can break map/state coherence if any state file is missing or malformed.
  2. Heavy scripted US splinter/transfer logic in `events/AOTA_events.txt`.
  3. Dynamic `transfer_state_to` and `remove_core_of` usage in multiple China/Congo-related state history files.

## B. Direct map files found

### Result

No direct map-generation/geography assets were found in the mod root tree for these targets:

- `map/`
- `map/definition.csv`
- `map/default.map`
- `map/adjacencies.csv`
- `map/continent.txt`
- `map/strategicregions/`
- `map/supplyareas/`
- terrain/province/height/rivers map files

### Interpretation

- AOTA does **not** directly edit province geometry, map raster data, adjacency topology, strategic regions, or supply area files through a shipped `map/` folder.
- The playable territorial experience is instead altered through state history replacement and scripts.

## C. State / territorial setup changes

### C1) Global replacement behavior

Both mod descriptors include:

- `replace_path = "history/states"`

Implication: the game uses AOTA's state history directory instead of vanilla. This is a full override strategy, not additive merge.

### C2) State history coverage and territorial fields

- `history/states/` contains **1,046** state files.
- Territorial/state-shaping fields detected across state files:
  - `owner =` (1078 occurrences)
  - `controller =` (125)
  - `add_core_of =` (1586)
  - `remove_core_of =` (28)
  - `add_claim_by =` (48)
  - `remove_claim_by =` (5)
  - `transfer_state_to =` (24)
  - `set_demilitarized_zone =` (13)
  - `impassable = yes` (19 files)

These are direct territorial setup changes (state-level ownership/core/claim/control configuration).

### C3) Country setup implications

- `history/countries/` has 42 country history files with `capital =` definitions (including custom tags such as ACC/AWU/ANA/APF/ACG/ASL/CCW).
- `common/country_tags/` defines additional tags (US splinter tags + other added tags), and `common/countries/` includes corresponding country definitions/colors.

This means the territorial setup includes new playable entities and capitals that interact with state ownership and scripted partition logic.

## D. Indirect map-changing scripted content

### D1) Events

#### `events/AOTA_events.txt`

Contains direct map-territory effects:

- `release =` (US splinter releases)
- many `transfer_state = TAG`
- many `add_core_of = TAG`
- `set_capital =` for splinter tags
- `declare_war_on = { ... type = annex_everything }`
- one `add_claim_by = ITA`

This is high-impact dynamic territorial repartition logic.

#### `events/AOTA_china_unification_events.txt`

Contains `set_autonomy =` effects affecting sovereignty status (indirect territorial/political map behavior).

### D2) Scripted effects

#### `common/scripted_effects/AOTA_country_presence_resolution_effects.txt`

Contains:

- `annex_country = { ... }` (2)
- `set_autonomy = { ... }` (11)

These alter sovereignty control relationships and can reshape political map outcomes.

### D3) Focus trees

Detected territorial-pressure logic in focus files via `create_wargoal = { type = take_state_focus ... }`:

- `common/national_focus/AOTA_ARG.txt`
- `common/national_focus/AOTA_BRA.txt`
- `common/national_focus/AOTA_DEN.txt`
- `common/national_focus/AOTA_NOR.txt`
- `common/national_focus/AOTA_SOV.txt`
- `common/national_focus/AOTA_SWE.txt`

These are indirect map-affecting changes (future conquest pathing), not immediate start-map edits.

### D4) Not found in this pass

No direct `set_owner` / `set_controller` scripted effects were found in scanned scripted content folders (outside of state history files).

## E. Replace path findings

Relevant `replace_path` entries:

- `replace_path = "history/states"` (**map-critical**)
- `replace_path = "common/ideologies"` (non-map, but broad DB replacement)

No `replace_path` for:

- `map`
- `map/strategicregions`
- `map/supplyareas`
- `history/countries`

Implications:

- No direct map file override.
- State history is fully replaced and therefore drives most map-behavior divergence.

## F. Risk notes

### Likely safe / coherent

- Strategy appears intentional: no direct map raster edits, but broad state-history rewrite and scripted territorial systems.
- Custom tags + country files + capitals exist to support scripted partitions.

### Potentially risky

1. **Full `history/states` replace-path coupling**
   - Missing/invalid state files can cause desyncs, parser issues, or unexpected missing states.
2. **State-script interaction complexity**
   - `transfer_state_to` and `remove_core_of` in several files (notably China/Congo areas) require careful ordering and compatibility with events/focuses.
3. **Large scripted partition chains**
   - US-splinter event blocks repeatedly transfer/corify states and trigger wars; high chance of logic regressions if tags/cores/states drift.

### Potential conflict points (mod compatibility)

- Any other mod touching `history/states` is very likely to conflict due to AOTA replace-path strategy.
- Other mods that alter US splinter tags, China warlords, or Congo-related tags can conflict with scripted transfer logic.

### Manual review items recommended

- Validate all referenced state IDs used in scripted transfers exist and are owned as expected at trigger time.
- Confirm no missing vanilla states under replace-path coverage.
- Run parser + observe early game event chains for US split and China/Congo transitions.

---

## Audit method notes

- File-system pass across repository tree for direct map assets and target directories.
- Pattern scan across events/focus/decisions/scripted_effects/scripted_triggers/on_actions for territorial effects.
- State-history keyword census for ownership/core/claim/controller/DMZ/impassable/transfer usage.


## G. Concrete validation checklist (focus: Risk #1 `replace_path = "history/states"`)

Use this as an actionable QA sequence to validate that full state-history replacement is coherent and safe.

### G1) File coverage and naming integrity

- [ ] Confirm `history/states/` exists and is populated with expected scale.
  - Command: `find history/states -maxdepth 1 -type f | wc -l`
- [ ] Ensure each file has a numeric state ID prefix and no obvious naming anomalies.
  - Command: `find history/states -maxdepth 1 -type f -printf '%f\n' | rg -n -v '^[0-9]+.*\.txt$'`
- [ ] Detect duplicate numeric IDs in filenames (possible overwrite/ambiguity risk).
  - Command: `find history/states -maxdepth 1 -type f -printf '%f\n' | sed -E 's/^([0-9]+).*/\1/' | sort | uniq -d`

### G2) Internal state-file schema sanity

- [ ] Every state file should contain key blocks/fields (`state = {`, `id =`, `history =`, `provinces =`).
  - Command: `python - <<'PY'
import os,re
missing=[]
for fn in os.listdir('history/states'):
    fp=os.path.join('history/states',fn)
    if not os.path.isfile(fp):
        continue
    t=open(fp,encoding='utf-8-sig',errors='ignore').read()
    req=[r'\bstate\s*=\s*\{',r'\bid\s*=\s*\d+',r'\bhistory\s*=\s*\{',r'\bprovinces\s*=\s*\{']
    bad=[r for r in req if not re.search(r,t)]
    if bad: missing.append((fn,bad))
print('files_missing_required_blocks=',len(missing))
for m in missing[:50]: print(m)
PY`
- [ ] Verify state IDs inside files match filename prefixes.
  - Command: `python - <<'PY'
import os,re
m=[]
for fn in os.listdir('history/states'):
    fp=os.path.join('history/states',fn)
    if not os.path.isfile(fp):
        continue
    mfn=re.match(r'(\d+)',fn)
    if not mfn: continue
    t=open(fp,encoding='utf-8-sig',errors='ignore').read()
    mid=re.search(r'\bid\s*=\s*(\d+)',t)
    if not mid or mid.group(1)!=mfn.group(1):
        m.append((fn, mid.group(1) if mid else None))
print('id_mismatches=',len(m))
for x in m[:50]: print(x)
PY`

### G3) Territorial data consistency checks

- [ ] Flag state files missing a baseline owner assignment in history.
  - Command: `python - <<'PY'
import os,re
miss=[]
for fn in os.listdir('history/states'):
    fp=os.path.join('history/states',fn)
    if not os.path.isfile(fp): continue
    t=open(fp,encoding='utf-8-sig',errors='ignore').read()
    if 'history' in t and not re.search(r'\bhistory\s*=\s*\{[\s\S]*?\bowner\s*=\s*\w+',t):
        miss.append(fn)
print('missing_owner=',len(miss))
for x in miss[:50]: print(x)
PY`
- [ ] Review states using `transfer_state_to` / `remove_core_of` for date/condition correctness.
  - Command: `rg -n '\b(transfer_state_to|remove_core_of)\b' history/states`
- [ ] Review any `set_demilitarized_zone` and `impassable = yes` states for intended design.
  - Command: `rg -n '\b(set_demilitarized_zone|impassable\s*=\s*yes)\b' history/states`

### G4) Script-to-state reference integrity

- [ ] Extract all numeric state IDs referenced in scripted transfers/events and verify corresponding state files exist.
  - Command: `python - <<'PY'
import re,glob,os
files=glob.glob('events/*.txt')+glob.glob('common/**/*.txt',recursive=True)
ids=set()
for fp in files:
    t=open(fp,encoding='utf-8-sig',errors='ignore').read()
    for m in re.finditer(r'(^|\s)(\d+)\s*=\s*\{[^}]*\b(transfer_state|add_core_of|add_claim_by)\b',t,re.M):
        ids.add(int(m.group(2)))
missing=[]
for sid in sorted(ids):
    pref=f'{sid}-'
    ok=any(os.path.isfile(os.path.join('history/states',f)) and f.startswith(pref) for f in os.listdir('history/states'))
    if not ok: missing.append(sid)
print('script_referenced_state_ids=',len(ids))
print('missing_state_files_for_script_ids=',len(missing))
print('missing_ids_sample=',missing[:100])
PY`
- [ ] Confirm all scripted country tags used in map-changing effects are defined in `common/country_tags/`.
  - Command: `rg -n '\b(release|transfer_state|add_core_of|set_capital|set_autonomy|annex_country)\b' events common/scripted_effects | head -n 200`

### G5) Replace-path compatibility and conflict checks

- [ ] Confirm replace-path declarations are identical in both mod descriptors.
  - Command: `diff -u descriptor.mod AOTA.mod`
- [ ] Check for other map-critical replace paths that could amplify conflicts.
  - Command: `rg -n 'replace_path' descriptor.mod AOTA.mod`

### G6) Runtime/parse validation (manual in-game)

- [ ] Launch with AOTA only, verify no startup parser/map errors.
  - Check: `error.log` contains no state-history parse failures.
- [ ] Observe first 30 in-game days for scripted territorial chains (US split, China/Congo transitions) and verify no orphan states/tags.
- [ ] Trigger known map-changing events/focuses and confirm ownership/core changes apply to existing valid states.

### G7) Release gate recommendation

Treat build as **map-safe** only if all are true:

1. No missing/duplicate/mismatched state IDs.
2. No required-block omissions in state files.
3. No unresolved scripted references to non-existent states/tags.
4. No parser errors tied to `history/states` under AOTA-only load.
5. No unintended territorial regressions in first-month scripted flows.
