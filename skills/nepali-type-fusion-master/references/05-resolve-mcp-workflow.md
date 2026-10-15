# DaVinci Resolve (Mac) and Claude MCP: Execution Protocol

## Index
Capability discovery; safe-edit handshake; project setup; manipulation; inspect/verify; failure paths; response contract.

## 1. Never infer tool capability from its name

User may have DaVinci Resolve 21.x Free on macOS and an MCP bridge (e.g., community repo). Those bridges vary dramatically: some read media/timelines, some add clips/markers, a few manipulate Fusion composition nodes. A tool labelled `DaVinci` does not prove keyframe editing or visual preview. **Discover actual tool manifest and argument schemas before writing code or issuing edits.** Do not pass unverified commands to an external tool.

If an MCP connection is missing/broken: say so and provide the best local executable fallback (title PNG + cue sheet + exact manual node recipe), not a fantasy `rendered successfully`.

## 2. Safe-edit handshake (ordered)

1. Query current Resolve version/tier where available, OS, session availability.
2. List permitted MCP tools and test one read-only call, such as active project/timeline info.
3. Record output dimensions, FPS (23.976 ≠ 24), timeline name, media paths, and accessible track/clip operations.
4. Ask only for essential missing source if not already attached; if no audio is given, proceed with visual storyboard and provisional frames.
5. Protect user work: duplicate timeline/project when tool supports it and permission exists; otherwise warn and minimize changes.
6. Read back text/source before edits; take baseline frame/screenshot only if tool actually returns it.
7. Try first reversible 1–2s clip with a complex test phrase.
8. Verify roundtrip: node graph/clip exists, accurate string, frames positioned correctly, render/viewer output confirmed if supported.
9. Continue batch scenes only after successful proof. Make the output reproducible.

### Capability matrix to fill before action

| Capability | Verified yes/no | How confirmed |
|---|---|---|
| Resolve connected |  | Real read-only response |
| Timeline inspection |  | API/MCP return |
| Track and clip insertion |  | Tool manifest + safe test |
| Fusion composition creation |  | Tool manifest + safe test |
| Text+/image import |  | Actual graph or clip state |
| Keyframing transforms |  | Actual keyframe readback |
| Render or still export |  | File saved + inspected |
| PNG alpha handling |  | Transparent output test |

## 3. Best-practice project structure

- Organize bins: `01_SCRIPT`, `02_VOICE`, `03_FOOTAGE`, `04_TITLES`, `05_SFX`, `06_COMPS`, `07_EXPORTS`.
- Timeline name descriptive, e.g. `NGO_Cambodia_NepaliType_V01_9x16`.
- Reserve tracks logically: source plate below; title comps above; accents and overlays on own tracks where useful.
- Use reusable anchor guides and consistent group naming, but don't impose needless folders on a short edit.
- Note project frame rate **before** conforming source. Do not switch timeline FPS mid-project without planning.
- Respect vertical deliverables and upper/lower interface overlays specific to platform. No universal TikTok/Instagram safe pixels promised.

## 4. Fusion edits

For one title:
1. Place an actual Fusion Composition or title on a timeline track that spans its intended frames.
2. Open Fusion and inspect nodes. Establish image input / transparent output / MediaOut path.
3. Test correct Nepali font and Unicode on actual Text+. If defective, use verified shaped title PNG or similar asset.
4. Build animate-only Transform and masks as separate nodes for reversible adjustment.
5. Use keyframe ranges relative to *clip local frame start*; map to timeline frame indexes explicitly.
6. Scrub the entry and hold; test alpha on nonblack background to reveal unwanted matte.
7. Render/export still/frame and visually compare to plan; adjust optical position and acceleration.

For long pieces: mass-produce title assets only once composition standards and Unicode rendering are validated. Never assume all text behaves the same; difficult clusters may differ.

## 5. Practical fallback matrix

| Blocker | Honest solution |
|---|---|
| No MCP exposed | Provide manual Resolve steps, validated PNG title asset generator + cue CSV |
| MCP can create clips but not nodes | Import pre-shaped PNGs and animate transforms via available tools, or document human step |
| Text+ shaping broken | Shape to transparent RGBA using `render_nepali_title.py`; animate image layer in Fusion |
| MCP cannot render frames | Label composition as unverified; ask for screenshot/export only if needed to complete requested validation |
| Resolve Free cannot access requested feature | Use free built-in node alternative or 2D-based compositing; do not claim Studio features |
| Font not installed | List tested source candidates and install instructions; use verified fallback with matching license |
| No narration yet | Give sequence planning and reversible animation scaffolds; leave timecode as provisional |
| Render slow | Cache/proxy where appropriate; use 2D replacements for gratuitous 3D; QA at final resolution |

## 6. Honest handoff block

Include:

```
ACTUAL WORK
- [Executed] Exact operations confirmed by tools...
- [Verified] Frame(s), filenames, clip/node readback...
- [Planned only] Fusion graph or timing not yet applied...
- [Blocked] Feature/tool/OS issue with direct alternative...
DELIVERABLES
- ...
QA STATUS
- Copy fidelity: pass / needs review
- Unicode shaping: pass / needs review
- Motion timing: pass / provisional
- Visual render review: pass / not accessible
```

Never say `I checked the timeline and it looks premium` if no actual image or render was viewed. Always distinguish asset prepared vs timeline updated vs rendered final.
