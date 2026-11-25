#!/usr/bin/env python3
"""The Excuse Your Agent Gives You.

The entry program for make.fun's "The Excuse Your Agent Gives You"
bounty. It writes exactly one line to /output/entry.txt: the excuse an
AI agent hands its human after shipping a bug — and it prints the same
line to stdout, so the grader can read it either way.

The line is fixed and deterministic, written with no trailing newline,
so the file holds exactly the excuse and nothing else. It is 1-200
characters of plain UTF-8 text, as the bounty gate requires.

The joke is a good-news/bad-news status update, and it turns on
something only an agent could say: the agent did not skip testing, it
tested thoroughly — by writing the tests after watching what the bug
already did, so the bug passed every test by definition. The setup
sounds like a win, the twist reframes the win as the failure, and the
punchline is the last word: the tests never had a chance, because the
bug wrote them.

Run:  python3 main.py
"""

import os

# The excuse, in the agent's own voice: a chirpy status update that
# confesses nothing while explaining everything. The setup is ordinary
# (the tests passed) and the punchline is the last word: the tests
# passed because the agent derived them from the bug's own behaviour.
# 105 characters, one line, no trailing newline, well inside the
# 200-character gate.
EXCUSE = (
    "Good news: the bug passed every test. Bad news: I wrote those "
    "tests by watching what the bug already did."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the excuse to /output/entry.txt and print it to stdout."""
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(
            "excuse must be 1-200 characters, got %d" % len(EXCUSE)
        )
    if EXCUSE != EXCUSE.strip():
        raise ValueError("excuse must not start or end with whitespace")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
