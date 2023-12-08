# 040.py
""" Advent Of Code - Day 4 Puzzle 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

PUZZLE = "04-2"
INPUT_PATH = "inputs/04.txt"


def main(games_file):
    with open(games_file) as f:
        N = []
        for game in f:
            _, number_s = game.split(":")
            winning_s, my_s = number_s.split("|")
            winning_n = set(int(i) for i in winning_s.split())
            my_n = set(int(i) for i in my_s.split())
            matches = winning_n.intersection(my_n)
            n_matches = len(matches)
            N.append(n_matches)

    C = [1 for _ in N]

    length = len(N)

    for i, n in enumerate(N):
        for j in range(i + 1, min(length, n + i + 1)):
            C[j] += C[i]

    for c, n in zip(C, N):
        print(f"{c}: {n}")

    print(sum(C))


if __name__ == "__main__":
    main(INPUT_PATH)
