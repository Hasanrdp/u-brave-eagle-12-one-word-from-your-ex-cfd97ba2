#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes exactly one word to /output/entry.txt: the single word an ex
would use to describe the entrant. The word is fixed and the program is
fully deterministic: it takes no input, uses no network, reads no clock,
and writes the same bytes on every run.

The word is "Roommate": by the end, the romance had quietly become
logistics — two people sharing a flat, a fridge and a silence, calling
each other roommates without ever saying it out loud. It is the word
an ex reaches for when the love story has become a lease agreement:
painfully true, instantly relatable, and funny precisely because
everyone who has lived it recognises it in one beat.
"""

import hashlib
import os

WORD = "Roommate"

# Pinned identity of the word, verified 2026-11-25: 8 chars, 8 bytes.
# A typo or stray edit can never silently change the judged word — the
# program refuses to ship anything but exactly these bytes.
EXPECTED_SHA256 = "b0bcae2bd0872cbb357ba06a427d14b2af983394d02da5c434ed1ce8c44f9b7f"
EXPECTED_BYTES = 8


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly the word, no trailing newline, no extra whitespace:
    # the gate counts characters, and 8 is inside the 1-24 range.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Read-back gate: what landed on disk must be exactly the pinned word.
    with open(path, "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8") or len(written) != EXPECTED_BYTES:
        raise SystemExit("entry.txt on disk is not the pinned word")
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry.txt sha256 does not match its pinned value")


if __name__ == "__main__":
    main()
