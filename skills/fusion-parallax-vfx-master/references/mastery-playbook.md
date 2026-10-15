# Fusion 2.5D Parallax and VFX Master: mastery playbook

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
1. Inspect actual media frame dimensions, bit depth, alpha, frame rate, and color pipeline.
2. Draw node graph before executing: layers, masks, depth, 3D scene, Renderer3D, output.
3. Cut accurate masks; inspect hair, motion blur and edge halos at 200%.
4. Fill revealed background holes, not just move foreground over black.
5. Set depth for composition, not extreme exaggerated stereo; test edge reveal throughout move.
6. Use smooth Bezier camera motion, staged focal point, restrained easing.
7. Preview full frame and vertical crop, first/middle/last, motion blur, text safe zones.
8. Cache/render intermediate passes when costly; preserve editable project.
9. Use MCP only for actions actually advertised by connected tools; get readback and saved confirmation.

## Discipline-specific doctrine
Separate imagery into independent depth layers, repair holes by painting/inpainting with inspection, maintain realistic occlusion, add subtle atmospheric perspective, and animate a virtual camera with restrained perspective. Understand that Fusion capabilities differ by Resolve edition, GPU and installed plugins. Plan native nodes first: MediaIn, Transform, Polygon/BSpline, Merge, Text+, ImagePlane3D, Camera3D, Merge3D, Renderer3D, MediaOut. Verify each node exists before scripting it.

## Test case
Example graph: BackgroundPlate → ImagePlane3D(back); SubjectRGBA → ImagePlane3D(front); Camera3D → Merge3D → Renderer3D → Merge titles → MediaOut. Write concrete transform/keyframe notes and a rollback plan.

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
