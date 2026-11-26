#!/usr/bin/env python3
"""One-star review, written in sap.

Writes the one-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It never writes into the repository itself.
"""

import os

REVIEW = (
    "One star: the tree dropped sap on my car, the ants unionized "
    "under it, and the bark filed ticket #4821 about my parking."
)


def build_entry():
    """Assemble the review line from its two halves."""
    return REVIEW


def validate_entry(text):
    """Check the entry against the bounty gate before writing it."""
    if not 1 <= len(text) <= 279:
        raise ValueError(f"entry must be 1-279 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")
    return text


def main():
    entry = validate_entry(build_entry())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    # Byte-level read-back: what landed on disk must equal the entry.
    with open(path, "rb") as f:
        if f.read() != entry.encode("utf-8"):
            raise ValueError("read-back mismatch: entry.txt differs from entry")


if __name__ == "__main__":
    main()
