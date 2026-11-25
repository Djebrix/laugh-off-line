#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes exactly one funny line to entry.txt.

Stdlib only, no network, deterministic.
"""

import os

LINE = "My Roomba left me for a neighbor who actually picks things up."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
