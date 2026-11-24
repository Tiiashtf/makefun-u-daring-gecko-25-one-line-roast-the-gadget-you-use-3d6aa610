#!/usr/bin/env python3
"""One-line roast of the gadget used every day.

Writes a single original roast (one line, <= 200 chars) to /output/entry.txt.
Stdlib only, no network, deterministic: every run writes the same bytes.
"""

import os
import shutil

ROAST = (
    "My earbuds die mid-sentence every single call, yet survive forty "
    "minutes of hold music \u2014 even they refuse to listen to my boss."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of /output, never the directory itself:
    # the grader may run with a root-owned /output inside a sticky parent.
    # Recursive cleanup handles nested stale directories, not just one level.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
