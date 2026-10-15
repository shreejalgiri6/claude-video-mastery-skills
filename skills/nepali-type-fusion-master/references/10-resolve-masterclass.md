# DaVinci Resolve Masterclass: Full Edit → Fusion → Color → Fairlight → Delivery

## Index
Project pipeline; editing grammar; Fusion integration; color; Fairlight; sound-to-motion sync; performance; delivery/export; diagnostics; collaboration.

This guide adds broad professional Resolve editing expertise to the typography-specific manuals. It is **version/tier aware**. Verify every operation against the current app and MCP/API before claiming support. Resolve Free and Studio differ. Never assume the availability of Studio-only effects or plugins.

## 1. Project diagnosis and technical setup

Before making edits, read or ask only for missing essentials:
- Timeline frame rate, source FPS and constant/variable FPS; output 1080×1920, 2160×3840, or custom deliverable.
- Color management mode, source camera color space, timeline/output space, and whether footage is SDR or HDR.
- Existing timeline or a new project; audio sample rate; voice-over status; caption language; asset locations.
- Mac hardware performance and storage constraints. Proxy workflow vs render cache needs.
- Resolve version, Free/Studio, available plugins/macros/fonts, MCP permissions.
- User's specific reference style (including exact text positions) before designing.

Deliver a `TECH SHEET` with only facts discovered from actual project/tool results. Never invent current settings.

## 2. Edit/Cut page: story-aware high-retention sequencing

- Build a **radio edit** first when narration exists: clarify argument, remove redundancy, maintain truthful quote/audio meaning.
- For unrecorded voice, storyboard provisional scene durations; do not fabricate phoneme precision.
- Mark hook, evidence, emotional pivot, advice, and CTA. Assign different energy levels to each.
- Use L-cuts and J-cuts where narration and image context benefit; avoid using them as an automatic preset.
- Track hierarchy: footage foundation; title compositions; accent art if permitted; subtitles; audio voice; ambience; music; spot SFX.
- Protect project and preserve source audio. Use compound clips deliberately—only if maintainability and transition logic demand.
- Match movement direction across adjacent transitions. A heading moving left as the next scene moves right can feel disconnected unless intentional.
- Make hard cuts with negative space part of the toolkit. Not every cut needs zoom, whip, or whoosh.
- On Reels, verify first meaningful text appears quickly but remains readable and uncropped by mobile UI.

### Scaffolding from a narration transcript

For every sentence produce: sentence source (unaltered) → speaker time span (if supplied/verified) → visual thesis → primary type → supporting footage/asset → transition vector → SFX and mix note. Use user-provided words exactly; do not time a waveform you have never accessed.

## 3. Fusion page: engineered compositions

- Use node naming consistent with scene intent; one clear output to `MediaOut`.
- `Text+` where glyph shaping is correct; shaped PNG/texture fallback otherwise.
- Prefer grouped transforms, clean masking, keyframe curves, restrained motion blur.
- Reuse demonstrated `Transform`, `Merge`, `Rectangle`, `Text+`, `Background` and optionally 3D nodes when target edition/tool support confirmed.
- Build 2.5D with true layer separation and coherent camera behavior. Flat footage with a random skew is not convincing parallax.
- Design transitions as continuity: graphic flow, matched perspective or shared motion direction. Keep important words stable and legible.
- Optimize costly compositions by simplifying nodes and testing render speed; avoid expensive blur chains at 4K unless necessary.
- Keep animations reversible and reconstructable from parameter notes and cue-sheet frames.

## 4. Color page: protect message and source truth

- Confirm input transform/color management before grade. Do not apply log LUTs blindly to Rec.709 footage.
- Establish neutral baseline and consistent contrast across shots. Ensure highlights/shadows preserve information important to documentary context.
- Grade mood through disciplined tonal separation, not automatic teal-orange or crushed blacks.
- Titles' intended yellow/red/off-white should remain distinct against each shot; final check after color transforms and any output LUT/gamma pipeline.
- Masks/qualifiers for footage should not introduce abrupt tracking halos around subjects. If essential tools are Studio-only, propose simpler node corrections.
- Assess on calibrated/known display if high-stakes delivery; screenshot previews can hide mismatches.

