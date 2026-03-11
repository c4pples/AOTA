# AOTA Base Focus Tree Migration Report

## Scope and safety rule applied
This pass implements a **safe fallback architecture**:
- Preserve all countries with meaningful mod contact.
- Migrate only clearly unsupported countries with no visible mod-specific touchpoints in this repository.
- Preserve uncertain or high-risk cases by default.

## 1) Audit summary of current focus content
`common/national_focus/` currently contains bespoke AOTA trees for:
`ALB ARG AUS BEL BRA BUL CHI CZE DEN EST FIN FRA GER GRE HOL HUN IRE ITA JAP LAT LIT LUX MEX NOR POL POR PRC ROM SER SPA SWE SWI YUG`.

Additionally, `history/countries/` contains direct focus assignments for `JAP` and `SER`, reinforcing mod-touched status.

## 2) Classification

### Preserved as mod-touched
All countries with dedicated AOTA focus files are preserved unchanged:
`ALB ARG AUS BEL BRA BUL CHI CZE DEN EST FIN FRA GER GRE HOL HUN IRE ITA JAP LAT LIT LUX MEX NOR POL POR PRC ROM SER SPA SWE SWI YUG`.

### Clearly safe unsupported countries migrated to AOTA base tree
Migrated (explicit assignment to the new fallback tree):
`AFG BHU NEP PER IRQ SAU OMA YEM SIA MON TAN TIB SIK XSM SHX YUN GXC MEN MAN PHI INS ECU BOL PAR URG PRU COL VEN CHL GUA HON ELS NIC COS PAN CUB DOM HAI`.

Rationale: these are Asian and non-Asian minors with no country-specific focus files, hooks, or history overrides found in this mod repository during audit, and they are the clearest unsupported candidates for a shared AOTA fallback architecture.

### Borderline/high-risk cases preserved by default
Not migrated in this pass:
- Major powers and explicit no-touch countries: `GER FRA ITA USA`.
- Other likely fragile/interesting countries (kept on existing behavior): all non-listed tags, including potential civil-war/splinter tags and countries that may rely on vanilla/DLC event chains.

## 3) AOTA base tree design rationale
The fallback tree (`aota_base_fallback_focus`) is compact and structured around six sections:
1. Internal political consolidation.
2. Economic recovery and industrial planning.
3. Military reform and readiness.
4. Diplomacy/alignment/regional posture.
5. Governance posture (civic legitimacy vs security mandate).
6. Late survival/resilience utility.

Design goals met:
- Mod-toned post-armistice framing.
- Country-agnostic mechanics suitable for unsupported minors.
- No map/province custom assumptions.
- Avoids oversized conquest fantasy; keeps limited late utility.

## 4) Supporting conflict suppressions
No broad suppression rewrites were made.
- No edits to existing bespoke trees.
- No edits to events/decisions/ideas/history for touched countries.
- Migration is done through explicit target-tag weighting in one new focus tree file only.

## 5) Validation checklist used
- New focus IDs are globally unique via `AOTA_base_` prefix.
- New tree has localization for every added focus key.
- Existing mod-touched trees/files are left intact.
- Migrated set is explicit and narrow to avoid accidental overrides.
