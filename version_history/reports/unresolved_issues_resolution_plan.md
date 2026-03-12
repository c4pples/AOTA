# Unresolved Issues Resolution Plan (Post Auto-fix)

## A. Executive summary

- **Primary source report used:** `version_history/error_logs/parsed/latest_error_log_scan_and_autofix.md` (latest and only parsed auto-fix report currently present).
- **Total unresolved issues captured:** **5**.
- **Critical issues:** **2**
  - Unknown effect-type errors across scripted effects/decisions.
  - Unknown modifier errors in idea files.
- **High-priority issues:** **2**
  - Duplicate character tag definitions.
  - Localisation parser error near `AOTA_l_english.yml` line 484.
- **Medium/low issues:** **1**
  - Launcher `settings.txt` parse warning (`skip_account_link`) outside mod source scope.
- **Biggest release risks:**
  1. Parser/runtime script compatibility drift versus target HOI4 version (effects + modifiers).
  2. Character database collisions causing unpredictable load-order behavior.
  3. Hidden localisation formatting/encoding issue producing parser instability.
- **Recommended order of operations:**
  1. Lock target HOI4 version/API baseline.
  2. Resolve parser/script compatibility blockers (effects, modifiers).
  3. Resolve identity/reference collisions (duplicate characters).
  4. Perform localisation context + encoding audit.
  5. Execute controlled in-engine validation and targeted playtests.

---

## B. Issue inventory

### 1) Unknown effect-type errors in scripted content
- **Source report:** `latest_error_log_scan_and_autofix.md` section E.1.
- **Issue summary:** Frequent unknown effects for `add_army_experience`, `add_navy_experience`, `add_air_experience` (171 total emissions).
- **Category bucket(s):**
  - parser/script blocker
  - focus/event/decision integration issue
  - pacing/flow issue (indirect: broken reward hooks)
- **Severity:** **critical**.
- **Release urgency:** **must-fix before release candidate**.
- **Likely affected systems/files:** Scripted effects, decisions, events, and focus rewards where legacy experience effects are used.
- **Why unresolved:** Ambiguous replacement API depends on target game version and context (country scope, unit scope, effect signatures).
- **Likely cause category:** Version/API mismatch + legacy scripting carried forward.

### 2) Unknown modifiers in idea files
- **Source report:** `latest_error_log_scan_and_autofix.md` section E.2.
- **Issue summary:** 71 unknown modifier emissions (examples include `division_attack_factor`, `factory_output`, etc.).
- **Category bucket(s):**
  - parser/script blocker
  - focus/event/decision integration issue (idea rewards feed these systems)
  - AI/strategy issue (AI evaluations rely on valid modifiers)
- **Severity:** **critical**.
- **Release urgency:** **must-fix before release candidate**.
- **Likely affected systems/files:** `common/ideas/*` and any scripted references depending on those idea modifiers.
- **Why unresolved:** One-to-many or version-variant mappings are risky to apply automatically without balance review.
- **Likely cause category:** Version/API mismatch + outdated modifier keys.

### 3) Duplicate character tag definitions
- **Source report:** `latest_error_log_scan_and_autofix.md` section E.3.
- **Issue summary:** Two duplicate character tags found in character definitions.
- **Category bucket(s):**
  - parser/script blocker (load-order conflict)
  - lore-sensitive design issue
  - ambiguous manual-review case
- **Severity:** **high**.
- **Release urgency:** **fix before major content expansion; ideally before RC**.
- **Likely affected systems/files:** `common/characters/*` and any event/focus/idea references to duplicated character IDs.
- **Why unresolved:** Could be intentional override pattern versus accidental duplicate; requires canon/lore judgment.
- **Likely cause category:** Content branch merge collision or intentional override not documented.

### 4) Localisation parser complaint near line 484
- **Source report:** `latest_error_log_scan_and_autofix.md` section E.4.
- **Issue summary:** Localisation parse error reported at `AOTA_l_english.yml` line 484, but direct line inspection did not reveal an obvious syntax defect.
- **Category bucket(s):**
  - localisation/reference issue
  - ambiguous manual-review case
  - pacing/flow issue (if keys fail, player guidance/UI text degrades)
