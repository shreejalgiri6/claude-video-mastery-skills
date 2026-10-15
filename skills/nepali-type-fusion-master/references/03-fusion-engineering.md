# Fusion Engineering: From Static Type to Professional Motion

## Index
1. Architecture, 2. Node patterns, 3. Keyframes and curves, 4. Matting and depth, 5. Text+ vs shaped art, 6. Reuse, 7. Troubleshooting.

## 1. Know the actual context

Fusion compositions are node graphs. Some nodes and API operations vary by Resolve version/tier. The artist must inspect actual tool names and node behaviors. Common concepts include `Text+`, `Transform`, `Merge`, `Background`, `Rectangle`, `Blur`, `Drop Shadow`, `ImagePlane3D`, `Camera3D`, `Merge3D`, and `Renderer3D`. Blackmagic documents Fusion text animation and 2D/3D title possibilities; exact controls / availability must be verified on machine.

DO NOT paste untested .setting blob claiming compatibility with Resolve 21. When tool execution is requested, build the smallest possible proof composition and render one frame.

## 2. Reliable 2D graph patterns

### A. Floating crisp text on footage
```
MediaIn ------------------------- Merge1 (BG) -> MediaOut
Text1 -> Transform1 ------------- Merge1 (FG)
```
Set Text1's generated frame/transparency correctly. Animate Transform1 (Center/Size/Angle) and Text+ opacity/shading or a downstream dissolve as verified. Clip input may be absent in a standalone Fusion composition; adapt graph accordingly.

### B. Background-free text overlay
```
Text1 -> Transform1 -> MediaOut
```
The title must render transparent outside glyphs. If source text has a solid Background node, set alpha=0; do not accidentally composite opaque black.

### C. Revealed shaped text via matte
```
Text1 or MediaIn_PNG -> Transform1 -> Merge1 (FG)
Background/Footage ----------------> Merge1 (BG)
Rectangle1 ------------------------> Merge1 (mask, suitable input)
```
Place the mask on a node that supports it and verify if mask coordinates are local or downstream space. Animate mask position/width across **complete shaped text**, keeping the actual text constant. Avoid direct per-codepoint Typewriter on untested Devanagari clusters.

### D. Multiple independently moving whole-word layers
```
WordA -> TransformA -> MergeA -> MergeB -> MediaOut
WordB -> TransformB ----------> MergeB (FG)
```
Arrange merges with a clear background chain. Node naming: `TXT_01_RISK`, `MOVE_01_RISK`, `TXT_02_CONTEXT`, `MASK_01_REVEAL`, etc. This is maintainable and debuggable.

## 3. Easing is choreography

Use Spline Editor for position/scale/opacity and inspect how two dimensions change together. Professional defaults by role:
- Entrance: quick acceleration or confident decelerating entry; should stop on a stable optical landing.
- Settle: tiny overshoot only for lively concepts; never physical bounce on serious loss or tragedy.
- Transition: outgoing focal element leads eye towards new focal element; not two independent contradictory moves.
- Hold: actual stillness. Avoid continual floating just to fill time.

**Illustrative 30 fps beat**, provisional until voice sync:
- F0–F4: pre-roll/offscreen position (or invisible), ensure not oddly clipped.
- F5–F13: enter with eased translation + opacity rise, no large scale bounce.
- F14–F52: stable hold.
- F53–F63: exit following camera's next direction, or hard cut if more powerful.

Change these timings for project FPS and word length. A 3-word long conjunct-heavy line may require a longer hold than the above. Curves should be tuned visually; a timing formula isn't a substitute for review.

## 4. 2.5D spatial realism

Create convincing parallax only with actual layered imagery/text and a coherent virtual camera. Two strategies:

**Simple 2D parallax:** several layers through `Transform` nodes with different relative travel distances; background travels least, foreground most. Add very subtle relative scale/blur. Keep the plane positions and movement consistent.

**True Fusion 3D (when available and justified):**
```
Text+ or alpha Image -> ImagePlane3D -> Merge3D -> Renderer3D -> Merge2D -> MediaOut
                                   Camera3D ---^
```
This is a conceptual graph; confirm exact connections and lighting behavior. Place near/far layers at distinct Z depths. Camera should translate modestly rather than distort typography grotesquely. Render a clean title at end.

A 3D plane containing a **correctly rendered PNG** is often safer for Devanagari than relying on 3D extrusion of a faulty Unicode Text+ render. Real motion blur can make fine vowel signs illegible; limit appropriately.

### Depth language
- Foreground text: high contrast, crisp, stays legible.
- Background: subdued / slower moving to imply dimension.
- Middle subject: supports scene, not competing with information.
- No arbitrary dramatic camera roll. Perspective does not automatically equal premium.

## 5. Text+ and Unicode safety

Test typing or pasting `वैदेशिक रोजगारीमा नेपाली श्रमिक`, `त्र`, `र्क`, `काठमाडौँ` before full build. If rendering fails, do not solve by adding random kerning or splitting characters. Replace text generator with shaped full-phrase PNG. Rebuild mask movement at image level. With entire phrase rasterized, changes require rerender; preserve text source and font metadata.

For text in **one straight line but different sizes**: use multiple independently typeset full-word layers sharing one intended baseline and optically adjusted positions. Changing font size per character with a faulty shaping engine could corrupt glyph joins. Render each formatted segment separately and verify gaps; animate as a coordinated group.

## 6. Production hygiene and asset management

- Each scene: one logical Fusion comp (unless user wants scene-wide structure), clearly named nodes.
- Use named controllers or exposed settings if building reusable custom titles, but test on target version.
- Save fusion setting / macro only once proven. Document editable parameters and fonts.
- Avoid nesting expensive effects where one shared layer would suffice.
- Keep 2D motion blur moderate; verify alpha edge quality after transform.
- Render reduced-resolution proxies for speed if needed, always final-check at native output.
- For long lines, use large raster titles so PNG movement doesn't soften at maximum zoom.

## 7. Troubleshooting ladder

1. Is the correct clip/timeline selected? Node graph connected to the actual MediaOut?
2. Correct alpha handling (no black/white rectangle behind title)?
3. Project resolution, timeline aspect and title resolution match expected frame?
4. Are keyframes on correct Transform node, not global unrelated track transforms?
5. Are masks clipping matras at highest/lowest position?
6. Are Devanagari glyph joins correct at frame 1, middle, and end?
7. Do motion curves start and stop smoothly? Does a downstream scale introduce blur?
8. Any render-cache artifact? Retest with cache disabled if permitted.
9. Does Free edition provide this effect? If not, switch to core tools.
10. If tool can't modify Fusion: provide exact node map and manual recreation steps, label **not executed**.
