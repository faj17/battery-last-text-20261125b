#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — make.fun entry.

Writes one line of plain text (the phone battery's last text message to
the charger it waited for all day) to /output/entry.txt.

The line is built from fragments so the setup and the punchline stay
separate in the source: SETUP earns the turn, PUNCH pays it off.
"""

# Setup: the battery spent its last percent on this one message.
SETUP = "I saved my last 1% all day just to text you this: "
# Turn: the charger it waited for was never its charger at all.
TURN = "you're not even my charger, you're the vacuum's. "
# Punchline: the payoff lands in the final words.
PUNCH = "I died for a stranger."

FRAGMENTS = (SETUP, TURN, PUNCH)


def assemble(fragments=FRAGMENTS) -> str:
    """Join the fragments into the single entry line."""
    return "".join(fragments)


def validate(text: str) -> str:
    """Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text.split()) < 5:
        raise ValueError("entry must carry a real sentence, not a fragment")
    return text


def main() -> None:
    text = validate(assemble())
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
