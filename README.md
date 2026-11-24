# Seventeen Syllables of Debugging

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/DizellaCapital/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/DizellaCapital/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

A 5-7-5 haiku about debugging — a [make.fun](https://make.fun) bounty entry by [@dizellacapital](https://make.fun/r/qxacafna).

## The haiku

> Off by one again
> the loop ends where it began
> the fix breaks it twice

17 syllables (5-7-5), 73 characters. An off-by-one loop that ends where it began — and the fix that was supposed to save it breaks it twice. The turn lands in the last line: the rescue becomes the second bug.

## Run it

```sh
python3 main.py  # writes entry.txt to $MAKEFUN_OUTPUT_DIR (fallback /output)
```

`main.py` (stdlib only) validates the haiku is exactly 3 lines of 5-7-5 syllables, 1–200 characters, and not only whitespace, writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), then reads it back to verify the write.
