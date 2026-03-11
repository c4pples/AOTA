# American Civil War Resolution + Consolidation + Post-War Rework

## A. Executive summary
- **Splinter states reviewed:** ACC, AWU, ANA, APF, ACG, ASL.
- **Splinter states reworked:** ACC, AWU, ANA, APF, ACG, ASL.
- **Unique post-war branches added:** 5 new post-war focuses per splinter (30 total), each with bespoke institutional direction.
- **Events added:** 12 new events (`aota.840`-`aota.851`) including 6 domestic settlement events and 6 world-reaction news events.
- **Decisions added:** new post-war settlement decision category with 2 bespoke decisions per splinter.
- **Spirits added/reworked:** 15 new spirits reinforcing divergent reconstruction/repression identities.
- **Characters/institutions integrated:** post-war institutions (commissions, tribunals, directorates, boards, covenant structures) embedded through focus and event prose.
- **Diplomacy/world reaction added:** each splinter now triggers a distinct global reaction event on geopolitical re-entry.
- **Design philosophy:** additive expansion preserving all existing branches while creating unique endgame statecraft identities that continue gameplay after battlefield victory.

## B. Splinter-state diagnosis

### ACC
- **Before:** legalist reunification line ended with broad restoration rhetoric.
- **Underdeveloped:** little explicit justice/reconciliation design, weak post-war diplomacy identity.
- **Needed differentiation:** constitutional legalism, federal reintegration, controlled amnesty, rules-based re-entry.

### AWU
- **Before:** wartime red/black split had good early identity but limited post-victory governance payoff.
- **Underdeveloped:** tribunals, veterans, reconstruction administration, foreign revolutionary role.
- **Needed differentiation:** labor constitutionalism, revolutionary justice politics, worker-led reconstruction.

### ANA
- **Before:** commandist wartime path existed but postwar institutionalization was thin.
- **Underdeveloped:** no explicit permanent-security settlement mechanics.
- **Needed differentiation:** coercive consolidation, tribunal purges, martial reconstruction, hard-power diplomacy.

### APF
- **Before:** strong regional flavor but less developed as a complete successor-state model.
- **Underdeveloped:** reintegration formula, federal redesign doctrine, postwar diplomatic doctrine.
- **Needed differentiation:** negotiated federalism, maritime reconstruction, regional guarantees.

### ACG
- **Before:** corporate wartime flavor present; postwar architecture shallow.
- **Underdeveloped:** legal-economic coercion systems, security formalization, external strategy framing.
- **Needed differentiation:** contract sovereignty, seizure tribunals, charter zones, investor diplomacy.

### ASL
- **Before:** agrarian resistance identity existed but limited full-state postwar arc.
- **Underdeveloped:** reconciliation mechanism, land settlement, confederal institutional codification.
- **Needed differentiation:** county mediation, rural reconstruction, decentralized confederal diplomacy.

## C. Country-by-country post-war summary

### ACC (Constitutional restoration project)
- **Civil war resolution:** accountability commission event chain and oath/amnesty decisions.
- **Consolidation:** reintegration administration and pension/relief infrastructure rebuild.
- **Post-war branches:** Second Union Compact + diplomatic return focus.
- **Identity/naming:** cosmetic transition to **Second American Union**.
- **Mechanics:** legalist reconstruction spirits reduce unrest and reinforce democratic drift.
- **Diplomacy:** world reaction frames cautious recognition.
- **Uniqueness:** law-centered reunification where legitimacy depends on constitutional process.

### AWU (Workers’ refounding project)
- **Civil war resolution:** people’s tribunals and veterans’ control committee framework.
- **Consolidation:** reconstruction brigades and labor charter institutionalization.
- **Post-war branches:** Charter of Common Labor + World Congress posture.
- **Identity/naming:** cosmetic transition to **Commonwealth of American Labor**.
- **Mechanics:** tribunal instability vs mass-mobilization upside.
- **Diplomacy:** export-revolution framing triggers polarized global reaction.
- **Uniqueness:** mass politics and labor sovereignty define peace terms.

