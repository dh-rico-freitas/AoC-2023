# 02-2.py
""" Advent Of Code - Day 2 Puzzle 2

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""
import functools

PUZZLE = "02-2"
INPUT_PATH = "inputs/02.txt"


def main(games_file):
    with open(games_file) as f:
        data = (parse(game) for game in f if game.strip())
        print(sum(power(sets_dicts) for _, sets_dicts in data))


def parse(game):
    """
    sets and set refers to the game "set", NOT the python object.
    """
    game = game.strip()
    game_string, sets_string = game.split(":")
    game_ID = int(game_string[4:])

    sets_strings = sets_string.split(";")
    sets_lists_ball_strings = (balls.split(",") for balls in sets_strings)
    sets_lists_ball_lists = (
        (ball_string.split() for ball_string in set_)
        for set_ in sets_lists_ball_strings
    )
    sets_dicts = (
        dict((color, int(number)) for number, color in set_)
        for set_ in sets_lists_ball_lists
    )
    return game_ID, sets_dicts


def validate(sets_dict, bag):
    for set_ in sets_dict:
        for color, amount in set_.items():
            if amount > bag[color]:
                return False
    return True

def power(game_results):
    maxes = {"red": 0, "green": 0, "blue": 0}
    for set_ in game_results:
        for color, number in set_.items():
            maxes[color] = max(maxes[color], number)
    return functools.reduce(lambda x, y: x * y,  maxes.values())
    


if __name__ == "__main__":
    main(INPUT_PATH, bag)