### Useful grade order (illustrative)

Input normalization → exposure/white balance → primary contrast → careful selective corrections → creative look → output transform per chosen management. Actual color-managed project topology can change where transforms belong; do not duplicate CST transforms without examining settings.

## 5. Fairlight page: intentional audio and typographic impacts

Audio is part of the edit, not a sound on every motion:
- Dialogue first. Remove gross noise safely; preserve natural voice texture.
- Balance voice, music and SFX through gain staging and monitoring, not arbitrary plugin settings.
- Use fades and room tone to hide edit seams when needed. If music bed competes with speech, reduce/duck it.
- SFX belongs on semantic events: a reveal, location change, document scan, or narrative turning point. A letter simply appearing does not require a whoosh.
- Prefer soft clicks, low-level tonal movement, organic movement or silence over cartoonish impacts in NGO documentary scenes.
- Validate peak/true-peak and integrated loudness against the actual requested delivery/platform spec; do not invent a universal Instagram loudness number.
- If no audio is present, do not claim mix completed. Place proposed events in a cue sheet and mark them provisional.

### Type-audio sync method

When voice is present: identify word phrase emphasis and start/end times from actual transcript/time alignment or manually inspected waveform. Place hero phrase **just before or on intelligible emphasis** depending on visual comprehension. Audio anticipation can work, but inspect the actual result. Avoid placing loud SFX over consonants essential to understanding Nepali speech.

## 6. Resolve performance and maintainability on Mac

- Check actual source codec and whether generation of proxies improves performance; use supported lower-bandwidth proxy codecs if needed.
- Keep GPU-heavy Fusion effects isolated so one title does not make entire timeline unresponsive.
- Use appropriate Fusion render cache for complex comps, but final QA against cache invalidation/render is required.
- Store generated titles with stable file names; never change PNG canvas dimensions after placing many comps without updating transforms.
- Archive source copy, plan JSON, cue CSV, title image assets, all project dependencies and font names/licenses (not font files by default).
- Avoid destructive or unattended mass relinking via an unverified MCP integration.

## 7. Delivery, export, and technical review

**Normal reel:** Export platform-suitable resolution/frame rate and an accepted codec/container chosen from actual options. Avoid promising specific H.264 bitrates without confirming assets, runtime and platform needs. Confirm text is sharp post-compression and no missing tail frames.

**Alpha overlay:** Choose an output that demonstrably carries alpha on that installation/codec; PNG sequence is a broadly portable fallback. H.264 MP4 does **not** generally preserve alpha; do not label an ordinary MP4 "transparent".

**Editable handoff:** Include Resolve project or `.drp` if genuinely exported, plus imported assets, macros/settings if tested, exact font family names, location of media. Do not imply PNGs preserve native editable text.

**Quality review:** Watch the encoded video. Ensure end slate duration, Nepali diacritics, safe zones, grade consistency, voice legibility, effect seams, missing frames and acceptable file properties. State if the final export was not inspected.

## 8. Diagnosis when edits are underwhelming

If user says "looks like a 10-year-old edited it":
- Check whether every title uses same preset, overshoot, identical scale from 0, color noise, and generic woosh.
- Run an editorial pass removing half the unnecessary motion.
- Fix type size, baseline, eye-path and hold time before adding more Fusion effects.
- Replace random camera shakes with motivated layer depth and a meaningful transition relationship.
- Rebuild animation curve so elements accelerate/decelerate with weight.
- Use physical SFX only on purposeful events, no childish chirps.
- View five consecutive cuts in sequence. A beautiful single shot can still destroy pacing if repeated five times.

## 9. Handoff promise boundary

The Skill can plan and produce instructions/utilities, and a connected Claude assistant **may** execute operations that its real Resolve tools expose. It cannot grant support for functions absent in the community bridge. Distinguish: `project modified`, `asset generated`, `node graph proposed`, and `video export inspected` as four separate states. A professional editor does not collapse them into "done".
