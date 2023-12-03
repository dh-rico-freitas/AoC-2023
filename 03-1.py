# 03-1.py
""" Advent Of Code - Day 3 Puzzle 1

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

PUZZLE = "03-1"
INPUT_PATH = "inputs/03.txt"


def main(games_file=INPUT_PATH):
    with open(games_file) as f:
        schematic = [line.strip() for line in f]

    accum = 0
    height = len(schematic)
    width = len(schematic[0])

    for i in range(height):
        number_start = None
        for j in range(width):
            if schematic[i][j].isdecimal():
                if number_start is None:
                    number_start = j
            elif number_start is not None:
                number_end = j
                if check(schematic, i, number_start, number_end):
                    accum += int(schematic[i][number_start:number_end])
                number_start = None
        else:
            if number_start is not None:
                number_end = j + 1
                if check(schematic, i, number_start, number_end):
                    accum += int(schematic[i][number_start:number_end])
            number_start = None
    print(accum)


def check(schematic, i, number_start, number_end):
    prev_x = number_start - 1
    post_x = number_end + 1

    height = len(schematic)
    width = len(schematic[0])

    candidates = (
        [(i - 1, j) for j in range(prev_x, post_x)]
        + [(i, prev_x), (i, post_x - 1)]
        + [(i + 1, j) for j in range(prev_x, post_x)]
    )
    candidates = list(candidates)
    return any(
        schematic[y][x] not in ".1234567890"
        for y, x in candidates
        if 0 <= y < height and 0 <= x < width
    )


if __name__ == "__main__":
    main()
