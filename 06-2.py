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


def version_1(times, distances):
    ways = []
    for t, d in zip(times, distances):
        accum = 0
        for x in range(1, t):
            if x * (t - x) > d:
                accum += 1
        ways.append(accum)
    return reduce(lambda x, y: x * y, ways)


def version_2(times, distances):
    ways = []
    for t, d in zip(times, distances):
        # t/2 is a symmetry point of x, only need to do half of it.
        for x in range(1, (t + 1) // 2):
            if x * (t - x) > d:
                break
        ways.append(t + 1 - 2 * x)
    return reduce(lambda x, y: x * y, ways)


def version_3(times, distances):
    ways = []
    for t, d in zip(times, distances):
        min_x = round(general_binary_search(1, t, d, lambda x: distance(x, t)))
        ways.append(t - min_x * 2 + 1)
    return reduce(lambda x, y: x * y, ways)


def version_4(times, distances):
    ways = []
    for t, d in zip(times, distances):
        min_x = round(
            general_binary_search(
                1,
                t,
                d,
                lambda x: distance(x, t),
                new_candidate=lambda x, y: ((x + y) / 2 + sqrt(x * y)) / 2,
            )
        )
        ways.append(t - min_x * 2 + 1)
    return reduce(lambda x, y: x * y, ways)


def general_binary_search(
    min_x, max_x, target, function, new_candidate=lambda x, y: (x + y) / 2, tol=0.25
):
    min_err = abs(function(min_x) - target)
    max_err = abs(function(max_x) - target)

    def f(min_x, min_err, max_x, max_err):
        candidate = new_candidate(min_x, max_x)
        result = function(candidate)
        if (candidate_error := abs(target - result)) < tol:
            return candidate
        elif result > target:
            return f(min_x, min_err, candidate, candidate_error)
        else:
            return f(candidate, candidate_error, max_x, max_err)

    return f(min_x, min_err, max_x, max_err)


def distance(time, total_time):
    return time * (total_time - time)


if __name__ == "__main__":
    with open(INPUT_PATH) as f:
        times = [int("".join(f.readline().split(":")[1].split()))]
        distances = [int("".join(f.readline().split(":")[1].split()))]

    start_time = perf_counter()
    rta_1 = version_1(times, distances)
    end_time = perf_counter()
    print(f"Version 1 run in {end_time - start_time}s: {rta_1}")

    start_time = perf_counter()
    rta_2 = version_2(times, distances)
    end_time = perf_counter()
    print(f"Version 2 run in {end_time - start_time}s: {rta_2}")

    start_time = perf_counter()
    rta_3 = version_3(times, distances)
    end_time = perf_counter()
    print(f"Version 3 run in {end_time - start_time}s: {rta_3}")

    start_time = perf_counter()
    rta_4 = version_4(times, distances)
    end_time = perf_counter()
    print(f"Version 4 run in {end_time - start_time}s: {rta_4}")
