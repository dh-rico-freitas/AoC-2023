# 05-2.py
""" Advent Of Code - Day 5 Puzzle 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

PUZZLE = "05-2"
INPUT_PATH = "inputs/05.txt"


def main(games_file=INPUT_PATH):
    with open(games_file) as f:
        seeds_full_string = f.readline()
        _, seeds_string = seeds_full_string.split(":")
        seeds_pairs = [int(s) for s in seeds_string.split()]
        seeds_iter = seeds_pairs.__iter__()
        seeds_pairs = [
            (min_, min_ + range_) for min_, range_ in zip(seeds_iter, seeds_iter)
        ]

        rest = f.read()
        maps = [
            [[int(n) for n in line.split()] for line in block.split("\n")[1:]]
            for block in rest.strip().split("\n\n")
        ]

    land = 0
    while True:
        candidate = land
        for map_ in maps[::-1]:
            candidate = apply_reverse_map(candidate, map_)
        for min_, max_ in seeds_pairs:
            if min_ <= candidate < max_:
                return land
        land += 1


def apply_reverse_map(s, map_):
    """
    apply a map_ to the element passed.
    s: from seed, but actually is the source category
    """
    for dest_start, source_start, length in map_:
        if dest_start <= s < dest_start + length:
            return source_start - dest_start + s
    return s


if __name__ == "__main__":
    rta = main("inputs/05.txt")
    print(rta)