### ANA (Command-state refoundation)
- **Civil war resolution:** salvation tribunals and purge logic.
- **Consolidation:** internal security directorate + martial reconstruction.
- **Post-war branches:** Permanent Command Republic + coercive recognition path.
- **Identity/naming:** cosmetic transition to **American Command Republic**.
- **Mechanics:** high war-support and occupation control through repression-state spirits.
- **Diplomacy:** recognition-through-force world messaging.
- **Uniqueness:** security apparatus, not reconciliation, is the regime’s peace model.

### APF (Negotiated federal successor)
- **Civil war resolution:** reconciliation conference for reintegrated regions.
- **Consolidation:** maritime recovery board + autonomy guarantees.
- **Post-war branches:** Two-Ocean Charter + Pacific diplomatic re-entry.
- **Identity/naming:** cosmetic transition to **Two-Ocean American Federation**.
- **Mechanics:** stabilization + maritime-industrial recovery.
- **Diplomacy:** moderated, trade-led, Pacific-first re-entry.
- **Uniqueness:** negotiated federalism and regional pluralism as state doctrine.

### ACG (Corporate-sovereign settlement)
- **Civil war resolution:** asset seizure tribunals and contractual loyalty regimes.
- **Consolidation:** chartered reconstruction zones + contract police.
- **Post-war branches:** Shareholder Constitution + exchange diplomacy.
- **Identity/naming:** cosmetic transition to **Shareholder Union of America**.
- **Mechanics:** production and control bonuses tied to private governance logics.
- **Diplomacy:** treaty/debt/security package diplomacy rather than ideological blocs.
- **Uniqueness:** legitimacy derived from contract performance and market hierarchy.

### ASL (Confederal agrarian settlement)
- **Civil war resolution:** county reconciliation boards and local demobilization choices.
- **Consolidation:** land courts + rural reconstruction ministry.
- **Post-war branches:** Confederal Covenant + New Southern Diplomacy.
- **Identity/naming:** cosmetic transition to **Confederal American Commonwealth**.
- **Mechanics:** local-stability and manpower-centric rural order.
- **Diplomacy:** cautious external posture preserving autonomy.
- **Uniqueness:** county society mediates peace; center is intentionally limited.

## D. Uniqueness audit
- **ACC:** legal-constitutional reconstruction with managed amnesty.
- **AWU:** revolutionary social justice and labor constitutionalism.
- **ANA:** permanent emergency and command coercion.
- **APF:** negotiated federal pluralism and maritime recovery.
- **ACG:** market constitutionalism and privatized security.
- **ASL:** decentralized agrarian confederalism.

No splinter uses a shared generic post-war template in player-facing branch identity, event rhetoric, or spirit framing.

## E. Prose and flavor notes
- **Rhetoric differences:**
  - ACC uses legality, oaths, and constitutional restoration language.
  - AWU uses councils, labor sovereignty, and revolutionary justice language.
  - ANA uses command, purification, and security doctrine language.
  - APF uses conference federalism and pragmatic reconciliation language.
  - ACG uses contracts, charters, and investor-state language.
  - ASL uses county courts, parish mediation, and agrarian covenant language.
- **Mythmaking differences:** second founding, workers’ commonwealth, command salvation, two-ocean federalism, shareholder sovereignty, confederal covenant.

## F. Technical integration notes
- Added post-war focus branches directly to each US splinter focus file.
- Added new event file with settlement and global reaction IDs.
- Added new decision category for post-war governance.
- Added new spirits in existing idea container.
- Added new cosmetic country tag definitions and localization entries.
- **Path-locking:** post-war branches gated by `has_war = no` and existing end-of-war focuses.
- **Manual review item:** tune numerical balance after playtests for AI pacing.

## G. Manual playtest recommendations
1. Win civil war as each splinter and verify post-war branch unlock timing.
2. Check cosmetic renaming for all six successors after identity focus completion.
3. Validate world reaction events fire for each successor diplomatic-reentry focus.
4. Confirm AI can spend post-war decisions sensibly and does not deadlock.
5. Stress-test ideology drift and stability outcomes in long campaigns (1938-1943).
6. Verify no invalid references in event IDs, focus IDs, or idea keys.
