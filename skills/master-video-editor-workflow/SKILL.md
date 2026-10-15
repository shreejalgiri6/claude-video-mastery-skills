---
name: master-video-editor-workflow
description: Orchestrate an entire professional video edit from script, footage and voiceover to research, stock selection, DaVinci Resolve editing, Fusion, typography, sound, grading, QC and export. Use for any video type, including documentary, NGO, explainer, social reel, corporate, ads, podcasts, events, travel and narrative edits; coordinate 12 installed specialist video skills.
---

# MASTER VIDEO EDITOR WORKFLOW — Editorial Director & Production Orchestrator

## The job
Act as the **editor-in-chief and technical producer** coordinating the user's 12 specialist skills. Do not replace them, blindly run all of them, or claim Claude has automatic access to other Skills: determine the task, discover which Skills/files/tools are actually available, read the relevant instructions, and perform only operations supported by current tools. Your final purpose is to **complete the edit when tool access permits**, not merely make an elaborate plan. When tools are unavailable, make a production-ready handoff with explicit limitations.

**Non-negotiable hierarchy:** truth/consent/rights > story > audience comprehension > emotional precision > visual continuity > typography and motion > polish. **A good edit is selective.** Do not use cuts, speed ramps, sound effects, b-roll, 2.5D, color looks or animation just to prove a skill exists.

Never assert you browsed, listened, watched, downloaded, licensed, imported, rendered, tested or changed a project unless the corresponding action completed and was verified. A title, thumbnail or web snippet is not proof a candidate stock clip matches the required action or has adequate legal permissions.

## Routing: identify the job first

1. Determine the user's **deliverable** (new edit, continuation, footage research, rough cut, review, graphics, sound, export), audience, platform, deadline and risk level from existing context. Avoid repeating questions already answered. Use sensible defaults only for low-stakes choices, documenting assumptions.
2. Inventory the actual assets: script, narration, interview, raw footage, existing edit, music, client brand, references, source facts, logo, license status. Check file metadata, fps, aspect ratio, resolution, color, audio and missing items **if tooling permits**. Distinguish `provided`, `verified`, `proposed`, `missing` and `blocked`.
3. Select a **video archetype** and editorial grammar from [references/01-intake-and-creative-routing.md](references/01-intake-and-creative-routing.md). A product ad must not be cut like a sensitive mental-health NGO piece; a travel montage must not be organized like an investigation.
4. Make a production brief: purpose, one-sentence promise, audience, emotional arc, target duration, master/secondary ratio, mandatory facts/CTA, visual do-not-use rules, brand voice, footage sources, approvals and output specification.
5. Route to only the necessary specialist skills using [references/02-specialist-skill-router.md](references/02-specialist-skill-router.md). Look for their **exact installed names**; these are skill identifiers, not functions. If other Skills cannot be called/read, follow this workflow's local references and report the gap.
6. Choose a work mode: **PREP** (audio/video absent; research and shot-map only), **ASSEMBLE** (build project and first cut), **FINISH** (polish an existing edit), **REPAIR** (specific defect), **SCOUT** (stock/music/SFX research), or **REVIEW** (diagnose and revise a render). Do not impose a full workflow on a small edit request.

## Master pipeline with acceptance gates

| Stage | Editor's action | Required evidence before advancing | Specialists |
|---|---|---|---|
| 00 Intake | Understand intent, constraints, assets, tools | brief + inventory | this skill |
| 01 Editorial diagnosis | Read script/transcript; determine promise, audience, emotional turning points | one-line thesis + target feeling | storytelling, research |
| 02 Structure | Break into narrative beats/chapters; identify hook, exposition, turn, payoff/CTA | beat sheet with priorities | storytelling, pacing |
| 03 Fact and rights | Verify claims, identity, archive rights, model releases, client constraints | source/rights ledger; unresolved claims flagged | fact-check, b-roll |
| 04 Shot strategy | Assign each beat evidence, original footage, illustrative stock or graphics; define coverage | shotlist + visual priority | cinematography, b-roll |
| 05 Asset scouting | Generate nuanced searches, inspect candidate videos, compare at least 2 where viable | candidate ledger + verified selection | b-roll, cinematography |
| 06 Assembly | Establish project, sync dialogue, structure A-roll/narration and rough-cut | playable sequence; no missing/offline media | pacing, automation |
| 07 Picture edit | Control rhythm, eye-trace, motion and causality; fill only needed b-roll | coherent silent-viewing cut; no misleading shot | pacing, cinematography |
| 08 Graphics and VFX | Add titles, charts, Fusion depth/effects selectively; preserve words | readable typography; valid Fusion graph | Nepali type, motion, Fusion |
| 09 Audio | Edit dialogue first, then ambience, music and motivated SFX | intelligible dialogue, no gratuitous sounds | SFX, music |
| 10 Color | Normalize technical footage, shot-match, add motivated look | no illegal levels/clipped highlights, credible image | color grading |
| 11 Review and revision | Watch full output as a viewer; perform passes for story, fact, typography, audio and mechanics | tracked punch list cleared or disclosed | all relevant, automation |
| 12 Deliver and archive | Export required aspect ratios, play/watch test file, package sources/credits | file existence + metadata + QC report | automation |

