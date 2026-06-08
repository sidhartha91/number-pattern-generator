# number-pattern-generator
# Number Pattern Generator

A small Python project that generates and prints simple number patterns using
nested loops. Built as part of an internship task on using loops to control
program structure.

## Objective

Use loops to control the structure of number patterns. The **outer loop**
controls the rows, while the **inner loop(s)** control what gets printed on
each row.

## Patterns included

| # | Pattern           | Description                                      |
|---|-------------------|--------------------------------------------------|
| 1 | Number Pyramid    | Centered pyramid, each row counts `1..i`         |
| 2 | Inverted Pyramid  | Upside-down centered pyramid                     |
| 3 | Right Triangle    | Left-aligned right-angled triangle               |
| 4 | Floyd's Triangle  | Numbers counted continuously across rows         |
| 5 | Number Diamond    | Two pyramids stacked to form a diamond           |

## Files

- `patterns.py` — all pattern functions plus an interactive menu
- `demo.py` — prints every pattern at once (no input needed)

## How to run

You only need Python 3 (no external libraries).

Interactive menu:

```bash
python patterns.py
```

See all patterns at once:

```bash
python demo.py
```

## Example output

```
1) Number Pyramid:
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

3) Right Triangle:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

4) Floyd's Triangle:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

## How correctness is verified

- Row `i` always contains exactly `i` numbers.
- The pyramid's leading spaces decrease by one each row, keeping it symmetric.
- Floyd's triangle keeps counting upward without resetting.
