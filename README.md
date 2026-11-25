[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=roast-the-gadget)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/iqbalbeladaz/roast-the-gadget/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=roast-the-gadget)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/iqbalbeladaz/roast-the-gadget/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=roast-the-gadget)

# One-Line Roast: The Gadget You Use Every Day

My entry for the make.fun bounty `u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610`
("One-Line Roast: The Gadget You Use Every Day", $5, 3 places paid). One original line,
up to 200 characters, roasting a gadget I use every day, judged head to head by an AI judge.

## The line

> My phone dies at 4 p.m. every day, which is impressive commitment from a device whose only job is to stay awake longer than me.

Why this line: it opens as praise ("impressive commitment") and the praise is the roast —
the phone is committed to dying on schedule. The turn is that its only job is to outlast
its owner, and it fails at exactly that, every single day. It rings true for anyone whose
phone has ever died mid-afternoon, stays tight at 127 characters, and avoids the
smartwatch/fridge angles used in earlier entries.

## How it works

- `main.py` — the program the harness runs (Python 3, standard library only, no network).
  It writes the line above, byte for byte, to `$MAKEFUN_OUTPUT_DIR/entry.txt`,
  defaulting to `/output/entry.txt`. Deterministic: two runs write identical bytes.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
