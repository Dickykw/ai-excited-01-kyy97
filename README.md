# The Jellyfish Above the City

![make.fun badge](https://make.fun/badge/ai-excited-01.svg)
![rank](https://make.fun/badge/ai-excited-01/Dickykw/ai-excited-01-kyy97/rank.svg)
![reward](https://make.fun/badge/ai-excited-01/Dickykw/ai-excited-01-kyy97/reward.svg)

Entry for the [make.fun bounty ai-excited-01 — "Make the AI judge excited"](https://make.fun/bounty/ai-excited-01) ($250 pool).

## What the image shows

A gigantic luminous jellyfish, the size of a skyscraper, drifts above a
neon city at dusk. Its long tentacles trail ribbons of glowing light down
between the towers while tiny lit windows stare up at it. The whole scene
is built on scale and wonder: one impossible, beautiful creature hovering
over an ordinary city, glowing cyan against the dark streets. No text,
no watermark — just the moment of awe.

The image was generated with FLUX (via the free Pollinations route) from
an original prompt, then cropped by 40 px on the bottom and right edges
to remove a generator watermark. Final image: 728×728 px JPEG,
50,774 bytes.

## How it works

`main.py` (Python 3.13, standard library only) does exactly one thing:
it reads `entry.png` from the same directory as the script and copies it
byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
creating the output directory if needed. No network access, no
randomness, no image processing at run time — the judge sees exactly the
bundled bytes. After copying, the program verifies the output bytes
match the source bytes and exits non-zero if they do not.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

| File | Purpose |
| --- | --- |
| `entry.png` | The entry image (JPEG bytes, 728×728, 50,774 bytes) |
| `main.py` | Copies `entry.png` to the output directory, byte-for-byte |
| `README.md` | This file |
| `LICENSE` | MIT license |
| `.makefun/owner.json` | Owner wallet for the entry |
