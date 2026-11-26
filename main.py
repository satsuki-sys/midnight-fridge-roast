#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes one roast line to /output/entry.txt: a smart fridge that
refuses to open after midnight, roasted at its own door.
"""
import os

ENTRY = (
    "My smart fridge locks at midnight because a sandwich at 12:01 is, "
    "in its opinion, a cry for help."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
