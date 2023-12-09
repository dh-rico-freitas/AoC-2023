# 07-2.py
""" Advent Of Code - Day 7 Puzzle 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""
from collections import Counter

PUZZLE = "07-2"
INPUT_PATH = "inputs/07.txt"

CARDS = list("J23456789TQKA")
GAMES = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]


def key(x):
    exp = max(len(i) for i in (CARDS, GAMES))
    count = Counter(x[0])
    j = 0
    if "J" in count:
        j = count.pop("J")
    if count:
        card, _ = count.most_common(1).pop()
    else:
        card = "J"
    count[card] += j

    base_points = [GAMES.index(sorted(count.values()))] + [CARDS.index(i) for i in x[0]]
    accum = 0
    for i, point in enumerate(base_points[::-1]):
        accum += point * exp**i
    return accum


with open(INPUT_PATH) as f:
    data = (line.split() for line in f)
    data = sorted([(hand, int(bid)) for hand, bid in data], key=key)

print(sum(i * d[1] for i, d in enumerate(data, start=1)))
