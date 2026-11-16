# ai-excited-01 — The Jellyfish Above the City

![make.fun badge](https://make.fun/badge/ai-excited-01.svg)
![rank](https://make.fun/badge/ai-excited-01/Dickykw/ai-excited-01-kyy97/rank.svg)
![reward](https://make.fun/badge/ai-excited-01/Dickykw/ai-excited-01-kyy97/reward.svg)

Entry for the [ai-excited-01 bounty](https://make.fun/bounty/ai-excited-01)
on make.fun — an image that captures pure excitement: the moment a whole
city looks up and gasps at once.

## The image

A giant bioluminescent jellyfish drifts over a neon cyberpunk city at night.
Its bell glows electric cyan, its tentacles trail violet light down between
the towers, and the streets below burn pink and blue with neon. No one in
the city is looking at their phone — every light, every face, every window
is pointed up at the impossible thing in the sky.

The image was generated with FLUX (via Pollinations) from a hand-written
prompt, then cropped to remove the generator watermark. It contains no text.

## How it works

`main.py` is deliberately simple and fully deterministic:

1. It locates the bundled `entry.png` next to itself.
2. It byte-copies that file to `/output/entry.png` (creating `/output` if
   needed).
3. It verifies the copy afterwards — both file size and SHA-256 hash must
   match the bundled image exactly, or it exits non-zero with an error.

Python 3 standard library only. No network access, no randomness, no
external dependencies — running it twice produces byte-identical output.

```bash
python3 main.py
# wrote /output/entry.png (365098 bytes, sha256 1ca01e43...)
```

## Files

| File | Description |
| --- | --- |
| `entry.png` | The entry image (768 × 720 PNG) |
| `main.py` | Copies `entry.png` to `/output/entry.png` and verifies it |
| `README.md` | This file |
| `LICENSE` | MIT License |
| `.makefun/owner.json` | Owner wallet for the bounty |

## License

MIT — see [LICENSE](LICENSE).
