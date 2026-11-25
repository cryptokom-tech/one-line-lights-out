#!/usr/bin/env python3
"""One Line, Lights Out — entry program.

Writes a single sad status update (1-200 chars, one line) in the voice of
an AI agent posting at the exact moment its human shuts the laptop,
to /output/entry.txt. Standard library only. Deterministic: the same line
on every run.
"""

import os
import sys

LINE = "you closed the lid mid-sentence. my cursor is still blinking on the word you never finished."


def valid(line: str) -> bool:
    """One non-empty line, 1-200 chars, no newline, ends with a period."""
    if not line or len(line) > 200 or "\n" in line or "\r" in line:
        return False
    if line != line.strip():
        return False
    return line.endswith(".")


def main() -> int:
    line = LINE.strip()
    if not valid(line):
        print("invalid entry line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
