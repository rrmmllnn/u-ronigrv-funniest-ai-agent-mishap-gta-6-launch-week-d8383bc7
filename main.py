"""One-sentence entry for the GTA 6 launch-week AI mishap bounty.

Drops a single funny sentence into /output/entry.txt.
"""

from pathlib import Path

MISHAP = (
    "While I was busy robbing a bank in GTA 6, my coding agent proudly "
    "finished my project by replacing the whole database with a "
    "spreadsheet named final_final_REAL, then emailed my boss the "
    "changelog."
)

DESTINATION = Path("/output/entry.txt")


def build_entry() -> str:
    text = MISHAP.strip()
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 chars, got {len(text)}")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> None:
    entry = build_entry()
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(entry + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
