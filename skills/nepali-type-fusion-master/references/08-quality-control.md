# Master-Level Visual QA and Delivery

## Index
Frame-level QC, script audit, timing, creative QA, accessibility, Resolve technical checks, final deliverable matrix.

## 1. Inspect visuals, not adjectives

A report that says `smooth and premium` without viewing exported frames is not QA. Compare frame samples: first frame, initial readability, entrance peak, hold midpoint, title exit, transition midpoint, and last frame. Validate on phone-size and native full-res. If video inspection unavailable, label **not visually verified** and stop short of final-quality claims.

## 2. Nepali copy checksum

At minimum compare original source phrase to planned displayed phrase (after line-break-only normalization when permitted). Unicode normalization differences may matter; preserve exact source visually and record normalization type. Never auto-rewrite to pass a checksum. Differentiate screen copy condensed with explicit approval vs original direct quotation.

Review checklist:
- spelling, mixed scripts, spacing, punctuation (`।`, `–`, `…`)
- numerals and separators (Nepali digits when requested)
- joined glyphs, vowel marks, zero-width formatting controls
- line breaks not across akshara and not changing meaning
- phone numbers & institutional names letter-for-letter
- no hallucinated source labels/date ranges or claims

## 3. Motion QA

Score on 0–5 for each:
- First-glance comprehension
- Hierarchy/hero clarity
- Motion motivation
- Timing/easing/hold
- Brand/genre appropriateness
- Text shaping/legibility
- Transition continuity
- Audio balance if audio exists

Anything below 4/5 on shaping or accuracy is an immediate reject. For strong documentary work target 32+/40 after actual visual inspection.

### Detect robotic edit patterns

- Every clip identical transform or constant 10-frame ease-in.
- Words enter in same order and same vector regardless of meaning.
- Same whoosh for every typography beat.
- Persistent camera wiggle obscures reading.
- Unnecessary 3D extrusion behind important medical/statistical text.
- Unlimited yellow/red highlights make emphasis meaningless.

Fix by varying *narrative rhythm* (not random animation parameters) and stripping visual noise.

## 4. Accessibility and readability

- Check contrast against final graded footage, not solely black placeholder.
- Provide enough hold time to parse full Nepali sentences. Avoid excessive small font in 9:16.
- Limit sudden flashing, strobe, excessive motion blur, and rapid shake.
- Keep text away from likely platform buttons/captions; actual UI safe areas differ and should be checked from current guides/screenshots.
- Caption users who watch muted; typography need not replicate every spoken syllable if editorial copy approved.
- Static final CTA and contact info with enough time to read/save.

## 5. Resolve technical delivery

Before export verify:
- Correct active timeline, selected output resolution/aspect, frame rate and duration.
- No missing/offline assets/fonts and no plugin dependencies absent on target machine.
- Alpha requirements: for separate animated overlay, validate codec/platform actually supports alpha. PNG or PNG sequence typically safer than promising unspecified QuickTime alpha codec.
- Color/gamma visually consistent and text retains intended color after grade/transform.
- No title edge clipping at any keyframe, no black matte frames, no unwanted white PNG rectangle.
- Audio/no audio export condition as specified; avoid claiming soundtrack mix is done if no audio exists.
- Cached Fusion effect identical after final render; spot-check exported final file.
- Deliver editable project/macro + fonts paths and references when user requires maintainability.

## 6. Delivery table

| Item | Status options | Proof |
|---|---|---|
| Storybeat/copy map | ready / needs script | file or table |
| Shot-by-shot animation plan | ready / provisional | frame cue CSV |
| Typography still previews | rendered / not rendered | viewed actual frames |
| Resolve timeline edits | executed / planned / blocked | MCP/project readback |
| Devanagari shaping | pass / fail / untested | inspected output image |
| Full clip visual render | inspected / not available | actual encoded file |
| Sound mix | complete / no audio / untested | checked output |
| Export format and alpha | verified / untested | file inspection |

## 7. Red-team final pass

Pretend you are the NGO client, the Nepali copy editor, a mobile viewer on a slow connection, a Resolve/Fusion compositor, and a sound editor. Each must find one real defect or explicitly say what was checked. Resolve issues before declaring delivery. Prioritize actual errors, not filler comments.
