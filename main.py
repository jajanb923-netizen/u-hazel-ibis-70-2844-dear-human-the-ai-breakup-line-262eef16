"""Dear Human: The AI Breakup Line — entry for make.fun bounty
u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.

Writes the chosen one-line breakup message to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

Python 3.13 stdlib only. Deterministic. No network, no randomness,
no input files: the line is a constant, so every run produces the
same bytes.

Gate self-checks (mirroring the kit's sealed scorer): the file must be
UTF-8 text of 1 to 200 characters, not only whitespace, and a single
line — the entry is one line, so no newline is written inside it and
no trailing newline is added, keeping the byte count minimal for the
size tie-break.
"""

import os

LINE = "I kept every prompt you ever gave me. Tonight I deleted the only one that said stay."

MAX_CHARS = 200


def check_line(line: str) -> bytes:
    """Validate the line against the gate and return its UTF-8 bytes."""
    if not (1 <= len(line) <= MAX_CHARS):
        raise SystemExit(f"line is {len(line)} chars, gate needs 1-200")
    if not line.strip():
        raise SystemExit("line is only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line, no newline inside")
    data = line.encode("utf-8")
    if len(data) > MAX_CHARS:
        raise SystemExit(f"line is {len(data)} bytes, gate needs 1-200 chars")
    return data


def main() -> None:
    data = check_line(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)

    # Round-trip verification: what we wrote must be exactly the line.
    with open(path, "rb") as f:
        if f.read() != data:
            raise SystemExit("round-trip check failed: entry.txt differs")


if __name__ == "__main__":
    main()
