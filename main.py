#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — make.fun entry.

Writes a single roast line about a smart fridge to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

The program is fully deterministic: it takes no input, reads no files,
uses no randomness, no clock, and no network. It always writes the same
UTF-8 text, with no trailing newline.
"""

import os

ENTRY = "I asked my fridge for a snack and it showed me an ad for the cheese I already own."

MAX_CHARS = 200


def output_path():
    """Resolve the entry output path from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, over the %d-character limit"
            % (len(ENTRY), MAX_CHARS)
        )
    if not ENTRY.strip() or "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be one non-blank line")
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8", newline="") as f:
        if f.read() != ENTRY:
            raise SystemExit("round-trip mismatch: entry.txt differs from ENTRY")


if __name__ == "__main__":
    main()
