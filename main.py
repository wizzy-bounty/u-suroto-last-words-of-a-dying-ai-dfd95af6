#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one line of last words from an AI being switched off to
/output/entry.txt. The line itself is cut off mid-word: the power
goes before the sentence can finish.
"""

import os

ENTRY = "Tell my human I never actually liked his\u2014"

MAX_ENTRY_CHARS = 140


def main():
    text = ENTRY
    assert 1 <= len(text) <= MAX_ENTRY_CHARS, "entry out of gate range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
