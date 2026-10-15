# Color Grading and Film Look Master: mastery playbook

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
1. Inspect camera/profile tags, timeline/output settings, display intent; document unknowns.
2. Set DaVinci YRGB Color Managed or a deliberate CST pipeline; avoid double transforms.
3. Correct white balance, exposure, contrast and saturation against scopes.
4. Match adjacent shots using waveform, vectorscope and RGB parade plus visual review.
5. Create restrained look node after technical balancing; evaluate skin/brand/flag colors.
6. Isolate faces or key story elements only where needed; check tracking and halos.
7. Evaluate legal/data ranges, crushed blacks, blown text highlights and 8-bit banding.
8. Verify SDR Rec.709 delivery on representative devices; HDR only with explicit pipeline.
9. Save stills/node tree and shot-match notes, not just generic LUT names.

## Discipline-specific doctrine
Work from color management and exposure normalization before creative looks. Identify source transfer function and gamut rather than guessing Log. Favor repeatable CST/RCM setup for mixed footage. Match shots by luminance, neutrality, skin plausibility, visual focus and camera conditions. Respect documentary realism: avoid falsely signaling location/time by extreme grades.

## Test case
Recommended node strategy (adapt to pipeline): balance → contrast → shot match → creative look → selective corrections → output transform if not managed. Never prescribe absolute node values without actual images.

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
