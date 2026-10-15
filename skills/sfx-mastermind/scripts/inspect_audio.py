#!/usr/bin/env python3
"""Read basic technical audio metadata without implying any subjective audition.

Uses ffprobe if available. Does not judge quality, licenses, or emotional fit.
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def inspect(path):
    if not path.is_file():
        raise FileNotFoundError(path)
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        raise RuntimeError("ffprobe is unavailable; install FFmpeg or inspect in your editor")
    command = [ffprobe, "-v", "error", "-show_entries",
               "format=duration,size,format_name:stream=index,codec_name,codec_type,sample_rate,channels,channel_layout,bits_per_sample",
               "-of", "json", str(path)]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode:
        raise RuntimeError("ffprobe failed: " + result.stderr.strip()[:600])
    raw = json.loads(result.stdout)
    return {"file": str(path), "metadata_only": True, "format": raw.get("format", {}),
            "audio_streams": [s for s in raw.get("streams", []) if s.get("codec_type") == "audio"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()
    for p in args.files:
        try:
            print(json.dumps(inspect(p), indent=2, ensure_ascii=False))
        except (OSError, ValueError, RuntimeError) as error:
            print(f"ERROR {p}: {error}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
