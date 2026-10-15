# Verified Devanagari Rendering and Transparent Title Workflow

## Index
Shaping hierarchy; Unicode linter; PNG renderer; Resolution/alpha; Editability tradeoffs; Mac/Resolve implementation; QA.

## 1. Renderer preference

1. **Native Text+ when proven correct** for target phrase and output. Best for live editability.
2. **Shaping-capable raster title** for phrases that fail natively; use a real HarfBuzz/RAQM/Pango/Quartz/CoreText-capable rendering engine. Our `scripts/render_nepali_title.py` uses Pillow + RAQM if available and refuses to silently run with broken shaping.
3. **Other vector-shaped text** via verified browser/SVG-to-path or external vector tools, if user requests vectors. Merely storing `<text>` in an SVG does not guarantee same shaping when imported in another app. Export/test via known renderer.
4. **Preeti/legacy encoding:** convert to Unicode with a verified conversion table, confirm words by a Nepali-reading human where high-stakes. Don't apply an English keyboard font to Unicode bytes.

## 2. Unicode linter utility

Run:
```
python scripts/validate_nepali.py --text 'वैदेशिक रोजगारी र मानसिक स्वास्थ्य'
python scripts/validate_nepali.py --file my-script.txt --json
```

It reports NFC differences, ZWJ/ZWNJ, unusual controls, and range observations. It does **not** prove correctness of Nepali spelling or automatically determine safe akshara boundaries.

## 3. Shape title to alpha PNG

Requirements: Python 3.9+ and Pillow with **RAQM** capability enabled. `python -m pip install Pillow` where permitted; verify installed build with Python check and tool runtime. macOS Homebrew/system Python installation differences exist; avoid forcing dependencies without user consent.

Example:
```
python scripts/render_nepali_title.py \
  --text 'वैदेशिक रोजगारी' \
  --font '/path/to/installed/NotoSansDevanagari-Bold.ttf' \
  --output 'title-nepali.png' \
  --canvas 1080x360 \
  --size 110 \
  --fill '#F4F3EF' \
  --align center \
  --stroke-width 0
```

**Fitted title example (long phrase):**
```
python scripts/render_nepali_title.py \
  --text 'तर हरेक सपना साँचो हुँदैन।' \
  --font '/path/to/your/license-verified/font.ttf' \
  --output 'warning.png' --canvas 1600x400 --size 130 \
  --fit --padding 32 --fill '#F4C94D'
```

### Why large high-quality PNGs?

When enlarging a small raster title in Fusion 2.5D, sharp edges blur. Generate at least final displayed dimension; for significant zoom, render at a reasonable higher size. Transparent PNG retains shaped ink, and Fusion can move, scale, perspective-transform, blur, or mask it safely without messing up conjuncts. Keep the original UTF-8 text and a `title-metadata.json` note with font file path, copyright/license status, text, canvas, source script, render time.

If output must stay editable as typography, a raster workaround is **not** a substitute for editable Text+; explicitly state and offer alternative editing process.

## 4. Transparent alpha pitfalls

- RGBA with transparent outside text, not fake transparency checkerboard baked as pixels.
- Check antialiasing against both black and white backgrounds; beware pale edge halos.
- Don't crop to shirorekha top edge; ink bounding box includes diacritical marks.
- Include optional stroke only if contrast truly requires it. Thick stroke can close Devanagari counters and become illegible.
- Ensure imported media retains RGBA/alpha. Test overlay on bright color to prove transparency.
- For partial reveals, animate a downstream rectangular matte over already fully shaped title layer.

## 5. Text positioning constraints

Raster text has bbox margins; downstream Fusion `Transform` center moves whole PNG, including transparent padding. Use alignment metadata and test optical center. A group with multiple word PNGs should share a baseline, computed per font bounding box and manually corrected for visible balance. Do not use automatic forced character spacing between conjunct components.

## 6. QA gold phrases

Run tests on strings:

```
वैदेशिक रोजगारीमा नेपाली श्रमिकहरू
आत्महत्या
काठमाडौँ
प्रश्न र उत्तर
क्षेत्र, त्रुटि, ज्ञान, श्रमिक
२०२० देखि २०२६ सम्म
मन दुख्दा लुकाउने होइन, सुनाउने हो।
```

Visually inspect for displaced `ि`, collapsed `्`, truncated `ं`/`ँ` and uneven line break. Compare with original pasted text. Have a native Nepali reviewer confirm orthography when the stakes are high.

## 7. Deliverability

For each title provide original UTF-8 text, chosen font name, verified font license/source when relevant, image dimensions, color hex, used renderer and whether shape verified, alpha checked, and where to position in Fusion. Rendering engine support is environment dependent; never claim RAQM shapes correctly unless tested in that environment.
