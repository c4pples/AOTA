# Country Presence Resolution — Implemented

## A. Executive summary

- Total undercovered countries processed from `country_presence_resolution_plan`: **51**.
- Countries annexed/absorbed: **2** (`AFA` into `ETH`, `TAN` into `SOV`).
- Countries subordinated/clientized: **11** (`BHU`, `BRM`, `ICE`, `IRQ`, `KUW`, `NEP`, `OMA`, `PHI`, `SER`, `SYR`, `YEM`).
- Countries kept with minimum viable content package: **19** (`ALG`, `BEL`, `BUL`, `COG`, `EGY`, `ETH`, `GXC`, `MAN`, `MEN`, `PER`, `POR`, `SAU`, `SHX`, `SIA`, `SIK`, `SPR`, `XSM`, `YUN`, `VEN`).
- Countries kept as constrained background states: **18** (`BOL`, `CHL`, `COL`, `COS`, `DOM`, `ECU`, `ELS`, `GUA`, `HAI`, `HON`, `LIB`, `MON`, `NIC`, `PAN`, `PAR`, `PRU`, `URG`, `TIB`).
- Manual review cases remaining: **1** (`AFG`, explicitly constrained and flagged for future expansion decision).
- Biggest structural change made: the full plan was operationalized directly in start-state country setup through one guarded resolution pipeline (`AOTA_country_presence_resolved`) that performs absorption, subject setup, role-appropriate idea assignment, anti-chaos diplomacy limits, and content package activation.

## B. Country-by-country implementation log

### Absorbed
- `AFA`: unsupported micro-tag -> **absorbed** into `ETH` via start-state integration effect; retained future regional identity potential by keeping the solution in script (can be reversed in future event content without map surgery).
- `TAN`: unsupported Siberian edge actor -> **absorbed** into `SOV` via start-state integration effect to stabilize northern pacing.

### Subordinated/clientized
- `BHU`, `NEP`, `BRM`: unsupported independent edge actors -> **RAJ puppet ring** with `can_create_factions = no` and subordinate administration spirit.
- `ICE`: unsupported sovereign behavior risk -> **DEN dependency** with constrained diplomacy.
- `PHI`: unsupported free actor risk -> **USA dominion-tier dependency** with subordinate behavior lock.
- `SER`: from unstable independent behavior -> **AUS puppet-state formalization** with anti-wildcard constraints.
- `IRQ`, `SYR`, `KUW`, `OMA`, `YEM`: unsupported Middle East free actors -> **TUR provincial/protectorate client architecture** with constrained strategic profile.

### Retained with minimum viable content
- `ALG`, `BEL`, `BUL`, `COG`, `EGY`, `ETH`, `PER`, `POR`, `SAU`, `SIA`, `SPR`, `VEN`: assigned `aota_minimum_viable_statecraft`, flagged for statecraft decision category, and given startup consolidation event support.
- China frontier tags `GXC`, `MAN`, `MEN`, `SHX`, `SIK`, `XSM`, `YUN`: assigned `aota_frontier_realignment_authority`, flagged into the same minimum-viable governance path with specialized frontier spirit.

### Constrained background states
- `BOL`, `CHL`, `COL`, `COS`, `DOM`, `ECU`, `ELS`, `GUA`, `HAI`, `HON`, `LIB`, `MON`, `NIC`, `PAN`, `PAR`, `PRU`, `URG`, `TIB`: assigned a common passive-role package (`aota_limited_strategic_bandwidth`), faction creation lock, and a dedicated low-interference decision category.

### Manual-review handling
- `AFG`: assigned `aota_buffer_state_neutrality`, faction lock, and manual-review flag to keep corridor logic stable while preserving room for a future Persia-India expansion pass.

## C. Annexation / absorption changes

- `ETH` now annexes `AFA` during start-state setup if both exist.
- `SOV` now annexes `TAN` during start-state setup if both exist.
- Effects are guarded and idempotent under global flag `AOTA_country_presence_resolved` to prevent duplicate execution.

## D. Minimum viable content packages added

Implemented as reusable systems rather than empty placeholders:

- New country spirits:
  - `aota_minimum_viable_statecraft`
  - `aota_frontier_realignment_authority`
- Startup event support for kept-active tags (`aota_country_presence.2`).
- New “Regional Statecraft Program” decision category:
  - `AOTA_presence_regional_compact`
  - `AOTA_presence_internal_security_reform`
  - `AOTA_presence_limited_rearmament`

Intended gameplay role: active but bounded regional participation without allowing unsupported snowball outcomes.

## E. Constrained background-state handling

Implemented for the full passive set through:

- Spirit: `aota_limited_strategic_bandwidth`.
- Rule lock: `can_create_factions = no`.
- Role flag: `AOTA_presence_background_state`.
- Flavor + posture event: `aota_country_presence.3`.
- Dedicated “Background Stability Measures” decision category:
  - `AOTA_presence_reaffirm_neutrality`
  - `AOTA_presence_border_patrol_protocols`

Outcome: retained map texture with reduced war-driving and diplomatic chaos potential.

## F. Technical notes

### Files changed
- `common/on_actions/AOTA_on_actions.txt`
- `history/countries/GER - Germany.txt`
- `common/scripted_effects/AOTA_country_presence_resolution_effects.txt` (new)
- `events/AOTA_country_presence_resolution_events.txt` (new)
- `common/ideas/AOTA_country_presence_resolution_ideas.txt` (new)
- `common/decisions/AOTA_country_presence_resolution_decisions.txt` (new)
- `localisation/english/AOTA_country_presence_resolution_l_english.yml` (new)
- `version_history/reports/country_presence_resolution_implemented.md` (new)

### Validation checks performed
- Script parse-oriented smoke checks (file-level syntax sanity and structural review).
- Coverage check against the full undercovered list from the resolution plan.
- One-shot guard flag present to prevent duplicate start-state mutation.

### Remaining manual review items
- `AFG` long-arc branching (strict passive buffer vs expanded corridor actor) remains intentionally deferred and flagged in-script.

## G. Final status check

- “Present but unsupported” countries from the plan are now all assigned a deterministic role bucket at startup: absorbed, subordinated, minimum-viable active, constrained passive, or explicit manual-review constrained.
- No plan-listed undercovered country is left in unresolved free-actor limbo after start-state execution.
