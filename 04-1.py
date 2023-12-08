# 04-1.py
""" Advent Of Code - Day 4 Puzzle 1

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

PUZZLE = "04-1"
INPUT_PATH = "inputs/04.txt"


def main(games_file):
    with open(games_file) as f:
        total = 0
        for game in f:
            card_s, number_s = game.split(":")
            winning_s, my_s = number_s.split("|")
            winning_n = set(int(i) for i in winning_s.split())
            my_n = set(int(i) for i in my_s.split())
            matches = winning_n.intersection(my_n)
            n_matches = len(matches)
            points = 0
            if n_matches:
                points = 2 ** (n_matches - 1)
            print(f"{card_s}: {points}")
            total += points
    print(total)


if __name__ == "__main__":
    main(INPUT_PATH)
