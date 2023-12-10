# 10-1.py
""" Advent Of Code - Day 10 Puzzle 1

Author: Daniel Hernán Rico Freitas
github: https://github.com/dh-rico-freitas
"""

from enum import Enum
from time import perf_counter

PUZZLE = "10-1"
INPUT_PATH = "inputs/10.txt"


class Coord(tuple):
    """
    Coordinates in screen position.
    (y, x) with x from left to right and y from top to bottom.
    """

    def __new__(cls, y, x):
        return super(Coord, cls).__new__(cls, (y, x))

    @property
    def x(self):
        return self[1]

    @property
    def y(self):
        return self[0]

    def __add__(self, other):
        if isinstance(other, Direction):
            other = other.value
        return self.__class__(self.y + other.y, self.x + other.x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return super().__hash__()


class Direction(Enum):
    NORTH = Coord(-1, 0)
    EAST = Coord(0, 1)
    SOUTH = Coord(1, 0)
    WEST = Coord(0, -1)


class Maze:
    desp_table = {
        Direction.NORTH: {
            "7": Direction.WEST,
            "S": Direction.NORTH,
            "|": Direction.NORTH,
            "F": Direction.EAST,
        },
        Direction.EAST: {
            "J": Direction.NORTH,
            "S": Direction.EAST,
            "-": Direction.EAST,
            "7": Direction.SOUTH,
        },
        Direction.SOUTH: {
            "L": Direction.EAST,
            "S": Direction.SOUTH,
            "|": Direction.SOUTH,
            "J": Direction.WEST,
        },
        Direction.WEST: {
            "F": Direction.SOUTH,
            "S": Direction.WEST,
            "-": Direction.WEST,
            "L": Direction.NORTH,
        },
    }

    def __init__(self, maze_string):
        self.maze = maze_string.split("\n")

    @classmethod
    def from_file(cls, file):
        with open(file) as f:
            return Maze(f.read())

    def __getitem__(self, coord):
        return self.maze[coord.y][coord.x]

    def __str__(self):
        return "\n".join(self.maze)

    def calc_move(self, coord, direction):
        new_direction = self.desp_table[direction][self[coord]]
        return coord + new_direction, new_direction

    def find_start(self):
        for i, line in enumerate(self.maze):
            if (j := line.find("S")) != -1:
                return Coord(i, j)
        else:
            raise ValueError("Maze doesn't have starting possition [S]")

    def create_walkers(self):
        start = self.find_start()
        walkers = [
            Walker(self, start, d)
            for d in Direction
            if self[start + d] in self.desp_table[d]
        ]
        return walkers


class Walker:
    def __init__(self, maze, position, direction):
        self.maze = maze
        self.position = position
        self.direction = direction

    def walk(self):
        self.position, self.direction = self.maze.calc_move(
            self.position, self.direction
        )

    def __str__(self):
        return f"Walker at {self.position=}, goin {self.direction=}"

    def __eq__(self, other):
        return self.position == other.position

    def __iter__(self):
        return WalkerIterator(self.maze, self.position, self.direction)


class WalkerIterator(Walker):
    def __init__(self, *args):
        super().__init__(*args)
        self.first = True

    __iter__ = None

    def __next__(self):
        if self.first:
            self.first = False
        else:
            self.walk()
        return self.position

    def __str__(self):
        return f"Walker iterator at {self.position=}, goin {self.direction=}"


maze = Maze.from_file(INPUT_PATH)
start = maze.find_start()
w1, w2 = maze.create_walkers()
for i, (pos_1, pos_2) in enumerate(zip(w1, w2)):
    if pos_1 == pos_2 and pos_1 != start:
        break
print(i)
