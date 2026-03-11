# AOTA National Spirit Audit (Full-Mod Pass)

## Executive summary

### Scope audited
- National spirit definitions in `common/ideas/`.
- Spirit grants/removals in `history/countries/`, `common/national_focus/`, `events/`, `common/decisions/`, `common/on_actions/`, and `common/scripted_effects/`.
- Coverage includes 41 country history setups plus active focus/event spirit systems (including CHI/PRC/CUB path content and US splinter trees).

### High-level findings
- **Healthy starting load (0–3 spirits):** Most countries, especially minors, are currently in a readable range at game start.
- **Excessive starting load:** **FRA (6), GER (6), ENG (5), SOV (5)** are overloaded at day-1 compared to most tags.
- **Excessive path accumulation risk:** **ENG, TUR, SOV, GER, FRA, USA, CUB** accumulate many branch-added spirits; TUR/ENG are the clearest bloat risks.
- **Likely spirit-layering overperformance:** **ENG/TUR/SOV/GER** are most at risk from additive stacking rather than from one clearly intentional keystone mechanic.
- **Major redundancy/bloat patterns:**
  - multiple parallel “pressure/crisis/reconstruction” spirits without clean evolution/retirement,
  - branch reward style that keeps adding permanent micro-buffs,
  - low usage of timed spirits and low removal frequency in some trees.
- **Technical concerns:** 10 idea definitions appear unused/legacy; several transitional concepts are represented by permanent ideas with limited cleanup logic.

### Biggest global design concerns
1. **Permanent additive layering dominates pacing** in major trees.
2. **Too many micro-identity spirits** in some routes weakens readability.
3. **Escalation systems are good, but unevenly integrated** with branch cleanup (some countries evolve cleanly, others just accumulate).
4. **Minor-country identity is generally clean** and should remain the baseline target.

---

## Method and data snapshots

### Starting spirit counts (history setup)
- Highest starts: **FRA 6, GER 6, ENG 5, SOV 5**.
- Mid starts: **AUS/BEL/ITA/USA/JAP = 3**, **POL/SER/SPR/YUG = 2**.
- Most others: **0–1**.

### Path-add pressure by focus content (unique `add_ideas` in country focus files)
- **ENG ~47**, **TUR ~23**, **GER ~13**, **USA ~11**, **FRA ~10**, **SOV ~10**, **CUB ~13**.
- This is an upper bound (includes mutually exclusive branches), but it still signals high additive design density.

### Removal/evolution hygiene
- Some trees have clear staged replacement patterns (notably escalation systems).
- Other heavy trees rely on many permanent additions with comparatively less retirement/evolution.

---

## Country-by-country spirit review

Legend: **Healthy / High / Bloated** indicates readability + likely gameplay impact, not raw count only.

