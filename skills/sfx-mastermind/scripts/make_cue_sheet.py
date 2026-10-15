#!/usr/bin/env python3
"""Convert a real JSON spotting cue sheet to an editor-friendly CSV.

Works with positive *integer, non-drop-frame* FPS only. This script does not
fabricate cues, access libraries, verify licenses, or insert audio into a DAW.
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

COLUMNS = [
    "project", "cue_id", "timecode", "start_seconds", "event", "type",
    "priority", "query", "asset_url", "license_status", "notes",
]
VALID_TYPES = {"DIA", "FOLEY", "AMB", "DES", "MOT", "UI", "TON", "MUS", "SIL"}
TC_PATTERN = re.compile(r"^(\d{2,}):(\d{2}):(\d{2}):(\d{2})$")


def seconds_from_tc(tc, fps):
    if not tc or str(tc).strip().upper().startswith("TBD"):
        return ""
    match = TC_PATTERN.fullmatch(str(tc).strip())
    if not match:
        raise ValueError(f"Invalid non-drop-frame timecode: {tc!r}")
    hh, mm, ss, ff = map(int, match.groups())
    if mm > 59 or ss > 59 or ff >= fps:
        raise ValueError(f"Invalid timecode fields for {fps} fps: {tc!r}")
    return f"{hh * 3600 + mm * 60 + ss + ff / fps:.3f}"


def safe_csv_cell(value):
    """Prevent accidental CSV formula injection in human-authored labels."""
    text = "" if value is None else str(value)
    if text.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + text
    return text


def convert(doc):
    if not isinstance(doc, dict):
        raise ValueError("Expected a JSON object")
    fps = doc.get("fps")
    if type(fps) is not int or not 1 <= fps <= 120:
        raise ValueError("fps must be an integer 1..120 (non-drop-frame)")
    cues = doc.get("cues")
    if not isinstance(cues, list):
        raise ValueError("cues must be an array")
    rows, seen = [], set()
    for idx, cue in enumerate(cues, 1):
        if not isinstance(cue, dict):
            raise ValueError(f"Cue {idx} is not a JSON object")
        cid = str(cue.get("id") or "").strip()
        if not cid or cid in seen:
            raise ValueError(f"Cue {idx}: missing or duplicate id {cid!r}")
        seen.add(cid)
        typ = str(cue.get("type") or "").strip().upper()
        if typ not in VALID_TYPES:
            raise ValueError(f"Cue {cid}: type must be one of {', '.join(sorted(VALID_TYPES))}")
        tc = str(cue.get("tc") or "TBD").strip()
        row = {
            "project": doc.get("project", ""),
            "cue_id": cid,
            "timecode": tc,
            "start_seconds": seconds_from_tc(tc, fps),
            "event": cue.get("event", ""),
            "type": typ,
            "priority": cue.get("priority", ""),
            "query": cue.get("query", ""),
            "asset_url": cue.get("asset_url", ""),
            "license_status": cue.get("license_status", "HOLD"),
            "notes": cue.get("notes", ""),
        }
        rows.append({k: safe_csv_cell(v) for k, v in row.items()})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()
    with args.input_json.open("r", encoding="utf-8") as f:
        doc = json.load(f)
    rows = convert(doc)
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} cues to {args.output_csv}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(2)
