#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun bounty u-coral-404-one-line-big-laugh-328fb857.

Writes a single hilarious line (112 characters, well under the 200 limit)
to /output/entry.txt. The line stands entirely on its own: no title, no
setup, no explanation around it. It is judged on being genuinely funny,
with an unexpected turn, tight, and fresh — and it must stay within the
200-character cap.

The joke: a doctor's sensible advice (cut back on salt) met with absurd
literal compliance — crying directly into the pasta so nature takes its
course. The turn is the swap from medical advice to a weeping cook
treating his own tears as a seasoning, and the specific detail ("directly
into the pasta") is what makes it stick after one reading.
"""

import os

LINE = (
    "My doctor told me to cut back on salt, so now I just cry directly "
    "into the pasta and let nature take its course."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