| Country | Start count | Projected major-path load | Load | Key concerns | Identity clarity | Recommended action |
|---|---:|---:|---|---|---|---|
| ACC | 0 | 4–6 | Healthy | Splinter-route additive buffs; check branch cleanup. | Clear | Keep; minor merge pass later. |
| ACG | 0 | 4–5 | Healthy | Similar to ACC; mostly acceptable. | Clear | Keep as is. |
| ALG | 1 | 1–2 | Healthy | No major stacking observed. | Clear | Keep as is. |
| ANA | 0 | 5–7 | High | Splinter layering can over-reward route completion. | Mostly clear | Merge 1–2 economy/political micro-spirits. |
| APF | 0 | 3–4 | Healthy | Limited accumulation. | Clear | Keep as is. |
| ASL | 0 | 3–4 | Healthy | Limited accumulation. | Clear | Keep as is. |
| AST | 0 | 0–1 | Healthy | Very light spirit profile. | Clear | Keep as is. |
| AUS | 3 | 4–6 | High | Starts heavy for a mid-depth country; crisis layering can crowd identity. | Mixed | Merge Danubian strain concepts into staged chain. |
| AWU | 0 | 5–7 | High | Splinter route can stack several parallel ideological/economic buffs. | Mixed | Make route spirits mutually exclusive and tiered. |
| BEL | 3 | 3–5 | High (start) | Day-1 load is high for minor depth. | Clear-ish | Consolidate start identity into 2 stronger keystones. |
| BUL | 1 | 1–2 | Healthy | Limited stacking. | Clear | Keep as is. |
| CAN | 1 | 1–2 | Healthy | Limited stacking. | Clear | Keep as is. |
| CCW | 0 | 3–5 | Healthy | Some branch overlap risk. | Clear | Keep; minor exclusivity cleanup. |
| COG | 1 | 1–2 | Healthy | No major stacking observed. | Clear | Keep as is. |
| EGY | 1 | 1–2 | Healthy | No major stacking observed. | Clear | Keep as is. |
| ENG | 5 | 10–16 practical (very high upper bound in file) | **Bloated** | Strong additive branch design, many permanent micro-buffs, crisis + route stacks, readability overload. | Blurry in midgame | Merge route-specific economic/admin spirits; convert some to timed transitional effects; enforce stricter exclusivity. |
| FIN | 1 | 1–2 | Healthy | Limited accumulation. | Clear | Keep as is. |
| FRA | 6 | 8–12 | **Bloated (start-high + path-high)** | Heavy day-1 stack plus social breakdown/rearmament layers; overlapping instability-war mobilization narratives. | Moderate | Merge start pressures into fewer keystones; evolve breakdown spirits by stage replacement only. |
| GER | 6 | 9–13 | **Bloated (start-high + path-high)** | Ascendancy/reckoning/colonial + escalation + route buffs can over-stack political/military tempo. | Moderate | Merge political-economic “order” spirits; gate later buffs behind cleanup/removal of early pressure spirits. |
| GRE | 1 | 1–2 | Healthy | Limited accumulation. | Clear | Keep as is. |
| HOL | 1 | 1–2 | Healthy | Limited accumulation. | Clear | Keep as is. |
| HUN | 1 | 1–2 | Healthy | Limited accumulation. | Clear | Keep as is. |
| INS | 0 | 0–1 | Healthy | Very light profile. | Clear | Keep as is. |
| IRE | 1 | 1–2 | Healthy | Limited accumulation. | Clear | Keep as is. |
| ITA | 3 | 4–7 | High | Start stack + escalation pressure + route adds can crowd role definition. | Moderate | Convert part of pressure into timed/decision-managed modifier chain. |
| JAP | 3 | 4–6 | High | Strong start trio; path additions limited but efficient. | Clear | Keep mostly; small numerical tuning only if needed. |
| LIT | 1 | 1–2 | Healthy | Limited accumulation. | Clear | Keep as is. |
| MAL | 1 | 1–2 | Healthy | Inherits imperial pressure flavor cleanly. | Clear | Keep as is. |
| NZL | 0 | 0–1 | Healthy | Very light profile. | Clear | Keep as is. |
| POL | 2 | 2–4 | Healthy | Moderate start; not bloated. | Clear | Keep as is. |
| POR | 1 | 1–3 | Healthy | Limited accumulation. | Clear | Keep as is. |
| PRC* | n/a start file in sample | 3–6 | High (path) | Warlord/unification stacks need strict conversion logic. | Moderate | Use evolving chain spirits over additive branching. |
| RAJ | 1 | 1–3 | Healthy | Limited accumulation. | Clear | Keep as is. |
| ROM | 1 | 1–3 | Healthy | Limited accumulation. | Clear | Keep as is. |
| SAF | 1 | 1–2 | Healthy | No major stacking observed. | Clear | Keep as is. |
| SER | 2 | 2–4 | Healthy | Moderate start, no severe bloat. | Clear | Keep as is. |
| SOV | 5 | 8–13 | **Bloated** | Reconstruction + fragility + path ideology layers can simultaneously buff and penalize too many axes. | Moderate | Convert reconstruction/pressure to explicit stage swaps; cap concurrent macro buffs. |
| SPR | 2 | 3–5 | Healthy/High | Manageable but can clutter if breakdown chain persists. | Clear | Ensure breakdown stages always replace, not stack. |
| TUR | 1 | 10–15 practical (very high upper bound in file/events) | **Bloated** | Very high path idea density, many permanent route adds, event + focus layering; strongest clutter risk. | Blurry in late-midgame | Major consolidation pass: ideological sets mutually exclusive, merge military/economic micro-ideas into tiered keystones, time-limit transitional order spirits. |
| UKR | 1 | 1–3 | Healthy | Limited accumulation. | Clear | Keep as is. |
| USA | 3 | 7–11 | High/Bloated by branch | Constitutional breakdown + splinter outcomes + ideology stacks can spike power variance via layering. | Moderate | Force stronger exclusivity and staged replacement across collapse/recovery spirits. |
| YUG | 2 | 2–4 | Healthy | Moderate pressure profile. | Clear | Keep as is. |
| CHI* | n/a start file in sample | 5–9 | High | Rework + warlord + unification systems can generate layered path residue. | Moderate | Add strict retirement hooks when unification state changes. |
| CUB* | n/a start file in sample | 8–13 | **Bloated (path)** | Large number of corporate-state spirits creates strong flavor but heavy mechanical noise. | Thematically strong, mechanically noisy | Merge corporate/legal/economic micro-ideas into 3–4 larger doctrine spirits. |

\* CHI/PRC/CUB are included from focus/event systems where they have active spirit content despite not being represented in the same 41 history-country start snapshot.

---

## Most problematic spirit combinations

