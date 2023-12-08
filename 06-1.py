# 06-1.py
""" Advent Of Code - Day 6 Puzzle 1

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""
from functools import reduce
from math import sqrt

PUZZLE = "06-1"
INPUT_PATH = "inputs/06.txt"


def main(games_file=INPUT_PATH):
    with open(games_file) as f:
        times = (int(i) for i in f.readline().split(":")[1].split())
        distances = (int(i) for i in f.readline().split(":")[1].split())
    ways = []
    for t, d in zip(times, distances):
        accum = 0
        print(t, d, accum)
        for x in range(1, t):
            print(x, x * (t - x), x * (t - x) > d)
            if x * (t - x) > d:
                accum += 1
        ways.append(accum)
    print(ways)
    print(reduce(lambda x, y: x * y, ways))


if __name__ == "__main__":
    main()
