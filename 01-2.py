# 01-2.py
""" Advent Of Code - Day 1 Puzzle 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

from collections import defaultdict

PUZZLE = "01-2"
INPUTS_PATH = "inputs/01.txt"


def main(processor):
    with open(INPUTS_PATH) as f:
        numbers = (processor.get_number(l) for l in f)
        print(sum(numbers))


class SubsSearcher:
    def __init__(self, tokens_dict):
        self.forward_dict = tokens_dict
        self.backward_dict = {k[::-1]: v for k, v in tokens_dict.items()}

    def get_number(self, string):
        first = self._search_f(string)
        last = self._search_b(string)
        return first * 10 + last

    def _search_f(self, string):
        return self._search(string, self.forward_dict)

    def _search_b(self, string):
        return self._search(string[::-1], self.backward_dict)

    def _search(self, string, reference):
        for i in range(len(string)):
            substring = string[i:]
            for key, value in reference.items():
                if substring.startswith(key):
                    return value
        else:
            raise ValueError("Didn't find any number")


class FastSubsSearcher(SubsSearcher):
    def __init__(self, tokens_dict):
        super().__init__(tokens_dict)
        self.forward_processors = self._generate_table(self.forward_dict)
        self.backward_processors = self._generate_table(self.backward_dict)

    def _generate_table(self, tokens):
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

    def _search_f(self, string):
        return self._search(string, self.forward_processors)

    def _search_b(self, string):
        return self._search(string[::-1], self.backward_processors)

    def _search(self, string, reference):
        for i, char in enumerate(string):
            if char in reference and (value := reference[char](string[i:])) is not None:
                return value
        else:
            raise ValueError("Didn't find any number")


if __name__ == "__main__":
    import argparse
    import time

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

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--timed", action="store_true")
    parser.add_argument("-f", "--fast", action="store_true")
    args = parser.parse_args()

    if args.timed:
        start_time = time.perf_counter()

    processor = SubsSearcher(NUMBERS)
    if args.fast:
        processor = FastSubsSearcher(NUMBERS)

    main(processor)

    if args.timed:
        end_time = time.perf_counter()
        print(f"Execution time= {(end_time - start_time) * 1000} ms")
