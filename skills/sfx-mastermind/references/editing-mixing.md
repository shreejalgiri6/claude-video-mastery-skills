# Advanced Editing, Fairlight, Mix and Delivery Playbook

Use for timeline implementation, audio cleanup, technical evaluation, DaVinci/Fairlight work, CapCut handoff, final mixes, and output quality control.

## 1. Production pipeline: protect dialogue and originals

Preferred logical stems/tracks (adapt to software, do not claim they exist):

- `DIA_NEPALI_VO` — narration; most important audible content.
- `AMB_LOCATION` — room tone/location environments; gently continuous.
- `FOLEY_ACTION` — diegetic objects, movement, hands, footsteps, luggage, paper.
- `DES_TRANSITIONS` — selective graphical motion accents.
- `DES_EMPHASIS` — rare factual reveal/hero accents.
- `TONAL_TEXT` — short abstract emotion/pressure where warranted.
- `MUS` — optional scoring, if authorized and licensed.
- `MIX_BUS` / SFX subgroup — level control/EQ/automation as supported.

Group related effects logically. Preserve originals. Name clips meaningfully (`S012_C03_paper_soft_land_v02`), not `sound3_final_NEW`. Keep a source/license manifest. If the user wants VO only with no background music, **do not add music** as an invented prerequisite.

## 2. Timing that survives a professional review

1. Confirm timeline frame rate and source audio rate; don't assume 24, 25, 30 or 60 fps.
2. Put a marker at the **actual visual event**, not simply at the nearest edit point. Frame-based targets: 25 fps is 40 ms/frame; 30 fps is ~33.33 ms/frame; 23.976 fps is ~41.71 ms/frame.
3. Align the **audible onset and perceptual attack**, not an arbitrary waveform sample where the file begins with silence.
4. Test any deliberate anticipation/lead or slight lag against picture. Do not use a fixed advance on every cue.
5. Match crescendo/air speed to velocity/easing curve. Damping often matters more than a big end-impact.
6. Use tiny fades/crossfades to avoid zero-crossing clicks and abrupt ambience gaps. Exact length depends on transient and source; avoid fading away the main attack.
7. Preserve tails if they support location; trim tails if they muddy the next narration word or cause a repeated identity.
8. Prefer waveform inspection at sufficient zoom, ears, and sync against locked picture.
9. A/B multiple likely placements including no-SFX. For serious facts, test without the effect on a phone speaker.

### When voice has not been recorded
Use markers `on phrase “...” / at first appearance of exact word / on final 3-digit number settling`, rather than pretending to know timestamps. Record `timecode: TBD—lock to VO` and update only after real footage/VO exists.

### Timestamp notation
Use `HH:MM:SS:FF @ FPS` for picture-locked cues and seconds/milliseconds for audio envelopes. Respect actual drop-frame rules and project timebase when converting; do not turn 29.97 DF into 30.00 NDF blindly. Cue-sheet code supports common integer/non-drop frame rates only and clearly identifies limitations.

## 3. Cue processing order and reasons

**Source check** → trim/sync → gain staging → corrective EQ/filter → noise repair when warranted → dynamics/transient shaping → pitch/time shape if needed → pan/space/reverb → scene automation → master QA.

Do not process automatically. Most effects should survive with trims, fades, level and occasional filter. Over-processing makes a library sound artificial.

### Gain hierarchy
- Balance the narrator for steady understandability in context; don't just normalize each clip to a number.
- Make environmental beds feel like *air in the space*, not a separate competing soundtrack.
- Give loud accents only to hero moments that can perceptually earn them; transitions shouldn't punch the listener every 1–2 seconds.
- Set clip levels listening under the **final voice loudness**. Check speech with music/SFX on, not solo.
- Use fader automation (or clip keyframes) for critical words; do not rely entirely on broad compression to solve a local masking issue.

### EQ principles
- Identify the problem before reaching for a fixed frequency. Low rumble/hiss and low-mid mud can be reduced when they are irrelevant to the effect's identity.
- Narration intelligibility depends partly on consonant energy in the presence region; harsh designed SFX or foley can mask it even if their RMS seems low.
- If a transient clashes with speech, first turn down or move it; then shorten, shape or filter. A complicated EQ notch is often unnecessary.
- Use high-pass on effects **when** excess lows interfere, not automatically on footsteps or car recordings where low frequency conveys mass.
- Use low-pass/distance filtering to place distant objects perceptually, while guarding against bland over-muffled ambience.
- Tonal tension should not hum at speech fundamentals/harmonics in a way that makes voice feel thin or phasey.

### Dynamics and transient design
- Compression can control very variable ambience or attack but can also exaggerate noise floors; use lightly and A/B.
- Limit sharp transient overs rather than maximizing every SFX. Hard limiting can flatten organic realism.
- Avoid extremely fast gating that chops natural room decay. Draw manual volume ramps when possible.
- If a sidechain duck is audible as pumping, favor manual keyframes near dialogue or smoother detector timings.
- A deep “sub impact” may disappear on phones while causing an excessive peak on headphones; choose controlled midrange body over pure sub.

### Space and stereo
- Use coherent believable acoustic size; match mono close foley with environmental reverb lightly if picture calls for it.
- Pan source movement to match picture when spatial information is useful. Some explanatory UI sounds work better dead center.
- Essential narrative information must not rely solely on left/right placement or frequencies small speakers cannot reproduce.
- Check mono sum for lost frequencies, phasey wide whooshes, and disappearing tonal beds.

## 4. Dialogue-first ducking strategy

Rank priorities: critical message/helpline > normal speech > realistic foreground foley > atmospheres > optional music > dramatic decorative cues. For each voice phrase:

