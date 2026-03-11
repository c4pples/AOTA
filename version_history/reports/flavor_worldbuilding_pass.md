# Flavor & Worldbuilding Pass Report

## A. Executive summary
- **Countries reviewed:** ACC, AWU, ANA, APF, ACG, ASL, CCW, IRE, FIN, UKR, ALG, COG (all AOTA-specific country tags and split-state tags).
- **Countries changed directly in this pass:** IRE, FIN, UKR, ALG, COG.
- **Leaders adjusted:** 2 starting governor titles/descriptions updated (ALG, COG).
- **Characters added:** 15 total (3 each for IRE/FIN/UKR/ALG/COG).
- **Advisors added:** 15 total (all new characters are integrated advisors or high command).
- **Institutions / industrial-national systems added:** 5 starting national spirits.
- **Country names changed:** 5 (IRE, FIN, UKR, ALG, COG).
- **Country colors changed:** 5 (IRE, FIN, UKR, ALG, COG).
- **Dynamic flavor additions:** 2 startup events (ALG, COG) and startup on_action integration.
- **Major lore/theme goals:**
  - Make under-authored regional/minor states feel institutionally alive.
  - Clarify regime identity for colonial administrations.
  - Anchor each country in social blocs (bureaucrats, labor, officers, concession networks).
  - Preserve bleak/serious AOTA tone while improving political texture.

## B. Country-by-country summary

### Irish Republic (IRE)
- Added a clearer state identity name, adjective, and map color adjustment for readability and tone consistency.
- Added 3 characters: a modernization broker, a border-military organizer, and a civil-rights republican figure.
- Added a new starting national spirit (`Civic Republican Networks`) to represent local governance and legitimacy networks.
- Lore fit: reflects an insecure but politically dense republic balancing institution-building and frontier pressure.

### Republic of Finland (FIN)
- Added revised naming and adjective setup plus a colder, readable map tint.
- Added 3 characters representing diplomatic realism, winter logistics command, and labor-republic compromise politics.
- Added `White Guard Compact` as a starting institutional spirit.
- Lore fit: reinforces Finland's civic-military preparedness culture and elite bargaining model.

### Ukrainian People's Republic (UKR)
- Updated identity naming and color toward a darker frontier-green profile.
- Added 3 characters spanning socialist cadre politics, military frontier command, and anarchist organizing.
- Added `Frontier Atamanates` starting spirit.
- Lore fit: better reflects fragmented coercive authority and ideological competition between disciplined party structures and local militancy.

### French Algeria (ALG)
- Renamed state presentation from generic Algeria to explicit colonial-regime framing.
- Updated color for North African colonial readability and distinctiveness.
- Replaced generic governor label with named governor-general and dedicated regime description.
- Added 3 characters: colonial administrative machine, worker-national tribune, and militia instructor.
- Added `Colonial Dual State` spirit and a startup flavor event (`aota.1314`).
- Lore fit: presents Algeria as an unstable dual sovereignty system rather than a blank colonial placeholder.

### Congo Administration (COG)
- Renamed state to colonial administrative framing and updated adjective/DEF presentation.
- Updated color for central-African distinction and map clarity.
- Replaced generic governor title with named administrator and dedicated regime description.
- Added 3 characters: concessionary liaison, congregational mobilizer, and Force Publique stabilizer.
- Added `Concessionary Regime` spirit and startup flavor event (`aota.1315`).
- Lore fit: emphasizes extraction politics, coercive institutions, and mediated sovereignty.

## C. Character and institution log

### New leaders/figures and advisor clusters
- **IRE cluster:** Seán Lemass, Frank Aiken, Hanna Sheehy Skeffington.
  - Rationale: state-building triangle of industry, security, and civic legitimacy.
- **FIN cluster:** Juho K. Paasikivi, Valo Nihtilä, Väinö Tanner.
  - Rationale: elite negotiation under permanent military pressure.
- **UKR cluster:** Volodymyr Vynnychenko, Mykhailo Omelianovych-Pavlenko, Nina Strokata.
  - Rationale: red/black ideological contest plus operational command realities.
- **ALG cluster:** Marcel Régnier, Messali Hadj, Hocine Aït Ahmed.
  - Rationale: colonial bureaucracy vs anti-colonial mass politics and armed cadre evolution.
- **COG cluster:** Albert Nyssens, Simon Kimbangu, Léon Bobozo.
  - Rationale: company-state extraction, religious social networks, and coercive security apparatus.

### New institutional spirits
- `aota_ire_civic_republic_networks`
- `aota_fin_white_guard_compact`
- `aota_ukr_frontier_atamanates`
- `aota_alg_colonial_dual_state`
- `aota_cog_concessionary_regime`

Each spirit was intentionally modest in mechanics to preserve game balance while increasing world texture.

## D. Name/color review
- **IRE:** Ireland -> Irish Republic; green shifted darker for stronger identity contrast.
- **FIN:** Finland -> Republic of Finland; pale-blue toned down for readability.
- **UKR:** Ukraine -> Ukrainian People's Republic; green darkened to avoid blend with nearby palettes.
- **ALG:** Algeria -> French Algeria; color shifted toward muted colonial ochre.
- **COG:** Congo -> Congo Administration; color shifted to a deeper steel-blue for distinction from neighboring colonial hues.

Rationale across all five: improve lore signaling on map without introducing extreme/garish colors or breaking recognition.

## E. Integration notes
- Added character definitions in a dedicated file and hooked all 15 into country history setup via `recruit_character`.
- Added 5 new country spirits and attached each in corresponding country history files.
- Added 2 startup flavor events for ALG/COG and linked them through `common/on_actions/AOTA_v13_on_actions.txt`.
- Updated country-level localisation for names/DEF/ADJ plus regime descriptors.
- No changes were made to supported version or mod version metadata.

## F. Manual review items
- **Lore-thin areas (future pass):** finer sub-faction differentiation for COG interior polities and ALG settler party blocs would benefit from dedicated focus/event branches.
- **Portrait needs:** all 15 added characters currently use generic portrait assets and should receive bespoke art later.
- **Future event support:** IRE/FIN/UKR now have denser advisor rosters, but would benefit from cabinet shuffle events akin to major-power presentation.
- **Potential future mechanics:** path-specific cosmetic tags for ALG and COG decolonization outcomes are not implemented in this pass.

---

## Extension Pass: Non-AOTA Core Powers (GER/ENG/ITA/SOV/FRA/JAP)

### Executive additions
- Added **18 major-power characters** (3 per country) across cabinet, industrial, and military blocs.
- Added **6 major institutional spirits** for political-economy/world-system flavor.
- Added **6 startup flavor events** (`aota.1330`–`aota.1335`) wired to on_startup.
- Integrated all new content in country history setup for each major.

### Country notes
- **GER:** Cartel-finance governance texture with constitutional and military elite balancing.
- **ENG:** Committee-imperial governance, labor-state brokerage, and authoritarian opposition pressure.
- **ITA:** Corporative-state bargaining between crown, army, and industrial syndicates.
- **SOV (Russia):** Reconstruction compacts between center/periphery, with competing democratic, military, and revolutionary blocs.
- **FRA:** Metropolitan fragility tied to colonial extraction networks and industrial defense lobbies.
- **JAP:** Zaibatsu-state mobilization nexus and civilian-vs-expansionist strategic contest.

### Manual follow-up for this extension
- Portrait set remains generic and should be replaced with bespoke assets.
- If desired, each new major startup event can later branch into country-specific mini chains tied to focus completion.
