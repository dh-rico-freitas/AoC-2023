# 01-2.py
""" Advent Of Code - Day 1 Puzzle 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

from collections import defaultdict

PUZZLE = "01-2"
INPUTS_PATH = "inputs/01-1.txt"


def main():
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
            return target == string[:len(target)]
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


if __name__ == "__main__":
    main()
