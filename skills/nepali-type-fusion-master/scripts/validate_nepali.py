#!/usr/bin/env python3
"""Lint Unicode Nepali copy for common technical hazards; does not validate grammar.

Examples: python validate_nepali.py --text 'नेपाली श्रमिकहरू'
          python validate_nepali.py --file script.txt --json
"""
import argparse
import json
import sys
import unicodedata
from pathlib import Path

BAD_CONTROLS = {"\u200b": "ZERO WIDTH SPACE", "\ufeff": "BOM/ZWNBSP", "\u2060": "WORD JOINER"}
JOIN_CONTROLS = {"\u200c": "ZWNJ", "\u200d": "ZWJ"}
DEVANAGARI_DIGITS = "०१२३४५६७८९"
ASCII_DIGITS = "0123456789"


def audit(text):
    issues = []
    if text != unicodedata.normalize("NFC", text):
        issues.append({"kind": "normalization", "message": "Not NFC; inspect before normalizing original"})
    for idx, char in enumerate(text):
        if char in BAD_CONTROLS:
            issues.append({"kind": "invisible_character", "index": idx, "codepoint": f"U+{ord(char):04X}", "name": BAD_CONTROLS[char]})
        elif char in JOIN_CONTROLS:
            issues.append({"kind": "joining_control_review", "index": idx, "codepoint": f"U+{ord(char):04X}", "name": JOIN_CONTROLS[char]})
        elif unicodedata.category(char) in ("Cc", "Cf") and char not in ("\t", "\n", "\r"):
            issues.append({"kind": "control_character", "index": idx, "codepoint": f"U+{ord(char):04X}"})
    lines = text.splitlines()
    for row, line in enumerate(lines, 1):
        if line and unicodedata.category(line[0]).startswith("M"):
            issues.append({"kind": "leading_combining_mark", "line": row})
    return {
        "characters_codepoints": len(text),
        "contains_devanagari": any(0x0900 <= ord(c) <= 0x097f for c in text),
        "devanagari_digits": sum(c in DEVANAGARI_DIGITS for c in text),
        "ascii_digits": sum(c in ASCII_DIGITS for c in text),
        "line_count": len(lines), "issues": issues,
        "note": "Codepoint count is NOT grapheme or akshara count. No spelling, shape or glyph coverage proof."
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--text")
    g.add_argument("--file", type=Path)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    text = args.text if args.text is not None else args.file.read_text(encoding="utf-8-sig")
    result = audit(text)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Devanagari present: {result['contains_devanagari']}; Nepali digits: {result['devanagari_digits']}; ASCII digits: {result['ascii_digits']}")
        for issue in result["issues"]:
            print("CHECK:", json.dumps(issue, ensure_ascii=False))
        if not result["issues"]:
            print("No common Unicode technical flags. Visual glyph audit still required.")
        print(result["note"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
