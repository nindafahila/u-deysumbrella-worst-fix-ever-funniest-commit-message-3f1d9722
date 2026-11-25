#!/usr/bin/env python3
"""u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722 -- make.fun entry.

The entry is one line of text: a commit message for a bug fix that
made everything worse. This program writes that line, byte for byte,
to <output>/entry.txt, so every run produces the exact same file:
deterministic, no network, no randomness, no clock. Python 3.13,
standard library only.

Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ENTRY = "fix: silence the disk alarm by deleting the database"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
