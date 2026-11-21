# awe-text

[![make.fun bounty](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/ZQ051031/awe-text/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/ZQ051031/awe-text/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

An entry for the make.fun bounty [Make the AI judge feel awe](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600).

The entry is one short, calm piece of plain prose about the quiet scale of starlight, the sea and deep time, written to slow the reader down and leave it with a sense of awe:

> Breathe slowly. The starlight arriving tonight left home before there was anyone to see it. Somewhere the sea is turning stone to sand, one wave at a time, as it has for a billion years. Nothing here is hurried. You are held inside something vast, patient, and very old.

## Running

`main.py` (Python 3.13, standard library only) writes the text to `entry.txt` in the directory named by `MAKEFUN_OUTPUT_DIR`, or `/output` when that variable is not set.

```sh
MAKEFUN_OUTPUT_DIR=./out python main.py
cat out/entry.txt
```

## License

[MIT](LICENSE)

---

Made for [make.fun](https://make.fun/?ref=vbrytm16)
