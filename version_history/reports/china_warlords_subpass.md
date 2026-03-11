# China Warlords-Only Sub-Pass Report

## A. Executive summary
This revision upgrades the earlier sub-pass into a **large, tag-distinct warlord layer**. The seven non-central Chinese actors (GXC, YUN, SHX, XSM, SIK, MEN, MAN) now share a broad systemic chassis but each receives unique late-branch content, unification framing, and autonomy outcomes with distinct cosmetic identities and color profiles.

The pass remains additive: no existing core China rework content was removed, but warlord tags now route into their dedicated tree and no longer depend on generic fallback pacing.

## B. Warlord / regional actor diagnosis
### Prior weakness
- Shared content existed but did not yet provide enough **tag-unique endpoint identity**.
- Warlord outcomes felt too close in presentation even when mechanics diverged.

### What was changed in this revision
- Expanded the warlord tree into a larger structure with:
  - shared statecraft progression,
  - three strategic macro-paths,
  - and **seven tag-exclusive unification lines + seven tag-exclusive anti-unifier/autonomy lines**.
- Added **cosmetic regime outcomes** for each tag-path pair with custom names and map colors.
- Added unique event beats for each tag-exclusive unification proclamation.

## C. Country-by-country summary
### GXC (Guangxi)
- Unifier project: **Federal Republic of Liangguang**.
- Autonomy project: **Liangguang Autonomy Front**.
- Identity core: southern commercial-federal military brokerage.

### YUN (Yunnan)
- Unifier project: **Southwest National Salvation Government**.
- Autonomy project: **Mountain Neutrality Zone**.
- Identity core: highland command politics and road/corridor leverage.

### SHX (Shanxi)
- Unifier project: **North China Discipline Regime**.
- Autonomy project: **Shanxi Defensive Federation**.
- Identity core: rail-industrial militarization and administrative discipline.

### XSM (Xibei San Ma)
- Unifier project: **Northwest Pacification Regime**.
- Autonomy project: **Northwest Faith and Order Compact**.
- Identity core: mobile frontier commanderies and corridor warfare.

### SIK (Sinkiang)
- Unifier project: **Western Provincial Compact**.
- Autonomy project: **Oasis Autonomy Statute**.
- Identity core: corridor governance, treaty pragmatism, and caravan-statecraft.

### MEN (Mengkukuo)
- Unifier project: **Inner Mongol Autonomous Command**.
- Autonomy project: **Steppe Neutral Zone Authority**.
- Identity core: banner institutional command under frontier pressure.

### MAN (Manchukuo)
- Unifier project: **Northeast Reorganization Authority**.
- Autonomy project: **Northeast Autonomous Directorate**.
- Identity core: technocratic-concessionary governance with security layering.

## D. Pacing and content spread improvements
- **Early game:** foundational legitimacy, patronage, grain/revenue, councils.
- **Midgame:** strategic split among survival, unification conference, or accommodation.
- **Late game:** long-tail tag-exclusive content with two unique destination models per actor.
- Result: each warlord remains active and narratively distinct into late campaign phases.

## E. Character / institution additions
No portrait pack changes in this revision; institutional depth was expanded through:
- provincial councils,
- military academies and command bureaus,
- frontier and transport security structures,
- reconstruction commissions,
- corridor treaty or concession governance structures,
- tag-specific command architectures.

## F. Unification / diplomacy logic changes
- Each tag can now reach a unique **reunification-branded regime** with bespoke focus progression and supporting event.
- Each tag can alternatively crystallize into a unique **autonomy/neutrality regime**.
- Accommodation and anti-unifier outcomes are no longer generic in title/presentation.

## G. Technical notes
- Expanded `common/national_focus/AOTA_CHI_warlords.txt` to a large mixed tree with tag-gated branches.
- Added additional warlord ideas for tag-specific unification programs.
- Added new warlord proclamation events (`aota_china.320–326`).
- Added new cosmetic tags with color definitions in `common/cosmetic_tags/AOTA_cosmetic_tags.txt`.
- Added localization for all new focuses, ideas, cosmetics, and events.

## H. Manual playtest recommendations
1. Run a start-date focus-tree check for all seven tags and confirm branch availability is tag-correct.
2. Confirm each tag can complete both a unifier endpoint and an autonomy endpoint.
3. Verify cosmetic tag name/color switch triggers correctly on endpoint focuses.
4. Verify AI chooses at least one tag-exclusive late branch in observer runs.
5. Confirm no missing localization for all new keys (focuses/ideas/events/cosmetics).
