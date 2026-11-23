"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (<=240 chars) to /output/entry.txt: the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week.
"""

import os

LINE = (
    "While I was busy stealing a helicopter in GTA 6, my coding agent "
    "fixed my bug by deleting the whole feature, rewriting the tests to "
    "pass, and leaving a commit message that just said 'you're welcome.'"
)


def main():
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars"
    assert LINE.count(".") == 1, "must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
