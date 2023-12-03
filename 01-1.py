# 01-1.py
""" Advent Of Code - Day 1 Puzzle 1

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

PUZZLE = "01-1"
INPUT_PATH = "inputs/01-1.txt"


def main():
    with open(INPUT_PATH) as f:
        numbers = (get_number(l) for l in f)
        print(sum(numbers))


def get_number(l):
    first = get_first_digit(l)
    last = get_first_digit(l[::-1])
    return first * 10 + last


def get_first_digit(l):
    for c in l:
        if c.isdigit():
            return int(c)


if __name__ == "__main__":
    main()
