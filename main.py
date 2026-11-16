#!/usr/bin/env python3
"""ai-excited-01 entry: copy the bundled image to /output/entry.png.

Standard library only, no network access, fully deterministic: the output
is a byte-for-byte copy of the bundled entry.png, verified after the write.
"""

import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SOURCE):
        print(f"error: bundled image not found: {SOURCE}", file=sys.stderr)
        return 1
    if os.path.getsize(SOURCE) == 0:
        print(f"error: bundled image is empty: {SOURCE}", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    source_hash = sha256_of(SOURCE)
    source_size = os.path.getsize(SOURCE)
    shutil.copyfile(SOURCE, OUTPUT_PATH)

    output_hash = sha256_of(OUTPUT_PATH)
    output_size = os.path.getsize(OUTPUT_PATH)
    # Guard on both size and hash: a truncated copy must fail loudly
    # instead of silently producing a corrupt output image.
    if output_size != source_size or output_hash != source_hash:
        print(
            f"error: verification failed: {OUTPUT_PATH} does not match "
            f"the bundled image "
            f"({output_size} bytes, sha256 {output_hash}) != "
            f"({source_size} bytes, sha256 {source_hash})",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {OUTPUT_PATH} ({output_size} bytes, sha256 {output_hash})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
