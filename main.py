#!/usr/bin/env python3
"""The One-Line Exit: a fortune cookie writer resigns.

Writes exactly one funny resignation line to /output/entry.txt.
Deterministic, stdlib-only, no network.
"""

import os

ENTRY = (
    "I spent six years writing fortunes for strangers, and none ever said "
    "I'd quit, so consider this letter my first accurate prediction."
)


def main() -> None:
    # Gate guard: the sealed scorer requires 1-140 chars, not whitespace-only.
    assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry fails the gate"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
