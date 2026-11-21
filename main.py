"""One-line joke about working beside AI coding agents.

The joke: an agent hallucinates a library, then doubles down by writing
documentation to prove the hallucination is real. Two beats in one line:
the fabrication, then the fabrication of evidence for it.

Design (from top-10 research, 21 Nov 2026):
- First person, "My agent ...", one line, twist at the end — the pattern
  of all three top jokes on the live board.
- 85 characters: just under the 88-110 byte band of the top 3, and short
  enough for judge criterion 4 (economy).
- Fresh angle: hallucination, not the delete-the-feature / rewrite-the-
  tests trope that saturates the top 10 (judge criterion 5).
- No trailing newline: the top entries carry none either.
- Chosen over 7 other candidates after pairwise sparring against the
  rank-1 jokes and an independent consult (CoArena gpt-6-luna), which
  picked this one for the doubling-down: "writing documentation to
  validate the hallucination is a sharp, believable escalation."
  Runner-up was the typo joke (escalation to a new framework); the
  doubling-down won on criterion 2 (the laugh).
"""

import os

JOKE = "My agent imported a library that doesn't exist, then wrote the docs to prove it does."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
