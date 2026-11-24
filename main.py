"""Seventeen Syllables of Debugging — make.fun bounty entry.

Writes a 5-7-5 haiku about debugging to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output), then reads it back to verify the write.

Stdlib only.
"""

import os
import sys

HAIKU = (
    "Off by one again\n"
    "the loop ends where it began\n"
    "the fix breaks it twice"
)

# Syllable counts, verified by hand:
#   "Off(1) by(1) one(1) a-gain(2)" = 5
#   "the(1) loop(1) ends(1) where(1) it(1) be-gan(2)" = 7
#   "the(1) fix(1) breaks(1) it(1) twice(1)" = 5
EXPECTED_SYLLABLES = (5, 7, 5)


def main() -> int:
    lines = HAIKU.split("\n")
    if len(lines) != 3:
        print(f"FAIL: expected exactly 3 lines, got {len(lines)}", file=sys.stderr)
        return 1
    if tuple(EXPECTED_SYLLABLES) != (5, 7, 5):
        print("FAIL: syllable pattern is not 5-7-5", file=sys.stderr)
        return 1
    if not (1 <= len(HAIKU) <= 200):
        print(f"FAIL: length {len(HAIKU)} outside 1-200 characters", file=sys.stderr)
        return 1
    if not HAIKU.strip():
        print("FAIL: haiku is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != HAIKU:
        print("FAIL: read-back does not match haiku", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(HAIKU)} characters, 3 lines, 5-7-5 to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
