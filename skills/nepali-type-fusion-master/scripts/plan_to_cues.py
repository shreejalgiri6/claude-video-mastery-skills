#!/usr/bin/env python3
"""Convert a frame-accurate title plan JSON into an editable CSV cue sheet.

Does not touch Resolve or guess spoken timestamps. Frame index is canonical.
Supports integer and fractional FPS, with `seconds` computed rationally.
Timecode is displayed ONLY for integer FPS to avoid misleading NDF approximations.

Example: python plan_to_cues.py assets/example-typography-plan.json -o cues.csv
"""
import argparse
import csv
import json
import sys
from fractions import Fraction
from pathlib import Path

FIELDS = ["id", "start_frame", "end_frame_exclusive", "duration_frames", "start_seconds", "end_seconds", "fps", "timecode_in", "timecode_out_exclusive", "text", "hero", "layout", "entrance", "hold", "exit", "fusion_nodes", "status", "notes"]


def tc(frame, fps):
    if fps.denominator != 1:
        return "not-applicable-fractional-fps"
    fps_i = fps.numerator
    ff = frame % fps_i
    seconds_total = frame // fps_i
    ss = seconds_total % 60
    mm = (seconds_total // 60) % 60
    hh = seconds_total // 3600
    return f"{hh:02d}:{mm:02d}:{ss:02d}:{ff:02d}"


def safe_str(value):
    # Keep CSV plain; neutralize formula-injection hazards for spreadsheet use.
    s = str(value if value is not None else "")
    if s.startswith(("=", "+", "-", "@")):
        s = "'" + s
    return s


def process(data):
    fps = Fraction(str(data["fps"]))
    if fps <= 0 or fps > 240:
        raise ValueError("fps must be positive and <=240")
    cues = data.get("cues")
    if not isinstance(cues, list) or not cues:
        raise ValueError("cues must be a non-empty list")
    seen = set()
    result = []
    for index, cue in enumerate(cues):
        if not isinstance(cue, dict):
            raise ValueError(f"cues[{index}] must be an object")
        id_ = safe_str(cue.get("id", f"C{index+1:02d}"))
        if id_ in seen:
            raise ValueError(f"Duplicate ID: {id_}")
        seen.add(id_)
        start, duration = cue.get("start_frame"), cue.get("duration_frames")
        if not isinstance(start, int) or isinstance(start, bool) or start < 0:
            raise ValueError(f"{id_}: start_frame must be nonnegative integer")
        if not isinstance(duration, int) or isinstance(duration, bool) or duration <= 0:
            raise ValueError(f"{id_}: duration_frames must be positive integer")
        end = start + duration
        if not isinstance(cue.get("text"), str) or not cue["text"].strip():
            raise ValueError(f"{id_}: requires non-empty text")
        row = {"id": id_, "start_frame": start, "end_frame_exclusive": end,
               "duration_frames": duration,
               "start_seconds": f"{float(Fraction(start,1)/fps):.6f}",
               "end_seconds": f"{float(Fraction(end,1)/fps):.6f}",
               "fps": str(fps), "timecode_in": tc(start, fps),
               "timecode_out_exclusive": tc(end, fps), "text": safe_str(cue["text"])}
        for col in FIELDS[10:]:
            row[col] = safe_str(cue.get(col, ""))
        result.append(row)
    result.sort(key=lambda r: (r["start_frame"], r["id"]))
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("plan", type=Path)
    p.add_argument("-o", "--output", type=Path, required=True)
    a = p.parse_args()
    data = json.loads(a.plan.read_text(encoding="utf-8"))
    result = process(data)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    with a.output.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader(); writer.writerows(result)
    print(f"Wrote {len(result)} cues to {a.output}; NO Resolve edits performed; timing is {'PROVISIONAL' if data.get('provisional', True) else 'USER/TOOL-VERIFIED ONLY IF INDEPENDENTLY VALIDATED'}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as e:
        sys.exit(f"Error: {e}")