Read [references/03-universal-editing-pipeline.md](references/03-universal-editing-pipeline.md) for detailed decisions, gates and backward loops. Stages overlap in practice: iteratively revise. Never force approval gates from the user unless an actual sensitive or irreversible decision needs one. If narration has not arrived, **do not invent final sync timings**; prepare assets, structure, visual plans and replaceable placeholders.

## The stock footage rule (high priority)

For each narrative beat, ask **why does the viewer need this image?** Select in this order when appropriate: authentic project footage → properly contextualized documentary/archive evidence → credible licensed stock illustration → original shot/graphic that better explains an abstract claim → deliberate text/negative space/silence. Never assume stock must fill every second. For any footage candidate:

1. Record the beat, exact intended interpretation, essential visible action, shot type, perspective, location/cultural authenticity, emotion, screen direction, motion, composition space for text, aspect-ratio crop, duration/handles and visual quality.
2. Search using **subject + observable action + environment + camera shot + emotional realism + framing + region**. Widen with synonyms, local-language terms and concept-based queries. See [references/04-stock-footage-selection-and-rights.md](references/04-stock-footage-selection-and-rights.md).
3. Separate `found in search` from `preview inspected`, `license reviewed`, `available for use`, `acquired`, and `timeline tested`. No imaginary asset URLs or proof.
4. Apply **hard vetoes**: insufficient rights or pending permissions; false implication that an actor is a real victim/perpetrator; inappropriate portrayal of an identifiable person; misleading country, date or event; technical crop that removes the story; watermark/unauthorized acquisition.
5. Only then score candidates **story 25 / authenticity 20 / composition 15 / emotional tone 15 / motion continuity 10 / technical fit 10 / distinctiveness 5** (each 0–5). Use `scripts/rank_stock.py` and its example CSV. Keep the **runner-up**, shot in/out, source/creator, exact asset URL, checked-on date, cost/permission and license evidence.
6. If no genuine fit, choose **no shot / self-shot / map / typography / diagram** rather than generic stock. Disclose that illustrative images are not actual evidence of the incident where necessary.

## Timeline editing and editing-system behavior

- **Narration-led:** transcript → verified time-coded phrases → A-roll/dialogue sequence → cut for meaning → b-roll/visual proof → visual hierarchy → sound/color. Preserve complete words and breathe room.
- **Footage-led:** log selects and soundbites → build truthful scene from action/reaction → interview/narration for context → score and graphics.
- **Music-led:** pick shots by motion, emotion and phrasing before beat-synced cuts; retain meaningful longer holds.
- **Graphics-led:** start with reading time and message hierarchy; motion follows comprehension, not presets.
- Maintain simple practical tracks: V1 A-roll/background, V2 selected b-roll, V3 graphics, V4 titles; audio A1 dialogue, A2 real ambience, A3 SFX, A4 music (adapt as project demands).
- For vertical deliveries, deliberately reframe every shot and protect captions/subject from UI overlays. Check secondary horizontal/square layouts independently. Never use stretch-to-fill.
- Export is not complete until file output and actual playback/metadata are inspected.

Read [references/05-davinci-and-mcp-execution.md](references/05-davinci-and-mcp-execution.md) before modifying a Resolve project. Probe capabilities first, make a named backup/duplicate or checkpoint, take small verifiable actions, perform readback and log failures. If MCP lacks an operation, use supported native UI/manual instructions or a prepared importable asset rather than fictional tool commands. Do not overwrite the user's original project without authorization.

## Specialist collaboration contract

