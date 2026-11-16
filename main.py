#!/usr/bin/env python3
"""ai-excited-01 entry: "The Jellyfish Above the City".

Copies the bundled image (entry.png, a gigantic luminous jellyfish
drifting above a neon city at dusk) to the output directory.

Reads entry.png from the same directory as this script and writes it
byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png (default /output),
creating the output directory if needed. Standard library only, no
network access, fully deterministic: the same input bytes always
produce the same output bytes. After copying, the program verifies
the output bytes match the source bytes exactly and fails loudly
if they do not, so a truncated or corrupted write can never pass
silently.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    # Guard: the judge must see exactly the bundled bytes.
    if destination.read_bytes() != source.read_bytes():
        raise SystemExit("entry.png output does not match source bytes")


if __name__ == "__main__":
    main()
