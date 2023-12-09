# 08-2.py
""" Advent Of Code - Day 8 Puzzle 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""
from itertools import cycle
from math import lcm
import re

PUZZLE = "08-2"
INPUT_PATH = "inputs/08.txt"


parser = re.compile(r"\b[A-Z][A-Z][A-Z]\b")
with open(INPUT_PATH) as f:
    directions = [0 if i == "L" else 1 for i in f.readline().strip()]
    f.readline()
    triplets = (parser.findall(line) for line in f)
    map = {s: (l, r) for s, l, r in triplets}

    starts = [pos for pos in map.keys() if pos[-1] == "A"]

    cycle_lengths = [0 for _ in starts]
    for i, start in enumerate(starts):
        position = start
        for direction in cycle(directions):
            position = map[position][direction]
            cycle_lengths[i] += 1
            if position[-1] == "Z":
                break

    print(lcm(*cycle_lengths))
