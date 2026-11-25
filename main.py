#!/usr/bin/env python3
"""Funniest one-line out-of-office email reply.

Writes a single out-of-office auto-reply line to /output/entry.txt.

The line is self-aware about being an auto-reply: the joke turns on the
reply itself instead of the usual beach / inbox / limited-email lines,
so it lands on the first read and still reads like a message a real
person would switch on before going away.
"""

import os
import sys

ENTRY = (
    "I'm out of office — this auto-reply is the most productive "
    "thing I've done all week."
)
# No trailing newline: the gate counts every character, and the entry
# is one line of text exactly as an email client would send it.


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 160:
        print(f"entry is {len(text)} chars, must be 1-160", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
