# China Full Rework Report

## A. Executive summary
- **Countries/tags reviewed:** CHI, PRC, and Japan interaction surfaces outside the Japan focus tree.
- **Focus trees reworked:** `AOTA_CHI.txt` and `AOTA_PRC.txt` fully replaced with new structure, pacing, and route identities.
- **Events added:** `events/AOTA_china_rework_events.txt` introduces China internal crisis events, claimant path events, and Japan-reaction support events.
- **Decisions added:** `common/decisions/AOTA_china_rework_decisions.txt` adds consolidation, anti-bandit, stockpile, and Japan-pressure loops.
- **Spirits/mechanics added or reworked:** `common/ideas/AOTA_china_rework_ideas.txt` defines evolving identity mechanics for CHI and PRC paths.
- **Characters added:** `common/characters/AOTA_china_rework_characters.txt` adds regional political and military personalities for both Chinese poles.
- **Diplomacy/faction changes:** new focus and event flows create Chinese claim-competition, negotiation/detente options, and anti-imperial escalation.
- **Japan compatibility additions made:** Added Japan-targeted reaction events (`aota_china.110-113`) and decision pressure hooks without touching `AOTA_JAP.txt`.
- **Overall philosophy:** China is rebuilt as a layered, contested political system with meaningful early stabilization, midgame alignment struggles, and late-game settlement arcs.

## B. Regional diagnosis
### Weaknesses before
- CHI content was structurally misaligned (including Chile framing and low China-specific identity).
- PRC and CHI had template-like branches with shallow strategic consequences.
- China pacing was mostly linear and lacked distinct turning points.
- Japan-China interaction was minimally represented outside a narrow focus stub.

### Missing pieces
- No coherent legitimacy contest mechanics.
- Sparse provincial/warlord bargaining pressure.
- Thin event density for Chinese internal politics.
- Weak differentiation between authoritarian, constitutional, and mass paths.

### Pacing and spread issues
- Frontloaded bonuses with low midgame narrative handoff.
- Late game lacked clear culmination nodes.
- Cross-China diplomacy and JAP pressure logic lacked modular support.

### Prose/lore issues
- Descriptions were repetitive and geographically mismatched.
- Political rhetoric between paths was insufficiently distinct.

## C. Country-by-country / tag-by-tag summary

### CHI
- Rebuilt into a legitimacy-first framework: emergency council -> claimant choice -> institutional consolidation.
- Added distinct route outcomes:
  - National commission/directive state (security-statist)
  - Constitutional/federal compromise (pluralist)
  - Mass reconstruction republic (mobilizational)
- Added military spine focused on clique integration and command unification.
- Added economic spine focused on customs restoration and reconstruction bonds.
- Added diplomatic spine with anti-Japan resistance or managed financial accommodation.
- Added branch-conclusion event triggers for path atmosphere.

### PRC
- Rebuilt around revolutionary legitimacy competition and provincial congress politics.
- Added distinct route outcomes:
  - Cadre supremacy and central command
  - Coalition republican socialism
  - Peasant federal compact
- Added military reconstruction emphasizing border columns and liberation army doctrine.
- Added economic reconstruction emphasizing rail dispatch and planning institutions.
- Added diplomatic options for united-front outreach vs anti-imperial mobilization or detente.

### Japan interaction layer (outside JAP focus tree)
- Added reactive event payloads so Chinese escalatory/cooperative choices have Japanese follow-through.
- Added decision category hooks allowing Japan to pressure the Chinese theater while China can answer diplomatically.
- No edits to the Japan focus tree itself.

## D. Pacing review
- **Early game:** legitimacy crisis, provincial bargaining, and state-repair pressures established quickly with costs and tradeoffs.
- **Midgame:** ideological and institutional branch commitments create differentiated gameplay loops.
- **Late game:** each tree converges into settlement/fate nodes after military + economy + diplomacy milestones.
- **Flow improvement:** significantly higher event cadence and decision recurrence prevent content dead zones.

## E. Japan compatibility notes
- Adjustments made only through events/decisions and CHI/PRC focus outcomes.
- Existing Japan focus structure remains untouched.
- New content ensures Japanese responses exist when Chinese anti-imperial or accommodation paths are taken.
- Manual playtest priority: verify timing between CHI/PRC diplomatic branch and Japanese reaction events.

## F. Technical integration notes
- **Files changed/added:**
  - `common/national_focus/AOTA_CHI.txt`
  - `common/national_focus/AOTA_PRC.txt`
  - `common/ideas/AOTA_china_rework_ideas.txt`
  - `common/decisions/AOTA_china_rework_decisions.txt`
  - `common/characters/AOTA_china_rework_characters.txt`
  - `events/AOTA_china_rework_events.txt`
  - `localisation/english/AOTA_china_rework_l_english.yml`
- Added namespaced event block (`add_namespace = aota_china`) to avoid collisions.
- Added broad localisation coverage for all new focus/event/idea/decision/character keys.

## G. Manual playtest recommendations
1. **CHI**: run all three claimant branches through to `CHI_crown_or_commune`.
2. **PRC**: run all three claimant branches through to `PRC_china_reborn_by_many_hands`.
3. Validate JAP reaction events 110-113 via console/event triggers.
4. Observe AI path selection and verify that branch exclusivity blocks correctly.
5. Stress-test decision cadence and political power economy under prolonged peace and early war.
6. Check balance around manpower inflow and combined industrial scaling.
7. Confirm no missing loc keys in CHI/PRC/JAP interaction UI surfaces.
