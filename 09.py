# 09.py
""" Advent Of Code - Day 9 Puzzles 1 & 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

PUZZLE = "09-1&2"
INPUT_PATH = "inputs/09.txt"

from time import perf_counter


def propagate(serie):
    prediction = serie[-1]
    differences = [s - f for f, s in zip(serie, serie[1:])]
    if any(differences):
        prediction += propagate(differences)
    return prediction


def propagate_while(serie):
    prediction = serie[-1]
    diff = serie[:]
    while any(diff := [s - f for f, s in zip(diff, diff[1:])]):
        prediction += serie[-1]
    return prediction


with open(INPUT_PATH) as f:
    numbers = [[int(i) for i in line.split()] for line in f]

start_time = perf_counter()
print("Puzzle 1:", sum(propagate(n) for n in numbers))
end_time = perf_counter()
print(f"Solved in {end_time - start_time} s")

start_time = perf_counter()
print("Puzzle 2:", sum(propagate(n[::-1]) for n in numbers))
end_time = perf_counter()
print(f"Solved in {end_time - start_time} s")

print()

start_time = perf_counter()
print("Puzzle 1:", sum(propagate_while(n) for n in numbers))
end_time = perf_counter()
print(f"Solved in {end_time - start_time} s")

start_time = perf_counter()
print("Puzzle 2:", sum(propagate_while(n[::-1]) for n in numbers))
end_time = perf_counter()
print(f"Solved in {end_time - start_time} s")
