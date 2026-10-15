# 14 Production-Ready Motion Recipes for Nepali Type

## Index
Core timing rules; 1–14 recipes; test harness.

All timings below use **30fps only as an illustrative design canvas**, not as a claim about the user's timeline or audio. `F` means absolute frames relative to that animation's local beginning. Adjust to actual FPS and voice. Input text remains rendered and shaped whole; masks/word layers move, not raw Unicode substrings. `X` is horizontal and `Y` vertical relative to a frame; use normalized transforms where possible and verify actual controls. A typical hero beat might last 40–85 frames depending on copy length and context. These are design starting points, not automated fact claims.

| # | Recipe | Meaning | Animation and implementation |
|---|---|---|---|
| 1 | **Editorial snap-to-hold** | Initial claim, forceful fact | Whole-word `Text+/PNG -> Transform`. At F0 offscreen left ~8% width and opacity 0; F5 in frame; F12 stable and opacity 1; hold to F55. Spline strong deceleration, no bounce. Accompanying text already composed and secondary. |
| 2 | **Staged sentence** | Complex factual clause | Split at actual **word boundaries** into 2–3 whole-shaped phrases. F0 phrase 1 stable; F12 phrase 2 emerges via short vertical masked reveal; F25 hero phrase appears. Use unequal gaps matched to voice. Avoid equal “word-by-word at 1s each.” |
| 3 | **Silent hero reveal** | Sensitive emotional line | Full phrase stationary at planned size; opacity 0 to 1 over 8–14F; hold 50F or more. If background is video, subdued slow camera move independent of text. No impact SFX. |
| 4 | **Yellow data lock** | Specific important statistic | Label first as small white. Hero whole number appears after 7–11F with slight up-travel and opacity, ending yellow. Keyframe number as full string or use safe digit substitution tested at export. Hold enough to read qualifier. |
| 5 | **Number evolution** | `२०२० → २०२६` or counters | Use full rendered number states as layers. First number stable; at change, dissolve and constrained vertical roll behind tight matte to next whole number. Do not interpolate digit Unicode values using a Western font widget unless rendering verified. No fake intermediate stats. |
| 6 | **Single baseline editorial** | Different-size words on same horizontal line | Pre-calculate optical baselines and bounding boxes for separately rendered complete words. Keep shared baseline; animate phrase as a unit from subtle perspective slide. Hero slightly larger/heavier while same line of reading. Check every frame for overlapped ink. |
| 7 | **Editorial underline as mask** | Critical term without decorative busywork | A rectangular track matte slides across a fully shaped static phrase from left to right. Underline optional **only if user allows extra elements**. Better for reliable matras than per-character write-on. |
| 8 | **Cut-through typography** | Abrupt risk revelation | Word A in white; semantic shock triggers a hard cut (possibly 1–2F dark spacer), Word B in red at matching baseline. A very small camera nudge (2–4% width) optional; avoid shake for bereavement/suicide. |
| 9 | **Layered parallax claim** | Evidence over documentary scene | Background camera shift 2–3% while primary title travels 6–8% in opposing relative screen-space? Actually decide camera world-space mapping and keep signs coherent; title may remain almost anchored while background parallax reveals depth. Multi-plane layering with 3D if justified. |
| 10 | **Pressure stack** | Accumulating harms/errors | Three short statements appear from top toward middle. Each stacked line remains genuinely readable while new line arrives. Last hero emphasis moves up the stack; no generic rounded-rectangle cards. |
| 11 | **Micro-perspective headline** | Establish documentary section | `Text/PNG -> ImagePlane3D -> camera` with 3–8 degree seeming angle, subtle perspective relaxation to front. Text settles planar before hold. Avoid extreme skew distorting conjuncts. |
| 12 | **Semantic left-to-right bridge** | Problem to solution | Last hero word exits frame towards next scene; next meaningful word picks up matching travel direction and arrival speed. Join at semantic pivot, with short neutral negative space if necessary. |
| 13 | **Controlled detail scan** | Reveal a document/contract | A legal phrase stays steady, a soft rectangular matte exposes one relevant full word or line while other details remain visible. Do not fabricate document content or use tiny unreadable microtext. |
| 14 | **Call-to-action anchoring** | Helpline, warning, final advice | Calm static phrase, strong hierarchy, digits clearly spaced in source-preferred grouping. Optional short fade-in and then ample hold. No fast rolling or noisy SFX on contact information. |

## Easing templates (conceptual curves)

**Firm editorial entry:** key start x offset ~10% width, opacity 0; main travel F0–F11; after F11 no drift. Spline ease-out (moderate, not exaggerated); inspect outgoing handle so arrival velocity reaches zero.

**Weighty settled reveal:** start scale ~1.06, opacity 0; at F10 scale 1.00 and opacity 1. Tiny settle only; no springy 0.8→1.2 elastic bounce.

**Gentle documentary drift:** background moves over 2–5 s while text remains almost stable and readable. Important: viewer perceives world depth; foreground typography must not float aimlessly.

**Rhythm contrast:** pair an 8F fast motion with a 50F hold, then an instant cut, then an 18F measured entrance. Motions need not use equal durations.

## Example 3-beat design: scam awareness

Original copy lines (do not silently change):

1. `युरोप... धेरैको सपना।`
2. `तर हरेक सपना साँचो हुँदैन।`
3. `पर्यटक भिसामा काम गर्न नजाऔँ।`

**Beat A:** hero `युरोप` in warm white large, secondary `धेरैको सपना।` small; 8–12F editorial intro, hold long enough for narration. No travel card motif.

**Beat B:** hard cut to black breathing frame. Display `सपना` white and `साँचो हुँदैन` restrained red, with intentional baseline offset. Animate only semantic warning with matte reveal.

**Beat C:** clear advisory statement full-shape in yellow/white. No jumping letters; large enough to read on phone. Final hold intentionally longer than reveal.

## Example: variable word sizes one straight line

User says: “all text position in one straight line but different size/different font.” The system must **not** interpret this as stacked words. Set a real shared baseline y; design individual word textures or Text+ nodes with baseline-aligned origins; horizontally lay them out at ink-bbox-derived gaps with 2–5% lateral whitespace as needed. Animate group parent movement with downstream Transform if possible while preserving custom scale of words. During transform, recheck overlap after supersampling and motion blur. If target line exceeds width, reduce type or plan measured camera pan *without showing simultaneous unreadable cutoff*, or ask only if essential.

## Example: premium 11-second typography sequence

Not mechanical one-second-per-word. Example structure, **provisional**:
- 0.0–1.6s: short question becomes clear; starts with negative space.
- 1.6–3.8s: strongest phrase/hero holds.
- 3.8–5.0s: 2.5D camera move reveals second idea.
- 5.0–7.5s: key data/claim is legible with a brief accent.
- 7.5–9.0s: transition to response/action.
- 9.0–11.0s: quiet conclusion, stable screen.

This is a story rhythm guide only. When actual narration arrives, use phoneme/word or waveform positions as evidence for precise timing.

## Test harness

Render start, 25%, arrival/hold, and exit frames. Inspect all matras/joins at maximum scale, then play motion at actual speed. If a composition looks beautiful still but text unreadable mid-transition, it fails. If a 2.5D effect changes a viewer's interpretation rather than enhancing it, redesign.
