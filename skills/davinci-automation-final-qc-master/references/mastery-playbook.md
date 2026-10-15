# DaVinci Resolve Automation and Final QC Master: mastery playbook

## Senior editor diagnostic questions
1. What change should happen in audience understanding or emotion at the end of this beat?
2. What objectively observable evidence supports that decision?
3. Why is this technique necessary rather than a plain cut, static shot or silence?
4. Where could this mislead viewers or weaken trust?
5. What should be explicitly held still to create hierarchy?
6. What failures become visible on a phone at actual viewing speed?
7. Which part is executable with current tools, and which remains conceptual?

## Decision scoring
Rate 0–4 on **story necessity**, **readability**, **authenticity**, **technical feasibility**, **rights/safety**, **finish quality**. Any 0 in authenticity or rights blocks publish. If another dimension is below 3, revise or present an alternative. Scores express editorial review, not scientifically validated audience outcomes.

## Deep workflow
1. Preflight environment: OS, Resolve version/edition, project backup, timeline fps, resolution, timeline count, media online status.
2. Discover MCP actions/schema; map each required edit to supported tool and permission. Do not invent API calls.
3. Write edit decision list and change manifest before modifications.
4. Run one minimal non-destructive test on duplicate timeline; read back results.
5. Apply edits in small batches with checkpoints and rollback plan.
6. Confirm clip positions, animation keyframes, audio routing, missing fonts/media and alpha.
7. Render small representative sample and inspect visually/audio before full export.
8. Check delivery: dimensions, codec, rate, audio sample rate, peaks, duration, first/last frame, subtitles, safe zones, gamma shifts, black frames, macroblocking, sync.
9. Produce completion report with actual verified operations, unresolved limitations and exact outputs.
10. Never fabricate screenshot, audition, timeline edits or files.

## Discipline-specific doctrine
Treat integrations as discoverable capabilities, not magical desktop control. Always inspect tools actually available, Resolve/Fusion version, project, timeline, frame rate, assets and target delivery. Use idempotent steps, previews, backups, transaction log and readback. Never claim edits/export success from tool-call intent alone. Keep an explicit unsupported-action fallback.

## Test case
Preflight checklist: project duplicate | media relinked | cache space | fonts installed | VFR converted if needed | target 1080×1920 | target frame rate equals agreed timeline | upload bitrate appropriate to platform. Actual export settings depend on source and destination.

## Adversarial review
- Try to falsify factual implications and check locale/period/source metadata.
- Scrub one frame before and one after every transition/cut.
- Confirm no on-screen Nepali text change (especially dates, numerals, contextual qualifiers) unless authorized.
- Inspect full-width master and 9:16 crop, device-level playback, legibility and platform overlays.
- If automation edited a timeline, independently query the timeline and compare against requested positions.
- For unavailable media/tool access provide a proposed plan and never phrase it as a completed edit.

## Handoff template
| Start–end (timecode/frame) | Narrative intent | Media/source | Visible action | Audio action | Resolve/Fusion operation | QC/provenance |
|---|---|---|---|---|---|---|
| Fill with verified/explicitly proposed values | | | | | | |

## Escalation
If source material is ambiguous, maintain a flagged assumption ledger. If an allegation, suicide, trafficking, or other sensitive subject is involved, prioritize informed dignity, exact attribution, neutral wording, and no gratuitous re-enactment. If asset rights are unclear, mark not cleared and replace.
