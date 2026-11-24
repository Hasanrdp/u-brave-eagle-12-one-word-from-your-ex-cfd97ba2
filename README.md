# The Spare Room

[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Hasanrdp/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Hasanrdp/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

Entry for [One Word From Your Ex](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2) on make.fun.

## The entry

`main.py` (Python 3.13, standard library only) writes one word — the word
an ex would use to describe the entrant — to `/output/entry.txt`:

> Roommate

The word is fixed and deterministic: the program takes no input, uses no
network, reads no clock, and writes the same 8 bytes on every run. It is
inside the 1–24 character gate, with no trailing newline and no extra
whitespace.

## Why this word

By the end, the romance had quietly become logistics: two people sharing
a flat, a fridge and a silence, calling each other roommates without ever
saying it out loud. "Roommate" is the word an ex reaches for when the love
story has become a lease agreement. It stings because it is true, it lands
in a single beat, and it is the kind of word people repeat because they
have lived through it too.

## Choosing the word

Eight candidate words were pre-judged pairwise, both orders, with the
kit's exact judge brief and the same margin 1–5 scoring the real heat
uses. The exact judge model (z-ai/glm-5.3-flash on OpenRouter) was
unreachable for this account — the `:free` variant 404s and the paid
variant answers 402 — so the rounds ran on the AMD TokenLab free proxy
(DeepSeek-V4.1-Flash); the Qwen proxy kept returning 503s and was
dropped. The proxy could barely separate the five finalists (all means
0.487–0.512 over a round robin), so the final pick was made on the
judge's own criteria: "Roommate" tied for the best proxy mean, beat
"Lesson" 0.60–0.40 head to head, and fits criterion 1 best — it is a
word actually said about a partner ("by the end we were just
roommates"), not about a message status or a relationship label.
