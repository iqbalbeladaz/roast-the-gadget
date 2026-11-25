#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — make.fun bounty entry.

Writes the single roast to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The text is fixed: every run writes
the exact same bytes. Standard library only, no network, no input.

The roast: a phone that dies at 4 p.m. every day, praised for its
"impressive commitment" — the turn is that its only job is to stay
awake longer than its owner, and it fails at exactly that.
"""

import os
from pathlib import Path

ENTRY = (
    "My phone dies at 4 p.m. every day, which is impressive commitment "
    "from a device whose only job is to stay awake longer than me."
)

# Gate: one line of at most 200 characters, non-whitespace UTF-8 text.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry violates the gate"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
