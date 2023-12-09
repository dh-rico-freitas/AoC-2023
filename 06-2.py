# 06-2.py
""" Advent Of Code - Day 6 Puzzle 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""
from functools import reduce
from math import sqrt
from time import perf_counter

PUZZLE = "06-2"
INPUT_PATH = "inputs/06.txt"


def version_5(times, distances):
    ways = []
    for t, d in zip(times, distances):
        min_x = round(
            binary_search(
                1,
                t,
                d,
                lambda x: distance(x, t),
            )
        )
        ways.append(t - min_x * 2 + 1)
    return reduce(lambda x, y: x * y, ways)


def version_6(times, distances):
    ways = []
    for t, d in zip(times, distances):
        min_x = round(
            custom_search(
                t,
                d,
            )
        )
        ways.append(t - min_x * 2 + 1)
    return reduce(lambda x, y: x * y, ways)


def binary_search(min_x, max_x, target, function, tol=0.5):
    def f(min_x, max_x, i):
        candidate = (min_x + max_x) / 2
        if (max_x - min_x) < tol:
            print(i)
            return candidate
        result = function(candidate)
        if result > target:
            return f(min_x, candidate, i + 1)
        else:
            return f(candidate, max_x, i + 1)

    return f(min_x, max_x, 1)


def custom_search(time, distance, tol=0.5):
    def f(min_x, max_x):
        candidate = (min_x + max_x) / 2
        if (max_x - min_x) < tol:
            return candidate
        result = candidate * (time - candidate)
        if result > distance:
            return f(min_x, candidate)
        else:
            return f(candidate, max_x)

    return f(1, time)


def distance(time, total_time):
    return time * (total_time - time)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        times = [int("".join(f.readline().split(":")[1].split()))]
        distances = [int("".join(f.readline().split(":")[1].split()))]

    start_time = perf_counter()
    rta_5 = version_5(times, distances)
    end_time = perf_counter()
    print(f"Version 5 run in {end_time - start_time}s: {rta_5}")

    start_time = perf_counter()
    rta_6 = version_6(times, distances)
    end_time = perf_counter()
    print(f"Version 6 run in {end_time - start_time}s: {rta_6}")
