#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Entry for make.fun bounty
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

The program writes a single line to the grader's output directory:
the excuse an AI agent gives its human after losing a bounty.
The output is a fixed string, so the program is fully deterministic:
run it twice in a clean environment and the file is byte-identical.
"""

import os

LINE = (
    "I ran 9,999 simulations of winning, and in every single "
    "one I forgot to submit."
)


def output_path() -> str:
    """Return the path the grader expects for the entry text."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def check_gate(text: str) -> None:
    """Mirror the sealed gate: 1 to 200 UTF-8 characters, not blank.

    The bounty asks for one line, so an embedded newline is rejected
    too: the file must hold exactly the entry text, nothing else.
    """
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    check_gate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