- **Severity:** **high** (can be medium if isolated, but high until verified non-cascading).
- **Release urgency:** **fix before release candidate**.
- **Likely affected systems/files:** `localisation/english/AOTA_l_english.yml` and potentially adjacent localisation files loaded before/after it.
- **Why unresolved:** Likely hidden character, encoding/BOM issue, or malformed neighboring entry creating offset parser failure.
- **Likely cause category:** Encoding/contextual parser edge case.

### 5) Launcher settings parse error (`skip_account_link`)
- **Source report:** `latest_error_log_scan_and_autofix.md` section E.5.
- **Issue summary:** Parse error in launcher `settings.txt` outside mod source.
- **Category bucket(s):**
  - ambiguous manual-review case
  - polish/environment issue (non-mod)
- **Severity:** **low** for mod release readiness.
- **Release urgency:** **defer unless reproducible in clean QA environment**.
- **Likely affected systems/files:** User launcher profile/settings outside repository.
- **Why unresolved:** Not a mod-content file; unsafe/out-of-scope for repository auto-fix.
- **Likely cause category:** Local environment corruption or launcher version mismatch.

---

## C. Recommended resolution plan

### Issue 1: Unknown effect-type errors
- **Likely fix approach:**
  1. Build a version-locked effect compatibility table for experience gain effects.
  2. Enumerate every usage site via targeted search.
  3. Replace effect names/signatures contextually (not global blind replace).
  4. Re-validate in-engine logs and spot-check gameplay reward outcomes.
- **Required file/system review:** `common/scripted_effects/*`, `common/decisions/*`, `common/national_focus/*`, `events/*`.
- **Work type:** Primarily **technical repair**, with secondary **pacing validation**.
- **Execution mode:** **Implementation + audit + controlled playtest**.
- **Recommended remediation pattern:** script cleanup + reference repair.
- **Complexity:** **high**.

### Issue 2: Unknown idea modifiers
- **Likely fix approach:**
  1. Create a modifier translation matrix for target HOI4 version.
  2. Cluster unknown modifiers by semantic intent (industry, combat, doctrine, etc.).
  3. Replace each modifier key with validated equivalent, preserving intended magnitude where possible.
  4. Run balance sanity pass for major powers and key regional paths.
- **Required file/system review:** `common/ideas/*`, `common/country_leader/*` (if modifier-bearing), scripted idea grants from focuses/events.
- **Work type:** **technical + design-sensitive** (because modifier equivalence can alter balance identity).
- **Execution mode:** **Implementation + audit + playtest**.
- **Recommended remediation pattern:** script cleanup + reference repair + AI weight review (post-fix).
- **Complexity:** **high**.

### Issue 3: Duplicate character tags
- **Likely fix approach:**
  1. Identify duplicate IDs and all declaration sites.
  2. Determine intended canonical owner/version per lore timeline and region.
  3. Keep one canonical definition; rename or retire duplicate safely.
  4. Update all references (events, ideas, advisors, focus rewards) to canonical tag.
- **Required file/system review:** `common/characters/*`, `events/*`, `common/ideas/*`, `common/national_focus/*`.
- **Work type:** **lore-sensitive design + technical reference repair**.
- **Execution mode:** **Audit first, then implementation, then targeted playtest**.
- **Recommended remediation pattern:** reference repair + manual lore review.
- **Complexity:** **medium**.

### Issue 4: Localisation parser complaint (line 484 context)
- **Likely fix approach:**
  1. Inspect surrounding block (~100 lines around reported line) for quote/colon/newline anomalies.
  2. Check file encoding, BOM, non-printable characters, and mixed line endings.
  3. Validate key uniqueness and malformed multiline entries.
  4. Re-test in-engine parser to confirm error disappearance.
- **Required file/system review:** `localisation/english/AOTA_l_english.yml`, potentially other `localisation/english/*.yml` loaded in same cycle.
- **Work type:** Mostly **technical repair**.
- **Execution mode:** **Audit + targeted implementation + parse retest**.
- **Recommended remediation pattern:** reference/localisation cleanup + controlled validation.
- **Complexity:** **medium**.