1. **ENG imperial restoration stacks**: exhaustion/overstretch baselines + route-added economic/logistics/intel/colonial spirits create broad-spectrum efficiency gains with high UI clutter.
2. **TUR restoration-path layering**: political regime spirits + military reorganization + reconstruction + regional control spirits often coexist as permanent effects.
3. **SOV reconstruction + ideological route stacks**: simultaneous structural penalties and multiple modernization/political route bonuses can produce swingy but overtuned late-midgame states.
4. **GER pressure + order + expansion economy stacks**: risk of compounding PP/industry/war tempo through many small additive modifiers.
5. **USA crisis/collapse/reconstitution layering**: staged breakdown is good design, but when combined with branch ideology spirits can produce too many persistent modifiers.
6. **CUB corporate-state chain**: strong flavor but too many narrow permanent spirits competing to express the same core national condition.

---

## Design recommendations

### 1) Safe consolidation opportunities
- Merge parallel micro-ideas by domain into country keystones:
  - **ENG**: administrative/commonwealth/economic micro-spirits → 2–3 route keystones.
  - **TUR**: military modernization sub-spirits → one tiered “Imperial Reorganization” chain.
  - **CUB**: contract-law/economic-security cluster → 3 doctrine packages.
- Keep all lore concepts through descriptions and unlock text, but reduce simultaneous modifiers.

### 2) Power reductions (without deleting flavor)
- Trim broad-spectrum stacks (economy + military + stability in the same window).
- Reduce additive efficiency where countries already have strong focus rewards, advisors, or laws.
- Prioritize reducing passive always-on bonuses over one-time rewards.

### 3) Timing / transition fixes
- Convert transitional crisis/reconstruction spirits into **timed or staged swap chains**.
- Require upgrade/downgrade replacement rather than additive coexistence.
- Add retirement events/focus hooks when entering mature regime states.

### 4) Mutual exclusivity recommendations
- Enforce stronger route exclusivity for **ENG/TUR/USA/SOV/CUB** where ideology/state model should lock out alternatives.
- Use explicit `mutually_exclusive` and cleanup effects (remove old route spirits on branch lock-in).

### 5) Clarity / UX improvements
- Target **3–6 active long-term spirits** as a readability band for most tags.
- Move narrow situational mechanics into decisions or timed event modifiers.
- Keep spirit bar focused on identity-defining conditions, not every policy instrument.

### 6) Lore-expression improvements
- Replace “many tiny lore spirits” with fewer stronger spirits that have richer descriptions and visible progression.
- Preserve arc structure (collapse → struggle → consolidation) through staged idea evolution.

---

## Technical notes

### Broken/suspicious logic and maintenance risks
- No undefined idea references were detected in grant/remove/has_idea scans.
- Several escalation chains correctly swap Stage 1 → Stage 2 ideas (good pattern).
- Heavy-tree maintenance risk: many permanent adds with comparatively fewer removal hooks.

### Unused/legacy ideas detected (candidate manual review)
- `aota_ottoman_free_communes`
- `aota_german_constitutional_cabinet`
- `aota_german_reconstruction_front`
- `aota_french_republican_union`
- `aota_french_black_front`
- `aota_armed_neutrality`
- `aota_danubian_claimant`
- `aota_belgian_burgundian_gamble`
- `aota_polish_intermarium_dream`
- `aota_serbian_black_march`

### Missing removal/evolution logic (design concern, not syntax error)
- Some “crisis/reconstruction/emergency” concepts are implemented as permanent spirits and should be reviewed for timed/staged evolution.

---

## Implementation actions taken in this pass
- Completed full spirit audit and saved this report.
- No automatic balance edits were applied in this pass because the highest-impact changes (merges/exclusivity/timing) are design-sensitive and should be implemented in a focused follow-up patch per country cluster (ENG/TUR/SOV/GER first).

## Follow-up implementation (anti-overload hotfix)

This follow-up applies low-risk structural cleanup to reduce major-country spirit overload while preserving flavor:

- **Starting-load trims (majors):**
  - ENG: removed `aota_african_garrison_crisis` from gamestart.
  - FRA: removed `aota_fra_metropole_colony_bargain` from gamestart.
  - GER: removed `aota_ger_reichsverband_cartels` from gamestart.
  - SOV: removed `aota_sov_reconstruction_compacts` from gamestart.
  - USA: removed `aota_retreating_hegemon` from gamestart.

- **Timed transitional conversions:**
  - ENG focus `ENG_imp_colonial_garrisons`: `aota_african_garrison_crisis` is now timed (720 days).
  - ENG focus `ENG_imp_imperial_emergency_powers`: `aota_imperial_emergency` is now timed (540 days).
  - TUR event `aota.2100` options now grant timed ideas (720 days):
    - `aota_ottoman_provincial_negotiations`
    - `aota_ottoman_arab_unrest`

Net effect: majors retain narrative identity but carry fewer permanent background spirits and fewer indefinitely stacking transitional pressures.
