"""
Number Pattern Generator
========================

Generates and prints simple number patterns using nested loops.

Each function takes the number of rows as input and prints the pattern.
The outer loop controls the rows; the inner loop(s) control what is
printed on each row.
"""


def number_pyramid(rows):
    """Print a centered pyramid of numbers.

    Example (rows=4):
           1
          1 2
         1 2 3
        1 2 3 4
    """
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")      # leading spaces to center
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def inverted_pyramid(rows):
    """Print an upside-down centered pyramid of numbers.

    Example (rows=4):
        1 2 3 4
         1 2 3
          1 2
           1
    """
    for i in range(rows, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def right_triangle(rows):
    """Print a left-aligned right-angled triangle.

    Example (rows=4):
        1
        1 2
        1 2 3
        1 2 3 4
    """
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def floyds_triangle(rows):
    """Print Floyd's triangle (numbers counted continuously).

    Example (rows=4):
        1
        2 3
        4 5 6
        7 8 9 10
    """
    num = 1
    for i in range(1, rows + 1):
        for _ in range(i):
            print(num, end=" ")
            num += 1
        print()


def number_diamond(rows):
    """Print a diamond made of two pyramids.

    Example (rows=3):
          1
         1 2
        1 2 3
         1 2
          1
    """
    number_pyramid(rows)
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# Maps a menu choice to its function and a short label.
PATTERNS = {
    "1": ("Number Pyramid", number_pyramid),
    "2": ("Inverted Pyramid", inverted_pyramid),
    "3": ("Right Triangle", right_triangle),
    "4": ("Floyd's Triangle", floyds_triangle),
    "5": ("Number Diamond", number_diamond),
}


def main():
    print("=" * 40)
    print(" Number Pattern Generator")
    print("=" * 40)
    for key, (name, _) in PATTERNS.items():
        print(f"  {key}. {name}")
    print("  0. Exit")

    while True:
        choice = input("\nChoose a pattern (0-5): ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in PATTERNS:
            print("Invalid choice. Please pick a number from 0 to 5.")
            continue

        try:
            rows = int(input("Enter number of rows: ").strip())
            if rows <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("That's not a valid number.")
            continue

        name, func = PATTERNS[choice]
        print(f"\n{name}:")
        func(rows)


if __name__ == "__main__":
    main()
