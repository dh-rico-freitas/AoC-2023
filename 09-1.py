# 09-1.py
""" Advent Of Code - Day 9 Puzzle 1

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

PUZZLE = "09-1"
INPUT_PATH = "inputs/09.txt"


def propagate(serie):
    prediction = serie[-1]
    differences = [s - f for f, s in zip(serie, serie[1:])]
    if any(differences):
        prediction += propagate(differences)
    return prediction


with open(INPUT_PATH) as f:
    numbers = [[int(i) for i in line.split()] for line in f]
    print(sum(map(propagate, numbers)))
