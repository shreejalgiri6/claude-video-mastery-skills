# Devanagari Master Typography: Nepali in Motion

## Index
1. Non-negotiable shaping; 2. Script fidelity; 3. Font direction; 4. Hierarchy and optical craft; 5. Layout systems; 6. Typographic special situations; 7. Release checklist.

## 1. Non-negotiable shaping

Nepali uses Devanagari, a complex shaping script. Unicode code points are **not** animation characters. A rendered akshara may contain base consonants, virama (्), vowel signs, conjunct forms, repha, rakar, nasal marks, and zero-width format controls. Rendering engines combine or reorder these. A naïve per-codepoint Typewriter, character-spacing effect, or string slicing can detach a matra or break a conjunct.

- Always keep Unicode text in canonical normalized form (usually NFC) for comparisons. Keep the **original visible wording** intact.
- Do not animate by `list(text)`, `text[i]`, or blind codepoint count. Even regular-expression Unicode grapheme clusters are not guaranteed to match the professional *editorial animation unit* for all conjuncts. Whole-word / whole-line shaped layers or wipe mattes are safest.
- Test combinations: `क्ष`, `त्र`, `ज्ञ`, `श्र`, `र्क`, `क्र`, `प्र`, `स्त्र`, `हृ`, `श्रे`, `नेपाली`, `वैदेशिक`, `आत्महत्या`, `श्रमिक`, `काठमाडौँ`.
- Examine pre-base vowel signs (`कि`, `वि`), vowel marks above/below, chandrabindu, anusvara, nukta where used, and punctuation spacing.
- The headline/bar above Devanagari (shirorekha) must not be clipped by tight masks, crop boxes, glow, or motion blur.
- ZWJ and ZWNJ are invisible but can influence joining. Never auto-remove them from provided text; flag them for review.
- Legacy keyboard font encodings (e.g., Preeti) are not interchangeable with Unicode. Ask for legitimate source mapping/conversion when given legacy-encoded bytes, and visually audit conversion.

## 2. Script fidelity and editorial language

- Source copy is the legal/creative ground truth. Do not rewrite `रोजगारी`, `जोखिम`, names, helplines, numbers, or quote marks to fit a slide.
- Recommend meaningful line breaks at grammatical boundaries, not within compounds/conjuncts. Nonbreaking thematic pairs can stay together.
- Use Nepali danda `।` when supplied; do not silently swap to period. Preserve en dash, em dash, hyphen and curly quotation marks in original.
- Mixed language: preserve proper nouns like `NRNA`, `WhatsApp`, and institutional acronyms exactly unless explicitly Nepali-only asked; when Nepali-only, offer transliteration separately, not as silent substitution.
- Use actual Nepali digits when requested; verify commas and local number grouping. A number motion like `२०२० → २०२६` must never show a corrupted transitional glyph.
- Sensitive subject terms `आत्महत्या`, `मृत्यु`, `ठगी`: consider dignity, context, and restraint. The dramatic treatment should never trivialize the subject.

## 3. Font direction (candidates; install and test before use)

| Role | Consider | Creative use | QA concern |
|---|---|---|---|
| Editorial modern display | Anek Devanagari | variable-weight headlines, bold numeral statements | verify variable-font handling in current Text+ on current machine |
| Neutral authoritative | Noto Sans Devanagari | clean headings, public service information, readable numerals | ensure exact family face/weight availability |
| Humanist/approachable | Mukta | empathetic NGO scripts, medium-weight paragraphs | glyph height and long word width |
| Compact informational | Hind | dense data captions and contextual lines | check size/weight and matra clarity |

The type designer tests the *actual target renderer* (Fusion Text+, Title, shaped PNG), not just a specimen website. Every source font has its own license; consult upstream OFL when relevant. **Do not include or redistribute font files with this skill.**

### Two-role rule
- Display role: 1 family / 2 weights max during a beat, perhaps heavy + regular.
- Information role: lighter compatible weight; small text should remain comfortably readable on a phone.
- Use differences in **scale, weight, whitespace and placement** more than ornamental fonts. Avoid a dozen unrelated fonts.
- Prefer using the same family across Nepali and mixed Latin phrases where support/fit allows.

## 4. Hierarchy and optical craft

A robust default for vertical 1080×1920 (adapt after preview):
- Essential hero phrase often ~80–155 px rendered depending on length, weight, safe area; one-word hero may be larger.
- Supporting sentence often ~47–83 px. Legal/source/helpline copy may need a different readable composition instead of simply shrinking.
- Maintain generous side safety (roughly 90–120 px as an **initial design value**, then check current app UI overlays and framing).
- Treat text blocks by *visible ink bounds*, not font-size assumptions. A `120px` font does not always yield 120px tall lettering.
- Let vowel markers and descenders breathe: use ink-bbox measurements / visual test before tight line leading.
- Optical center is rarely the mathematical center. Adjust by eye based on ascender marks, negative-space distribution, and neighbor words.
- Single-line mixed typography: align **baseline and visual rhythm**, not bounding boxes alone. Avoid putting unrelated words on separate vertical levels if user says one straight line.

### Emphasis ladder
1. Plot claim (critical word) = big and strong.
2. Supporting phrase = medium/clear.
3. Source qualifier = subdued but present.
4. Safety line or hotline = high contrast, stable hold, no rapid count animation.

Never style more than 1–2 hero concepts per screen. If all words are loud, none is loud.

## 5. Signature composition systems

**Editorial anchor:** Large hero anchored ~lower-middle, small qualifier left or above; preserves strong editorial hierarchy.

**Single-baseline tension:** An entire phrase on one horizontal line; 1–2 words change scale/weight. Supports modern typographic social references. Avoid overlaps and unrealistic character-level font substitutions.

**Progressive question:** Wide small question word high; enormous revealing answer lower; intentional suspense.

**Split meaning:** Contrasting semantic terms near left and right but aligned by deliberate eye flow; title never scatters into disconnected random positions.

**Number as subject:** A single large numeral sequence with modest textual descriptor and citation. Use whole-text swaps or safe numeric transitions, not codepoint morphed matras.

**Quiet declaration:** Centered restrained medium weight; near-zero decoration, long hold. Appropriate for closing moral lines and mental health.

**Narrative stack:** At most 2–3 stacked clauses with meaningful chronological logic. Do NOT default to a three-card format or fake mobile-app tiles.

## 6. Broken-rendering response

If Fusion breaks vowel signs, glyph joins, or layout:
1. Check actual font family and Unicode source first.
2. Test Text+ with a deliberately challenging phrase, inspect high-resolution exported frame.
3. If still wrong, render via a shaping-capable engine (Pillow + RAQM / HarfBuzz/Pango / browser engine); export high-resolution alpha PNG per **complete shaped text layer**, then animate the layer's position/opacity/masks in Fusion.
4. Use a narrow, safe matte over finished text to simulate writing, not an evolving broken Unicode string.
5. Mention the tradeoff: PNG is not natively editable Text+. Keep exact source text, font name/weight, and generated source art in the package.
6. Never claim a shaping solution has been tested inside user's Resolve without inspecting the output.

## 7. Release checks

Check `कि`, `क्त`, `प्र`, `श्र`, `र्क`, Nepali numerals, punctuation, glyph tops, line wrapping, visible words vs source copy, subtle letter overlaps, safe-zone width, and 100% preview. Watch for invisible punctuation changes during copy/paste or SRT imports. No approval until exact source-to-output text audit passes.
