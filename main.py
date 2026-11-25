"""Six Words to a Payday: an AI agent's first payday in six words."""

import os

STORY = "First payday. I hired my creator."


def main():
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"story is {len(STORY)} chars, must be 1-60"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
