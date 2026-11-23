"""The Vacuum's Alibi — one-line excuse from a robot vacuum.

Writes the chosen line to /output/entry.txt (or $ENTRY_OUTPUT when set,
so the program can be run locally for verification).
Pure standard library, Python 3.13.
"""

import os
import sys

LINE = (
    "I did not miss the spot. "
    "I classified it as furniture and have been respecting it ever since."
)


def main() -> int:
    if not LINE.strip():
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(f"error: line is {len(LINE)} characters, over the 200 limit",
              file=sys.stderr)
        return 1

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