- If background masks words, first try **removing one decorative sound**.
- If essential ambience, trim its spectral/dynamic masking instead of cutting to unnatural dead silence.
- Duck smoothly into important narration with clip volume keyframes; maintain natural tail rather than jerky up/down steps.
- If supported, use sidechain compression driven by narration for continuously competing beds. A/B against manual automation. Avoid deep pumping if it feels unnatural.
- Take special care with Nepali pronunciation and numerals; don't hide information between syllables or truncate a phone number.

## 5. DaVinci Resolve / Fairlight practical implementation

Blackmagic officially documents Fairlight's clip adjustments, fades, per-track EQ/dynamics, waveform editing, automation, mixer and loudness monitoring: https://www.blackmagicdesign.com/products/davinciresolve/fairlight . Availability and exact UI differ with version/edition; inspect the installed application.

**Manual workflow if using Resolve:**
1. Import licensed originals and save a duplicate timeline/version before complex changes.
2. On the Edit page or Fairlight page, create logically named dialogue, ambience, action Foley, transition and designed-texture tracks as needed.
3. Place narration first and lock the voice spine. Spot critical beats with markers aligned to actual frames/word groups.
4. Slip/cut selected portions of a longer recording; create short fades, preserve transients and use split clips to isolate the right take.
5. Adjust clip volume and pan initially; use channel mixer EQ/dynamics or effects *only when needed*.
6. Put room tone under scene cuts and crossfade the right acoustic continuity.
7. Automate beds/SFX around key words in the Fairlight timeline or automate mixer controls if appropriate.
8. Monitor the whole bus; examine loudness stats, peaks, mono and voice clarity rather than trusting a single numeric preset.
9. Review on phone/headphones and run an uncued A/B to see whether any effect distracts.
10. Export final picture/audio and required split stems if requested, ensuring licensing documentation is stored separately.

**Connected MCP workflow:** first discover tools, read the project's timeline/media/tracks/settings, dry-run plan when possible, and only then call supported actions. Never assume an MCP server exposes full Fairlight automation, plug-ins, file import, exports, or Fusion node operations. If actions are unavailable, hand off exact manual steps rather than fabricating success.

**Fusion caveat:** Fusion can animate visuals; this is not evidence it can place audio clips or edit Fairlight routing. Use the right page/tool for the right operation.

## 6. CapCut practical implementation

If editing in CapCut on Mac, inspect current interface/version before claiming an option exists. A conservative approach is to import audio, arrange SFX on separate clips/tracks as available, trim to movement, add fades, level to voice, and check on the master output. Use native audio processing options only if visible in that version. If essential advanced routing, multiband EQ, surround or true sidechaining is unavailable in CapCut, propose finishing the mix in Fairlight or another DAW; don't give fantasy controls.

## 7. File hygiene and delivery specs

Prefer lossless WAV/BWF at the project's agreed audio sample rate (48 kHz is a common video post workflow) and 24-bit when practical, while retaining source masters unmodified. A 44.1 kHz source is not automatically poor; conversion should be done with good resampling tools, not by renaming a file. Preserve original multi-channel files and separate stereo or mono edit versions as needed. MP3/AAC assets may be acceptable for preview but can reveal artifacts when repeatedly stretched or recompressed.

**Do not claim a loudness target from social-media folklore.** Use actual client/platform/broadcast specs if given. EBU R128's -23 LUFS reference pertains to its relevant broadcast context; it is **not** a universal Instagram/YouTube requirement: https://tech.ebu.ch/publications/r128 . If no delivery spec is given, avoid clipping/overs, balance voice and check listening consistency, and label your chosen measured delivery targets as project assumptions.

Recommended evidence for a professional handoff:
- Cue sheet and timeline version.
- Original source links and local filenames/asset IDs.
- License documents and attribution list.
- Mix notes/known issues and stem definitions.
- Frame rate, audio sample rate, codec/channel layout and checked render.
- Confirmation of what was actually tested (audition, imported, mixed, rendered, QC'd) vs merely planned.

## 8. Mix QA sequence

**Pass 1: no sound effects** — dialogue and music/room, understand story and identify where sound is genuinely missing.

**Pass 2: causality** — play all foley and environments only. Is every sound believable for the picture?

**Pass 3: designed motion** — add selective transitions/emphasis. Does motion feel more physical or just noisier?

**Pass 4: narration masking** — listen during all information-heavy seconds. Do names, Nepali numbers and warnings remain clear without effort?

**Pass 5: shock and fatigue** — do multiple bright swooshes, clicks, impacts, alarms or low-end boosts become irritating over 30+ seconds?

**Pass 6: technical** — clipping, pumping, abrupt ambience gaps, cut-off tails, stereo phase, clicks, hiss, unnatural material, spikes. If tools permit, inspect waveform and meter values.

**Pass 7: translation** — headphone, ordinary small speaker/phone, mono, low listening volume. Essential information must survive.

**Pass 8: ethics/license** — no fake evidentiary cues, no rights uncertainty presented as clearance, no location sound mistaken for real audio if stock/dramatized.

## 9. For machine-readable cue sheets

`scripts/make_cue_sheet.py` takes one JSON object:

```json
{
  "project":"NGO Explainer",
  "fps":25,
  "cues":[
    {"id":"S01-C01","tc":"00:00:02:10","event":"Map pins Kathmandu","type":"FOLEY","priority":"LOW","query":"soft location marker click dry","asset_url":"","license_status":"HOLD","notes":"Recheck if sound needed under VO"}
  ]
}
```

Run `python3 scripts/make_cue_sheet.py input.json output.csv` if a Python environment is available. Leave unknown timecodes blank or `TBD`; do not fabricate timings. The converter validates fields, creates seconds for common *non-drop-frame* rates, and fails on invalid frame notation. For 29.97 DF broadcasts or unusual rates, use project-native timecode handling instead of this helper.
