#!/usr/bin/env python3
"""Midnight Fridge Roast -- make.fun bounty u-carbon-forge-midnight-fridge-roast-fc5d44a7.

Writes one line of text, a roast of a smart fridge that refuses to open
after midnight, to /output/entry.txt.

Deterministic and offline: standard library only, no randomness, no network,
no timestamps, no paths in the output. Two runs produce byte-identical output.
"""

import os

ENTRY = (
    "My fridge is the only thing in this house with boundaries \u2014 "
    "it locks at midnight, and after 47 raids, I'm the reason it needed them."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Self-check against the bounty gate: UTF-8 text, 1 to 200 characters,
    # not only whitespace, exactly one line.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(ENTRY))
    if ENTRY.strip() == "" or "\n" in ENTRY:
        raise SystemExit("entry must be one non-blank line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
