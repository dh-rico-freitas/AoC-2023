# 02-1.py
""" Advent Of Code - Day 2 Puzzle 1

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

PUZZLE = "02-1"
INPUT_PATH = "inputs/02-1.txt"


def main(games_file, bag):
    with open(games_file) as f:
        data = (parse(game) for game in f if game.strip())
        print(sum(id for id, sets_dicts in data if validate(sets_dicts, bag)))


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


if __name__ == "__main__":
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    main(INPUT_PATH, bag)
