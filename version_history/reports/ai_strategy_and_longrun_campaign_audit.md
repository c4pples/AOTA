# AOTA AI Strategy and Long-Run Campaign Audit

## A. Executive summary

### Countries / systems audited
This pass audited full-mod AI support architecture with emphasis on high-impact campaign actors and shared systems:
- Major focus trees and progression architecture: GER, FRA, ENG, SOV, USA, ITA, TUR, CHI, PRC, JAP.
- High-content regional/splinter clusters: US splinters (ACC/AWU/ANA/APF/ACG/ASL/CCW), China actors, faction-evolution participants.
- AI support systems: focus weighting scaffolds, ai_strategy, ai_strategy_plans, decisions, event ai_chance coverage, and focus-gating hygiene.

### Trees with good baseline usability
- Most trees are structurally traversable from a prerequisite perspective.
- Many major trees already contain coherent ideological rails via `mutually_exclusive` and branch-specific rewards.
- Late-arc content exists for villain/good-guy outcomes rather than ending at early crisis beats.

### Trees with major AI pathing issues (pre-fix)
- **Global issue**: almost all focus trees lacked explicit `ai_will_do`; AI relied entirely on default generic scoring.
- **Critical blocker**: multiple major trees (GER/SOV/USA) used stray top-level `available = { ... }` lines not attached to focus objects, effectively disabling intended branch gating for AI and player.
- **Branch coherence risk**: without weights or strategy plans, ideological commitment could drift and undercut country identity.

### Economy buildup issues (pre-fix)
- Economy/military pacing was mostly focus-driven; when AI drifted from intended branch rails it underutilized industrial clusters.
- Decision-heavy reconstruction paths (China and US postwar) had no AI pull, making economies stall after scripted crises.

### Army buildup issues (pre-fix)
- AI had limited doctrine/path guidance for midgame escalation outside a handful of strategy snippets.
- Reunification/collapse actors often lacked steering to continue active military buildup post-crisis.

### Decision/event AI issues (pre-fix)
- Most decision categories had **no** `ai_will_do` entries.
- Many event files had low/zero `ai_chance` coverage relative to multi-option event volume.

### Biggest long-run weaknesses
- AI frequently failed to self-direct through reconstruction/unification loops.
- Diplomacy/faction systems were mostly player-driven due to no decision weights.
- Major ideological macro-arcs existed but had weak AI steering into mid/late game blocs.

### Biggest fixes applied in this pass
1. Repaired focus gating bugs in major trees (GER/SOV/USA) by embedding `available` on focus nodes.
2. Reworked broken ai_strategy syntax in `AOTA_v12_ai_strategy.txt` into valid per-plan blocks.
3. Expanded ai strategy planning for villain/democratic GER, SOV reunification, CHI/PRC reunification, and US splinter postwar behavior.
4. Added AI decision weights for China unification and reconstruction loops, faction-evolution invites, and US postwar settlement decisions.

---

## B. Focus tree AI review

### Global review
- Focus content breadth is high across majors/minors, but AI control was under-specified.
- No broad per-focus weighting layer currently exists in `common/ai_focuses`; this remains a recommended future pass.

### Germany (GER)
- **Pre-fix issue**: ideological split and timeline gates had detached `available` blocks, causing branch access bugs and incoherent progression.
- **Fix**: moved each `available` condition directly into the corresponding focus definitions.
- **Result**: AI can now properly wait for stage/date gates and enter intended democratic/authoritarian arc timing.

### Soviet/Russia (SOV)
- **Pre-fix issue**: six detached `available` gates on stage-1 ideological forks.
- **Fix**: inlined availability on each gated focus.
- **Result**: AI can consistently hit intended reunification/ideological branch entry logic rather than taking paths prematurely or inconsistently.

### United States (USA)
- **Pre-fix issue**: detached timeline gating for mobilization/arsenal progression.
- **Fix**: inlined the two date gates onto their target focuses.
- **Result**: better campaign pacing through pre-fracture buildup and crisis sequencing.

### FRA/ENG/TUR/ITA/CHI/PRC/JAP and minors
- Structural traversal is mostly valid, but branch frequency/coherence is still constrained by missing per-focus AI weighting.
- Strategy/decision improvements in this pass reduce drift for their downstream systems, but a dedicated focus-weight pass is still recommended.

---

## C. Economy / construction review

### Key findings
- Industrial growth scaffolding exists in trees, but AI frequently failed to trigger adjacent decision systems that convert victory/stabilization into scaling.
- Post-unification and post-fracture economic phases (China, US splinters) were especially vulnerable to passivity.

### Fixes applied
- Added `ai_will_do` to China legitimacy/reconstruction decisions so AI can actively transition from contested to consolidated economy.
- Added `ai_will_do` to US postwar settlement decisions so splinters/reintegrators continue state-building after military phase.

