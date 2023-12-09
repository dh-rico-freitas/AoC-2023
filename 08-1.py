# 08-1.py
""" Advent Of Code - Day 8 Puzzle 1

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""
from itertools import cycle
import re

PUZZLE = "08-1"
INPUT_PATH = "inputs/08.txt"


parser = re.compile(r"\b[A-Z][A-Z][A-Z]\b")
with open(INPUT_PATH) as f:
    directions = cycle(0 if i == "L" else 1 for i in f.readline().strip())
    f.readline()
    triplets = (parser.findall(line) for line in f)
    map = {s: (l, r) for s, l, r in triplets}

    START = "AAA"
    END = "ZZZ"

    steps = 0
    position = START
    for direction in directions:
        position = map[position][direction]
        steps += 1
        if position == END:
            break

    print(steps)
