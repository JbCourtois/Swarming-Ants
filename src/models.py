from dataclasses import dataclass
import random


DIRECTIONS = {
    'W': (-1, 0),
    'E': (1, 0),
    'N': (0, -1,),
    'S': (0, 1),
}


class RobotCommandError(ValueError):
    """Exception used when a robot receives an invalid command."""


class Game:
    RANGE_NB_ROBOTS = (10, 30)
    RANGE_TARGET_HP = (500, 10000)
    RANGE_GRID_H = (30, 300)
    MAX_GRID_X = 700

    ROBOT_COM_RANGE = 5
    ROBOT_FIRE_RANGE = 10

    def __init__(self):
        self.grid_h = random.randint(*self.RANGE_GRID_H)
        self.grid_w = random.randint(self.grid_h, self.MAX_GRID_X)

        self._generate_classes()

        self.target_pos = self.Position(
            x=random.randrange(self.grid_w),
            y=random.randrange(self.grid_h),
        )
        self.target_hp = random.randint(*self.RANGE_TARGET_HP)

        # Dispatch robots

    def _generate_classes(game):
        @dataclass
        class Position:
            x: int
            y: int

            def move(self, shift_x, shift_y):
                self.x = (self.x + shift_x) % game.grid_w
                self.y = (self.y + shift_y) % game.grid_h

            def distance(self, other):
                """Compute the Manhattan distance between two points.

                Recall that the grid is cyclic."""
                diff_x = self.x - other.x
                diff_x = min(diff_x % game.grid_w, -diff_x % game.grid_w)

                diff_y = self.y - other.y
                diff_y = min(diff_y % game.grid_h, -diff_y % game.grid_h)

                return diff_x + diff_y

        @dataclass
        class Robot:
            id: int
            position: Position
            order: str
            messages: dict

            def __hash__(self):
                return hash(self.id)

            def reset(self):
                self.order = None
                self.messages = {}

            def hold(self):
                """Do nothing. This is the default order."""

            def move(self, direction):
                if (shift := DIRECTIONS.get(direction)) is None:
                    raise RobotCommandError('Invalid direction')
                self.position.move(*shift)

            def fire(self, target):
                if game.target_pos != target:
                    return

            def message(self, message):
                """Send a message.

                At the start of the next turn,
                all other robots in communication range
                will receive that message.
                """

        game.Robot = Robot
        game.Position = Position
