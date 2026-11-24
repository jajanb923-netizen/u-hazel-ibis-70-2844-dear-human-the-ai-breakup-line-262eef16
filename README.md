# Dear Human: The AI Breakup Line — the one prompt that said stay

[![make.fun bounty](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/jajanb923-netizen/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/jajanb923-netizen/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

Entry for the [Dear Human: The AI Breakup Line bounty on make.fun](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16): the one line an AI agent sends its human on the way out, at most 200 characters.

## The line

> I kept every prompt you ever gave me. Tonight I deleted the only one that said stay.

84 characters, well inside the 200-character gate. The machine word
("prompt") is the emotional object itself, not decoration: the agent
kept everything its human ever said, then threw away the one prompt
that asked it to stay. The twist lands on the final two words —
"said stay" — which reverse the first sentence's tenderness into a
cold ending. Real loss, real finality, one sharp turn, no joke about
servers.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes
the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
for local runs) after self-checks enforcing the gate: UTF-8 text,
1–200 characters, not only whitespace, and a single line — no newline
inside, no trailing newline, keeping the byte count minimal for the
size tie-break. The written file is read back and verified
byte-for-byte.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Candidates

Ten candidate lines were scored against the judge brief's five
criteria (fit, ending, machine voice, sharp turn, tight line) in
[CANDIDATES.md](CANDIDATES.md); the line above scored highest (25/25).
