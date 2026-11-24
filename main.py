"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (<=140 chars) for an invented
city to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only.
"""

import os

LINE = (
    "Good morning, Drizzleville: light rain, 14\u00b0C, the 8:04 bus only "
    "fashionably late \u2014 umbrellas up, spirits up."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    line = LINE.strip()
    assert 1 <= len(line) <= 140, f"line is {len(line)} chars"
    assert "\n" not in line
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