### Remaining recommendations
- Add country-specific construction strategy weights (civ→mil transition windows) in `common/ai_strategy` or dedicated scripted economy planners.
- Add periodic AI catch-up decisions for states with deep debuff stacks.

---

## D. Military buildup review

### Army
- Major trees include military rewards, but AI momentum post-crisis was weak without strategic directives.
- Added strategy plans to keep SOV, CHI/PRC, GER-hegemonic, and US successors oriented toward military relevance.

### Air
- Air progression exists in focuses (e.g., USA/GER), but no dedicated air AI support layer was found in this pass.
- Recommendation: add `ai_equipment` bias updates for air-relevant countries once playtest data confirms shortages.

### Naval
- Naval identities exist for selected powers but are not strongly guided by current strategy plans.
- Recommendation: add naval theater and dockyard production priorities for island/naval actors in a follow-up.

### Templates/OOB
- Not deeply modified in this pass; no content removals applied.
- Recommendation: run scenario-level OOB stress tests for splinters and China actors after 1938/1942 checkpoints.

---

## E. Decision / event / mechanic AI review

### Systems that were AI-underused
- China unification category
- Japan anti-unification response category
- Faction-evolution invite decisions
- US postwar settlement decision category

### Systems now AI-supported
- Added explicit `ai_will_do` across the above categories to ensure AI progression through core mod-only mechanics.

### Remaining manual-review areas
- Multi-option event files still have uneven `ai_chance` coverage.
- Some story events likely still depend on default first-option behavior and should receive deliberate ideology/path-aware weighting.

---

## F. Diplomacy / faction / war review

### Findings
- Faction invite logic existed but was effectively player-driven without decision weights.
- A legacy ai_strategy file contained malformed syntax, weakening global AI diplomatic/war behavior.

### Fixes applied
- Rewrote `AOTA_v12_ai_strategy.txt` into valid strategy entries.
- Expanded strategy plans:
  - Democratic GER cooperation.
  - Hegemonic/villain GER external pressure behavior.
  - SOV reunification militarized frontier pressure.
  - CHI/PRC reunification-war preparation.
  - US splinter postwar armed consolidation posture.

### Recommendations
- Add peace behavior tuning in `common/ai_peace` for multi-actor civil conflicts and reunifiers.

---

## G. Long-run campaign health

### Countries scaling better after this pass
- GER, SOV, USA: branch/timeline progression is now mechanically reliable.
- CHI/PRC/JAP: unification-response loops now have decision AI pull and strategy support.
- Faction leaders in evolution system can now autonomously invite partners.
- US successors now continue postwar governance/economic loop decisions.

### Still likely to need playtest observation
- FRA/ENG/TUR/ITA late-game path coherence under heavy world divergence.
- Naval powers and island actors for air/naval allocation quality.
- Hidden/villain branches requiring specific event chains.

### Likely remaining AI pain points
- Missing tree-wide focus weighting means some branches may still be under-selected.
- Event-option AI logic remains uneven outside already-covered files.

---

## H. Technical notes

### Files changed
- `common/national_focus/AOTA_GER.txt`
- `common/national_focus/AOTA_SOV.txt`
- `common/national_focus/AOTA_USA.txt`
- `common/ai_strategy/AOTA_v12_ai_strategy.txt`
- `common/ai_strategy_plans/AOTA_ai_strategy_plans.txt`
- `common/decisions/AOTA_china_unification_decisions.txt`
- `common/decisions/AOTA_faction_evolution_decisions.txt`
- `common/decisions/AOTA_v44_us_postwar_decisions.txt`

### AI logic added
- Focus availability attached to focus definitions (major gating fix).
- Valid ai_strategy entries replacing malformed structure.
- New strategy plans for long-run ideological/geopolitical coherence.
- AI decision weights for high-importance mechanic categories.

### Remaining edge cases
- Global lack of per-focus `ai_will_do` remains the largest systemic gap.
- Event `ai_chance` normalization is incomplete and should be tackled in a dedicated pass.

---

## I. Manual playtest recommendations

### Countries to observe
- GER, FRA, ENG, SOV, USA, CHI, PRC, JAP, TUR, ITA.
- US splinters: ACC/AWU/ANA/APF/ACG/ASL/CCW.

### Paths to test
- GER democratic vs villain track (ensure coherent bloc behavior).
- SOV ideological forks and reunification tempo.
- USA fracture and postwar successor consolidation decisions.
- CHI/PRC unification and JAP fragmentation/response loop.

### Wars to watch
- GER-FRA timing under both restrained and hegemonic arcs.
- China theater escalation from contested stage to reunification.
- US successor wars and reconsolidation.

### Late-game scenarios to verify
- Post-victory/post-reconstruction activity after 1942+.
- Faction evolution persistence and invite behavior.
- Whether reunified actors keep scaling military+industry instead of stalling.
