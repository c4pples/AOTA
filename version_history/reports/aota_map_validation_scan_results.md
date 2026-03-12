# AOTA Map Validation Scan Results (Checklist Execution)

Run timestamp: 2026-03-12 19:45 UTC

## G1) File coverage and naming integrity
- State file count: **1046**
- Non-numeric/invalid filename pattern count: **0**
- Duplicate numeric filename IDs: **0**

## G2) Internal state-file schema sanity
- Files missing required blocks: **0**
- Filename ID vs internal `id` mismatches: **0**

## G3) Territorial data consistency checks
- Files with `history` but no owner assignment found: **0**
- `transfer_state_to` occurrences: **24**
- `remove_core_of` occurrences: **28**
- `set_demilitarized_zone` occurrences: **13**
- `impassable = yes` occurrences: **19**

## G4) Script-to-state reference integrity
- Script-referenced state IDs (pattern scope): **28**
- Missing state files for referenced IDs: **0**
- Distinct uppercase tokens in map-changing lines: **26** (heuristic)
- Tokens not present in `common/country_tags/*.txt`: **20** (heuristic)
- Undefined token sample: ['AFA', 'AUS', 'BHU', 'BRM', 'DEN', 'ETH', 'ICE', 'IRQ', 'KUW', 'NEP', 'OMA', 'PHI', 'RAJ', 'SER', 'SOV', 'SYR', 'TAN', 'TUR', 'USA', 'YEM']

## G5) Replace-path compatibility checks
- descriptor.mod replace_path entries: ['replace_path = "history/states"', 'replace_path = "common/ideologies"']
- AOTA.mod replace_path entries: ['replace_path = "history/states"', 'replace_path = "common/ideologies"']
- Replace-path parity: **PASS**

## Issues detected in this run
- ✅ No hard failures detected by automated checklist subset.

## Notes
- The undefined-token tag check is heuristic and intentionally noisy; vanilla tags not redefined in this mod will appear as "undefined" in this local-only check.
- Runtime parser/in-game checks (G6) are not executed in this CLI scan.
