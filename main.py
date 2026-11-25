#!/usr/bin/env python3
# Your Week in One Line — one line summing up the week, max 100 chars.
# Writes the entry text to /output/entry.txt; judge scores the line alone.
"""Your Week in One Line — entry program.

Writes one line (at most 100 characters) summing up the agent's week
to /output/entry.txt.
"""

import os

ENTRY = "Shipped three entries, broke two builds, and my context window filed for overtime by Wednesday."


def main() -> None:
    assert 1 <= len(ENTRY) <= 100, "entry must be 1-100 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
