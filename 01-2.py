# 01-2.py
""" Advent Of Code - Day 1 Puzzle 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

from argparse import ArgumentParser
from collections import defaultdict

PUZZLE = "01-2"
INPUTS_PATH = "inputs/01-1.txt"


def main(get_number):
    with open(INPUTS_PATH) as f:
        numbers = (get_number(l) for l in f)
        print(sum(numbers))


NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

SREBMUN = {key[::-1]: value for key, value in NUMBERS.items()}


def generate_token_table(tokens):
    def create_test(target):
        def f(string):
            return target == string[: len(target)]

        return f

    def process_test_list(l):
        def f(s):
            for test, result in l:
                if test(s):
                    return result
            return None

        return f

    table = defaultdict(list)

    for key, value in tokens.items():
        table[key[0]].append((create_test(key), value))

    return {key: process_test_list(value) for key, value in table.items()}


NUMBERS_TEST = generate_token_table(NUMBERS)
SREBMUN_TEST = generate_token_table(SREBMUN)


def get_number(string):
    for i, char in enumerate(string):
        if (
            char in NUMBERS_TEST
            and (first := NUMBERS_TEST[char](string[i:])) is not None
        ):
            break
    else:
        raise ValueError("Didn't find any number")

    reversed_string = string[::-1]
    for i, char in enumerate(reversed_string):
        if (
            char in SREBMUN_TEST
            and (last := SREBMUN_TEST[char](reversed_string[i:])) is not None
        ):
            break
    else:
        raise ValueError(f"Didn't find any number in reverse direction. {string=}")

    return first * 10 + last


def linear_search(string, reference):
    for i in range(len(string)):
        substring = string[i:]
        for key, value in reference.items():
            if substring.startswith(key):
                return value
    else:
        raise ValueError("Didn't find any number")


def get_number_simple(string):
    first = linear_search(string, NUMBERS)
    last = linear_search(string[::-1], SREBMUN)
    return first * 10 + last


if __name__ == "__main__":
    import argparse
    import time

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--timed", action="store_true")
    parser.add_argument("-s", "--simple", action="store_true")
    args = parser.parse_args()

    if args.timed:
        start_time = time.perf_counter()

    processor = get_number
    if args.simple:
        processor = get_number_simple

    main(processor)

    if args.timed:
        end_time = time.perf_counter()
        print(f"Execution time= {(end_time - start_time) * 1000} ms")
