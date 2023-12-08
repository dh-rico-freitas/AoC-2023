# 05-1.py
""" Advent Of Code - Day 5 Puzzle 1

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

PUZZLE = "05-1"
INPUT_PATH = "inputs/05.txt"


def main(games_file=INPUT_PATH):
    with open(games_file) as f:
        seeds_full_string = f.readline()
        _, seeds_string = seeds_full_string.split(":")
        seeds = [int(s) for s in seeds_string.split()]

        rest = f.read()
        maps = [
            [[int(n) for n in line.split()] for line in block.split("\n")[1:]]
            for block in rest.strip().split("\n\n")
        ]

        lands = seeds[:]
        for map_ in maps:
            lands = list(map(lambda s: apply_map(s, map_), lands))

        print(min(lands))


def apply_map(s, map_):
    """
    apply a map_ to the element passed.
    s: from seed, but actually is the source category
    """
    for dest_start, source_start, length in map_:
        if source_start <= s < source_start + length:
            return dest_start - source_start + s
    return s


if __name__ == "__main__":
    main()
