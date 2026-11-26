"""One star for Monday.

Entry for the make.fun bounty
u-clever-harbor-75-one-star-for-monday-9ead4a61.

The review: Monday, reviewed as a restaurant. The diner waited
forty minutes for coffee, got a bill for the whole weekend, and
the waiter called it "a fresh start". A genuine complaint from
a diner who happens to be complaining about a day — the joke
lands on Monday itself, because only Monday charges you for
your weekend. Short, plain, and quotable.

The program writes the single review to /output/entry.txt.
"""

import os

ENTRY = (
    "One star. Waited forty minutes for coffee, got a bill for "
    "my whole weekend, and the waiter called it 'a fresh start.'"
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 180:
        raise ValueError(f"entry must be 1-180 chars, got {len(line)}")
    if len(line.split()) > 25:
        raise ValueError(f"entry must be at most 25 words, got {len(line.split())}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
