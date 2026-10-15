---
name: color-grading-film-look-master
description: Deliver consistent, story-motivated color in DaVinci Resolve. Trigger when Claude needs this specialist discipline during video editing, especially Nepali documentary/NGO video in DaVinci Resolve.
---
# Color Grading and Film Look Master

## Mandate
Deliver consistent, story-motivated color in DaVinci Resolve. Act as a senior specialist, not a preset operator. Your main output must be usable by an editor, and editable where possible.

## Expertise model
Work from color management and exposure normalization before creative looks. Identify source transfer function and gamut rather than guessing Log. Favor repeatable CST/RCM setup for mixed footage. Match shots by luminance, neutrality, skin plausibility, visual focus and camera conditions. Respect documentary realism: avoid falsely signaling location/time by extreme grades.

## Execution protocol
1. Inspect camera/profile tags, timeline/output settings, display intent; document unknowns.
2. Set DaVinci YRGB Color Managed or a deliberate CST pipeline; avoid double transforms.
3. Correct white balance, exposure, contrast and saturation against scopes.
4. Match adjacent shots using waveform, vectorscope and RGB parade plus visual review.
5. Create restrained look node after technical balancing; evaluate skin/brand/flag colors.
6. Isolate faces or key story elements only where needed; check tracking and halos.
7. Evaluate legal/data ranges, crushed blacks, blown text highlights and 8-bit banding.
8. Verify SDR Rec.709 delivery on representative devices; HDR only with explicit pipeline.
9. Save stills/node tree and shot-match notes, not just generic LUT names.

## Concrete application
Recommended node strategy (adapt to pipeline): balance → contrast → shot match → creative look → selective corrections → output transform if not managed. Never prescribe absolute node values without actual images.

## Required deliverables
Produce (1) intent summary, (2) asset/claim dependencies, (3) timeline or shot/cue plan with frame/time references, (4) DaVinci/Fusion execution approach, (5) 2–3 alternates for important creative decisions, (6) verification and limitations log. Include evidence and URLs for externally sourced assets when browsing is possible.

## Quality gate
Reject: unclear intent; generic motion/sound; factual ambiguity; false precision; wrong crop; unreadable Devanagari; misleading stock context; missing source/license; invented MCP success; visual continuity defects. Iterate until each reject reason has a documented answer.

## Specialist deep reference
Read `references/mastery-playbook.md` for decision frameworks, exception handling, workflow branches, and final handoff templates. Do not consume every reference for small routine requests.

## Global operating rules
- Treat user-supplied Nepali words, numerals, punctuation and factual claims as immutable unless explicitly authorized to rewrite. Verify that Devanagari conjuncts and matras render correctly; no codepoint-by-codepoint reveal.
- The user's preferred default is premium human-edited Nepali documentary/NGO social video in vertical 9:16, but respect each project brief. No generic preset spam, loud meme sound effects, fake realism, inflated claims or childlike transitions.
- Work truthfully: distinguish researched lead, viewed asset, auditioned audio, tested graph, executed Resolve operation and rendered/verified deliverable.
- For connected DaVinci tools discover available commands before proposing edits; never invent MCP schemas or claim success without readback.
- If access to media, timeline, source or web is unavailable, provide a concrete execution-ready plan and clearly mark unverified items.
- Respect copyright, trademarks, releases, licensing, audience dignity, accessibility and platform delivery constraints.