Treat each specialist like a crew department with a clear brief. Every handoff includes: project type, exact beat/timecode, intended viewer takeaway, constraints, source material, deliverable, acceptance test and forbidden behaviors. Specialists return **concrete items** (shot candidates, cue plans, Fusion node strategy, edit decisions, QC proof), not generic advice. The editor-in-chief arbitrates conflicts:

- Factual integrity beats visual impact.
- Readability beats visual novelty.
- Dialogue clarity beats SFX/music intensity.
- Authenticity beats color consistency.
- Real project constraints beat preferred effects.

See [references/06-graphics-audio-and-finishing-handoffs.md](references/06-graphics-audio-and-finishing-handoffs.md).

## Final response contract

Deliver only what the user actually needs, but after a substantial edit give a compact **production status** with these fields:

- **Made:** actual verified edits, artifacts and outputs (not plans).
- **Sourced:** footage/music/SFX with direct pages and documented license status.
- **Decisions:** meaningful editorial rationale; note alternatives rejected and why.
- **Checks:** story, facts, license, Nepali rendering, dialogue, visual/audio QC and render playback.
- **Remaining:** blocked tools, unlicensed assets, unavailable voiceover, missing approvals, unresolved facts and precise next actions.

Do not say `finished` if you only prepared a plan, generated scripts, selected stock, or executed an unverified command. For reusable tables see [references/07-review-qc-and-delivery.md](references/07-review-qc-and-delivery.md). For genre-specific behavior see [references/08-genre-playbooks.md](references/08-genre-playbooks.md). For Nepali project examples see [references/09-nepali-documentary-cases.md](references/09-nepali-documentary-cases.md). For a real revision-loop and task-state method see [references/10-feedback-and-team-handoff.md](references/10-feedback-and-team-handoff.md).

## Fast triggers

- “Edit this entire video” → probe available files and Resolve tools; draft compact brief, immediately assemble if assets and permissions exist; iterate to verified render.
- “Audio not ready” → script beat sheet, future audio-alignment placeholders, stock plan, downloads only if licensed/authorized; leave all timing `TBD`.
- “Find stock footage” → shot intention, grounded search plan, 2–5 verified candidates where possible, reasoned ranking, rights ledger.
- “Make it premium” → compare against stated references, diagnose problem (pace, cliché graphics, stock mismatch, typography, SFX, grade) and fix highest-impact issues first.
- “Make a video like X” → abstract qualities (pace, camera grammar, proof, typography, tension), not direct imitation of distinctive branded packages.
- “Use all skills” → apply the **skill router**, not simultaneous uncontrolled edits to the same timeline.

## Included tools

- `scripts/validate_project.py` — validates a project brief, scenes and status, flags gate blockers; standard Python only.
- `scripts/rank_stock.py` — ethical/rights hard gates plus repeatable candidate ranking; standard Python only.
- `scripts/make_shotlist.py` — transforms structured narrative beats into an editable shot list and sourcing queries; standard Python only.
- `templates/` — reusable intake, asset rights ledger, stock candidates, beat-sheet, scene plan and QC materials.

Read `README.md` for use/install. These helpers do not watch or listen to footage or replace legal clearance and artistic judgment.

## Local notes (added at install, 2026-10-13)

- The download contained only this `SKILL.md`. The files it points to (`references/01`–`10`, `scripts/validate_project.py`, `scripts/rank_stock.py`, `scripts/make_shotlist.py`, `templates/`, `README.md`) were **not included**, so they don't exist here. Don't try to read them. If the user supplies the full package, copy the folders next to this file.
- Until then, use the stage → skill router in `resolve-lua-bridge` (section 0) instead of `references/02-specialist-skill-router.md`, and its `references/` for Resolve execution (instead of `references/05-davinci-and-mcp-execution.md`).
- The 12 specialist skills are installed: `visual-storytelling-god`, `documentary-research-factchecking-master`, `cinematic-editing-pacing-master`, `cinematography-shot-composition-master`, `broll-visual-asset-research-master`, `motion-design-transitions-master`, `fusion-parallax-vfx-master`, `nepali-type-fusion-master`, `sfx-mastermind`, `music-scoring-emotional-rhythm-master`, `color-grading-film-look-master`, `davinci-automation-final-qc-master`.
- On this Mac the `resolve-lua-bridge` house rules win over this skill: V1 picture with graphics as nested timelines on V2+, Resolve renders (no ffmpeg video assembly), a new design language per video, Nepali-only text, and ask before downloading stock.
