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

import os

WORD = "Roommate"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly the word, no trailing newline, no extra whitespace:
    # the gate counts characters, and 8 is inside the 1-24 range.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