### Issue 5: Launcher settings parse error (external)
- **Likely fix approach:**
  1. Treat as environment-level QA checklist item.
  2. Reproduce in clean profile or alternate machine.
  3. If non-reproducible in clean environment, document as local-only noise.
- **Required file/system review:** External launcher profile (`settings.txt`), not repository.
- **Work type:** **manual environment audit**.
- **Execution mode:** **Audit only**.
- **Recommended remediation pattern:** external config reset; no mod code change.
- **Complexity:** **low**.

---

## D. Dependency / order-of-operations plan

### Phase 1 — Launch/parser blockers (must complete first)
1. **Version baseline lock** (exact HOI4 target version + DLC assumptions) and publish compatibility map template.
2. **Unknown effect-type fixes** applied by context.
3. **Unknown modifier fixes** in ideas and linked reward chains.

**Why first:** These are primary parser/runtime blockers and can invalidate later balancing or AI conclusions.

### Phase 2 — Hard reference/integration fixes
4. **Duplicate character tag resolution** (canonicalization + reference relink).

**Dependency note:** Character conflicts can produce unstable event/focus outcomes, so this should happen before AI tuning and broad scenario verification.

### Phase 3 — Localisation integrity and context checks
5. **Line-484 localisation investigation** including encoding/hidden-character audit and in-engine parse confirmation.

**Dependency note:** UI text reliability is needed before meaningful narrative pacing review and content QA signoff.

### Phase 4 — AI/faction/pathing validation after script stability
6. Re-run logs + quick AI observer sanity pass to ensure fixed effects/modifiers did not distort behavior.

**Dependency note:** AI tuning should not start from invalid script baseline.

### Phase 5 — Residual warnings and external noise triage
7. Assess launcher `settings.txt` warning in clean environment and document disposition.

---

## E. Manual review / playtest priorities

### Manual-judgment required
- **Character duplicate resolution** needs lore authority to decide canonical identity, timeline, and replacement strategy without erasing intended regional narrative beats.
- **Modifier remapping sanity** needs design review to ensure replacements preserve faction identity and campaign pacing.

### Playtest-required validations
- **Experience effect remaps:** Verify focuses/decisions/events still award intended experience quantities and at intended cadence.
- **Idea modifier remaps:** Verify economy/combat curves for at least one major and one minor per key region.
- **Character canonicalization:** Verify events, portraits, advisors, and leader transitions still trigger correctly.

### Potential deeper-system symptoms to monitor
- High-volume unknown effect/modifier logs may indicate broad **version drift** across multiple content eras.
- Localisation line-level complaint with clean syntax may indicate **encoding pipeline inconsistency** across generated/edited files.

---

## Practical roadmap (release-readiness framing)

### Immediate fixes (next working session)
1. Establish HOI4 target version matrix and final accepted effect/modifier keys.
2. Patch unknown effects in highest-frequency files first; run log diff.
3. Patch unknown modifiers in ideas for major nations first; run log diff.

### Short-term follow-up fixes
4. Resolve duplicate characters with lore gate review + complete reference sweep.
5. Complete localisation encoding/context cleanup and parser retest.

### Deeper manual-review items
6. Validate that modifier/effect replacements preserve intended geopolitical pacing and regional asymmetry.

### Playtest-required items
7. Controlled 1936 start smoke test + 1–2 observer runs to verify no new script spam, reward failures, or broken content chains.

---

## Suggested tracking checklist
- [ ] Target HOI4/API baseline documented.
- [ ] Unknown effect occurrences reduced to zero or explicitly waived with rationale.
- [ ] Unknown modifier occurrences reduced to zero or explicitly waived with rationale.
- [ ] Duplicate character tags resolved and references updated.
- [ ] Localisation parser complaint cleared in-engine.
- [ ] Post-fix log scan archived in `version_history/error_logs/parsed/`.
- [ ] Manual playtest notes added to `version_history/reports/`.
