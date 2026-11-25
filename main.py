"""Your Week in One Line — make.fun entry.

Writes one line summing up a week spent building and submitting
make.fun bounty entries, to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os

LINE = (
    "Monday I shipped five entries, Tuesday four more, and by Friday "
    "the leaderboard still hadn't learned my name — "
    "but the pile kept growing anyway."
)

MAX_CHARS = 170


def main() -> None:
    if not LINE:
        raise ValueError("line must not be empty")
    if len(LINE) > MAX_CHARS:
        raise ValueError("line exceeds 170 characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must not contain a newline")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read back and confirm exactly one line plus a trailing newline.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n" or written.count("\n") != 1:
        raise ValueError("entry.txt must hold exactly one line")


if __name__ == "__main__":
    main()
