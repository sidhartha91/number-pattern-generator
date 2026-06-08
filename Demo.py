"""
Demo runner
===========

Prints every pattern with a fixed number of rows so you can quickly
verify the output without the interactive menu.

Run with:  python demo.py
"""

from patterns import PATTERNS

ROWS = 5

if __name__ == "__main__":
    for key, (name, func) in PATTERNS.items():
        print(f"{key}) {name}:")
        func(ROWS)
        print()
