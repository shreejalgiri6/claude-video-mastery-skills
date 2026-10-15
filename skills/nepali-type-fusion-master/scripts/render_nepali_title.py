#!/usr/bin/env python3
"""Render accurately shaped Nepali/Devanagari UTF-8 text as transparent RGBA PNG.

Requires Python >=3.9 and Pillow with RAQM support. Does not ship fonts.
Example:
  python render_nepali_title.py --text 'वैदेशिक रोजगारी' \
    --font '/path/to/font.ttf' --output title.png \
    --canvas 1080x360 --size 112 --fit --align center

Always visually inspect the rendered output. The result is a raster image, not
native editable DaVinci Resolve Text+ content.
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from datetime import datetime, timezone

try:
    from PIL import Image, ImageDraw, ImageFont, features
except ImportError:
    sys.exit("Pillow is required. Install with: python -m pip install Pillow")


def parse_canvas(s):
    m = re.fullmatch(r"(\d+)x(\d+)", s.lower())
    if not m:
        raise argparse.ArgumentTypeError("Canvas must be WIDTHxHEIGHT, e.g. 1080x360")
    w, h = int(m.group(1)), int(m.group(2))
    if not 1 <= w <= 16384 or not 1 <= h <= 16384:
        raise argparse.ArgumentTypeError("Canvas dimensions must be 1..16384")
    return w, h


def hex_rgba(s):
    if not re.fullmatch(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", s):
        raise argparse.ArgumentTypeError("Color must be #RRGGBB or #RRGGBBAA")
    h = s[1:]
    vals = tuple(int(h[i:i+2], 16) for i in range(0, len(h), 2))
    return vals if len(vals) == 4 else (*vals, 255)


def get_font(font_path, size):
    return ImageFont.truetype(str(font_path), size, layout_engine=ImageFont.Layout.RAQM)


def text_geometry(lines, font, stroke, line_gap):
    # Bounding boxes are measured in the same shaping engine used for drawing.
    d = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    arr = [d.textbbox((0, 0), line if line else " ", font=font,
                      stroke_width=stroke, direction="ltr", language="ne")
           for line in lines]
    widths = [max(0, r-l) for l,t,r,b in arr]
    heights = [max(1, b-t) for l,t,r,b in arr]
    total_h = sum(heights) + (len(lines)-1)*line_gap
    return arr, widths, heights, max(widths), total_h


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--text", help="Literal Nepali Unicode text; use \\n for line break")
    g.add_argument("--text-file", type=Path, help="UTF-8 text file")
    p.add_argument("--font", type=Path, required=True, help="Path to legal installed OTF/TTF font")
    p.add_argument("--output", type=Path, required=True, help="Transparent PNG output")
    p.add_argument("--canvas", type=parse_canvas, default=None, help="Fixed W×H e.g. 1080x360")
    p.add_argument("--size", type=int, default=110, help="Font pixel size (default 110)")
    p.add_argument("--fit", action="store_true", help="Shrink size to fit canvas without cropping")
    p.add_argument("--padding", type=int, default=28, help="Padding on all sides")
    p.add_argument("--line-gap", type=int, default=24, help="Gap between visible ink boxes")
    p.add_argument("--fill", type=hex_rgba, default=hex_rgba("#F4F3EF"))
    p.add_argument("--stroke-fill", type=hex_rgba, default=hex_rgba("#0E1117"))
    p.add_argument("--stroke-width", type=int, default=0)
    p.add_argument("--align", choices=["left", "center", "right"], default="center")
    p.add_argument("--metadata", type=Path, help="Optional JSON metadata output")
    args = p.parse_args()
    if not features.check("raqm"):
        p.error("Pillow RAQM is unavailable. Install a build supporting libraqm/HarfBuzz; refusing broken Devanagari shaping.")
    if not args.font.is_file():
        p.error("Font file does not exist. Give an installed font file path; no fonts are bundled.")
    if args.size < 1 or args.padding < 0 or args.line_gap < 0 or args.stroke_width < 0:
        p.error("size must be positive; padding, line gap and stroke width must be nonnegative")
    original = args.text_file.read_text(encoding="utf-8-sig") if args.text_file else args.text.replace("\\n", "\n")
    original = original.rstrip("\n")
    if not original.strip():
        p.error("Text must not be empty")
    normalized = unicodedata.normalize("NFC", original)
    if normalized != original:
        print("WARNING: text is not NFC normalized; preserving source Unicode unchanged", file=sys.stderr)
    lines = original.split("\n")
    # Find a font size that can genuinely fit at the tested shaping engine.
    chosen_size = args.size
    while True:
        font = get_font(args.font, chosen_size)
        geom = text_geometry(lines, font, args.stroke_width, args.line_gap)
        boxes, widths, heights, ink_width, ink_height = geom
        target_w = ink_width + 2*args.padding
        target_h = ink_height + 2*args.padding
        if args.canvas is None or (target_w <= args.canvas[0] and target_h <= args.canvas[1]):
            break
        if not args.fit or chosen_size <= 1:
            p.error(f"Text ink + padding ({target_w}x{target_h}) does not fit canvas {args.canvas}; use --fit or larger canvas")
        chosen_size -= 1
    canvas = args.canvas or (max(1,target_w), max(1,target_h))
    image = Image.new("RGBA", canvas, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    y_cursor = (canvas[1] - ink_height)/2
    for line, (left, top, right, bottom), line_w, line_h in zip(lines, boxes, widths, heights):
        if args.align == "center":
            x_ink = (canvas[0] - line_w)/2
        elif args.align == "left":
            x_ink = args.padding
        else:
            x_ink = canvas[0] - args.padding - line_w
        # Shift by bbox extents so matras and glyphs stay inside the intended ink rectangle.
        draw.text((round(x_ink-left), round(y_cursor-top)), line, font=font,
                  fill=args.fill, stroke_width=args.stroke_width, stroke_fill=args.stroke_fill,
                  direction="ltr", language="ne")
        y_cursor += line_h + args.line_gap
    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output)
    meta = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "text": original, "text_normalized_nfc": normalized == original,
        "font_file": str(args.font), "font_px": chosen_size,
        "canvas_px": list(canvas), "ink_max_width_px": ink_width, "ink_total_height_px": ink_height,
        "align": args.align, "line_gap_px": args.line_gap, "padding_px": args.padding,
        "fill_rgba": args.fill, "stroke_rgba": args.stroke_fill,
        "stroke_px": args.stroke_width, "renderer": "Pillow RAQM/HarfBuzz",
        "editable_in_resolve": False, "font_redistributed": False,
        "visual_qc": "NOT DONE: inspect PNG at actual size and after importing to Resolve",
    }
    if args.metadata:
        args.metadata.parent.mkdir(parents=True, exist_ok=True)
        args.metadata.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(args.output), "canvas": canvas,
                      "chosen_font_px": chosen_size, "visual_qc": "required"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
