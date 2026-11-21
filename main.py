import os
from pathlib import Path

ENTRY = (
    "Breathe slowly. The starlight arriving tonight left home before there was "
    "anyone to see it. Somewhere the sea is turning stone to sand, one wave at a "
    "time, as it has for a billion years. Nothing here is hurried. You are held "
    "inside something vast, patient, and very old."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 280 and ENTRY.strip()
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
