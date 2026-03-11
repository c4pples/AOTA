# China-Japan Interaction Audit

## A. Executive summary
- Conducted a full pass of China-region interaction points with Japan across focuses, events, decisions, triggers, on-actions, AI strategy, and diplomacy-layer modifiers.
- Preserved Japan's focus tree structure and content while adding additive support systems around it.
- Added a staged pressure/accommodation/resistance framework so China-Japan interaction can evolve through multiple political states before open war.
- Added differentiated responses for CHI, PRC, and regional Chinese actors (warlords / frontier regimes), including accommodation and backlash loops.

## B. Existing interaction diagnosis
Before this pass, China-Japan interaction was concentrated in a thin set of focus-linked events (`aota_china.100-113`) and two simple decisions in `AOTA_china_rework_decisions`.

Observed issues:
- Limited escalation depth (mostly immediate symbolic event responses).
- Limited actor differentiation (CHI/PRC had mirrored options and warlords had almost no explicit Japan-pressure handling).
- Missing systemic recurrence (no periodic pressure loop or backlash loop).
- Underdeveloped collaboration/proxy handling (no sustained accommodation-versus-backlash mechanics).
- Japan compatibility hooks existed in focus flavor but lacked external support logic tied to China-side outcomes.

## C. Escalation pacing review
Implemented a multi-step ladder instead of one-step escalation:
1. Japan enters diplomatic pressure phase when its existing continental-focus line is online.
2. Monthly pulse triggers a policy review event for Japan (escalate, negotiate, or covert pressure).
3. Chinese actors receive direct pressure/settlement events and can pick resistance, delay, or accommodation.
4. Accommodation can trigger anti-collaboration backlash over time, potentially forcing a policy reversal.

This creates variable pacing: diplomatic pressure and influence competition can persist before direct military confrontation.

## D. China-side response diversity review
Added differentiated response pathways:
- **CHI:** direct demand response, explicit delay strategy, local accommodation route.
- **PRC:** anti-imperial mobilization route, tactical delay, selective detente route.
- **Regional actors:** separate pressure event with simplified resist-or-delay choices.
- **All China-region actors:** decisions enabling emergency defense council, local accommodation, and later anti-collaboration purge.

This supports divergent political-military outcomes instead of a single generic anti-Japan behavior.

## E. Japan-side support content added
Without touching Japan's focus tree internals, added support around it:
- Scripted trigger checks keyed to existing Japan continental focus progression.
- Monthly policy review event (`aota_china.430`) for Japan.
- Japan decisions for incremental demands, compartmentalized settlements, and sponsor-network pressure.
- New pressure apparatus national spirit and compatibility hooks that interact with CHI/PRC/regional actors.

## F. Collaboration / puppet / concession logic review
Added a layered collaboration cycle:
- China-side local accommodation spirit represents concessionary governance.
- Japan-side regional security sponsorship expands influence and pressure effects.
- Periodic backlash event (`aota_china.420`) models anti-collaboration mobilization and legitimacy conflict.
- China can purge collaboration brokers, shifting back toward resistance politics.

This models comprador/intermediary politics and anti-collaboration contestation rather than binary war/peace.

## G. Diplomacy / faction implications
Diplomatic layer improvements:
- Added opinion modifiers for refusal, temporary settlement, and collaboration crackdowns.
- Decisions/events now shape bilateral stance trajectories (hardening hostility vs tactical coexistence).
- AI strategy hooks bias Japan and major Chinese actors toward preparation logic when resistance line is chosen.

This creates stronger pre-war diplomatic signaling and better differentiation in AI behavior.

## H. Technical notes
Added files:
- `common/scripted_triggers/AOTA_china_japan_interaction_triggers.txt`
- `common/ideas/AOTA_china_japan_interaction_ideas.txt`
- `common/decisions/AOTA_china_japan_interaction_decisions.txt`
- `common/on_actions/AOTA_china_japan_interaction_on_actions.txt`
- `common/ai_strategy/AOTA_china_japan_ai_strategy.txt`

Updated files:
- `events/AOTA_china_rework_events.txt` (new event chain 401-403, 411-412, 420, 430-432)
- `common/opinion_modifiers/AOTA_opinion_modifiers.txt` (added missing and new bilateral modifiers)
- `localisation/english/AOTA_china_rework_l_english.yml` (new localization for decisions, ideas, and events)

Safety constraints respected:
- No removal/rewrite/restructure of Japan focus tree.
- Additive compatibility content only.

## I. Manual playtest recommendations
1. **CHI resistance run:** choose repeated resistance outcomes and validate pressure-to-war pacing.
2. **CHI accommodation run:** take local accommodation, then observe backlash timing and purge decision effects.
3. **PRC delay run:** select delay choices and test whether AI Japan escalates coherently across pulses.
4. **Regional actor run (e.g., SHX or GXC):** confirm warlord-level pressure responses appear and are meaningful.
5. **Japan run:** cycle through all three policy-review options and verify event/decision cooldown behavior.
6. **AI observer run:** let game run to 1939 and confirm China/Japan behavior diverges based on chosen lines instead of converging into immediate deterministic war.
