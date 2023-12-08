# 06-2.py
""" Advent Of Code - Day 6 Puzzle 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""
from functools import reduce
from math import sqrt

PUZZLE = "06-2"
INPUT_PATH = "inputs/06.txt"


def main(games_file=INPUT_PATH):
    with open(games_file) as f:
        times = [int("".join(f.readline().split(":")[1].split()))]
        distances = [int("".join(f.readline().split(":")[1].split()))]
    ways = []
    for t, d in zip(times, distances):
        accum = 0
        for x in range(1, t):
            if x * (t - x) > d:
                accum += 1
        ways.append(accum)
    print(reduce(lambda x, y: x * y, ways))


if __name__ == "__main__":
    main()
